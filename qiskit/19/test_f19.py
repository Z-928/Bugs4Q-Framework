import unittest
from qiskit.extensions import HGate, CXGate
import qiskit.quantum_info as qi
from qiskit import *

class Test(unittest.TestCase):

        
    def test_f19(self):
        try:
            qc = QuantumCircuit(2)
            qc.h(0)
            qc.cx(0,1)

            qc.draw('mpl')
            # no issues with the below line
            qi.Operator.from_label('H') 
            qi.Operator.from_label('X')
        except Exception as e:
            #self.assertEqual(type(e), TypeError)
            print('Reason:', e)
        else:
            self.fail('There is no error raised')

if __name__ == '__main__':
    unittest.main(argv=[''])
