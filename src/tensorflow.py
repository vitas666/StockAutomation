import numpy as np
import tensorflow as tf
from tensorflow import keras


# what is tensor? A tensor is a multi-dimensional array used to represent data in TensorFlow.
# A tensor is a generalization of vectors and matrices to potentially higher dimensions. Internally, TensorFlow represents tensors as n-dimensional arrays of base datatypes.

# how to activate venv? 
# Linux: python3 -m venv venv
# source venv/bin/activate
# note: tensorflow is conflict with some versions of protobuf required by google-generativeai, better not install tensorflow in the same venv as google-generativeai

#Let's design a financial dataset in csv to regonize the linear relationship between users age, gender vs their monthly spending amount and bank balancce
