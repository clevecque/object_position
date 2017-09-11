import csv

cr = csv.reader(open("myntra.csv","r"))
c = csv.writer(open("myntra_real.csv","w"))

for row in cr :
  if row[0] == 'item':
    c.writerow(row)
  else:
    new_row=[row[0],row[1],row[2],row[3],row[4]]
    new_row+=[row[5][14:]]
    row_splitted = row[6].split('/')
    row_splitted[3]='h_640,q_90,w_480'
    new_row+=[('/').join(row_splitted)]
    c.writerow(new_row)
