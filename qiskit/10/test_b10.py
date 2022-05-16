import unittest
from qiskit import *

class Test(unittest.TestCase):
    def test_b10(self):

        qc = QuantumCircuit(1)
        qc.u1(0.24,0)
        print(qc.decompose())

        self.assertEqual(str(qc.decompose()),'     ┌──────────┐\nq_0: ┤ U1(0.24) ├\n     └──────────┘')


if __name__ == '__main__':
    unittest.main(argv=[''])
