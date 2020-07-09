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

        gunzip $exp'/'$var'/'VISIT_$exp'_'$var'.'nc.gz
    done
done

for exp in S0 S1 S2 S3 S4; do
    for var in nbp gpp ra rh fFire evapotrans cVeg; do
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
