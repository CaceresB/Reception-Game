from random import randint
from Queue import Queue
from time import sleep
from getkey import getkey
from threading import Thread
from Employee import Employee

class Box:
  numE = 1
  lineSize = 10
  bLen = 13
  bWid=int(9)
  box=Queue()
  money = int(30)
  IMG_life = "❤︎"
  eSymbols = ["👩‍", "👨"]
  lives = 5
  running = True
  level, customers, seen=0, 0, 0
  speed = range(10, 5, -1)
  cap=200
  Employees=[Employee(eSymbols[randint(0,1)])]
  eCost = 175
  lCost = 50

  def __init__(self):
    self.createBox()

  def createBox(self):
    for i in range(self.lineSize):
      self.box.enqueue(' '*int(self.bWid/2-1) +'| |')
    self.printBox()

  def printBox(self):
    #make a print thing
    print("\033[H",end="")
    print("Press E to buy an Employee $"+ "{}".format(self.eCost)) 
    print("Press L to buy a life $"+ "{}".format(self.lCost)) 
    print("Press B to bet a coin" ) 
    print((self.IMG_life+" ")*self.lives+"_"*(10-self.lives))
    print('Seen: '+"{}".format(self.customers))
    print('Budget: '+"{:03}".format(self.money), "")
    
    
    print('+'+('-'*(self.bWid-2))+'+')
    pCash='|  '
    registers = '|_'
    for i in self.Employees:
      pCash+=(i.emoji+'   ')
      if i.isBusy():
        registers+='_|C|'
        
      else: registers+='_|_|'
    registers+='__|'
    pCash+=' |'
    print(pCash)
    print(registers)
    self.box.display()
    
  def roundG(self):
    addCust = randint(0, int(3-(self.seen/60)))
    if addCust != 0 or self.customers==self.cap:
      self.box.enqueue(' '*int(self.bWid/2-1) +'| |')
    else:
      #bInd = int((self.C+3*self.C)/2)-1
      self.box.enqueue((' '*(int(self.bWid/2-1)))+ '|'+'C' +'|')
      self.customers+=1

    s=-1 #visitor seen
    for i in range(self.numE):
        if self.Employees[i].isBusy():
          if self.Employees[i].round():
            self.money+=randint(1, int(10-(self.seen/23)))
            if s==-1: s=i
        else:
          if s==-1: s=i
    if self.box.dequeue().find('C')>-1:
      self.seen+=1
      if s==-1:
        self.lives-=1
      else:
        self.Employees[s].help(self.seen)    
    self.printBox()

  def run(self):
    while self.running:
      self.roundG()
      sleep(self.speed[int((self.seen-9)/40)]/100) #sleep(speed[level])
      if self.seen == self.cap or self.lives==0: #10
        self.running=False
        
  def keypress(self,key):
    if key == key == "e": self.addEmp()
    if key == key == "l": self.addLife()
    if key == key == "b": self.bet()

  def addEmp(self):
    if self.money>=self.eCost:
      self.numE+=1
      self.money-=self.eCost
      self.bWid+=4
      self.Employees+=[Employee(self.eSymbols[randint(0,1)])]

  def addLife(self):
    if self.money>=50:
      self.lives+=1
      self.money-=50

  def bet(self):
    if self.money>=1:
      self.money+=randint(-9,10)-1


class KeyboardThread(Thread):
  running=True
  def __init__(self, input_cbk = None, name='keyboard-input-thread'):
      self.input_cbk = input_cbk
      super(KeyboardThread, self).__init__(name=name)
      self.start()

  def run(self):
      while self.running:
          self.input_cbk(getkey())