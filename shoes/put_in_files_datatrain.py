import os
import random

repartition = ['train']*80+['validation']*20
folder_train = 'data/train/three_quarters_front_left/'
folder_validation = 'data/validation/three_quarters_front_left/'

for element in os.listdir('three_quarters_front_left'):
  if os.path.isdir(element):
    next
  else:
    place = random.choice(repartition)
    if place == 'train':
      os.rename('three_quarters_front_left/'+element,folder_train+element)
      print('image displaced')
    else:
      os.rename('three_quarters_front_left/'+element,folder_validation+element)
      print('image displaced')

