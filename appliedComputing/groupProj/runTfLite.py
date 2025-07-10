import tensorflow as tf
import fruitClassifierActual
import numpy as np


fruit_path = '/Users/home/Downloads/apple.png'

img_height = 180
img_width = 180

img = tf.keras.utils.load_img(
    fruit_path, target_size=(img_height, img_width)
)

img_array = tf.keras.utils.img_to_array(img)
img_array = tf.expand_dims(img_array, 0) # Create a batch

class_names = fruitClassifierActual.classNames() # Get the class names from the model


TF_MODEL_FILE_PATH = 'fruitModel.tflite' # The default path to the saved TensorFlow Lite model

interpreter = tf.lite.Interpreter(model_path=TF_MODEL_FILE_PATH)


sig = interpreter.get_signature_list()

print("Signature List:", sig)

classify_lite = interpreter.get_signature_runner('serving_default')
classify_lite



predictions_lite = classify_lite(dense_input=img_array)['dense_2']
score_lite = tf.nn.softmax(predictions_lite)

print(
    "This image most likely belongs to {} with a {:.2f} percent confidence."
    .format(class_names[np.argmax(score_lite)], 100 * np.max(score_lite))
)





