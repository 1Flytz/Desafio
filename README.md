
# Validador de Acesso

Sistema que verifica se um usuário tem permissão para acessar determinadas áreas com base no JSON.

## Como funciona
- O programa lê as permissões do arquivo `permissoes.json`
- Pede o nome do usuário e a área que deseja acessar
- Verifica se o acesso é permitido ou não

## Estrutura
- `Main.py`: Programa principal
- `src/`: Código fonte do validador
- `banco_dados_permissoes/`: Arquivo com as permissões

## Como usar
1. Execute o arquivo `Main.py`
2. Digite seu nome
3. Digite a área que deseja acessar
