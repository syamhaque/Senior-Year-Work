#EECS 118 mp5
#Mohammed Haque
#62655407
#11/18/19
import tensorflow as tf
from tensorflow import keras

mnist = tf.keras.datasets.mnist
(training_images, training_labels), (testing_images, testing_labels) = mnist.load_data()

model = tf.keras.models.load_model('model.h5')
testing_images = testing_images.reshape(10000,28,28,-1) / 255.0
testing_images = tf.keras.utils.normalize(testing_images, axis=1)

testing_loss, testing_acc = model.evaluate(testing_images, testing_labels)

print("The accuracy of the prediction result of my model: ", testing_acc)
