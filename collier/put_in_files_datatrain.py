import os
import random

repartition = ['train']*80+['validation']*20
folder_train = 'data/train/zoom/'
folder_validation = 'data/validation/zoom/'

for element in os.listdir('zoom'):
  if os.path.isdir(element):
    next
  else:
    place = random.choice(repartition)
    if place == 'train':
      os.rename('zoom/'+element,folder_train+element)
      print('image displaced')
    else:
      os.rename('zoom/'+element,folder_validation+element)
      print('image displaced')
