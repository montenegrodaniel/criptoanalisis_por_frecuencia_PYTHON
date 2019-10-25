#!/usr/bin/python
# -*- coding: latin-1 -*-
import os, sys
import ayuda #se importa el archivo ayuda.py para poder llamar sus funciones
import validaciones #importamos el archivo validaciones.py para poder llamar sus funciones
import alfabeto #se importa el archivo alfabeto.py

numArg=len(sys.argv) #captura el argumento de entrada en la consola
arg=sys.argv


if(numArg==1): #pregunta si la entrada del argumento es de tamaño 1 
	ayuda.ayudaPrincipal() #llama al archivo ayuda.py y la funcion ayudaPrincipal()
elif(numArg==2): #pregunta si la entrada del argumento es de tamaño 2 y continua al siguiente if
	if(arg[1]=="-fre"): #si la entrada del argumento en la posicion 1 es "-fre" 
		ayuda.ayudaFrecuencia() #llama a la funcion ayudaFrecuencia del archivo ayuda.py
	elif(arg[1]=="-tof"):#si la entrada del argumento en la posicion 1 es "-tof" 
		ayuda.ayudafermat() #llama a la funcion ayudafermat del archivo ayuda.py
	elif(arg[1]=="-teu"):
		ayuda.ayudaeuclides()
	elif(arg[1]=="-cre"):
		ayuda.ayudacriba()
	elif(arg[1]=="-ces"):
		ayuda.ayudacesar()
	elif(arg[1]=="-ale"):
		ayuda.ayudaeuler()
        
	else:#si no tiene el tamaño de los argumentos  imprime la siguiente linea:
		print ("EL ALGORIMO QUE DIGITÓ NO ES UNA OPCION VÁLIDA") 
else:	
	if(arg[1]=="-fre"):#si la entrada del argumento en la posicion 1 es "-fre"
		validaciones.validacionFrecuencia(arg)#llama a la funcion validacionFrecuencia del archivo validaciones y le envia el argumento
	elif(arg[1]=="-tof"):
		validaciones.validaciofermat(arg)
	elif(arg[1]=="-teu"):
		validaciones.validacioneuclides(arg)
	elif(arg[1]=="-cre"):
		validaciones.validacioncriba(arg)
	elif(arg[1]=="-ces"):
		validaciones.validacioncesar(arg)
	elif(arg[1]=="-ale"):
		validaciones.validacioneuler(arg)
        
	else:
		print ("EL COMANDO QUE DIGITÓ NO ES UNA OPCION VÁLIDA")

