# pip3 install requests
from distutils.log import info
import requests

# Macowins tinda de venta de ropa:
# Protocolo: https
# Dominio: macowins-server.herokuapp.com
# /prendas/1: correponde al primer item del del recurso pandas

# HTTP tine vernbos que me hbalan que dicen que hacer con los recursos

# GET es un verbo HTTP se utiliza para que traiga informacion del servidor 

r = requests.get('https://macowins-server.herokuapp.com/prendas/1')

#json es para traer infromacion de prendas 
#json es como un diccionario 

print(r.json())

#prendas 
r_prendas = requests.get('https://macowins-server.herokuapp.com/prendas')
prendas = r_prendas.json()
#ventas como es unna lista me devuelve el largo de la lista
r_ventas = requests.get('https://macowins-server.herokuapp.com/ventas')
ventas = r_ventas.json()

print(prendas)

print("\n",len(ventas))
print("\n",r_prendas.headers)
#pantalones porfa --> (?) con esto le digo que me busque, despues le digo que el tipo sea igual a pantalon y me traiga todos

print("\n",requests.get('https://macowins-server.herokuapp.com/prendas?tipo=pantalon').json())
#pantalon talle 42
print("\n",requests.get('https://macowins-server.herokuapp.com/prendas?tipo=pantalon&talle=42').json())

"""
PROTOCOLOS:

OPTIONS: consultar meta-datos o configuraciones de HTTP
GET: consultar un contenido sin efecto
POST: crear un contenido
PUT: actualizar de forma total un contenido
PATCH: actualizar de forma parcial un contenido
DELETE: eliminar un contenido
"""
#de esta manera cargo un nuevo producto a mi tienda 
url = "https://macowins-server.herokuapp.com/prendas"
producto = {"id":45, "tipo": "gorro","talle":"12"}

# print("\n",requests.post(url, data=producto))
# request(se pone siempre).post(crea un nuevo contenido)(esto puede cambiar)((a donde quiero acceder URL), SIEMPRE data= (lo que quiera agregar))
