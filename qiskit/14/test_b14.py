import unittest
from qiskit import Aer, QuantumCircuit

from qiskit.opflow import CircuitSampler, StateFn, Z, Y, I
from qiskit.utils import QuantumInstance
from qiskit.opflow.expectations import PauliExpectation

class Test(unittest.TestCase):
    def test_f14(self):
        
        state = QuantumCircuit(2)

        state.h(1)
        state.sdg(1)
        state.cz(0, 1)
        state.h(1)
        print(state)
        
        obs = (Z ^ I) - 1j * (Y ^ I)
        exp_val = ~StateFn(obs) @ StateFn(state)
        

        print(exp_val)

        print('Eval ', exp_val.eval())  # = 0+1j
        print('Qasm ', CircuitSampler(QuantumInstance(Aer.get_backend('qasm_simulator'),
                                       shots=100000)).convert(exp_val).eval())  # = 0 (up to shot noise)
        

        self.assertEqual(str(exp_val.eval()),'(-2.22e-16+0.9999999999999991j)')


if __name__ == '__main__':
    unittest.main(argv=[''])
