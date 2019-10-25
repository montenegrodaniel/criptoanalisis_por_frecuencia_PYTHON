#!/usr/bin/python
# -*- coding: utf8 -*-
import os, sys

def funceuler(primo):    ####funcion funceuler recibe un valor
  v_1=int(primo) ##convierte la entrada en  un entero
  i=2 #inicia la variable i = 2
  res=(i**(v_1-1)) %v_1 #aplica la formula de euler 
  print ("\tResultado Aplicando teorema de Euler = ",res) #imprime el resultado 
  if (res == 1):    #si el resultado es igual a 1 el numero es primo 
      print("\t\t -el numero es primo")
  else:    
      print("\t\t -el numero no es primo")    

