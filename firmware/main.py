import time
import board
import digitalio
import pwmio
import util
import effects

pwmOff = 0
pwmDim = 500
pwmBright1 = 10000
pwmBright2 = 30000
pwmMax = ((2 ** 16) - 1)

ledExt = digitalio.DigitalInOut(board.A0)
ledExt.switch_to_output(value=False)

ledCpu = pwmio.PWMOut(board.MOSI, duty_cycle=pwmDim)
ledAct = pwmio.PWMOut(board.MISO, duty_cycle=pwmOff)

print('mocha')

def actButtonDown():
  print('button down')
  ledAct.duty_cycle = pwmBright1
  effects.nextEffect()

def actButtonUp():
  print('button up')
  ledAct.duty_cycle = pwmOff

util.registerButton(board.SCK, actButtonDown, actButtonUp)


# Run loop
while True:
  util.checkButtons()
  effects.runEffect()
