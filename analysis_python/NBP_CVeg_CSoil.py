import numpy as np
import netCDF4 as nc
import matplotlib.pyplot as plt
import pandas as pd
from pylab import text
from mask import (
    mask,
    tropics_mask,
    savanna_mask,
    warm_temperate_mask,
    cool_temperate_mask,
    mediterranean_mask,
    desert_mask,
    total_mask,
    model_names,
    colours,
    titles,
    veg_masks
    )

fig = plt.figure(figsize=(10.0,10))

fig.subplots_adjust(hspace=0.12)
fig.subplots_adjust(wspace=0.18)
fig.subplots_adjust(right=0.98)
fig.subplots_adjust(left=0.08)
fig.subplots_adjust(bottom=0.17)
fig.subplots_adjust(top=0.94)

plt.rcParams['text.usetex'] = False
plt.rcParams['axes.labelsize'] = 12
plt.rcParams['font.size'] = 11
plt.rcParams['legend.fontsize'] = 12
plt.rcParams['xtick.labelsize'] = 11
plt.rcParams['ytick.labelsize'] = 11

ax1 = fig.add_subplot(2,2,1)
ax2 = fig.add_subplot(2,2,2)
ax3 = fig.add_subplot(2,2,3)
ax4 = fig.add_subplot(2,2,4)

df_NBP = pd.DataFrame()
df_CVeg = pd.DataFrame()
df_CSoil = pd.DataFrame()

dataframes = [df_NBP, df_CVeg, df_CSoil]
vars = ['nbp', 'cVeg', 'cSoil']

for df, v in zip(dataframes, vars):
    df['CABLE-POP'] = mask(v, total_mask, 'CABLE-POP')
    df['CLASS-CTEM'] = mask(v, total_mask, 'CLASS-CTEM')
    df['CLM5.0'] = mask(v, total_mask, 'CLM5.0')
    df['ISAM'] = mask(v, total_mask, 'ISAM')
    df['ISBA-CTRIP'] = mask(v, total_mask, 'ISBA-CTRIP')
    df['JSBACH'] = mask(v, total_mask, 'JSBACH')
    df['JULES-ES'] = mask(v, total_mask, 'JULES-ES')
    df['LPX-Bern'] = mask(v, total_mask, 'LPX-Bern')
    df['OCN'] = mask(v, total_mask, 'OCN')
    df['ORCHIDEE'] = mask(v, total_mask, 'ORCHIDEE')
    df['ORCHIDEE-CNP'] = mask(v, total_mask, 'ORCHIDEE-CNP')
    df['SDGVM'] = mask(v, total_mask, 'SDGVM')
    df['VISIT'] = mask(v, total_mask, 'VISIT')

df_NBP['max'] = df_NBP.max(axis=1)
df_NBP['min'] = df_NBP.min(axis=1)
df_NBP['mean'] = df_NBP.mean(axis=1)

df_NBP['year'] = np.arange(1901,2018)

ax1.plot(df_NBP['year'], df_NBP['mean'],lw=3.0, ls="-",
         label = 'TRENDY ensemble mean', alpha = 1, color = 'tab:green')

ax1.fill_between(df_NBP['year'], df_NBP['min'], df_NBP['max'],
                 color =  'tab:green', alpha = 0.15, label = 'Model spread')

## Cumulative sum individual models
for mn, c in zip(model_names, colours):
    ax2.plot(df_NBP['year'], df_NBP[mn].cumsum(), color = c,
             lw = 2.0, label = mn)
    ax3.plot(df_NBP['year'],df_CVeg[mn], color = c, lw = 2.0, label = mn)
    ax4.plot(df_NBP['year'],df_CSoil[mn], color = c, lw = 2.0, label = mn)

obs = mask('Aboveground Biomass Carbon', total_mask, mn)
ax3.plot(df_NBP['year'][-25:-6], obs, color = 'k', lw = 4.0, label = 'VOD')

ax1.axhline(linewidth=2, color='k', alpha = 0.5)
ax1.set_xticklabels([])
ax1.set_ylim([-0.95,1.7])
ax1.set_ylabel('NBP [PgC yr-1]')
ax1.legend(loc='upper left', ncol=1, fancybox=False, frameon=False, fontsize=12)
ax1.set_title('Annual NBP Australia')

ax2.axhline(linewidth=1, color='k', alpha = 0.5)
ax2.set_xticklabels([])
ax2.set_ylabel('Cumulative NBP [PgC]')
ax2.set_title('Cumulative NBP Australia')

ax3.set_ylabel('$\mathrm{C_{Veg}}$ [PgC]')
ax3.legend(loc='upper center', bbox_to_anchor=(1.1, -0.1), ncol=4)
ax3.set_title('Carbon stored in vegetation Australia')

ax4.set_ylabel('$\mathrm{C_{Soil}}$ [PgC]')
ax4.set_title('Carbon stored in soil Australia')

text(0.04, 1.02, 'a)', ha='center',transform=ax1.transAxes, fontsize = 14)
text(0.04, 1.02, 'b)', ha='center',transform=ax2.transAxes, fontsize = 14)
text(0.04, 1.02, 'c)', ha='center',transform=ax3.transAxes, fontsize = 14)
text(0.04, 1.02, 'd)', ha='center',transform=ax4.transAxes, fontsize = 14)

plt.show()
