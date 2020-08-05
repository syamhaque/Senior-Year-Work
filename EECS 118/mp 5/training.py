#EECS 118 mp5
#Mohammed Haque
#62655407
#11/18/19
import tensorflow as tf
from tensorflow import keras

mnist = tf.keras.datasets.mnist
(training_images, training_labels), (testing_images, testing_labels) = mnist.load_data()

training_labels = training_labels[:20000]
training_images = training_images[:20000].reshape(20000,28,28,-1) / 255.0
training_images = tf.keras.utils.normalize(training_images, axis=1)

model = tf.keras.models.Sequential([
  tf.keras.layers.Conv2D(32, (3,3), padding='valid', activation='relu', input_shape=(28, 28, 1)),
  tf.keras.layers.MaxPooling2D((2,2)),
  tf.keras.layers.Conv2D(64, (3,3), padding='valid', activation='relu'),
  tf.keras.layers.MaxPooling2D((2,2), strides=2),
  tf.keras.layers.Flatten(),
  tf.keras.layers.Dense(128, activation='relu'),
  tf.keras.layers.Dense(10, activation='softmax')
])

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
model.summary()
model.fit(training_images, training_labels, epochs=9)
model.save("model.h5")
