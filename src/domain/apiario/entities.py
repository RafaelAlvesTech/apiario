from datetime import datetime
from dataclasses import dataclass, field
from typing import Optional
import uuid

@dataclass()
class Apiary:

    id: uuid.UUID = field(
        default_factory=lambda: uuid.uuid4)
    id_user: int
    name: str
    status: str = 'A'
    activity: str = 'T'
    structure: str = 'F'
    cep : str
    address: str
    number: str
    complement: str
    neighborhood: str
    city: str
    state: str
    responsible: str
    phone: str
    latitude: str
    longitude: str
    observation: str
