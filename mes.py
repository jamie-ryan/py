import numpy as np
import scipy 
import matplotlib.pyplot as plt
from scipy.io.idl import readsav
from datetime import datetime as dt

###read in idl sav files
#use readsav as you would use idlsave.read.
irissj = readsav('iris-16-03-15.sav', verbose = True) 
irissg = readsav('sp2826-Apr28-2015.sav', verbose = True) 
hmi = readsav('hmi-12-05-15.sav', verbose = True)
#HMI-diff-15-Oct-15.sav

#time_frames = the number of time frames that ribbon coords have been sampled from.
#nsi, nmg, nbalm, nmgw, nhim are the number of ribbon coords for each data set. I think this is the bast way, as each data set has different sized ribbons, therefore it is unreasonable to assume that one spatial coord could relate to that of another dataset. So instead, I am going to produce high resolution energy distribution plots for each dataset, looking for common features. This approach should help to highlight regions in each dataset-ribbons that are related. i.e, there's a peak here and a trough to the right, there's the same feature in the ribbon above and below (in altitude)



#below this line needs converting from idl to python
##########################################################################
###date string

###directories
pltdir = '/disk/solar3/jsr2/Data/SDO/DATA-ANALYSIS/plots/'
datdir = '/disk/solar3/jsr2/Data/SDO/DATA-ANALYSIS/Dat/'

###iris spectra fits
fsp = findfile('/disk/solar3/jsr2/Data/IRIS/*raster*.fits')

sample = 1


###arrays to contain energy values for each coord through the entire time series.
#eg: sidata[0, x, y]
sidata = fltarr(time_frames,nsi,nsi)
mgdata = fltarr(time_frames,nmg,n_elements(tmg))
balmerdata = fltarr(time_frames,nbalm,n_elements(tspqk))
mgwdata = fltarr(time_frames,nmgw,n_elements(tmgw))
hmidata = fltarr(time_frames,nhmi,n_elements(thmi))

###make n for loops
nmg = n_elements(submg) #nmg = n_elements(submg[17:*])
nmgw = n_elements(diff2832)
nsi = n_elements(map1400) #nsi = n_elements(map1400[387:*])
nn = n_elements(fsp)
nnn = n_elements(diff)
nrb = 20 # number of ribbon sample points
nc = nrb/2

###calculate pixel location from given arcsec coords
#SDO HMI#############
#####################
#quake position

hqkxa = 517.2 #my old coords for hmi
hqkya = 261.4 #my old coords for hmi
qkxa = 518.5 #Donea et al 2014
qkya = 264.0 #Donea et al 2014
hqkxp = convert_coord_hmi(hqkxa, diffindex[63],  /x, /a2p)
hqkyp = convert_coord_hmi(hqkya, diffindex[63],  /y, /a2p)
qkxp = convert_coord_hmi(qkxa, diffindex[63],  /x, /a2p)
qkyp = convert_coord_hmi(qkya, diffindex[63],  /y, /a2p)
qksixp = convert_coord_iris(qkxa, sji_1400_hdr[498], /x, /a2p)
qksixa = convert_coord_iris(qkxa, sji_1400_hdr[498], /x, /p2a)
qksiyp = convert_coord_iris(qkya, sji_1400_hdr[498], /y, /a2p)
qkmgxp = convert_coord_iris(qkxa, sji_2796_hdr[664], /x, /a2p)
qkmgxa = convert_coord_iris(qkxa, sji_2796_hdr[664], /x, /p2a)
qkmgyp = convert_coord_iris(qkya, sji_2796_hdr[664], /y, /a2p)
qkmgwxp = convert_coord_iris(qkxa, sji_2832_hdr[167], /x, /a2p)
qkmgwxa = convert_coord_iris(qkxa, sji_2832_hdr[167], /x, /p2a)
qkmgwyp = convert_coord_iris(qkya, sji_2832_hdr[167], /y, /a2p)
#qkslitp = #find_iris_slit_pos(qkxa,sp2826)
#qkspyp = #find_iris_slit_pos(qkya,sp2826, /y, /a2p)


###read in coord files for each data set
###(to change coords ammend file, eg, hmicoords1.txt)
###based on naming convention (no zero, always start with 1), eg, hmicoords1, hmicoords2, hmicoords3 etc.
dataset = ['si', 'mg', 'balmer', 'mgw', 'hmi']
for i = 1,time_frames do begin
    ii = string(i, format = '(I0)')
    for k = 0, n_elements(dataset)-1 do begin
        flnm = dataset[k]+'coords'+ii+'.txt' #eg, flnm=hmicoords1.txt
        openr, lun, flnm, /get_lun
        nlin =  file_lines(flnm)
        tmp = fltarr(2, nlin)
        readf, lun, tmp
        com = dataset[k]+'coords'+ii+ '= tmp' #readf,lun,hmg
        exe = execute(com)
        free_lun, lun
    endfor
endfor










end
