cdo -L -sellonlatbox,112.25,153.75,-43.75,-10.25 -timmean -selyear,2001/2018 \
    -remapycon,../fine_grid.txt -invertlat -vertsum -sellevel,1,2,3,4 \
    ../../S3/landCoverFrac/CABLE-POP_S3_landCoverFrac.nc CABLE-POP_S3_Tree.nc

cdo -L -setvrange,0,1000 -sellonlatbox,56.25,98.75,-43.75,-10.25 \
    -remapycon,../fine_grid.txt -timmean  -selyear,2001/2018 -vertsum \
    -sellevel,2/9 ../../S3/landCoverFrac/CLM5.0_S3_landCoverFrac.nc \
    CLM5.0_S3_Tree.nc

cdo -L -sellonlatbox,112.25,153.75,-43.75,-10.25 -vertsum \
    -sellevel,1,2,3,4,5,14,15,16,17,18,20,24 -timmean -selyear,2001/2018 \
    ../../S3/landCoverFrac/ISAM_S3_landCoverFrac.nc ISAM_S3_Tree.nc

cdo -b F64 -L -sellonlatbox,112.25,153.75,-43.75,-10.25 \
    -remapycon,../fine_grid.txt -selyear,2001/2018 -vertsum \
    -sellevel,4,5,6,13,14,15,16,17 \
    ../../S3/landCoverFrac/ISBA-CTRIP_S3_landCoverFrac.nc \
    ISBA-CTRIP_S3_Tree.nc

cdo -L -sellonlatbox,112.25,153.75,-43.75,-10.25 -remapycon,../fine_grid.txt \
    -invertlat -vertsum -sellevel,2/9 -timmean -selyear,2001/2018 \
    ../../S3/landCoverFrac/OCN_S3_landCoverFrac.nc OCN_S3_Tree.nc

cdo -L -sellonlatbox,112.25,153.75,-43.75,-10.25 -remapycon,../fine_grid.txt \
    -invertlat -vertsum -sellevel,2/9 -timmean -selyear,2001/2018 \
    ../../S3/landCoverFrac/ORCHIDEE-CNP_S3_landCoverFrac.nc \
    ORCHIDEE-CNP_S3_Tree.nc

cdo -L -sellonlatbox,112.25,153.75,43.75,10.25 -remapycon,../fine_grid.txt \
    -invertlat -vertsum -sellevel,2/9 -timmean -selyear,2001/2018 \
    ../../S3/landCoverFrac/ORCHIDEE_S3_landCoverFrac.nc ORCHIDEE_S3_Tree.nc

cdo -L -sellonlatbox,112.25,153.75,-43.75,-10.25 -remapycon,../fine_grid.txt \
    -invertlat -vertsum -sellevel,7,8,9,10 -timmean -selyear,2001/2018 \
    ../../../TRENDY_v9/S3/landCoverFrac/SDGVM_S3_landCoverFrac.nc \
    SDGVM_S3_Tree.nc

cdo -L -sellonlatbox,112.25,153.75,-43.75,-10.25 -invertlat -vertsum \
    -sellevel,1/8 ../../S3/landCoverFrac/VISIT_S3_landCoverFrac.nc \
    VISIT_S3_Tree.nc

module unload cdo
module load cdo/1.6.1

cdo -L -sellonlatbox,112.25,153.75,-43.75,-10.25 -remapcon,../fine_grid.txt \
    -vertsum -sellevel,1/5 -timmean -selyear,2001/2018 \
    ../../S3/landCoverFrac/CLASS-CTEM_S3_landCoverFrac.nc \
    CLASS-CTEM_S3_Tree.nc

cdo -L -sellonlatbox,112.25,153.75,-43.75,-10.25 -remapcon,../fine_grid.txt \
    -timmean -selyear,2001/2018 -vertsum -sellevel,3,4,5,6 \
    ../../S3/landCoverFrac/JSBACH_S3_landCoverFrac.nc JSBACH_S3_Tree.nc

cdo -L -setvrange,0,1000 -vertsum -sellevel,0/4 \
    -sellonlatbox,112.25,153.75,-43.75,-10.25 -remapcon,../fine_grid.txt \
    -timmean -selyear,2001/2018 \
    ../../S3/landCoverFrac/JULES-ES_S3_landCoverFrac.nc JULES-ES_S3_Tree.nc

module unload cdo
module load cdo

cdo -chname,sum,landCoverFrac -timmean \
    -expr,'sum=TrBE+TrBR+TeNE+TeBE+TeBS+BNE+BNS+BBS+PeatTrBE+PeatTrBR;' \
    ../NonTree/LPX-Bern_S3_landCoverFrac.nc LPX-Bern_S3_Tree.nc
