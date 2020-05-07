# Self Driving Car

# Importing the libraries
import numpy as np
from random import random, randint
import matplotlib.pyplot as plt
import time
import gc

# Importing the Kivy packages
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.graphics import Color, Ellipse, Line
from kivy.config import Config
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock
from kivy.core.image import Image as CoreImage
from PIL import Image as PILImage
from kivy.graphics.texture import Texture

# Importing the Dqn object from our AI in ai.py
from ai import Dqn
# Free memory
gc.collect()

# Adding this line if we don't want the right click to put a red point
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')
Config.set('graphics', 'resizable', False)
Config.set('graphics', 'width', '1429')
Config.set('graphics', 'height', '660')

# Introducing last_x and last_y, used to keep the last point in memory when we draw the sand on the map
last_x = 0
last_y = 0
n_points = 0
length = 0

# Getting our AI, which we call "brain", and that contains our neural network that represents our Q-function
brain = Dqn(5,3,0.9) #
action2rotation = [0,5,-5]
last_reward = 0
scores = []
im = CoreImage("./images/MASK1.png")
# Initializing the map
first_update = True
def init():
    global sand
    global goal_x
    global goal_y
    global first_update
    global timestep
    sand = np.zeros((width, height))
    img = PILImage.open("./images/mask.png").convert('L')
    sand = np.asarray(img)/255
    goal_x = 304#Position XA
    goal_y = 375#position YA
    first_update = False
    global swap
    swap = 0
    timestep =0


# Initializing the last distance
last_distance = 0

# Creating the car class

class Car(Widget):
    
    angle = NumericProperty(0)
    rotation = NumericProperty(0)
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)
    sensor1_x = NumericProperty(0)
    sensor1_y = NumericProperty(0)
    sensor1 = ReferenceListProperty(sensor1_x, sensor1_y)
    sensor2_x = NumericProperty(0)
    sensor2_y = NumericProperty(0)
    sensor2 = ReferenceListProperty(sensor2_x, sensor2_y)
    sensor3_x = NumericProperty(0)
    sensor3_y = NumericProperty(0)
    sensor3 = ReferenceListProperty(sensor3_x, sensor3_y)
    signal1 = NumericProperty(0)
    signal2 = NumericProperty(0)
    signal3 = NumericProperty(0)

    def move(self, rotation):
        self.pos = Vector(*self.velocity) + self.pos
        self.rotation = rotation
        self.angle = self.angle + self.rotation
        self.sensor1 = Vector(30, 0).rotate(self.angle) + self.pos
        self.sensor2 = Vector(30, 0).rotate((self.angle+30)%360) + self.pos
        self.sensor3 = Vector(30, 0).rotate((self.angle-30)%360) + self.pos
        self.signal1 = int(np.sum(sand[int(self.sensor1_x)-10:int(self.sensor1_x)+10, int(self.sensor1_y)-10:int(self.sensor1_y)+10]))/400.
        self.signal2 = int(np.sum(sand[int(self.sensor2_x)-10:int(self.sensor2_x)+10, int(self.sensor2_y)-10:int(self.sensor2_y)+10]))/400.
        self.signal3 = int(np.sum(sand[int(self.sensor3_x)-10:int(self.sensor3_x)+10, int(self.sensor3_y)-10:int(self.sensor3_y)+10]))/400.
        if self.sensor1_x>width-10 or self.sensor1_x<10 or self.sensor1_y>height-10 or self.sensor1_y<10:
            self.signal1 = 1.# out of map detect full sand
        if self.sensor2_x>width-10 or self.sensor2_x<10 or self.sensor2_y>height-10 or self.sensor2_y<10:
            self.signal2 = 1.
        if self.sensor3_x>width-10 or self.sensor3_x<10 or self.sensor3_y>height-10 or self.sensor3_y<10:
            self.signal3 = 1.
        

class Ball1(Widget):
    pass
class Ball2(Widget):
    pass
class Ball3(Widget):
    pass

# Creating the game class

