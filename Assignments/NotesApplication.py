class NotesApplication(object):
	def __init__ (self, author):
		self.author = author
		self.notes = []

		
	def create(self, note_content):
		self.notes.append(note_content)

	def list(self):
		Notelist = ''
		for index in range(len(self.notes)):
			Notelist+=("\nNote ID: {}".format(index))
			Notelist+= ("\n" + self.notes[index])
			Notelist+=("\nBy Author: " + self.author)
		return Notelist

	def get(self, note_id):
		if note_id < 0 and  note_id >=len(self.notes):
			print "Error: Note ID out of range."
			return
		return self.notes[note_id]

	def search(self, search_text):
		print "\n Showing results for search " + search_text + "\n"

		for index in range(len(self.notes)):
			if search_text in self.notes[index]:
				print ("Note ID: {}".format(index))
				print (self.notes[index])
				print ("\nBy Author: " + self.author + "\n")


	def edit(self, note_id, new_content):
		self.notes[note_id] = new_content
	


# App = NotesApplication("Victor")
# App.create("This is the first note.")
# print(App.list())
# # App.edit(0, "This note has been edited")
# # App.list()
# # App.create("Why is Walter not coding?")
# # App.search("Walter")
# # print(App.get(0))









