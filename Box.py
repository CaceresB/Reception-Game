import random
from Queue import Queue
from time import sleep
from getkey import getkey, keys
from threading import Thread
from Recptionist import Receptionist

class Box:
  rPlaces = 3
  numR = 1
  lineSize = 10
  bLen = 10+3
  bWid=int(9)
  box=Queue()
  money = int(50)
  IMG_life = "❤︎"
  rSymbols = ["👩‍💼", "👨‍💼"]
  lives = 3
  running = True
  level, visitors, seen=0, 0, 0
  speed = [0.4, 0.20, 0.20, 0.15, 0.10, 0.08, 0.05]
  cap=20
  receptionists=[Receptionist()]

  def __init__(self):
    self.createBox()

  def createBox(self):
    for i in range(self.lineSize):
      self.box.enqueue(' '*int(self.bWid/2-1) +'| |')
    self.printBox()

  def printBox(self):
    #make a print thing
    print("\033[H",end="")
    print((self.IMG_life+" ")*self.lives)
    print('Budget: '+"{}".format(self.money), "")
    print('+'+('-'*(self.bWid-2))+'+')
    print('|   '+('R'+'   ')*self.numR+'|')
    self.box.display()
    print('+'+('-'*(self.bWid-2))+'+')
    
  def roundG(self):
    addVis = random.randint(0, 4)
    if addVis != 0 or self.visitors==self.cap:
      self.box.enqueue(' '*int(self.bWid/2-1) +'| |')
    else:
      #bInd = int((self.numR+3*self.numR)/2)-1
      self.box.enqueue((' '*(int(self.bWid/2-1)))+ '|'+'V' +'|')
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
      if self.seen == self.cap: #10
        self.running=False
        
  def keypress(self,key):
    global order
    if key == key == "r": self.addRec()
    if key == keys.DOWN or key == "s": order = "down"

  def addRec(self):
    if self.money>=100:
      self.numR+=1
      self.money-=100
      self.bWid+=4

  def helpVisit(self):
    return


class KeyboardThread(Thread):
  running=True
  def __init__(self, input_cbk = None, name='keyboard-input-thread'):
      self.input_cbk = input_cbk
      super(KeyboardThread, self).__init__(name=name)
      self.start()

  def run(self):
      while self.running:
          self.input_cbk(getkey())