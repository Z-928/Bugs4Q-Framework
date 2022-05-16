import unittest


class Test(unittest.TestCase):

    
    def test_f1(self):
        try:
            from qiskit import QuantumCircuit

            qc = QuantumCircuit(3)
            qc.cx(0, 1, ctrl_state='0')
            qc.ccx(0, 1, 2, ctrl_state='00')
        except TypeError as e:
            self.assertEqual(type(e), TypeError)
           
        else:
            self.fail('TypeError not raised')

if __name__ == '__main__':
    unittest.main(argv=[''])
