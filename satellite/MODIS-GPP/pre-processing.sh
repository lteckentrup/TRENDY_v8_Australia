gdal_translate -of NetCDF tif/MOD17A2HGF.006_Gpp_500m_doy2000361_aid0001.tif \
               netcdf/MODIS_GPP_doy2000361.nc
cdo -L -b F64 -chname,Band1,GPP -mulc,0.0001 -setrtomiss,32760,32767 \
    netcdf/MODIS_GPP_doy2000361.nc netcdf/MODIS_GPP_2000361.nc

cdo -L -b F64 -settaxis,2000-12-28,00:00,1day \
    netcdf/MODIS_GPP_2000361.nc netcdf/MODIS_GPP_2000-12-27.nc

rm netcdf/MODIS_GPP_doy2000361.nc
rm netcdf/MODIS_GPP_2000361.nc

for year in {2001..2018..1}; do
    for step in {001..361..8}; do
      gdal_translate -of NetCDF \
                     tif/MOD17A2HGF.006_Gpp_500m_doy${year}${step}_aid0001.tif \
                     netcdf/MODIS_GPP_doy${year}${step}.nc
      cdo -L -b F64 -chname,Band1,GPP -mulc,0.0001 -setrtomiss,32762,3276 \
          netcdf/MODIS_GPP_doy${year}${step}.nc netcdf/MODIS_GPP_${year}${step}.nc

      rm netcdf/MODIS_GPP_doy${year}${step}.nc
    done

  if [[ $year = 2004 ]] || [[ $year = 2008 ]] || [[ $year = 2012 ]] || [[ $year = 2016 ]]
  then
      cdo -L -b F64 -settaxis,${year}-01-01,00:00,1day \
          netcdf/MODIS_GPP_${year}001.nc netcdf/MODIS_GPP_${year}-01-01.nc
      cdo -L -b F64 -settaxis,${year}-01-09,00:00,1day \
          netcdf/MODIS_GPP_${year}009.nc netcdf/MODIS_GPP_${year}-01-09.nc
      cdo -L -b F64 -settaxis,${year}-01-17,00:00,1day \
          netcdf/MODIS_GPP_${year}017.nc netcdf/MODIS_GPP_${year}-01-17.nc
      cdo -L -b F64 -settaxis,${year}-01-25,00:00,1day \
          netcdf/MODIS_GPP_${year}025.nc netcdf/MODIS_GPP_${year}-01-25.nc
      cdo -L -b F64 -settaxis,${year}-02-02,00:00,1day \
          netcdf/MODIS_GPP_${year}033.nc netcdf/MODIS_GPP_${year}-02-02.nc
      cdo -L -b F64 -settaxis,${year}-02-10,00:00,1day \
          netcdf/MODIS_GPP_${year}041.nc netcdf/MODIS_GPP_${year}-02-10.nc
      cdo -L -b F64 -settaxis,${year}-02-18,00:00,1day \
          netcdf/MODIS_GPP_${year}049.nc netcdf/MODIS_GPP_${year}-02-18.nc
      cdo -L -b F64 -settaxis,${year}-02-26,00:00,1day \
          netcdf/MODIS_GPP_${year}057.nc netcdf/MODIS_GPP_${year}-02-26.nc
      cdo -L -b F64 -settaxis,${year}-03-05,00:00,1day \
          netcdf/MODIS_GPP_${year}065.nc netcdf/MODIS_GPP_${year}-03-05.nc
      cdo -L -b F64 -settaxis,${year}-03-13,00:00,1day \
          netcdf/MODIS_GPP_${year}073.nc netcdf/MODIS_GPP_${year}-03-13.nc
      cdo -L -b F64 -settaxis,${year}-03-21,00:00,1day \
          netcdf/MODIS_GPP_${year}081.nc netcdf/MODIS_GPP_${year}-03-21.nc
      cdo -L -b F64 -settaxis,${year}-03-29,00:00,1day \
          netcdf/MODIS_GPP_${year}089.nc netcdf/MODIS_GPP_${year}-03-29.nc
      cdo -L -b F64 -settaxis,${year}-04-06,00:00,1day \
          netcdf/MODIS_GPP_${year}097.nc netcdf/MODIS_GPP_${year}-04-06.nc
      cdo -L -b F64 -settaxis,${year}-04-14,00:00,1day \
          netcdf/MODIS_GPP_${year}105.nc netcdf/MODIS_GPP_${year}-04-14.nc
      cdo -L -b F64 -settaxis,${year}-04-22,00:00,1day \
          netcdf/MODIS_GPP_${year}113.nc netcdf/MODIS_GPP_${year}-04-22.nc
      cdo -L -b F64 -settaxis,${year}-04-30,00:00,1day \
          netcdf/MODIS_GPP_${year}121.nc netcdf/MODIS_GPP_${year}-04-30.nc
      cdo -L -b F64 -settaxis,${year}-05-08,00:00,1day \
          netcdf/MODIS_GPP_${year}129.nc netcdf/MODIS_GPP_${year}-05-08.nc
      cdo -L -b F64 -settaxis,${year}-05-16,00:00,1day \
          netcdf/MODIS_GPP_${year}137.nc netcdf/MODIS_GPP_${year}-05-16.nc
      cdo -L -b F64 -settaxis,${year}-05-24,00:00,1day \
          netcdf/MODIS_GPP_${year}145.nc netcdf/MODIS_GPP_${year}-05-24.nc
      cdo -L -b F64 -settaxis,${year}-06-01,00:00,1day \
          netcdf/MODIS_GPP_${year}153.nc netcdf/MODIS_GPP_${year}-06-01.nc
      cdo -L -b F64 -settaxis,${year}-06-09,00:00,1day \
          netcdf/MODIS_GPP_${year}161.nc netcdf/MODIS_GPP_${year}-06-09.nc
      cdo -L -b F64 -settaxis,${year}-06-17,00:00,1day \
          netcdf/MODIS_GPP_${year}169.nc netcdf/MODIS_GPP_${year}-06-17.nc
      cdo -L -b F64 -settaxis,${year}-06-25,00:00,1day \
          netcdf/MODIS_GPP_${year}177.nc netcdf/MODIS_GPP_${year}-06-25.nc
      cdo -L -b F64 -settaxis,${year}-07-03,00:00,1day \
          netcdf/MODIS_GPP_${year}185.nc netcdf/MODIS_GPP_${year}-07-03.nc
      cdo -L -b F64 -settaxis,${year}-07-11,00:00,1day \
          netcdf/MODIS_GPP_${year}193.nc netcdf/MODIS_GPP_${year}-07-11.nc
      cdo -L -b F64 -settaxis,${year}-07-19,00:00,1day \
          netcdf/MODIS_GPP_${year}201.nc netcdf/MODIS_GPP_${year}-07-19.nc
      cdo -L -b F64 -settaxis,${year}-07-27,00:00,1day \
          netcdf/MODIS_GPP_${year}209.nc netcdf/MODIS_GPP_${year}-07-27.nc
      cdo -L -b F64 -settaxis,${year}-08-04,00:00,1day \
          netcdf/MODIS_GPP_${year}217.nc netcdf/MODIS_GPP_${year}-08-04.nc
      cdo -L -b F64 -settaxis,${year}-08-12,00:00,1day \
          netcdf/MODIS_GPP_${year}225.nc netcdf/MODIS_GPP_${year}-08-12.nc
      cdo -L -b F64 -settaxis,${year}-08-20,00:00,1day \
          netcdf/MODIS_GPP_${year}233.nc netcdf/MODIS_GPP_${year}-08-20.nc
      cdo -L -b F64 -settaxis,${year}-08-28,00:00,1day \
          netcdf/MODIS_GPP_${year}241.nc netcdf/MODIS_GPP_${year}-08-28.nc
      cdo -L -b F64 -settaxis,${year}-09-05,00:00,1day \
          netcdf/MODIS_GPP_${year}249.nc netcdf/MODIS_GPP_${year}-09-05.nc
      cdo -L -b F64 -settaxis,${year}-09-13,00:00,1day \
          netcdf/MODIS_GPP_${year}257.nc netcdf/MODIS_GPP_${year}-09-13.nc
      cdo -L -b F64 -settaxis,${year}-09-21,00:00,1day \
          netcdf/MODIS_GPP_${year}265.nc netcdf/MODIS_GPP_${year}-09-21.nc
      cdo -L -b F64 -settaxis,${year}-09-29,00:00,1day \
          netcdf/MODIS_GPP_${year}273.nc netcdf/MODIS_GPP_${year}-09-29.nc
      cdo -L -b F64 -settaxis,${year}-10-07,00:00,1day \
          netcdf/MODIS_GPP_${year}281.nc netcdf/MODIS_GPP_${year}-10-07.nc
      cdo -L -b F64 -settaxis,${year}-10-15,00:00,1day \
          netcdf/MODIS_GPP_${year}289.nc netcdf/MODIS_GPP_${year}-10-15.nc
      cdo -L -b F64 -settaxis,${year}-10-23,00:00,1day \
          netcdf/MODIS_GPP_${year}297.nc netcdf/MODIS_GPP_${year}-10-23.nc
      cdo -L -b F64 -settaxis,${year}-10-31,00:00,1day \
          netcdf/MODIS_GPP_${year}305.nc netcdf/MODIS_GPP_${year}-10-31.nc
      cdo -L -b F64 -settaxis,${year}-11-08,00:00,1day \
          netcdf/MODIS_GPP_${year}313.nc netcdf/MODIS_GPP_${year}-11-08.nc
      cdo -L -b F64 -settaxis,${year}-11-16,00:00,1day \
          netcdf/MODIS_GPP_${year}321.nc netcdf/MODIS_GPP_${year}-11-16.nc
      cdo -L -b F64 -settaxis,${year}-11-24,00:00,1day \
          netcdf/MODIS_GPP_${year}329.nc netcdf/MODIS_GPP_${year}-11-24.nc
      cdo -L -b F64 -settaxis,${year}-12-02,00:00,1day \
          netcdf/MODIS_GPP_${year}337.nc netcdf/MODIS_GPP_${year}-12-02.nc
      cdo -L -b F64 -settaxis,${year}-12-10,00:00,1day \
          netcdf/MODIS_GPP_${year}345.nc netcdf/MODIS_GPP_${year}-12-10.nc
      cdo -L -b F64 -settaxis,${year}-12-18,00:00,1day \
          netcdf/MODIS_GPP_${year}353.nc netcdf/MODIS_GPP_${year}-12-18.nc
      cdo -L -b F64 -settaxis,${year}-12-26,00:00,1day \
          netcdf/MODIS_GPP_${year}361.nc netcdf/MODIS_GPP_${year}-12-26.nc

    else
      cdo -L -b F64 -settaxis,${year}-01-01,00:00,1day \
          netcdf/MODIS_GPP_${year}001.nc netcdf/MODIS_GPP_${year}-01-01.nc
      cdo -L -b F64 -settaxis,${year}-01-09,00:00,1day \
          netcdf/MODIS_GPP_${year}009.nc netcdf/MODIS_GPP_${year}-01-09.nc
      cdo -L -b F64 -settaxis,${year}-01-17,00:00,1day \
          netcdf/MODIS_GPP_${year}017.nc netcdf/MODIS_GPP_${year}-01-17.nc
      cdo -L -b F64 -settaxis,${year}-01-25,00:00,1day \
          netcdf/MODIS_GPP_${year}025.nc netcdf/MODIS_GPP_${year}-01-25.nc
      cdo -L -b F64 -settaxis,${year}-02-02,00:00,1day \
          netcdf/MODIS_GPP_${year}033.nc netcdf/MODIS_GPP_${year}-02-02.nc
      cdo -L -b F64 -settaxis,${year}-02-10,00:00,1day \
          netcdf/MODIS_GPP_${year}041.nc netcdf/MODIS_GPP_${year}-02-10.nc
      cdo -L -b F64 -settaxis,${year}-02-18,00:00,1day \
          netcdf/MODIS_GPP_${year}049.nc netcdf/MODIS_GPP_${year}-02-18.nc
      cdo -L -b F64 -settaxis,${year}-02-26,00:00,1day \
          netcdf/MODIS_GPP_${year}057.nc netcdf/MODIS_GPP_${year}-02-26.nc
      cdo -L -b F64 -settaxis,${year}-03-06,00:00,1day \
          netcdf/MODIS_GPP_${year}065.nc netcdf/MODIS_GPP_${year}-03-06.nc
      cdo -L -b F64 -settaxis,${year}-03-14,00:00,1day \
          netcdf/MODIS_GPP_${year}073.nc netcdf/MODIS_GPP_${year}-03-14.nc
      cdo -L -b F64 -settaxis,${year}-03-22,00:00,1day \
          netcdf/MODIS_GPP_${year}081.nc netcdf/MODIS_GPP_${year}-03-22.nc
      cdo -L -b F64 -settaxis,${year}-03-30,00:00,1day \
          netcdf/MODIS_GPP_${year}089.nc netcdf/MODIS_GPP_${year}-03-30.nc
      cdo -L -b F64 -settaxis,${year}-04-07,00:00,1day \
          netcdf/MODIS_GPP_${year}097.nc netcdf/MODIS_GPP_${year}-04-07.nc
      cdo -L -b F64 -settaxis,${year}-04-15,00:00,1day \
          netcdf/MODIS_GPP_${year}105.nc netcdf/MODIS_GPP_${year}-04-15.nc
      cdo -L -b F64 -settaxis,${year}-04-23,00:00,1day \
          netcdf/MODIS_GPP_${year}113.nc netcdf/MODIS_GPP_${year}-04-23.nc
      cdo -L -b F64 -settaxis,${year}-05-01,00:00,1day \
          netcdf/MODIS_GPP_${year}121.nc netcdf/MODIS_GPP_${year}-05-01.nc
      cdo -L -b F64 -settaxis,${year}-05-09,00:00,1day \
          netcdf/MODIS_GPP_${year}129.nc netcdf/MODIS_GPP_${year}-05-09.nc
      cdo -L -b F64 -settaxis,${year}-05-17,00:00,1day \
          netcdf/MODIS_GPP_${year}137.nc netcdf/MODIS_GPP_${year}-05-17.nc
      cdo -L -b F64 -settaxis,${year}-05-25,00:00,1day \
          netcdf/MODIS_GPP_${year}145.nc netcdf/MODIS_GPP_${year}-05-25.nc
      cdo -L -b F64 -settaxis,${year}-06-02,00:00,1day \
          netcdf/MODIS_GPP_${year}153.nc netcdf/MODIS_GPP_${year}-06-02.nc
      cdo -L -b F64 -settaxis,${year}-06-10,00:00,1day \
          netcdf/MODIS_GPP_${year}161.nc netcdf/MODIS_GPP_${year}-06-10.nc
      cdo -L -b F64 -settaxis,${year}-06-18,00:00,1day \
          netcdf/MODIS_GPP_${year}169.nc netcdf/MODIS_GPP_${year}-06-18.nc
      cdo -L -b F64 -settaxis,${year}-06-26,00:00,1day \
          netcdf/MODIS_GPP_${year}177.nc netcdf/MODIS_GPP_${year}-06-26.nc
      cdo -L -b F64 -settaxis,${year}-07-04,00:00,1day \
          netcdf/MODIS_GPP_${year}185.nc netcdf/MODIS_GPP_${year}-07-04.nc
      cdo -L -b F64 -settaxis,${year}-07-12,00:00,1day \
          netcdf/MODIS_GPP_${year}193.nc netcdf/MODIS_GPP_${year}-07-12.nc
      cdo -L -b F64 -settaxis,${year}-07-20,00:00,1day \
          netcdf/MODIS_GPP_${year}201.nc netcdf/MODIS_GPP_${year}-07-20.nc
      cdo -L -b F64 -settaxis,${year}-07-28,00:00,1day \
          netcdf/MODIS_GPP_${year}209.nc netcdf/MODIS_GPP_${year}-07-28.nc
      cdo -L -b F64 -settaxis,${year}-08-05,00:00,1day \
          netcdf/MODIS_GPP_${year}217.nc netcdf/MODIS_GPP_${year}-08-05.nc
      cdo -L -b F64 -settaxis,${year}-08-13,00:00,1day \
          netcdf/MODIS_GPP_${year}225.nc netcdf/MODIS_GPP_${year}-08-13.nc
      cdo -L -b F64 -settaxis,${year}-08-21,00:00,1day \
          netcdf/MODIS_GPP_${year}233.nc netcdf/MODIS_GPP_${year}-08-21.nc
      cdo -L -b F64 -settaxis,${year}-08-29,00:00,1day \
          netcdf/MODIS_GPP_${year}241.nc netcdf/MODIS_GPP_${year}-08-29.nc
      cdo -L -b F64 -settaxis,${year}-09-06,00:00,1day \
          netcdf/MODIS_GPP_${year}249.nc netcdf/MODIS_GPP_${year}-09-05.nc
      cdo -L -b F64 -settaxis,${year}-09-14,00:00,1day \
          netcdf/MODIS_GPP_${year}257.nc netcdf/MODIS_GPP_${year}-09-14.nc
      cdo -L -b F64 -settaxis,${year}-09-22,00:00,1day \
          netcdf/MODIS_GPP_${year}265.nc netcdf/MODIS_GPP_${year}-09-22.nc
      cdo -L -b F64 -settaxis,${year}-09-30,00:00,1day \
          netcdf/MODIS_GPP_${year}273.nc netcdf/MODIS_GPP_${year}-09-30.nc
      cdo -L -b F64 -settaxis,${year}-10-08,00:00,1day \
          netcdf/MODIS_GPP_${year}281.nc netcdf/MODIS_GPP_${year}-10-08.nc
      cdo -L -b F64 -settaxis,${year}-10-16,00:00,1day \
          netcdf/MODIS_GPP_${year}289.nc netcdf/MODIS_GPP_${year}-10-15.nc
      cdo -L -b F64 -settaxis,${year}-10-24,00:00,1day \
          netcdf/MODIS_GPP_${year}297.nc netcdf/MODIS_GPP_${year}-10-24.nc
      cdo -L -b F64 -settaxis,${year}-11-01,00:00,1day \
          netcdf/MODIS_GPP_${year}305.nc netcdf/MODIS_GPP_${year}-11-01.nc
      cdo -L -b F64 -settaxis,${year}-11-09,00:00,1day \
          netcdf/MODIS_GPP_${year}313.nc netcdf/MODIS_GPP_${year}-11-09.nc
      cdo -L -b F64 -settaxis,${year}-11-17,00:00,1day \
          netcdf/MODIS_GPP_${year}321.nc netcdf/MODIS_GPP_${year}-11-17.nc
      cdo -L -b F64 -settaxis,${year}-11-25,00:00,1day \
          netcdf/MODIS_GPP_${year}329.nc netcdf/MODIS_GPP_${year}-11-25.nc
      cdo -L -b F64 -settaxis,${year}-12-03,00:00,1day \
          netcdf/MODIS_GPP_${year}337.nc netcdf/MODIS_GPP_${year}-12-03.nc
      cdo -L -b F64 -settaxis,${year}-12-11,00:00,1day \
          netcdf/MODIS_GPP_${year}345.nc netcdf/MODIS_GPP_${year}-12-11.nc
      cdo -L -b F64 -settaxis,${year}-12-19,00:00,1day \
          netcdf/MODIS_GPP_${year}353.nc netcdf/MODIS_GPP_${year}-12-19.nc
      cdo -L -b F64 -settaxis,${year}-12-27,00:00,1day \
          netcdf/MODIS_GPP_${year}361.nc netcdf/MODIS_GPP_${year}-12-27.nc

  fi

  for step in {001..361..8}; do
      rm netcdf/MODIS_GPP_${year}${step}.nc
  done 
