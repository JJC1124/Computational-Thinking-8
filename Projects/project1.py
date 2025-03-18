###############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
###############################################
q1 = codesters.Square(100, 100, 200, 'blue')
q2 = codesters.Square(-100, 100, 200, 'Red')
q3 = codesters.Square(-100, -100,200,'green')
q4 = codesters.Square(100,-100, 200, 'turquoise')
stage.set_background("summer")
mySprite = codesters.Sprite("cardinal", -100, -100,)
codesters.Sprite("basketball",100, -100)
codesters.Sprite("bike",100, 100)
codesters.Sprite("waterbottle",-100, 100)