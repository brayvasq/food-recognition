import cv2

from prediccion import prediccion

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

# categorias=["Huevos","Arepas",...]
categorias = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16"]
reconocimiento = prediccion()
imagenPrueba = cv2.imread("test/tuca_frita.jpg", 0)
indiceCategoria = reconocimiento.predecir(imagenPrueba)
print("La imagen cargada es ", elegirCategoria(categorias[indiceCategoria]))
while True:
    cv2.imshow("imagen", imagenPrueba)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
cv2.destroyAllWindows()
