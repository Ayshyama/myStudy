import unittest


def calculate_average(numbers):
    if not numbers:
        return None
    total = sum(numbers)
    return total / len(numbers)


print(calculate_average([]) == None)


class TestCalculateAverage(unittest):
    def test_empty_list(self):
        numbers = []
        result = calculate_average(numbers)
        self.assertIsNone(result)

    def test_positive_numbers(self):
        numbers = [1, 2, 3, 4, 5]
        result = calculate_average(numbers)
        self.assertEqual(result, 3)

    def test_negative_numbers(self):
        numbers = [-1, -2, -3, -4, -5]
        result = calculate_average(numbers)
        self.assertEqual(result, -3)

    def test_mixed_numbers(self):
        numbers = [-1, 2, -3, 4, -5]
        result = calculate_average(numbers)
        self.assertEqual(result, -0.6)
