for exp in S0 S1 S2 S3 S4; do
    for var in nbp gpp ra rh fFire evapotrans lai landCoverFrac cVeg; do
        mv $exp'/'$var'/'CLM5.0_$exp'_'$var'.'nc \
           $exp'/'$var'/'CLM5.0_$exp'_'$var'_'original.nc
        
        ### remove time bounds
        ncatted -O -a bounds,time,d,, $exp'/'$var'/'CLM5.0_$exp'_'$var'_'original.nc \
                                      $exp'/'$var'/'CLM5.0_$exp'_'$var'.'nc

        mv $exp'/'$var'/'ISBA-CTRIP_$exp'_'$var'.'nc \
           $exp'/'$var'/'ISBA-CTRIP_$exp'_'$var'_'original.nc
        ### rename lon_Full to lon and lat_Full to lat
        ncrename -v lon_FULL,lon -v lat_FULL,lat \
           $exp'/'$var'/'ISBA-CTRIP_$exp'_'$var'_'original.nc \
           $exp'/'$var'/'ISBA_test.nc
          
        ### remove lon_FULL_bnds
        ncks -C -O -x -v lon_FULL_bnds $exp'/'$var'/'ISBA_test.nc \
           $exp'/'$var'/'ISBA_test1.nc
           
        ### remove lat_FULL_bnds
        ncks -C -O -x -v lat_FULL_bnds $exp'/'$var'/'ISBA_test1.nc \
           $exp'/'$var'/'ISBA_test2.nc
        
        ### rename time dimension
        ncrename -v time_counter,time $exp'/'$var'/'ISBA_test2.nc \
           $exp'/'$var'/'ISBA_test3.nc
         
        ### remove longitude bounds
        ncatted -O -a bounds,lon,d,, $exp'/'$var'/'ISBA_test3.nc \
           $exp'/'$var'/'ISBA_test4.nc
         
        ##3 remove latitude bounds
        ncatted -O -a bounds,lat,d,, $exp'/'$var'/'ISBA_test4.nc \
           $exp'/'$var'/'ISBA-CTRIP_$exp'_'$var'.'nc

        rm $exp'/'$var'/'ISBA_test.nc
        rm $exp'/'$var'/'ISBA_test1.nc
        rm $exp'/'$var'/'ISBA_test2.nc
        rm $exp'/'$var'/'ISBA_test3.nc
        rm $exp'/'$var'/'ISBA_test4.nc

        mv $exp'/'$var'/'DLEM_$exp'_'$var'.'nc \
           $exp'/'$var'/'DLEM_$exp'_'$var'_'original.nc
        
        ### rechunk to make calculations faster
        nccopy -c 'time/1,lat/,lon/' \
               $exp'/'$var'/'DLEM_$exp'_'$var'_'original.nc \
               $exp'/'$var'/'DLEM_$exp'_'$var'.'nc
        
        gunzip $exp'/'$var'/'VISIT_$exp'_'$var'.'nc.gz
    done
done

for exp in S0 S1 S2 S3 S4; do
    for var in nbp gpp ra rh fFire evapotrans cVeg; do
        mv $exp'/'$var'/'LPX-Bern_$exp'_'$var'.'nc \
           $exp'/'$var'/'LPX-Bern_$exp'_'$var'_'original.nc
           
        ### reorder coordinates to make model readable for CDO 
        ncpdq -F -O -a time,latitude,longitude \
              $exp'/'$var'/'LPX-Bern_$exp'_'$var'_'original.nc \
              $exp'/'$var'/'LPX-Bern_$exp'_'$var'_'fix_chunk.nc
        
        ### rechunk to make calculations faster
        nccopy -c 'time/1,latitude/,longitude/' \
               $exp'/'$var'/'LPX-Bern_$exp'_'$var'_'fix_chunk.nc \
               $exp'/'$var'/'LPX-Bern_$exp'_'$var'.'nc
    done
    for var in landCoverFrac lai; do
        mv $exp'/'$var'/'LPX-Bern_$exp'_'$var'.'nc \
           $exp'/'$var'/'LPX-Bern_$exp'_'$var'_'original.nc
           
        ### reorder coordinates to make model readable for CDO
        ncpdq -F -O -a time,PFT,latitude,longitude \
              $exp'/'$var'/'LPX-Bern_$exp'_'$var'_'original.nc \
              $exp'/'$var'/'LPX-Bern_$exp'_'$var'_'fix_chunk.nc
              
        ### rechunk to make calculations faster
        nccopy -c 'time/1,PFT/,latitude/,longitude/' \
               $exp'/'$var'/'LPX-Bern_$exp'_'$var'_'fix_chunk.nc \
               $exp'/'$var'/'LPX-Bern_$exp'_'$var'.'nc
    done
