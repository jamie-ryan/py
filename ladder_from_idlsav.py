import numpy as np
import scipy 
import matplotlib.pyplot as plt
from scipy.io.idl import readsav
from datetime import datetime as dt
from matplotlib.dates import DateFormatter

#use readsav as you would use idlsave.read.
filepath = '/unsafe/jsr2/'
ssi = readsav(filepath+'29-Mar-2014-energies-iris-siiv-single-pixel-Oct23-2015.sav', verbose = True) 
smg = readsav(filepath+'29-Mar-2014-energies-iris-mgii-single-pixel-Oct23-2015.sav', verbose = True) 
sbalmer = readsav(filepath+'29-Mar-2014-energies-iris-balmer-single-pixel-Oct23-2015.sav', verbose = True) 
smgw = readsav(filepath+'29-Mar-2014-energies-iris-mgw-single-pixel-Oct23-2015.sav', verbose = True) 
shmi = readsav(filepath+'29-Mar-2014-energies-hmi-single-pixel-Oct23-2015.sav', verbose = True)
 
dataset = ['si', 'mg', 'balmer', 'mgw', 'hmi']
#dataset = ['si', 'mg', 'mgw', 'hmi']
nrb = 1#20


hmfmt = DateFormatter('%H:%M')
#ribbons
#time string format: 29-Mar-2014 17:45:56.500
tsi = [dt.strptime(ti, '%d-%b-%Y %H:%M:%S.%f') for ti in ssi.tsi]
tmg = [dt.strptime(ti, '%d-%b-%Y %H:%M:%S.%f') for ti in smg.tmg]
tmgw = [dt.strptime(ti, '%d-%b-%Y %H:%M:%S.%f') for ti in smgw.tmgw]
thmi = [dt.strptime(ti, '%d-%b-%Y %H:%M:%S.%f') for ti in shmi.thmi]

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
    tb = [dt.strptime(ti, '%Y-%m-%dT%H:%M:%S.%f') for ti in sbalmer[t3]]
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
    #ax5.set_xticks(tsi)
    #ax5.set_xticklabels(mytime.strftime('%M:%S.%f') for mytime in tsi)
    # Fine-tune figure; make subplots close to each other and hide x ticks for
    # all but bottom plot.
    f.subplots_adjust(hspace=0)
    plt.setp([a.get_xticklabels() for a in f.axes[:-1]], visible=False)
    #for axi in f.axes:
    #    axi.set_xlim([dt(2014, 3, 29, 17, 26), dt(2014, 3, 29, 17, 55)])
    #plt.setp([a.get_xlim() for a in f.axes[:]],[dt(2014, 3, 29, 17, 26), dt(2014, 3, 29, 17, 55)])
    # Set common labels
    f.text(0.5, 0.04, 'Time', ha='center', va='center')
    f.text(0.06, 0.5, 'Energy [erg]', ha='center', va='center', rotation='vertical')
    ax5.xaxis.set_major_formatter(hmfmt) # Set the xaxis format
    #plt.savefig('energy_ladder_from_rb'+jj+'.png', dpi=300)
    plt.show()


###quake location
y1 = ssi.esiqk
y2 = smg.emgqk
y3 = sbalmer.ebalmerqk
y4 = smgw.emgwqk
y5 = shmi.ehmiqk
plt.close('all')
f, (ax1, ax2, ax3, ax4, ax5) = plt.subplots(5, sharex=True, sharey=True)
ax1.plot(tsi[447:],y1[447:])
ax1.set_title('Energy Over Time')
ax2.plot(tmg[595:],y2[595:] )
ax3.plot(tb[:],y3[:])
ax4.plot(tmgw[:],y4[:])
ax5.plot(thmi[:],s5[:])

# Fine-tune figure; make subplots close to each other and hide x ticks for
# all but bottom plot.
f.subplots_adjust(hspace=0)
plt.setp([a.get_xticklabels() for a in f.axes[:-1]], visible=False)
#for axi in f.axes:
#    axi.set_xlim([dt(2014, 3, 29, 17, 26), dt(2014, 3, 29, 17, 55)])
#plt.setp([a.get_xlim() for a in f.axes[:]],[dt(2014, 3, 29, 17, 26), dt(2014, 3, 29, 17, 55)])
# Set common labels
f.text(0.5, 0.04, 'Time', ha='center', va='center')
f.text(0.06, 0.5, 'Energy [erg]', ha='center', va='center', rotation='vertical')
ax5.xaxis.set_major_formatter(hmfmt) # Set the xaxis format
#plt.savefig('energy_ladder_from_rb'+jj+'.png', dpi=300)
plt.show()



