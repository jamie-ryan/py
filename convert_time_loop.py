import numpy as np
import scipy 
import matplotlib.pyplot as plt
from scipy.io.idl import readsav
from datetime import datetime as dt
#use readsav as you would use idlsave.read.
ssi = readsav('29-Mar-2014-energies-iris-siiv-single-pixel-Oct21-2015.sav', verbose = True) 
smg = readsav('29-Mar-2014-energies-iris-mg-single-pixel-Oct21-2015.sav', verbose = True) 
sbalmer = readsav('29-Mar-2014-energies-iris-balmer-single-pixel-Oct21-2015.sav', verbose = True) 
smgw = readsav('29-Mar-2014-energies-iris-mgw-single-pixel-Oct21-2015.sav', verbose = True) 
shmi = readsav('29-Mar-2014-energies-hmi-single-pixel-Oct21-2015.sav', verbose = True)
 

dataset = ['si', 'mg', 'balmer', 'mgw', 'hmi']
dataset = ['si', 'mg', 'mgw', 'hmi']
nrb = 20

for j in range(0, len(dataset)):
    st = 's'+dataset[j]+'.t'+dataset[j]
    t = np.zeros((st.shape), dtype='datetime64[us]')
    for i in range(0,len(st)): 
        t[i] = dt.strptime(st[i], '%d-%b-%Y %H:%M:%S.%f')
    exec('t'+dataset[j]+' = t')



s.t
s['t']
s.'t'
