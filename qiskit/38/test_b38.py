import unittest
from qiskit import *
from qiskit.providers.aer.library import *

class Test(unittest.TestCase):
    def test_b38(self):
        try:
            q1 = QuantumCircuit(2)
            q1.save_statevector()  # Save initial state
            q1.h(0)
            q1.save_statevector()  # Save state after Hadamard
            q1.cx(0, 1)
            q1.save_statevector()  # Save state after CNOT (also a final state)
            job = execute(q1, backend=Aer.get_backend('aer_simulator'), shots=1024)
            statevectors = job.result().get_statevector()
        except Exception as e:
            print('Reason:', e)
        else:
            self.fail('Error not raised')


if __name__ == '__main__':
    unittest.main()
