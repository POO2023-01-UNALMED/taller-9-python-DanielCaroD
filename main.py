from tkinter import Tk, Button, Entry

# Configuración ventana principal
root = Tk()
root.title("Calculadora POO")
root.resizable(0,0)
root.geometry("295x255")

# Configuración pantalla de salida 
pantalla = Entry(root, width=40, bg="black", fg="white", borderwidth=0, font=("arial", 18, "bold"))
pantalla.grid(row=0, column=0, columnspan=377, padx=1, pady=1)

# Configuración botones
boton_1 = Button(root, text="1", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2"); boton_1.grid(row=1, column=0, padx=1, pady=1)
boton_2 = Button(root, text="2", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2"); boton_2.grid(row=1, column=1, padx=1, pady=1)
boton_3 = Button(root, text="3", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2"); boton_3.grid(row=1, column=2, padx=1, pady=1)
boton_4 = Button(root, text="4", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2"); boton_4.grid(row=2, column=0, padx=1, pady=1)
boton_5 = Button(root, text="5", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2"); boton_5.grid(row=2, column=1, padx=1, pady=1)
boton_6 = Button(root, text="6", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2"); boton_6.grid(row=2, column=2, padx=1, pady=1)
boton_7 = Button(root, text="7", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2"); boton_7.grid(row=3, column=0, padx=1, pady=1)
boton_8 = Button(root, text="8", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2"); boton_8.grid(row=3, column=1, padx=1, pady=1)
boton_9 = Button(root, text="9", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2"); boton_9.grid(row=3, column=2, padx=1, pady=1)
boton_igual = Button(root, text="=", width=20, height=3, bg="red", fg="white", borderwidth=0, cursor=" hand2"); boton_igual.grid(row=4, column=0, columnspan=2, padx=1, pady=1)
boton_punto = Button(root, text=".", width=9, height=3, bg="spring green", fg="black", cursor="hand2", borderwidth=0); boton_punto.grid(row=4, column=2, padx=1, pady=1)
boton_mas = Button(root, text="+", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2"); boton_mas.grid(row=1, column=3, padx=1, pady=1)
boton_menos = Button(root, text="-", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2"); boton_menos.grid(row=2, column=3, padx=1, pady=1)
boton_multiplicacion = Button(root, text="*",  width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2"); boton_multiplicacion.grid(row=3, column=3, padx=1, pady=1)
boton_division = Button(root, text="/", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2"); boton_division.grid(row=4, column=3, padx=1, pady=1)

# Configuración de operaciones
botones = [boton_1, boton_2, boton_3, boton_4, boton_5, boton_6, boton_7, boton_8, boton_9]
operaciones = [boton_mas, boton_menos, boton_multiplicacion, boton_division]; simbolos = ["+", "-", "*", "/"]
n1 = ""; simb = ""; np = False; sm = False

def numero(evento):
    global n1, np, sm
    if np == True : pantalla.delete(0, "end"); np = False
    numero = evento.widget.cget("text")
    pantalla.insert("end", numero)
    n1 += numero; sm = True

def comb(evento):
    global n1, simb, sm
    if sm == True:
        simbolo = evento.widget.cget("text")
        if simb == "": n1 += simbolo
        else: 
            pantalla.delete(len(n1) - 1, "end")
            n1 = n1[:-1] + simbolo
        pantalla.insert("end", simbolo)
        simb = simbolo

def punto(evento):
    global n1, simb
    num = n1
    if simb != "": num = n1.split(simb)[-1]
    if "." not in num:
        pantalla.insert("end", ".")
        n1 += "."

def igual(evento):
    global n1, simb, np, sm
    resultado = eval(n1) + 0.0
    pantalla.delete(0, "end"); pantalla.insert("end", resultado)
    n1 = ""; simb = ""; np = True; sm = False

for boton in botones:
    boton.bind("<Button-1>", numero)
for operacion in operaciones:
    operacion.bind("<Button-1>", comb)
boton_punto.bind("<Button-1>", punto)
boton_igual.bind("<Button-1>", igual)

root.mainloop()

