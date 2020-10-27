from tkinter import ttk 
from tkinter import *

import sqlite3

class Product:

  def __init__(self, window):
    self.wind = window
    self.wind.title('Productos')

    #contenedor/frame
    frame = LabelFrame(self.wind, text = 'registra un nuevo produco')
    frame.grid(row = 0, column = 0, columnspan = 3, pady = 20)

    #Name input
    Label(frame, text = 'Nombre: ').grid(row = 1, column = 0)
    self.name = Entry(frame)
    self.name.grid(row = 1, column = 1)

    #price imput
    Label(frame, text = 'Precio: ').grid(row = 2, column = 0)
    self.price = Entry(frame)
    self.price.grid(row = 2, column = 1)

if __name__ == "__main__":
  window = Tk()
  application = Product(window)
  window.mainloop()