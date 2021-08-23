import numpy as np
import netCDF4 as nc
import matplotlib.pyplot as plt
import pandas as pd
from pylab import text
import matplotlib.gridspec as gridspec
import seaborn as sns
import xarray as xr

def LCF_groups(model):
    fname_cable_pop = ('../landcover/average/CABLE-POP_S3.nc')
    fname_class_ctem = ('../landcover/average/CLASS-CTEM_S3.nc')
    fname_clm = ('../landcover/average/CLM5.0_S3.nc')
    fname_isam = ('../landcover/average/ISAM_S3.nc')
    fname_isba_ctrip = ('../landcover/average/ISBA-CTRIP_S3.nc')
    fname_jsbach = ('../landcover/average/JSBACH_S3.nc')
    fname_jules = ('../landcover/average/JULES-ES_S3.nc')
    fname_lpx = ('../S3/landCoverFrac/LPX-Bern_S3_landCoverFrac.nc')
    fname_ocn = ('../landcover/average/OCN_S3.nc')
    fname_orchidee_cnp = ('../landcover/average/ORCHIDEE-CNP_S3.nc')
    fname_orchidee = ('../landcover/average/ORCHIDEE_S3.nc')
    fname_sdgvm = ('../../TRENDY_v9/landcover/average/SDGVM_S3.nc')
    fname_visit = ('../landcover/average/VISIT_S3.nc')

    ds_cable = xr.open_dataset(fname_cable_pop)
    ds_class_ctem = xr.open_dataset(fname_class_ctem)
    ds_clm = xr.open_dataset(fname_clm)
    ds_clm = ds_clm.sel(lon=slice(56.75,98.25))
    ds_isam = xr.open_dataset(fname_isam, decode_times=False)
    ds_isba_ctrip = xr.open_dataset(fname_isba_ctrip, decode_times=False)
    ds_jsbach = xr.open_dataset(fname_jsbach)
    ds_jules = xr.open_dataset(fname_jules)
    ds_lpx = xr.open_dataset(fname_lpx)
    ds_lpx = ds_lpx.sel(latitude=slice(-43.75,-10.25),
                        longitude=slice(112.25,153.75),
                        time=slice('1989-01-01', '2018-12-01')).mean(dim='time')
    ds_ocn = xr.open_dataset(fname_ocn)
    ds_orchidee_cnp = xr.open_dataset(fname_orchidee_cnp)
    ds_orchidee = xr.open_dataset(fname_orchidee)
    ds_sdgvm = xr.open_dataset(fname_sdgvm)
    ds_visit = xr.open_dataset(fname_visit, decode_times=False)

    ds_visit = xr.open_dataset(fname_visit, decode_times=False)

    ds_cable_EVG = ds_cable['landCoverFrac'][0,0,:,:] + \
                   ds_cable['landCoverFrac'][0,1,:,:]
    ds_cable_DCD = ds_cable['landCoverFrac'][0,2,:,:] + \
                   ds_cable['landCoverFrac'][0,3,:,:]
    ds_cable_C3G = ds_cable['landCoverFrac'][0,5,:,:]
    ds_cable_C4G = ds_cable['landCoverFrac'][0,6,:,:]
    ds_cable_C3Crop = ds_cable['landCoverFrac'][0,5,:,:]*0
    ds_cable_C4Crop = ds_cable['landCoverFrac'][0,6,:,:]*0

    ds_class_ctem_EVG = ds_class_ctem['landCoverFrac'][0,0,:,:] + \
                        ds_class_ctem['landCoverFrac'][0,2,:,:]
    ds_class_ctem_DCD = ds_class_ctem['landCoverFrac'][0,1,:,:] + \
                        ds_class_ctem['landCoverFrac'][0,3,:,:] + \
                        ds_class_ctem['landCoverFrac'][0,4,:,:]
    ds_class_ctem_C3G = ds_class_ctem['landCoverFrac'][0,7,:,:]
    ds_class_ctem_C4G = ds_class_ctem['landCoverFrac'][0,8,:,:]
    ds_class_ctem_C3Crop = ds_class_ctem['landCoverFrac'][0,5,:,:]
    ds_class_ctem_C4Crop = ds_class_ctem['landCoverFrac'][0,6,:,:]

    ds_clm_EVG = ds_clm['landCoverFrac'][0,1,:,:] + \
                 ds_clm['landCoverFrac'][0,2,:,:] + \
                 ds_clm['landCoverFrac'][0,4,:,:] + \
                 ds_clm['landCoverFrac'][0,5,:,:]
    ds_clm_DCD = ds_clm['landCoverFrac'][0,3,:,:] + \
                 ds_clm['landCoverFrac'][0,6,:,:] + \
                 ds_clm['landCoverFrac'][0,7,:,:] + \
                 ds_clm['landCoverFrac'][0,8,:,:]
    ds_clm_C3G = ds_clm['landCoverFrac'][0,12,:,:] + \
                 ds_clm['landCoverFrac'][0,13,:,:]
    ds_clm_C4G = ds_clm['landCoverFrac'][0,14,:,:]
    ds_clm_C3Crop = ds_clm['landCoverFrac'][0,15,:,:] + \
                    ds_clm['landCoverFrac'][0,16,:,:] + \
                    ds_clm['landCoverFrac'][0,19,:,:] + \
                    ds_clm['landCoverFrac'][0,20,:,:] + \
                    ds_clm['landCoverFrac'][0,21,:,:] + \
                    ds_clm['landCoverFrac'][0,22,:,:] + \
                    ds_clm['landCoverFrac'][0,23,:,:] + \
                    ds_clm['landCoverFrac'][0,24,:,:] + \
                    ds_clm['landCoverFrac'][0,25,:,:] + \
                    ds_clm['landCoverFrac'][0,26,:,:] + \
                    ds_clm['landCoverFrac'][0,31,:,:] + \
                    ds_clm['landCoverFrac'][0,32,:,:]
    ds_clm_C4Crop = ds_clm['landCoverFrac'][0,17,:,:] + \
                    ds_clm['landCoverFrac'][0,18,:,:] + \
                    ds_clm['landCoverFrac'][0,27,:,:] + \
                    ds_clm['landCoverFrac'][0,28,:,:] + \
                    ds_clm['landCoverFrac'][0,29,:,:] + \
                    ds_clm['landCoverFrac'][0,30,:,:]

    ds_isam_EVG = ds_isam['landCoverFrac'][0,0,:,:] + \
                  ds_isam['landCoverFrac'][0,2,:,:]
    ds_isam_DCD = ds_isam['landCoverFrac'][0,1,:,:] + \
                  ds_isam['landCoverFrac'][0,3,:,:] + \
                  ds_isam['landCoverFrac'][0,4,:,:] + \
                  ds_isam['landCoverFrac'][0,19,:,:] + \
                  ds_isam['landCoverFrac'][0,23,:,:]
    ds_isam_C3G = ds_isam['landCoverFrac'][0,6,:,:]
    ds_isam_C4G = ds_isam['landCoverFrac'][0,20,:,:]
    ds_isam_C3Crop = ds_isam['landCoverFrac'][0,11,:,:] + \
                     ds_isam['landCoverFrac'][0,12,:,:]
    ds_isam_C4Crop = ds_isam['landCoverFrac'][0,21,:,:] + \
                     ds_isam['landCoverFrac'][0,22,:,:]

    ds_isba_ctrip_EVG = ds_isba_ctrip['landCoverFrac'][0,4,:,:] + \
                        ds_isba_ctrip['landCoverFrac'][0,5,:,:] + \
                        ds_isba_ctrip['landCoverFrac'][0,13,:,:] + \
                        ds_isba_ctrip['landCoverFrac'][0,14,:,:]
    ds_isba_ctrip_DCD = ds_isba_ctrip['landCoverFrac'][0,3,:,:] + \
                        ds_isba_ctrip['landCoverFrac'][0,12,:,:] + \
                        ds_isba_ctrip['landCoverFrac'][0,15,:,:] + \
                        ds_isba_ctrip['landCoverFrac'][0,16,:,:]
    ds_isba_ctrip_C3G = ds_isba_ctrip['landCoverFrac'][0,9,:,:]
    ds_isba_ctrip_C4G = ds_isba_ctrip['landCoverFrac'][0,10,:,:]
    ds_isba_ctrip_C3Crop = ds_isba_ctrip['landCoverFrac'][0,6,:,:] + \
                           ds_isba_ctrip['landCoverFrac'][0,8,:,:]
    ds_isba_ctrip_C4Crop = ds_isba_ctrip['landCoverFrac'][0,7,:,:]

    ds_jsbach_EVG = ds_jsbach['landCoverFrac'][0,2,:,:] + \
                    ds_jsbach['landCoverFrac'][0,4,:,:]
    ds_jsbach_DCD = ds_jsbach['landCoverFrac'][0,3,:,:] + \
                    ds_jsbach['landCoverFrac'][0,5,:,:]
    ds_jsbach_C3G = ds_jsbach['landCoverFrac'][0,8,:,:]
    ds_jsbach_C4G = ds_jsbach['landCoverFrac'][0,9,:,:]
    ds_jsbach_C3Crop = ds_jsbach['landCoverFrac'][0,10,:,:] + \
                       ds_jsbach['landCoverFrac'][0,12,:,:]
    ds_jsbach_C4Crop = ds_jsbach['landCoverFrac'][0,11,:,:] + \
                       ds_jsbach['landCoverFrac'][0,13,:,:]

    ds_jules_EVG = ds_jules['landCoverFrac'][0,1,:,:] + \
                   ds_jules['landCoverFrac'][0,2,:,:] + \
                   ds_jules['landCoverFrac'][0,4,:,:]
    ds_jules_DCD = ds_jules['landCoverFrac'][0,0,:,:] + \
                   ds_jules['landCoverFrac'][0,3,:,:]
    ds_jules_C3G = ds_jules['landCoverFrac'][0,5,:,:]
    ds_jules_C4G = ds_jules['landCoverFrac'][0,8,:,:]
    ds_jules_C3Crop = ds_jules['landCoverFrac'][0,6,:,:] + \
                      ds_jules['landCoverFrac'][0,7,:,:]
    ds_jules_C4Crop = ds_jules['landCoverFrac'][0,9,:,:] + \
                      ds_jules['landCoverFrac'][0,10,:,:]

    ds_lpx_EVG = ds_lpx['landCoverFrac'][0,:,:] + ds_lpx['landCoverFrac'][2,:,:] + \
                 ds_lpx['landCoverFrac'][3,:,:] + ds_lpx['landCoverFrac'][5,:,:] + \
                 ds_lpx['landCoverFrac'][12,:,:]
    ds_lpx_DCD = ds_lpx['landCoverFrac'][1,:,:] + ds_lpx['landCoverFrac'][4,:,:] + \
                 ds_lpx['landCoverFrac'][6,:,:] + ds_lpx['landCoverFrac'][7,:,:] + \
                 ds_lpx['landCoverFrac'][13,:,:]
    ds_lpx_C3G = ds_lpx['landCoverFrac'][8,:,:] + ds_lpx['landCoverFrac'][10,:,:] + \
                 ds_lpx['landCoverFrac'][11,:,:] + ds_lpx['landCoverFrac'][8,:,:]
    ds_lpx_C4G = ds_lpx['landCoverFrac'][9,:,:]
    ds_lpx_C3Crop = ds_lpx['landCoverFrac'][15,:,:] + ds_lpx['landCoverFrac'][17,:,:]
    ds_lpx_C4Crop = ds_lpx['landCoverFrac'][16,:,:] + ds_lpx['landCoverFrac'][18,:,:]

    ds_ocn_EVG = ds_ocn['landCoverFrac'][0,1,:,:] + ds_ocn['landCoverFrac'][0,3,:,:] + \
                 ds_ocn['landCoverFrac'][0,4,:,:] + ds_ocn['landCoverFrac'][0,6,:,:]
    ds_ocn_DCD = ds_ocn['landCoverFrac'][0,2,:,:] + ds_ocn['landCoverFrac'][0,5,:,:] + \
                 ds_ocn['landCoverFrac'][0,7,:,:] + ds_ocn['landCoverFrac'][0,8,:,:]
    ds_ocn_C3G = ds_ocn['landCoverFrac'][0,9,:,:]
    ds_ocn_C4G = ds_ocn['landCoverFrac'][0,10,:,:]
    ds_ocn_C3Crop = ds_ocn['landCoverFrac'][0,11,:,:]
    ds_ocn_C4Crop = ds_ocn['landCoverFrac'][0,12,:,:]

    ds_orchidee_cnp_EVG = ds_orchidee_cnp['landCoverFrac'][0,1,:,:] + \
                          ds_orchidee_cnp['landCoverFrac'][0,3,:,:] + \
                          ds_orchidee_cnp['landCoverFrac'][0,4,:,:] + \
                          ds_orchidee_cnp['landCoverFrac'][0,6,:,:]
    ds_orchidee_cnp_DCD = ds_orchidee_cnp['landCoverFrac'][0,2,:,:] + \
                          ds_orchidee_cnp['landCoverFrac'][0,5,:,:] + \
                          ds_orchidee_cnp['landCoverFrac'][0,7,:,:] + \
                          ds_orchidee_cnp['landCoverFrac'][0,8,:,:]
    ds_orchidee_cnp_C3G = ds_orchidee_cnp['landCoverFrac'][0,9,:,:]
    ds_orchidee_cnp_C4G = ds_orchidee_cnp['landCoverFrac'][0,11,:,:]
    ds_orchidee_cnp_C3Crop = ds_orchidee_cnp['landCoverFrac'][0,10,:,:] + \
                             ds_orchidee_cnp['landCoverFrac'][0,13,:,:]
    ds_orchidee_cnp_C4Crop = ds_orchidee_cnp['landCoverFrac'][0,12,:,:] + \
                             ds_orchidee_cnp['landCoverFrac'][0,14,:,:]

    ds_orchidee_EVG = ds_orchidee['landCoverFrac'][0,1,:,:] + \
                          ds_orchidee['landCoverFrac'][0,3,:,:] + \
                          ds_orchidee['landCoverFrac'][0,4,:,:] + \
                          ds_orchidee['landCoverFrac'][0,6,:,:]
    ds_orchidee_DCD = ds_orchidee['landCoverFrac'][0,2,:,:] + \
                          ds_orchidee['landCoverFrac'][0,5,:,:] + \
                          ds_orchidee['landCoverFrac'][0,7,:,:] + \
                          ds_orchidee['landCoverFrac'][0,8,:,:]
    ds_orchidee_C3G = ds_orchidee['landCoverFrac'][0,9,:,:] + \
                      ds_orchidee['landCoverFrac'][0,13,:,:] + \
                      ds_orchidee['landCoverFrac'][0,14,:,:]
    ds_orchidee_C4G = ds_orchidee['landCoverFrac'][0,10,:,:]
    ds_orchidee_C3Crop = ds_orchidee['landCoverFrac'][0,11,:,:]
    ds_orchidee_C4Crop = ds_orchidee['landCoverFrac'][0,12,:,:]

    ds_sdgvm_EVG = ds_sdgvm['landCoverFrac'][0,8,:,:] + \
                   ds_sdgvm['landCoverFrac'][0,9,:,:]
    ds_sdgvm_DCD = ds_sdgvm['landCoverFrac'][0,6,:,:] + \
                   ds_sdgvm['landCoverFrac'][0,7,:,:]
    ds_sdgvm_C3G = ds_sdgvm['landCoverFrac'][0,2,:,:]
    ds_sdgvm_C4G = ds_sdgvm['landCoverFrac'][0,4,:,:]
    ds_sdgvm_C3Crop = ds_sdgvm['landCoverFrac'][0,3,:,:]
    ds_sdgvm_C4Crop = ds_sdgvm['landCoverFrac'][0,5,:,:]

    ds_visit_EVG = ds_visit['landCoverFrac'][0,0,:,:] + \
                   ds_visit['landCoverFrac'][0,2,:,:] + \
                   ds_visit['landCoverFrac'][0,3,:,:] + \
                   ds_visit['landCoverFrac'][0,5,:,:]
    ds_visit_DCD = ds_visit['landCoverFrac'][0,1,:,:] + \
                   ds_visit['landCoverFrac'][0,4,:,:] + \
                   ds_visit['landCoverFrac'][0,6,:,:]
    ds_visit_C3G = ds_visit['landCoverFrac'][0,9,:,:]
    ds_visit_C4G = ds_visit['landCoverFrac'][0,9,:,:]*0
    ds_visit_C3Crop = ds_visit['landCoverFrac'][0,15,:,:]
    ds_visit_C4Crop = ds_visit['landCoverFrac'][0,8,:,:]*0

    if model == 'CABLE-POP':
        return(ds_cable_EVG, ds_cable_DCD, ds_cable_C3G, ds_cable_C4G)
    elif model == 'CLASS-CTEM':
        return(ds_class_ctem_EVG, ds_class_ctem_DCD, ds_class_ctem_C3G,
               ds_class_ctem_C4G, ds_class_ctem_C3Crop, ds_class_ctem_C4Crop)
    elif model == 'CLM5.0':
        return(ds_clm_EVG, ds_clm_DCD, ds_clm_C3G, ds_clm_C4G, ds_clm_C3Crop,
               ds_clm_C4Crop)
    elif model == 'ISAM':
        return(ds_isam_EVG, ds_isam_DCD, ds_isam_C3G, ds_isam_C4G,
               ds_isam_C3Crop, ds_isam_C4Crop)
    elif model == 'ISBA-CTRIP':
        return(ds_isba_ctrip_EVG, ds_isba_ctrip_DCD, ds_isba_ctrip_C3G,
               ds_isba_ctrip_C4G, ds_isba_ctrip_C3Crop, ds_isba_ctrip_C4Crop)
    elif model == 'JSBACH':
        return(ds_jsbach_EVG, ds_jsbach_DCD, ds_jsbach_C3G,
               ds_jsbach_C4G, ds_jsbach_C3Crop, ds_jsbach_C4Crop)
    elif model == 'JULES-ES':
        return(ds_jules_EVG, ds_jules_DCD, ds_jules_C3G,
               ds_jules_C4G, ds_jules_C3Crop, ds_jules_C4Crop)
    elif model == 'LPX-Bern':
        return(ds_lpx_EVG, ds_lpx_DCD, ds_lpx_C3G, ds_lpx_C4G, ds_lpx_C3Crop,
               ds_lpx_C4Crop)
    elif model == 'OCN':
        return(ds_ocn_EVG, ds_ocn_DCD, ds_ocn_C3G,
               ds_ocn_C4G, ds_ocn_C3Crop, ds_ocn_C4Crop)
    elif model == 'ORCHIDEE-CNP':
        return(ds_orchidee_cnp_EVG, ds_orchidee_cnp_DCD, ds_orchidee_cnp_C3G,
               ds_orchidee_cnp_C4G, ds_orchidee_cnp_C3Crop,
               ds_orchidee_cnp_C4Crop)
    elif model == 'ORCHIDEE':
        return(ds_orchidee_EVG, ds_orchidee_DCD, ds_orchidee_C3G,
               ds_orchidee_C4G, ds_orchidee_C3Crop, ds_orchidee_C4Crop)
    elif model == 'SDGVM':
        return(ds_sdgvm_EVG, ds_sdgvm_DCD, ds_sdgvm_C3G, ds_sdgvm_C4G,
               ds_sdgvm_C3Crop, ds_sdgvm_C4Crop)
    elif model == 'VISIT':
        return(ds_visit_EVG, ds_visit_DCD, ds_visit_C3G, ds_visit_C4G,
               ds_visit_C3Crop, ds_visit_C4Crop)

def lcf_corr(model, var):
    fname = ('../'+var+'/sh_year/'+model+'_S3_'+var+'_australia_annual.nc')
    fname_ensmean = ('../'+var+'/sh_year/ensmean_australia_annual.nc')

    if model in ('ISAM', 'ISBA-CTRIP', 'VISIT'):
        ds = xr.open_dataset(fname, decode_times=False)
        ds['time']=pd.date_range(start='1/1/1901', freq='Y', periods=ds.time.size)
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
