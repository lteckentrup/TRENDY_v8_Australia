import xarray as xr
import numpy as np
from netCDF4 import Dataset as open_ncfile

def ugh(period, step):

    file = open_ncfile('MODIS_GPP_'+period+'.nc')

    lat = file.variables['lat'][:]
    lon = file.variables['lon'][:]
    veg = file.variables['Gpp_500m'][step,:,:]

    # create dataset
    ds = xr.Dataset({
        'GPP': xr.DataArray(data   = veg,
                            dims   = ['lat', 'lon'],
                            coords = [lat, lon],
                            attrs  = {'long_name': 'GPP',
                                      'units'     : 'kgC m-2'})},
                    attrs = {'Conventions':'CF-1.6',
                             'Institution':'Land Processes Distributed Active '
                             'Archive Center (LP DAAC)',
                             'Source': 'AppEEARS v2.53',
                             'Title':'MOD44B.006 for aid0001'}
                    )

    ds['lat'].attrs={'units':'degrees_north', 'long_name':'latitude',
                     'standard_name':'latitude', 'axis':'Y'}
    ds['lon'].attrs={'units':'degrees_east', 'long_name':'longitude',
                     'standard_name':'longitude', 'axis':'X'}

    ds.to_netcdf('GPP_'+str(step)+'.nc',
                 encoding={'lat':{'dtype': 'double'},'lon':{'dtype': 'double'},
                           'GPP':{'dtype': 'float32'}})


ugh('2001-2002', step)
