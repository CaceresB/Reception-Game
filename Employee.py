from random import randint
class Employee:
  busy = False
  cRounds = 0

  def __init__(self, emoji):
    self.speed =0
    self.emoji=emoji

  #def help(self, Visitor):
  def help(self, seen):
    self.busy = True
    if seen<10: self.cRounds = 1
    elif seen<45 : self.cRounds = randint(1,2)
    else:
      seen/15
      self.cRounds = randint(1,randint(2,int(seen/15)))
      
    #Visitor.turn()
    #if Visitor.getTurns==0:
    #  self.busy=False

  def round(self):
    self.cRounds-=1
    if self.cRounds==0:
      self.busy = False
      return True
    else:
      return False

  def isBusy(self):
    return self.busy
