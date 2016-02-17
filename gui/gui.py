#!/usr/bin/env python
# -*- coding: utf-8 -*
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

from Tkinter import *
from data import *
itemfortwo = ""
itemfortres = ""
frame = Tk()
#
l1 = Label(frame,text="Cursos:")
l2 = Label(frame,text="Dominio:")
l3 = Label(frame,text="Competencia:")
l4 = Label(frame,text="Capacidades:")
l5 = Label(frame,text="Indicadores:")
#PARte 1
scrollbar2 = Scrollbar(frame, orient=VERTICAL)
listbox2 = Listbox(frame, height=3,yscrollcommand=scrollbar2.set)
scrollbar2.config(command=listbox2.yview)

scrollbar = Scrollbar(frame, orient=VERTICAL)
listbox = Listbox(frame, height=3,yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

text = Text(frame,width=60,height=4)

button = Button(frame,width=20,height=3,text="Generar")
###################################################
#-----------------Parte edicion--------------------
btnNuevoCurso = Button(frame,text="Nuevo")
txtCurso = Entry(frame)

btnNuevoCompetencia = Button(frame,text="Nuevo")
txtCompetencia = Entry(frame)

btnGuardarD = Button(frame,text="Guardar",width=15,height=2)

txtCap1 = Entry(frame)
textI1 = Text(frame,width=60,height=8)

txtCap2 = Entry(frame)
textI2 = Text(frame,width=60,height=8)

txtCap3 = Entry(frame)
textI3 = Text(frame,width=60,height=8)

txtCap4 = Entry(frame)
textI4 = Text(frame,width=60,height=8)

txtCap5 = Entry(frame)
textI5 = Text(frame,width=60,height=8)

txtCap6 = Entry(frame)
textI6 = Text(frame,width=60,height=8)

btnGuardarCs = Button(frame,text="Guadar Indicadores",width=15,height=2)

#################################################
#gridsss
l1.grid(row=0,column=0,sticky=N)
l2.grid(row=1,column=0,sticky=N)
l3.grid(row=2,column=0,sticky=N)
l4.grid(row=3,column=0,sticky=N)

listbox.grid(row=0,column=1,sticky=W+E)
scrollbar.grid(row=0,column=2,sticky=W+N+S)
listbox2.grid(row=1,column=1,pady=5,sticky=W+E)
scrollbar2.grid(row=1,column=2,sticky=W+N+S,pady=5)
text.grid(row=2,column=1)

button.grid(row=2,column=5,pady=5)
#########################
#----Columna -- 4---- 
txtCurso.grid(row=0,column=3)
btnNuevoCurso.grid(row=0,column=4)

txtCompetencia.grid(row=1,column=3)
btnNuevoCompetencia.grid(row=1,column=4)

btnGuardarD.grid(row=2,column=3)

#capacidades ... 
txtCap1.grid(row=3,column=1,sticky=W+E,pady=5)
textI1.grid(row=4,column=1)

txtCap2.grid(row=5,column=1,sticky=W+E,pady=5)
textI2.grid(row=6,column=1)

txtCap3.grid(row=7,column=1,sticky=W+E,pady=5)
textI3.grid(row=8,column=1)

btnGuardarCs.grid(row=8,column=3)
txtCap4.grid(row=3,column=5,sticky=W+E,pady=5)
textI4.grid(row=4,column=5)

txtCap5.grid(row=5,column=5,sticky=W+E,pady=5)
textI5.grid(row=6,column=5)

txtCap6.grid(row=7,column=5,sticky=W+E,pady=5)
textI6.grid(row=8,column=5)
#############################
bd = base()
def llenar():
	for item in bd.get_cursos():
	    listbox.insert(END,item)

llenar()

def limpiartodo():
	text.delete('1.0',END)
	listbox2.delete(0,END)
	
	txtCap1.delete(0,END)
	txtCap2.delete(0,END)
	txtCap3.delete(0,END)
	txtCap4.delete(0,END)
	txtCap5.delete(0,END)
	txtCap6.delete(0,END)
	textI1.delete('1.0',END)
	textI2.delete('1.0',END)
	textI3.delete('1.0',END)
	textI4.delete('1.0',END)
	textI5.delete('1.0',END)
	textI6.delete('1.0',END)


def lb1seleccionado(e):
	global itemfortwo
	limpiartodo()
	item = listbox.get(listbox.curselection()[0])
	for i in bd.get_competencias(item):
		listbox2.insert(END,i)
	itemfortwo = item

def lb2seleccionado(e):
	global itemfortres
	text.delete('1.0',END)
	item = listbox2.get(listbox2.curselection()[0])
	try:
		text.insert(END,bd.get_descripcion(item))
	except:
		pass
	itemfortres	= item

	txtCap1.delete(0,END)
	txtCap2.delete(0,END)
	txtCap3.delete(0,END)
	txtCap4.delete(0,END)
	txtCap5.delete(0,END)
	txtCap6.delete(0,END)

	txtCap1.insert(END,bd.get_capacidad(item,1))
	txtCap2.insert(END,bd.get_capacidad(item,2))
	txtCap3.insert(END,bd.get_capacidad(item,3))
	txtCap4.insert(END,bd.get_capacidad(item,4))
	txtCap5.insert(END,bd.get_capacidad(item,5))
	txtCap6.insert(END,bd.get_capacidad(item,6))

	textI1.delete('1.0',END)
	textI2.delete('1.0',END)
	textI3.delete('1.0',END)
	textI4.delete('1.0',END)
	textI5.delete('1.0',END)
	textI6.delete('1.0',END)

	textI1.insert(END,bd.get_indicadores(1,item))
	textI2.insert(END,bd.get_indicadores(2,item))
	textI3.insert(END,bd.get_indicadores(3,item))
	textI4.insert(END,bd.get_indicadores(4,item))
	textI5.insert(END,bd.get_indicadores(5,item))
	textI6.insert(END,bd.get_indicadores(6,item))

def generar():
	import generar
def refresh():
	listbox.delete(0,END)
	llenar()
	limpiartodo()

def nuevo_curso():
	new= txtCurso.get()
	bd.new_curso(new)
	refresh()
	listbox.focus_set()
	txtCurso.delete(0,END)
	listbox.selection_set(END)

def nuevo_competencia():
	new= txtCompetencia.get()
	#print itemfortwo
	bd.new_competencia(new,itemfortwo)
	listbox2.delete(0,END)
	#print itemfortwo
	for i in bd.get_competencias(itemfortwo):
		listbox2.insert(END,i)

	listbox2.focus_set()
	listbox2.selection_set(END)
	txtCompetencia.delete(0,END)
	bd.bv_competencia()

def up_descri():
	new = text.get('1.0',END)
	bd.up_descripcion(new,itemfortres)

def nuevo_capacidad():
	new = txtCapacidad.get()
	bd.new_competencia(new,
		)


##caps
def caps():
	xs = []
	xs.append([txtCap1.get(),textI1.get('1.0',END)])
	xs.append([txtCap2.get(),textI2.get('1.0',END)])
	xs.append([txtCap3.get(),textI3.get('1.0',END)])
	xs.append([txtCap4.get(),textI4.get('1.0',END)])
	xs.append([txtCap5.get(),textI5.get('1.0',END)])
	xs.append([txtCap6.get(),textI6.get('1.0',END)])

	n=1
	for x in xs:
		bd.up_capacidad(n,x[0],x[1],itemfortres)
		n+=1
############################
listbox.bind("<<ListboxSelect>>", lb1seleccionado)
listbox2.bind("<<ListboxSelect>>", lb2seleccionado)

button.config(command=generar)

btnNuevoCurso.config(command=nuevo_curso)
btnNuevoCompetencia.config(command=nuevo_competencia)

btnGuardarD.config(command=up_descri)

btnGuardarCs.config(command=caps)



mainloop()