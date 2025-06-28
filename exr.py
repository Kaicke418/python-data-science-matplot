import tkinter as tk


def somar():
    n1 = float(input_1.get())
    n2 = float(input_2.get())
    somar = n1 + n2
    resultado.config(text = somar)







root = tk.Tk()
root.geometry('500x500')
root.title('Exemplo')
root.configure(bg = 'gray')


# widgets 

text_1 = tk.Label(root, text = 'CALCULADORA', font = ('roboto', 15)) 
text_1.grid(row = 1, column = 1, pady = 10)

input_1 =  tk.Entry(root, font = ('roboto', 15),  fg = 'blue')
input_1.grid(row = 2, column = 1, pady = 10, padx = 30)

input_2 =  tk.Entry(root, font = ('roboto', 15),  fg = 'blue')
input_2.grid(row = 3, column = 1, pady = 10, padx = 30)

btn = tk.Button(root, text = '+', font = ('roboto', 15), bg = 'black', fg = 'yellow', command = somar)
btn.grid(row = 5, column = 1, pady = 10)

resultado = tk.Label(root, text = 'Resultado = ', font = ('roboto', 15)) 
resultado.grid(row = 6, column = 1, pady = 10)

root.mainloop()