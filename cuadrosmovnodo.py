from __future__ import print_function
from cuadro import Cuadro
import Pyro4
import pygame, sys
import objectsConstantName

def main():

  Pyro4.Daemon.serveSimple(
    {
      Cuadro: "cuadroNodo"
    },
    ns = True, host="192.168.0.7"
  )

  #Added this

  for i in range (0,3):
    print(i)
   
  daemon = Pyro4.Daemon()
  ns = Pyro4.locateNS()
  uriMiCuadro = daemon.register(Cuadro)
  ns.register(objectsConstantName.CUADRO_REFERENCE, uriMiCuadro)
  print("Uri " + str(uriMiCuadro))
  daemon.requestLoop()

if __name__ == "__main__":
   main()


