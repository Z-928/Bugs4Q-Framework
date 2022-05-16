from qiskit import *
from math import pi
import numpy as np
from qiskit.visualization import plot_bloch_multivector, plot_histogram
from qiskit.quantum_info.operators import Operator
import unittest

class Test(unittest.TestCase):
    def test_b8(self):
        circ = QuantumCircuit(3)
        circ.crz(pi/2,2,0)
        circ.crz(pi/4,2,1)
        U = Operator(circ)

        qae = QuantumRegister(2,'qae')
        reg_b = QuantumRegister(2,'b')
        qc = QuantumCircuit(qae,reg_b)
        qc.append(U,[qae[0],reg_b[0],reg_b[1]])
        uni = Operator(qc)
        print(np.round(uni.data,1))
        qc.draw('mpl')
        self.assertEqual(str(np.round(uni.data,1)),'[[1. +0.j  0. +0.j  0. +0.j  0. +0.j  0. +0.j  0. +0.j  0. +0.j  0. +0.j\n  0. +0.j  0. +0.j  0. +0.j  0. +0.j  0. +0.j  0. +0.j  0. +0.j  0. +0.j ]\n [0. +0.j  0.4-0.9j 0. +0.j  0. +0.j  0. +0.j  0. +0.j  0. +0.j  0. +0.j\n  0. +0.j  0. +0.j  0. +0.j  0. +0.j  0. +0.j  0. +0.j  0. +0.j  0. +0.j ]\n [0. +0.j  0. +0.j  1. +0.j  0. +0.j  0. +0.j  0. +0.j  0. +0.j  0. +0.j\n  0. +0.j  0. +0.j  0. +0.j  0. +0.j  0. +0.j  0. +0.j  0. +0.j  0. +0.j ]\n [0. +0.j  0. +0.j  0. +0.j  0.4-0.9j 0. +0.j  0. +0.j  0. +0.j  0. +0.j\n  0. +0.j  0. +0.j  0. +0.j  0. +0.j  0. +0.j  0. +0.j  0. +0.j  0. +0.j ]\n [0. +0.j  0. +0.j  0. +0.j  0. +0.j  1. +0.j  0. +0.j  0. +0.j  0. +0.j\n  0. +0.j  0. +0.j  0. +0.j  0. +0.j  0. +0.j  0. +0.j  0. +0.j  0. +0.j ]\n [0. +0.j  0. +0.j  0. +0.j  0. +0.j  0. +0.j  0.9+0.4j 0. +0.j  0. +0.j\n  0. +0.j  0. +0.j  0. +0.j  0. +0.j  0. +0.j  0. +0.j  0. +0.j  0. +0.j ]\n [0. +0.j  0. +0.j  0. +0.j  0. +0.j  0. +0.j  0. +0.j  1. +0.j  0. +0.j\n  0. +0.j  0. +0.j  0. +0.j  0. +0.j  0. +0.j  0. +0.j  0. +0.j  0. +0.j ]\n [0. +0.j  0. +0.j  0. +0.j  0. +0.j  0. +0.j  0. +0.j  0. +0.j  0.9+0.4j\n  0. +0.j  0. +0.j  0. +0.j  0. +0.j  0. +0.j  0. +0.j  0. +0.j  0. +0.j ]\n [0. +0.j  0. +0.j  0. +0.j  0. +0.j  0. +0.j  0. +0.j  0. +0.j  0. +0.j\n  1. +0.j  0. +0.j  0. +0.j  0. +0.j  0. +0.j  0. +0.j  0. +0.j  0. +0.j ]\n [0. +0.j  0. +0.j  0. +0.j  0. +0.j  0. +0.j  0. +0.j  0. +0.j  0. +0.j\n  0. +0.j  0.9-0.4j 0. +0.j  0. +0.j  0. +0.j  0. +0.j  0. +0.j  0. +0.j ]\n [0. +0.j  0. +0.j  0. +0.j  0. +0.j  0. +0.j  0. +0.j  0. +0.j  0. +0.j\n  0. +0.j  0. +0.j  1. +0.j  0. +0.j  0. +0.j  0. +0.j  0. +0.j  0. +0.j ]\n [0. +0.j  0. +0.j  0. +0.j  0. +0.j  0. +0.j  0. +0.j  0. +0.j  0. +0.j\n  0. +0.j  0. +0.j  0. +0.j  0.9-0.4j 0. +0.j  0. +0.j  0. +0.j  0. +0.j ]\n [0. +0.j  0. +0.j  0. +0.j  0. +0.j  0. +0.j  0. +0.j  0. +0.j  0. +0.j\n  0. +0.j  0. +0.j  0. +0.j  0. +0.j  1. +0.j  0. +0.j  0. +0.j  0. +0.j ]\n [0. +0.j  0. +0.j  0. +0.j  0. +0.j  0. +0.j  0. +0.j  0. +0.j  0. +0.j\n  0. +0.j  0. +0.j  0. +0.j  0. +0.j  0. +0.j  0.4+0.9j 0. +0.j  0. +0.j ]\n [0. +0.j  0. +0.j  0. +0.j  0. +0.j  0. +0.j  0. +0.j  0. +0.j  0. +0.j\n  0. +0.j  0. +0.j  0. +0.j  0. +0.j  0. +0.j  0. +0.j  1. +0.j  0. +0.j ]\n [0. +0.j  0. +0.j  0. +0.j  0. +0.j  0. +0.j  0. +0.j  0. +0.j  0. +0.j\n  0. +0.j  0. +0.j  0. +0.j  0. +0.j  0. +0.j  0. +0.j  0. +0.j  0.4+0.9j]]')
        self.assertEqual(str(qc),'       ┌──────────┐\nqae_0: ┤0         ├\n       │          │\nqae_1: ┤          ├\n       │  Unitary │\n  b_0: ┤1         ├\n       │          │\n  b_1: ┤2         ├\n       └──────────┘')


if __name__ == '__main__':
    unittest.main(argv=[''])
