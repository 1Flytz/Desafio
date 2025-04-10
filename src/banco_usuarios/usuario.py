from typing import List

class Usuario:
    def __init__(self, nome: str, acessos: List[str]):
        self.nome = nome
        self.acessos = acessos

    def tem_acesso(self, area: str) -> bool:
        return area in self.acessos 