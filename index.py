#!/usr/bin/python3
# -*- coding: utf-8 -*-

#----------------------------------------------------------
# Start des Programms
#----------------------------------------------------------

# importiere tkinter für graphische Oberfläche
from tkinter import *
from utils import chrono


# erzeuge das Hauptfenster:
hauptfenster = Tk()
hauptfenster.title("ZEPT - Zeitrechner für Projekte")
hauptfenster.geometry("600x200")


# Startfunktion für das Ausführen der Zeitnahme
def start():
    if start_button["text"] == "Start":
        start_button["text"] = "Stop"
        chrono.set_start_time()
    else:
        chrono.set_stop_time()
        chrono.set_time_diff()
        start_button["text"] = "Start"



# ...................................
# grafische Elemente im Hauptfenster:
# :::::::::::::::::::::::::::::::::::

# Start/Stop-Knopf für Start und Stop der Zeitname
start_button = Button(hauptfenster, text="Start", width=60, command=start)
start_button.place(x=50, y=150)




# starte das Programm:
if __name__ == "__main__":
    hauptfenster.mainloop()