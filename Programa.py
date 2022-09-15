from tkinter import *
import random
from turtle import bgcolor 
  
Raíz = Tk()

Raíz.geometry("500x500") 
  
Raíz.title("Juego Piedra, Papel ó Tijera: ") 
  
Valor_PC ={
    "0":"Piedra", 
    "1":"Papel", 
    "2":"Tijeras"} 
  
def reset_game(): 
    b1["Estado"] = "Activo"
    b2["Estado"] = "Activo"
    b3["Estado"] = "Activo"
    l1.config(text = "Jugador              ") 
    l3.config(text = "PC") 
    l4.config(text = "") 
  
def button_Inactivo(): 
    b1["Estado"] = "Inactivo"
    b2["Estado"] = "Inactivo"
    b3["Estado"] = "Inactivo"
  
def isPiedra(): 
    c_v = Valor_PC[str(random.randint(0,2))] 
    if c_v == "Piedra": 
        Resultado = "¡Empate!"
    elif c_v=="Tijeras": 
        Resultado = "¡Jugador Gana!"
    else: 
        Resultado = "¡PC Gana!"
    l4.config(text = Resultado) 
    l1.config(text = "Piedra            ") 
    l3.config(text = c_v) 
    button_Inactivo() 
  
def isPapel(): 
    c_v = Valor_PC[str(random.randint(0, 2))] 
    if c_v == "Papel": 
        Resultado = "¡Empate!"
    elif c_v=="Tijeras": 
        Resultado = "¡PC Gana!"
    else: 
        Resultado = "¡Jugador Gana!"
    l4.config(text = Resultado) 
    l1.config(text = "Papel           ") 
    l3.config(text = c_v) 
    button_Inactivo() 
  
def isTijeras(): 
    c_v = Valor_PC[str(random.randint(0,2))] 
    if c_v == "Piedra": 
        Resultado = "¡PC Gana!"
    elif c_v == "Tijeras": 
        Resultado = "¡Empate!"
    else: 
        Resultado = "¡Jugador Gana!"
    l4.config(text = Resultado) 
    l1.config(text = "Tijeras         ") 
    l3.config(text = c_v) 
    button_Inactivo() 
  
Label(Raíz, 
      text = "Piedra Papel Tijeras", 
      font = "normal 20 bold", 
      fg = "blue").pack(pady = 20) 
  
frame = Frame(Raíz) 
frame.pack() 
  
l1 = Label(frame, 
           text = "Jugador              ", 
           font = 10) 
  
l2 = Label(frame, 
           text = "VS             ", 
           font = "normal 10 bold") 
  
l3 = Label(frame, text = "PC", font = 10) 
  
l1.pack(side = LEFT) 
l2.pack(side = LEFT) 
l3.pack() 
  
l4 = Label(Raíz, 
           text = "", 
           font = "normal 20 bold", 
           bg = "white", 
           width = 15 , 
           borderwidth = 2, 
           relief = "solid") 
l4.pack(pady = 20) 
  
frame1 = Frame(Raíz) 
frame1.pack() 
  
b1 = Button(frame1, text = "Piedra", 
            bg = "Yellow" ,
            font = 10, width = 7, 
            command = isPiedra) 
  
b2 = Button(frame1, text = "Papel ", 
            bg = "Blue" ,
            font = 10, width = 7, 
            command = isPapel) 
  
b3 = Button(frame1, text = "Tijeras", 
            bg = "red" ,
            font = 10, 
            width = 7,
            command = isTijeras)
            

  
b1.pack(side = LEFT, padx = 10) 
b2.pack(side = LEFT,padx = 10) 
b3.pack(padx = 10) 
  
Button(Raíz, text = "Reset Game", 
       font = 10, fg = "red", 
       bg = "black", command = reset_game).pack(pady = 20) 
  
Raíz.mainloop()