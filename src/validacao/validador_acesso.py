import json
from typing import Dict
from ..banco_usuarios.usuario import Usuario

class ValidadorAcesso:
    def __init__(self, arquivo_permissoes: str):
        self.arquivo_permissoes = arquivo_permissoes
        self.usuarios: Dict[str, Usuario] = {}
        self._carregar_permissoes()

    def _carregar_permissoes(self) -> None:
        with open(self.arquivo_permissoes, 'r', encoding='utf-8') as arquivo:
            dados = json.load(arquivo)
            for usuario_data in dados['usuarios']:
                usuario = Usuario(
                    nome=usuario_data['nome'],
                    acessos=usuario_data['acessos']
                )
                self.usuarios[usuario.nome] = usuario

    def verificar_acesso(self, nome: str, area: str) -> bool:
        if nome not in self.usuarios:
            return False
        return self.usuarios[nome].tem_acesso(area) 