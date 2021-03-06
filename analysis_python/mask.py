import numpy as np
import netCDF4 as nc
import matplotlib.pyplot as plt
import pandas as pd
from pylab import text
import matplotlib.gridspec as gridspec

pathwayIN_trendy = '/srv/ccrc/data02/z5227845/research/TRENDY_v8/impact_analysis/'
pathwayIN_gosif = '/srv/ccrc/data02/z5227845/research/SIF/TRENDY_comparison/'

data_vegetation_mask = nc.Dataset('../vegetation_mask.nc')
vegetation_mask = data_vegetation_mask.variables['land_cover'][:,:]

tropics_mask = vegetation_mask != 1
savanna_mask = vegetation_mask != 2
warm_temperate_mask = vegetation_mask != 3
cool_temperate_mask = vegetation_mask != 4
mediterranean_mask = vegetation_mask !=5
desert_mask = vegetation_mask !=6
total_mask = vegetation_mask > 6
total_mask = total_mask < 0

model_names = ['CABLE-POP', 'CLASS-CTEM', 'CLM5.0', 'ISAM', 'ISBA-CTRIP',
               'JSBACH', 'JULES-ES', 'LPX-Bern', 'OCN', 'ORCHIDEE',
               'ORCHIDEE-CNP', 'SDGVM', 'VISIT']
colours = ['tab:blue', 'tab:orange', 'tab:green', 'tab:red', 'tab:purple',
           'tab:brown', 'tab:pink', 'tab:olive', 'navy', 'tab:cyan',
           'rosybrown', 'gold', 'purple']

titles = ['Total', 'Tropics', 'Savanna', 'Warm temperate', 'Cool temperate',
          'Mediterranean', 'Desert']

veg_masks = [total_mask, tropics_mask, savanna_mask, warm_temperate_mask,
              cool_temperate_mask, mediterranean_mask, desert_mask]

def mask(time_res, exp, var, veg_mask, modelname):
    if time_res == 'annual':
        if modelname == 'SDGVM':
            if var == 'nbp':
                data_model = nc.Dataset('../../TRENDY_v9/impact_analysis/'+exp+
                                        '/sh_year/'+modelname+'_'+exp+'_'+var+
                                        '_australia_annual_area_weighted.nc')
            elif var in ('cVeg', 'cSoil', 'npp', 'fFire'):
                data_model = nc.Dataset('../../TRENDY_v9/'+var+'/sh_year/'+modelname+
                                        '_'+exp+'_'+var+
                                        '_australia_annual_area_weighted.nc')

        else:
            if var == 'nbp':
                data_model = nc.Dataset('../impact_analysis/'+exp+'/sh_year/'+
                                        modelname+'_'+exp+'_'+var+
                                        '_australia_annual_area_weighted.nc')
            elif var in ('cVeg', 'cSoil', 'npp', 'fFire'):
                data_model = nc.Dataset('../'+var+'/sh_year/'+modelname+'_'+exp+'_'+
                                        var+'_australia_annual_area_weighted.nc')
            elif var == 'Aboveground Biomass Carbon':
                data_model = nc.Dataset('../../VOD/cVeg_1992-2012.nc')
            elif var == 'co2fire':
                data_model = nc.Dataset('../../CAMS_GFAS/sh_year/CMAS_GFAS_fFire_australia_annual_area_weighted.nc')

        if var =='fFire':
            model = data_model.variables[var][-16:,:,:]
        else:
            model = data_model.variables[var][:,:,:]
        model_masked = np.ma.array(model, mask = model*veg_mask[np.newaxis,:,:])

        timeseries_model = []

        if var == 'Aboveground Biomass Carbon':
            for i in range(0,19):
                sum_model = model_masked[i,:,:].sum()
                timeseries_model.append(sum_model)
        elif var in ('co2fire', 'fFire'):
            for i in range(0,15):
                sum_model = model_masked[i,:,:].sum()
                timeseries_model.append(sum_model)
        else:
            for i in range(0,117):
                sum_model = model_masked[i,:,:].sum()
                timeseries_model.append(sum_model)

    elif time_res == 'monthly':
        if var == 'fFire':
            if modelname == 'SDGVM':
                data_model = nc.Dataset('../../TRENDY_v9/fFire/sh_year/'+
                                        modelname+'_S3_'+var+
                                        '_australia_monthly_area_weighted.nc')
            else:
                data_model = nc.Dataset('../fFire/sh_year/'+modelname+'_S3_'+
                                        var+'_australia_monthly_area_weighted.nc')
            model = data_model.variables[var][-192:,:,:]
        else:
            data_model = nc.Dataset('../../CAMS_GFAS/sh_year/CMAS_GFAS_fFire_australia_monthly_area_weighted.nc')
            model = data_model.variables[var][:,:,:]

        model_masked = np.ma.array(model, mask = model*veg_mask[np.newaxis,:,:])
        timeseries_model = []

        if var == 'prec':
            for i in range(0,155):
                sum_data = model_masked[i,:,:].sum()
                sum_gridarea = gridarea_masked[:,:].sum()
                mean_data = (sum_data/sum_gridarea)*10000000
                timeseries_model.append(mean_data)
        else:
            for i in range(0,192):
                sum_model = model_masked[i,:,:].sum()
                timeseries_model.append(sum_model)

    return(timeseries_model)
