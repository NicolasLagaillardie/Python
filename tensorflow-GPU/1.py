# -*- coding: utf-8 -*-
"""
Created on Sat Jun  2 16:38:01 2018

@author: Lagai
"""

import tensorflow as tf

c = tf.constant('Hello, world!')

with tf.Session() as sess:

    print(sess.run(c))
    
with tf.Graph().as_default():
  # Create a six-element vector (1-D tensor).
  primes = tf.constant([2, 3, 5, 7, 11, 13], dtype=tf.int32)

  # Create another six-element vector. Each element in the vector will be
  # initialized to 1. The first argument is the shape of the tensor (more
  # on shapes below).
  ones = tf.ones([6], dtype=tf.int32)

  # Add the two vectors. The resulting tensor is a six-element vector.
  just_beyond_primes = tf.add(primes, ones)

  # Create a session to run the default graph.
  with tf.Session() as sess:
    print(just_beyond_primes.eval())
    
with tf.Graph().as_default():
  # A scalar (0-D tensor).
  scalar = tf.ones([])

  # A vector with 3 elements.
  vector = tf.ones([3])

  # A matrix with 2 rows and 3 columns.
  matrix = tf.ones([2, 3])

  with tf.Session() as sess:
    print('scalar has shape', scalar.get_shape(), 'and value:\n', scalar.eval())
    print('vector has shape', vector.get_shape(), 'and value:\n', vector.eval())
    print('matrix has shape', matrix.get_shape(), 'and value:\n', matrix.eval())

with tf.Graph().as_default():
  # Create a six-element vector (1-D tensor).
  primes = tf.constant([2, 3, 5, 7, 11, 13], dtype=tf.int32)

  # Create a constant scalar with value 1.
  ones = tf.constant(1, dtype=tf.int32)

  # Add the two tensors. The resulting tensor is a six-element vector.
  just_beyond_primes = tf.add(primes, ones)

  with tf.Session() as sess:
    print(just_beyond_primes.eval())
    
    
with tf.Graph().as_default():
  # Create a matrix (2-d tensor) with 3 rows and 4 columns.
  x = tf.constant([[5, 2, 4, 3], [5, 1, 6, -2], [-1, 3, -1, -2]],
                  dtype=tf.int32)

  # Create a matrix with 4 rows and 2 columns.
  y = tf.constant([[2, 2], [3, 5], [4, 5], [1, 6]], dtype=tf.int32)

  # Multiply `x` by `y`. 
  # The resulting matrix will have 3 rows and 2 columns.
  matrix_multiply_result = tf.matmul(x, y)

  with tf.Session() as sess:
    print(matrix_multiply_result.eval())
    
with tf.Graph().as_default():
  # Create an 8x2 matrix (2-D tensor).
  matrix = tf.constant([[1,2], [3,4], [5,6], [7,8],
                        [9,10], [11,12], [13, 14], [15,16]], dtype=tf.int32)

  # Reshape the 8x2 matrix into a 2x8 matrix.
  reshaped_2x8_matrix = tf.reshape(matrix, [2,8])
  
  # Reshape the 8x2 matrix into a 4x4 matrix
  reshaped_4x4_matrix = tf.reshape(matrix, [4,4])

  with tf.Session() as sess:
    print("Original matrix (8x2):")
    print(matrix.eval())
    print("Reshaped matrix (2x8):")
    print(reshaped_2x8_matrix.eval())
    print("Reshaped matrix (4x4):")
    print(reshaped_4x4_matrix.eval())
    
with tf.Graph().as_default():
  # Create an 8x2 matrix (2-D tensor).
  a = tf.constant([5, 3, 2, 7, 1, 4])

  # Reshape the 8x2 matrix into a 2x8 matrix.
  b = tf.constant([4, 6, 3])
  
  # Reshape the 8x2 matrix into a 4x4 matrix
  reshaped_4x4_matrix = tf.reshape(a, [4,4])

  with tf.Session() as sess:
    print("Original matrix (8x2):")
    print(matrix.eval())
    print("Reshaped matrix (2x8):")
    print(reshaped_2x8_matrix.eval())
    print("Reshaped matrix (4x4):")
    print(reshaped_4x4_matrix.eval())
    