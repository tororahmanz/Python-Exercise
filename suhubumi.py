import math
import os
eta=0.7
deta=0.025

n=14
Rb=6400000
Rm=6.9570E8
Dbm=1.471E11
Tm=5500
i=1

while i<n :
  Tb0=Tm/eta**0.25*(Rm/Dbm/2)**0.5
#  print ("Suhu bumi tanpa gas rumah kaca: (K) ",Tb0)
  print ("Suhu bumi tanpa gas rumah kaca (C) untuk eta=:", eta," adalah ",Tb0-273)
  i=i+1
  eta=eta+deta