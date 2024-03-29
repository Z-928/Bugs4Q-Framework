import unittest
from qiskit import *
from qiskit.compiler import *

class Test(unittest.TestCase):
    def test_f37(self):
        try:
            n_qubits = 5
            qc_list = []

            for i in range(n_qubits):
                qr = QuantumRegister(n_qubits)
                cr = ClassicalRegister(n_qubits)
                qc = QuantumCircuit(qr, cr)
                qc.x(qr[i])
                qc.measure(qr, cr)
                qc_list.append(qc)

            backend = Aer.get_backend('qasm_simulator')
            transpiled_circs = transpile(qc_list, backend=backend)
            qobjs = assemble(transpiled_circs, backend=backend)
            job_info = backend.run(qobjs)
            for circ_index in range(len(transpiled_circs)):
                print(job_info.result().get_counts(transpiled_circs[circ_index]))
        except Exception as e:
            print('Reason:', e)
        else:
            self.fail('Error not raised')


if __name__ == '__main__':
    unittest.main(argv=[''])
