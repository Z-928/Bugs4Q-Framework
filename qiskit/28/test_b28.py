import unittest
from qiskit import *

class Test(unittest.TestCase):
    def test_b28(self):
        try:
            circuit = QuantumCircuit(1)
            circuit.iden(0)
            print(circuit)
        except AttributeError:
            print('AttributeError raised')
            pass
        else:
            self.fail('AttributeError not raised')


if __name__ == '__main__':
    unittest.main(argv=[''])
