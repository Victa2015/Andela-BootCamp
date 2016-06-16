import NotesApplication
import unittest


class NotesApplication_test(unittest.TestCase):


	def test_returns_note_at_given_index(self):
		self.assertEqual(NotesApplication.get(num), NotesApplication.notes[num] )