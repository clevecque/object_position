import os
import random

repartition = ['train']*80+['validation']*20
folder_train = 'data/train/boucle/'
folder_validation = 'data/validation/boucle/'

for element in os.listdir('images/boucles'):
  if os.path.isdir(element):
    next
  else:
    place = random.choice(repartition)
    if place == 'train':
      os.rename('images/boucles/'+element,folder_train+element)
      print('image displaced')
    else:
      os.rename('images/boucles/'+element,folder_validation+element)
      print('image displaced')
