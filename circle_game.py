import arcade
import random

### Represents a velocity in the coordinate system
class Velocity:
    ### Initialize a Velocity object with default values
    def __init__(self):
        self.dx = 0.0
        self.dy = 0.0

### Represents a point in the coordinate system
class Point:
    ### Initialize a Point object with default values
    def __init__(self):
        self.x = 0.0
        self.y = 0.0

class Circle:

    ### Initialize a Ball object with random velocity, color, and radius
    ### The user must specify the location
    def __init__(self, x, y):
        self.center = Point()
        self.velocity = Velocity()
        self.center.x = x
        self.center.y = y
        self.velocity.dx = random.uniform(-5,5)
        self.velocity.dy = random.uniform(-5,5)
        self.color = (random.randint(0,256), random.randint(0,256), random.randint(0,256)) #RGB tuple
        self.radius = random.uniform(0,20)

    ### Draw the circle
    def draw(self):
        arcade.draw_circle_filled(self.center.x, self.center.y, self.radius, self.color)

    ### Advance the circle based on velocity for 1 frame
    def advance(self):
        self.center.x += self.velocity.dx
        self.center.y += self.velocity.dy

# Ball Game
class Game(arcade.Window):

    ### Initialize the game window and any game components
    def __init__(self):
        super().__init__(500,500)
        arcade.set_background_color(arcade.color.WHITE)
        self.circles = []

    ### Will be called by the arcade every frame and is used to draw objects
    def on_draw(self):
        # clear the screen to begin drawing
        arcade.start_render()
        for circle in self.circles:
            circle.draw()
            
    ### Will be called by the arcade every frame and is used to update objects
    def update(self, delta_time):
        for circle in self.circles:
            circle.advance()
            # Remove circle if outside of window
            if (circle.center.x > 500 or circle.center.x < 0 or 
                circle.center.y > 500 or circle.center.y < 0):
                self.circles.remove(circle)
        
    
    ### Will be called whenever a key is pressed
    def on_key_press(self, key, key_modifiers):
        if key == arcade.key.SPACE:
            new_circle = Circle(250,250)  # Create circle in the middle of the game screen
            self.circles.append(new_circle)

# Run the game
window = Game()
arcade.run()