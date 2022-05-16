import unittest
from qiskit import *
from qiskit.visualization import plot_histogram
from qiskit.test import *

class TestAerSimulation(QiskitTestCase,unittest.TestCase):
    def test_b39(self):
        qc = QuantumCircuit(4, 4)
        qc.cx(3, 1)
        qc.cx(1, 0)
        qc.cx(0, 1)
        qc.ccx(3, 2, 1)
        qc.cx(1, 2)
        qc.cx(3, 2)
        qc.measure(0, 0)
        qc.measure(1, 1)
        qc.measure(2, 2)
        qc.measure(3, 3)
        job = execute(qc, backend=Aer.get_backend('qasm_simulator'), shots=1024)
        result = job.result()
        count = result.get_counts()
        plot_histogram(count)
        print(count)
        self.assertDictAlmostEqual({'0000':64, '0001':64, '0010':64, '0011':64, '0100':64, '0101':64, '0110':64, '0111':64, '1000':64, '1001':64, '1010':64, '1011':64, '1100':64, '1101':64, '1110':64, '1111':64},
                              count,
                              delta=30)


if __name__ == '__main__':
    unittest.main(argv=[''])
