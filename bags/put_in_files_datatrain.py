import os
import random

repartition = ['train']*80+['validation']*20
folder_train = 'data_backpacks/train/three_quarter_right/'
folder_validation = 'data_backpacks/validation/three_quarter_right/'

for element in os.listdir('data_backpacks/three_quarter_right'):
  if os.path.isdir(element):
    next
  else:
    place = random.choice(repartition)
    if place == 'train':
      os.rename('data_backpacks/three_quarter_right/'+element,folder_train+element)
      print('image displaced')
    else:
      os.rename('data_backpacks/three_quarter_right/'+element,folder_validation+element)
      print('image displaced')
