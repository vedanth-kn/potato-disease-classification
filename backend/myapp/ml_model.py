from django.db import models
import tensorflow as tf
import os
# Create your models here.

model_path = "C:/Users/user/OneDrive/Desktop/potato_disease_classification/Training/potatoes.keras"
model = tf.keras.models.load_model(model_path)
CLASS_NAMES = ['Early Blight', 'Late Blight', 'Healthy']