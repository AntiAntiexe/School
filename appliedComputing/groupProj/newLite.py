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


TF_MODEL_PATH = 'model.tflite'

