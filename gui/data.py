#!/usr/bin/env python
# -*- coding: utf-8 -*
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import sqlite3

class base():
	def __init__(self):
		self.conn = sqlite3.connect('base.sqlite')
	def get_cursos(self):
		cursor = self.conn.execute("SELECT Distinct curso  from cursos")
		cs = []
		for x in cursor:
			cs.append(str(x[0]))
		return cs
	def get_competencias(self,i):
		cad = "SELECT competencia from cursos where curso= '" + i + "'"
		cursor = self.conn.execute(cad)
		cs = []
		for x in cursor:
			cs.append(x[0])
		return cs

	def get_descripcion(self,i):
		cad = "SELECT descripcion from cursos where competencia= '" + i + "'"
		cursor = self.conn.execute(cad)
		for x in cursor:
			return x[0]

	def get_capacidad(self,i,n):
		cad = "SELECT cap"+str(n)+" from cursos where competencia='"+str(i)+"'"
		#print cad
		
		cursor = self.conn.execute(cad)
		for x in cursor:
			if x[0] == None:
				return ""
			else: 
				return x[0]

	def get_indicadores(self,i,item):
		cad = "SELECT i"+str(i) +" from cursos where competencia='"+item+"'"
		#print cad
		cursor = self.conn.execute(cad)

		for x in cursor:
			if x[0] == None:
				return ""
			else: 
				return x[0]

	def new_curso(self,new):
		#cursor = self.conn.execute("SELECT Distinct curso  from cursos")
		cad = "INSERT into cursos(curso) values ('" + str(new) + "')"
		#print cad
		cursor	= self.conn.execute(cad)
		self.conn.commit()

	def new_competencia(self,new,itemant):
		cad = "INSERT into cursos(curso,competencia) values ('" + str(itemant)+ "','"+str(new) + "')"
		#print cad
		cursor	= self.conn.execute(cad)
		self.conn.commit()

	def bv_competencia(self):
		cad = "delete from cursos where competencia is null"
		cursor	= self.conn.execute(cad)
		self.conn.commit()

	def up_descripcion(self,new,itemant):
		cad = "UPDATE cursos set descripcion='"+str(new)+"' where competencia='" + str(itemant) + "'"
		cursor	= self.conn.execute(cad)
		self.conn.commit()

	def up_capacidad(self,n,nuevoc,indic,itemant):
		cad = "update cursos set cap"+str(n)+"='"+nuevoc+"', i"+str(n)+ "='"+indic+"' where competencia ='"+str(itemant)+"'"
		#print cad
		cursor	= self.conn.execute(cad)
		self.conn.commit()

#bases = base()
#print bases.get_indicadores(2,"Comprensión Oral")		