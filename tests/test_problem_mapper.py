import unittest
from product.problem_mapper import ProblemMapper


class TestProblemMapper(unittest.TestCase):

    def setUp(self):
        self.mapper = ProblemMapper()

    def test_onboarding_issue(self):
        test_input = "Users are dropping off during signup"
        result = self.mapper.map(test_input)
        self.assertEqual(result.get("problem_type"), "onboarding")

    def test_performance_issue(self):
        test_input = "The dashboard is very slow to load"
        result = self.mapper.map(test_input)
        self.assertEqual(result.get("problem_type"), "performance")


if __name__ == "__main__":
    unittest.main()
