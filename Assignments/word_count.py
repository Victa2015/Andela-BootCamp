def words(words):
  wordict = {}
  for word in words.split():
    if word.isdigit():
      word = int(word)
    wordict.setdefault(word, 0)
    wordict[word] += 1
      
  return wordict