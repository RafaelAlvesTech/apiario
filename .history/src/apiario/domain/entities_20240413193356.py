from dataclasses import dataclasses

@dataclass()
class Apiario:

    id: int
    id_usuario: int
    status: str
    atividade: str
    nome: str
    estrutura: str
    

