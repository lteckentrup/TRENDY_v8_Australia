import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import netCDF4 as nc
import os
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

nino_years = [1902,1905,1911,1914,1923,1925,1930,1940,1941,1957,1963,1965,1968,
              1969,1972,1976,1977,1982,1986,1987,1991,1994,1997,2002,2004,2006,
              2009,2015]

nina_years = [1903,1906,1909,1910,1916,1917,1922,1924,1928,1933,1938,1942,1949,
              1950,1954,1955,1956,1964,1970,1973,1974,1975,1988,1989,1993,1998,
              1999,2000,2007,2008,2010,2011,2015]

pIOD = [1902,1913,1919,1923,1926,1935,1944,1945,1946,1957,1961,1963,1972,1982,
        1983,1995,1997,2002,2006,2012,2015]
nIOD = [1906,1909,1915,1916,1917,1930,1933,1942,1958,1960,1964,1974,1975,1980,
        1981,1985,1989,1992,1996,1998,2010,2014]

pathwayIN_prec = '../../TRENDY_v7/IOD_detrend_new/prec/sh_year/'

fig = plt.figure(figsize=(9, 11.5))

fig.subplots_adjust(hspace=0.20)
fig.subplots_adjust(wspace=0.18)
fig.subplots_adjust(right= 0.99)
fig.subplots_adjust(bottom=0.15)
fig.subplots_adjust(top=0.93)

plt.rcParams['text.usetex'] = False
plt.rcParams['axes.labelsize'] = 12
plt.rcParams['font.size'] = 12
plt.rcParams['legend.fontsize'] = 12
plt.rcParams['xtick.labelsize'] = 12
plt.rcParams['ytick.labelsize'] = 12

ax1 = fig.add_subplot(4,2,1)
ax2 = fig.add_subplot(4,2,2)
ax3 = fig.add_subplot(4,2,3)
ax4 = fig.add_subplot(4,2,4)
ax5 = fig.add_subplot(4,2,5)
ax6 = fig.add_subplot(4,2,6)
ax7 = fig.add_subplot(4,2,7)
ax8 = fig.add_subplot(4,2,8)

data_prec = nc.Dataset(pathwayIN_prec+
                       'prec_1901-2018_anomaly_annual_australia.nc')

