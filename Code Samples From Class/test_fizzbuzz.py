import unittest
import fizzbuzz

class FizzBuzzTest(unittest.TestCase):
	"""Testing the Fizzbuzz"""
	

	def test_returns_fizz_if_divisible_by_three(self):
		"""Test reutrns fizz when input is divisible by three."""

		self.assertEqual(fizzbuzz.fizz_buzz(3), "fizz")

	def test_returns_fizzbuzz_if_divisible_by_three_and_five(self):
		"""Test reutrns fizzbuzz when input is divisible by three and five"""

		self.assertEqual(fizzbuzz.fizz_buzz(30), "fizzbuzz")

	def test_returns_fizz_if_divisible_by_five(self):
		"""Test reutrns buzz when input is divisible by three."""

		self.assertEqual(fizzbuzz.fizz_buzz(7), "buzz")

