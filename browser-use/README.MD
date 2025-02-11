# Projeto: Browser Use Tests com Agentes IA

## 📋 Descrição

Este projeto demonstra o uso de agentes de IA para automatizar testes e interações com navegadores web. Os agentes são capazes de realizar tarefas complexas como busca de preços, preenchimento de formulários e navegação em sites.

## 🎯 Objetivo

Demonstrar diferentes cenários de uso de agentes de IA manipulando browsers para:

- Busca automatizada de preços em farmácias
- Comparação de preços entre diferentes estabelecimentos
- Automação de testes em interfaces web
- Interação com formulários e validações

## 🛠️ Tecnologias

### Principais

- Python 3.9+
- LangChain
- OpenAI GPT-4
- Ollama (modelo deepseek-r1)
- Browser-Use (biblioteca para automação de browser)

### Dependências

```bash
pip install -r requirements.txt
```

```markdown
langchain
langchain-openai
langchain-ollama
python-dotenv
browser-use
```

git clone <repository-url>
cd agentes-ia-testes

cp .env.example .env

OPENAI_API_KEY=sua_chave_api

## 📁 Estrutura do Projeto
```
.
├── README.md
├── browser-use/
│   ├── find_best_price.py      # Exemplo de busca de preços
│   └── clean.sh                # Script para limpeza de diretórios
├── conversations/              # Armazena histórico de conversas
├── execucoes/                 # Armazena GIFs das execuções
├── logs/                      # Logs de execução
├── recordings/                # Gravações das sessões
└── results/                   # Resultados das buscas
```

💡 Funcionalidades
Busca de Preços: Automatiza a busca de medicamentos em diferentes farmácias
Comparação de Preços: Analisa e compara preços entre estabelecimentos
Geração de Relatórios: Cria relatórios detalhados das buscas realizadas
Gravação de Execuções: Salva GIFs das execuções para análise posterior

🔧 Uso
Para executar a busca de preços:

python browser-use/find_best_price.py

./clean.sh

📝 Exemplos

# Exemplo de execução de busca

await run_task("""
    Acessar os sites das farmácias e buscar o preço do Xifaxan 550mg 28 comprimidos.
    Lista de farmácias: Drogasil, Drogaria São Paulo, Pague Menos...
""", "busca_medicamento")

🤝 Contribuindo

Fork o projeto
Crie sua Feature Branch (git checkout -b feature/AmazingFeature)
Commit suas mudanças (git commit -m 'Add some AmazingFeature')
Push para a Branch (git push origin feature/AmazingFeature)
Abra um Pull Request
**
