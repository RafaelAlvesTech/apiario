from dataclasses import dataclasses

@dataclass()
class Apiario:

    id: int
    id_usuario: int
    status: str = A
    atividade: str = T
    nome: str 
    estrutura: str = F
    
    

