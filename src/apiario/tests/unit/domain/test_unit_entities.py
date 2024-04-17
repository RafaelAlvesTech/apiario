from dataclasses import is_dataclass
from datetime import datetime
import unittest
from apiario.domain.entities import Apiario

class TestApiarioUnit(unittest.TestCase):
    def test_if_is_a_dataclass(self):
        self.assertTrue(is_dataclass(Apiario)) # Verifica se a classe Apiario é data classe
# ir do test mais simples posssível
    def test_construtor(self): #testa a criação do construtor
        apiario = Apiario(id=1, id_usuario = 1, nome ="Favo Amarelo" )
        self.assertEqual(apiario.id, 1)
        self.assertEqual(apiario.id_usuario, 1)
        self.assertEqual(apiario.nome, "Favo Amarelo")
        self.assertEqual(apiario.status, "A")
        self.assertEqual(apiario.atividade, "T")
        self.assertEqual(apiario.estrutura, "F")
        self.assertIsInstance(apiario.data_criacao, datetime)
        self.assertIsNone(apiario.cep)
        self.assertIsNone(apiario.logradouro)
        self.assertIsNone(apiario.numero)
        self.assertIsNone(apiario.complemento)
        self.assertIsNone(apiario.bairro)
        self.assertIsNone(apiario.cidade)
        self.assertIsNone(apiario.estado)
        self.assertIsNone(apiario.responsavel)
        self.assertIsNone(apiario.telefone)
        self.assertIsNone(apiario.latitude)
        self.assertIsNone(apiario.longitude)
        self.assertIsNone(apiario.observacao)
        data_criacao = datetime.now() #testando a data de criação
        apiario = Apiario(
            id=1,
            id_usuario=1,
            nome="Favo Amarelo",
            status="I",
            atividade="C",
            estrutura="A",
            data_criacao=data_criacao,
            cep="12345678",
            logradouro="Rua dos Bobos",
            numero="0",
            complemento="",
            bairro="Centro",
            cidade="São Paulo",
            estado="SP",
            responsavel="Fulano",
            telefone="11999999999",
            latitude=0.0,
            longitude=0.0,
            observacao="Observaçao"

        )
        self.assertEqual(apiario.id, 1)
        self.assertEqual(apiario.id_usuario, 1)
        self.assertEqual(apiario.nome, "Favo Amarelo")
        self.assertEqual(apiario.status, "I")
        self.assertEqual(apiario.atividade, "C")
        self.assertEqual(apiario.estrutura, "A")
        self.assertEqual(apiario.data_criacao, data_criacao)
        self.assertEqual(apiario.cep, "12345678")
        self.assertEqual(apiario.logradouro, "Rua dos Bobos")
        self.assertEqual(apiario.numero, "0")
        self.assertEqual(apiario.complemento, "")
        self.assertEqual(apiario.bairro, "Centro")
        self.assertEqual(apiario.cidade, "São Paulo")
        self.assertEqual(apiario.estado, "SP")
        self.assertEqual(apiario.responsavel, "Fulano")
        self.assertEqual(apiario.telefone, "11999999999")
        self.assertEqual(apiario.latitude, 0.0)
        self.assertEqual(apiario.longitude, 0.0)
        self.assertEqual(apiario.observacao, "Observaçao")
def test_if_data_criacao_is_generated_in_constructor(self): #testa se a data de criação é um datetime
    apiario = Apiario(id=1, id_usuario=1, nome="Favo Amarelo")
    apiario2 = Apiario(id=2, id_usuario=2, nome="Bico Doce")
    self.assertNotEqual(
        apiario.data_criacao.timestamp(),
        apiario2.data_criacao.timestamp()

    )

