
# 🎬 SerieFixer

<p align="center">
  <img src="assets/seriefixer-logo.png" alt="SerieFixer Logo" width="200"/>
</p>

**SerieFixer** é uma ferramenta em Python que renomeia arquivos de vídeo de episódios de séries e atualiza seus metadados (título, título original, gênero, etc).  
Ideal para organizar suas séries com nomes corretos e limpos, direto no terminal.

---

## 🚀 Funcionalidades

- Renomeia os arquivos de vídeo com base no nome da série, temporada e título do episódio.
- Atualiza metadados dos vídeos (title, original_title, genre).
- Suporte a `.mp4`, `.mkv`, `.avi`
- Integração com a [API pública do TVMaze](https://www.tvmaze.com/api) para buscar os episódios.

---

## 💻 Pré-requisitos

- Python 3.8+
- [FFmpeg](https://ffmpeg.org/) instalado e acessível via terminal

### ✅ Como instalar o FFmpeg

1. Baixe o FFmpeg para Windows: https://www.gyan.dev/ffmpeg/builds/
2. Extraia o arquivo `.zip`
3. Adicione a pasta `bin` do FFmpeg no **Path** das Variáveis de Ambiente:
   - Ex: `C:\ffmpeg\bin`

Para verificar se deu certo, abra o terminal e digite:

```bash
ffmpeg -version
```

---

## 📦 Instalação

```bash
git clone https://github.com/seu-usuario/SerieFixer.git
cd SerieFixer
pip install requests
```

---

## ⚙️ Como usar

Navegue até a pasta onde estão os vídeos da série e execute:

```bash
python seriefixer.py -n "Nome da Série" -s "Número da Temporada"
```

### 🔁 Exemplo:

```bash
python seriefixer.py -n "Stranger Things" -s 1
```

Os arquivos serão renomeados como:

```
Stranger Things S01E01 - E01 - Chapter One: The Vanishing of Will Byers.mkv
Stranger Things S01E02 - E02 - The Weirdo on Maple Street.mkv
...
```

---

## 📸 Exemplo visual

> Interface não-gráfica (CLI), mas os arquivos renomeados ficam assim:

```
📁 Pasta:
├── Stranger Things S01E01 - E01 - Chapter One: The Vanishing of Will Byers.mkv
├── Stranger Things S01E02 - E02 - The Weirdo on Maple Street.mkv
├── ...
```

---

## 📃 Licença

MIT © [Saulo Godoy Proetti](https://github.com/saulogp)

---

## ✨ Créditos

- [TVMaze API](https://www.tvmaze.com/api)
- Logo criada com IA by [ChatGPT + DALL·E](https://openai.com/)
