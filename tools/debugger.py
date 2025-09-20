import pickle
from OpenAICompatibleAPI import *
# load the pkl file
with open('saved_object.pkl', 'rb') as f:
    obj = pickle.load(f)
print(obj)