import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
import tensorflow as tf
sess = tf.Session()
a = tf.constant(10)
b = tf.constant(32)
print(sess.run(a+b))