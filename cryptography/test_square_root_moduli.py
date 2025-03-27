import unittest
import square_root_moduli


#SQR := square_root_moduli
class Test_SQR(unittest.TestCase):
    def test_compute_prime_factors(self):
        self.assertEqual(square_root_moduli.prime_factors(3143), [7, 449])
        self.assertEqual(square_root_moduli.prime_factors(868), [4, 7, 31])
