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
    ttk.Button(frame, text = 'guardar producto', command = self.add_product).grid(row = 3, columnspan = 2, sticky = W + E)

    #mensajes de salida 
    self.message = Label(text = '', fg = 'red')
    self.message.grid(row = 3, column = 0, columnspan = 2, sticky = W + E)

    #tabla
    self.tree = ttk.Treeview(height = 10, columns = 2)
    self.tree.grid(row = 4, column = 0, columnspan = 2)
<<<<<<< HEAD
    self.tree.heading('#0',text = 'Nombre',anchor = CENTER)
    self.tree.heading('#1',text = 'Precio',anchor = CENTER)
=======
    self.tree.heading('#0',text = 'Nombre', anchor = CENTER)
    self.tree.heading('#1',text = 'Precio', anchor = CENTER)

    #botones
    ttk.Button(text = 'Borrar').grid(row = 5, column = 0, sticky = W + E)
    ttk.Button(text = 'Editar').grid(row = 5, column = 1, sticky = W + E)
    
    #llenando filas
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

  def validation(self):
    return len(self.name.get()) != 0 and len(self.price.get()) != 0  

  def add_product(self):
    if self.validation():
      query = 'INSERT INTO product VALUES(NULL, ?,?)'
      parameters = (self.name.get(), self.price.get())
      self.run_query(query, parameters)
      self.message['text'] = 'Producto {} agregado satisfactoriamente'.format(self.name.get())
      self.name.delete(0, END)
      self.price.delete(0, END)
    else:
      self.message['text'] = 'nombre y precio requerido'
    self.get_product() 

>>>>>>> test

if __name__ == "__main__":
  window = Tk()
  application = Product(window)
  window.mainloop()