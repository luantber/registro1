#!/usr/bin/env python
# -*- coding: utf-8 -*
import sys
reload(sys)
sys.setdefaultencoding("utf-8")


import sqlite3

conn = sqlite3.connect('base.sqlite')
def curso(id):
	cad = "SELECT curso from cursos where idcurso="+str(id)
	#print cad
	cursor = conn.execute(cad)
	for x in cursor:
		return x[0]

def descripcion(id):
	cad = "SELECT descripcion from cursos where idcurso="+str(id)
	#print cad
	cursor = conn.execute(cad)
	for x in cursor:
		if x[0]==None:
			return ""
		else:
			return x[0]

def competencia(id):
	cad = "SELECT competencia from cursos where idcurso="+str(id)
	#print cad
	cursor = conn.execute(cad)
	for x in cursor:
		if x[0]==None:
			return ""
		else:
			return x[0]

def capacidades(id):
	def get_capacidad(i):
		cad = "SELECT cap"+str(i)+" from cursos where idcurso="+str(id)
			
		cursor = conn.execute(cad)
		for x in cursor:
			if x[0] == None:
				return ""
			else: 
				return x[0]

	xs = []
	for i in range(1,7):
		xs.append(get_capacidad(i))

	return xs

def indicadores(id):
	def get_indicador(i):
		cad = "SELECT i"+str(i)+" from cursos where idcurso="+str(id)
			
		cursor = conn.execute(cad)
		for x in cursor:
			if x[0] == None:
				return []
			else: 
				cad = unicode(str(x[0]))
				cad = cad.split("\n")
				#print cad
				return cad

	xs = []
	for i in range(1,7):
		xs.append(get_indicador(i))

	for a in xs:
		cant = len(a)
		for b in range(5-cant):
			a.append("")

	return xs

def contar():
	cad = "SELECT idcurso from cursos"
	cursor = conn.execute(cad)
	xs = []
	for x in cursor:
		#print str(x[0]) + " cursos encontrados"
		xs.append(x[0])

	return xs
	
def refresh():

	cad ="UPDATE cursos set idcurso="+str(n)

indicadores(2)[1]
print "------"
