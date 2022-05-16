import unittest
from qiskit import QuantumCircuit

class Test(unittest.TestCase):

        
    def test_f13(self):
        try:
            qc = QuantumCircuit(3)

            outer_level = QuantumCircuit(2, name='outer')
            inner_level = QuantumCircuit(2, name='inner')
            inner_level.x(0)
            outer_level.append(inner_level.to_gate(), [0,1])

            qc.append(outer_level.control(), [0,1,2])
        except Exception as e:
            #self.assertEqual(type(e), TypeError)
            print('Reason:', e)
        else:
            self.fail('There is no error raised')

if __name__ == '__main__':
    unittest.main(argv=[''])
