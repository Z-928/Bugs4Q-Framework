from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, Aer, execute
import unittest
from qiskit.test import *


class TestAerSimulation(QiskitTestCase,unittest.TestCase):
    def test_f30(self):
        # Initialize circuit
        m_qubit = QuantumRegister(1)
        search_register = QuantumRegister(4)
        result_register = ClassicalRegister(4)
        ancillaries = QuantumRegister(3)
        circuit = QuantumCircuit(search_register, result_register, m_qubit, ancillaries)

        # Put M qubit into 1-superposition
        circuit.x(m_qubit)
        circuit.h(m_qubit)

        # Put search qubits into superposition
        circuit.h(search_register)

        for _ in range(2):

            # Encode S1 * !S2 * S3
            circuit.x( search_register[2] )
            circuit.ccx( search_register[1], search_register[2], ancillaries[0] )
            circuit.ccx( search_register[3], ancillaries[0], ancillaries[1] )
            circuit.x( search_register[2] )

            # Encode S0 * S1
            circuit.ccx( search_register[0], search_register[1], ancillaries[2] )

            # Encode oracle ((S0 * S1) + (S1 * !S2 * S3))
            circuit.x(ancillaries)
            circuit.ccx( ancillaries[1], ancillaries[2], m_qubit[0] )
            circuit.x(ancillaries)
            circuit.x(m_qubit)

            # Reset ancillaries to be used later
            circuit.reset(ancillaries)

            # Do rotation about the average
            circuit.h(search_register)
            circuit.x(search_register)
            circuit.ccx( search_register[0], search_register[1], ancillaries[0] )
            circuit.ccx( search_register[2], ancillaries[0], ancillaries[1] )
            circuit.ccx( search_register[3], ancillaries[1], m_qubit[0] )
            circuit.x(search_register)
            circuit.x(m_qubit)
            circuit.h(search_register)

            # Reset ancillaries for use later
            circuit.reset(ancillaries)
        
        circuit.measure(search_register, result_register)

        # Run the circuit with a given number of shots
        backend_sim = Aer.get_backend('qasm_simulator')
        job_sim = execute(circuit, backend_sim, shots = 1024)
        result_sim = job_sim.result()

        # get_counts returns a dictionary with the bit-strings as keys
        # and the number of times the string resulted as the value
        print(result_sim.get_counts(circuit))
        self.assertDictAlmostEqual({'0000':63, '0001':44, '0010':60, '0011':71, '0100':78, '0101':36, '0110':70, '0111':108, '1000':61, '1001':50, '1010':54, '1011':48, '1100':73, '1101':61, '1110':51, '1111':78},
                              result_sim.get_counts(),
                              delta=30)


if __name__ == '__main__':
    unittest.main(argv=[''])