done

for year in {2001..2018..1}; do
    cdo mergetime netcdf/MODIS_GPP_${year}-01*.nc netcdf/MODIS_GPP_${year}-01.nc
    cdo mergetime netcdf/MODIS_GPP_${year}-02*.nc netcdf/MODIS_GPP_${year}-02.nc
    cdo mergetime netcdf/MODIS_GPP_${year}-03*.nc netcdf/MODIS_GPP_${year}-03.nc
    cdo mergetime netcdf/MODIS_GPP_${year}-04*.nc netcdf/MODIS_GPP_${year}-04.nc
    cdo mergetime netcdf/MODIS_GPP_${year}-05*.nc netcdf/MODIS_GPP_${year}-05.nc
    cdo mergetime netcdf/MODIS_GPP_${year}-06*.nc netcdf/MODIS_GPP_${year}-06.nc
    cdo mergetime netcdf/MODIS_GPP_${year}-07*.nc netcdf/MODIS_GPP_${year}-07.nc
    cdo mergetime netcdf/MODIS_GPP_${year}-08*.nc netcdf/MODIS_GPP_${year}-08.nc
    cdo mergetime netcdf/MODIS_GPP_${year}-09*.nc netcdf/MODIS_GPP_${year}-09.nc
    cdo mergetime netcdf/MODIS_GPP_${year}-10*.nc netcdf/MODIS_GPP_${year}-10.nc
    cdo mergetime netcdf/MODIS_GPP_${year}-11*.nc netcdf/MODIS_GPP_${year}-11.nc
    cdo mergetime netcdf/MODIS_GPP_${year}-12*.nc netcdf/MODIS_GPP_${year}-12.nc
  
  for month in {01..12..1}; do
      cdo -b F64 monthsum netcdf/MODIS_GPP_${year}_${month}.nc \
          netcdf/MODIS_GPP_${year}_${month}_monthsum.nc
      cdo -b F64 remapycon,fine_grid.txt \
          netcdf/MODIS_GPP_${year}_${month}_monthsum.nc \
          netcdf/MODIS_GPP_${year}_${month}_remapycon.nc
      cdo -b F64 sellonlatbox,112.25,153.75,-43.75,-9.75 \
          netcdf/MODIS_GPP_${year}_${month}_remapycon.nc \
          MODIS_GPP_${year}_${month}_australia.nc

      rm netcdf/MODIS_GPP_${year}_${month}.nc
      rm netcdf/MODIS_GPP_${year}_${month}_monthsum.nc
      rm netcdf/MODIS_GPP_${year}_${month}_remapycon.nc
   done   
done
