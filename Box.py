import random
from Queue import Queue
from time import sleep
from getkey import getkey
from threading import Thread
from Receptionist import Receptionist

class Box:
  rPlaces = 3
  numR = 1
  lineSize = 10
  bLen = 10+3
  bWid=int(9)
  box=Queue()
  money = int(0)
  IMG_life = "❤︎"
  rSymbols = ["👩‍💼", "👨‍💼"]
  lives = 3
  running = True
  level, visitors, seen=0, 0, 0
  speed = range(10, 5, -1)
  vStay = [1]
  cap=200
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
    print((self.IMG_life+" ")*self.lives+"_"*(10-self.lives))
    print('Seen: '+"{}".format(self.visitors))
    print('Budget: '+"{:03}".format(self.money), "")
    print('+'+('-'*(self.bWid-2))+'+')
    print('|   '+('R'+'   ')*self.numR+'|')
    desks = '|_'
    for i in self.receptionists:
      if i.isBusy():
        desks+='_|V|'
      else: desks+='_|_|'
    desks+='__|'
    print(desks)
    self.box.display()
    print('+'+('-'*(self.bWid-2))+'+')
    
  def roundG(self):
    addVis = random.randint(0, int(3-(self.seen/60)))
    if addVis != 0 or self.visitors==self.cap:
      self.box.enqueue(' '*int(self.bWid/2-1) +'| |')
    else:
      #bInd = int((self.numR+3*self.numR)/2)-1
      self.box.enqueue((' '*(int(self.bWid/2-1)))+ '|'+'V' +'|')
      self.visitors+=1

    s=-1 #visitor seen
    for i in range(self.numR):
        if self.receptionists[i].isBusy():
          if random.randint(0, 8-int((self.seen+10)/30))!=0:
            self.money+=random.randint(1, int(10-(self.seen/23)))
            self.receptionists[i].done()
            if s==-1: s=i
        else:
          if s==-1: s=i
    if self.box.dequeue().find('V')>-1:
      self.seen+=1
      if s==-1:
        self.lives-=1
      else:
        self.receptionists[s].help()    
    self.printBox()

  def run(self):
    while self.running:
      self.roundG()
      sleep(self.speed[int((self.seen-9)/40)]/100) #sleep(speed[level])
      if self.seen == self.cap: #10
        self.running=False
        
  def keypress(self,key):
    if key == key == "r": self.addRec()
    if key == key == "l": self.addLife()

  def addRec(self):
    if self.money>=200:
      self.numR+=1
      self.money-=200
      self.bWid+=4
      self.receptionists+=[Receptionist()]

  def addLife(self):
    if self.money>=50:
      self.lives+=1
      self.money-=50


class KeyboardThread(Thread):
  running=True
  def __init__(self, input_cbk = None, name='keyboard-input-thread'):
      self.input_cbk = input_cbk
      super(KeyboardThread, self).__init__(name=name)
      self.start()

  def run(self):
      while self.running:
          self.input_cbk(getkey())