import csv
import urllib
import urllib.request
import os

cr = csv.reader(open('myntra_belts.csv'))

def verify_path(path):
  if os.path.exists(path) is False :
    os.makedirs(path)

folder = 'images/myntra'
verify_path(folder)

for row in cr :
  if row[0]!= 'item':
    try:
      nom = os.path.join(folder,row[5]+'_belt'+row[6][-6:])
      urllib.request.urlretrieve(row[6],nom)
    except IndexError :
      continue