def boxplot(var, season, ylabel, vegetation, veg_mask):
    df = pd.DataFrame()
    df['CABLE-POP'] = mask('S3', var, total_mask, 'CABLE-POP')
    df['CLASS-CTEM'] = mask('S3', var, total_mask, 'CLASS-CTEM')
    df['CLM5.0'] = mask('S3', var, total_mask, 'CLM5.0')
    df['ISAM'] = mask('S3', var, total_mask, 'ISAM')
    df['ISBA-CTRIP'] = mask('S3', var, total_mask, 'ISBA-CTRIP')
    df['JSBACH'] = mask('S3', var, total_mask, 'JSBACH')
    df['JULES-ES'] = mask('S3', var, total_mask, 'JULES-ES')
    df['LPX-Bern'] = mask('S3', var, total_mask, 'LPX-Bern')
    df['OCN'] = mask('S3', var, total_mask, 'OCN')
    df['ORCHIDEE'] = mask('S3', var, total_mask, 'ORCHIDEE')
    df['ORCHIDEE-CNP'] = mask('S3', var, total_mask, 'ORCHIDEE-CNP')
    df['SDGVM'] = mask('S3', var, total_mask, 'SDGVM')
    df['VISIT'] = mask('S3', var, total_mask, 'VISIT')
    df['year'] = np.arange(1901,2018)

    df_prec = pd.DataFrame(data_prec.variables['prec'][:,0,0],
                           columns = ['prec'])
    df_prec['year'] = np.arange(1901,2018)
    df_prec_dry = df_prec.nsmallest(10, 'prec')
    dry_years = df_prec_dry['year'].tolist()

    df_prec_wet = df_prec.nlargest(10, 'prec')
    wet_years = df_prec_wet['year'].tolist()

    df_pIOD = df[df.year.isin(pIOD)]
    df_nIOD = df[df.year.isin(nIOD)]
    df_nino = df[df.year.isin(nino_years)]
    df_nina = df[df.year.isin(nina_years)]
    df_dry = df[df.year.isin(dry_years)]
    df_wet = df[df.year.isin(wet_years)]

    df_positive = df.mask(df <= 0, np.nan)
    df_negative = df.mask(df >= 0, np.nan)

    df_not_pIOD = df_negative[~df_negative.year.isin(pIOD)]
    df_neg = df_not_pIOD[~df_not_pIOD.year.isin(nino_years)]

    df_not_nIOD = df_positive[~df_positive.year.isin(nIOD)]
    df_pos = df_not_nIOD[~df_not_nIOD.year.isin(nina_years)]

    axes = [ax1, ax2, ax3, ax4, ax5, ax6, ax7, ax8]
    dataframes = [df_pIOD, df_nIOD, df_nino, df_nina, df_neg, df_pos, df_dry,
                  df_wet]
    titles = ['pIOD', 'nIOD', r'El Ni$\mathrm{\tilde{n}}$o',
              r'La Ni$\mathrm{\tilde{n}}$a', 'other negative',
              'other positive', 'Driest years', 'Wettest years']

    for a, d, t in zip(axes, dataframes, titles):
          boxplots = a.boxplot([d['CABLE-POP'].dropna(),
                                d['CLASS-CTEM'].dropna(), d['CLM5.0'].dropna(),
                                d['ISAM'].dropna(), d['ISBA-CTRIP'].dropna(),
                                d['JSBACH'].dropna(), d['JULES-ES'].dropna(),
                                d['LPX-Bern'].dropna(), d['OCN'].dropna(),
                                d['ORCHIDEE'].dropna(),
                                d['ORCHIDEE-CNP'].dropna(), d['SDGVM'].dropna(),
                                d['VISIT'].dropna()],
                               labels=model_names,
                               widths = .7, patch_artist=True,
                               medianprops = dict(linestyle='-', linewidth=2,
                                                  color='Yellow'),
                               boxprops = dict(linestyle='--', linewidth=2,
                                               color='Black',
                                               facecolor='green', alpha=.8))


          print(t)
          if t in ('pIOD', r'El Ni$\mathrm{\tilde{n}}$o', 'other positive'):
              print(d.quantile(.75) - d.quantile(.25))
              #print(d.quantile(.75))
          #print('Median')
          #print(d.median())
          #print('IQR')
          #print(d.quantile(.75)-d.quantile(.25))
          #print('Spread')
          #print((d.quantile(.75) + 1.5*(d.quantile(.75)-d.quantile(.25)))-(d.quantile(.25) - 1.5*(d.quantile(.75)-d.quantile(.25))))
          #print(d.quantile(.75) + 1.5*(d.quantile(.75)-d.quantile(.25)))
          #print(d.quantile(.25) - 1.5*(d.quantile(.75)-d.quantile(.25)))
          a.set_title(t)
          a.axhline(linewidth=1, color='k', alpha = 0.5)

          boxplot1 = boxplots['boxes'][0]
          boxplot2 = boxplots['boxes'][1]
          boxplot3 = boxplots['boxes'][2]
          boxplot4 = boxplots['boxes'][3]
          boxplot5 = boxplots['boxes'][4]
          boxplot6 = boxplots['boxes'][5]
          boxplot7 = boxplots['boxes'][6]
          boxplot8 = boxplots['boxes'][7]
          boxplot9 = boxplots['boxes'][8]
          boxplot10 = boxplots['boxes'][9]
          boxplot11 = boxplots['boxes'][10]
          boxplot12 = boxplots['boxes'][11]
          boxplot13 = boxplots['boxes'][12]

          boxplot_list = [boxplot1, boxplot2, boxplot3, boxplot4, boxplot5,
                          boxplot6, boxplot7, boxplot8, boxplot9, boxplot10,
                          boxplot11, boxplot12, boxplot13]

          for bl, c in zip(boxplot_list, colours):
              bl.set_facecolor(c)
              
          if a in (ax1, ax2, ax3, ax4, ax5, ax6):
              a.set_xticklabels([])
          else:
              a.set_xticklabels(labels=model_names,
                                rotation=90, ha='center')
          if a in (ax1, ax3, ax5, ax7):
              a.set_ylabel(ylabel)

boxplot('nbp', 'annual', 'NBP \n [PgC yr-1]', 'australia_', total_mask)

# plt.savefig('boxplot_trendy_nbp_s3_australia_SDGVM_v9.pdf')
plt.show()
