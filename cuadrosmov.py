import pygame, sys, Pyro4
from pygame.locals import *
from cuadro import Cuadro
import objectsConstantName

def main():
    miCuadro = Pyro4.Proxy("PYRONAME:"+objectsConstantName.CUADRO_REFERENCE)

    ventana = pygame.display.set_mode((1000, 600))
    pygame.display.set_caption("Salomon OS")

    gameisExecuting = True

    while gameisExecuting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameisExecuting = False

        #Update window frames cleaning up
        ventana.fill((255,255,255))

        #get the current active key
        activeKey = pygame.key.get_pressed()

        #Close with x
        if activeKey[pygame.K_x]:
            gameisExecuting = False

        if activeKey[pygame.K_RIGHT]:
            miCuadro.move(1,0)
        elif activeKey[pygame.K_LEFT]:
            miCuadro.move(-1,0)
        elif activeKey[pygame.K_UP]:
            miCuadro.move(0,-1)
        elif activeKey[pygame.K_DOWN]:
            miCuadro.move(0,1)

        try:
            imgn = pygame.image.fromstring(miCuadro.getimage(), "RGB")
            print('Si se pudo recibir la imagen')
        except:
            pass
            ##print('Error al convertir a imagen ')

        try:
            rectangulopt = pygame.image.fromstring(miCuadro.getrectangulo(), "RGB")
            print("Si se pudo recibir la imagenss")
        except:
            pass
            #print('Error al convertir a rectangulo')

        #ventana.blit(miCuadro.getimage(), miCuadro.getrectangulo())
        pygame.display.update()

    pygame.quit()
    quit()

if __name__ == "__main__":
    main()
