import numpy as np
import netCDF4 as nc
import matplotlib.pyplot as plt
import pandas as pd
from pylab import text
import matplotlib.gridspec as gridspec
import seaborn as sns
import xarray as xr

def LCF_groups(model):
    if model == 'LPX-Bern':
        fname = '../S3/landCoverFrac/LPX-Bern_S3_landCoverFrac.nc'
    elif model == 'SDGVM':
        fname = '../../TRENDY_v9/landcover/average/SDGVM_S3.nc'
    else:
        fname = '../landcover/average/'+model+'_S3.nc'

    if model == 'CLM5.0':
        ds = xr.open_dataset(fname)
        ds = ds.sel(lon=slice(56.75,98.25))
    elif model in ('ISAM', 'ISBA-CTRIP', 'VISIT'):
        ds = xr.open_dataset(fname, decode_times=False)
    elif model == 'LPX-Bern':
        ds = xr.open_dataset(fname)
        ds = ds.sel(latitude=slice(-43.75,-10.25),
                    longitude=slice(112.25,153.75),
                    time=slice('1989-01-01', '2018-12-01')).mean(dim='time')
    else:
        ds = xr.open_dataset(fname)

    if model == 'CABLE-POP':
        ds_EVG = ds['landCoverFrac'][0,0,:,:] + ds['landCoverFrac'][0,1,:,:]
        ds_DCD = ds['landCoverFrac'][0,2,:,:] + ds['landCoverFrac'][0,3,:,:]
        ds_C3G = ds['landCoverFrac'][0,5,:,:]
        ds_C4G = ds['landCoverFrac'][0,6,:,:]

    elif model == 'CLASS-CTEM':
        ds_EVG = ds['landCoverFrac'][0,0,:,:] + ds['landCoverFrac'][0,2,:,:]
        ds_DCD = ds['landCoverFrac'][0,1,:,:] + ds['landCoverFrac'][0,3,:,:] + \
                 ds['landCoverFrac'][0,4,:,:]
        ds_C3G = ds['landCoverFrac'][0,7,:,:]
        ds_C4G = ds['landCoverFrac'][0,8,:,:]
        ds_C3Crop = ds['landCoverFrac'][0,5,:,:]
        ds_C4Crop = ds['landCoverFrac'][0,6,:,:]

    elif model == 'CLM5.0':
        ds_EVG = ds['landCoverFrac'][0,1,:,:] + ds['landCoverFrac'][0,2,:,:] + \
                 ds['landCoverFrac'][0,4,:,:] + ds['landCoverFrac'][0,5,:,:]
        ds_DCD = ds['landCoverFrac'][0,3,:,:] + ds['landCoverFrac'][0,6,:,:] + \
                 ds['landCoverFrac'][0,7,:,:] + ds['landCoverFrac'][0,8,:,:]
        ds_C3G = ds['landCoverFrac'][0,12,:,:] + ds['landCoverFrac'][0,13,:,:]
        ds_C4G = ds['landCoverFrac'][0,14,:,:]
        ds_C3Crop = ds['landCoverFrac'][0,15,:,:] + \
                    ds['landCoverFrac'][0,16,:,:] + \
                    ds['landCoverFrac'][0,19,:,:] + \
                    ds['landCoverFrac'][0,20,:,:] + \
                    ds['landCoverFrac'][0,21,:,:] + \
                    ds['landCoverFrac'][0,22,:,:] + \
                    ds['landCoverFrac'][0,23,:,:] + \
                    ds['landCoverFrac'][0,24,:,:] + \
                    ds['landCoverFrac'][0,25,:,:] + \
                    ds['landCoverFrac'][0,26,:,:] + \
                    ds['landCoverFrac'][0,31,:,:] + \
                    ds['landCoverFrac'][0,32,:,:]
        ds_C4Crop = ds['landCoverFrac'][0,17,:,:] + \
                    ds['landCoverFrac'][0,18,:,:] + \
                    ds['landCoverFrac'][0,27,:,:] + \
                    ds['landCoverFrac'][0,28,:,:] + \
                    ds['landCoverFrac'][0,29,:,:] + \
                    ds['landCoverFrac'][0,30,:,:]

    elif model == 'ISAM':
        ds_EVG = ds['landCoverFrac'][0,0,:,:] + ds['landCoverFrac'][0,2,:,:]
        ds_DCD = ds['landCoverFrac'][0,1,:,:] + ds['landCoverFrac'][0,3,:,:] + \
                 ds['landCoverFrac'][0,4,:,:] + ds['landCoverFrac'][0,19,:,:] + \
                 ds['landCoverFrac'][0,23,:,:]
        ds_C3G = ds['landCoverFrac'][0,6,:,:]
        ds_C4G = ds['landCoverFrac'][0,20,:,:]
        ds_C3Crop = ds['landCoverFrac'][0,11,:,:] + ds['landCoverFrac'][0,12,:,:]
        ds_C4Crop = ds['landCoverFrac'][0,21,:,:] + ds['landCoverFrac'][0,22,:,:]

    elif model == 'ISBA-CTRIP':
        ds_EVG = ds['landCoverFrac'][0,4,:,:] + ds['landCoverFrac'][0,5,:,:] + \
                 ds['landCoverFrac'][0,13,:,:] + ds['landCoverFrac'][0,14,:,:]
        ds_DCD = ds['landCoverFrac'][0,3,:,:] + ds['landCoverFrac'][0,12,:,:] + \
                 ds['landCoverFrac'][0,15,:,:] + ds['landCoverFrac'][0,16,:,:]
        ds_C3G = ds['landCoverFrac'][0,9,:,:]
        ds_C4G = ds['landCoverFrac'][0,10,:,:]
        ds_C3Crop = ds['landCoverFrac'][0,6,:,:] + ds['landCoverFrac'][0,8,:,:]
        ds_C4Crop = ds['landCoverFrac'][0,7,:,:]

    elif model == 'JSBACH':
        ds_EVG = ds['landCoverFrac'][0,2,:,:] + ds['landCoverFrac'][0,4,:,:]
        ds_DCD = ds['landCoverFrac'][0,3,:,:] + ds['landCoverFrac'][0,5,:,:]
        ds_C3G = ds['landCoverFrac'][0,8,:,:]
        ds_C4G = ds['landCoverFrac'][0,9,:,:]
        ds_C3Crop = ds['landCoverFrac'][0,10,:,:] + ds['landCoverFrac'][0,12,:,:]
        ds_C4Crop = ds['landCoverFrac'][0,11,:,:] + ds['landCoverFrac'][0,13,:,:]

    elif model == 'JULES-ES':
        ds_EVG = ds['landCoverFrac'][0,1,:,:] + ds['landCoverFrac'][0,2,:,:] + \
                 ds['landCoverFrac'][0,4,:,:]
        ds_DCD = ds['landCoverFrac'][0,0,:,:] + ds['landCoverFrac'][0,3,:,:]
        ds_C3G = ds['landCoverFrac'][0,5,:,:]
        ds_C4G = ds['landCoverFrac'][0,8,:,:]
        ds_C3Crop = ds['landCoverFrac'][0,6,:,:] + ds['landCoverFrac'][0,7,:,:]
        ds_C4Crop = ds['landCoverFrac'][0,9,:,:] + ds['landCoverFrac'][0,10,:,:]

    elif model == 'LPX-Bern':
        ds_EVG = ds['landCoverFrac'][0,:,:] + ds['landCoverFrac'][2,:,:] + \
                 ds['landCoverFrac'][3,:,:] + ds['landCoverFrac'][5,:,:] + \
                 ds['landCoverFrac'][12,:,:]
        ds_DCD = ds['landCoverFrac'][1,:,:] + ds['landCoverFrac'][4,:,:] + \
                 ds['landCoverFrac'][6,:,:] + ds['landCoverFrac'][7,:,:] + \
                 ds['landCoverFrac'][13,:,:]
        ds_C3G = ds['landCoverFrac'][8,:,:] + ds['landCoverFrac'][10,:,:] + \
                 ds['landCoverFrac'][11,:,:] + ds['landCoverFrac'][8,:,:]
        ds_C4G = ds['landCoverFrac'][9,:,:]
        ds_C3Crop = ds['landCoverFrac'][15,:,:] + ds['landCoverFrac'][17,:,:]
        ds_C4Crop = ds['landCoverFrac'][16,:,:] + ds['landCoverFrac'][18,:,:]

    elif model == 'OCN':
        ds_EVG = ds['landCoverFrac'][0,1,:,:] + ds['landCoverFrac'][0,3,:,:] + \
                 ds['landCoverFrac'][0,4,:,:] + ds['landCoverFrac'][0,6,:,:]
        ds_DCD = ds['landCoverFrac'][0,2,:,:] + ds['landCoverFrac'][0,5,:,:] + \
                 ds['landCoverFrac'][0,7,:,:] + ds['landCoverFrac'][0,8,:,:]
        ds_C3G = ds['landCoverFrac'][0,9,:,:]
        ds_C4G = ds['landCoverFrac'][0,10,:,:]
        ds_C3Crop = ds['landCoverFrac'][0,11,:,:]
        ds_C4Crop = ds['landCoverFrac'][0,12,:,:]

    elif model == 'ORCHIDEE-CNP':
        ds_EVG = ds['landCoverFrac'][0,1,:,:] + ds['landCoverFrac'][0,3,:,:] + \
                 ds['landCoverFrac'][0,4,:,:] + ds['landCoverFrac'][0,6,:,:]
        ds_DCD = ds['landCoverFrac'][0,2,:,:] + ds['landCoverFrac'][0,5,:,:] + \
                 ds['landCoverFrac'][0,7,:,:] + ds['landCoverFrac'][0,8,:,:]
        ds_C3G = ds['landCoverFrac'][0,9,:,:]
        ds_C4G = ds['landCoverFrac'][0,11,:,:]
        ds_C3Crop = ds['landCoverFrac'][0,10,:,:] + ds['landCoverFrac'][0,13,:,:]
        ds_C4Crop = ds['landCoverFrac'][0,12,:,:] + ds['landCoverFrac'][0,14,:,:]

    elif model == 'ORCHIDEE':
        ds_EVG = ds['landCoverFrac'][0,1,:,:] + ds['landCoverFrac'][0,3,:,:] + \
                 ds['landCoverFrac'][0,4,:,:] + ds['landCoverFrac'][0,6,:,:]
        ds_DCD = ds['landCoverFrac'][0,2,:,:] + ds['landCoverFrac'][0,5,:,:] + \
                 ds['landCoverFrac'][0,7,:,:] + ds['landCoverFrac'][0,8,:,:]
        ds_C3G = ds['landCoverFrac'][0,9,:,:] + ds['landCoverFrac'][0,13,:,:] + \
                 ds['landCoverFrac'][0,14,:,:]
        ds_C4G = ds['landCoverFrac'][0,10,:,:]
        ds_C3Crop = ds['landCoverFrac'][0,11,:,:]
        ds_C4Crop = ds['landCoverFrac'][0,12,:,:]

    elif model == 'SDGVM':
        ds_EVG = ds['landCoverFrac'][0,8,:,:] + ds['landCoverFrac'][0,9,:,:]
        ds_DCD = ds['landCoverFrac'][0,6,:,:] + ds['landCoverFrac'][0,7,:,:]
        ds_C3G = ds['landCoverFrac'][0,2,:,:]
        ds_C4G = ds['landCoverFrac'][0,4,:,:]
        ds_C3Crop = ds['landCoverFrac'][0,3,:,:]
        ds_C4Crop = ds['landCoverFrac'][0,5,:,:]

    elif model == 'VISIT':
        ds_EVG = ds['landCoverFrac'][0,0,:,:] + ds['landCoverFrac'][0,2,:,:] + \
                 ds['landCoverFrac'][0,3,:,:] + ds['landCoverFrac'][0,5,:,:]
        ds_DCD = ds['landCoverFrac'][0,1,:,:] + ds['landCoverFrac'][0,4,:,:] + \
                 ds['landCoverFrac'][0,6,:,:]
        ds_C3G = ds['landCoverFrac'][0,9,:,:]
        ds_C4G = ds['landCoverFrac'][0,9,:,:]*0
        ds_C3Crop = ds['landCoverFrac'][0,15,:,:]
        ds_C4Crop = ds['landCoverFrac'][0,8,:,:]*0

    if model == 'CABLE-POP':
        return(ds_EVG, ds_DCD, ds_C3G, ds_C4G)
    else:
        return(ds_EVG, ds_DCD, ds_C3G, ds_C4G, ds_C3Crop, ds_C4Crop)

