import unittest
from qiskit import *

class Test(unittest.TestCase):
    def test_b5(self):
       

        qasm = '''OPENQASM 2.0;
        include "qelib1.inc";
        qreg q[1];
        creg c[1];
        measure q -> c;'''
        qc = QuantumCircuit()
        qc.from_qasm_str(qasm)

        print( qc.qasm() )

        self.assertEqual(str(qc.qasm()),'OPENQASM 2.0;\ninclude "qelib1.inc";\nqreg q[1];\ncreg c[1];\nmeasure q[0] -> c[0];\n')


if __name__ == '__main__':
    unittest.main(argv=[''])


