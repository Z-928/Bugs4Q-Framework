import unittest
from qiskit import *

class Test(unittest.TestCase):
    def test_b37(self):
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
            qobj_list = [compile(qc, backend) for qc in qc_list]
            job_list = [backend.run(qobj) for qobj in qobj_list]

            while job_list:
                for job in job_list:
                    if job.status() in JOB_FINAL_STATES:
                        job_list.remove(job)
                        print(job.result().get_counts())
        except Exception as e:
            print('Reason:', e)
        else:
            self.fail('Error not raised')


if __name__ == '__main__':
    unittest.main(argv=[''])
