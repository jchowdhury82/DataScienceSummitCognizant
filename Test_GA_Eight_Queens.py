import unittest
import CognizantDS20_GA_EightQueens as cg

class TestEvolution(unittest.TestCase):

    def setUp(self):
        self.g = cg.Generation(size = 20)

    def test_evolve_success_0(self):
        with self.assertRaises(AssertionError):
            self.g = cg.Generation(size = 0)

    def test_evolve_success_1(self):
        self.g.evolve(crosspoint=4, mutationrate=0.1, maxgenerations=100)
        self.assertGreater(self.g.generation, 0)
        self.assertEqual(self.g.genpopulation.fitnessscore, 0)

    def test_evolve_success_2(self):
        self.g.evolve(crosspoint=2, mutationrate=0.2, maxgenerations=100)
        self.assertGreater(self.g.generation, 0)
        self.assertEqual(self.g.genpopulation.fitnessscore, 0)

    def test_evolve_success_3(self):
        self.g.evolve(crosspoint=6, mutationrate=0.3, maxgenerations=100)
        self.assertGreater(self.g.generation, 0)
        self.assertEqual(self.g.genpopulation.fitnessscore, 0)

    def test_evolve_fail_1(self):
        with self.assertRaises(AssertionError):
            self.g.evolve(crosspoint=8, mutationrate=0.1, maxgenerations=100)

    def test_evolve_fail_2(self):
        with self.assertRaises(AssertionError):
            self.g.evolve(crosspoint=0, mutationrate=0.1, maxgenerations=100)

    def test_evolve_fail_3(self):
        with self.assertRaises(AssertionError):
            self.g.evolve(crosspoint=0.5, mutationrate=0.1, maxgenerations=100)

    def test_evolve_fail_4(self):
        with self.assertRaises(AssertionError):
            self.g.evolve(crosspoint=4, mutationrate=0, maxgenerations=100)

    def test_evolve_fail_5(self):
        with self.assertRaises(AssertionError):
            self.g.evolve(crosspoint=4, mutationrate=2, maxgenerations=100)

    def test_evolve_fail_6(self):
        with self.assertRaises(AssertionError):
            self.g.evolve(crosspoint=4, mutationrate=-1, maxgenerations=100)




if __name__ == '__main__':
    unittest.main() 