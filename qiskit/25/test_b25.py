import unittest
from qiskit import QuantumCircuit, assemble
from qiskit import Aer, execute
from qiskit.tools.visualization import plot_histogram
class Test(unittest.TestCase):
	def test_b25(self):
		
		bit = 3
		bit_lst = list(range(bit))
		circuit = QuantumCircuit(bit, bit)
		circuit.reset(0)
		circuit.reset(1)
		circuit.reset(2)
		circuit.x(0)
		circuit.x(1)    
		circuit.ccx(0,1,2)
		circuit.barrier()
		circuit.measure(bit_lst,bit_lst)
		circuit.draw(output='mpl')
		backend = Aer.get_backend('statevector_simulator')
		statevector=backend.run(assemble(circuit)).result().get_statevector()
		print(statevector)
		backend = Aer.get_backend('qasm_simulator')
		counts1=backend.run(assemble(circuit)).result().get_counts()
		print(counts1)
		self.assertDictEqual({'111': 1024}, counts1)


if __name__ == '__main__':
    unittest.main(argv=[''])
