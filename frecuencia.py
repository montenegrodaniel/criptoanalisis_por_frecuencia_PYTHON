#!/usr/bin/python
# -*- coding: utf8 -*-
import os, sys
import archivo############
import alfabeto############ IMPORTA ARCHIVOS
import operator###########

TAM_ALFABETO = alfabeto.tamAlfabeto()#iguala el tamaño del alfabeto
abc = alfabeto.getAlfabeto()#iguala a la funcion getAlfabeto
frecuAlta = ['E','A','S','O', 'I', 'N', 'R', 'D', 'T']## definicion de frecuencias altas

	
def analisisFrecuencia(criptograma, nomArchivoSalida): ## funcion analisisFrecuencia recibe dos parametros
	listaFrecu = frecuencias(criptograma)# recibe e iguala criptograma de la funcion frecuencias en la variable listaFrecu
	k = verificarHipostesis(listaFrecu)### recibe la clave de la funcion verificarHipotesis 
	print ('La clave con la que se cifró es: ',k) ###imprime la clave con la que se cifro
	mensajeClaro = ""
	i=0
	while (i < len(criptograma)): #mientras i sea menor que el criptograma
		ci = alfabeto.getPosicion(criptograma[i]) #llama funcion getPosicion de archivo alfabeto y le iguala el valor de criptograma[i] a la variable ci
		modulo = (ci-k)%TAM_ALFABETO #aplica formula de cesar y la iguala a variable modulo
		mensajeClaro = mensajeClaro + abc[modulo]#mensajeclaro se iguala al mensajeclaro + variable abc posicion modulo
		i+=1 #aumenta el contador i
	f = archivo.escribirArchivo(nomArchivoSalida,mensajeClaro) #llama a la funcion escribir Archivo de el archico "archico.py" recibe dos parametros y los iguala a f
	if f=='':
		print ('Ocurrio un error al intentar escribir en', nomArchivoSalida)
	else:
		print ('El mensaje descifrado se guardo correctamente en',nomArchivoSalida)
	#print mensajeClaro
		
		
def verificarHipostesis(listaFrecu): #funcion para verificar la hipotesis y calcular k y k'
	K = 0
	k1 = 0
	k2 = 0
	for i in frecuAlta:#ciclo de i en frecuAlta
		for j in frecuAlta:#ciclo de j en frecuAlta
			if (i!=j):#pregunta si i es diferente a j
				k1 = encontrarK(i, listaFrecu[0][0]) #k1 lo iguala a la funcion encontrarK con sus valores recibidos
				k2 = encontrarK(j, listaFrecu[1][0])
				if(k1==k2):#pregunta si k1 = k2
					return k1 #retorna k1
					break
				else:#intercambia las hipotesis ahora k1 es igual a j y k2 igual a i
					k1 = encontrarK(j, listaFrecu[0][0])
					k2 = encontrarK(i, listaFrecu[1][0])
					if(k1==k2):
						return k1
						break


def encontrarK(letraMi, letraCi):#funcion para encontrark
	mi = alfabeto.getPosicion(letraMi)#toma  la letra en el alfabeto
	ci = alfabeto.getPosicion(letraCi)#toma la letra cifrada del texto
	return (ci-mi)%TAM_ALFABETO#retorna la formula para aencontrar k

def contar(letra, texto): #funcion contar
	contador = 0
	i = 0
	while (i < len(texto)):#mientrar i sea menor que texto (variable recibida)
		if texto[i] == '\xc3' or texto[i] == '\xc2':
			caracter = texto[i] + texto[i + 1] #caracter lo iguala a texto en psicion i + texto en la siguiente posicion
			i+=1 #aumento de contador
		else:
			caracter = texto[i]
		if caracter == letra:
				contador = contador + 1
		i+=1
	return contador

def frecuencias(texto):#FUNCIONFRECUENCIAS RECIBE EL TEXTO
	listaFrecuencias = {}
	i = 0
	while (i < len(abc)):
		n = contar(abc[i],texto) #cuenta los caracteres en el texto
		if (n != 0):
			listaFrecuencias[abc[i]] = n
		i+=1
	resultado =  sorted(listaFrecuencias, key=listaFrecuencias.get, reverse=True)
	print ('primer letra con mas frecuencia en el criptograma  : %s **************************************'% resultado[0]) ###
	print ('segunda letra con mas frecuencia en el criptograma : %s ******************************'% resultado[1])####
	print ('tercer letra con mas frecuencia en el criptograma  : %s ********************'% resultado[2])###         IMPRIME LOS PRIMERO 4 CARACTERES CON MAYOR FRECUENCIA EN EL CRIPTOGRAMA
	print ('cuarta letra con mas frecuencia en el criptograma  : %s ************'% resultado[3])###
	return resultado	

