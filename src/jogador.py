class Jogador():
  def __init__(self, player_name):
    self.name = player_name
    self.score = 0

  def setScore(self, score):
    self.score = score

  def getScore(self):
    return self.score