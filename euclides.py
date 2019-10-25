#!/usr/bin/python
# -*- coding: utf8 -*-
import os, sys



def eucExt(valor,valor1):#funcion eucExt recibe dos valores
 i_v=int(valor)#convierte la entrada en valores enteros y lo iguala a variable i_v
 iv1=int(valor1)
 r = [i_v,iv1]#vector posiciones de valores de entrada
 s = [1,0] ####   vectores para realizar calculos
 t = [0,1]###
 i = 1 #inicializamos variable i
 q = [[]]## vector vacio
 while (r[i] != 0): #haga mientras vecot r en posicion i sea diferente de 0
  q = q + [r[i-1] // r[i]]
  r = r + [r[i-1] % r[i]]
  s = s + [s[i-1] - q[i]*s[i]]
  t = t + [t[i-1] - q[i]*t[i]]
  i = i+1
 print(" el MCD de los numeros ingresados es: ",r[i-1]) # imprime el MCD el cual es la penultima posicion del vector r
 print("Demostracion:   ")
 print ("\t\t",r[i-1] , "=", i_v, "(",s[i-1],") +", iv1, "(",t[i-1], ")") #imprime la demostracion del MCD = valor ingresado * el inverso + segundo valor ingresado * su inverso
 return (r[i-1], s[i-1], t[i-1])

