import random
from Queue import Queue

class Box:
  rPlaces = 3
  numR = 1
  lineSize = 10
  bLen = 10+3
  box=Queue()
  money = int(50)

  def __init__(self):
    self.createBox()

  def createBox(self):
    for i in range(self.lineSize):
      self.box.enqueue('|'+(' '*self.numR*3) +'|')
    self.printBox()

  def printBox(self):
    #make a print thing
    print('Budget: '+"{}".format(self.money))
    print('+'+('-'*self.numR*3)+'+')
    print('|'+' R '*self.numR+'|')
    self.box.display()
    print('+'+('-'*self.numR*3)+'+')
    
  def roundG(self):
    addRec = random.randint(0, 4)
    if addRec != 0:
      self.box.enqueue('|'+(' '*self.numR*3) +'|')
      self.box.dequeue()
      self.money+=1
    else:
      bInd = int((self.numR+3)/2)-1
      self.box.enqueue('|'+(' '*bInd)+ 'V' +(' '*bInd)+'|')
      self.box.dequeue()
      self.money+=10
    
    self.printBox()
