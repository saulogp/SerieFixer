import argparse
import requests
import subprocess
import os
import re

# ========== API ==========

def buscar_serie(nome_serie):
    url = f"https://api.tvmaze.com/singlesearch/shows?q={nome_serie}"
    resposta = requests.get(url)
    if resposta.ok:
        return resposta.json()
    print("❌ Série não encontrada.")
    return None

def buscar_episodios_por_temporada(show_id, temporada):
    url = f"https://api.tvmaze.com/shows/{show_id}/episodes"
    resposta = requests.get(url)
    if resposta.ok:
        todos_episodios = resposta.json()
        temporada = int(temporada)
        return [ep for ep in todos_episodios if ep.get("season") == temporada]
    print("❌ Episódios não encontrados.")
    return []

# ========== UTILS ==========

def limpar_nome_arquivo(nome):
    return re.sub(r'[\\/*?:"<>|]', '', nome)

def formatar_generos(generos):
    return ", ".join(generos)

def extrair_episodios(lista_episodios):
    return [f"E{ep['number']:02} - {ep['name']}" for ep in lista_episodios]

# ========== CORE ==========

def update_metadata(caminho_arquivo, titulo, season_episode, generos):
    temp_file = f"temp_{caminho_arquivo}"
    comentario = "Edited by SerieFixer"

    comando = [
        'ffmpeg', '-i', caminho_arquivo,
        '-metadata', f'title={season_episode}',
        '-metadata', f'original_title={titulo.title()}',
        '-metadata', f'comment={comentario}',
        '-metadata', f'genre={generos}',
        '-codec', 'copy',
        temp_file
    ]

    subprocess.run(comando, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    os.replace(temp_file, caminho_arquivo)
    print(f"✅ Metadados atualizados: {caminho_arquivo}")

def rename_files(serie, temporada, generos, episodios):
    arquivos = sorted(f for f in os.listdir('.') if f.lower().endswith(('.mp4', '.mkv', '.avi')))

    for idx, arquivo in enumerate(arquivos, start=1):
        ext = os.path.splitext(arquivo)[1]
        nome_ep = limpar_nome_arquivo(episodios[idx - 1])
        novo_nome = f"{serie.title()} S{temporada.zfill(2)}E{str(idx).zfill(2)} - {nome_ep}{ext}"

        os.rename(arquivo, novo_nome)
        print(f"🔁 Renomeado: {arquivo} -> {novo_nome}")

        update_metadata(novo_nome, serie, nome_ep, generos)

# ========== MAIN ==========

def main():
    parser = argparse.ArgumentParser(description='Renomeia arquivos de série e altera metadados.\n Mantenha no diretório apenas os episódios de uma temporada e os arquivos ordenados.\n Formatos conhecidos [.mp4, .mkv e .avi]')
    parser.add_argument('-n', '--name', required=True, help='Nome da série')
    parser.add_argument('-s', '--season', required=True, help='Número da temporada')

    args = parser.parse_args()
    nome_serie = args.name.strip().lower()
    temporada = args.season.strip()

    serie = buscar_serie(nome_serie)
    if not serie:
        return

    generos = formatar_generos(serie.get('genres', []))
    lista_episodios = buscar_episodios_por_temporada(serie['id'], int(temporada))
    episodios = extrair_episodios(lista_episodios)

    rename_files(nome_serie, temporada, generos, episodios)

if __name__ == "__main__":
    main()
