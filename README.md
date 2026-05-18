# Anime Report 📊

Ferramenta em Python que coleta, organiza e envia automaticamente um relatório dos animes em exibição na temporada atual.

## Funcionalidades
- Busca todos os animes de TV em exibição pela Jikan API
- Percorre todas as páginas disponíveis automaticamente
- Exporta os dados para uma planilha Excel formatada
- Envia o relatório por email automaticamente
- Registra todas as etapas em um arquivo de log

## Tecnologias
- Python 3.14
- [Jikan API](https://docs.api.jikan.moe/) — API não oficial do MyAnimeList
- openpyxl — geração e formatação do Excel
- smtplib — envio de email

## Instalação

1. Clone o repositório
```bash
git clone https://github.com/vitor-emanueldev/anime-report.git
```

2. Instale as dependências
```bash
pip install requests openpyxl
```

3. Configure seu email e senha de app em `email_sender.py`

## Como usar
```bash
python main.py
```

## Resultado
- `animes.xlsx` — planilha formatada com título, nota, episódios, status, gêneros e sinopse
- `anime_report.log` — arquivo de log da execução