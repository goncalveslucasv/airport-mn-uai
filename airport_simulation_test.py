import unittest
from io import StringIO
import sys
import numpy as np
import mock
import airport_simulation

class TestAirportSimulation(unittest.TestCase):

    def test_simulation_results(self):
        # Set random seed for reproducibility
        np.random.seed(42)

        # Set up mock inputs
        input_values = [
            "42\n",  # Random seed
        ]
        with mock.patch('builtins.input', side_effect=input_values):
            # Redirect stdout to capture output
            captured_output = StringIO()
            sys.stdout = captured_output

            # Run the simulation
            airport_simulation.main()

            # Restore stdout
            sys.stdout = sys.__stdout__

            # Get the captured output
            output = captured_output.getvalue()

            # Assertions
            self.assertIn("Resultados de la simulación:", output)
            self.assertIn("Número de aviones:", output)
            self.assertIn("Número de rechazos:", output)
            self.assertIn("Tiempo promedio de permanencia en el aire:", output)
            self.assertIn("Longitud promedio de la cola de aterrizaje:", output)
            self.assertIn("Rechazos por combustible crítico:", output)
            self.assertIn("Tiempo total ocioso de cada pista:", output)
            self.assertIn("Tiempo máximo ocioso de cada pista:", output)

if __name__ == '__main__':
    unittest.main()