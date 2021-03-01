import matplotlib
import matplotlib.pyplot as plt
import netCDF4 as nc
import numpy as np
import pandas as pd
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

fig = plt.figure(figsize=(14,10))

fig.subplots_adjust(hspace=0.20)
fig.subplots_adjust(wspace=0.15)
fig.subplots_adjust(top=0.95)
fig.subplots_adjust(bottom=0.19)
fig.subplots_adjust(right=0.99)
fig.subplots_adjust(left=0.06)

plt.rcParams['text.usetex']=False
plt.rcParams['axes.labelsize']=12
plt.rcParams['font.size']=12
plt.rcParams['legend.fontsize']=12
plt.rcParams['xtick.labelsize']=12
plt.rcParams['ytick.labelsize']=12

ax1 = fig.add_subplot(3,3,1)
ax2 = fig.add_subplot(3,3,2)
ax3 = fig.add_subplot(3,3,3)
ax4 = fig.add_subplot(3,3,4)
ax5 = fig.add_subplot(3,3,5)
ax6 = fig.add_subplot(3,3,6)
ax8 = fig.add_subplot(3,3,8)

axes = [ax1, ax2, ax3, ax4, ax5, ax6, ax8]

for vegm, ax, t in zip(veg_masks, axes, titles):

    cable_pop_list_effect = []
    class_ctem_list_effect = []
    clm_list_effect = []
    isam_list_effect = []
    isba_ctrip_list_effect = []
    jsbach_list_effect = []
    jules_es_list_effect = []
    lpx_list_effect = []
    ocn_list_effect = []
    orchidee_list_effect = []
    orchidee_cnp_list_effect = []
    sdgvm_list_effect = []
    visit_list_effect = []

    df_NBP_S0 = pd.DataFrame()
    df_NBP_S1 = pd.DataFrame()
    df_NBP_S2 = pd.DataFrame()
    df_NBP_S3 = pd.DataFrame()

    dataframes = [df_NBP_S0, df_NBP_S1, df_NBP_S2, df_NBP_S3]
    experiments = ['S0', 'S1', 'S2', 'S3']
    effect_list = [cable_pop_list_effect, class_ctem_list_effect,
                   clm_list_effect, isam_list_effect, isba_ctrip_list_effect,
                   jsbach_list_effect, jules_es_list_effect, lpx_list_effect,
                   ocn_list_effect, orchidee_list_effect,
                   orchidee_cnp_list_effect, sdgvm_list_effect,
                   visit_list_effect]

    for exp, df in zip(experiments, dataframes):
        df['CABLE-POP'] = mask(exp, 'nbp', vegm, 'CABLE-POP')
        df['CLASS-CTEM'] = mask(exp, 'nbp', vegm, 'CLASS-CTEM')
        df['CLM5.0'] = mask(exp, 'nbp', vegm, 'CLM5.0')
        df['ISAM'] = mask(exp, 'nbp', vegm, 'ISAM')
        df['ISBA-CTRIP'] = mask(exp, 'nbp', vegm, 'ISBA-CTRIP')
        df['JSBACH'] = mask(exp, 'nbp', vegm, 'JSBACH')
        df['JULES-ES'] = mask(exp, 'nbp', vegm, 'JULES-ES')
        df['LPX-Bern'] = mask(exp, 'nbp', vegm, 'LPX-Bern')
        df['OCN'] = mask(exp, 'nbp', vegm, 'OCN')
        df['ORCHIDEE'] = mask(exp, 'nbp', vegm, 'ORCHIDEE')
        df['ORCHIDEE-CNP'] = mask(exp, 'nbp', vegm, 'ORCHIDEE-CNP')
        df['SDGVM'] = mask(exp, 'nbp', vegm, 'SDGVM')
        df['VISIT'] = mask(exp, 'nbp', vegm, 'VISIT')

    for el, mn in zip(effect_list, model_names):
        el.append(df_NBP_S1[mn].sum() - df_NBP_S0[mn].sum())
        el.append(df_NBP_S2[mn].sum() - df_NBP_S0[mn].sum())
        el.append(df_NBP_S3[mn].sum() - df_NBP_S0[mn].sum())

    labels = ['$\mathrm{CO_2}$', '$\mathrm{CO_2}$+\nCLIM ',
              '$\mathrm{CO_2}$+  \nCLIM+\nLUC   ']

    x = np.arange(len(labels))  # the label locations
    width = 0.07  # the width of the bars

    r1 = np.arange(len(cable_pop_list_effect))
    r2 = [x + width for x in r1]
    r3 = [x + width for x in r2]
    r4 = [x + width for x in r3]
    r5 = [x + width for x in r4]
    r6 = [x + width for x in r5]
    r7 = [x + width for x in r6]
    r8 = [x + width for x in r7]
    r9 = [x + width for x in r8]
    r10 = [x + width for x in r9]
    r11 = [x + width for x in r10]
    r12 = [x + width for x in r11]
    r13 = [x + width for x in r12]

    position_list = [r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11, r12, r13]

    for el, pl, mn, c in zip(effect_list, position_list, model_names, colours):
            ax.bar(pl, el, width, label=mn, color=c)
            if ax == ax1:
                print(mn)
                print(el)

    ax.set_title(t)
    ax.set_xticks([r + 6.5*width for r in range(len(cable_pop_list_effect))])
    ax.axhline(linewidth=1, color='k')
    ax.axvline(x=-0.075, color='k')
    ax.axvline(x=0.925, color='k')
    ax.axvline(x=1.925, color='k')
    ax.axvline(x=2.925, color='k')

for a in (ax1,ax2,ax3,ax5):
    a.set_xticklabels([])
for a in (ax4, ax6, ax8):
    a.set_xticklabels(labels)

for a in (ax1, ax4, ax8):
    a.set_ylabel('$\mathrm{NBP_{cum}}$ [PgC]')

ax1.legend(loc='upper center', bbox_to_anchor=(1.6, -2.7), ncol=4)
#plt.subplot_tool()
plt.show()
# plt.savefig('sensitivity_barplot.pdf')