done

mv S3/landCoverFrac/CLM5.0_S3_landCoverFrac.nc S3/landCoverFrac/CLM5.0_S3_landCoverFrac_old.nc
ncrename -d ncl3,lon -d ncl2,lat -d ncl1,PFT -d ncl0,time \
         S3/landCoverFrac/CLM5.0_S3_landCoverFrac_old.nc S3/landCoverFrac/test.nc
cdo settaxis,1700-01-01,00:00,1month S3/landCoverFrac/test.nc \
    S3/landCoverFrac/test1.nc
cdo setgrid,S3/landCoverFrac/clm.txt S3/landCoverFrac/test1.nc \
    S3/landCoverFrac/CLM5.0_S3_landCoverFrac.nc

ncatted -O -a comment,global,a,c,"Land cover types:\n" \
        S3/landCoverFrac/CLM5.0_S3_landCoverFrac.nc
ncatted -O -a comment,global,a,c,"Level 1: not vegetated \n" \
        S3/landCoverFrac/CLM5.0_S3_landCoverFrac.nc
ncatted -O -a comment,global,a,c,"Level 2: needleleaf_evergreen_temperate_tree \n" \
        S3/landCoverFrac/CLM5.0_S3_landCoverFrac.nc 
ncatted -O -a comment,global,a,c,"Level 3: needleleaf_evergreen_boreal_tree	\n" \
        S3/landCoverFrac/CLM5.0_S3_landCoverFrac.nc
ncatted -O -a comment,global,a,c,"Level 4: needleleaf_deciduous_boreal_tree	\n" \
        S3/landCoverFrac/CLM5.0_S3_landCoverFrac.nc
ncatted -O -a comment,global,a,c,"Level 5: broadleaf_evergreen_tropical_tree \n" \
        S3/landCoverFrac/CLM5.0_S3_landCoverFrac.nc       
ncatted -O -a comment,global,a,c,"Level 6: broadleaf_evergreen_temperate_tree \n" \
        S3/landCoverFrac/CLM5.0_S3_landCoverFrac.nc
ncatted -O -a comment,global,a,c,"Level 7: broadleaf_deciduous_tropical_tree \n" \
        S3/landCoverFrac/CLM5.0_S3_landCoverFrac.nc 
ncatted -O -a comment,global,a,c,"Level 8: broadleaf_deciduous_temperate_tree	\n" \
        S3/landCoverFrac/CLM5.0_S3_landCoverFrac.nc
ncatted -O -a comment,global,a,c,"Level 9: broadleaf_deciduous_boreal_tree \n" \
        S3/landCoverFrac/CLM5.0_S3_landCoverFrac.nc
ncatted -O -a comment,global,a,c,"Level 10: broadleaf_evergreen_shrub \n" \
        S3/landCoverFrac/CLM5.0_S3_landCoverFrac.nc
ncatted -O -a comment,global,a,c,"Level 11: broadleaf_deciduous_temperate_shrub \n" \
        S3/landCoverFrac/CLM5.0_S3_landCoverFrac.nc
ncatted -O -a comment,global,a,c,"Level 12: broadleaf_deciduous_boreal_shrub \n" \
        S3/landCoverFrac/CLM5.0_S3_landCoverFrac.nc 
