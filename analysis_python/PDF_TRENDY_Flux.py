from scipy import stats
import matplotlib.pyplot as plt
import numpy as np
import netCDF4 as nc
import pandas as pd
from glob import glob
from pylab import text
import seaborn as sn
pathwayIN = '/srv/ccrc/data02/z5227845/research/Fluxdata/TRENDY'
pathwayIN_SDGVM = '/srv/ccrc/data02/z5227845/research/Fluxdata/TRENDY_v9'
fig = plt.figure(figsize=(18.5,12.0))

fig.subplots_adjust(hspace=0.25)
fig.subplots_adjust(wspace=0.25)
fig.subplots_adjust(right=0.98)
fig.subplots_adjust(left=0.07)
fig.subplots_adjust(bottom=0.05)
fig.subplots_adjust(top=0.9)

plt.rcParams['text.usetex'] = False
plt.rcParams['axes.labelsize'] = 12
plt.rcParams['font.size'] = 11
plt.rcParams['legend.fontsize'] = 12
plt.rcParams['xtick.labelsize'] = 11
plt.rcParams['ytick.labelsize'] = 11

ax1 = fig.add_subplot(4,6,1)
ax2 = fig.add_subplot(4,6,2)
ax3 = fig.add_subplot(4,6,3)
ax4 = fig.add_subplot(4,6,4)
ax5 = fig.add_subplot(4,6,5)
ax6 = fig.add_subplot(4,6,6)
ax7 = fig.add_subplot(4,6,7)
ax8 = fig.add_subplot(4,6,8)
ax9 = fig.add_subplot(4,6,9)
ax10 = fig.add_subplot(4,6,10)
ax11 = fig.add_subplot(4,6,11)
ax12 = fig.add_subplot(4,6,12)
ax13 = fig.add_subplot(4,6,13)
ax14 = fig.add_subplot(4,6,14)
ax15 = fig.add_subplot(4,6,15)
ax16 = fig.add_subplot(4,6,16)
ax17 = fig.add_subplot(4,6,17)
ax18 = fig.add_subplot(4,6,18)
ax19 = fig.add_subplot(4,6,19)
ax20 = fig.add_subplot(4,6,20)
ax21 = fig.add_subplot(4,6,21)
ax22 = fig.add_subplot(4,6,22)
ax23 = fig.add_subplot(4,6,23)
ax24 = fig.add_subplot(4,6,24)

axes_nee_wet = [ax1, ax7, ax13, ax19]
axes_nee_dry = [ax2, ax8, ax14, ax20]
axes_gpp_wet = [ax3, ax9, ax15, ax21]
axes_gpp_dry = [ax4, ax10, ax16, ax22]
axes_ter_wet = [ax5, ax11, ax17, ax23]
axes_ter_dry = [ax6, ax12, ax18, ax24]

sites = ['AU-How', 'AU-DaS', 'AU-Dry', 'AU-Stp']

models = ['OBS', 'CABLE-POP', 'CLASS-CTEM', 'CLM5.0', 'ISAM', 'ISBA-CTRIP',
          'JSBACH', 'JULES-ES', 'LPX-Bern', 'OCN', 'ORCHIDEE', 'ORCHIDEE-CNP',
          'SDGVM', 'VISIT']

colours = ['k', 'tab:blue', 'tab:orange', 'tab:green', 'tab:red', 'tab:purple',
           'tab:brown', 'tab:pink', 'tab:olive', 'navy', 'tab:cyan', 'rosybrown',
           'gold', 'purple']

def pdf_wet(axes_list, var):
    for a, s in zip(axes_list, sites):
        for m, c in zip(models, colours):
            if m == 'SDGVM':
                data = nc.Dataset(pathwayIN_SDGVM+'/'+var+'_'+m+'_'+s+'.nc')
            else:
                data = nc.Dataset(pathwayIN+'/'+var+'_'+m+'_'+s+'.nc')
            if m == 'OBS':
                df = pd.DataFrame(data.variables[var][:,0,0]*1000,
                                  columns=['Observation'])
                df_season = pd.DataFrame(columns=['Observation'])
            else:
                df = pd.DataFrame(data.variables[var][:,0,0]*1000, columns=[m])
                df_season = pd.DataFrame(columns=[m])

            if axes_list in (axes_nee_wet, axes_gpp_wet, axes_ter_wet):
                if m in ('JSBACH', 'VISIT') and s == 'AU-How':
                    pass
                else:
                    for i in np.arange(0,len(df),12):
                        df_season = df_season.append(df[i:i+4])
                        df_season = df_season.append(df[i+10:i+12])

                if m == 'OBS':
                    a = df_season.plot.kde(ax=a, color=c, lw=3.0, zorder=15)
                elif m in ('JSBACH', 'VISIT') and s == 'AU-How':
                    pass
                else:
                    a = df_season.plot.kde(ax=a, color=c, lw=2.0)

            else:
                if m in ('JSBACH', 'VISIT') and s == 'AU-How':
                    pass
                else:
                    for i in np.arange(0,len(df),12):
                        df_season = df_season.append(df[i+4:i+10])

                if m == 'OBS':
                    a = df_season.plot.kde(ax=a, color=c, lw=3.0, zorder=15)
                elif m in ('JSBACH', 'VISIT') and s == 'AU-How':
                    pass
                else:
                    a = df_season.plot.kde(ax=a, color=c, lw=2.0)

        a.legend().set_visible(False)
        a.set_ylabel('')

