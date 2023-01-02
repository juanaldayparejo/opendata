#Routine to read all profiles
from readfiles_co import *
import numpy as np
import matplotlib.pyplot as plt
import os,sys

curr = os.getcwd()  #Current directory

#Reading the parameters of the observations
filename = 'ACSMIR_CO_Database.txt'
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
co_vmr = np.zeros([maxpro,nobs])
co_err = np.zeros([maxpro,nobs])
co18_vmr = np.zeros([maxpro,nobs])
co18_err = np.zeros([maxpro,nobs])
co13_vmr = np.zeros([maxpro,nobs])
co13_err = np.zeros([maxpro,nobs])
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
    runname = obs

    #Reading files
    npro1,height1,temp1,temperr1,co_vmr1,co_err1,co13_vmr1,co13_err1,co18_vmr1,co18_err1 = read_res_co_dataproduct(runname)
    npro[i] = npro1
    height[0:npro[i],i] = height1[0:npro[i]]
    temp[0:npro[i],i] = temp1[0:npro[i]]
    temperr[0:npro[i],i] = temperr1[0:npro[i]]
    co_vmr[0:npro[i],i] = co_vmr1[:]
    co_err[0:npro[i],i] = co_err1[:]
    co13_vmr[0:npro[i],i] = co13_vmr1[:]
    co13_err[0:npro[i],i] = co13_err1[:]
    co18_vmr[0:npro[i],i] = co18_vmr1[:]
    co18_err[0:npro[i],i] = co18_err1[:]

    for j in range(nobsd):
        if runname[0:len(runname)-3]==fname[j]:
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


#Making summary figure
fig,(ax1,ax2) = plt.subplots(1,2,figsize=(10,6))
VPDB = 0.0112372
VSMOW = 2005.2e-6
for i in range(nobs):
    ax1.plot((co13_vmr[0:npro[i],i]/co_vmr[0:npro[i],i])/VPDB,height[0:npro[i],i],linewidth=0.5,c='tab:blue')
    ax2.plot((co18_vmr[0:npro[i],i]/co_vmr[0:npro[i],i])/VSMOW,height[0:npro[i],i],linewidth=0.5,c='tab:orange')
ax1.grid()
ax2.grid()
ax1.set_xlabel('$^{13}$C/$^{12}$C (VPDB)')
ax1.set_ylabel('Altitude (km)')
ax2.set_xlabel('$^{18}$O/$^{16}$O (VSMOW)')
ax2.set_ylabel('Altitude (km)')
ax1.set_xlim(0.0,2.0)
ax2.set_xlim(0.0,2.0)
plt.tight_layout()
fig.savefig('co_isotopes.png',dpi=300)

