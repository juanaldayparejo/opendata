#Routine to read all profiles
from readfiles import *
import numpy as np
import os,sys

curr = os.getcwd()  #Current directory

#Reading the parameters of the observations
filename = 'ACSMIR_CO2_Database.txt'
nobsd,fname,orbit,IEflag,Pos,FPflag,Lsd,Loctd,Latd,Lond = read_database_dataproduct(filename)

#Reading the names of the available observations
observation = os.listdir('PROFILES/')
observation = np.sort(observation)
nobs = len(observation)


#Reading the files and storing the data in arrays
maxpro = 200
npro = np.zeros([nobs],dtype='int')
height = np.zeros([maxpro,nobs])
temp = np.zeros([maxpro,nobs])
temperr = np.zeros([maxpro,nobs])
c13prof = np.zeros([maxpro,nobs])
c13err = np.zeros([maxpro,nobs])
o18prof = np.zeros([maxpro,nobs])
o18err = np.zeros([maxpro,nobs])
o17prof = np.zeros([maxpro,nobs])
o17err = np.zeros([maxpro,nobs])
lat = np.zeros([nobs])
lon = np.zeros([nobs])
Ls = np.zeros([nobs])
Loct = np.zeros([nobs])
IEobs = np.zeros([nobs],dtype='int32')   #Ingress or Egress
imy35 = 0
for i in range(nobs):
    os.chdir(curr)

    obs1 = observation[i]
    obs = obs1[0:len(obs1)-4]
    obs = obs.upper()

    print(obs)
    os.chdir('PROFILES/')
    runname = obs.lower()

    #Reading files
    npro1,height1,temp1,temperr1,c13ratio1,c13ratioerr1,o18ratio1,o18ratioerr1,o17ratio1,o17ratioerr1 = read_res_co2_dataproduct(runname)
    npro[i] = npro1
    height[0:npro[i],i] = height1[0:npro[i]]
    temp[0:npro[i],i] = temp1[0:npro[i]]
    temperr[0:npro[i],i] = temperr1[0:npro[i]]
    c13prof[0:npro[i],i] = c13ratio1[:]
    c13err[0:npro[i],i] = c13ratioerr1[:]
    o18prof[0:npro[i],i] = o18ratio1[:]
    o18err[0:npro[i],i] = o18ratioerr1[:]
    o17prof[0:npro[i],i] = o17ratio1[:]
    o17err[0:npro[i],i] = o17ratioerr1[:]

    for j in range(nobsd):
        if runname[0:len(runname)-4]==fname[j]:
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

    lat[i] = lat1
    lon[i] = lon1
    Loct[i] = Loct1

    os.chdir(curr)

