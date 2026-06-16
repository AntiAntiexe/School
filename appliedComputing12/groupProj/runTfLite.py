import tensorflow as tf
import numpy as np


class Classifier:
    def __init__(self, model_path):
        self.MODEL_PATH = model_path
        self.interpreter = tf.lite.Interpreter(model_path=self.MODEL_PATH)

        self.class_names = ['Apple', 'Banana', 'Carambola', 'Guava', 'Kiwi', 'Orange', 'Peach', 'Pear', 'Persimmon', 'Plum', 'Pomegranate', 'Tomatoes', 'muskmelon']
    
    def classify(self, image_path):
        img_height = 180
        img_width = 180

        img = tf.keras.utils.load_img(
            image_path, target_size=(img_height, img_width)
        )

        img_array = tf.keras.utils.img_to_array(img)
        img_array = tf.expand_dims(img_array, 0)

        sig = self.interpreter.get_signature_list()

        print("Signature List:", sig)

        classify_lite = self.interpreter.get_signature_runner('serving_default')
        classify_lite
        predictions_lite = classify_lite(dense_input=img_array)['dense_2']
        self.score_lite = tf.nn.softmax(predictions_lite)

        print(
        "This image most likely belongs to {} with a {:.2f} percent confidence."
        .format(self.class_names[np.argmax(self.score_lite)], 100 * np.max(self.score_lite))
        )









