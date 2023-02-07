# Calculadora feita com tkinter e python

from tkinter import *

# configurações do aplicativo Desktop
root = Tk()
root.title('Sua calculadora')
root.geometry('408x355')
root.minsize(400,355)
root.maxsize(400,355)
numero_um = ''
divisao = FALSE
multiplicacao = FALSE
adicao = FALSE
subtracao = FALSE

root.configure(background='#282828')

#funções operadores e numeros

#função de entrada de números
# também pode ser digitado pelo teclado menos os operadores
def botao_click(num):
    e.insert(END, num)

# funcao dividir
def botao_divisao():
    global numero_um
    global divisao
    divisao = TRUE
    numero_um = e.get()
    e.delete(0,END)

# funcao multiplicar
def botao_multiplicacao():
    global numero_um
    global multiplicacao
    multiplicacao = TRUE
    numero_um = e.get()
    e.delete(0,END)

# funcao subtrair
def botao_subtrair():
    global numero_um
    global subtracao
    subtracao = TRUE
    numero_um = e.get()
    e.delete(0,END)

# funcao somar
def botao_somar():
    global numero_um
    global adicao
    adicao = TRUE
    numero_um = e.get()
    e.delete(0,END)

# funcao botao limpar
def botao_limpar():
    e.delete(0, END)

# botao igual
def botao_igual():
    global subtracao
    global adicao
    global multiplicacao
    global divisao
    numero_dois = e.get()
    e.delete(0, END)
    if adicao == TRUE:
        e.insert(0, int(numero_um)+ int(numero_dois))
        adicao = FALSE

    if multiplicacao == TRUE:
        e.insert(0, int(numero_um)* int(numero_dois))
        multiplicacao = FALSE

    if subtracao == TRUE:
        e.insert(0, int(numero_um)- int(numero_dois))
        subtracao = FALSE
    if divisao == TRUE:
        e.insert(0, int(numero_um)/ int(numero_dois))
        divisao = FALSE

# funcao que mostra os operadores lógicos na telinha
def operadores_mostrar(texto,nome_funcao, row, column):
    operador = Button(root,
                text=texto,
                padx=40,
                pady=20,
                command=nome_funcao,
                fg='#FFFFFF',
                activeforeground='#FFFFFF',
                bg="#320064",
                background='#240046',
                relief=FLAT,
                font=('futura',12,'bold')
    )

    operador.grid(row=row, column=column)

# funcao que mostra os numeros na telinha
def numeros_mostrar(texto,padx,num,row,column,columnspan):
    numero = Button(root,
                text=texto,
                padx=padx,
                pady=20,
                command=lambda: botao_click(num),
                fg='#FFFFFF',
                activeforeground='#FFFFFF',
                bg="#320064",
                background='#240046',
                relief=FLAT,
                font=('futura',12,'bold')
    )
    numero.grid(row=row, column=column, columnspan=columnspan)

#primeira fileira
e = Entry(root,width=15,borderwidth=4,relief=FLAT, fg='#FFFFFF', bg='#a7a28f',font=('futura',25,'bold'), justify=CENTER)
e.grid(
    row=0,
    column=0,
    columnspan=4,
    pady=2
)
operadores_mostrar('+',botao_divisao,0,4)

#segunda fileira
numeros_mostrar(1,40,1,1,1,1)
numeros_mostrar(2,40,2,1,2,1)
numeros_mostrar(3,40,3,1,3,1)
operadores_mostrar('x',botao_multiplicacao,1,4)

#terceira fileira
numeros_mostrar(4,40,4,2,1,1)
numeros_mostrar(5,40,5,2,2,1)
numeros_mostrar(6,40,6,2,3,1)
operadores_mostrar('-',botao_subtrair,2,4)

#quarta fileira
numeros_mostrar(7,40,7,3,1,1)
numeros_mostrar(8,40,8,3,2,1)
numeros_mostrar(9,40,9,3,3,1)
operadores_mostrar('+',botao_somar,3,4)

#quinta fileira
numeros_mostrar(0,91,0,4,1,2)
operadores_mostrar('C',botao_limpar,4,3)
operadores_mostrar('=',botao_igual,4,4)

root.mainloop()