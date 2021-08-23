import numpy as np
import netCDF4 as nc
import matplotlib.pyplot as plt
import pandas as pd
from pylab import text
import matplotlib.gridspec as gridspec
import seaborn as sns
import xarray as xr
from LCF_groups_corr import (
    LCF_groups,
    lcf_corr
    )
from mask import (
    model_names,
    colours
    )

fig = plt.figure(figsize=(8,11.0))

fig.subplots_adjust(hspace=0.2)
fig.subplots_adjust(wspace=0.18)
fig.subplots_adjust(right=0.98)
fig.subplots_adjust(left=0.1)
fig.subplots_adjust(bottom=0.05)
fig.subplots_adjust(top=0.87)

plt.rcParams['text.usetex'] = False
plt.rcParams['axes.labelsize'] = 12
plt.rcParams['font.size'] = 11
plt.rcParams['legend.fontsize'] = 12
plt.rcParams['xtick.labelsize'] = 11
plt.rcParams['ytick.labelsize'] = 11

ax1 = fig.add_subplot(3,2,1)
ax2 = fig.add_subplot(3,2,2)
ax3 = fig.add_subplot(3,2,3)
ax4 = fig.add_subplot(3,2,4)
ax5 = fig.add_subplot(3,2,5)
ax6 = fig.add_subplot(3,2,6)

def plot(carbon_var):
    for c,mn in zip(colours,model_names):
        if mn == 'CABLE-POP':
            ds_EVG, ds_DCD, ds_C3G, ds_C4G = LCF_groups(mn)
            ds_lcf = [ds_EVG, ds_DCD, ds_C3G, ds_C4G]
            axes = [ax1,ax2,ax3,ax4]
        else:
            ds_EVG, ds_DCD, ds_C3G, ds_C4G, ds_C3Crop, ds_C4Crop = LCF_groups(mn)
            ds_lcf = [ds_EVG, ds_DCD, ds_C3G, ds_C4G, ds_C3Crop, ds_C4Crop]
            axes = [ax1,ax2,ax3,ax4,ax5,ax6]

        ds_cveg = lcf_corr(mn, carbon_var)

        for a,ds in zip(axes, ds_lcf):
            if mn in ('ISBA-CTRIP', 'JULES-ES', 'VISIT'):
                sns.regplot(ds.where(ds>5).values.flatten(),
                            ds_cveg[carbon_var].values.flatten(),
                            scatter=True, color=c, ax=a, label=mn,
                            scatter_kws={'s':1})
            else:
                sns.regplot(ds.where(ds>0.05).values.flatten()*100, \
                            ds_cveg[carbon_var].values.flatten(),
                            scatter=True, color=c, ax=a, label=mn,
                            scatter_kws={'s':1})

        if carbon_var == 'cVeg':
            title = 'C$_\mathrm{{Veg}}$ - C$_\mathrm{{Veg,ensmean}}$ [kgC m$^{-2}$]'
        elif carbon_var == 'cSoil':
            title = 'C$_\mathrm{{Soil}}$ - C$_\mathrm{{Soil,ensmean}}$ [kgC m$^{-2}$]'
        elif carbon_var == 'NBP':
            title = 'NBP - NBP$_\mathrm{{ensmean}}$ [kgC m$^{-2}$]'

        for a in (ax1,ax3,ax5):
            a.set_ylabel(title)

plot('cVeg')

ax5.set_xlabel('Landcover Fraction')
ax6.set_xlabel('Landcover Fraction')

ax1.set_title('Evergreen trees')
ax2.set_title('Deciduous trees')
ax3.set_title('C3G')
ax4.set_title('C4G')
ax5.set_title('C3 Crop')
ax6.set_title('C4 Crop')

ax1.axhline(linewidth=1, color='k', alpha=0.5)
ax2.axhline(linewidth=1, color='k', alpha=0.5)
ax3.axhline(linewidth=1, color='k', alpha=0.5)
ax4.axhline(linewidth=1, color='k', alpha=0.5)
ax5.axhline(linewidth=1, color='k', alpha=0.5)
ax6.axhline(linewidth=1, color='k', alpha=0.5)

ax3.legend(loc='upper center', bbox_to_anchor=(1.0, 2.75), ncol=4)
# plt.subplot_tool()
plt.show()
# plt.savefig('CVeg_LCF.png', dpi=400)
