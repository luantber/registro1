#!/usr/bin/env python
# -*- coding: utf-8 -*
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import win32com.client
win32com.client.gencache.is_readonly=False
win32com.client.gencache.GetGeneratePath()
from data2 import *
#---------------------------------------------MAIN-----------------------------------------
excel = win32com.client.Dispatch('Excel.Application')
wb = excel.Workbooks.Open(r'C:\Users\LuisAntonio\Desktop\proyecto2\reg01.xlsx')
print "Conectado con Excel"
'''except:
	ex = str(input("Path"))
	wb = excel.Workbooks.Open(r'C:'+ex)'''
excel.Visible=True
ws = wb.Worksheets("base")
###################
print "Conectado con 'base'"
def limpiar():
	n = wb.Worksheets.Count
	wb.Application.DisplayAlerts = False
	for x in range(n-1-11):
		wb.Worksheets(12).Delete()

def bim(b,c):
	ws.Range("AB1").Value=b
	ws.Range("AH1").Value=c
	wb.Save
	print "Llenando Bimestre y Ciclo"

def generarhoja(id):
	global wb
	wb.Worksheets("base").Copy(After=wb.Worksheets(wb.Worksheets.Count))
	#wb.Worksheets("base").Copy(After=wb.Worksheets(wb.Worksheets.Count))
	print "Copia Realizada"
	wb.Worksheets("base (2)").Range("E1").Value=curso(id)
	wb.Worksheets("base (2)").Range("B2").Value=competencia(id)
	wb.Worksheets("base (2)").Range("B3").Value=descripcion(id)

	wb.Worksheets("base (2)").Range("B6").Value=capacidades(id)[0]
	wb.Worksheets("base (2)").Range("H6").Value=capacidades(id)[1]
	wb.Worksheets("base (2)").Range("N6").Value=capacidades(id)[2]
	wb.Worksheets("base (2)").Range("T6").Value=capacidades(id)[3]
	wb.Worksheets("base (2)").Range("Z6").Value=capacidades(id)[4]
	wb.Worksheets("base (2)").Range("AF6").Value=capacidades(id)[5]

	
	wb.Worksheets("base (2)").Range("B7:F7").Value=indicadores(id)[0]
	wb.Worksheets("base (2)").Range("H7:L7").Value=indicadores(id)[1]
	wb.Worksheets("base (2)").Range("N7:R7").Value=indicadores(id)[2]
	wb.Worksheets("base (2)").Range("T7:X7").Value=indicadores(id)[3]
	wb.Worksheets("base (2)").Range("Z7:AD7").Value=indicadores(id)[4]
	wb.Worksheets("base (2)").Range("AF7:AJ7").Value=indicadores(id)[5]
	


	wb.Worksheets("base (2)").Name=curso(id)+str(id)
	print "nombre cambiado"
#### MAIN
limpiar()
print "limipado ..."
for i in contar():
	try:
		generarhoja(i)
	except:
		pass
		
print "Terminado"
wb.Close(SaveChanges=1)
#wb.SaveAs('reg01.xlsx')
excel.Application.Quit()
