### calculate terrestrial ecocystem respiration (TER) and net ecosystem exchange (NEE)
for model in CABLE-POP CLASS-CTEM CLM5.0 DLEM ISAM ISBA-CTRIP JSBACH JULES-ES LPX-Bern_S0 OCN ORCHIDEE-CNP ORCHIDEE SDGVM VISIT; do
    for exp in S0 S1 S2 S3 S4; do
        cdo -L -chname,ra,ter -add $exp'/'ra/$model'_'$exp'_'ra.nc \
            $exp'/'rh/$model'_'$exp'_'rh.nc $exp'/'ter/$model'_'$exp'_'ter.nc
        cdo -L -chname,ter,nee -sub $exp'/'ter/$model'_'$exp'_'ter.nc \
            $exp'/'gpp/$model'_'$exp'_'gpp.nc $exp'/'nee/$model'_'$exp'_'nee.nc
    done
done 
