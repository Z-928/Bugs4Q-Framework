import unittest
from qiskit import *
from qiskit.providers.aer import *

class Test(unittest.TestCase):
    def test_b17(self):
        
        n = 3
        q = QuantumRegister(n)
        c = ClassicalRegister(n)
        qc = QuantumCircuit(q, c, name="circuit")
        qc.x(0)
        qc.measure([1, 0, 2], [1, 0, 2])
        BACKEND_OPTS_SV = {"method": "statevector"}
        res_SV = execute([qc], QasmSimulator(), backend_options=BACKEND_OPTS_SV, shots=1).result()
        print("counts = " + str(res_SV.get_counts()))
        

        self.assertEqual(str(res_SV.get_counts()),"{'010': 1}")


if __name__ == '__main__':
    unittest.main(argv=[''])
