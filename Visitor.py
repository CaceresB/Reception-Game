class Visitor:
  def __init__(self, turns):
    self.turns =turns

  def turn(self):
    self.turns-=1

  def getTurn(self):
    return self.turns

