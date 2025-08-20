import numpy as np
from PIL import Image
from tensorflow import keras
from tensorflow.keras.preprocessing import image
from tensorflow.keras.preprocessing.image import load_img
from tkinter.filedialog import askopenfilename


class FruitClassifier:
    def __init__(self):
        model_dir = "appliedComputing/groupProj/mainModel/model.h5"
        self.model = keras.models.load_model(model_dir)
    
    def runClassifier(self, fileName):
        image = Image.open(fileName)

        img_array = np.array(image.resize((128, 128), Image.LANCZOS))
        img_array = np.array(img_array, dtype="uint8")
        img_array = np.array(img_array) / 255.0
        
        train_labels = {
                "Apple": 0,
                "Banana": 1,
                "Mango": 2,
                "Orange": 3,
                "Pineapple": 4,
            }
        labels = dict((value, key) for key, value in train_labels.items())

        # Predicting
        predictions = self.model.predict(img_array[np.newaxis, ...])
        acc = np.max(predictions[0]) * 100
        result = labels[np.argmax(predictions[0], axis=-1)]
        
        print(f'The uploaded image has been classified as " {result}" with confidence {acc}%.')
        
        return acc, result
        
        
