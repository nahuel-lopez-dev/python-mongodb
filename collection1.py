# importando pymongo
import pymongo
# para que tome caracteres especiales y acentos
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

### Cadena de conexión de Mongo Atlas
MONGO_URL = "mongodb+srv://<username>:<password>@cluster0.xxxxxxx.mongodb.net/?retryWrites=true&w=majority"
MONGO_BASEDATOS = "database" # base de datos a utilizar
MONGO_COLECCION = "collection" # coleccion a utilizar
MONGO_TIME_OUT=1000 #Por defecto necesita un time out para realizar la conexión

### Anticipando errores de ejecución usando 'TRY y EXCEPT'
try:
    ### Variable cliente que se va a conectar al cliente de Mongo
    cliente=pymongo.MongoClient(MONGO_URL,serverSelectionTimeoutMS=MONGO_TIME_OUT)
    db = cliente[MONGO_BASEDATOS]
    coleccion = db[MONGO_COLECCION]
      
    coleccion.insert_many([
    {"nombre": "Fulano", "fecha": "1900-12-30", "long": 48.829534, "lat": 55.258882},
    {"nombre": "Sultano", "fecha": "1900-12-30", "long": 48.463983, "lat": 55.756767},
    {"nombre": "Mengano", "fecha": "1900-12-30", "long": 48.113737, "lat": 55.329381},
    {"nombre": "Montoto", "fecha": "1900-12-30", "long": 48.436374, "lat": 55.687439}
    ])   
        
    cliente.close()
    
# Error por exceso de tiempo de respuesta    
except pymongo.errors.ServerSelectionTimeoutError as errorTiempo:
    print("Tiempo excedido de carga")

# Error de conexión    
except pymongo.errors.ConnectionFailure as errorConexion:
    print("Fallo al conectarse a mongodb"+errorConexion)