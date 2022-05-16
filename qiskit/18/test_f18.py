import unittest
from qiskit import *

class Test(unittest.TestCase):

    
    def test_f18(self):
        try:
            if __name__ == "__main__":
                backend = Aer.get_backend('statevector_simulator')
                qc = QuantumCircuit(2, 2)
                qc = QuantumCircuit(2, 2)
                qc.h(0)
                qc.cx(0, 1)
                qc.measure([0,1], [0,1])
                result = execute(qc, backend, shots =100).result()
                print(result.get_counts(qc))
        except TypeError as e:
            self.assertEqual(type(e), TypeError)
           
        else:
            self.fail('TypeError not raised')

if __name__ == '__main__':
    unittest.main(argv=[''])
