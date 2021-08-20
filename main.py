from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

URLK = os.getcwd() 
mydir = f"sqlite:///{URLK}/dbejemplo.db"


app = Flask (__name__)
app.config[ "SQLALCHEMY_DATABASE_URI"]= mydir
app.config[ "SQLALCHEMY_TRACK_MODIFICATIONS" ] = False

dbapp = SQLAlchemy(app)

#creamos la base de datos con ORM SQLAlchemy
class Libros(db.model):
  id = db.Column(db.Integer, primary_key=True)
  nombreLibro = db.Column(db.String(80))
  categoria = db.Column(db.String(80))
  
  def __repr__(self):
    return "<Libros %r>" % self.nombreLibro


def agregar_libro_nuevo(nombre, category):
  creator_ecomy = Libros(nombreLibro=f'{nombre}',categoria = f"{category}")
  db.session.add(creator_ecomy)
  db.session.commit()
  
def mostrar_libros_registrados():
  mislibros = Libros.query.all()
  for i in mislibros:
    print (i.nombreLibro)

def seleccionar_libro(nombrex):
  existe = Libros.query.filter_by(nombre=f"{nombrex}").first()
  print(existe.nombreLibro)

def delete_libro(nombrex):
  existe = Libros.query.filter(Libros.nombreLibro==f"{nombrex}").first()
  if existe:
    db.session.delete(existe)
    db.session.commit()
    print(f"se ha eliminado el libro:  {nombrex}")
  else:
    print ("No se elimino ningun libro")

def update_libro(nombrex):
  existe = Libros.query.filter(Libros.nombreLibro==f"{nombrex}").first()
  if existe:
    print (f"actualizando libro {nombrex}")
    print("favor agregar el nuevo nombre y la nueva categoria")
    print("")
    nom = str(input("Nombre nuevo: "))
    
    cat = str(input("Categoria nueva: "))
    existe.nombreLibro = nom
    existe.categoria = cat
    db.session.commit()
    print("Se ha actualizado tu libro")
    print("")
  else:
    print("no ha actualizado ningun libro")

if __name__=="__main__":
  db.create_all()
  app.run(debug=True, port = 8989)

  
