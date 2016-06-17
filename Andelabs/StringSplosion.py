class StringSplosion(object):
  def __init__(self, word):
    self.word = word
    
  def manipulate():
	  length = len(self.word) + 1
	  newWord =''
	  
	  for i in range(length):
		  newWord +=self.word[:i]

	  return newWord
		
