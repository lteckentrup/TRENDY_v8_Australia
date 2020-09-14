from scipy import stats
import matplotlib.pyplot as plt
import numpy as np
import netCDF4 as nc
import pandas as pd
from glob import glob

pathwayIN = '/srv/ccrc/data02/z5227845/research/Fluxdata/TRENDY/'

fig = plt.figure(figsize=(13.5,12.0))

fig.subplots_adjust(hspace=0.15)
fig.subplots_adjust(wspace=0.25)
fig.subplots_adjust(right=0.98)
fig.subplots_adjust(left=0.06)
fig.subplots_adjust(bottom=0.15)
fig.subplots_adjust(top=0.85)

plt.rcParams['text.usetex'] = False
plt.rcParams['axes.labelsize'] = 12
plt.rcParams['font.size'] = 11
plt.rcParams['legend.fontsize'] = 12
plt.rcParams['xtick.labelsize'] = 11
plt.rcParams['ytick.labelsize'] = 11

ax1 = fig.add_subplot(3,4,1)
ax2 = fig.add_subplot(3,4,2)
ax3 = fig.add_subplot(3,4,3)
ax4 = fig.add_subplot(3,4,4)
ax5 = fig.add_subplot(3,4,5)
ax6 = fig.add_subplot(3,4,6)
ax7 = fig.add_subplot(3,4,7)
ax8 = fig.add_subplot(3,4,8)
ax9 = fig.add_subplot(3,4,9)
ax10 = fig.add_subplot(3,4,10)
ax11 = fig.add_subplot(3,4,11)
ax12 = fig.add_subplot(3,4,12)

axes_pdf = [ax1, ax2 ,ax3, ax4]
axes_boxplot = [ax5, ax6, ax7, ax8]
axes_boxplot_annual = [ax9, ax10, ax11, ax12]

sites = ['AU-How', 'AU-DaS', 'AU-Dry', 'AU-Stp']

models = ['CABLE-POP', 'CLASS-CTEM', 'CLM5.0', 'ISAM', 'ISBA-CTRIP', 'JSBACH',
          'JULES-ES', 'LPX-Bern', 'OBS', 'OCN', 'ORCHIDEE-CNP', 'ORCHIDEE',
          'SDGVM', 'VISIT']

colours = ['tab:blue', 'tab:orange', 'tab:green', 'tab:red', 'tab:purple',
           'tab:brown', 'tab:pink', 'tab:olive', 'k', 'navy', 'tab:cyan',
           'rosybrown', 'gold', 'purple']

model_labels = ['OBS', 'CABLE-POP', 'CLASS-CTEM', 'CLM5.0', 'ISAM', 'ISBA-CTRIP',
                'JSBACH', 'JULES-ES', 'LPX-Bern', 'OCN', 'ORCHIDEE',
                'ORCHIDEE-CNP', 'SDGVM', 'VISIT']

for a, s in zip(axes_pdf, sites):
    for m, c in zip(models, colours):
        if m == 'SDGVM' and s in ('AU-DaS', 'AU-Dry', 'AU-Stp'):
            pass
        elif m == 'CLM5.0' and s == 'AU-DaS':
            pass
        elif m in ('JSBACH', 'VISIT') and s == 'AU-How':
            pass
        elif m == 'OBS':
            CRU = nc.Dataset(pathwayIN+s+'/'+m+'_'+s+'.nc')
            df = pd.DataFrame(CRU.variables['nee'][:,0,0],
                              columns=['Observation'])
            a = df.plot.kde(ax=a, color=c, lw=3.0)

        else:
            CRU = nc.Dataset(pathwayIN+s+'/'+m+'_'+s+'.nc')
            df = pd.DataFrame(CRU.variables['nee'][:,0,0],columns=[m])
            a = df.plot.kde(ax=a, color=c, lw=2.0)

    a.legend().set_visible(False)
    a.set_xlim([-0.2,0.2])
    a.set_ylim([0,48])
    if a == ax1:
        a.set_ylabel('Monthly \n KDE PD')
    else:
        a.set_ylabel('')

