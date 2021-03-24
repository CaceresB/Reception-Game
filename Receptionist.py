class Receptionist:
  busy = False

  def __init__(self):
    self.speed =0

  #def help(self, Visitor):
  def help(self):
    self.busy = True
    #Visitor.turn()
    #if Visitor.getTurns==0:
    #  self.busy=False

  def done(self):
    self.busy= False

  def isBusy(self):
    return self.busy