pdf_wet(axes_nee_wet, 'nee')
pdf_wet(axes_gpp_wet, 'gpp')
pdf_wet(axes_ter_wet, 'ter')
pdf_wet(axes_nee_dry, 'nee')
pdf_wet(axes_gpp_dry, 'gpp')
pdf_wet(axes_ter_dry, 'ter')

ax16.legend(loc='upper center', bbox_to_anchor=(-0.25, 4.05), ncol=7)

ax1.set_title('Wet')
ax2.set_title('Dry')
ax3.set_title('Wet')
ax4.set_title('Dry')
ax5.set_title('Wet')
ax6.set_title('Dry')

ax1.set_ylabel('AU-How \n (MAP = 1662 mm) \n \n Probability density')
ax7.set_ylabel('AU-DaS \n (MAP = 1324 mm) \n \n Probability density')
ax13.set_ylabel('AU-Dry \n (MAP = 925 mm) \n \n Probability density')
ax19.set_ylabel('AU-Stp \n (MAP = 719 mm) \n \n Probability density')

ax19.set_xlabel('NEE [gC mon-1 m-2]')
ax20.set_xlabel('NEE [gC mon-1 m-2]')
ax21.set_xlabel('GPP [gC mon-1 m-2]')
ax22.set_xlabel('GPP [gC mon-1 m-2]')
ax23.set_xlabel('TER [gC mon-1 m-2]')
ax24.set_xlabel('TER [gC mon-1 m-2]')

ax1.set_xlim([-150,150])
ax2.set_xlim([-150,150])
ax3.set_xlim([-100,400])
ax4.set_xlim([-100,400])
ax5.set_xlim([-50,400])
ax6.set_xlim([-50,400])
ax7.set_xlim([-150,150])
ax8.set_xlim([-150,150])
ax9.set_xlim([-100,400])
ax10.set_xlim([-100,400])
ax11.set_xlim([-50,400])
ax12.set_xlim([-50,400])
ax13.set_xlim([-150,150])
ax14.set_xlim([-150,150])
ax15.set_xlim([-100,400])
ax16.set_xlim([-100,400])
ax17.set_xlim([-50,400])
ax18.set_xlim([-50,400])
ax19.set_xlim([-150,150])
ax20.set_xlim([-150,150])
ax21.set_xlim([-100,400])
ax22.set_xlim([-100,400])
ax23.set_xlim([-50,400])
ax24.set_xlim([-50,400])

ax7.set_ylim([0,0.04])
ax8.set_ylim([0,0.06])
ax9.set_ylim([0,0.03])
ax10.set_ylim([0,0.035])
ax11.set_ylim([0,0.085])
ax12.set_ylim([0,0.085])
# ax1.set_ylim([0,0.07])
# ax2.set_ylim([0,0.07])
# ax3.set_ylim([0,0.04])
# ax4.set_ylim([0,0.04])
# ax5.set_ylim([0,0.14])
# ax6.set_ylim([0,0.14])
# ax7.set_ylim([0,0.06])
# ax8.set_ylim([0,0.06])
# ax9.set_ylim([0,0.035])
# ax10.set_ylim([0,0.035])
# ax11.set_ylim([0,0.085])
# ax12.set_ylim([0,0.085])
# ax13.set_ylim([0,0.07])
# ax14.set_ylim([0,0.07])
# ax15.set_ylim([0,0.055])
# ax16.set_ylim([0,0.055])
# ax17.set_ylim([0,0.095])
# ax18.set_ylim([0,0.095])
# ax19.set_ylim([0,0.12])
# ax20.set_ylim([0,0.12])
# ax21.set_ylim([0,0.037])
# ax22.set_ylim([0,0.135])
# ax23.set_ylim([0,0.085])
# ax24.set_ylim([0,0.085])

axes_wet = [ax1, ax7, ax13, ax19, ax3, ax9, ax15, ax21, ax5, ax11, ax17, ax23]
axes_dry = [ax2, ax8, ax14, ax20, ax4, ax10, ax16, ax22, ax6, ax12, ax18, ax24]

for aw in axes_wet:
    aw.set_facecolor('#ccdaf1')

for ad in axes_dry:
    ad.set_facecolor('#f1ccda')
# plt.show()
plt.savefig('pdf_wet_dry_SDGVM_v9.pdf')