class Game(Widget):

    car = ObjectProperty(None)  # getting the car object from our kivy file
    ball1 = ObjectProperty(None)
    ball2 = ObjectProperty(None)
    ball3 = ObjectProperty(None)

    def serve_car(self):# starting the car when we launch the application
        self.car.center = self.center # the car will start at the center of the map
        self.car.velocity = Vector(6, 0)# the car will start to go horizontally to the right with a speed of 6

    def update(self, dt):

        global brain
        global last_reward
        global scores#the means of the rewards
        global last_distance #the last distance from the car to the goal
        global goal_x
        global goal_y
        global width #width of the map
        global height # height of the map
        global swap
        global timestep

        width = self.width
        height = self.height
        if first_update:
            init()

        xx = goal_x - self.car.x #difference of x-coordinates between the goal and the car
        yy = goal_y - self.car.y # difference of y-coordinates between the goal and the car
        orientation = Vector(*self.car.velocity).angle((xx,yy))/180.## direction of the car with respect to the goal (if the car is heading perfectly towards the goal, then orientation = 0)
        last_signal = [self.car.signal1, self.car.signal2, self.car.signal3, orientation, -orientation]#input state vector, composed of the three signals received by the three sensors, plus the orientation and -orientation
        action = brain.update(last_reward, last_signal)# playing the action from our ai (the object brain of the dqn class)
        scores.append(brain.score())# appending the score (mean of the last 100 rewards to the reward window)
        rotation = action2rotation[action]# converting the action played (0, 1 or 2) into the rotation angle (0°, 20° or -20°)
        self.car.move(rotation)# moving the car according to this last rotation angle
        distance = np.sqrt((self.car.x - goal_x)**2 + (self.car.y - goal_y)**2) # getting the new distance between the car and the goal right after the car moved
        self.ball1.pos = self.car.sensor1 # updating the position of the first sensor (ball1) right after the car moved
        self.ball2.pos = self.car.sensor2 # updating the position of the second sensor (ball1) right after the car moved
        self.ball3.pos = self.car.sensor3 # updating the position of the  third sensor (ball1) right after the car moved
        timestep = timestep +1


        if sand[int(self.car.x),int(self.car.y)] > 0: # if the car is on the sand
            self.car.velocity = Vector(1, 0).rotate(self.car.angle) # it is slowed down (speed = 1)

            print(timestep,1, goal_x, goal_y, distance, int(self.car.x), int(self.car.y),
                  im.read_pixel(int(self.car.x), int(self.car.y)))
            last_reward = -1  # and reward = -1
        else: # otherwise
            self.car.velocity = Vector(3, 0).rotate(self.car.angle) # it goes to a normal speed (speed = 6)
            last_reward = -0.2 # and it gets living penalty

            if distance < last_distance: # however if it getting close to the goal
                last_reward = 0.5 # it still gets slightly positive reward 0.1

            print(timestep,0, goal_x, goal_y, distance, int(self.car.x), int(self.car.y),
                  im.read_pixel(int(self.car.x), int(self.car.y)))

        if self.car.x < 10: # if the car is in the left edge of the frame
            self.car.x = 10 # it is not slowed down
            last_reward = -1 # but it gets bad reward -1
        if self.car.x > self.width-10: # if the car is in the right edge of the frame
            self.car.x = self.width-10 # it is not slowed down
            last_reward = -1 # but it gets bad reward -1
        if self.car.y < 10: # if the car is in the bottom edge of the frame
            self.car.y = 10 # it is not slowed down
            last_reward = -1 # but it gets bad reward -1
        if self.car.y > self.height-10: # if the car is in the upper edge of the frame
            self.car.y = self.height-10 # it is not slowed down
            last_reward = -1 # but it gets bad reward -1


        # Updating the last distance from the car to the goal
        last_distance = distance




        if distance < 25:# when the car reaches its goal
            if swap == 0:
                goal_x = 304
                goal_y = 375
                swap = 1
                last_distance=distance # Updating the last distance from the car to the goal
            elif swap == 1:
                goal_x = 225
                goal_y = 63
                swap = 2
                last_distance=distance
            else:
               goal_x = 800
               goal_y = 60
               swap=0
               last_distance = distance




    # Adding the painting tools

class MyPaintWidget(Widget):

    def on_touch_down(self, touch):# putting some sand when we do a left click
        global length, n_points, last_x, last_y
        with self.canvas:
            Color(0.8,0.7,0)
            d = 10.
            touch.ud['line'] = Line(points = (touch.x, touch.y), width = 10)
            last_x = int(touch.x)
            last_y = int(touch.y)
            n_points = 0
            length = 0
            sand[int(touch.x),int(touch.y)] = 1
            img = PILImage.fromarray(sand.astype("uint8")*255)
            img.save("./images/sand.jpg")

    def on_touch_move(self, touch): # putting some sand when we move the mouse while pressing left
        global length, n_points, last_x, last_y
        if touch.button == 'left':
            touch.ud['line'].points += [touch.x, touch.y]
            x = int(touch.x)
            y = int(touch.y)
            length += np.sqrt(max((x - last_x)**2 + (y - last_y)**2, 2))
            n_points += 1.
            density = n_points/(length)
            touch.ud['line'].width = int(20 * density + 1)
            sand[int(touch.x) - 10 : int(touch.x) + 10, int(touch.y) - 10 : int(touch.y) + 10] = 1
            last_x = x
            last_y = y

# Adding the API Buttons (clear, save and load)

class CarApp(App):

    def build(self):
        parent = Game()
        parent.serve_car()
        Clock.schedule_interval(parent.update, 1.0/60.0)
        self.painter = MyPaintWidget()
        clearbtn = Button(text = 'clear')
        savebtn = Button(text = 'save', pos = (parent.width, 0))
        loadbtn = Button(text = 'load', pos = (2 * parent.width, 0))
        clearbtn.bind(on_release = self.clear_canvas)
        savebtn.bind(on_release = self.save)
        loadbtn.bind(on_release = self.load)
        parent.add_widget(self.painter)
        parent.add_widget(clearbtn)
        parent.add_widget(savebtn)
        parent.add_widget(loadbtn)
        return parent

    def clear_canvas(self, obj):
        global sand
        self.painter.canvas.clear()
        sand = np.zeros((width, height))

    def save(self, obj):
        print("saving brain...")
        brain.save()
        plt.plot(scores)
        plt.show()

    def load(self, obj):
        print("loading last saved brain...")
        brain.load()




# Running the whole thing
if __name__ == '__main__':
    CarApp().run()
