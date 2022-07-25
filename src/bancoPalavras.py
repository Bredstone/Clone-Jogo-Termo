import random, unidecode

class BancoPalavras():
  def __init__(self, file_path):
    with open(file_path) as f:
      self.word_list = [word.strip().lower() for word in f.readlines()]

  def getRandomWord(self, wordLen):
    filtered_list = [word for word in self.word_list if len(word) == wordLen]
    return random.choice(filtered_list)

  def verifyWord(self, word):
    word_dict = dict([(unidecode.unidecode(word), word) for word in self.word_list])
    return word_dict[word] if word in word_dict.keys() else None