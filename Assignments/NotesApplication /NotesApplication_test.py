import NotesApplication
import unittest


class NotesApplication_test(unittest.TestCase):


	def setUp(self):
	    self.oneNote = NotesApplication.NotesApplication("Mandela")    
	def test_objects_actually_created_during_instantiation(self):
	    """Test whether objects of class NotesApplication are successfully
	    created during instantiation
	    """
	    self.assertIsInstance(self.oneNote, NotesApplication.NotesApplication)

	def test_author_stored_during_instantiation(self):
	    """Tests whether the author parameter passed during instantiation
	    is stored in the instance variable author"""
	    self.assertEqual(self.oneNote.author, "Mandela")

	def test_noteslist_created_on_instantiation(self):
	    """Tests whether an empty list has been assigned to an instance variable
	    noteslist during instantiation"""
	    self.assertEqual(self.oneNote.notes_list, [])

	def test_get_method_with_out_of_range_index_returns_none(self):
	    """Tests whether calling the get method with a note_id which is greater than
	    the last index of notes_list returns None. That is, no note is returned.
	    Normally, we would expect that an IndexError would be raised. Butt since we want
	    to provide for an exception to handle such a situation, the method should simply
	    not return anything when an out of range index(note_id) is passed to the method
	    """
	    self.assertEqual(self.oneNote.get(20000000000), None)

	def test_whether_return_type_of_get_method_when_the_expected_note_is_a_number(self):
	    """Test whether the get method returns a string even when the note that was\
	    stored at that note_id position is a number. This is in line with the requirements\
	    which specify that the note must be returned as a string.
	    """
	    self.oneNote.create(2525364753684584878)
	    self.assertTrue(type(self.oneNote.get(0)) == str)

	#def test_get_method_with_out_of_range_note_id_prints_appropriate_error_msg(self):
	    """Tests whether calling the get method with an out of index note_id prints
	    the error message: "Get unsuccessful. The note_id you entered doesnt exist"
	    """
	#def test_edit_method_modifies_a_note(self): 
	    """Test whether calling the edit method actually modifies a note"""

	def test_edit_method_with_note_id_that_is_not_an_integer(self): 
	    """Test whether passing a non-integer note_id to the edit method returns None
	    and prints out the appropriate error message.
	    Normally, we would expect that a TypeError is raised. But we plan to handle this
	    exception
	    """
	    self.assertEqual(self.oneNote.get("first item"), None)

	def test_get_method_with_normal_input(self):
	    """Test whether the get method returns the expected note when a valid note_id is passed
	    to the method."""
	    self.oneNote.create("I wish I could fly") #this must be at note_id = 0
	    self.oneNote.create("I want live more than once") #this must be note_id =1
	    self.assertEqual(self.oneNote.get(0), "I wish I could fly")
	    self.assertEqual(self.oneNote.get(1), "I want live more than once")

	#def test_edit_with_out_of_range_note_id_prints_appropriate_error_msg(self):
	    """Test whether calling the edit method with an out of index note_id prints the error
	    message: "Edit unsuccessful. The note_id you entered doesn't exist" 
	    """