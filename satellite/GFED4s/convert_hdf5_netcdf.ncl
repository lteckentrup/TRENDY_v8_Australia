*****************************************************************
; gfed_3.ncl
;
; Concepts illustrated:
;   - Creating function to perform specific tasks
;     Create a 'group' path; access data; rearrange data; add meyta data
;   - Getting all file names
;   - Looping over files
;   - Extracting specific variables from nested hdf5 groups
;   - Creating CF conforming netCDF
;
;******************************************************************
; GFED: Global Fire Emmisions Database
; Convert hdf5 with embedded 'groups' to CF conformant netCDF-4
; Make the variables conform to the same ordering of CESM spatial coordinates
; This latter step is not necessary. It facilitates CESM post processing.
;******************************************************************
;
undef("addMeta")
procedure addMeta(x:numeric, time[*]:numeric, lat[*]:numeric, lon[*]:numeric)
;
; [1] add meta data
; [2] For consistency with CESM:
;     (a) make South-to-North ordering
;     (b) make array start at GM: all positive longitudes
; Options 2a and 2b can be commented if they are not desired
;
local dimx, rankx, xx
begin
     dimx   = dimsizes(x)
     rankx  = dimsizes(dimx)
            ; only 2D or 3D
     if (.not.(rankx.eq.2 .or. rankx.eq.3)) then
         print("addMeta: rankx="+rankx+" not supported")
         print(dimx)
         exit
     end if

     if (rankx.eq.2) then
         x!0   = "lat"
         x!1   = "lon"
         x&lat = lat
         x&lon = lon
         x = x(::-1,:)        ;make S->N
     else
         x!0   = "time"
         x!1   = "lat"
         x!2   = "lon"

         x&time= time
         x&lat = lat
         x&lon = lon
         x   = x(:,::-1,:)    ;make S->N
     end if
                         ;for consistency with CESM order
     x = lonFlip(x)      ;make start at/near Grenwich Meridion
end

;---

undef("get_gefd_var")
function get_gefd_var(f:file, grp_name[*]:string, var_name[1]:string  \
                     ,time[*], lat[*], lon[*]     )
;
;---Create an appropriate group path
;---Loop over the 12 monthly groups and, where appropriate sub-groups
;---Create and 'fill' array with appropriate values
;---Add meta data
;
local nlat, mlon, ngrp, nmo, nmos, varType, grp_month, pth_name, x
begin
  nmos = 12
  nlat = dimsizes(lat)
  mlon = dimsizes(lon)
            ; explicitly create  month 'groups' with 0-filled values
  grp_month = sprinti("%0.2i",ispan(1,nmos,1))   ; "01", "02",..., "12"

  ngrp = dimsizes(grp_name)
  if (ngrp.eq.1) then
      pth_name = "/"+grp_name+"/"+grp_month+"/"+var_name
  else
      pth_name = "/"+grp_name(0)+"/"+grp_month+"/"+grp_name(1)+"/"+var_name
  end if

  varType = getfilevartypes(f, pth_name)
  x       = new ( (/nmos,nlat,mlon/), varType, "No_FillValue")
  do nmo=1,nmos
     x(nmo-1,:,:)   = f->$pth_name(nmo-1)$
  end do

; procedure to add appropriate meta data to each variable
  addMeta(x , time, lat, lon)
  return(x)
end

;**********************************************************
;                           MAIN
;***********************************************************
;---Avoid printing Warning messages
    err = NhlGetErrorObjectId()
    setvalues err
      "errLevel" : "Fatal"          ; only report Fatal errors
    end setvalues

;---netCDF
    netCDF = True                   ; =True  create netCDF-4
                                    ; =False print only; no file creation
    dirnc  = "./netCDF/"               ; any directory

;---read names of source files which are GFED.1s_*.hdf5
    diri   = "./hdf5/"        ; directory with source hdf5 files

    all_files = systemfunc ("cd "+diri+" ; ls GFED4.1s_*hdf5")
    print(all_files)
    pthi   = diri+all_files     ;create file path
    print(pthi)

    nfil   = dimsizes(pthi)
    print("nfil="+nfil)

;---loop over each year file. The year is in the file name.
;---There is no time internal to the file.

  do nf=0,nfil-1
     print("File loop: "+all_files(nf))

;---extract time with "_" and "." delimiters ; convert string to integer

    year = toint(str_get_field(all_files(nf),3,"_."))

;---create a CF conforming time coordinate (technically: 1997 is 'arbitrary')

    units  = "hours since 1997-01-01 00:00:00" ; "seconds/hours/days since ...."
                                               ;  do NOT use "months since ...."
    mm     = ispan(1,12,1)
    yyyymm = year*100+mm
    yyyy   = yyyymm/100
    dd     = conform(yyyymm,   1, -1)
    hh     = conform(yyyymm,   0, -1)
    mn     = conform(yyyymm,   0, -1)
    sc     = conform(yyyymm,   0, -1)
    time   = cd_inv_calendar(yyyy,mm,dd,hh,mn,sc,units, 0)
    time@info   = "time corresponds to the 1st day of current month"
    time!0      = "time"
    time&time   =  time
   ;print(time)

    yyyymm!0    = "time"
    yyyymm&time =  time              ; associate 'time' with 'yyyymm'
    yyyymm@long_name = "current year and month: YYYYMM"
   ;print(yyyymm)

