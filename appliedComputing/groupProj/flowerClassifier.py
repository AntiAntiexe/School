import PIL.Image
import matplotlib.pyplot as plt
import numpy as np
import PIL 
import tensorflow as tf

from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential

import pathlib

# Manually download the file by visiting this URL in your browser:
# https://storage.googleapis.com/download.tensorflow.org/example_images/flower_photos.tgz
# Save it to a known location, e.g., "/Users/stineyttingejstrup/Downloads/flower_photos.tgz"

import tarfile
import pathlib

# Path to the manually downloaded file
downloaded_file = "/Users/home/Downloads/flower_photos.tgz"
extract_path = "/Users/home/Downloads"

# Extract the tar.gz file
with tarfile.open(downloaded_file, "r:gz") as tar:
    tar.extractall(path=extract_path)

data_dir = pathlib.Path(extract_path) / "flower_photos"

image_count = len(list(data_dir.glob('*/*.jpg')))
print(f"Total images found: {image_count}")

batch_size = 32
img_height = 180
img_width = 180

train_ds = tf.keras.utils.image_dataset_from_directory(
    data_dir,
    validation_split=0.2,
    subset="training",
    seed=123,
    image_size=(img_height, img_width),
    batch_size=batch_size)

val_ds = tf.keras.utils.image_dataset_from_directory(
    data_dir,
    validation_split=0.2,
    subset="validation",
    seed=123,
    image_size=(img_height, img_width),
    batch_size=batch_size)

plt.figure(figsize=(10, 10))

class_names = train_ds.class_names

for images, labels in train_ds.take(1):
    for i in range(9):
        ax = plt.subplot(3, 3, i + 1)
        plt.imshow(images[i].numpy().astype("uint8"))
        plt.title(class_names[labels[i]])
        plt.axis("off")
AUTOTUNE = tf.data.AUTOTUNE

train_ds = train_ds.cache().shuffle(1000).prefetch(buffer_size=AUTOTUNE)
val_ds = val_ds.cache().prefetch(buffer_size=AUTOTUNE)


normalization_layer = layers.Rescaling(1./255)

normalized_ds = train_ds.map(lambda x, y: (normalization_layer(x), y))
image_batch, labels_batch = next(iter(normalized_ds))
first_image = image_batch[0]

num_classes = len(class_names)

model = Sequential([
    layers.Rescaling(1./255, input_shape=(img_height, img_width, 3)),
    layers.Conv2D(16, 3, padding='same', activation='relu'),
    layers.MaxPooling2D(),
    layers.Conv2D(32, 3, padding='same', activation='relu'),
    layers.MaxPooling2D(),
    layers.Conv2D(64, 3, padding='same', activation='relu'),
    layers.MaxPooling2D(),
    layers.Flatten(),
    layers.Dense(128, activation='relu'),
    layers.Dense(num_classes)
])


model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

model.summary()




epochs = 10

history = model.fit(
    train_ds, 
    validation_data=val_ds,
    epochs=epochs
)

'''

tf.keras.models.save_model(model, 'model.pbtxt')

#convert model to TensorFlow Lite
converter = tf.lite.TFLiteConverter.from_keras_model(model = model)
tflite_model = converter.convert()

open("imgModel.tflite", "wb").write(tflite_model)


'''






acc = history.history['accuracy']
val_acc = history.history['val_accuracy']

loss = history.history['loss']
val_loss = history.history['val_loss']

epochs_range = range(epochs)

downloaded_img = "/Users/home/Downloads/592px-Red_sunflower.jpg"




data_dir = pathlib.Path(extract_path)
sunflower_path = data_dir / "592px-Red_sunflower.jpg"


img = tf.keras.utils.load_img(
    sunflower_path, target_size=(img_height, img_width)
)

img_array = tf.keras.utils.img_to_array(img)
img_array = tf.expand_dims(img_array, 0)  # Create a batch

predictions = model.predict(img_array)
score = tf.nn.softmax(predictions[0])
print(
    "This image most likely belongs to {} with a {:.2f} percent confidence."
    .format(class_names[np.argmax(score)], 100 * np.max(score))
)

plt.figure(figsize=(8, 8))
plt.subplot(1, 2, 1)
plt.plot(epochs_range, acc, label='Training Accuracy')
plt.plot(epochs_range, val_acc, label='Validation Accuracy')
plt.legend(loc='lower right')
plt.title('Training and Validation Accuracy')

plt.subplot(1, 2, 2)
plt.plot(epochs_range, loss, label='Training Loss')
plt.plot(epochs_range, val_loss, label='Validation Loss')
plt.legend(loc='upper right')
plt.title('Training and Validation Loss')
plt.show()
