import time
import board
import digitalio

debounceMs = 20
buttons = []


## Button Helpers ##
class Button: 
  def __init__(self, pinRef, onPress, onRelease, lastOpen):
    self.pinRef = pinRef
    self.onPress = onPress
    self.onRelease = onRelease
    self.lastOpen = lastOpen

def registerButton(pin, onPress, onRelease):
  pinRef = digitalio.DigitalInOut(pin)
  pinRef.switch_to_input(digitalio.Pull.UP)
  buttons.append(Button(pinRef, onPress, onRelease, True))

def checkButtons():
  for button in buttons:
    nowOpen = button.pinRef.value

    if nowOpen != button.lastOpen:
      time.sleep((1000/debounceMs) ** -1)

      if nowOpen == button.pinRef.value:
        button.lastOpen = nowOpen

        if nowOpen:
          button.onRelease()
        else:
          button.onPress()

