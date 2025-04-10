<<<<<<< HEAD
# Validador de Acesso

Um programa simples em Python que valida o acesso de usuários a diferentes áreas com base em um arquivo JSON de permissões.

## Funcionalidades

- Carrega permissões de usuários de um arquivo JSON
- Valida o acesso de usuários a áreas específicas
- Interface de linha de comando amigável
- Tratamento de erros para arquivo não encontrado ou formato inválido

## Estrutura do Projeto

- `Main.py`: Arquivo principal com a implementação do validador
- `permissoes.json`: Arquivo de configuração com as permissões dos usuários

## Como Usar

1. Certifique-se de ter Python 3.6+ instalado
2. Execute o programa:
   ```bash
   python Main.py
   ```
3. Digite seu nome e a área que deseja acessar quando solicitado

## Exemplo de Uso

```
=== Sistema de Validação de Acesso ===
Digite seu nome: Alice
Digite a área que deseja acessar: sala de reunião
✅ Acesso permitido!
```

## Estrutura do JSON

O arquivo `permissoes.json` deve seguir o seguinte formato:

```json
{
    "usuarios": [
        {"nome": "Usuario1", "acessos": ["area1", "area2"]},
        {"nome": "Usuario2", "acessos": ["area1"]}
    ]
}
``` 
=======
# Desafio
>>>>>>> b6fa42ba36244a4109492d1c592d2e9b6838be9f
