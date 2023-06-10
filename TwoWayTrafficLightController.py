# Import  Library classes  needed - Model is obviously needed
import time
import random
from Model import *
from Button import *
from Counters import *
from myclasses import *
from Lights import *
from Displays import *
from TrafficLights import *

""" This is a traffic light controller class that willl implement basic
light switch from red, green, yellow and show messages on display """

#Constructor: Initialize the necessary component
class TwoWayTrafficLightController:
    def __init__(self):
        print("TrafficLightController: Constructor")
        self._number = 0
        self._button1 = Button(0, "lightSwitch", buttonhandler=None)
        self._display = LCDDisplay(sda = 20, scl = 21, i2cid = 0)
        
        self._tl = TrafficLights()
        # Instantiate a Model. Needs to have the number of states, self as the handler
        self._model = Model(3, self, debug=True)
        # pedestrian request crossing button   
        self._model.addButton(self._button1)

        # Now add all the transitions that are supported by my Model
        self._model.addTransition(0, BTN1_PRESS, 1)

    def run(self):
        # The run method should simply do any initializations (if needed)
        # and then call the model's run method.
        # You can send a delay as a parameter if you want something other
        # than the default 0.1s. e.g.,  self._model.run(0.25)
        self._model.run()

        """
        stateDo - the method that handles the do/actions for each state
        """
    def stateDo(self, state):
            
        if state == 0:
           print('keep lights on')
           self._tl.redLight()
           self._model.gotoState(1) 
        elif state == 1:
           print('switch lights ')
           self._tl.greenLight()
           self._model.gotoState(2) 
        elif state == 2:
             
           self._model.gotoState(3)
            # State 2 do/actions
        elif state == 3:
           print('switch lights ')
           print('Red Lights')
           self._tl.redLight()
           self._model.gotoState(4)
            # State 2 do/actions
        elif state == 4:
           print('switch lights ')
           print('Red Lights')
           self._tl.redLight()
           self._model.gotoState(5)
            # State 2 do/actions
        elif state == 5:
           print('switch lights ')
           print('Red Lights')
           self._tl.redLight()
           self._model.gotoState(6)
            # State 2 do/actions  
           pass  
          
         

        """
    stateEntered - is the handler for performing entry/actions
    You get the state number of the state that just entered
    Make sure actions here are quick
    """
    def stateEntered(self, state):
        # Again if statements to do whatever entry/actions you need
        if state == 0:
            # entry actions for state 0
            print('State 0 entered')
            print('Green light / red Light')
            self._tl.redLight()
            self._tl.greenLight()
       
        
        elif state == 1:
            # entry actions for state 1
            print('State 1 entered')
            print('Counter Switch off Toggle Light to change')
            print('')
            print('Green Light')
            self._tl.greenLight()
            print('')
            print('')
          
        elif state == 2:
            # entry actions for state 2
            print('State 2 entered')
            print('Transitioning from Green to RED')
            print('Yellow Lights')
            self._tl.yellowLight()
            print('')
            print('')
        elif state == 3:
            # entry actions for state 
            print('State 3 entered')
            print('Transitioning from Green to RED')
            print('Red Lights')
            self._tl.redLight()
            print('')
            print('') 
        elif state == 4:
            # entry actions for state 
            print('State 4 entered')
            print('Flashing pedestian crossing sign')
            print('Red Lights')
            self._tl.redLight()
            print('')
            print('')
        elif state == 5:
            # entry actions for state 
            print('State 5 entered')
            print('Pedestrian request crossing')
            print('Red Lights')
            self._tl.redLight()
            print('')
            print('') 
        elif state == 6:
            # entry actions for state 
            print('State 6 entered')
            print('Emergency vehicle Approaching')
            print('Flash yellow light')
            self._tl.yellowLight()
            print('')
            print('')               
          
        
    def stateLeft(self, state):
        if state == 2:
            self._tl.yellowLight() 
    
    # Test your model. Note that this only runs the template class above
# If you are using a separate main.py or other control script,
# you will run your model from there.
if __name__ == '__main__':
    MyControllerTemplate().run()
                       