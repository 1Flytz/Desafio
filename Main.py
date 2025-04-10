from src.validacao.validador_acesso import ValidadorAcesso

def main():
    validador = ValidadorAcesso('./banco_dados_permissoes/permissoes.json')
    
    print("=== Sistema de Validação de Acesso ===")
    nome = input("digite seu nome: ")
    area = input("digite a área que deseja acessar: ").strip().lower()

    if validador.verificar_acesso(nome, area):
        print("acesso permitido")
    else:
        print("acesso negado")

if __name__ == "__main__":
    main()
