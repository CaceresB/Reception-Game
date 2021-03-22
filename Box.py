import random
from Queue import Queue
from time import sleep
from getkey import getkey, keys
from threading import Thread

class Box:
  rPlaces = 3
  numR = 1
  lineSize = 10
  bLen = 10+3
  box=Queue()
  money = int(50)
  IMG_life = "❤︎"
  receptionists = ["👩‍💼", "👨‍💼"]
  lives = 3
  running = True
  level, visitors, seen=0, 0, 0
  speed = [0.20, 0.20, 0.15, 0.10, 0.08, 0.05]

  def __init__(self):
    self.createBox()

  def createBox(self):
    for i in range(self.lineSize):
      self.box.enqueue('|'+(' '*self.numR*3) +'|')
    self.printBox()

  def printBox(self):
    #make a print thing
    print("\033[H",end="")
    print((self.IMG_life+" ")*self.lives)
    print('Budget: '+"{}".format(self.money), "")
    print('+'+('-'*self.numR*3)+'+')
    print('|'+' R '*self.numR+'|')
    self.box.display()
    print('+'+('-'*self.numR*3)+'+')
    
  def roundG(self):
    addRec = random.randint(0, 4)
    if addRec != 0 or self.visitors==10:
      self.box.enqueue('|'+(' '*self.numR*3) +'|')
    else:
      bInd = int((self.numR+3)/2)-1
      self.box.enqueue('|'+(' '*bInd)+ 'V' +(' '*bInd)+'|')
      self.visitors+=1
    if self.box.dequeue().find('V')>-1:
      self.seen+=1
      self.money+=10
    else:
      self.money+=1
    self.printBox()

  def run(self):
    while self.running:
      self.roundG()
      sleep(self.speed[0]) #sleep(speed[level])
      if self.seen ==10:
        self.running=False
      