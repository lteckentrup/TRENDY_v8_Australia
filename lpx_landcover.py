import xarray as xr
import numpy as np
from netCDF4 import Dataset as open_ncfile
import pandas as pd

def ugh(exp):

    file = open_ncfile('../../'+exp+'/landCoverFrac/LPX-Bern_'+exp+'_landCoverFrac_original.nc')

    lat = file.variables['latitude'][92:160]
    lon = file.variables['longitude'][584:668]

    time = pd.date_range(start='1/1/2001', end='1/01/2019', freq='M')

    veg1 = file.variables['landCoverFrac'][584:668,92:160,3612:,0]
    veg2 = file.variables['landCoverFrac'][584:668,92:160,3612:,1]
    veg3 = file.variables['landCoverFrac'][584:668,92:160,3612:,2]
    veg4 = file.variables['landCoverFrac'][584:668,92:160,3612:,3]
    veg5 = file.variables['landCoverFrac'][584:668,92:160,3612:,4]
    veg6 = file.variables['landCoverFrac'][584:668,92:160,3612:,5]
    veg7 = file.variables['landCoverFrac'][584:668,92:160,3612:,6]
    veg8 = file.variables['landCoverFrac'][584:668,92:160,3612:,7]
    veg9 = file.variables['landCoverFrac'][584:668,92:160,3612:,8]
    veg10 = file.variables['landCoverFrac'][584:668,92:160,3612:,9]
    veg11 = file.variables['landCoverFrac'][584:668,92:160,3612:,10]
    veg12 = file.variables['landCoverFrac'][584:668,92:160,3612:,11]
    veg13 = file.variables['landCoverFrac'][584:668,92:160,3612:,12]
    veg14 = file.variables['landCoverFrac'][584:668,92:160,3612:,13]
    veg15 = file.variables['landCoverFrac'][584:668,92:160,3612:,14]
    veg16 = file.variables['landCoverFrac'][584:668,92:160,3612:,15]
    veg17 = file.variables['landCoverFrac'][584:668,92:160,3612:,16]
    veg18 = file.variables['landCoverFrac'][584:668,92:160,3612:,17]
    veg19 = file.variables['landCoverFrac'][584:668,92:160,3612:,18]
    veg20 = file.variables['landCoverFrac'][584:668,92:160,3612:,19]

    pft_short = ['TrBR', 'TeNE', 'TeBE', 'TeBS', 'BNE', 'BNS', 'BBS', 'C3G',
                 'C4G', 'PeatGr', 'PeatSM', 'PeatTrBE', 'PeatTrBR', 'PeatHerb',
                 'C3Crop', 'C4Crop', 'C3Past', 'C4Past', 'UrbanBare']

    pfts = ['Tropical broad raingreen', 'Temperate needle evergreen',
            'Temperate broad evergeen', 'Temperate broad summergreen',
            'Boreal needle evergreen', 'Boreal needle summergreen',
            'Boreal broad summergreen', 'C3 herbaceous', 'C4 herbaceous',
            'Peat graminoid', 'Peat sphagnum moss',
            'Peat flood tolerant tropical broad evergreen',
            'Peat flood tolerant tropical broad raingreen',
            'Peat flood tolerant herbaceous', 'Cropland C3 herbaceous',
            'Cropland C4 herbaceous', 'Pasture C3 herbaceous',
            'Pasture C4 herbaceous', 'Urban Bare']

    vegs = [veg2, veg3, veg4, veg5, veg6, veg7, veg8, veg9, veg10, veg11, veg12,
            veg13, veg14, veg15, veg16, veg17, veg18, veg19, veg20]

    # create dataset
    ds = xr.Dataset({
        'TrBE': xr.DataArray(data   = np.transpose(veg1),
                             dims   = ['time', 'latitude', 'longitude'],
                             coords = [time, lat, lon],
                             attrs  = {'long_name': 'Tropical broad evergreen',
                                       'units'     : '%'})},
                    attrs = {'Conventions':'CF-1.6',
                             'Institution':'Climate and Environmental Physics, '
                                           'University of Bern',
                             'Source': 'Extracted from LPX-Bern_S3_01 at '
                                       '2019-08-13T17:58:26.478921',
                             'Title':'Fractional Land Cover of PFT output from '
                                     'LPX-Bern for GCP201',
                             'Contact': 'lienert@climate.unibe.ch'}
                    )
    for v, ps, p in zip(vegs, pft_short, pfts):
        ds[ps] = xr.DataArray(data = np.transpose(v),
                             dims   = ['time', 'latitude', 'longitude'],
                             coords = [time, lat, lon],
                             attrs  = {'long_name': p,
                                       'units'     : '%'})

    ds['latitude'].attrs={'units':'degrees_north', 'long_name':'latitude',
                     'standard_name':'latitude', 'axis':'Y'}
    ds['longitude'].attrs={'units':'degrees_east', 'long_name':'longitude',
                     'standard_name':'longitude', 'axis':'X'}

    ds.to_netcdf('LPX-Bern_'+exp+'_landCoverFrac.nc',
                 encoding={'latitude':{'dtype': 'double'},
                           'longitude':{'dtype': 'double'},
                           'time':{'dtype': 'double'},
                           'TrBE':{'dtype': 'float32'},
                           'TrBR':{'dtype': 'float32'},
                           'TeNE':{'dtype': 'float32'},
                           'TeBE':{'dtype': 'float32'},
                           'TeBS':{'dtype': 'float32'},
                           'BNE':{'dtype': 'float32'},
                           'BNS':{'dtype': 'float32'},
                           'BBS':{'dtype': 'float32'},
                           'C3G':{'dtype': 'float32'},
                           'C4G':{'dtype': 'float32'},
                           'PeatGr':{'dtype': 'float32'},
                           'PeatSM':{'dtype': 'float32'},
                           'PeatTrBE':{'dtype': 'float32'},
                           'PeatTrBR':{'dtype': 'float32'},
                           'PeatHerb':{'dtype': 'float32'},
                           'C3Crop':{'dtype': 'float32'},
                           'C4Crop':{'dtype': 'float32'},
                           'C3Past':{'dtype': 'float32'},
                           'C4Past':{'dtype': 'float32'},
                           'UrbanBare':{'dtype': 'float32'}})

ugh('S2')
ugh('S3')
