import unittest
import operacoes

class TestCase(unittest.TestCase):
    def test_adicao(self):
        self.assertEqual(operacoes.soma(10, 5), 15)
        self.assertEqual(operacoes.soma(-1, 1), 0)
        self.assertEqual(operacoes.soma(-1, -1), -2)

    def test_subtracao(self):
        self.assertEqual(operacoes.subtracao(10, 5), 5)
        self.assertEqual(operacoes.subtracao(-1, 1), -2)
        self.assertEqual(operacoes.subtracao(-1, -1), 0)

    def test_multiplicacao(self):
        self.assertEqual(operacoes.multiplicacao(10, 5), 50)
        self.assertEqual(operacoes.multiplicacao(-1, 1), -1)
        self.assertEqual(operacoes.multiplicacao(-1, -1), 1)

    def test_divisao(self):
        self.assertEqual(operacoes.divisao(10, 5), 2)
        self.assertEqual(operacoes.divisao(-1, 1), -1)
        self.assertEqual(operacoes.divisao(-1, -1), 1)
        self.assertEqual(operacoes.divisao(5, 2), 2.5)

        with self.assertRaises(ValueError):
            operacoes.divisao(10, 0)

if __name__ == "__main__":
    unittest.main()