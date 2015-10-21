import numpy as np
import scipy 
import matplotlib.pyplot as plt
from scipy.io.idl import readsav
from datetime import datetime as dt
#use readsav as you would use idlsave.read.
ssi = readsav('29-Mar-2014-energies-iris-siiv-single-pixel-Oct21-2015.sav', verbose = True) 
smg = readsav('29-Mar-2014-energies-iris-mgii-single-pixel-Oct21-2015.sav', verbose = True) 
sbalmer = readsav('29-Mar-2014-energies-iris-balmer-single-pixel-Oct21-2015.sav', verbose = True) 
smgw = readsav('29-Mar-2014-energies-iris-mgw-single-pixel-Oct21-2015.sav', verbose = True) 
shmi = readsav('29-Mar-2014-energies-hmi-single-pixel-Oct21-2015.sav', verbose = True)
 
dataset = ['si', 'mg', 'balmer', 'mgw', 'hmi']
#dataset = ['si', 'mg', 'mgw', 'hmi']
nrb = 1#20
dtus = 'datetime64[us]'
col = 'b'


#ribbons
#time string format: 29-Mar-2014 17:45:56.500
for j in range(0,nrb):
    jj = str(j)
    s1 = 'ssi.esirb'+jj
    #exec('ssi+jj = s')
    s2 = 'smg.emgrb'+jj
    #exec('smg'+jj+' = s')
    s3 = 'sbalmer.ebalmerrb'+jj
    #exec('sb'+jj+' = s')
    t3 = 'tsprb'+jj
    #exec('tb'+jj+' = tb)   
    s4 = 'smgw.emgwrb'+jj
    #exec('smgw'+jj+' = s')
    s5 = 'shmi.ehmirb'+jj
    #exec('shmi'+jj+' = s')
    tsi = np.zeros((ssi.tsi.shape), dtype='datetime64[us]')
    tmg = np.zeros((smg.tmg.shape), dtype='datetime64[us]')
    tb = np.zeros((sbalmer.tspqk.shape), dtype=dtus)
    tmgw = np.zeros((smgw.tmgw.shape), dtype='datetime64[us]')
    thmi = np.zeros((shmi.thmi.shape), dtype='datetime64[us]')
    for i in range(0,len(ssi.tsi)): 
        tsi[i] = dt.strptime(ssi.tsi[i], '%d-%b-%Y %H:%M:%S.%f')
    for i in range(0,len(smg.tmg)): 
        tmg[i] = dt.strptime(smg.tmg[i], '%d-%b-%Y %H:%M:%S.%f')
    for i in range(0,len(sbalmer.tspqk)): 
        tb[i] = dt.strptime(sbalmer[t3][i], '%Y-%m-%dT%H:%M:%S.%f')
    for i in range(0,len(smgw.tmgw)): 
        tmgw[i] = dt.strptime(smgw.tmgw[i], '%d-%b-%Y %H:%M:%S.%f')
    for i in range(0,len(shmi.thmi)): 
        thmi[i] = dt.strptime(shmi.thmi[i], '%d-%b-%Y %H:%M:%S.%f')
    plt.close('all')
    f, (ax1, ax2, ax3, ax4, ax5) = plt.subplots(5, sharex=True, sharey=True)
    #ax1.plt(x1, y1, color='b')
    exec('ax1.plot(tsi[447:],'+s1+'[447:])')
    ax1.set_title('Energy Over Time')
    #ax2.scatter(x2, y2, color='b')
    exec('ax2.plot(tmg[595:],'+s2+'[595:] )')
    #ax3.scatter(x3, y3, color='b')
    exec('ax3.plot(tb[:],'+s3+'[:])')
    #ax4.scatter(x4, y4, color='b')
    exec('ax4.plot(tmgw[:],'+s4+'[:])')
    #ax5.scatter(x5, y5, color='b')
    exec('ax5.plot(thmi[:],'+s5+'[:])')
    ax5.set_xticks(tsi)
    ax5.set_xticklabels(mytime.strftime('%M:%S.%f') for mytime in tsi)
    # Fine-tune figure; make subplots close to each other and hide x ticks for
    # all but bottom plot.
    f.subplots_adjust(hspace=0)
    plt.setp([a.get_xticklabels() for a in f.axes[:-1]], visible=False)
    # Set common labels
    f.text(0.5, 0.04, 'Time', ha='center', va='center')
    f.text(0.06, 0.5, 'Energy [erg]', ha='center', va='center', rotation='vertical')
    #plt.savefig('energy_ladder_from_rb'+jj+'.png', dpi=300)
    plt.show()




###quake location
x1 = ssi.esiqk
x2 = smg.emgqk
x3 = sbalmer.ebalmerqk
x4 = smgw.emgwqk
x5 = shmi.ehmiqk
 
y1 = ssi.tsi
y2 = smg.tmg
y3 = sbalmer.tspqk
y4 = smgw.tmgw
y5 = shim.thmi

plt.close('all')

f, (ax1, ax2, ax3, ax4) = plt.subplots(4, sharex=True, sharey=True)
ax1.plot(x1, y2, color='b')
ax1.set_title('Energy Over Time')
ax2.scatter(x2, y2, color='b')
ax3.scatter(x3, y3, color='b')
ax4.scatter(x4, y4, color='b')
# Fine-tune figure; make subplots close to each other and hide x ticks for
# all but bottom plot.
f.subplots_adjust(hspace=0)
plt.setp([a.get_xticklabels() for a in f.axes[:-1]], visible=False)

# Set common labels
f.text(0.5, 0.04, 'Time', ha='center', va='center')
f.text(0.06, 0.5, 'Energy [erg]', ha='center', va='center', rotation='vertical')
plt.savefig('energy_ladder_from_qk.png', dpi=300)
plt.show()
