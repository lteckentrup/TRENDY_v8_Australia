import numpy as np
import netCDF4 as nc
import matplotlib.pyplot as plt
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
    colours
    )

fig = plt.figure(figsize=(10,10))

fig.subplots_adjust(hspace=0.20)
fig.subplots_adjust(wspace=0.15)
fig.subplots_adjust(top=0.95)
fig.subplots_adjust(bottom=0.12)
fig.subplots_adjust(right=0.93)
fig.subplots_adjust(left=0.08)

plt.rcParams['text.usetex'] = False
plt.rcParams['font.family'] = "sans-serif"
plt.rcParams['font.sans-serif'] = "Helvetica"
plt.rcParams['axes.labelsize'] = 12
plt.rcParams['font.size'] = 12
plt.rcParams['legend.fontsize'] = 12
plt.rcParams['xtick.labelsize'] = 12
plt.rcParams['ytick.labelsize'] = 12

ax1 = fig.add_subplot(3,2,1)
ax2 = fig.add_subplot(3,2,2)
ax3 = fig.add_subplot(3,2,3)
ax4 = fig.add_subplot(3,2,4)
ax5 = fig.add_subplot(3,2,5)
ax6 = fig.add_subplot(3,2,6)

titles = ['Tropics', 'Warm temperate', 'Cool temperate', 'Mediterranean',
          'Savanna', 'Desert']
veg_masks = [tropics_mask, warm_temperate_mask, cool_temperate_mask,
             mediterranean_mask, savanna_mask, desert_mask]
axes = [ax1, ax2, ax3, ax5, ax4, ax6]

time = np.arange(1,13)
idx = [6,7,8,9,10,11,0,1,2,3,4,5]

for vegm, ax, t in zip(veg_masks, axes, titles):
    annual_gosif = mask('seasonal', 'S3', 'GPP', vegm, 'GOSIF-GPP')
    annual_gosif_sd = mask('seasonal', 'S3', 'GPP_SD', vegm, 'GOSIF-GPP_SD')

    annual_upper = np.array(annual_gosif) + np.array(annual_gosif_sd)
    annual_lower = np.array(annual_gosif) - np.array(annual_gosif_sd)

    ax.plot(time, np.array(annual_gosif)[idx], color = 'k', lw = 4.0,
            label = 'GOSIF-GPP')
    ax.fill_between(time, annual_upper[idx], annual_lower[idx], color = 'k',
                    alpha = 0.3)
    ax.set_xticks(time)
    ax.set_title(t)

    for mn, c in zip(model_names, colours):
        annual = mask('seasonal', 'S3', 'gpp', vegm, mn)
        ax.plot(time, np.array(annual)[idx], color = c, lw = 2.0, label = mn)

    if ax in (ax4, ax6):
        ax.set_ylim([0,0.37])
    elif ax in (ax3,ax5):
        ax.set_ylim([0,0.1])

xlabels = ['J', 'A', 'S', 'O', 'N', 'D', 'J', 'F', 'M', 'A','M', 'J']

for ax in (ax5, ax6):
    ax.set_xticklabels(xlabels)
for ax in (ax1, ax2, ax3, ax4):
    ax.set_xticklabels([])

ax1.set_ylabel('GPP [PgC mon-1]')
ax3.set_ylabel('GPP [PgC mon-1]')
ax5.set_ylabel('GPP [PgC mon-1]')

ax1.legend(loc='upper center', bbox_to_anchor=(1.1, -2.5), ncol=5, frameon = True)
#plt.subplot_tool()
plt.show()

# plt.savefig('seasonal_GPP_australia_trendy_SDGVM_v9.pdf')
