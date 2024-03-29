import unittest
from math import  pi,pow
from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, BasicAer, execute

class Test(unittest.TestCase):
	def test_f27(self):
		def QFT(n, inverse=False):
		    """This function returns a circuit implementing the (inverse) QFT."""

		    circuit = QuantumCircuit(n, name='IQFT' if inverse else 'QFT')
		   
		    # here's your old code, building the inverse QFT
		    for i in range(int(n/2)):
		        # note that I removed the qin register, since registers are not 
		        # really needed and you can just use the qubit indices 
		        circuit.swap(i, n - 1 - i)
		    for i in range(n):
		        circuit.h(i)
		        for j in range(i + 1, n, 1):
		            circuit.cu1(-pi / pow(2, j - i), j, i)
		 
		    # now we invert it to get the regular QFT
		    if inverse:
		        circuit = circuit.inverse()
		    
		    return circuit

		n = 3
		qin = QuantumRegister(n)
		cr = ClassicalRegister(n)
		circuit = QuantumCircuit(qin, cr)

		circuit.h(qin)
		circuit.z(qin[2])
		circuit.s(qin[1])
		circuit.z(qin[0])
		circuit.t(qin[0])

		# get the IQFT and add it to your circuit with ``compose``
		# if you want the regular QFT, just set inverse=False
		iqft = QFT(n, inverse=True)   
		circuit.compose(iqft, inplace=True) 

		circuit.measure (qin, cr)


		backend = BasicAer.get_backend("qasm_simulator")
		result = execute(circuit, backend, shots = 500).result()
		counts = result.get_counts(circuit)
		print(counts)
		self.assertDictEqual({'011': 500}, counts)

if __name__ == '__main__':
    unittest.main(argv=[''])
