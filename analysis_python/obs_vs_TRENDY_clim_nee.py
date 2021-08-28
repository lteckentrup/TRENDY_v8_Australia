import numpy as np
import netCDF4 as nc
import matplotlib.pyplot as plt
import pandas as pd
from pylab import text
import matplotlib.patches as patches
from matplotlib import gridspec

pathwayIN_trendy = '/srv/ccrc/data02/z5227845/research/Fluxdata/TRENDY/'

fig = plt.figure(figsize=(14.0,12.0))

fig.subplots_adjust(hspace=0.27)
fig.subplots_adjust(wspace=0.25)
fig.subplots_adjust(right=0.98)
fig.subplots_adjust(left=0.07)
fig.subplots_adjust(bottom=0.15)
fig.subplots_adjust(top=0.95)

plt.rcParams['text.usetex'] = False
plt.rcParams['axes.labelsize'] = 12
plt.rcParams['font.size'] = 11
plt.rcParams['legend.fontsize'] = 12
plt.rcParams['xtick.labelsize'] = 11
plt.rcParams['ytick.labelsize'] = 11

ax1 = fig.add_subplot(4,4,1)
ax2 = fig.add_subplot(4,4,2)
ax3 = fig.add_subplot(4,4,3)
ax4 = fig.add_subplot(4,4,4)
ax5 = fig.add_subplot(4,4,5)
ax6 = fig.add_subplot(4,4,6)
ax7 = fig.add_subplot(4,4,7)
ax8 = fig.add_subplot(4,4,8)
ax9 = fig.add_subplot(4,4,9)
ax10 = fig.add_subplot(4,4,10)
ax11 = fig.add_subplot(4,4,11)
ax12 = fig.add_subplot(4,4,12)
ax13 = fig.add_subplot(4,4,13)
ax14 = fig.add_subplot(4,4,14)
ax15 = fig.add_subplot(4,4,15)
ax16 = fig.add_subplot(4,4,16)

sites = ['AU-How', 'AU-DaS', 'AU-Dry', 'AU-Stp']
axes_temp = [ax1, ax2, ax3, ax4]
axes_prec = [ax5, ax6, ax7, ax8]
axes_insol = [ax9, ax10, ax11, ax12]
axes_nee = [ax13, ax14, ax15, ax16]

def compare_obs(var, axes_var):
    for s,a in zip(sites, axes_var):
        CRU = nc.Dataset(pathwayIN_trendy+'CRU_'+var+'_'+s+'.nc')
        OBS = nc.Dataset(pathwayIN_trendy+var+'_OBS_'+s+'.nc')
        CRU_DAY = nc.Dataset(pathwayIN_trendy+'CRU_'+var+'_'+s+'_daily.nc')
        OBS_DAY = nc.Dataset(pathwayIN_trendy+var+'_OBS_'+s+'_daily_noleap.nc')

        df = pd.DataFrame(CRU.variables[var][:,0,0],columns=['cru'])
        df_day = pd.DataFrame(CRU_DAY.variables[var][:,0,0],columns=['cru'])

        if var == 'temp':
            df['obs'] = OBS.variables[var][:,0,0]+273.15
            df_day['obs'] = OBS_DAY.variables[var][:,0,0]+273.15
        else:
            df['obs'] = OBS.variables[var][:,0,0]
            df_day['obs'] = OBS_DAY.variables[var][:,0,0]

        time = np.arange(len(df['obs']))
        a.plot(df['obs'], color = 'tab:blue', label = 'Observation')
        a.plot(df['cru'], color = 'tab:orange', label = 'CRU-JRA')
        a.set_xticks(time[::12])
        a.set_xticklabels([])
        # a.set_title(s + '\n $\mathrm{\\rho_{day}}$ = '+
        #             str(format(df_day['obs'].corr(df_day['cru']), '.2f')) +
        #             '; $\mathrm{\\rho_{mon}}$ = '+
        #             str(format(df['obs'].corr(df['cru']), '.2f')))

        if var == 'temp':
            a.set_title(s + '\n $\mathrm{\\rho_{mon}}$ = '+
                        str(format(df['obs'].corr(df['cru']), '.2f')))
        else:
            a.set_title('$\mathrm{\\rho_{mon}}$ = '+
                        str(format(df['obs'].corr(df['cru']), '.2f')))

        if var == 'temp':
            a.set_ylim([288,307])
        elif var == 'prec':
            a.set_ylim([-10,915])
        elif var == 'insol':
            a.set_ylim([160,330])

compare_obs('temp', axes_temp)
compare_obs('prec', axes_prec)
compare_obs('insol', axes_insol)

models = ['CABLE-POP', 'CLASS-CTEM', 'CLM5.0', 'ISAM', 'ISBA-CTRIP',
               'JSBACH', 'JULES-ES', 'LPX-Bern', 'OCN', 'ORCHIDEE',
               'ORCHIDEE-CNP', 'SDGVM', 'VISIT', 'OBS']
colours = ['tab:blue', 'tab:orange', 'tab:green', 'tab:red', 'tab:purple',
           'tab:brown', 'tab:pink', 'tab:olive', 'navy', 'tab:cyan',
           'rosybrown', 'gold', 'purple', 'k']

for s,a in zip(sites, axes_nee):
    a.axhline(linewidth=1, color='k', alpha = 0.5)
    for m, c in zip(models, colours):
        data = nc.Dataset(pathwayIN_trendy+'nee_'+m+'_'+s+'.nc')
        df = pd.DataFrame(data.variables['nee'][:,0,0],columns=['nee'])
        if m in ('CABLE-POP', 'ISAM', 'JULES-ES', 'ORCHIDEE', 'VISIT'):
            ls = '--'
        elif m in ('CLASS-CTEM', 'ISBA-CTRIP', 'LPX-Bern', 'ORCHIDEE-CNP'):
            ls = '-'
        else:
            ls = '-.'
        time = np.arange(len(df['nee']))
        if m == 'OBS':
            a.plot(df['nee'], color = c, lw = 2.0, label = 'Observation')
        else:
            a.plot(df['nee'], color = c, linestyle=ls, label = m)

    a.set_xticks(time[::12])
    labels = np.arange(2018-(len(df['nee'])/12),2018)
    a.set_xticklabels(labels.astype(int), rotation=90)
    a.set_ylim([-0.19,0.22])

ax1.set_ylabel('Temperature [K]')
ax5.set_ylabel('Precipitation \n [mm month$^{-1}$]')
ax9.set_ylabel('Inc. SW Rad. \n [W m$^{-2}$]')
ax13.set_ylabel('NEE [gC month$^{-1}$]')
ax10.legend(loc='upper center', bbox_to_anchor=(1.0, 0), ncol=2)
ax14.legend(loc='upper center', bbox_to_anchor=(1.1, -0.3), ncol=5)

# plt.show()
plt.savefig('Fig12.pdf')
