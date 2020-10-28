from tkinter import ttk 
from tkinter import *

import sqlite3

class Product:

  db_name = 'database.db'

  def __init__(self, window):
    self.wind = window
    self.wind.title('Productos')

    #contenedor/frame
    frame = LabelFrame(self.wind, text = 'registra un nuevo produco')
    frame.grid(row = 0, column = 0, columnspan = 3, pady = 20)

    #Name input
    Label(frame, text = 'Nombre: ').grid(row = 1, column = 0)
    self.name = Entry(frame)
    self.name.focus()
    self.name.grid(row = 1, column = 1)

    #price imput
    Label(frame, text = 'Precio: ').grid(row = 2, column = 0)
    self.price = Entry(frame)
    self.price.grid(row = 2, column = 1)

    #boton para agregar producto 
    ttk.Button(frame, text = 'guardar producto').grid(row = 3, columnspan = 2, sticky = W + E)

    #tabla
    self.tree = ttk.Treeview(height = 10, columns = 2)
    self.tree.grid(row = 4, column = 0, columnspan = 2)
    self.tree.heading('#0',text = 'Nombre', anchor = CENTER)
    self.tree.heading('#1',text = 'Precio', anchor = CENTER)

    self.get_product()

  def run_query(self, query, parameters = ()):
    with sqlite3.connect(self.db_name) as conn:
      cursor = conn.cursor()
      result = cursor.execute(query, parameters)
      conn.commit()
      return result

  def get_product(self):
    #limpiando tabla
    records = self.tree.get_children()
    for element in records:
      self.tree.delete(element)
    #quering data
    query = 'SELECT * FROM product ORDER BY nombre DESC'
    db_rows = self.run_query(query)
    #rellenando datos
    for row in db_rows:
      self.tree.insert('', 0, text = row[1], values = row[2])

if __name__ == "__main__":
  window = Tk()
  application = Product(window)
  window.mainloop()