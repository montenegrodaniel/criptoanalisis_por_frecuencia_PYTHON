#!/usr/bin/python
# -*- coding: utf8 -*-
import os, sys

def revisionprimos(primo):    ###funcion revisionprimos recibe un valor
  v_1=int(primo)##convierte la entrada en  un entero
  i=2 
  res=(i**(v_1-1)) %v_1 #aplica formula fermat
  print ("\tResultado Aplicando Fermat = ",res)###imprime el resultado
  if (res == 1):    #si el resultado es igual a 1 el numero es primo 
      print("\t\t -el numero es primo")
  else:    
      print("\t\t -el numero no es primo")    

