import numpy as np
import h5py
import pandas as pd

months = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
sources = ['SAVA', 'BORF', 'TEMF', 'DEFO', 'PEAT', 'AGRI']

"""
Read in emission factors
"""
species = []
EFs     = np.zeros((41, 6))

k = 0
f = open('GFED4_Emission_Factors.txt')
while 1:
    line = f.readline()
    if line == "":
        break

    if line[0] != '#':
        contents = line.split()
        species.append(contents[0])
        EFs[k,:] = contents[1:]
        k += 1

f.close()

def monthly_emissions(month, index):
    EF_CO2 = EFs[2,:]

    start_year = 2001
    end_year   = 2019

    """
    make table with summed DM emissions for each region, year, and source
    """
    CO2_table = np.zeros((1, end_year - start_year + 1))

    for year in range(start_year, end_year+1):
        if year in (2017, 2018, 2019):
            string = 'hdf5/GFED4.1s_'+str(year)+'_beta.hdf5'
        else:
            string = 'hdf5/GFED4.1s_'+str(year)+'.hdf5'
        f = h5py.File(string, 'r')

        if year == start_year:
            basis_regions = f['/ancill/basis_regions'][:]
            grid_area     = f['/ancill/grid_cell_area'][:]

        CO2_emissions = np.zeros((720, 1440))

        string = '/emissions/'+months[index]+'/DM'
        DM_emissions = f[string][:]

        for source in range(6):
            # read in the fractional contribution of each source
            string = '/emissions/'+months[index]+'/partitioning/DM_'+sources[source]
            contribution = f[string][:]
            # calculate CO emissions as the product of DM emissions (kg DM per
            # m2 per month), the fraction the specific source contributes to
            # this (unitless), and the emission factor (g CO per kg DM burned)
            CO2_emissions += DM_emissions * contribution * EF_CO2[source]

        # fill table with total values for Australia
        mask = basis_regions == (14)
        CO2_table[0, year-start_year] = np.sum(grid_area * mask * CO2_emissions)

        print(year)

    CO2_table = CO2_table / 1E12

    return(CO2_table)

month_names = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
               'August', 'September', 'October', 'November', 'December']
indices = [0,1,2,3,4,5,6,7,8,9,10,11]

df = pd.DataFrame()
for mn, i in zip(month_names, indices):
    CO2_table=monthly_emissions(mn, i)
    df[mn]=CO2_table.flatten()

df.to_csv('GFED4s_monthly.csv', index=False)
