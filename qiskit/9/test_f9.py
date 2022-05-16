import unittest
from qiskit.circuit import Parameter
from qiskit import pulse
from qiskit.test.mock.backends.almaden import *

class Test(unittest.TestCase):
    def test_f9(self):
        phase = Parameter('phase')

        with pulse.build(FakeAlmaden()) as phase_test_sched:
            pulse.shift_phase(phase, pulse.drive_channel(0))

        phase_test_sched.instructions # ()
        self.assertEqual(str(phase_test_sched.instructions),'((0, ShiftPhase(phase, DriveChannel(0))),)')

if __name__ == '__main__':
    unittest.main(argv=[''])