;---import data from current hdf5 file
    f = addfile(pthi(nf),"r")        ; open file
   ;print(f)                         ; file overview

    if (nf.eq.0) then                ; time invariant information
        LAT     = f->lat             ; (:,:) .... replicated
        LON     = f->lon             ; (:,:)
                                     ; create 'coordinate variables'
        lat     = (/LAT(:,0)/)
        lon     = (/LON(0,:)/)
        lat@units = LAT@units
        lon@units = LON@units
        lat!0   = "lat"
        lon!0   = "lon"
        lat&lat =  lat
        lon&lon =  lon
                                     ; sizes
        nlat    = dimsizes(lat)
        mlon    = dimsizes(lon)
                                     ; invariant variables: 'ancill' group: add meta data
        basis_regions = f->/ancill/basis_regions
        addMeta(basis_regions, time, lat, lon)
        printVarSummary(basis_regions)       ; [lat | 720] x [lon | 1440]

        grid_cell_area = f->/ancill/grid_cell_area
        addMeta(grid_cell_area, time, lat, lon)
        printVarSummary(grid_cell_area)      ; [lat | 720] x [lon | 1440]

        delete([/ LAT,LON /])
    end if   ; nf=0   =1

;---Desired variables

    bf  = get_gefd_var(f, "burned_area", "burned_fraction", time, lat,lon)
    src = get_gefd_var(f, "burned_area", "source", time, lat,lon)
    c   = get_gefd_var(f, "emissions"  , "C"     , time, lat,lon)
    dm  = get_gefd_var(f, "emissions"  , "DM"    , time, lat,lon)
    smf = get_gefd_var(f, "emissions"  , "small_fire_fraction"    , time, lat,lon)
    bb  = get_gefd_var(f, "biosphere"  , "BB"    , time, lat,lon)
    npp = get_gefd_var(f, "biosphere"  , "NPP"   , time, lat,lon)
    rh  = get_gefd_var(f, "biosphere"  , "Rh"    , time, lat,lon)

    cagri = get_gefd_var(f, (/"emissions","partitioning"/) \
                             ,"C_AGRI", time, lat,lon)
    cborf = get_gefd_var(f, (/"emissions","partitioning"/) \
                             ,"C_BORF", time, lat,lon)
    cdefo = get_gefd_var(f, (/"emissions","partitioning"/) \
                             ,"C_DEFO", time, lat,lon)
    cpeat = get_gefd_var(f, (/"emissions","partitioning"/) \
                             ,"C_PEAT", time, lat,lon)
    csava = get_gefd_var(f, (/"emissions","partitioning"/) \
                             ,"C_SAVA", time, lat,lon)
    dmagri= get_gefd_var(f, (/"emissions","partitioning"/) \
                             ,"DM_AGRI", time, lat,lon)
    dmborf= get_gefd_var(f, (/"emissions","partitioning"/) \
                             ,"DM_BORF", time, lat,lon)
    dmdefo= get_gefd_var(f, (/"emissions","partitioning"/) \
                             ,"DM_DEFO", time, lat,lon)

;---Information: only for 1st file (nf=0; year)
    if (nf.eq.0) then
        printVarSummary(bf)     ;[time | 12] x [lat | 720] x [lon | 1440]
        printMinMax(bf,1)

        printVarSummary(src)    ;[time | 12] x [lat | 720] x [lon | 1440]
        printMinMax(src,1)

        printVarSummary(smf)    ;[time | 12] x [lat | 720] x [lon | 1440]
        printMinMax(smf,1)

        printVarSummary(rh)    ;[time | 12] x [lat | 720] x [lon | 1440]
        printMinMax(rh,1)

        printVarSummary(cagri) ;[time | 12] x [lat | 720] x [lon | 1440]
        printMinMax(cagri,1)
    end if

;---netCDF
  if (netCDF) then

;---remove any preexisting file
     filnc = "GFED4.1s_"+year+".nc"
     pthnc = dirnc+filnc
     system("/bin/rm -f "+pthnc)     ;remove any pre-existing file

;---open file, set file for nc4 [standard compression]
     setfileoption("nc", "Format", "NetCDF4")
     ncdf = addfile(pthnc,"c")       ;open output netCDF file

;---create global attributes of the file
     fAtt               = True
     fAtt@title         = "GFED: Global Fire Emissions DataBase"
     fAtt@GFED_WWW      = "http://www.globalfiredata.org/"
     fAtt@Conventions   = "CF-1.0"
     fAtt@NCL           = get_ncl_version()
     fAtt@creation_date = systemfunc ("date")

     fileattdef(ncdf, fAtt)                    ;copy file attributes

;---make time an 'UNLIMITED' dimension [NCO operators]
     filedimdef(ncdf,"time",-1,True)

     ncdf->yyyymm          = yyyymm            ; auxiliary 'time' variable

                                               ; 2D static variables
     ncdf->BASIS_REGIONS   = basis_regions     ; (lat,lon)
     ncdf->GRID_CELL_AREA  = grid_cell_area    ;     "

                                               ; 3D variables
     ncdf->BURNED_FRACTION = bf                ; (time,lat,lon)
     ncdf->SOURCE          = src               ;     "
     ncdf->C               = c               ;     "
     ncdf->DM              = dm
     ncdf->SMALL_FIRE_FRACTION = smf
     ncdf->BB              = bb
     ncdf->NPP             = npp
     ncdf->RH              = rh

     ncdf->C_AGRI          = cagri
     ncdf->C_BORF          = cborf
     ncdf->C_DEFO          = cdefo
     ncdf->C_PEAT          = cpeat
     ncdf->C_SAVA          = csava
     ncdf->DM_AGRI         = dmagri
     ncdf->DM_BORF         = dmborf
     ncdf->DM_DEFO         = dmdefo

  end if  ; netCDF

end do    ; file
