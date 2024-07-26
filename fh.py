from ursina import *

app = Ursina()

# Create a basic block (cube)
block = Entity(model='cube', texture='block_texture.png', scale=1)

# Set up camera and controls
camera.position = (0, 10, -20)
player = FirstPersonController()

# Generate a grid of blocks (you can customize this part)
for x in range(-10, 10):
    for z in range(-10, 10):
        new_block = duplicate(block)
        new_block.position = (x, 0, z)

app.run()
