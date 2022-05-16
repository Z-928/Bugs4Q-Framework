import unittest
from qiskit.test import QiskitTestCase
from qiskit import *
from qiskit.providers.aer import QasmSimulator

class Test(QiskitTestCase,unittest.TestCase):
	def test_f26(self):
		circuit = QuantumCircuit(2)
		circuit.h(0)
		circuit.x(1)
		circuit.cx(0,1)
		circuit.measure_all()

		backend=QasmSimulator()
		job_sim=backend.run(transpile(circuit,backend),shots=1024)
		result_sim=job_sim.result()

		counts=result_sim.get_counts(circuit)
		print(counts)
		print(circuit)
		self.assertDictAlmostEqual({'10': 500, '01': 500},
                                   counts,
                                   delta=500)

if __name__ == '__main__':
    unittest.main(argv=[''])
