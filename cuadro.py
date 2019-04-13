import pygame
import Pyro4
import pickle

@Pyro4.expose
@Pyro4.behavior(instance_mode="single")
class Cuadro(object):

  def __init__(self):
    self.image = pygame.Surface((100,100))
    self.image.fill((0,0,255))
    self.rectangulo = self.image.get_rect()
    self.rectangulo.x = 100
    self.rectangulo.y = 100
    self.speed = 1
    self.imageString = ""

  def move(self, xdir, ydir):
    print('------Called MOVE()------')
    self.rectangulo.x += xdir*self.speed
    self.rectangulo.y += ydir*self.speed
    self.image.fill((255,0,0))

  def getimage(self):

    objtr = ""

    try:
        objtr = pygame.image.tostring(image, "RGB")
    except Exception as e:
        print(str(e))

    return objtr

  def getrectangulo(self):
    return pygame.image.toString(image, "RGB")

  def getspeed(self):
      return self.speed
