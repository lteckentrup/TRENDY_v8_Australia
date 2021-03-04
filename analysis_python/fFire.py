import numpy as np
import netCDF4 as nc
import matplotlib.pyplot as plt
import pandas as pd
from pylab import text
import matplotlib.patches as patches
from matplotlib import gridspec
from mask import (
    mask,
    total_mask,
    )

pathwayIN_trendy = '/srv/ccrc/data02/z5227845/research/TRENDY_v8/impact_analysis/'
pathwayIN_gosif = '/srv/ccrc/data02/z5227845/research/SIF/TRENDY_comparison/'

fig = plt.figure(figsize=(9.0,8.5))

fig.subplots_adjust(hspace=0.2)
fig.subplots_adjust(wspace=0.25)
fig.subplots_adjust(right=0.90)
fig.subplots_adjust(left=0.1)
fig.subplots_adjust(bottom=0.16)
fig.subplots_adjust(top=0.95)

plt.rcParams['text.usetex'] = False
plt.rcParams['axes.labelsize'] = 12
plt.rcParams['font.size'] = 11
plt.rcParams['legend.fontsize'] = 12
plt.rcParams['xtick.labelsize'] = 11
plt.rcParams['ytick.labelsize'] = 11

ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,2,3)
ax3 = fig.add_subplot(2,2,4)

### Modelspread

model_names = ['CLASS-CTEM', 'CLM5.0', 'ISBA-CTRIP', 'JSBACH', 'LPX-Bern',
               'SDGVM', 'VISIT', 'CAMS_GFAS', 'GFED4s']
colours = ['tab:orange', 'tab:green', 'tab:purple', 'tab:brown', 'tab:olive',
           'gold', 'purple', 'k', 'tab:grey']

df_monthly = pd.DataFrame()
df_annual = pd.DataFrame()

dataframes = [df_monthly, df_annual]
time_res = ['monthly', 'annual']
test = mask('monthly', 'S3', 'fFire', total_mask, 'CLASS-CTEM')

for df, tr in zip(dataframes, time_res):
    df['CLASS-CTEM'] = mask(tr, 'S3', 'fFire', total_mask, 'CLASS-CTEM')
    df['CLM5.0'] = mask(tr, 'S3', 'fFire', total_mask, 'CLM5.0')
    df['ISBA-CTRIP'] = mask(tr, 'S3', 'fFire', total_mask, 'ISBA-CTRIP')
    df['JSBACH'] = mask(tr, 'S3', 'fFire', total_mask, 'JSBACH')
    df['LPX-Bern'] = mask(tr, 'S3', 'fFire', total_mask, 'LPX-Bern')
    df['SDGVM'] = mask(tr, 'S3', 'fFire', total_mask, 'SDGVM')
    df['VISIT'] = mask(tr, 'S3', 'fFire', total_mask, 'VISIT')
    df['CAMS_GFAS'] = mask(tr, '', 'co2fire', total_mask, 'CAMS_GFAS')

df_gfed = pd.read_csv('../../GFED4s/GFED4s_monthly.csv')
GFED4s_monthly = df_gfed.stack().to_numpy()
GFED4s_annual = np.sum(GFED4s_monthly[6:-18].reshape(-1, 12), axis=1)

df_monthly['GFED4s'] = GFED4s_monthly[:-12].tolist()
df_annual['GFED4s'] = GFED4s_annual.tolist()

df_annual['year'] = np.arange(2003,2018,1)

axis2 = ax1.twinx()
for mn, c in zip(model_names, colours):
    df_monthly[mn+'_scaled'] = (df_monthly[mn]-df_monthly[mn].min())/ \
                               (df_monthly[mn].max()-df_monthly[mn].min())
    if mn in ('CAMS_GFAS', 'GFED4s'):
        axis2.plot(df_monthly[mn], color=c, lw=2.0, label=mn)
        ax2 = df_monthly[mn+'_scaled'].plot.kde(ax=ax2, color=c, lw=3.0,
                                                label=mn)
    else:
        ax1.plot(df_monthly[mn], color=c, lw=2.0, label=mn)
        ax2 = df_monthly[mn+'_scaled'].plot.kde(ax=ax2, color=c, lw=3.0,
                                                label=mn)

    ax3.plot(df_annual['year'], df_annual[mn],lw=2.0, ls="-", color=c, label=mn)

xlabels = np.arange(2003,2019,1)

ax1.set_xticks(np.arange(0, 169, step=12))
ax1.set_xticklabels(xlabels)
ax1.set_ylabel('$\mathrm{fFire_{trendy}}$ [PgC mon-1]')
ax1.set_title('a) Monthly fire $\mathrm{CO_2}$ emissions')

axis2.set_ylabel('$\mathrm{fFire_{obs}}$ [PgC mon-1]')

ax2.set_xlim([-0.2,1.6])
ax2.set_xlabel('fFire [-]')
ax2.set_ylabel('Probability density')
ax2.set_title('b) Normalised monthly fire $\mathrm{CO_2}$ emissions')
ax2.legend(loc='upper center', bbox_to_anchor=(1.1, -0.15), ncol=3)

xlabels = np.arange(2003,2018,1)
ax3.set_ylabel('fFire [PgC yr-1]')
ax3.set_xticklabels(xlabels)
ax3.set_title('c) Annual fire $\mathrm{CO_2}$ emissions')

rect1 = patches.Rectangle((18,-0.5),8,8,linewidth=1,edgecolor='tab:red',
                          facecolor='tab:red', alpha = 0.4)
rect2 = patches.Rectangle((44,-0.5),5,8,linewidth=1,edgecolor='tab:red',
                          facecolor='tab:red', alpha = 0.4)
rect3 = patches.Rectangle((78,-0.5),9,8,linewidth=1,edgecolor='tab:red',
                          facecolor='tab:red', alpha = 0.4)
rect4 = patches.Rectangle((142,-0.5),19,8,linewidth=1,edgecolor='tab:red',
                          facecolor='tab:red', alpha = 0.4)
rect5 = patches.Rectangle((34,-0.5),5,8,linewidth=1,edgecolor='tab:blue',
                          facecolor='tab:blue', alpha = 0.4)
rect6 = patches.Rectangle((54,-0.5),12,8,linewidth=1,edgecolor='tab:blue',
                          facecolor='tab:blue', alpha = 0.4)
rect7 = patches.Rectangle((89,-0.5),22,8,linewidth=1,edgecolor='tab:blue',
                          facecolor='tab:blue', alpha = 0.4)
rect8 = patches.Rectangle((163,-0.5),5,8,linewidth=1,edgecolor='tab:blue',
                          facecolor='tab:blue', alpha = 0.4)

patches = [rect1, rect2, rect3, rect4, rect5, rect6, rect7, rect8]

for p in patches:
    ax1.add_patch(p)

plt.show()
# plt.savefig('fFire_S3_australia.pdf')
