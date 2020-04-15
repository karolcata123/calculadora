import tkinter as tk

root = tk.Tk()

numero_uno = tk.IntVar()
numero_dos = tk.IntVar()
resultado = tk.StringVar()

sw = True

def suma():
    a = numero_uno.get()
    b = numero_dos.get()
    c = a + b
    resultado.set(c)

def sum():
    print('h')

def resta():
    a = numero_uno.get()
    b = numero_dos.get()
    c = a - b
    resultado.set(c)
def multiplicacion():
    a = numero_uno.get()
    b = numero_dos.get()
    c = a * b
    resultado.set(c)
def division():
    a = numero_uno.get()
    b = numero_dos.get()
    c = a / b
    resultado.set(c)

root.geometry('310x290')
root.title('CALCULADORA')
root.configure(bg='black')

#Label
tk.Label(root, text='SEGUNDO NUMERO', bg="black", fg='white', font=('', 8)).place(x=100, y=5)
tk.Entry(root, justify='center', textvariable=numero_uno, font=('', 15)).place(x=50, y=30)
tk.Label(root, text='PRIMER NUMERO', bg="black", fg='white', font=('', 8)).place(x=100, y=65)
tk.Entry(root, justify='center', textvariable=numero_dos, font=('', 15)).place(x=50, y=80)
tk.Label(root, text='RESULTADO', bg="black", fg='white', font=('', 8)).place(x=120, y=250)
tk.Entry(root, justify='center', textvariable=resultado, font=('', 15)).place(x=50, y=220)


#Botones
tk.Button(root, text='+', bd=0, bg='red', font=('', 30), command=suma).place(x=30, y=130)


tk.Button(root, text='-', bd=0, bg='red', font=('', 30), command=resta).place(x=105, y=130)


tk.Button(root, text='*', bd=0, bg='red', font=('', 30), command=multiplicacion).place(x=170, y=130)


tk.Button(root, text='/', bd=0, bg='red', font=('', 30), command=division).place(x=240, y=130)
#command=listar_frutas

root.mainloop()