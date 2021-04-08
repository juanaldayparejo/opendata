#Routine to read all profiles
from readfiles import *
import numpy as np
import os,sys

curr = os.getcwd()  #Current directory

#Reading the parameters of the observations
filename = 'ACSMIR_H2O_Database.txt'
nobsd,fname,orbit,IEflag,Pos,FPflag,Lsd,Loctd,Latd,Lond = read_database_dataproduct(filename)

#Reading the names of the available observations
observation = os.listdir('DATA_PRODUCTS_v2/')
observation = np.sort(observation)
nobs = len(observation)


#Reading the files and storing the data in arrays
maxpro = 1000
npro = np.zeros([nobs],dtype='int')
height = np.zeros([maxpro,nobs])
temp = np.zeros([maxpro,nobs])
temperr = np.zeros([maxpro,nobs])
press = np.zeros([maxpro,nobs])
numdens = np.zeros([maxpro,nobs])
numdenserr = np.zeros([maxpro,nobs])
h2oprof = np.zeros([maxpro,nobs])
h2oerr = np.zeros([maxpro,nobs])
dhprof = np.zeros([maxpro,nobs])
dherr = np.zeros([maxpro,nobs])
o18prof = np.zeros([maxpro,nobs])
o18err = np.zeros([maxpro,nobs])
lat = np.zeros([nobs])
lon = np.zeros([nobs])
Ls = np.zeros([nobs])
Loct = np.zeros([nobs])
satratio_h2o = np.zeros([maxpro,nobs])
IEobs = np.zeros([nobs],dtype='int32')   #Ingress or Egress
imy35 = 0

for i in range(nobs):
    os.chdir(curr)

    obs1 = observation[i]
    obs = obs1[0:len(obs1)-4]
    obs = obs.upper()

    print(obs)
    os.chdir('DATA_PRODUCTS_v2/')
    runname = obs.lower()

    #Reading files
    npro1,height1,press1,temp1,temperr1,numdens1,numdenserr1,h2oprof1,h2oerr1,dhratio1,dhratioerr1,o18ratio1,o18ratioerr1 = read_res_h2o_dataproduct(runname)
    npro[i] = npro1
    height[0:npro[i],i] = height1[0:npro[i]]
    press[0:npro[i],i] = press1[0:npro[i]]
    temp[0:npro[i],i] = temp1[0:npro[i]]
    temperr[0:npro[i],i] = temperr1[0:npro[i]]
    h2oprof[0:npro[i],i] = h2oprof1[:]
    h2oerr[0:npro[i],i] = h2oerr1[:]
    dhprof[0:npro[i],i] = dhratio1[:]
    dherr[0:npro[i],i] = dhratioerr1[:]
    o18prof[0:npro[i],i] = o18ratio1[:]
    o18err[0:npro[i],i] = o18ratioerr1[:]

    for j in range(nobsd):
        if runname==fname[j]:
            Ls1 = Lsd[j]
            Loct1 = Loctd[j]
            lat1 = Latd[j]
            lon1 = Lond[j]

    if i>0:
        if Ls1<Ls[i-1]:
            imy35 = 1

    if imy35==1:
        Ls[i] = Ls1 + 360.
    else:
        Ls[i] = Ls1

    print(Ls[i])
    lat[i] = lat1
    lon[i] = lon1
    Loct[i] = Loct1

    os.chdir(curr)

