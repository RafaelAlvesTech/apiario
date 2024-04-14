from dataclasses import dataclass
from typing import Optional

@dataclass()
class Apiario:

    id: int
    id_usuario: int
    status: str = "A"
    atividade: str = "T"
    nome: str 
    estrutura: str = "F"
    cep: Optional[str] = None
    logradouro: Optional[str] = None
    numero: Optional[str] = None
    complemento: Optional[str] = None
    bairro: Optional[str] = None
    cidade: Optional[str] = None
    estado: Optional[str] = None
    responsavel: Optional[str] = None
    telefone: Optional[str] = None
    latitude: Optional[str] = None
    longitude: Optional[str] = None
    observacao: Optional[str] = None




