#!/usr/bin/python
# -*- coding: utf8 -*-
import os, sys

def eratostenes(valor,valor1): ## funcion eratostenes recibe dos valores
  i_v=int(valor) ## convertimos el valor de entrada en entero y lo igualamos a la variale i_v
  iv1=int(valor1)
  multiplos = set()
  for i in range(i_v, iv1+1):#se recorre  i en el rango de los valores de entrada
    if i not in multiplos:#pregunta si i no es multiplo
      print("[",i,"]", end=";") #imprimimos cada numero encontrado en la criba
      multiplos.update(range(i*i, iv1+1, i))#actualiza los valores encontrados


