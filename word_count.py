def words(args):
  """Counts the occurrences of characters in a word"""
  wordcount = {}
  for word in args.split():
    if word in wordcount.keys():
      if word == int:
        wordcount[word] += 1
      else:
        wordcount[word] += 1
    else:
      if word.isdigit():
        word = int(word)
        wordcount[word] = 1
      else:
        wordcount[word] = 1
  return wordcount