def boxplot(axis, site, temp_res):
    filenames = sorted(glob(pathwayIN+site+'/*nc'))
    df = pd.DataFrame(columns=models)

    for f, m in zip(filenames, models):
        if temp_res == 'Monthly':
            data = nc.Dataset(f).variables['nee'][:,0,0]
        elif temp_res == 'Annual':
            data = nc.Dataset(f).variables['nee'][6:-6,0,0]
        else:
            pass

        df[m] = data

    if temp_res == 'Monthly':
        axis.set_ylim([-0.25,0.25])

        if axis == ax5:
            axis.set_ylabel(temp_res+' NEE [gc mon-1]')
        else:
            axis.set_ylabel('')

    elif temp_res == 'Annual':
        df = df.groupby(df.index // 12).sum()

        axis.set_ylim([-0.7,0.6])

        if axis == ax9:
            axis.set_ylabel('Annual NEE [gc yr-1]')
        else:
            axis.set_ylabel('')
    else:
        pass

    axis.axhline(linewidth=1, color='k', alpha = 0.5)

    boxplots = axis.boxplot([df['OBS'], df['CABLE-POP'],
                             df['CLASS-CTEM'], df['CLM5.0'], df['ISAM'],
                             df['ISBA-CTRIP'], df['JSBACH'], df['JULES-ES'],
                             df['LPX-Bern'], df['OCN'], df['ORCHIDEE'],
                             df['ORCHIDEE-CNP'], df['SDGVM'], df['VISIT']],
                            labels=models, widths = .7, patch_artist=True,
                            medianprops = dict(linestyle='-', linewidth=2,
                            color='Yellow'), boxprops = dict(linestyle='--',
                            linewidth=2, color='Black', facecolor='green',
                            alpha=.8))

    if temp_res == 'Monthly':
        axis.set_xticklabels('')
    else:
        axis.set_xticklabels(labels=models, rotation=90, ha='center')
    boxplot1 = boxplots['boxes'][0]
    boxplot1.set_facecolor('black')
    boxplot2 = boxplots['boxes'][1]
    boxplot2.set_facecolor('tab:blue')
    boxplot3 = boxplots['boxes'][2]
    boxplot3.set_facecolor('tab:orange')
    boxplot4 = boxplots['boxes'][3]
    boxplot4.set_facecolor('tab:green')
    boxplot5 = boxplots['boxes'][4]
    boxplot5.set_facecolor('tab:red')
    boxplot6 = boxplots['boxes'][5]
    boxplot6.set_facecolor('tab:purple')
    boxplot7 = boxplots['boxes'][6]
    boxplot7.set_facecolor('tab:brown')
    boxplot8 = boxplots['boxes'][7]
    boxplot8.set_facecolor('tab:pink')
    boxplot9 = boxplots['boxes'][8]
    boxplot9.set_facecolor('tab:olive')
    boxplot10 = boxplots['boxes'][9]
    boxplot10.set_facecolor('navy')
    boxplot11 = boxplots['boxes'][10]
    boxplot11.set_facecolor('tab:cyan')
    boxplot12 = boxplots['boxes'][11]
    boxplot12.set_facecolor('rosybrown')
    boxplot13 = boxplots['boxes'][12]
    boxplot13.set_facecolor('gold')
    boxplot14 = boxplots['boxes'][13]
    boxplot14.set_facecolor('purple')

for a, s in zip(axes_boxplot, sites):
    boxplot(a, s, 'Monthly')

for a, s in zip(axes_boxplot_annual, sites):
    boxplot(a, s, 'Annual')

ax4.legend(loc='upper center', bbox_to_anchor=(-1.3, 1.7), ncol=4)

ax1.set_title('AU-How (MAP = 1700 mm)')
ax2.set_title('AU-DaS (MAP = 1170 mm)')
ax3.set_title('AU-Dry (MAP = 895 mm)')
ax4.set_title('AU-Stp (MAP = 640 mm)')

plt.show()
