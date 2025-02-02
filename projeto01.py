from tkinter import *
from tkinter import ttk

# cores

cor1 = "#1e1f1e" # PRETO
cor2 = "#feffff" # BRANCA
cor3 = "#38576b" # AZUL ESCURO
cor4 = "#ECEFF1" # CINZA
cor5 = "#FFAB40" # LARANJA

janela = Tk()
janela.title("Calculadora")
janela.geometry("235x318")
janela.config(bg=cor1)

# Criando frames 
frame_tela = Frame(janela, width=235, height=50, bg=cor3)
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(janela, width=235, height=268)
frame_corpo.grid(row=1, column=0)

# Criando botões
b_c = Button(frame_corpo, text="C", width=8, height=2, bg=cor4, font=('Ivy','12','bold'), relief=RAISED, overrelief=RIDGE)
b_c.place(x=0, y=0)
b_por = Button(frame_corpo, text="%", width=3, height=2, bg=cor4, font=('Ivy','12','bold'), relief=RAISED, overrelief=RIDGE)
b_por.place(x=115, y=0)
b_div = Button(frame_corpo, text="/", width=3, height=2, bg=cor5, fg=cor2, font=('Ivy','12','bold'), relief=RAISED, overrelief=RIDGE)
b_div.place(x=175, y=0)

# Criando botões segunda fileira
b_7 = Button(frame_corpo, text="7", width=3, height=3, bg=cor4, font=('Ivy','12','bold'), relief=RAISED, overrelief=RIDGE)
b_7.place(x=0, y=52)
b_8 = Button(frame_corpo, text="8", width=3, height=3, bg=cor4, font=('Ivy','12','bold'), relief=RAISED, overrelief=RIDGE)
b_8.place(x=59, y=52)
b_9 = Button(frame_corpo, text="9", width=3, height=3, bg=cor4, font=('Ivy','12','bold'), relief=RAISED, overrelief=RIDGE)
b_9.place(x=118, y=52)
b_10 = Button(frame_corpo, text="$", width=3, height=3, bg=cor5, fg=cor2, font=('Ivy','12','bold'), relief=RAISED, overrelief=RIDGE)
b_10.place(x=177, y=52)

# Criando botões terceira fileira
b_4 = Button(frame_corpo, text="4", width=3, height=2, bg=cor4, font=('Ivy','12','bold'), relief=RAISED, overrelief=RIDGE)
b_4.place(x=0, y=109)
b_5 = Button(frame_corpo, text="5", width=3, height=2, bg=cor4, font=('Ivy','12','bold'), relief=RAISED, overrelief=RIDGE)
b_5.place(x=59, y=109)
b_6 = Button(frame_corpo, text="6", width=3, height=2, bg=cor4, font=('Ivy','12','bold'), relief=RAISED, overrelief=RIDGE)
b_6.place(x=118, y=109)
b_x = Button(frame_corpo, text="X", width=3, height=2, bg=cor5, fg=cor2, font=('Ivy','12','bold'), relief=RAISED, overrelief=RIDGE)
b_x.place(x=177, y=109)

# Criando botões quarta fileira
b_1 = Button(frame_corpo, text="1", width=3, height=2, bg=cor4, font=('Ivy','12','bold'), relief=RAISED, overrelief=RIDGE)
b_1.place(x=0, y=160)
b_2 = Button(frame_corpo, text="2", width=3, height=2, bg=cor4, font=('Ivy','12','bold'), relief=RAISED, overrelief=RIDGE)
b_2.place(x=59, y=160)
b_3 = Button(frame_corpo, text="3", width=3, height=2, bg=cor4, font=('Ivy','12','bold'), relief=RAISED, overrelief=RIDGE)
b_3.place(x=118, y=160)
b_x = Button(frame_corpo, text="X", width=3, height=2, bg=cor5, fg=cor2, font=('Ivy','12','bold'), relief=RAISED, overrelief=RIDGE)
b_x.place(x=177, y=160)

# Criando botões quinta fileira
b_1 = Button(frame_corpo, text="C", width=8, height=2, bg=cor4, font=('Ivy','12','bold'), relief=RAISED, overrelief=RIDGE)
b_1.place(x=0, y=215)
b_2 = Button(frame_corpo, text="%", width=3, height=2, bg=cor4, font=('Ivy','12','bold'), relief=RAISED, overrelief=RIDGE)
b_2.place(x=115, y=215)
b_3 = Button(frame_corpo, text="/", width=3, height=2, bg=cor5, fg=cor2, font=('Ivy','12','bold'), relief=RAISED, overrelief=RIDGE)
b_3.place(x=175, y=215)



janela.mainloop()
