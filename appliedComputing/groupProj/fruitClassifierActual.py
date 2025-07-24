import PIL.Image
import matplotlib.pyplot as plt
import numpy as np
import PIL 
import tensorflow as tf

from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential

import zipfile


import mlcroissant as mlc
import pandas as pd

import pathlib

import tarfile
import pathlib

# Path to the manually downloaded file
downloaded_file = "/Users/home/Downloads/fruity.tgz"
extract_path = "/Users/home/Downloads"

# Extract the tar.gz file
#with tarfile.open(downloaded_file, "r:gz") as tar:
 #   tar.extractall(path=extract_path)

#data_dir = pathlib.Path(extract_path) / "fruity"
# If your images are already extracted in a folder, set the path directly:
data_dir = pathlib.Path("/Users/home/Downloads/fruity")

image_count = len(list(data_dir.glob('*/*.png')))
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

def classNames():
    return train_ds.class_names

print("Class names:", classNames())





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
              loss=tf.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])



model.summary()



epochs = 10

history = model.fit(
    train_ds, 
    validation_data=val_ds,
    epochs=epochs
)

tf.saved_model.save(model, "appliedComputing/groupProj/fruitModel")

#acc = history.history['accuracy']
#val_acc = history.history['val_accuracy']

#loss = history.history['loss']
#val_loss = history.history['val_loss']

#epochs_range = range(epochs)

#downloaded_img = "/Users/home/Downloads/apple.png"



