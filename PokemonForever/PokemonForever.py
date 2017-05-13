import pygame,sys,random,math,os
from pygame.locals import *

pygame.init()
#setting the directory so program knows where to look for the pokemon
os.chdir("C:/Pygame/PokemonForever/platinum")
#screen size
screenSize = width,height = 1200,750
pixelDimensions = 80

MAXpokemonArraySize = 20
pokemon = []


def randomBackground():
    randColor = random.randint(10,250)
    return randColor

#function for randomly picking a pokemon in file
def randomFilename():
    #there are 493 pokemon in total
    randomPokemon = random.randint(1,493)
    if(randomPokemon<10):
        found = "00"+str(randomPokemon) + ".png"
    elif(randomPokemon < 100):
        found = "0"+str(randomPokemon) + ".png"
    else:
        found = str(randomPokemon)+".png"
    return found




def randomLocation(isHeight):
    if isHeight:
        size = random.randint(100,height - 85)
    else:
        size = random.randint(100,width - 85)
    return size


class Pokemon:
        def __init__(self,x,y):
            self.colorKey = (0,0,0)
            self.alpha = 255
            self.x = x
            self.y = y
            self.image = pygame.Surface((pixelDimensions,pixelDimensions))
            self.speed = 0
            self.angle = 0
            self.size = pixelDimensions

        def __call__(self,x,y):
            self.colorKey = (0,0,0)
            self.alpha = 255
            self.x = x
            self.y = y
            self.image = pygame.Surface((pixelDimensions,pixelDimensions))
            self.speed = 0
            self.angle = 0
            self.size = pixelDimensions

        def load(self,filename):

            try:
                self.image = pygame.image.load(filename).convert_alpha()

            except:
                string = 'An error has occured while loading the image.'
                print(string)
                input('Press [Enter] to exit')
                exit(0)

        def move(self):
            self.x += math.sin(self.angle)*self.speed
            self.y -= math.cos(self.angle)*self.speed

        def bounce(self):
            if self.x > width - self.size:
                self.x = 2*(width - self.size) - self.x
                self.angle = - self.angle
                
               

            elif self.x < self.size:
                self.x = 2*self.size - self.x
                self.angle = - self.angle
                
                

            if self.y > height - self.size:
                self.y = 2*(height - self.size) - self.y
                self.angle = math.pi - self.angle
                
                

            elif self.y < self.size:
                self.y = 2*self.size - self.y
                self.angle = math.pi - self.angle
                
                
def addPokemon():
    p = Pokemon(randomLocation(False),randomLocation(True))
    p.load(randomFilename())
    p.speed = random.random()
    p.angle = random.uniform(0,math.pi*2)
    return p;
    


backgroundColor = (randomBackground(),randomBackground(),randomBackground())


screen = pygame.display.set_mode(screenSize)
pygame.display.set_caption("Pokemon Forever.")
screen.fill(backgroundColor)

#load the icon
icon = pygame.Surface((pixelDimensions,pixelDimensions))
icon = pygame.image.load("pokeball.png").convert_alpha()
pygame.display.set_icon(icon)


#start the image array
for n in range(MAXpokemonArraySize):
    pokemon.append(addPokemon())


while 1:

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    
    screen.fill(backgroundColor)
    for i, Pokemon in enumerate(pokemon):
        screen.blit(Pokemon.image,(Pokemon.x,Pokemon.y))
        Pokemon.move()
        Pokemon.bounce()
     

    pygame.display.flip()

pygame.quit
sys.exit()