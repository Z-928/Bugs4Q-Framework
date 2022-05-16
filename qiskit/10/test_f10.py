import unittest
from qiskit import *

class Test(unittest.TestCase):
    def test_f10(self):

        qc = QuantumCircuit(1)
        qc.u1(0.24,0)
        transpile(qc, basis_gates=['u1', 'u2', 'u3', 'cx'])
        print(qc)

        self.assertEqual(str(qc),'     ┌──────────┐\nq_0: ┤ U1(0.24) ├\n     └──────────┘')


if __name__ == '__main__':
    unittest.main(argv=[''])
