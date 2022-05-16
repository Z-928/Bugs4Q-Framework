import unittest
import qiskit
from qiskit import *
from qiskit import IBMQ

class Test(unittest.TestCase):
	def test_f24(self):
		qr = QuantumRegister(2)
		cr = ClassicalRegister(2)
		qc = QuantumCircuit(qr, cr)
		#%matplotlib inline
		qc.draw(output='mpl')
		try:
			qc.h(0)
		except TypeError:
			self.fail("TypeError")
		
		qc.draw(output='mpl')

if __name__ == '__main__':
    unittest.main(argv=[''])