def lcf_corr(model, var):
    fname = ('../'+var+'/sh_year/'+model+'_S3_'+var+'_australia_annual.nc')
    fname_ensmean = ('../'+var+'/sh_year/ensmean_australia_annual.nc')

    if model in ('ISAM', 'ISBA-CTRIP', 'VISIT'):
        ds = xr.open_dataset(fname, decode_times=False)
        if var == 'cVeg':
            ds['time']=pd.date_range(start='1/1/1901', freq='Y',
                                     periods=ds.time.size)
        elif var == 'cSoil':
            if model == 'ISAM':
                ds['time']=pd.date_range(start='1/1/1901', freq='Y',
                                         periods=ds.time.size)
            else:
                ds['time']=pd.date_range(start='1/1/1901', freq='M',
                                         periods=ds.time.size)
    else:
        ds = xr.open_dataset(fname)

    if model in ('ISAM', 'LPX-Bern'):
        ds = ds.rename({'latitude':'lat', 'longitude':'lon'})

    ds_mean = ds.sel(time=slice('1989-01-01', '2018-12-01')).mean(dim='time')

    ds_ensmean = xr.open_dataset(fname_ensmean)
    ds_ensmean_mean = ds_ensmean.sel(time=slice('1989-01-01',
                                                '2018-12-01')).mean(dim='time')

    ds_diff = ds_mean - ds_ensmean_mean

    return(ds_diff)
