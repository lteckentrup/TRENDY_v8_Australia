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

pathwayIN_trendy = '/srv/ccrc/data02/z5227845/research/TRENDY_v8/impact_analysis/'
pathwayIN_trendy_SDGVM = '/srv/ccrc/data02/z5227845/research/TRENDY_v9/impact_analysis/'

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

time = np.arange(1901,2018)

def tau(modelname):

    NPP = mask('annual', 'S3', 'npp', total_mask, mn)
    CVeg = mask('annual', 'S3', 'cVeg', total_mask, mn)

    time = np.arange(1901,2018)

    tau = []

    for i in range(0,116):
        tau_prel = CVeg [i+1]/ (NPP[i+1] - ((CVeg [i+1] - CVeg [i])/ (time[i+1] -
                   time[i])))
        tau.append(tau_prel)

    tau_change = tau-(sum(tau[:30])/len(tau[:30]))
    return(tau, tau_change)

for mn, c in zip(model_names, colours):
    NPP = mask('annual', 'S3', 'npp', total_mask, mn)
    NPP_change = NPP-(sum(NPP[:30])/len(NPP[:30]))

    if mn in ('CABLE-POP', 'ISAM', 'JULES-ES', 'ORCHIDEE', 'VISIT'):
        ls = '--'
    elif mn in ('CLASS-CTEM', 'ISBA-CTRIP', 'LPX-Bern', 'ORCHIDEE-CNP'):
        ls = '-'
    else:
        ls = '-.'

    ax1.plot(time, NPP_change, color=c, lw=2.0, linestyle=ls, label=mn)

    TAU, TAU_change = tau(mn)
    df_TAU = pd.DataFrame(TAU, columns = [mn])
    ax2.plot(time[1:], df_TAU[mn].rolling(window=5, center=True).mean(),
             color=c, linewidth=2.5, linestyle=ls, label=mn)
    ax2.plot(time[1:], df_TAU [mn], color=c, linestyle=ls, alpha=0.2)

    df_TAU_change = pd.DataFrame(TAU_change, columns=[mn])
    ax3.plot(time[1:], df_TAU_change[mn].rolling(window=5, center=True).mean(),
             color=c, linewidth=2.5, linestyle=ls, label=mn, alpha=1)
    ax3.plot(time[1:], df_TAU_change[mn], color=c, linestyle=ls, alpha=0.2)

    CVeg = mask('annual', 'S3', 'cVeg', total_mask, mn)
    CVeg_change = CVeg-(sum(CVeg[:30])/len(CVeg[:30]))
    ax4.plot(time, CVeg_change, color=c, lw=2.0, linestyle=ls, label=mn)

ax1.axhline(linewidth=1, color='k', alpha=0.5)
ax1.set_xticklabels([])
ax1.set_ylabel('$\mathrm{\Delta}$ NPP [PgC yr$^{-1}$]')
ax1.set_title('$\mathrm{\Delta}$ NPP')

ax2.set_xticklabels([])
ax2.set_ylabel('$\mathrm{\\tau}$ [yr]')
ax2.set_title('Carbon residence time $\mathrm{\\tau}$')

ax3.axhline(linewidth=2, color='k', alpha=0.5)
ax3.set_ylabel('$\mathrm{\Delta \\tau}$ [yr]')
ax3.set_title('$\mathrm{\Delta}$ Carbon residence time $\mathrm{\\tau}$             ')
ax3.legend(loc='upper center', bbox_to_anchor=(1.1, -0.1), ncol=4)

ax4.axhline(linewidth=1, color='k', alpha=0.5)
ax4.set_ylabel('$\mathrm{\Delta C_{Veg}}$ [PgC]')
ax4.set_title('$\mathrm{\Delta}$ Carbon stored in vegetation')

text(0.04, 1.02, 'a)', ha='center',transform=ax1.transAxes, fontsize = 14)
text(0.04, 1.02, 'b)', ha='center',transform=ax2.transAxes, fontsize = 14)
text(0.04, 1.02, 'c)', ha='center',transform=ax3.transAxes, fontsize = 14)
text(0.04, 1.02, 'd)', ha='center',transform=ax4.transAxes, fontsize = 14)

#plt.subplot_tool()
# plt.show()
plt.savefig('Fig5.pdf')
