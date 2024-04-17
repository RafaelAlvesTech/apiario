from dataclasses import dataclass, field #estude field muda a forma que o dataclass verifica os campos, seria um classe especifica para dados.
from typing import Optional #, NamedTuple # pesquisar sobre typing
from datetime import datetime
# from collections import namedtuple

# DDD atacar a complexidade no coração do software

#entidade é um conjunto de atributos + outras entidades + objetos de valor | identifcação + operações

# lapis - prorpiedades - color - mas não tem um id associado, ele pode se tornar um objetos de valor. Um cojunto fechado para descrever a representação do lápis.

#Se a gente precisa medir, quantificar ou descrever no domínio.

#Ele precisa modelar um todo conceitural em informações relacionadas se tornando uma única unidade.

#Exemplo o endereço dentro de um ecommerce pode ser um objeto de valor.

# Objeto tem que ser imutável. Tem que ser imutável
# é a outro verifirar propriedades pois não tem id

@dataclass(kw_only=True) #init, repr, eq(compraração), order e hash cria construtor tipado e outros métodos mágicos. Estude também namedtuples.
class Apiario:
    id: uuid.UUID = field(
        default_factory= lambda: uuid.uuid4()
    )
    id_usuario: int
    nome: str 
    status: str = "A"
    atividade: str = "T"
    estrutura: str = "F"
    data_criacao: Optional[datetime] = field(default_factory=lambda: datetime.now()) #estude default_factory, lambda e datetime. Ponto importante pra testes. funçãpo para gerar uma data nova em tempo de excução
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



#Unique Universally Identifer uuid
#testar as funcionalidades da classe Apiario isso se chama test unitário ou teste de unidades, tem que ser lever e rápido exemplos como  django.models.Model que envolve banco de dados não se aplicaria

#pesquisar sobre parâmetros nomeados

# class Product(NamedTuple):
#     id: int
#     name: str
 
#NamedTuple opções para versões mais antigas do python para também impplementar classes sem precisar de construtores

# Product = namedtuple('Product', ['id', 'name']) #estudar dicionários nomeados


#piramides de testes
# Os teste devem começar pelo teste unitário, depois teste de integração e por fim teste end-to-end por é uma sequencia do mais rapido e barato para mais lento e caro.
#testar as funcionalidades da classe Apiario isso se chama test unitário ou teste de unidades, tem que ser lever e rápido exemplos como  django.models.Model que envolve banco de dados não se aplicaria
# tudo que for externo tem que fazer um dublê de teste chamado de mock, ou seja, simular o comportamento de um objeto real, para que o teste seja leve e rápido. Exemplo se a classe envia um email vai fingir que enviou o email, mas não vai enviar de verdade.
# para testar o django.models.Model seria outro tipo de test chamado test de integração. Testa a integração entre duas ou mais unidades.
# e os teste end-to-end que testa a aplicação como um todo, como se fosse um usuário final e2e.