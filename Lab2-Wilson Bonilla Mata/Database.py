from pymongo import MongoClient # Importe para administrar bases de datos en MongoDB
from bson.objectid import ObjectId # Importe para manejar datos de tipo ObjectId

# Conexión a la base de datos MongoDB
client = MongoClient('localhost', 27017)

# Crear una nueva base de datos
db = client['enfermedades_plantas']

# Crear una colección llamada "reglas"
collection = db['reglas']

def get_collection():
    return collection

def agregar_regla(regla):
    collection.insert_one(regla)

def eliminar_regla(id):
    collection.delete_one({"_id": ObjectId(id)})

def obtener_reglas():
    return collection.find()

def obtener_lista_reglas():
    reglas = []
    for regla in obtener_reglas():
        reglas.append(regla)
    return reglas