import unittest
from qiskit.extensions.simulator import *
from qiskit import *

class Test(unittest.TestCase):
    def test_b36(self):
        try:
            qubit = QuantumRegister(1, 'qubit')
            circuit = QuantumCircuit(qubit)

            circuit.x(qubit)
            circuit.wait(1e-6, qubit)
            circuit.rx(3.1416, qubit)

            backend = Aer.get_backend('statevector_simulator')
            job = execute(circuit, backend)
            result = job.result()
            outputstate = result.get_statevector(circuit, decimals=3)
            print(outputstate)
        except AttributeError:
            pass
        else:
            self.fail('AttributeError not raised')


if __name__ == '__main__':
    unittest.main(argv=[''])
