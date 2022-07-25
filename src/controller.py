import random, unidecode

from jogador import Jogador
from bancoPalavras import BancoPalavras

class Termo():
  def __init__(self, player1_name, player2_name, interface):
    self.players_list = [Jogador(player1_name), Jogador(player2_name)]
    self.entry = ''
    self.random_word = ''
    self.cur_player = None
    self.turn_counter = 1
    self.entry_list = []
    self.hit_list = []
    self.interface = interface
    self.word_base = BancoPalavras('./brazilian')

  def selectRandomPlayer(self):
    return random.choice(self.players_list)

  def novaPartida(self):
    self.random_word = self.word_base.getRandomWord(wordLen=5)
    self.cur_player = self.selectRandomPlayer()
    self.players_list[0].setScore(score=0)
    self.players_list[1].setScore(score=0)
    self.interface.refreshScore(scorePlayer1=0, scorePlayer2=0)
    self.interface.setCurPlayer(self.players_list.index(self.cur_player))
    self.turn_counter = 1

  def verifyLetters(self, entry):
    hit_list = [0] * 5
    random_word = list(unidecode.unidecode(self.random_word))
    entry = list(entry)

    for i in range(5):
      if random_word[i] == entry[i]:
        random_word[i] = entry[i] = None
        hit_list[i] = 10

    for i in range(5):
      if entry[i] in random_word and entry[i]:
        random_word[random_word.index(entry[i])] = entry[i] = None
        hit_list[i] = 5

    return hit_list

  def calculateScore(self, hit_list):
    score = self.cur_player.getScore()
    score += sum(hit_list)
    return score

  def nextTurn(self):
    self.turn_counter += 1
    self.cur_player = self.players_list[1 - self.players_list.index(self.cur_player)]
    self.interface.setCurPlayer(self.players_list.index(self.cur_player))

  def verifyEntry(self, entry):
    self.entry = entry
    word = self.word_base.verifyWord(entry)

    if not word:
      self.interface.showNotification(1)
    else:
      self.entry_list.append(self.entry)
      self.hit_list = self.verifyLetters(entry)
      self.interface.refreshBoard(self.hit_list, word)

      if self.hit_list == [10, 10, 10, 10, 10]:
        self.interface.notifyWinner(self.players_list.index(self.cur_player), self.random_word)
      else:
        score = self.calculateScore(self.hit_list)
        self.cur_player.setScore(score)
        self.interface.refreshScore(self.players_list[0].getScore(), self.players_list[1].getScore())

        if self.turn_counter == 6:
          player1_score = self.players_list[0].getScore()
          player2_score = self.players_list[1].getScore()

          if player1_score > player2_score:
            player = 0
          elif player1_score < player2_score:
            player = 1
          else:
            player = 2

          self.interface.notifyWinner(player, self.random_word, False)
        else:
          self.nextTurn()
      
    
