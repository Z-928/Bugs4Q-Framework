from qiskit import *
import unittest

class Test(unittest.TestCase):
    def test_f36(self):
        try:
            qubit = QuantumRegister(1, 'qubit')
            circuit = QuantumCircuit(qubit)

            circuit.x(qubit)
            circuit.barrier(qubit)
            circuit.id(qubit)
            circuit.barrier(qubit)
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
