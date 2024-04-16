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

