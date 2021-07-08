import numpy as np
###############################################################################################

def read_database_dataproduct(filename):

    """

    FUNCTION NAME : read_database_dataproduct()

    DESCRIPTION : Read the database including the observations from pos4

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

def read_res_co2_dataproduct(filename):

    """

    FUNCTION NAME : read_res_co2_dataproduct()

    DESCRIPTION : Read the files created for storing the data products of the pos4 climatology

    INPUTS :

        filename :: Name of the file

    OPTIONAL INPUTS:

    OUTPUTS :

        npro :: Number of altitude levels
        height(npro) :: Altitude (km)
        temp(npro) :: Temperature (K)
        temperr(npro) :: Uncertainty in the temperature (K)
        c13ratio(npro) :: (13C)/(12C) ratio (VSMOW)
        c13ratioerr(npro) :: Uncertainty in (13C)/(12C) ratio (VSMOW)
        o18ratio(npro) :: (18O)/(16O) ratio (VSMOW)
        o18ratioerr(npro) :: Uncertainty in (18O)/(16O) ratio (VSMOW)
        o17ratio(npro) :: (18O)/(16O) ratio (VSMOW)
        o17ratioerr(npro) :: Uncertainty in (18O)/(16O) ratio (VSMOW)

    CALLING SEQUENCE:

        npro,height,temp,temperr,c13ratio,c13ratioerr,o18ratio,o18ratioerr,o17ratio,o17ratioerr = read_res_co2_dataproduct(filename)

    MODIFICATION HISTORY : Juan Alday (10/02/2021)

    """

    npro = file_lines(filename+'.res') - 2

    f = open(filename+'.res','r')
    header = f.readline().split()
    header = f.readline().split()

    height = np.zeros([npro])
    temp = np.zeros([npro])
    temperr = np.zeros([npro])
    c13ratio = np.zeros([npro])
    c13ratioerr = np.zeros([npro])
    o18ratio = np.zeros([npro])
    o18ratioerr = np.zeros([npro])
    o17ratio = np.zeros([npro])
    o17ratioerr = np.zeros([npro])
    for i in range(npro):
        s = f.readline().split()
        height[i] = float(s[0])
        temp[i] = float(s[4])
        temperr[i] = float(s[5])
        c13ratio[i] = float(s[6])
        c13ratioerr[i] = float(s[7])
        o18ratio[i] = float(s[8])
        o18ratioerr[i] = float(s[9])
        o17ratio[i] = float(s[10])
        o17ratioerr[i] = float(s[11])

    f.close()

    return npro,height,temp,temperr,c13ratio,c13ratioerr,o18ratio,o18ratioerr,o17ratio,o17ratioerr

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
