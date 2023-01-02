import numpy as np
###############################################################################################

def read_database_dataproduct(filename):

    """

    FUNCTION NAME : read_database_dataproduct()

    DESCRIPTION : Read the database including the observations from pos6

    INPUTS :

        filename :: Name of the file

    OPTIONAL INPUTS:

    OUTPUTS :

        nobs :: Number of observations in database
        fname :: Name of the files associated with each observation
        orbit :: Orbit number
        IEflag :: Flag indicating whether it was ingress (i) or egress (e)
        Pos :: Secondary grating position
        FPflag :: Flag indicating whether it was a full frame (F) or partial frame (P) observation
        Ls :: Solar longitude (deg)
        Loct :: Local time (h)
        Lat :: Latitude (deg)
        Lon :: Longitude (deg)

    CALLING SEQUENCE:

        nobs,fname,orbit,IEflag,Pos,FPflag,Ls,Loct,Lat,Lon = read_database_dataproduct(filename)

    MODIFICATION HISTORY : Juan Alday (10/02/2021)

    """

    nobs = file_lines(filename) - 1

    f = open(filename,'r')
    header = f.readline().split()

    fname = ['']*nobs
    orbit = np.zeros([nobs],dtype='int32')
    IEflag = ['']*nobs
    Pos = np.zeros([nobs],dtype='int32')
    FPflag = ['']*nobs
    Ls = np.zeros([nobs])
    Loct = np.zeros([nobs])
    Lat = np.zeros([nobs])
    Lon = np.zeros([nobs])

    for i in range(nobs):
        s = f.readline().split()
        fname[i] = s[0]
        orbit[i] = int(s[1])
        IEflag[i] = s[2]
        Pos[i] = int(s[3])
        FPflag[i] = s[4]
        Ls[i] = float(s[5])
        Loct[i] = float(s[6])
        Lat[i] = float(s[7])
        Lon[i] = float(s[8])


    return nobs,fname,orbit,IEflag,Pos,FPflag,Ls,Loct,Lat,Lon

###############################################################################################

def read_res_co_dataproduct(filename):

    """

    FUNCTION NAME : read_res_co_dataproduct()

    DESCRIPTION : Read the files created for storing the data products of the pos6 climatology

    INPUTS :

        filename :: Name of the file

    OPTIONAL INPUTS:

    OUTPUTS :

        npro :: Number of altitude levels
        height(npro) :: Altitude above the Mars areoid (km)
        temp(npro) :: Temperature (K)
        temperr(npro) :: Uncertainty in the temperature (K)
        co_vmr(npro) :: (12C)(16O) volume mixing ratio
        co_err(npro) :: (12C)(16O) volume mixing ratio uncertainty
        co13_vmr(npro) :: (13C)(16O) volume mixing ratio
        co13_err(npro) :: (13C)(16O) volume mixing ratio uncertainty
        co18_vmr(npro) :: (12C)(18O) volume mixing ratio
        co18_err(npro) :: (12C)(18O) volume mixing ratio uncertainty

    CALLING SEQUENCE:

        npro,height,temp,temperr,co_vmr,co_err,co13_vmr,co13_err,co18_vmr,co18_err = read_res_co_dataproduct(filename)

    MODIFICATION HISTORY : Juan Alday (02/01/2022)

    """

    npro = file_lines(filename+'.dat') - 1

    f = open(filename+'.dat','r')
    header = f.readline().split()

    height = np.zeros([npro])
    temp = np.zeros([npro])
    temperr = np.zeros([npro])
    co_vmr = np.zeros([npro])
    co_err = np.zeros([npro])
    co13_vmr = np.zeros([npro])
    co13_err = np.zeros([npro])
    co18_vmr = np.zeros([npro])
    co18_err = np.zeros([npro])
    for i in range(npro):
        s = f.readline().split()
        height[i] = float(s[0])
        temp[i] = float(s[1])
        temperr[i] = float(s[2])
        co_vmr[i] = float(s[3])
        co_err[i] = float(s[4])
        co13_vmr[i] = float(s[5])
        co13_err[i] = float(s[6])
        co18_vmr[i] = float(s[7])
        co18_err[i] = float(s[8])

    f.close()

    return npro,height,temp,temperr,co_vmr,co_err,co13_vmr,co13_err,co18_vmr,co18_err

###############################################################################################

def file_lines(fname):

    """
    FUNCTION NAME : file_lines()

    DESCRIPTION : Returns the number of lines in a given file

    INPUTS : 
 
        fname :: Name of the file

    OPTIONAL INPUTS: none
            
    OUTPUTS : 
 
        nlines :: Number of lines in file

    CALLING SEQUENCE:

        nlines = file_lines(fname)

    MODIFICATION HISTORY : Juan Alday (29/04/2019)

    """

    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

