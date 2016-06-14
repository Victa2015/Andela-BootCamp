class NotesApplication(object):
	def __init__ (self, author):
		self.author = author
		self.notes = []

		
	def create(self, note_content):
		self.notes.append(note_content)

	def list(self):
		for index in range(len(self.notes)):
			print ("Note ID: {}".format(index))
			print (self.notes[index])
			print ("By Author: " + self.author)

	def get(self, note_id):
		return self.notes[note_id]

	def search(self, search_text):
		print "Showing results for search " + search_text + "\n"

		for index in range(len(self.notes)):
			if search_text in self.notes[index]:
				print ("Note ID: {}".format(index))
				print (self.notes[index])
				print ("\nBy Author: " + self.author + "\n")


	def edit(self, note_id, new_content):
		self.notes[note_id] = new_content


App = NotesApplication("Victor")
App.create("This is the first")
App.list()
App.edit(0, "____")
App.list()
App.create("Why is Walter not coding?")
App.search("Walter")









