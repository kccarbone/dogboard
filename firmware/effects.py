import time
import board
import pwmio

pwmOff = 0
pwmMax = ((2 ** 16) - 1)
pwmGrad = [
  0,
  500,
  1000,
  2500,
  10000,
  25000,
  60000
]

# Outputs
branchA = pwmio.PWMOut(board.A1, duty_cycle=pwmOff)
branchB = pwmio.PWMOut(board.RX, duty_cycle=pwmOff)

# State vars
currentEffect = 0
effectSpeed = 10 
tick = 0

# Define effects
#   Based on 1,000 "steps" of roughly 10ms each
def off(_):
  branchA.duty_cycle = pwmOff
  branchB.duty_cycle = pwmOff

def alternatingBlink(step):
  stepInterval = 100 # Lower = faster

  if (step // stepInterval) % 2:
    branchA.duty_cycle = pwmOff
    branchB.duty_cycle = pwmGrad[3]
  else:
    branchB.duty_cycle = pwmOff
    branchA.duty_cycle = pwmGrad[3]

def crossFade(step):
  brightFactor = 50 # 1 - 100

  if step < 500:
    branchA.duty_cycle = step * brightFactor
    branchB.duty_cycle = (500 - step) * brightFactor
  else:
    branchA.duty_cycle = (1000 - step) * brightFactor
    branchB.duty_cycle = (step - 500) * brightFactor


# Add new effects to list
effectList = [
  off,
  alternatingBlink,
  crossFade
]

# Auto increment
def nextEffect():
  global tick
  tick = 0
  global currentEffect
  currentEffect += 1
  
  if currentEffect >= len(effectList):
    currentEffect = 0

# Executes once for each program cycle
def runEffect():
  global tick
  tick += 1

  if tick > ((101 - effectSpeed) * 1000):
    tick = 0
  
  step = tick // (101 - effectSpeed)
  effectList[currentEffect](step)

