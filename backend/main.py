
from PIL import Image
import numpy as np
import flask
import io
import base64
from os import path
import cv2
from prediccion import prediccion
import numpy as np
import json
import pruebita_svm


# initialize our Flask application and the Keras model
app = flask.Flask(__name__)
model = None
categorias = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16"]
reconocimiento = prediccion()

escenas = ["desayuno paisa","desayuno paisa cafetero","desayuno rolo","desayuno americano","desayuno americano ligth"]

def readb64(base64_string):
    sbuf = io.BytesIO()
    sbuf.write(base64.b64decode(base64_string))
    pimg = Image.open(sbuf)
    return cv2.cvtColor(np.array(pimg), cv2.COLOR_RGB2BGR)

def elegirCategoria(categoria):
    print(categoria)
    if categoria == "0":
        return "Huevos"
    if categoria == "1":
        return "Arepas"
    if categoria == "2":
        return "Mantequilla"
    if categoria == "3":
        return "Chocolate"
    if categoria == "4":
        return "Pan"
    if categoria == "5":
        return "Cereales"
    if categoria == "6":
        return "Cafe"
    if categoria == "7":
        return "Leche"
    if categoria == "8":
        return "Tocino"
    if categoria == "9":
        return "Changua"
    if categoria == "10":
        return "Tamal"
    if categoria == "11":
        return "Papas"
    if categoria == "12":
        return "Calentado"
    if categoria == "13":
        return "Yuca frita"
    if categoria == "14":
        return "Jugo naranja"
    if categoria == "15":
        return "Yogurth"
    if categoria == "16":
        return "Pollo"


@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
  return response

@app.route("/analisisEscena",methods=["GET", "POST"])
def analisis():
    data = {"success": False}
    if flask.request.method == "GET":
        return "No implementado"
    elif flask.request.method == "POST":
        data = json.loads(flask.request.data)
        data = data['materiales']
        vector = []
        
        for i in data:
            vector.append(str(i['idCategoria']))
            
        items = 6 - len(vector)
        for i in range(0,items):
            vector.append("-1")   
        resp = pruebita_svm.clf.predict([vector])
        resp = escenas[resp[0]]
        data = {
                "idPrueba": 0,
                "analisis_escena": resp,
                "probabilidades": []
        }
        return flask.jsonify(data)

@app.route("/predecir", methods=["GET", "POST"])
def predict():
    data = {"success": False}
    if flask.request.method == "GET":
        if flask.request.args.get("idPrueba"):
            idImagen = flask.request.args.get("idPrueba")
            image_path = "test/"+idImagen.split("_")[0]+"/"+idImagen+".jpg"
            base_path = path.dirname(__file__)
            file_path = base_path + "/" + image_path
            print(file_path)
            image = cv2.imread(file_path, 0)
            indiceCategoria, predicciones = reconocimiento.predecir(image)
            print(indiceCategoria)
            print(predicciones)
            predicciones = list(predicciones)
            predicciones = list(map(lambda x: float(x), predicciones))
            predicciones = list(map(lambda x: round(x,2), predicciones))
            data = {
                "idImagen": idImagen,
                "prediccion": elegirCategoria(categorias[indiceCategoria]).lower(),
                "probabilidades": predicciones
            }
            print(data)
    elif flask.request.method == "POST":
        if flask.request.form.get("imagen"):
            image = flask.request.form["imagen"]
            image = readb64(image)
            image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
 
            indiceCategoria, predicciones = reconocimiento.predecir(image)
            print(indiceCategoria)
            print(predicciones)
            predicciones = list(predicciones)
            predicciones = list(map(lambda x: float(x), predicciones))
            predicciones = list(map(lambda x: round(x,2), predicciones))
            data = {
                "idImagen": 0,
                "prediccion": elegirCategoria(categorias[indiceCategoria]).lower(),
                "probabilidades": predicciones
            }
            # proccess(image, data)
            #pass
    return flask.jsonify(data)


# if this is the main thread of execution first load the model and
# then start the server
if __name__ == "__main__":
    #load_model()
    app.run(debug=False, threaded=False)
