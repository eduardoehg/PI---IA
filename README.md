**# Detector de Phishing com spaCy e Expressões Regulares**

Este é um simples detector de phishing desenvolvido em Python utilizando a biblioteca spaCy para processamento de linguagem natural (NLP) e expressões regulares. Ele verifica e-mails em busca de sinais comuns de tentativas de phishing, como a presença de entidades nomeadas do tipo "EMAIL" e palavras-chave associadas a phishing.

### Como Funciona

O detector de phishing analisa o conteúdo do e-mail fornecido e realiza duas verificações principais:

1. **Verificação de Entidades Nomeadas:**
   - Utiliza o spaCy para identificar entidades nomeadas no texto, procurando por aquelas classificadas como "EMAIL". Isso pode ajudar a identificar endereços de e-mail falsos ou suspeitos.

2. **Verificação de Palavras-Chave:**
   - Utiliza expressões regulares para identificar palavras-chave comuns associadas a tentativas de phishing, como "senha", "urgente", "clique aqui" e "confirme sua identidade".

### Como Usar

1. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   ```

2. Navegue até o diretório do projeto:
   ```bash
   cd seu-repositorio
   ```

3. Execute o script Python:
   ```bash
   python nome-do-script.py
   ```
   O script solicitará que você cole o conteúdo do e-mail para verificação.

### Configuração

- Você pode personalizar a lista de palavras-chave no código-fonte para se adequar às suas necessidades específicas.

### Requisitos

- Python 3.x
- Bibliotecas Python: spacy

### Licença

Este projeto é licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.
