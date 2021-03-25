from Box import Box, KeyboardThread
from cursor import hide, show



hide()
world = Box()

kthread = KeyboardThread(world.keypress)


world.run()

show()
