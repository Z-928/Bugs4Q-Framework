import unittest
from qiskit.circuit import QuantumCircuit, Parameter
from qiskit.circuit.library import EfficientSU2

class Test(unittest.TestCase):
    def test_b11(self):
        
        circuit = EfficientSU2(1)
        x = Parameter("x")
        circuit.global_phase = x
        bound_circuit = circuit.assign_parameters({x: 0.001}, inplace=True)
        print(circuit.parameters)
        print(circuit.global_phase)
        

        self.assertEqual(str(circuit.global_phase),'x')


if __name__ == '__main__':
    unittest.main(argv=[''])
