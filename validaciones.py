#!/usr/bin/python
# -*- coding: utf8 -*-
import ayuda################
import archivo################
import euclides################
import criba################               IMPORTA LOS ARCHIVOS QUE VAMOS A UTILIZAR PARA PODER LLAMAR SUS FUNCIONES 
import fermat################
import euler################
import cesar################
import frecuencia################
from time import time ## importa la libreria time para calcular tiempos de ejecución


def validacionFrecuencia(argumentos): #funcion validacionFrecuencia recibe el argumento de entrada en consola
	if(len(argumentos)!=3):## pregunta si la posisicion del argumento de entrada es diferente de tamaño 3
		print ("\nEl número de parámetros es incorrecto")
		print ("Revisar la ayuda del algoritmo de criptoanalisis por frecuencia: python3 proyecto.py -fre\n")
	else:
		f = archivo.abrirArchivo(argumentos[2]) #llama la funcion abrirArchivo  del archivo "archivo" y iguala la posisicion 2 del argumento en la variable f
		if f=='':
			print ('No se encontro el archivo '+argumentos[2])
		else:
			texto = ""
			nomArchivoDec = argumentos[2].replace('.cif', '.dec')##TOMA el valor de argumentos en la posicion 2 y reemplaza por la extension .cif o .dec
			for pal in f.readlines():#lee las lineas del archivo  recorre la cadena de texto
				texto=texto+pal 
			f.close()
			start_time = time() #inicializa el tiempo de ejecucion del script
			frecuencia.analisisFrecuencia(texto, nomArchivoDec)#llama la funcion  analisisFrecuencia en el archivo frecuencia.py y le envia las variables texto y nomArchivoDec
			elapsed_time = time() - start_time #finaliza el tiempo de ejecucion del script
			print("Tiempo transcurrido: %.10f segundos." % elapsed_time) #imprime el tiempo de ejecucion total del script

######***************/////////////// EUCLIDES FUNCIONANDO ******************///////////////////////////
def validacioneuclides(argumentos): #funcion de validacioneuclides recibe el argumento de entrada en consola
	if(len(argumentos)==4):# pregunta si el tamaño del argumento de entrada es 4
		if(argumentos[1]=="-teu"):#pregunta si la posicion 1 del argumento de entrada es -teu
			start_time = time()#inicializa el tiempo de ejecucion del script
			euclides.eucExt(argumentos[2],argumentos[3])#llama a la funcion eucExt del archivo euclides y le envia dos parametros 
			elapsed_time = time() - start_time#finaliza el tiempo de ejecucion del script
			print("Tiempo transcurrido: %.10f segundos." % elapsed_time)#imprime el tiempo de ejecucion total del script
		
		else: 
				print ("\nEl modo ",argumentos[2]," es incorrecto")
				print ("Revisar la ayuda del algoritmo de Mascara Rotativa: python3 principal.py -mr\n")
		
	else:
		
			print ("\nEl número de parámetros es incorrecto")
			print ("Revisar la ayuda del algoritmo de Mascara Rotativa: python3 principal.py -mr\n")
################********////////HASTA AQUI EUCLIDES*************////////////////////////////

######***************/////////////// criba ******************///////////////////////////
def validacioncriba(argumentos):
	if(len(argumentos)==3):
		if(argumentos[1]=="-cre"):
			start_time = time()#inicializa el tiempo de ejecucion del script
			criba.eratostenes(2,argumentos[2])#llama a la funcion eratostenes del archivo criba
			elapsed_time = time() - start_time#imprime el tiempo de ejecucion total del script
			print("\nTiempo transcurrido: %.10f segundos." % elapsed_time)#imprime el tiempo de ejecucion total del script
		else:
			print("¡¡¡¡Revisar ayuda de sintaxis, numero inferior es mayor al numero superior!!!!")
		
	else:
		print ("\nEl número de parámetros es incorrecto")
		print ("Revisar la ayuda del algoritmo de Criba de Eratosthenes\n")
################********//////// fin criba*************////////////////////////////

