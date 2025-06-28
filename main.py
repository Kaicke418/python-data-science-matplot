import tkinter as tk



root = tk.Tk()
root.geometry('500x500')
root.title('Exemplo')



text_1 = tk.Label(root, text = 'ISSO É UM TEXTO', font = ('roboto', 15)) 
text_1.grid(row = 1, column = 1, pady = 10)



# widgets 
btn = tk.Button(root, text = 'clique aqui', font = ('roboto', 15))
btn.grid(row = 2, column = 1, pady = 10)


input_1 =  tk.Entry(root, font = ('roboto', 15), bg = 'red', fg = 'white')
input_1.grid(row = 3, column = 1, pady = 10, padx = 30)


root.mainloop()