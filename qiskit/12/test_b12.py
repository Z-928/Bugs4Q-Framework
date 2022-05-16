import unittest
from qiskit import *
from qiskit.test import QiskitTestCase

class TestAerSimulation(QiskitTestCase,unittest.TestCase):
    def test_b12(self):
        
        qr = QuantumRegister(2, name='qreg')
        cr = ClassicalRegister(2, name='creg')
        qc = QuantumCircuit(qr,cr)
        qc.h(qr)
        qc.measure_all()

        bkd = Aer.get_backend('qasm_simulator')
        res = execute(qc, backend = bkd).result()
        print(res.get_counts())
        
        self.assertDictAlmostEqual({'00':250 ,'01': 250,'10': 250,'11': 250},
                                   res.get_counts(),
                                   delta=500)
        
        self.assertIn('10 00', str(res.get_counts()))
        self.assertIn('00 00', str(res.get_counts()))
        self.assertIn('11 00', str(res.get_counts()))
        self.assertIn('01 00', str(res.get_counts()))


if __name__ == '__main__':
    unittest.main(argv=[''])
