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

def read_res_h2o_dataproduct(filename):

    """

    FUNCTION NAME : read_res_h2o_dataproduct()

    DESCRIPTION : Read the files created for storing the data products of the pos4 climatology

    INPUTS :

        filename :: Name of the file

    OPTIONAL INPUTS:

    OUTPUTS :

        npro :: Number of altitude levels
        height(npro) :: Altitude (km)
        press(npro) :: Pressure (mbar)
        temp(npro) :: Temperature (K)
        temperr(npro) :: Uncertainty in the temperature (K)
        numdens(npro) :: Number density (m-3)
        numdenserr(npro) :: Uncertainty in number density (m-3)
        h2oprof(npro) :: H2O volume mixing ratio
        h2oerr(npro) :: Uncertainty in H2O volume mixing ratio
        dhratio(npro) :: D/H ratio (VSMOW)
        dhratioerr(npro) :: Uncertainty in D/H ratio (VSMOW)
        o18ratio(npro) :: (18O)/(16O) ratio (VSMOW)
        o18ratioerr(npro) :: Uncertainty in (18O)/(16O) ratio (VSMOW)
 
    CALLING SEQUENCE:

        npro,height,press,temp,temperr,numdens,numdenserr,h2oprof,h2oerr,dhratio,dhratioerr,o18ratio,o18ratioerr = read_res_h2o_dataproduct(filename)

    MODIFICATION HISTORY : Juan Alday (10/02/2021)

    """

    npro = file_lines(filename+'.dat') - 1

    f = open(filename+'.dat','r')
    header = f.readline().split()


    height = np.zeros([npro])
    press = np.zeros([npro])
    temp = np.zeros([npro])
    temperr = np.zeros([npro])
    numdens = np.zeros([npro])
    numdenserr = np.zeros([npro])
    h2oprof = np.zeros([npro])
    h2oerr = np.zeros([npro])
    dhratio = np.zeros([npro])
    dhratioerr = np.zeros([npro])
    o18ratio = np.zeros([npro])
    o18ratioerr = np.zeros([npro])
    for i in range(npro):
        s = f.readline().split()
        height[i] = float(s[0])
        press[i] = float(s[1])
        temp[i] = float(s[2])
        temperr[i] = float(s[3])
        numdens[i] = float(s[4])
        numdenserr[i] = float(s[5])
        h2oprof[i] = float(s[6])
        h2oerr[i] = float(s[7])
        dhratio[i] = float(s[8])
        dhratioerr[i] = float(s[9])
        o18ratio[i] = float(s[10])
        o18ratioerr[i] = float(s[11])


    f.close()

    return npro,height,press,temp,temperr,numdens,numdenserr,h2oprof,h2oerr,dhratio,dhratioerr,o18ratio,o18ratioerr

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
