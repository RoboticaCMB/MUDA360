# -*- coding: utf-8 -*-
from guizero import *


app = App(title="MUDA360", width=400, height=250, layout="grid", bg = "white") #create the iterface
welcome_message = Text(app, text="MUDA360", size=35, grid=[0,0,2,1], color="pale green")



#set the variables (raspberry)
HU = 10
TEMP = 27
TIRR = 10
TLUZ = 10


#Humidade
humidade = Text(app, text="Humidade: ", grid=[0,1])
humidade_display = Text(app, text=str(HU) + " %", grid=[1,1])



#Temperatura
temperatura = Text(app, text="Temperatura: ", grid=[0,2])
temperatura_display = Text(app, text=str(TEMP) + " °C", grid=[1,2])



#Tempo de irrigacao
tempo_de_irrigacao = Text(app, text="Tempo de irrigação: ", grid=[0,3])
tempo_de_irrigacao_display = Text(app, text=str(TIRR), grid=[1,3])
ml_por_dia = Text(app, text="ml por dia", grid=[2,3])




#Tempo de luz 
tempo_de_luz = Text(app, text="Tempo de Luz: ", grid=[0,4])
tempo_de_luz_display = Text(app, text=str(TLUZ), grid=[1,4])
tempo_por_dia = Text(app, text="min por dia", grid=[2,4])
                            



#Funcoes de alteracao



### Segunda Janela ###


def open_window():
    window_2.show(wait=True)

window_2 = Window(app, title = "Alterar", layout="grid", bg="white", height=200, width=350)
window_2.hide()

alterar = PushButton(app, text="Alterar", command=open_window, grid=[0,5,2,1])


#Tempo de irrigacao
tempo_de_irrigacao = Text(window_2, text="Tempo de irrigação: ", grid=[0,0])
tempo_de_irrigacao_display_2 = Text(window_2, text=str(TIRR), grid=[1,0])
ml_por_dia = Text(window_2, text="ml por dia", grid=[2,0])



#Tempo de luz 
tempo_de_luz = Text(window_2, text="Tempo de Luz: ", grid=[0,1])
tempo_de_luz_display_2 = Text(window_2, text=str(TLUZ), grid=[1,1])
tempo_por_dia = Text(window_2, text="min por dia", grid=[2,1])







### Alteracoes ###


def aumenta_tempo_de_irrigacao():
    tempo_de_irrigacao_display_2.value = str(int(tempo_de_irrigacao_display.value) + 1)
    tempo_de_irrigacao_display.value = tempo_de_irrigacao_display_2.value
    print(tempo_de_irrigacao_display.value)


def diminui_tempo_de_irrigacao():
    tempo_de_irrigacao_display_2.value = str(int(tempo_de_irrigacao_display.value) - 1)
    tempo_de_irrigacao_display.value = tempo_de_irrigacao_display_2.value
    print(tempo_de_irrigacao_display.value)


irrigacao = Text(window_2, text="Tempo de irrigação: ", grid=[0,2])
update_text = PushButton(window_2, command=aumenta_tempo_de_irrigacao, text="+", grid=[1,2])
update_text = PushButton(window_2, command=diminui_tempo_de_irrigacao, text="-", grid=[2,2])





def aumenta_tempo_de_luz():
    tempo_de_luz_display_2.value = str(int(tempo_de_luz_display.value) + 1)
    tempo_de_luz_display.value = tempo_de_luz_display_2.value
    print(tempo_de_luz_display.value)


def diminui_tempo_de_luz():
    tempo_de_luz_display_2.value = str(int(tempo_de_luz_display.value) - 1)
    tempo_de_luz_display.value = tempo_de_luz_display_2.value
    print(tempo_de_luz_display.value)


    
irrigacao = Text(window_2, text="Tempo de Luz: ", grid=[0,3])
update_text = PushButton(window_2, command=aumenta_tempo_de_luz, text="+", grid=[1,3])
update_text = PushButton(window_2, command=diminui_tempo_de_luz, text="-", grid=[2,3])



def alteracoes_salvas():
    info("Alterar", "Alterações salvas!")
    window_2.hide()

alteracoes_salvas = PushButton(window_2, command=alteracoes_salvas, text="OK", grid=[1,4,2,1], align="left")






app.display()
