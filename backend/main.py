# import the necessary packages
from keras.applications import ResNet50
from keras.preprocessing.image import img_to_array
from keras.applications import imagenet_utils
from PIL import Image
import numpy as np
import flask
import io
import base64
from os import path

# initialize our Flask application and the Keras model
app = flask.Flask(__name__)
model = None


def load_model():
    # load the pre-trained Keras model (here we are using a model
    # pre-trained on ImageNet and provided by Keras, but you can
    # substitute in your own networks just as easily)
    global model
    model = ResNet50(weights="imagenet")


def prepare_image(image, target):
    # if the image mode is not RGB, convert it
    if image.mode != "RGB":
        image = image.convert("RGB")

    # resize the input image and preprocess it
    image = image.resize(target)
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)
    image = imagenet_utils.preprocess_input(image)

    # return the processed image
    return image


def proccess(image, data):
    image = prepare_image(image, target=(224, 224))

    # classify the input image and then initialize the list
    # of predictions to return to the client
    preds = model.predict(image)
    results = imagenet_utils.decode_predictions(preds)
    print(results)
    data["predictions"] = []

    # loop over the results and add them to the list of
    # returned predictions
    for (imagenetID, label, prob) in results[0]:
        r = {"label": label, "probability": float(prob)}
        data["predictions"].append(r)

    data["success"] = True


@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
  return response

@app.route("/predecir", methods=["GET", "POST"])
def predict():
    data = {"success": False}
    if flask.request.method == "GET":
        if flask.request.args.get("idPrueba"):
            image_path = flask.request.args.get("idPrueba")
            image_path = "test/"+image_path.split("_")[0]+"/"+image_path+".jpg"
            base_path = path.dirname(__file__)
            file_path = base_path + "/" + image_path
            print(file_path)
            image = open(file_path, "rb").read()
            image = Image.open(io.BytesIO(image))

            proccess(image, data)

    elif flask.request.method == "POST":
        if flask.request.form.get("imagen"):
            image = flask.request.form["imagen"]

            image = Image.open(io.BytesIO(base64.b64decode(image)))
            proccess(image, data)

    return flask.jsonify(data)


# if this is the main thread of execution first load the model and
# then start the server
if __name__ == "__main__":
    load_model()
    app.run(debug=False, threaded=False)