######***************/////////////// inicio fermat  ******************///////////////////////////
def validaciofermat(argumentos):
	if(len(argumentos)==3):
		if(argumentos[1]=="-tof"):
			start_time = time()
			fermat.revisionprimos(argumentos[2])
			elapsed_time = time() - start_time
			print("\nTiempo transcurrido: %.10f segundos." % elapsed_time)
				
		else: 
				print ("\nEl modo ",argumentos[2]," es incorrecto")
				print ("Revisar la ayuda del algoritmo de Criba de Eratosthenes\n")
		
	else:
		
			print ("\nEl número de parámetros es incorrecto")
			print ("Revisar la ayuda del algoritmo de Criba de Eratosthenes\n")
################********//////// fin fermat*************////////////////////////////

######***************/////////////// inicio EULER  ******************///////////////////////////
def validacioneuler(argumentos):
	if(len(argumentos)==3):
		if(argumentos[1]=="-ale"):
			start_time = time()
			euler.funceuler(argumentos[2])
			elapsed_time = time() - start_time
			print("\nTiempo transcurrido: %.10f segundos." % elapsed_time)
				
		else: 
				print ("\nEl modo ",argumentos[2]," es incorrecto")
				print ("Revisar la ayuda del algoritmo de Criba de Eratosthenes\n")
		
	else:
		
			print ("\nEl número de parámetros es incorrecto")
			print ("Revisar la ayuda del algoritmo de Criba de Eratosthenes\n")
################********//////// fin EULER*************////////////////////////////

######################## INICIO CIFRADO CESAR########################
def validacioncesar(argumentos):
	texto = ""
	if(len(argumentos)==6):
		if(argumentos[5]=="-c64"):
			if(argumentos[2]=="-c"):
				f = archivo.abrirArchivo64(argumentos[3])
				if f=='':
					print ('No se encontro el archivo '+argumentos[3])
				else:
					texto = f
					clave = cesar.obtenerEntero(argumentos[4])
					if(clave != -1):
						start_time = time()
						cesar.cifrarCesar(texto, clave, argumentos[3]+".cif", "-c64")
						elapsed_time = time() - start_time
						print("Tiempo transcurrido: %.10f segundos." % elapsed_time)
			elif(argumentos[2]=="-d"):
				f = archivo.abrirArchivo(argumentos[3])
				if f=='':
					print ('No se encontro el archivo '+argumentos[3])
				else:
					for pal in f.readlines():
						texto=texto+pal
					f.close()
					clave = cesar.obtenerEntero(argumentos[4])
					nomArchivoDec = argumentos[3].replace('.cif', '.dec')
					if(clave != -1):
						start_time = time()
						cesar.descifrarCesar(texto, clave, nomArchivoDec,"-c64")
						elapsed_time = time() - start_time
						print("Tiempo transcurrido: %.10f segundos." % elapsed_time)				
		else:
			print("Si deseas codificar o decodificar usa la bandera -c64 en lugar de ",argumentos[5])
	else:
		if(len(argumentos)!=5):
			print ("\nEl número de parámetros es incorrecto")
			print ("Revisar la ayuda del algoritmo de cesar: python3 principal.py -sc\n")
		else:
			if(argumentos[2]=="-c"):
				f = archivo.abrirArchivo(argumentos[3])
				if f=='':
					print ('No se encontro el archivo '+argumentos[3])
				else:
					for pal in f.readlines():
						texto=texto+pal
					f.close()
					clave = cesar.obtenerEntero(argumentos[4])
					if(clave != -1):
						start_time = time()
						cesar.cifrarCesar(texto, clave, argumentos[3]+".cif", "")
						elapsed_time = time() - start_time
						print("Tiempo transcurrido: %.10f segundos." % elapsed_time)
			elif(argumentos[2]=="-d"):
				f = archivo.abrirArchivo(argumentos[3])
				if f=='':
					print ('No se encontro el archivo '+argumentos[3])
				else:
					for pal in f.readlines():
						texto=texto+pal
					f.close()
					clave = cesar.obtenerEntero(argumentos[4])
					nomArchivoDec = argumentos[3].replace('.cif', '.dec')
					if(clave != -1):
						start_time = time()
						cesar.descifrarCesar(texto, clave, nomArchivoDec, "")
						elapsed_time = time() - start_time
						print("Tiempo transcurrido: %.10f segundos." % elapsed_time)
			else: 
				print ("\nEl modo ",argumentos[2]," es incorrecto")
				print ("Revisar la ayuda del algoritmo de cesar: python3 principal.py -sc\n")
####################### FIN CIFRADO CESAR#######################################################################################
		
