import time
import board
import pwmio
import util
import effects

pwmOff = 0
pwmDim = 500
pwmBright1 = 10000
pwmBright2 = 30000
pwmMax = ((2 ** 16) - 1)

ledExt = pwmio.PWMOut(board.A0, duty_cycle=pwmOff)
ledCpu = pwmio.PWMOut(board.A1, duty_cycle=pwmOff)
ledAct = pwmio.PWMOut(board.RX, duty_cycle=pwmOff)

def actButtonDown():
  print('button down')
  ledAct.duty_cycle = pwmBright1
  effects.nextEffect()

def actButtonUp():
  print('button up')
  ledAct.duty_cycle = pwmOff

util.registerButton(board.SCK, actButtonDown, actButtonUp)

# Startup animation
time.sleep(0.5)
ledAct.duty_cycle = pwmBright1
time.sleep(0.2)
ledAct.duty_cycle = pwmOff
ledCpu.duty_cycle = pwmBright1
time.sleep(0.2)
ledCpu.duty_cycle = pwmOff
ledExt.duty_cycle = pwmBright1
time.sleep(0.2)
ledExt.duty_cycle = pwmOff
ledCpu.duty_cycle = pwmBright1
time.sleep(0.2)
ledCpu.duty_cycle = pwmOff
ledAct.duty_cycle = pwmBright1
time.sleep(0.2)
ledAct.duty_cycle = pwmOff
time.sleep(0.2)
ledCpu.duty_cycle = pwmDim
ledExt.duty_cycle = pwmDim


# Run loop
while True:
  util.checkButtons()
  effects.runEffect()
