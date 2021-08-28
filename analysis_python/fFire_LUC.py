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

fig = plt.figure(figsize=(11.0,5.0))

fig.subplots_adjust(hspace=0.25)
fig.subplots_adjust(wspace=0.25)
fig.subplots_adjust(right=0.98)
fig.subplots_adjust(left=0.10)
fig.subplots_adjust(bottom=0.15)
fig.subplots_adjust(top=0.90)

plt.rcParams['text.usetex'] = False
plt.rcParams['axes.labelsize'] = 12
plt.rcParams['font.size'] = 11
plt.rcParams['legend.fontsize'] = 12
plt.rcParams['xtick.labelsize'] = 11
plt.rcParams['ytick.labelsize'] = 11

ax1 = fig.add_subplot(1,2,1)
ax2 = fig.add_subplot(1,2,2)

model_names = ['CLASS-CTEM', 'CLM5.0', 'ISBA-CTRIP', 'JSBACH', 'LPX-Bern',
               'SDGVM', 'VISIT']
colours = ['tab:orange', 'tab:green', 'tab:purple', 'tab:brown', 'tab:olive',
           'gold', 'purple']

for mn, c in zip(model_names, colours):
    monthly_s2 = mask('monthly', 'S2', 'fFire', total_mask, mn)
    monthly_s3 = mask('monthly', 'S3', 'fFire', total_mask, mn)
    annual_s2  = mask('annual', 'S2', 'fFire', total_mask, mn)
    annual_s3 = mask('annual', 'S3', 'fFire', total_mask, mn)

    diff_monthly = (np.array(monthly_s3) - np.array(monthly_s2))
    diff_annual = (np.array(annual_s3) - np.array(annual_s2))

    if mn in ('CABLE-POP', 'ISAM', 'JULES-ES', 'ORCHIDEE', 'VISIT'):
        ls = '--'
    elif mn in ('CLASS-CTEM', 'ISBA-CTRIP', 'LPX-Bern', 'ORCHIDEE-CNP',
                'CAMS_GFAS', 'GFED4s'):
        ls = '-'
    else:
        ls = '-.'

    ax1.plot(diff_monthly, color = c, lw = 2.0, linestyle=ls, label = mn)
    ax2.plot(diff_annual, color = c, lw = 2.0, linestyle=ls, label = mn)

xlabels = np.arange(2003,2020,step=2)

ax1.set_xticks(np.arange(0, 204, step=24))
ax1.set_xticklabels(xlabels)
ax1.set_ylabel('$\Delta$ fFire [PgC mon$^{-1}$]')
ax1.set_title('a) Monthly fire $\mathrm{CO_2}$ emissions')

xlabels = np.arange(2003,2021,step=3)
ax2.set_xticks(np.arange(0, 18, step=3))
ax2.set_ylabel('$\Delta$  fFire [PgC yr$^{-1}$]')
ax2.set_xticklabels(xlabels)
ax2.set_title('b) Annual fire $\mathrm{CO_2}$ emissions')

ax2.legend(loc='upper center', bbox_to_anchor=(-0.2, -0.07), ncol=7)
ax1.axhline(linewidth=2, color='k', alpha = 0.5)
ax2.axhline(linewidth=2, color='k', alpha = 0.5)

# plt.show()
plt.savefig('Fig16.pdf')

