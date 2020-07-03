from pynput.mouse import Button, Controller
from pynput import keyboard
import time


mouse = Controller()       
print("hello world")
break_program = False
        
def on_press(key):
        global break_program
                
        if key == keyboard.Key.end:
            print('end pressed')
            break_program = True
            return False        
with keyboard.Listener(on_press=on_press) as listener:
        while break_program==False:
            print('Position: '+str(mouse.position))
            time.sleep(0.01)
        listener.join()

