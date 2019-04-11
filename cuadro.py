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

   def move(self, xdir, ydir):
       self.rectangulo.x += xdir*self.speed
       self.rectangulo.y += ydir*self.speed
       self.image.fill((255,0,0))

   def getimage(self):
       return self.image

   """def __getstate__(self):
       state = self.__dict__.copy()
       surface = state.pop("surface")
       state["surface-string"] = (pygame.image.tostring(surface, "RGB"). surface.get:size())
       return state

   def __setstate__(self,state):
       surface_string, size = state.pop("surface_string")
       state["surface"] = pygame.image.fromString(surface_string, size, "RGB")
       self.__dict__.update(state)"""



   def getrectangulo(self):
       return self.rectangulo
  
   def getspeed(self):
       return self.speed


  