ncatted -O -a comment,global,a,c,"Level 13: c3_arctic_grass \n" \
        S3/landCoverFrac/CLM5.0_S3_landCoverFrac.nc
ncatted -O -a comment,global,a,c,"Level 14: c3_non-arctic_grass \n" \
        S3/landCoverFrac/CLM5.0_S3_landCoverFrac.nc
ncatted -O -a comment,global,a,c,"Level 15: c4_grass \n" \
        S3/landCoverFrac/CLM5.0_S3_landCoverFrac.nc       
ncatted -O -a comment,global,a,c,"Level 16: c3_crop \n" \
        S3/landCoverFrac/CLM5.0_S3_landCoverFrac.nc
ncatted -O -a comment,global,a,c,"Level 17: c3_irrigated \n" \
        S3/landCoverFrac/CLM5.0_S3_landCoverFrac.nc 
ncatted -O -a comment,global,a,c,"Level 18: temperate_corn \n" \
        S3/landCoverFrac/CLM5.0_S3_landCoverFrac.nc
ncatted -O -a comment,global,a,c,"Level 19: irrigated_temperate_corn \n" \
        S3/landCoverFrac/CLM5.0_S3_landCoverFrac.nc
ncatted -O -a comment,global,a,c,"Level 20: spring_wheat \n" \
        S3/landCoverFrac/CLM5.0_S3_landCoverFrac.nc
ncatted -O -a comment,global,a,c,"Level 21: irrigated_spring_wheat \n" \
        S3/landCoverFrac/CLM5.0_S3_landCoverFrac.nc
ncatted -O -a comment,global,a,c,"Level 22: winter_wheat (empty) \n" \
        S3/landCoverFrac/CLM5.0_S3_landCoverFrac.nc 
ncatted -O -a comment,global,a,c,"Level 23: irrigated_winter_wheat (empty) \n" \
        S3/landCoverFrac/CLM5.0_S3_landCoverFrac.nc
ncatted -O -a comment,global,a,c,"Level 24: temperate_soybean \n" \
        S3/landCoverFrac/CLM5.0_S3_landCoverFrac.nc
ncatted -O -a comment,global,a,c,"Level 25: irrigated_temperate_soybean \n" \
        S3/landCoverFrac/CLM5.0_S3_landCoverFrac.nc       
ncatted -O -a comment,global,a,c,"Level 26: barley (empty) \n" \
        S3/landCoverFrac/CLM5.0_S3_landCoverFrac.nc
ncatted -O -a comment,global,a,c,"Level 27: irrigated_barley (empty) \n" \
        S3/landCoverFrac/CLM5.0_S3_landCoverFrac.nc 
ncatted -O -a comment,global,a,c,"Level 28: winter_barley (empty) \n" \
        S3/landCoverFrac/CLM5.0_S3_landCoverFrac.nc
ncatted -O -a comment,global,a,c,"Level 29: irrigated_winter_barley (empty) \n" \
        S3/landCoverFrac/CLM5.0_S3_landCoverFrac.nc                
ncatted -O -a comment,global,a,c,"Level 30: rye (empty) \n" \
        S3/landCoverFrac/CLM5.0_S3_landCoverFrac.nc
ncatted -O -a comment,global,a,c,"Level 31: irrigated_rye (empty) \n" \
        S3/landCoverFrac/CLM5.0_S3_landCoverFrac.nc
ncatted -O -a comment,global,a,c,"Level 32: winter_rye (empty) \n" \
        S3/landCoverFrac/CLM5.0_S3_landCoverFrac.nc 
ncatted -O -a comment,global,a,c,"Level 33: irrigated_winter_rye (empty) \n" \
        S3/landCoverFrac/CLM5.0_S3_landCoverFrac.nc
ncatted -O -a comment,global,a,c,"Level 34: cassava (empty) \n" \
        S3/landCoverFrac/CLM5.0_S3_landCoverFrac.nc
ncatted -O -a comment,global,a,c,"Level 35: irrigated_cassava (empty) \n" \
        S3/landCoverFrac/CLM5.0_S3_landCoverFrac.nc       
