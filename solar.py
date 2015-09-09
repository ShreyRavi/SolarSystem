"""
A Solar System graphics example using the PyGame library and the Python language.
(C) Shreyas Tallamraju 2015
"""
import pygame
import math
import solarColorPalette
from planet import planet
 
pygame.init()
 
# Set the width and height of the screen [width, height]
screenWidth = 1024
screenHeight = 768
screenWidthHalf = screenWidth // 2
screenHeightHalf = screenHeight // 2

size = (screenWidth, screenHeight)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Solar System") #set title
#logo = pygame.image.load("solar.gif") #set logo of program
#pygame.display.set_icon(logo)
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
#initialize planets
#mercury
mercury = planet('Mercury')
mercury.setColor(solarColorPalette.mercuryColor)
mercury.setWidth(3)
mercury.setRadius(50)
mercury.setSpeed(4.5)
mercury.setX(50)
mercury.setY(250)
#venus
venus = planet('Venus')
venus.setColor(solarColorPalette.venusColor)
venus.setWidth(7)
venus.setRadius(100)
venus.setSpeed(4)
venus.setX(100)
venus.setY(250)
#earth
earth = planet('Earth')
earth.setColor(solarColorPalette.earthColor)
earth.setWidth(6)
earth.setRadius(150)
earth.setSpeed(3)
earth.setX(150)
earth.setY(250)
#mars
mars = planet('Mars')
mars.setColor(solarColorPalette.marsColor)
mars.setWidth(5)
mars.setRadius(180)
mars.setSpeed(2.5)
mars.setX(180)
mars.setY(250)
#jupiter
jupiter = planet('Jupiter')
jupiter.setColor(solarColorPalette.jupiterColor)
jupiter.setWidth(15)
jupiter.setRadius(250)
jupiter.setSpeed(2)
jupiter.setX(250)
jupiter.setY(250)
#saturn
saturn = planet('Saturn')
saturn.setColor(solarColorPalette.saturnColor)
saturn.setWidth(10)
saturn.setRadius(280)
saturn.setSpeed(2.3)
saturn.setX(280)
saturn.setY(250)
saturn.toggleRings()
#uranus
uranus = planet('Uranus')
uranus.setColor(solarColorPalette.uranusColor)
uranus.setWidth(9)
uranus.setRadius(320)
uranus.setSpeed(1.8)
uranus.setX(320)
uranus.setY(250)
#neptune
neptune = planet('Neptune')
neptune.setColor(solarColorPalette.neptuneColor)
neptune.setWidth(8)
neptune.setRadius(350)
neptune.setSpeed(1.2)
neptune.setX(350)
neptune.setY(250)

def drawPlanets(planetIn):
	pygame.draw.circle(screen, solarColorPalette.white, [screenWidthHalf,screenHeightHalf], planetIn.getRadius(), 1)
	pygame.draw.circle(screen, planetIn.getColor(), [planetIn.getX(), planetIn.getY()], planetIn.getWidth(), planetIn.getWidth())
	if planetIn.hasRings() == True:
		pygame.draw.circle(screen, solarColorPalette.white, [planetIn.getX(), planetIn.getY()], planetIn.getWidth()+5, 1)

def movePlanets(planetIn):
	angl = planetIn.getNextAngle()
	planetIn.setX(int(screenWidthHalf + math.sin(angl) * planetIn.getRadius()))
	planetIn.setY(int(screenHeightHalf + math.cos(angl) * planetIn.getRadius()))

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    # drawing
    screen.fill(solarColorPalette.black)
    #sun
    pygame.draw.circle(screen, solarColorPalette.yellow, [screenWidthHalf, screenHeightHalf], 40, 40)

    #mercury
    drawPlanets(mercury)
	#venus
    drawPlanets(venus)
    #earth
    drawPlanets(earth)
    #mars
    drawPlanets(mars)
	#jupiter
    drawPlanets(jupiter)
	#saturn
    drawPlanets(saturn)
	#uranus
    drawPlanets(uranus)
	#neptune
    drawPlanets(neptune)

    #Moving the planets along orbit
    #mercury
    movePlanets(mercury)
    #venus
    movePlanets(venus)
    #earth
    movePlanets(earth)
	#mars
    movePlanets(mars)
	#jupiter
    movePlanets(jupiter)
	#saturn
    movePlanets(saturn)
	#uranus
    movePlanets(uranus)
	#neptune
    movePlanets(neptune)
    
    pygame.display.flip()
 
    # --- Limit to 120 frames per second
    clock.tick(120)
 
pygame.quit()