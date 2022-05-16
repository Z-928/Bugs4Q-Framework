import unittest
from qiskit import *

class Test(unittest.TestCase):
    def test_f16(self):
        
        qr = QuantumRegister(5,'qr')
        cr = ClassicalRegister(5, 'cr')
        ghz = QuantumCircuit(qr, cr)

        ghz.h(qr[0])
        ghz.cx(qr[0],qr[1])
        ghz.cx(qr[1],qr[2])
        ghz.cx(qr[2],qr[3])
        ghz.cx(qr[3],qr[4])
        ghz.barrier(qr)
        ghz.draw()

        sim_backend = BasicAer.get_backend('statevector_simulator')
        sim_result = execute(ghz, sim_backend).result()
        print(sim_result.get_statevector(0))
        

        self.assertEqual(str(sim_result.get_statevector(0)),'[0.70710678+0.j 0.        +0.j 0.        +0.j 0.        +0.j\n 0.        +0.j 0.        +0.j 0.        +0.j 0.        +0.j\n 0.        +0.j 0.        +0.j 0.        +0.j 0.        +0.j\n 0.        +0.j 0.        +0.j 0.        +0.j 0.        +0.j\n 0.        +0.j 0.        +0.j 0.        +0.j 0.        +0.j\n 0.        +0.j 0.        +0.j 0.        +0.j 0.        +0.j\n 0.        +0.j 0.        +0.j 0.        +0.j 0.        +0.j\n 0.        +0.j 0.        +0.j 0.        +0.j 0.70710678+0.j]')


if __name__ == '__main__':
    unittest.main(argv=[''])