ncatted -O -a comment,global,a,c,"Level 36: citrus (empty) \n" \
        S3/landCoverFrac/CLM5.0_S3_landCoverFrac.nc
ncatted -O -a comment,global,a,c,"Level 37: irrigated_citrus (empty) \n" \
        S3/landCoverFrac/CLM5.0_S3_landCoverFrac.nc 
ncatted -O -a comment,global,a,c,"Level 38: cocoa (empty) \n" \
        S3/landCoverFrac/CLM5.0_S3_landCoverFrac.nc
ncatted -O -a comment,global,a,c,"Level 39: irrigated_cocoa (empty) \n" \
        S3/landCoverFrac/CLM5.0_S3_landCoverFrac.nc
ncatted -O -a comment,global,a,c,"Level 40: coffee (empty) \n" \
        S3/landCoverFrac/CLM5.0_S3_landCoverFrac.nc
ncatted -O -a comment,global,a,c,"Level 41: irrigated_coffee (empty) \n" \
        S3/landCoverFrac/CLM5.0_S3_landCoverFrac.nc
ncatted -O -a comment,global,a,c,"Level 42: cotton \n" \
        S3/landCoverFrac/CLM5.0_S3_landCoverFrac.nc 
ncatted -O -a comment,global,a,c,"Level 43: irrigated_cotton \n" \
        S3/landCoverFrac/CLM5.0_S3_landCoverFrac.nc
ncatted -O -a comment,global,a,c,"Level 44: datepalm (empty) \n" \
        S3/landCoverFrac/CLM5.0_S3_landCoverFrac.nc
ncatted -O -a comment,global,a,c,"Level 45: irrigated_datepalm (empty) \n" \
        S3/landCoverFrac/CLM5.0_S3_landCoverFrac.nc       
ncatted -O -a comment,global,a,c,"Level 46: foddergrass (empty) \n" \
        S3/landCoverFrac/CLM5.0_S3_landCoverFrac.nc
ncatted -O -a comment,global,a,c,"Level 47: irrigated_foddergrass (empty) \n" \
        S3/landCoverFrac/CLM5.0_S3_landCoverFrac.nc 
ncatted -O -a comment,global,a,c,"Level 48: grapes (empty) \n" \
        S3/landCoverFrac/CLM5.0_S3_landCoverFrac.nc
ncatted -O -a comment,global,a,c,"Level 49: irrigated_grapes (empty) \n" \
        S3/landCoverFrac/CLM5.0_S3_landCoverFrac.nc
ncatted -O -a comment,global,a,c,"Level 50: groundnuts (empty) \n" \
        S3/landCoverFrac/CLM5.0_S3_landCoverFrac.nc
ncatted -O -a comment,global,a,c,"Level 51: irrigated_groundnuts (empty) \n" \
        S3/landCoverFrac/CLM5.0_S3_landCoverFrac.nc
ncatted -O -a comment,global,a,c,"Level 52: millet (empty) \n" \
        S3/landCoverFrac/CLM5.0_S3_landCoverFrac.nc 
ncatted -O -a comment,global,a,c,"Level 53: irrigated_millet (empty) \n" \
        S3/landCoverFrac/CLM5.0_S3_landCoverFrac.nc
ncatted -O -a comment,global,a,c,"Level 54: oilpalm (empty) \n" \
        S3/landCoverFrac/CLM5.0_S3_landCoverFrac.nc
ncatted -O -a comment,global,a,c,"Level 55: irrigated_oilpalm (empty) \n" \
        S3/landCoverFrac/CLM5.0_S3_landCoverFrac.nc       
ncatted -O -a comment,global,a,c,"Level 56: potatoes (empty) \n" \
        S3/landCoverFrac/CLM5.0_S3_landCoverFrac.nc
ncatted -O -a comment,global,a,c,"Level 57: irrigated_potatoes (empty) \n" \
        S3/landCoverFrac/CLM5.0_S3_landCoverFrac.nc 
