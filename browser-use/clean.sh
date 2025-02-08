#!/bin/bash

# Lista de diretórios para limpar/criar
DIRS="conversations execucoes logs recordings results"

# Cores para output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

# Função para limpar/criar um diretório
clean_directory() {
    if [ -d "$1" ]; then
        echo -e "${GREEN}Limpando diretório: $1${NC}"
        
        # Remove conteúdo preservando .gitkeep
        find "$1" -type f ! -name '.gitkeep' -delete 2>/dev/null
        find "$1" -mindepth 1 -type d -delete 2>/dev/null
    else
        echo -e "${YELLOW}Criando novo diretório: $1${NC}"
        mkdir -p "$1"
    fi

    # Verifica e cria .gitkeep se não existir
    if [ ! -f "$1/.gitkeep" ]; then
        touch "$1/.gitkeep"
        echo -e "${YELLOW}Arquivo .gitkeep criado em: $1${NC}"
    fi
}

echo "Iniciando processo de limpeza e criação de diretórios..."

# Processa cada diretório da lista
for dir in $DIRS; do
    clean_directory "$dir"
done

echo -e "${GREEN}Processo finalizado com sucesso!${NC}"