ncatted -O -a comment,global,a,c,"Level 58: pulses (empty) \n" \
        S3/landCoverFrac/CLM5.0_S3_landCoverFrac.nc
ncatted -O -a comment,global,a,c,"Level 59: irrigated_pulses (empty) \n" \
        S3/landCoverFrac/CLM5.0_S3_landCoverFrac.nc
ncatted -O -a comment,global,a,c,"Level 60: rapeseed (empty) \n" \
        S3/landCoverFrac/CLM5.0_S3_landCoverFrac.nc
ncatted -O -a comment,global,a,c,"Level 61: irrigated_rapeseed (empty) \n" \
        S3/landCoverFrac/CLM5.0_S3_landCoverFrac.nc
ncatted -O -a comment,global,a,c,"Level 62: rice \n" \
        S3/landCoverFrac/CLM5.0_S3_landCoverFrac.nc 
ncatted -O -a comment,global,a,c,"Level 63: irrigated_rice \n" \
        S3/landCoverFrac/CLM5.0_S3_landCoverFrac.nc
ncatted -O -a comment,global,a,c,"Level 64: sorghum (empty) \n" \
        S3/landCoverFrac/CLM5.0_S3_landCoverFrac.nc
ncatted -O -a comment,global,a,c,"Level 65: irrigated_sorghum (empty) \n" \
        S3/landCoverFrac/CLM5.0_S3_landCoverFrac.nc       
ncatted -O -a comment,global,a,c,"Level 66: sugarbeet (empty) \n" \
        S3/landCoverFrac/CLM5.0_S3_landCoverFrac.nc
ncatted -O -a comment,global,a,c,"Level 67: irrigated_sugarbeet (empty) \n" \
        S3/landCoverFrac/CLM5.0_S3_landCoverFrac.nc 
ncatted -O -a comment,global,a,c,"Level 68: sugarcane \n" \
        S3/landCoverFrac/CLM5.0_S3_landCoverFrac.nc
ncatted -O -a comment,global,a,c,"Level 69: irrigated_sugarcane \n" \
        S3/landCoverFrac/CLM5.0_S3_landCoverFrac.nc
ncatted -O -a comment,global,a,c,"Level 70: sunflower (empty) \n" \
        S3/landCoverFrac/CLM5.0_S3_landCoverFrac.nc
ncatted -O -a comment,global,a,c,"Level 71: irrigated_sunflower (empty) \n" \
        S3/landCoverFrac/CLM5.0_S3_landCoverFrac.nc
ncatted -O -a comment,global,a,c,"Level 72: miscanthus (empty) \n" \
        S3/landCoverFrac/CLM5.0_S3_landCoverFrac.nc 
ncatted -O -a comment,global,a,c,"Level 73: irrigated_miscanthus (empty) \n" \
        S3/landCoverFrac/CLM5.0_S3_landCoverFrac.nc
ncatted -O -a comment,global,a,c,"Level 74: switchgrass (empty) \n" \
        S3/landCoverFrac/CLM5.0_S3_landCoverFrac.nc
ncatted -O -a comment,global,a,c,"Level 75: irrigated_switchgrass (empty) \n" \
        S3/landCoverFrac/CLM5.0_S3_landCoverFrac.nc       
ncatted -O -a comment,global,a,c,"Level 76: tropical_corn \n" \
        S3/landCoverFrac/CLM5.0_S3_landCoverFrac.nc
ncatted -O -a comment,global,a,c,"Level 77: irrigated_tropical_corn \n" \
        S3/landCoverFrac/CLM5.0_S3_landCoverFrac.nc 
ncatted -O -a comment,global,a,c,"Level 78: tropical_soybean \n" \
        S3/landCoverFrac/CLM5.0_S3_landCoverFrac.nc
ncatted -O -a comment,global,a,c,"Level 79: irrigated_tropical_soybean" \
        S3/landCoverFrac/CLM5.0_S3_landCoverFrac.nc

rm S3/landCoverFrac/test.nc
rm S3/landCoverFrac/test1.nc
