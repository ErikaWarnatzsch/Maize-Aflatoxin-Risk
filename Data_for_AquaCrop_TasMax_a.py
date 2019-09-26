"""
Created on Tuesday 9 July 2019

@author: s0899345
"""

import matplotlib.pyplot as plt
import iris
import iris.coord_categorisation as iriscc
import iris.plot as iplt
import iris.analysis.cartography
import numpy as np
import calendar
import cf_units
from cf_units import Unit

#this file is split into parts as follows:
    #PART 1: Load and Format all Past Models
    #PART 2: Load and Format all Future Models
    #PART 3: Load and Format Observed Data
    #PART 4: Format Data General
    #PART 5: Format Data to be Geographically Specific and Re-Baseline
    #PART 6: print data
    
    
def main():
    #promote iris.FUTURE to true to fix cube
    iris.FUTURE.netcdf_promote = True
    
    #-------------------------------------------------------------------------
    #PART 1: LOAD and FORMAT ALL PAST MODELS   
    CCCmaCanRCM_past = '/exports/csce/datastore/geos/users/s0899345/AFR_44_tasmax/Historical_daily/tasmax_AFR-44_CCCma-CanESM2_historical_r1i1p1_CCCma-CanRCM4_r2_day_19710101-20001231.nc'
    CCCmaSMHI_past = '/exports/csce/datastore/geos/users/s0899345/AFR_44_tasmax/Historical_daily/tasmax_AFR-44_CCCma-CanESM2_historical_r1i1p1_SMHI-RCA4_v1_day_19710101-20001231.nc'   
    CNRM_past = '/exports/csce/datastore/geos/users/s0899345/AFR_44_tasmax/Historical_daily/tasmax_AFR-44_CNRM-CERFACS-CNRM-CM5_historical_r1i1p1_CLMcom-CCLM4-8-17_v1_day_19710101-20001231.nc'
    CNRMSMHI_past = '/exports/csce/datastore/geos/users/s0899345/AFR_44_tasmax/Historical_daily/tasmax_AFR-44_CNRM-CERFACS-CNRM-CM5_historical_r1i1p1_SMHI-RCA4_v1_day_19710101-20001231.nc'
    CSIRO_past = '/exports/csce/datastore/geos/users/s0899345/AFR_44_tasmax/Historical_daily/tasmax_AFR-44_CSIRO-QCCCE-CSIRO-Mk3-6-0_historical_r1i1p1_SMHI-RCA4_v1_day_19710101-20001231.nc'
    ICHECDMI_past = '/exports/csce/datastore/geos/users/s0899345/AFR_44_tasmax/Historical_daily/tasmax_AFR-44_ICHEC-EC-EARTH_historical_r3i1p1_DMI-HIRHAM5_v2_day_19710101-20001231.nc'   
    ICHECCCLM_past = '/exports/csce/datastore/geos/users/s0899345/AFR_44_tasmax/Historical_daily/tasmax_AFR-44_ICHEC-EC-EARTH_historical_r12i1p1_CLMcom-CCLM4-8-17_v1_day_19710101-20001231.nc'    
    ICHECKNMI_past = '/exports/csce/datastore/geos/users/s0899345/AFR_44_tasmax/Historical_daily/tasmax_AFR-44_ICHEC-EC-EARTH_historical_r1i1p1_KNMI-RACMO22T_v1_day_19710101-20001231.nc'
    ICHECMPI_past = '/exports/csce/datastore/geos/users/s0899345/AFR_44_tasmax/Historical_daily/tasmax_AFR-44_ICHEC-EC-EARTH_historical_r12i1p1_MPI-CSC-REMO2009_v1_day_19710101-20001231.nc'
    ICHECSMHI_past = '/exports/csce/datastore/geos/users/s0899345/AFR_44_tasmax/Historical_daily/tasmax_AFR-44_ICHEC-EC-EARTH_historical_r12i1p1_SMHI-RCA4_v1_day_19710101-20001231.nc'
    
    #Load exactly one cube from given file
    CCCmaCanRCM_past =  iris.load_cube(CCCmaCanRCM_past)
    CCCmaSMHI_past =  iris.load_cube(CCCmaSMHI_past)
    CNRM_past =  iris.load_cube(CNRM_past)
    CNRMSMHI_past =  iris.load_cube(CNRMSMHI_past)
    CSIRO_past =  iris.load_cube(CSIRO_past)
    ICHECDMI_past =  iris.load_cube(ICHECDMI_past, 'air_temperature')
    ICHECCCLM_past =  iris.load_cube(ICHECCCLM_past)
    ICHECKNMI_past =  iris.load_cube(ICHECKNMI_past)
    ICHECMPI_past =  iris.load_cube(ICHECMPI_past)
    ICHECSMHI_past =  iris.load_cube(ICHECSMHI_past)
    
    #remove flat latitude and longitude and only use grid latitude and grid longitude to make consistent with the observed data, also make sure all of the longitudes are monotonic. 
    lats = iris.coords.DimCoord(CCCmaCanRCM_past.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = CCCmaCanRCM_past.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees')
                              
    CCCmaCanRCM_past.remove_coord('latitude')
    CCCmaCanRCM_past.remove_coord('longitude')
    CCCmaCanRCM_past.remove_coord('grid_latitude')
    CCCmaCanRCM_past.remove_coord('grid_longitude')
    CCCmaCanRCM_past.add_dim_coord(lats, 1)
    CCCmaCanRCM_past.add_dim_coord(lons, 2)
    
    lats = iris.coords.DimCoord(CCCmaSMHI_past.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = CCCmaSMHI_past.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees')
    
    CCCmaSMHI_past.remove_coord('latitude')
    CCCmaSMHI_past.remove_coord('longitude')
    CCCmaSMHI_past.remove_coord('grid_latitude')
    CCCmaSMHI_past.remove_coord('grid_longitude')
    CCCmaSMHI_past.add_dim_coord(lats, 1)
    CCCmaSMHI_past.add_dim_coord(lons, 2)  
    
    lats = iris.coords.DimCoord(CNRM_past.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = CNRM_past.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees')
                                
    CNRM_past.remove_coord('latitude')
    CNRM_past.remove_coord('longitude')
    CNRM_past.remove_coord('grid_latitude')
    CNRM_past.remove_coord('grid_longitude')
    CNRM_past.add_dim_coord(lats, 1)
    CNRM_past.add_dim_coord(lons, 2) 
    
    lats = iris.coords.DimCoord(CNRMSMHI_past.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = CNRMSMHI_past.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees')
    
    CNRMSMHI_past.remove_coord('latitude')
    CNRMSMHI_past.remove_coord('longitude')
    CNRMSMHI_past.remove_coord('grid_latitude')
    CNRMSMHI_past.remove_coord('grid_longitude')
    CNRMSMHI_past.add_dim_coord(lats, 1)
    CNRMSMHI_past.add_dim_coord(lons, 2) 
    
    lats = iris.coords.DimCoord(CSIRO_past.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = CSIRO_past.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees')
    
    CSIRO_past.remove_coord('latitude')
    CSIRO_past.remove_coord('longitude')
    CSIRO_past.remove_coord('grid_latitude')
    CSIRO_past.remove_coord('grid_longitude')
    CSIRO_past.add_dim_coord(lats, 1)
    CSIRO_past.add_dim_coord(lons, 2) 
    
    lats = iris.coords.DimCoord(ICHECDMI_past.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = ICHECDMI_past.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees')    
    
    ICHECDMI_past.remove_coord('latitude')
    ICHECDMI_past.remove_coord('longitude')
    ICHECDMI_past.remove_coord('grid_latitude')
    ICHECDMI_past.remove_coord('grid_longitude')
    ICHECDMI_past.add_dim_coord(lats, 1)
    ICHECDMI_past.add_dim_coord(lons, 2)
    
    lats = iris.coords.DimCoord(ICHECCCLM_past.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = ICHECCCLM_past.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees') 
    
    ICHECCCLM_past.remove_coord('latitude')
    ICHECCCLM_past.remove_coord('longitude')
    ICHECCCLM_past.remove_coord('grid_latitude')
    ICHECCCLM_past.remove_coord('grid_longitude')
    ICHECCCLM_past.add_dim_coord(lats, 1)
    ICHECCCLM_past.add_dim_coord(lons, 2)
    
    lats = iris.coords.DimCoord(ICHECKNMI_past.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = ICHECKNMI_past.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees') 
    
    ICHECKNMI_past.remove_coord('latitude')
    ICHECKNMI_past.remove_coord('longitude')
    ICHECKNMI_past.remove_coord('grid_latitude')
    ICHECKNMI_past.remove_coord('grid_longitude')
    ICHECKNMI_past.add_dim_coord(lats, 1)
    ICHECKNMI_past.add_dim_coord(lons, 2)
    
    lats = iris.coords.DimCoord(ICHECMPI_past.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = ICHECMPI_past.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees') 
    
    ICHECMPI_past.remove_coord('latitude')
    ICHECMPI_past.remove_coord('longitude')
    ICHECMPI_past.remove_coord('grid_latitude')
    ICHECMPI_past.remove_coord('grid_longitude')
    ICHECMPI_past.add_dim_coord(lats, 1)
    ICHECMPI_past.add_dim_coord(lons, 2)
    
    lats = iris.coords.DimCoord(ICHECSMHI_past.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = ICHECSMHI_past.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees')
    
    ICHECSMHI_past.remove_coord('latitude')
    ICHECSMHI_past.remove_coord('longitude')
    ICHECSMHI_past.remove_coord('grid_latitude')
    ICHECSMHI_past.remove_coord('grid_longitude')
    ICHECSMHI_past.add_dim_coord(lats, 1)
    ICHECSMHI_past.add_dim_coord(lons, 2)
    
    #guess bounds    
    CCCmaCanRCM_past.coord('latitude').guess_bounds()
    CCCmaSMHI_past.coord('latitude').guess_bounds()
    CNRM_past.coord('latitude').guess_bounds()
    CNRMSMHI_past.coord('latitude').guess_bounds()
    CSIRO_past.coord('latitude').guess_bounds()
    ICHECDMI_past.coord('latitude').guess_bounds()
    ICHECCCLM_past.coord('latitude').guess_bounds()
    ICHECKNMI_past.coord('latitude').guess_bounds()
    ICHECMPI_past.coord('latitude').guess_bounds()
    ICHECSMHI_past.coord('latitude').guess_bounds()
    
    CCCmaCanRCM_past.coord('longitude').guess_bounds()
    CCCmaSMHI_past.coord('longitude').guess_bounds()
    CNRM_past.coord('longitude').guess_bounds()
    CNRMSMHI_past.coord('longitude').guess_bounds()
    CSIRO_past.coord('longitude').guess_bounds()
    ICHECDMI_past.coord('longitude').guess_bounds()
    ICHECCCLM_past.coord('longitude').guess_bounds()
    ICHECKNMI_past.coord('longitude').guess_bounds()
    ICHECMPI_past.coord('longitude').guess_bounds()
    ICHECSMHI_past.coord('longitude').guess_bounds()
    
    
    #-------------------------------------------------------------------------
    #PART 2: LOAD and FORMAT PROJECTED MODELS   
    CCCmaCanRCM= '/exports/csce/datastore/geos/users/s0899345/AFR_44_tasmax/4.5/tasmax_AFR-44_CCCma-CanESM2_rcp45_r1i1p1_CCCma-CanRCM4_r2_day_20060101-20701231.nc'
    CCCmaSMHI= '/exports/csce/datastore/geos/users/s0899345/AFR_44_tasmax/4.5/tasmax_AFR-44_CCCma-CanESM2_rcp45_r1i1p1_SMHI-RCA4_v1_day_20060101-20701231.nc'   
    CNRM= '/exports/csce/datastore/geos/users/s0899345/AFR_44_tasmax/4.5/tasmax_AFR-44_CNRM-CERFACS-CNRM-CM5_rcp45_r1i1p1_CLMcom-CCLM4-8-17_v1_day_20060101-20701231.nc'
    CNRMSMHI= '/exports/csce/datastore/geos/users/s0899345/AFR_44_tasmax/4.5/tasmax_AFR-44_CNRM-CERFACS-CNRM-CM5_rcp45_r1i1p1_SMHI-RCA4_v1_day_20060101-20701231.nc'
    CSIRO = '/exports/csce/datastore/geos/users/s0899345/AFR_44_tasmax/4.5/tasmax_AFR-44_CSIRO-QCCCE-CSIRO-Mk3-6-0_rcp45_r1i1p1_SMHI-RCA4_v1_day_20060101-20701231.nc'
    ICHECDMI = '/exports/csce/datastore/geos/users/s0899345/AFR_44_tasmax/4.5/tasmax_AFR-44_ICHEC-EC-EARTH_rcp45_r3i1p1_DMI-HIRHAM5_v2_day_20060101-20701231.nc'   
    ICHECCCLM = '/exports/csce/datastore/geos/users/s0899345/AFR_44_tasmax/4.5/tasmax_AFR-44_ICHEC-EC-EARTH_rcp45_r12i1p1_CLMcom-CCLM4-8-17_v1_day_20060101-20701231.nc'    
    ICHECKNMI = '/exports/csce/datastore/geos/users/s0899345/AFR_44_tasmax/4.5/tasmax_AFR-44_ICHEC-EC-EARTH_rcp45_r1i1p1_KNMI-RACMO22T_v1_day_20060101-20701231.nc'
    ICHECMPI = '/exports/csce/datastore/geos/users/s0899345/AFR_44_tasmax/4.5/tasmax_AFR-44_ICHEC-EC-EARTH_rcp45_r12i1p1_MPI-CSC-REMO2009_v1_day_20060101-20701231.nc'
    ICHECSMHI = '/exports/csce/datastore/geos/users/s0899345/AFR_44_tasmax/4.5/tasmax_AFR-44_ICHEC-EC-EARTH_rcp45_r12i1p1_SMHI-RCA4_v1_day_20060101-20701231.nc'
    
    CCCmaCanRCM85 = '/exports/csce/datastore/geos/users/s0899345/AFR_44_tasmax/8.5/tasmax_AFR-44_CCCma-CanESM2_rcp85_r1i1p1_CCCma-CanRCM4_r2_day_20060101-20701231.nc'
    CCCmaSMHI85 = '/exports/csce/datastore/geos/users/s0899345/AFR_44_tasmax/8.5/tasmax_AFR-44_CCCma-CanESM2_rcp85_r1i1p1_SMHI-RCA4_v1_day_20060101-20701231.nc'   
    CNRM85 = '/exports/csce/datastore/geos/users/s0899345/AFR_44_tasmax/8.5/tasmax_AFR-44_CNRM-CERFACS-CNRM-CM5_rcp85_r1i1p1_CLMcom-CCLM4-8-17_v1_day_20060101-20701231.nc'
    CNRMSMHI85 = '/exports/csce/datastore/geos/users/s0899345/AFR_44_tasmax/8.5/tasmax_AFR-44_CNRM-CERFACS-CNRM-CM5_rcp85_r1i1p1_SMHI-RCA4_v1_day_20060101-20701231.nc'
    CSIRO85 = '/exports/csce/datastore/geos/users/s0899345/AFR_44_tasmax/8.5/tasmax_AFR-44_CSIRO-QCCCE-CSIRO-Mk3-6-0_rcp85_r1i1p1_SMHI-RCA4_v1_day_20060101-20701231.nc'
    ICHECDMI85 = '/exports/csce/datastore/geos/users/s0899345/AFR_44_tasmax/8.5/tasmax_AFR-44_ICHEC-EC-EARTH_rcp85_r3i1p1_DMI-HIRHAM5_v2_day_20060101-20701231.nc'   
    ICHECCCLM85 = '/exports/csce/datastore/geos/users/s0899345/AFR_44_tasmax/8.5/tasmax_AFR-44_ICHEC-EC-EARTH_rcp85_r12i1p1_CLMcom-CCLM4-8-17_v1_day_20060101-20701231.nc'    
    ICHECKNMI85 = '/exports/csce/datastore/geos/users/s0899345/AFR_44_tasmax/8.5/tasmax_AFR-44_ICHEC-EC-EARTH_rcp85_r1i1p1_KNMI-RACMO22T_v1_day_20060101-20701231.nc'
    ICHECMPI85 = '/exports/csce/datastore/geos/users/s0899345/AFR_44_tasmax/8.5/tasmax_AFR-44_ICHEC-EC-EARTH_rcp85_r12i1p1_MPI-CSC-REMO2009_v1_day_20060101-20701231.nc'
    ICHECSMHI85 = '/exports/csce/datastore/geos/users/s0899345/AFR_44_tasmax/8.5/tasmax_AFR-44_ICHEC-EC-EARTH_rcp85_r12i1p1_SMHI-RCA4_v1_day_20060101-20701231.nc'
    
    #Load exactly one cube from given file
    CCCmaCanRCM = iris.load_cube(CCCmaCanRCM)
    CCCmaSMHI = iris.load_cube(CCCmaSMHI)
    CNRM = iris.load_cube(CNRM)
    CNRMSMHI = iris.load_cube(CNRMSMHI)
    CSIRO = iris.load_cube(CSIRO)
    ICHECDMI = iris.load_cube(ICHECDMI, 'air_temperature')
    ICHECCCLM = iris.load_cube(ICHECCCLM)
    ICHECKNMI = iris.load_cube(ICHECKNMI)
    ICHECMPI = iris.load_cube(ICHECMPI)
    ICHECSMHI = iris.load_cube(ICHECSMHI)
    
    CCCmaCanRCM85 = iris.load_cube(CCCmaCanRCM85)
    CCCmaSMHI85 = iris.load_cube(CCCmaSMHI85)
    CNRM85 = iris.load_cube(CNRM85)
    CNRMSMHI85 = iris.load_cube(CNRMSMHI85)
    CSIRO85 = iris.load_cube(CSIRO85)
    ICHECDMI85 = iris.load_cube(ICHECDMI85, 'air_temperature')
    ICHECCCLM85 = iris.load_cube(ICHECCCLM85)
    ICHECKNMI85 = iris.load_cube(ICHECKNMI85)
    ICHECMPI85 = iris.load_cube(ICHECMPI85)
    ICHECSMHI85 = iris.load_cube(ICHECSMHI85)
    
    #remove flat latitude and longitude and only use grid latitude and grid longitude to make consistent with the observed data, also make sure all of the longitudes are monotonic. 
    lats = iris.coords.DimCoord(CCCmaCanRCM.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = CCCmaCanRCM.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees')
                              
    CCCmaCanRCM.remove_coord('latitude')
    CCCmaCanRCM.remove_coord('longitude')
    CCCmaCanRCM.remove_coord('grid_latitude')
    CCCmaCanRCM.remove_coord('grid_longitude')
    CCCmaCanRCM.add_dim_coord(lats, 1)
    CCCmaCanRCM.add_dim_coord(lons, 2)
    
    lats = iris.coords.DimCoord(CCCmaSMHI.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = CCCmaSMHI.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees')
    
    CCCmaSMHI.remove_coord('latitude')
    CCCmaSMHI.remove_coord('longitude')
    CCCmaSMHI.remove_coord('grid_latitude')
    CCCmaSMHI.remove_coord('grid_longitude')
    CCCmaSMHI.add_dim_coord(lats, 1)
    CCCmaSMHI.add_dim_coord(lons, 2)  
    
    lats = iris.coords.DimCoord(CNRM.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = CNRM.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees')
                                
    CNRM.remove_coord('latitude')
    CNRM.remove_coord('longitude')
    CNRM.remove_coord('grid_latitude')
    CNRM.remove_coord('grid_longitude')
    CNRM.add_dim_coord(lats, 1)
    CNRM.add_dim_coord(lons, 2) 
    
    lats = iris.coords.DimCoord(CNRMSMHI.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = CNRMSMHI.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees')
    
    CNRMSMHI.remove_coord('latitude')
    CNRMSMHI.remove_coord('longitude')
    CNRMSMHI.remove_coord('grid_latitude')
    CNRMSMHI.remove_coord('grid_longitude')
    CNRMSMHI.add_dim_coord(lats, 1)
    CNRMSMHI.add_dim_coord(lons, 2) 
    
    lats = iris.coords.DimCoord(CSIRO.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = CSIRO.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees')
    
    CSIRO.remove_coord('latitude')
    CSIRO.remove_coord('longitude')
    CSIRO.remove_coord('grid_latitude')
    CSIRO.remove_coord('grid_longitude')
    CSIRO.add_dim_coord(lats, 1)
    CSIRO.add_dim_coord(lons, 2) 
    
    lats = iris.coords.DimCoord(ICHECDMI.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = ICHECDMI.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees')    
    
    ICHECDMI.remove_coord('latitude')
    ICHECDMI.remove_coord('longitude')
    ICHECDMI.remove_coord('grid_latitude')
    ICHECDMI.remove_coord('grid_longitude')
    ICHECDMI.add_dim_coord(lats, 1)
    ICHECDMI.add_dim_coord(lons, 2)
    
    lats = iris.coords.DimCoord(ICHECCCLM.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = ICHECCCLM.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees') 
    
    ICHECCCLM.remove_coord('latitude')
    ICHECCCLM.remove_coord('longitude')
    ICHECCCLM.remove_coord('grid_latitude')
    ICHECCCLM.remove_coord('grid_longitude')
    ICHECCCLM.add_dim_coord(lats, 1)
    ICHECCCLM.add_dim_coord(lons, 2)
    
    lats = iris.coords.DimCoord(ICHECKNMI.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = ICHECKNMI.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees') 
    
    ICHECKNMI.remove_coord('latitude')
    ICHECKNMI.remove_coord('longitude')
    ICHECKNMI.remove_coord('grid_latitude')
    ICHECKNMI.remove_coord('grid_longitude')
    ICHECKNMI.add_dim_coord(lats, 1)
    ICHECKNMI.add_dim_coord(lons, 2)
    
    lats = iris.coords.DimCoord(ICHECMPI.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = ICHECMPI.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees') 
    
    ICHECMPI.remove_coord('latitude')
    ICHECMPI.remove_coord('longitude')
    ICHECMPI.remove_coord('grid_latitude')
    ICHECMPI.remove_coord('grid_longitude')
    ICHECMPI.add_dim_coord(lats, 1)
    ICHECMPI.add_dim_coord(lons, 2)
    
    lats = iris.coords.DimCoord(ICHECSMHI.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = ICHECSMHI.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees')
    
    ICHECSMHI.remove_coord('latitude')
    ICHECSMHI.remove_coord('longitude')
    ICHECSMHI.remove_coord('grid_latitude')
    ICHECSMHI.remove_coord('grid_longitude')
    ICHECSMHI.add_dim_coord(lats, 1)
    ICHECSMHI.add_dim_coord(lons, 2)
    
    lats = iris.coords.DimCoord(CCCmaCanRCM85.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = CCCmaCanRCM85.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees')
                              
    CCCmaCanRCM85.remove_coord('latitude')
    CCCmaCanRCM85.remove_coord('longitude')
    CCCmaCanRCM85.remove_coord('grid_latitude')
    CCCmaCanRCM85.remove_coord('grid_longitude')
    CCCmaCanRCM85.add_dim_coord(lats, 1)
    CCCmaCanRCM85.add_dim_coord(lons, 2)
    
    lats = iris.coords.DimCoord(CCCmaSMHI85.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = CCCmaSMHI85.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees')
    
    CCCmaSMHI85.remove_coord('latitude')
    CCCmaSMHI85.remove_coord('longitude')
    CCCmaSMHI85.remove_coord('grid_latitude')
    CCCmaSMHI85.remove_coord('grid_longitude')
    CCCmaSMHI85.add_dim_coord(lats, 1)
    CCCmaSMHI85.add_dim_coord(lons, 2)  
    
    lats = iris.coords.DimCoord(CNRM85.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = CNRM85.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees')
                                
    CNRM85.remove_coord('latitude')
    CNRM85.remove_coord('longitude')
    CNRM85.remove_coord('grid_latitude')
    CNRM85.remove_coord('grid_longitude')
    CNRM85.add_dim_coord(lats, 1)
    CNRM85.add_dim_coord(lons, 2) 
    
    lats = iris.coords.DimCoord(CNRMSMHI85.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = CNRMSMHI85.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees')
    
    CNRMSMHI85.remove_coord('latitude')
    CNRMSMHI85.remove_coord('longitude')
    CNRMSMHI85.remove_coord('grid_latitude')
    CNRMSMHI85.remove_coord('grid_longitude')
    CNRMSMHI85.add_dim_coord(lats, 1)
    CNRMSMHI85.add_dim_coord(lons, 2) 
    
    lats = iris.coords.DimCoord(CSIRO85.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = CSIRO85.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees')
    
    CSIRO85.remove_coord('latitude')
    CSIRO85.remove_coord('longitude')
    CSIRO85.remove_coord('grid_latitude')
    CSIRO85.remove_coord('grid_longitude')
    CSIRO85.add_dim_coord(lats, 1)
    CSIRO85.add_dim_coord(lons, 2) 
    
    lats = iris.coords.DimCoord(ICHECDMI85.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = ICHECDMI85.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees')    
    
    ICHECDMI85.remove_coord('latitude')
    ICHECDMI85.remove_coord('longitude')
    ICHECDMI85.remove_coord('grid_latitude')
    ICHECDMI85.remove_coord('grid_longitude')
    ICHECDMI85.add_dim_coord(lats, 1)
    ICHECDMI85.add_dim_coord(lons, 2)
    
    lats = iris.coords.DimCoord(ICHECCCLM85.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = ICHECCCLM85.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees') 
    
    ICHECCCLM85.remove_coord('latitude')
    ICHECCCLM85.remove_coord('longitude')
    ICHECCCLM85.remove_coord('grid_latitude')
    ICHECCCLM85.remove_coord('grid_longitude')
    ICHECCCLM85.add_dim_coord(lats, 1)
    ICHECCCLM85.add_dim_coord(lons, 2)
    
    lats = iris.coords.DimCoord(ICHECKNMI85.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = ICHECKNMI85.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees') 
    
    ICHECKNMI85.remove_coord('latitude')
    ICHECKNMI85.remove_coord('longitude')
    ICHECKNMI85.remove_coord('grid_latitude')
    ICHECKNMI85.remove_coord('grid_longitude')
    ICHECKNMI85.add_dim_coord(lats, 1)
    ICHECKNMI85.add_dim_coord(lons, 2)
    
    lats = iris.coords.DimCoord(ICHECMPI85.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = ICHECMPI85.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees') 
    
    ICHECMPI85.remove_coord('latitude')
    ICHECMPI85.remove_coord('longitude')
    ICHECMPI85.remove_coord('grid_latitude')
    ICHECMPI85.remove_coord('grid_longitude')
    ICHECMPI85.add_dim_coord(lats, 1)
    ICHECMPI85.add_dim_coord(lons, 2)
    
    lats = iris.coords.DimCoord(ICHECSMHI85.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = ICHECSMHI85.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees')
    
    ICHECSMHI85.remove_coord('latitude')
    ICHECSMHI85.remove_coord('longitude')
    ICHECSMHI85.remove_coord('grid_latitude')
    ICHECSMHI85.remove_coord('grid_longitude')
    ICHECSMHI85.add_dim_coord(lats, 1)
    ICHECSMHI85.add_dim_coord(lons, 2)
    
    #guess bounds   
    CCCmaCanRCM.coord('latitude').guess_bounds()
    CCCmaSMHI.coord('latitude').guess_bounds()
    CNRM.coord('latitude').guess_bounds()
    CNRMSMHI.coord('latitude').guess_bounds()
    CSIRO.coord('latitude').guess_bounds()
    ICHECDMI.coord('latitude').guess_bounds()
    ICHECCCLM.coord('latitude').guess_bounds()
    ICHECKNMI.coord('latitude').guess_bounds()
    ICHECMPI.coord('latitude').guess_bounds()
    ICHECSMHI.coord('latitude').guess_bounds()
    
    CCCmaCanRCM85.coord('latitude').guess_bounds()
    CCCmaSMHI85.coord('latitude').guess_bounds()
    CNRM85.coord('latitude').guess_bounds()
    CNRMSMHI85.coord('latitude').guess_bounds()
    CSIRO85.coord('latitude').guess_bounds()
    ICHECDMI85.coord('latitude').guess_bounds()
    ICHECCCLM85.coord('latitude').guess_bounds()
    ICHECKNMI85.coord('latitude').guess_bounds()
    ICHECMPI85.coord('latitude').guess_bounds()
    ICHECSMHI85.coord('latitude').guess_bounds()
    
    CCCmaCanRCM.coord('longitude').guess_bounds()
    CCCmaSMHI.coord('longitude').guess_bounds()
    CNRM.coord('longitude').guess_bounds()
    CNRMSMHI.coord('longitude').guess_bounds()
    CSIRO.coord('longitude').guess_bounds()
    ICHECDMI.coord('longitude').guess_bounds()
    ICHECCCLM.coord('longitude').guess_bounds()
    ICHECKNMI.coord('longitude').guess_bounds()
    ICHECMPI.coord('longitude').guess_bounds()
    ICHECSMHI.coord('longitude').guess_bounds()
    
    CCCmaCanRCM85.coord('longitude').guess_bounds()
    CCCmaSMHI85.coord('longitude').guess_bounds()
    CNRM85.coord('longitude').guess_bounds()
    CNRMSMHI85.coord('longitude').guess_bounds()
    CSIRO85.coord('longitude').guess_bounds()
    ICHECDMI85.coord('longitude').guess_bounds()
    ICHECCCLM85.coord('longitude').guess_bounds()
    ICHECKNMI85.coord('longitude').guess_bounds()
    ICHECMPI85.coord('longitude').guess_bounds()
    ICHECSMHI85.coord('longitude').guess_bounds()
    
    
    #-------------------------------------------------------------------------
    #PART 3: LOAD AND FORMAT OBSERVED DATA
    #bring in all the files we need and give them a name
    CRU= '/exports/csce/datastore/geos/users/s0899345/Actual_Data/cru_ts4.01.1901.2016.tmx.dat.nc'
    
    #Load exactly one cube from given file
    CRU = iris.load_cube(CRU, 'near-surface temperature maximum')
    
    #guess bounds  
    CRU.coord('latitude').guess_bounds()
    
    CRU.coord('longitude').guess_bounds()
    
    
    #-------------------------------------------------------------------------
    #PART 4: FORMAT DATA GENERAL
    #Convert units to match, CORDEX data is in Kelvin but Observed data in Celsius, we would like to show all data in Celsius
    CCCmaCanRCM_past.convert_units('Celsius')
    CCCmaSMHI_past.convert_units('Celsius')
    CNRM_past.convert_units('Celsius')
    CNRMSMHI_past.convert_units('Celsius')
    CSIRO_past.convert_units('Celsius')
    ICHECDMI_past.convert_units('Celsius')
    ICHECCCLM_past.convert_units('Celsius') 
    ICHECKNMI_past.convert_units('Celsius')
    ICHECMPI_past.convert_units('Celsius')
    ICHECSMHI_past.convert_units('Celsius')
    
    CCCmaCanRCM.convert_units('Celsius')
    CCCmaSMHI.convert_units('Celsius')
    CNRM.convert_units('Celsius')
    CNRMSMHI.convert_units('Celsius')
    CSIRO.convert_units('Celsius')
    ICHECDMI.convert_units('Celsius')
    ICHECCCLM.convert_units('Celsius') 
    ICHECKNMI.convert_units('Celsius')
    ICHECMPI.convert_units('Celsius')
    ICHECSMHI.convert_units('Celsius')
    
    CCCmaCanRCM85.convert_units('Celsius')
    CCCmaSMHI85.convert_units('Celsius')
    CNRM85.convert_units('Celsius')
    CNRMSMHI85.convert_units('Celsius')
    CSIRO85.convert_units('Celsius')
    ICHECDMI85.convert_units('Celsius')
    ICHECCCLM85.convert_units('Celsius') 
    ICHECKNMI85.convert_units('Celsius')
    ICHECMPI85.convert_units('Celsius')
    ICHECSMHI85.convert_units('Celsius')
    
    #rename units to match
    CRU.units = Unit('Celsius')
    
    #add day of the year to all files
    iriscc.add_day_of_year(CCCmaCanRCM_past, 'time')
    iriscc.add_day_of_year(CCCmaSMHI_past, 'time')
    iriscc.add_day_of_year(CNRM_past, 'time')
    iriscc.add_day_of_year(CNRMSMHI_past, 'time')
    iriscc.add_day_of_year(CSIRO_past, 'time')
    iriscc.add_day_of_year(ICHECDMI_past, 'time')
    iriscc.add_day_of_year(ICHECCCLM_past, 'time')
    iriscc.add_day_of_year(ICHECKNMI_past, 'time')
    iriscc.add_day_of_year(ICHECMPI_past, 'time')
    iriscc.add_day_of_year(ICHECSMHI_past, 'time')
    
    iriscc.add_day_of_year(CCCmaCanRCM, 'time')
    iriscc.add_day_of_year(CCCmaSMHI, 'time')
    iriscc.add_day_of_year(CNRM, 'time')
    iriscc.add_day_of_year(CNRMSMHI, 'time')
    iriscc.add_day_of_year(CSIRO, 'time')
    iriscc.add_day_of_year(ICHECDMI, 'time')
    iriscc.add_day_of_year(ICHECCCLM, 'time')
    iriscc.add_day_of_year(ICHECKNMI, 'time')
    iriscc.add_day_of_year(ICHECMPI, 'time')
    iriscc.add_day_of_year(ICHECSMHI, 'time')
    
    iriscc.add_day_of_year(CCCmaCanRCM85, 'time')
    iriscc.add_day_of_year(CCCmaSMHI85, 'time')
    iriscc.add_day_of_year(CNRM85, 'time')
    iriscc.add_day_of_year(CNRMSMHI85, 'time')
    iriscc.add_day_of_year(CSIRO85, 'time')
    iriscc.add_day_of_year(ICHECDMI85, 'time')
    iriscc.add_day_of_year(ICHECCCLM85, 'time')
    iriscc.add_day_of_year(ICHECKNMI85, 'time')
    iriscc.add_day_of_year(ICHECMPI85, 'time')
    iriscc.add_day_of_year(ICHECSMHI85, 'time')
    
    iriscc.add_day_of_year(CRU, 'time')
    
    #add year data to files
    iriscc.add_year(CCCmaCanRCM_past, 'time')
    iriscc.add_year(CCCmaSMHI_past, 'time')
    iriscc.add_year(CNRM_past, 'time')
    iriscc.add_year(CNRMSMHI_past, 'time')
    iriscc.add_year(CSIRO_past, 'time')
    iriscc.add_year(ICHECDMI_past, 'time')
    iriscc.add_year(ICHECCCLM_past, 'time')
    iriscc.add_year(ICHECKNMI_past, 'time')
    iriscc.add_year(ICHECMPI_past, 'time')
    iriscc.add_year(ICHECSMHI_past, 'time')
    
    iriscc.add_year(CCCmaCanRCM, 'time')
    iriscc.add_year(CCCmaSMHI, 'time')
    iriscc.add_year(CNRM, 'time')
    iriscc.add_year(CNRMSMHI, 'time')
    iriscc.add_year(CSIRO, 'time')
    iriscc.add_year(ICHECDMI, 'time')
    iriscc.add_year(ICHECCCLM, 'time')
    iriscc.add_year(ICHECKNMI, 'time')
    iriscc.add_year(ICHECMPI, 'time')
    iriscc.add_year(ICHECSMHI, 'time')
    
    iriscc.add_year(CCCmaCanRCM85, 'time')
    iriscc.add_year(CCCmaSMHI85, 'time')
    iriscc.add_year(CNRM85, 'time')
    iriscc.add_year(CNRMSMHI85, 'time')
    iriscc.add_year(CSIRO85, 'time')
    iriscc.add_year(ICHECDMI85, 'time')
    iriscc.add_year(ICHECCCLM85, 'time')
    iriscc.add_year(ICHECKNMI85, 'time')
    iriscc.add_year(ICHECMPI85, 'time')
    iriscc.add_year(ICHECSMHI85, 'time')

    iriscc.add_year(CRU, 'time')
    
    #limit time series of data
    #time constraint to make past and obsered data only from 1971-2000 
    iris.FUTURE.cell_datetime_objects = True
    t_constraint_past = iris.Constraint(time=lambda cell: 1971 <= cell.point.year <= 2000)
    
    CCCmaCanRCM_past =  CCCmaCanRCM_past.extract(t_constraint_past)
    CCCmaSMHI_past =  CCCmaSMHI_past.extract(t_constraint_past)
    CNRM_past =  CNRM_past.extract(t_constraint_past)
    CNRMSMHI_past =  CNRMSMHI_past.extract(t_constraint_past)
    CSIRO_past =  CSIRO_past.extract(t_constraint_past)
    ICHECDMI_past =  ICHECDMI_past.extract(t_constraint_past)
    ICHECCCLM_past =  ICHECCCLM_past.extract(t_constraint_past)
    ICHECKNMI_past =  ICHECKNMI_past.extract(t_constraint_past)
    ICHECMPI_past =  ICHECMPI_past.extract(t_constraint_past)
    ICHECSMHI_past =  ICHECSMHI_past.extract(t_constraint_past)
    
    CRU = CRU.extract(t_constraint_past)
    
    #time constraint to make future data only from 2020-2049
    iris.FUTURE.cell_datetime_objects = True
    t_constraint_future = iris.Constraint(time=lambda cell: 2020 <= cell.point.year <= 2049)
    
    CCCmaCanRCM_30 = CCCmaCanRCM.extract(t_constraint_future)
    CCCmaSMHI_30 = CCCmaSMHI.extract(t_constraint_future)
    CNRM_30 = CNRM.extract(t_constraint_future)
    CNRMSMHI_30 = CNRMSMHI.extract(t_constraint_future)
    CSIRO_30 = CSIRO.extract(t_constraint_future)
    ICHECDMI_30 = ICHECDMI.extract(t_constraint_future)
    ICHECCCLM_30 = ICHECCCLM.extract(t_constraint_future)
    ICHECKNMI_30 = ICHECKNMI.extract(t_constraint_future)
    ICHECMPI_30 = ICHECMPI.extract(t_constraint_future)
    ICHECSMHI_30 = ICHECSMHI.extract(t_constraint_future)
    
    CCCmaCanRCM85_30 = CCCmaCanRCM85.extract(t_constraint_future)
    CCCmaSMHI85_30 = CCCmaSMHI85.extract(t_constraint_future)
    CNRM85_30 = CNRM85.extract(t_constraint_future)
    CNRMSMHI85_30 = CNRMSMHI85.extract(t_constraint_future)
    CSIRO85_30 = CSIRO85.extract(t_constraint_future)
    ICHECDMI85_30 = ICHECDMI85.extract(t_constraint_future)
    ICHECCCLM85_30 = ICHECCCLM85.extract(t_constraint_future)
    ICHECKNMI85_30 = ICHECKNMI85.extract(t_constraint_future)
    ICHECMPI85_30 = ICHECMPI85.extract(t_constraint_future)
    ICHECSMHI85_30 = ICHECSMHI85.extract(t_constraint_future)
    
    #time constraint to make future data only from 2040-2069
    iris.FUTURE.cell_datetime_objects = True
    t_constraint_future = iris.Constraint(time=lambda cell: 2040 <= cell.point.year <= 2069)
    
    CCCmaCanRCM_50 = CCCmaCanRCM.extract(t_constraint_future)
    CCCmaSMHI_50 = CCCmaSMHI.extract(t_constraint_future)
    CNRM_50 = CNRM.extract(t_constraint_future)
    CNRMSMHI_50 = CNRMSMHI.extract(t_constraint_future)
    CSIRO_50 = CSIRO.extract(t_constraint_future)
    ICHECDMI_50 = ICHECDMI.extract(t_constraint_future)
    ICHECCCLM_50 = ICHECCCLM.extract(t_constraint_future)
    ICHECKNMI_50 = ICHECKNMI.extract(t_constraint_future)
    ICHECMPI_50 = ICHECMPI.extract(t_constraint_future)
    ICHECSMHI_50 = ICHECSMHI.extract(t_constraint_future)
    
    CCCmaCanRCM85_50 = CCCmaCanRCM85.extract(t_constraint_future)
    CCCmaSMHI85_50 = CCCmaSMHI85.extract(t_constraint_future)
    CNRM85_50 = CNRM85.extract(t_constraint_future)
    CNRMSMHI85_50 = CNRMSMHI85.extract(t_constraint_future)
    CSIRO85_50 = CSIRO85.extract(t_constraint_future)
    ICHECDMI85_50 = ICHECDMI85.extract(t_constraint_future)
    ICHECCCLM85_50 = ICHECCCLM85.extract(t_constraint_future)
    ICHECKNMI85_50 = ICHECKNMI85.extract(t_constraint_future)
    ICHECMPI85_50 = ICHECMPI85.extract(t_constraint_future)
    ICHECSMHI85_50 = ICHECSMHI85.extract(t_constraint_future)
    
    
    #-------------------------------------------------------------------------
    #PART 5: FORMAT DATA TO GEOGRAPHICALLY SPECIFIC AND RE-BASELINE
    #PART 5A: NORTHERN MALAWI
    #we are only interested in the latitude and longitude relevant to Central Malawi 
    Northern_Malawi = iris.Constraint(longitude=lambda v: 32.5 <= v <= 35, latitude=lambda v: -12.5 <= v <= -8.5) 
    
    CCCmaCanRCM_past_N = CCCmaCanRCM_past.extract(Northern_Malawi)
    CCCmaSMHI_past_N = CCCmaSMHI_past.extract(Northern_Malawi)
    CNRM_past_N = CNRM_past.extract(Northern_Malawi)
    CNRMSMHI_past_N = CNRMSMHI_past.extract(Northern_Malawi)
    CSIRO_past_N = CSIRO_past.extract(Northern_Malawi)
    ICHECDMI_past_N = ICHECDMI_past.extract(Northern_Malawi)
    ICHECCCLM_past_N = ICHECCCLM_past.extract(Northern_Malawi)
    ICHECKNMI_past_N = ICHECKNMI_past.extract(Northern_Malawi)
    ICHECMPI_past_N = ICHECMPI_past.extract(Northern_Malawi)
    ICHECSMHI_past_N = ICHECSMHI_past.extract(Northern_Malawi)
    
    CCCmaCanRCM_30_N = CCCmaCanRCM_30.extract(Northern_Malawi)
    CCCmaSMHI_30_N = CCCmaSMHI_30.extract(Northern_Malawi)
    CNRM_30_N = CNRM_30.extract(Northern_Malawi)
    CNRMSMHI_30_N = CNRMSMHI_30.extract(Northern_Malawi)
    CSIRO_30_N = CSIRO_30.extract(Northern_Malawi)
    ICHECDMI_30_N = ICHECDMI_30.extract(Northern_Malawi)
    ICHECCCLM_30_N = ICHECCCLM_30.extract(Northern_Malawi)
    ICHECKNMI_30_N = ICHECKNMI_30.extract(Northern_Malawi)
    ICHECMPI_30_N = ICHECMPI_30.extract(Northern_Malawi)
    ICHECSMHI_30_N = ICHECSMHI_30.extract(Northern_Malawi)
    
    CCCmaCanRCM85_30_N = CCCmaCanRCM85_30.extract(Northern_Malawi)
    CCCmaSMHI85_30_N = CCCmaSMHI85_30.extract(Northern_Malawi)
    CNRM85_30_N = CNRM85_30.extract(Northern_Malawi)
    CNRMSMHI85_30_N = CNRMSMHI85_30.extract(Northern_Malawi)
    CSIRO85_30_N = CSIRO85_30.extract(Northern_Malawi)
    ICHECDMI85_30_N = ICHECDMI85_30.extract(Northern_Malawi)
    ICHECCCLM85_30_N = ICHECCCLM85_30.extract(Northern_Malawi)
    ICHECKNMI85_30_N = ICHECKNMI85_30.extract(Northern_Malawi)
    ICHECMPI85_30_N = ICHECMPI85_30.extract(Northern_Malawi)
    ICHECSMHI85_30_N = ICHECSMHI85_30.extract(Northern_Malawi)
    
    CCCmaCanRCM_50_N = CCCmaCanRCM_50.extract(Northern_Malawi)
    CCCmaSMHI_50_N = CCCmaSMHI_50.extract(Northern_Malawi)
    CNRM_50_N = CNRM_50.extract(Northern_Malawi)
    CNRMSMHI_50_N = CNRMSMHI_50.extract(Northern_Malawi)
    CSIRO_50_N = CSIRO_50.extract(Northern_Malawi)
    ICHECDMI_50_N = ICHECDMI_50.extract(Northern_Malawi)
    ICHECCCLM_50_N = ICHECCCLM_50.extract(Northern_Malawi)
    ICHECKNMI_50_N = ICHECKNMI_50.extract(Northern_Malawi)
    ICHECMPI_50_N = ICHECMPI_50.extract(Northern_Malawi)
    ICHECSMHI_50_N = ICHECSMHI_50.extract(Northern_Malawi)
    
    CCCmaCanRCM85_50_N = CCCmaCanRCM85_50.extract(Northern_Malawi)
    CCCmaSMHI85_50_N = CCCmaSMHI85_50.extract(Northern_Malawi)
    CNRM85_50_N = CNRM85_50.extract(Northern_Malawi)
    CNRMSMHI85_50_N = CNRMSMHI85_50.extract(Northern_Malawi)
    CSIRO85_50_N = CSIRO85_50.extract(Northern_Malawi)
    ICHECDMI85_50_N = ICHECDMI85_50.extract(Northern_Malawi)
    ICHECCCLM85_50_N = ICHECCCLM85_50.extract(Northern_Malawi)
    ICHECKNMI85_50_N = ICHECKNMI85_50.extract(Northern_Malawi)
    ICHECMPI85_50_N = ICHECMPI85_50.extract(Northern_Malawi)
    ICHECSMHI85_50_N = ICHECSMHI85_50.extract(Northern_Malawi)
    
    CRU_N = CRU.extract(Northern_Malawi)
    
    #We are interested in plotting the data by date, so we need to take a mean of all the data by day of the year
    CCCmaCanRCM_past_N = CCCmaCanRCM_past_N.aggregated_by('day_of_year', iris.analysis.MEAN)
    CCCmaSMHI_past_N = CCCmaSMHI_past_N.aggregated_by('day_of_year', iris.analysis.MEAN)
    CNRM_past_N = CNRM_past_N.aggregated_by('day_of_year', iris.analysis.MEAN)
    CNRMSMHI_past_N = CNRMSMHI_past_N.aggregated_by('day_of_year', iris.analysis.MEAN)
    CSIRO_past_N = CSIRO_past_N.aggregated_by('day_of_year', iris.analysis.MEAN)
    ICHECDMI_past_N = ICHECDMI_past_N.aggregated_by('day_of_year', iris.analysis.MEAN)
    ICHECCCLM_past_N = ICHECCCLM_past_N.aggregated_by('day_of_year', iris.analysis.MEAN)
    ICHECKNMI_past_N = ICHECKNMI_past_N.aggregated_by('day_of_year', iris.analysis.MEAN)
    ICHECMPI_past_N = ICHECMPI_past_N.aggregated_by('day_of_year', iris.analysis.MEAN)
    ICHECSMHI_past_N = ICHECSMHI_past_N.aggregated_by('day_of_year', iris.analysis.MEAN)
    
    CCCmaCanRCM_30_N = CCCmaCanRCM_30_N.aggregated_by('day_of_year', iris.analysis.MEAN)
    CCCmaSMHI_30_N = CCCmaSMHI_30_N.aggregated_by('day_of_year', iris.analysis.MEAN)
    CNRM_30_N = CNRM_30_N.aggregated_by('day_of_year', iris.analysis.MEAN)
    CNRMSMHI_30_N = CNRMSMHI_30_N.aggregated_by('day_of_year', iris.analysis.MEAN)
    CSIRO_30_N = CSIRO_30_N.aggregated_by('day_of_year', iris.analysis.MEAN)
    ICHECDMI_30_N = ICHECDMI_30_N.aggregated_by('day_of_year', iris.analysis.MEAN)
    ICHECCCLM_30_N = ICHECCCLM_30_N.aggregated_by('day_of_year', iris.analysis.MEAN)
    ICHECKNMI_30_N = ICHECKNMI_30_N.aggregated_by('day_of_year', iris.analysis.MEAN)
    ICHECMPI_30_N = ICHECMPI_30_N.aggregated_by('day_of_year', iris.analysis.MEAN)
    ICHECSMHI_30_N = ICHECSMHI_30_N.aggregated_by('day_of_year', iris.analysis.MEAN)
    
    CCCmaCanRCM85_30_N = CCCmaCanRCM85_30_N.aggregated_by('day_of_year', iris.analysis.MEAN)
    CCCmaSMHI85_30_N = CCCmaSMHI85_30_N.aggregated_by('day_of_year', iris.analysis.MEAN)
    CNRM85_30_N = CNRM85_30_N.aggregated_by('day_of_year', iris.analysis.MEAN)
    CNRMSMHI85_30_N = CNRMSMHI85_30_N.aggregated_by('day_of_year', iris.analysis.MEAN)
    CSIRO85_30_N = CSIRO85_30_N.aggregated_by('day_of_year', iris.analysis.MEAN)
    ICHECDMI85_30_N = ICHECDMI85_30_N.aggregated_by('day_of_year', iris.analysis.MEAN)
    ICHECCCLM85_30_N = ICHECCCLM85_30_N.aggregated_by('day_of_year', iris.analysis.MEAN)
    ICHECKNMI85_30_N = ICHECKNMI85_30_N.aggregated_by('day_of_year', iris.analysis.MEAN)
    ICHECMPI85_30_N = ICHECMPI85_30_N.aggregated_by('day_of_year', iris.analysis.MEAN)
    ICHECSMHI85_30_N = ICHECSMHI85_30_N.aggregated_by('day_of_year', iris.analysis.MEAN)
    
    CCCmaCanRCM_50_N = CCCmaCanRCM_50_N.aggregated_by('day_of_year', iris.analysis.MEAN)
    CCCmaSMHI_50_N = CCCmaSMHI_50_N.aggregated_by('day_of_year', iris.analysis.MEAN)
    CNRM_50_N = CNRM_50_N.aggregated_by('day_of_year', iris.analysis.MEAN)
    CNRMSMHI_50_N = CNRMSMHI_50_N.aggregated_by('day_of_year', iris.analysis.MEAN)
    CSIRO_50_N = CSIRO_50_N.aggregated_by('day_of_year', iris.analysis.MEAN)
    ICHECDMI_50_N = ICHECDMI_50_N.aggregated_by('day_of_year', iris.analysis.MEAN)
    ICHECCCLM_50_N = ICHECCCLM_50_N.aggregated_by('day_of_year', iris.analysis.MEAN)
    ICHECKNMI_50_N = ICHECKNMI_50_N.aggregated_by('day_of_year', iris.analysis.MEAN)
    ICHECMPI_50_N = ICHECMPI_50_N.aggregated_by('day_of_year', iris.analysis.MEAN)
    ICHECSMHI_50_N = ICHECSMHI_50_N.aggregated_by('day_of_year', iris.analysis.MEAN)
    
    CCCmaCanRCM85_50_N = CCCmaCanRCM85_50_N.aggregated_by('day_of_year', iris.analysis.MEAN)
    CCCmaSMHI85_50_N = CCCmaSMHI85_50_N.aggregated_by('day_of_year', iris.analysis.MEAN)
    CNRM85_50_N = CNRM85_50_N.aggregated_by('day_of_year', iris.analysis.MEAN)
    CNRMSMHI85_50_N = CNRMSMHI85_50_N.aggregated_by('day_of_year', iris.analysis.MEAN)
    CSIRO85_50_N = CSIRO85_50_N.aggregated_by('day_of_year', iris.analysis.MEAN)
    ICHECDMI85_50_N = ICHECDMI85_50_N.aggregated_by('day_of_year', iris.analysis.MEAN)
    ICHECCCLM85_50_N = ICHECCCLM85_50_N.aggregated_by('day_of_year', iris.analysis.MEAN)
    ICHECKNMI85_50_N = ICHECKNMI85_50_N.aggregated_by('day_of_year', iris.analysis.MEAN)
    ICHECMPI85_50_N = ICHECMPI85_50_N.aggregated_by('day_of_year', iris.analysis.MEAN)
    ICHECSMHI85_50_N = ICHECSMHI85_50_N.aggregated_by('day_of_year', iris.analysis.MEAN)
    
    CRU_N = CRU_N.aggregated_by('day_of_year', iris.analysis.MEAN)
    
    #Returns an array of area weights, with the same dimensions as the cube
    CCCmaCanRCM_past_N_grid_areas = iris.analysis.cartography.area_weights(CCCmaCanRCM_past_N)
    CCCmaSMHI_past_N_grid_areas = iris.analysis.cartography.area_weights(CCCmaSMHI_past_N)
    CNRM_past_N_grid_areas = iris.analysis.cartography.area_weights(CNRM_past_N)
    CNRMSMHI_past_N_grid_areas = iris.analysis.cartography.area_weights(CNRMSMHI_past_N)
    CSIRO_past_N_grid_areas = iris.analysis.cartography.area_weights(CSIRO_past_N)
    ICHECDMI_past_N_grid_areas = iris.analysis.cartography.area_weights(ICHECDMI_past_N)
    ICHECCCLM_past_N_grid_areas = iris.analysis.cartography.area_weights(ICHECCCLM_past_N)
    ICHECKNMI_past_N_grid_areas = iris.analysis.cartography.area_weights(ICHECKNMI_past_N)
    ICHECMPI_past_N_grid_areas = iris.analysis.cartography.area_weights(ICHECMPI_past_N)
    ICHECSMHI_past_N_grid_areas = iris.analysis.cartography.area_weights(ICHECSMHI_past_N)
    
    CCCmaCanRCM_30_N_grid_areas = iris.analysis.cartography.area_weights(CCCmaCanRCM_30_N)
    CCCmaSMHI_30_N_grid_areas = iris.analysis.cartography.area_weights(CCCmaSMHI_30_N)
    CNRM_30_N_grid_areas = iris.analysis.cartography.area_weights(CNRM_30_N)
    CNRMSMHI_30_N_grid_areas = iris.analysis.cartography.area_weights(CNRMSMHI_30_N)
    CSIRO_30_N_grid_areas = iris.analysis.cartography.area_weights(CSIRO_30_N)
    ICHECDMI_30_N_grid_areas = iris.analysis.cartography.area_weights(ICHECDMI_30_N)
    ICHECCCLM_30_N_grid_areas = iris.analysis.cartography.area_weights(ICHECCCLM_30_N)
    ICHECKNMI_30_N_grid_areas = iris.analysis.cartography.area_weights(ICHECKNMI_30_N)
    ICHECMPI_30_N_grid_areas = iris.analysis.cartography.area_weights(ICHECMPI_30_N)
    ICHECSMHI_30_N_grid_areas = iris.analysis.cartography.area_weights(ICHECSMHI_30_N)
    
    CCCmaCanRCM85_30_N_grid_areas = iris.analysis.cartography.area_weights(CCCmaCanRCM85_30_N)
    CCCmaSMHI85_30_N_grid_areas = iris.analysis.cartography.area_weights(CCCmaSMHI85_30_N)
    CNRM85_30_N_grid_areas = iris.analysis.cartography.area_weights(CNRM85_30_N)
    CNRMSMHI85_30_N_grid_areas = iris.analysis.cartography.area_weights(CNRMSMHI85_30_N)
    CSIRO85_30_N_grid_areas = iris.analysis.cartography.area_weights(CSIRO85_30_N)
    ICHECDMI85_30_N_grid_areas = iris.analysis.cartography.area_weights(ICHECDMI85_30_N)
    ICHECCCLM85_30_N_grid_areas = iris.analysis.cartography.area_weights(ICHECCCLM85_30_N)
    ICHECKNMI85_30_N_grid_areas = iris.analysis.cartography.area_weights(ICHECKNMI85_30_N)
    ICHECMPI85_30_N_grid_areas = iris.analysis.cartography.area_weights(ICHECMPI85_30_N)
    ICHECSMHI85_30_N_grid_areas = iris.analysis.cartography.area_weights(ICHECSMHI85_30_N)
    
    CCCmaCanRCM_50_N_grid_areas = iris.analysis.cartography.area_weights(CCCmaCanRCM_50_N)
    CCCmaSMHI_50_N_grid_areas = iris.analysis.cartography.area_weights(CCCmaSMHI_50_N)
    CNRM_50_N_grid_areas = iris.analysis.cartography.area_weights(CNRM_50_N)
    CNRMSMHI_50_N_grid_areas = iris.analysis.cartography.area_weights(CNRMSMHI_50_N)
    CSIRO_50_N_grid_areas = iris.analysis.cartography.area_weights(CSIRO_50_N)
    ICHECDMI_50_N_grid_areas = iris.analysis.cartography.area_weights(ICHECDMI_50_N)
    ICHECCCLM_50_N_grid_areas = iris.analysis.cartography.area_weights(ICHECCCLM_50_N)
    ICHECKNMI_50_N_grid_areas = iris.analysis.cartography.area_weights(ICHECKNMI_50_N)
    ICHECMPI_50_N_grid_areas = iris.analysis.cartography.area_weights(ICHECMPI_50_N)
    ICHECSMHI_50_N_grid_areas = iris.analysis.cartography.area_weights(ICHECSMHI_50_N)
    
    CCCmaCanRCM85_50_N_grid_areas = iris.analysis.cartography.area_weights(CCCmaCanRCM85_50_N)
    CCCmaSMHI85_50_N_grid_areas = iris.analysis.cartography.area_weights(CCCmaSMHI85_50_N)
    CNRM85_50_N_grid_areas = iris.analysis.cartography.area_weights(CNRM85_50_N)
    CNRMSMHI85_50_N_grid_areas = iris.analysis.cartography.area_weights(CNRMSMHI85_50_N)
    CSIRO85_50_N_grid_areas = iris.analysis.cartography.area_weights(CSIRO85_50_N)
    ICHECDMI85_50_N_grid_areas = iris.analysis.cartography.area_weights(ICHECDMI85_50_N)
    ICHECCCLM85_50_N_grid_areas = iris.analysis.cartography.area_weights(ICHECCCLM85_50_N)
    ICHECKNMI85_50_N_grid_areas = iris.analysis.cartography.area_weights(ICHECKNMI85_50_N)
    ICHECMPI85_50_N_grid_areas = iris.analysis.cartography.area_weights(ICHECMPI85_50_N)
    ICHECSMHI85_50_N_grid_areas = iris.analysis.cartography.area_weights(ICHECSMHI85_50_N)
    
    CRU_N_grid_areas = iris.analysis.cartography.area_weights(CRU_N)
    
    #We want to plot the mean for the whole region so we need a mean of all the lats and lons
    CCCmaCanRCM_past_N_mean = CCCmaCanRCM_past_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CCCmaCanRCM_past_N_grid_areas) 
    CCCmaSMHI_past_N_mean = CCCmaSMHI_past_N.collapsed(['latitude', 'longitude'],iris.analysis.MEAN, weights=CCCmaSMHI_past_N_grid_areas)
    CNRM_past_N_mean = CNRM_past_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CNRM_past_N_grid_areas)                           
    CNRMSMHI_past_N_mean = CNRMSMHI_past_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CNRMSMHI_past_N_grid_areas)  
    CSIRO_past_N_mean = CSIRO_past_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CSIRO_past_N_grid_areas)
    ICHECDMI_past_N_mean = ICHECDMI_past_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECDMI_past_N_grid_areas) 
    ICHECCCLM_past_N_mean = ICHECCCLM_past_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECCCLM_past_N_grid_areas)
    ICHECKNMI_past_N_mean = ICHECKNMI_past_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECKNMI_past_N_grid_areas)
    ICHECMPI_past_N_mean = ICHECMPI_past_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECMPI_past_N_grid_areas)
    ICHECSMHI_past_N_mean = ICHECSMHI_past_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECSMHI_past_N_grid_areas)
    
    CCCmaCanRCM_30_N_mean = CCCmaCanRCM_30_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CCCmaCanRCM_30_N_grid_areas) 
    CCCmaSMHI_30_N_mean = CCCmaSMHI_30_N.collapsed(['latitude', 'longitude'],iris.analysis.MEAN, weights=CCCmaSMHI_30_N_grid_areas)
    CNRM_30_N_mean = CNRM_30_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CNRM_30_N_grid_areas)                           
    CNRMSMHI_30_N_mean = CNRMSMHI_30_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CNRMSMHI_30_N_grid_areas)  
    CSIRO_30_N_mean = CSIRO_30_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CSIRO_30_N_grid_areas)
    ICHECDMI_30_N_mean = ICHECDMI_30_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECDMI_30_N_grid_areas) 
    ICHECCCLM_30_N_mean = ICHECCCLM_30_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECCCLM_30_N_grid_areas)
    ICHECKNMI_30_N_mean = ICHECKNMI_30_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECKNMI_30_N_grid_areas)
    ICHECMPI_30_N_mean = ICHECMPI_30_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECMPI_30_N_grid_areas)
    ICHECSMHI_30_N_mean = ICHECSMHI_30_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECSMHI_30_N_grid_areas)
    
    CCCmaCanRCM85_30_N_mean = CCCmaCanRCM85_30_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CCCmaCanRCM85_30_N_grid_areas) 
    CCCmaSMHI85_30_N_mean = CCCmaSMHI85_30_N.collapsed(['latitude', 'longitude'],iris.analysis.MEAN, weights=CCCmaSMHI85_30_N_grid_areas)
    CNRM85_30_N_mean = CNRM85_30_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CNRM85_30_N_grid_areas)                           
    CNRMSMHI85_30_N_mean = CNRMSMHI85_30_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CNRMSMHI85_30_N_grid_areas)  
    CSIRO85_30_N_mean = CSIRO85_30_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CSIRO85_30_N_grid_areas)
    ICHECDMI85_30_N_mean = ICHECDMI85_30_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECDMI85_30_N_grid_areas) 
    ICHECCCLM85_30_N_mean = ICHECCCLM85_30_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECCCLM85_30_N_grid_areas)
    ICHECKNMI85_30_N_mean = ICHECKNMI85_30_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECKNMI85_30_N_grid_areas)
    ICHECMPI85_30_N_mean = ICHECMPI85_30_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECMPI85_30_N_grid_areas)
    ICHECSMHI85_30_N_mean = ICHECSMHI85_30_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECSMHI85_30_N_grid_areas)
    
    CCCmaCanRCM_50_N_mean = CCCmaCanRCM_50_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CCCmaCanRCM_50_N_grid_areas) 
    CCCmaSMHI_50_N_mean = CCCmaSMHI_50_N.collapsed(['latitude', 'longitude'],iris.analysis.MEAN, weights=CCCmaSMHI_50_N_grid_areas)
    CNRM_50_N_mean = CNRM_50_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CNRM_50_N_grid_areas)                           
    CNRMSMHI_50_N_mean = CNRMSMHI_50_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CNRMSMHI_50_N_grid_areas)  
    CSIRO_50_N_mean = CSIRO_50_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CSIRO_50_N_grid_areas)
    ICHECDMI_50_N_mean = ICHECDMI_50_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECDMI_50_N_grid_areas) 
    ICHECCCLM_50_N_mean = ICHECCCLM_50_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECCCLM_50_N_grid_areas)
    ICHECKNMI_50_N_mean = ICHECKNMI_50_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECKNMI_50_N_grid_areas)
    ICHECMPI_50_N_mean = ICHECMPI_50_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECMPI_50_N_grid_areas)
    ICHECSMHI_50_N_mean = ICHECSMHI_50_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECSMHI_50_N_grid_areas)
    
    CCCmaCanRCM85_50_N_mean = CCCmaCanRCM85_50_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CCCmaCanRCM85_50_N_grid_areas) 
    CCCmaSMHI85_50_N_mean = CCCmaSMHI85_50_N.collapsed(['latitude', 'longitude'],iris.analysis.MEAN, weights=CCCmaSMHI85_50_N_grid_areas)
    CNRM85_50_N_mean = CNRM85_50_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CNRM85_50_N_grid_areas)                           
    CNRMSMHI85_50_N_mean = CNRMSMHI85_50_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CNRMSMHI85_50_N_grid_areas)  
    CSIRO85_50_N_mean = CSIRO85_50_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CSIRO85_50_N_grid_areas)
    ICHECDMI85_50_N_mean = ICHECDMI85_50_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECDMI85_50_N_grid_areas) 
    ICHECCCLM85_50_N_mean = ICHECCCLM85_50_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECCCLM85_50_N_grid_areas)
    ICHECKNMI85_50_N_mean = ICHECKNMI85_50_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECKNMI85_50_N_grid_areas)
    ICHECMPI85_50_N_mean = ICHECMPI85_50_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECMPI85_50_N_grid_areas)
    ICHECSMHI85_50_N_mean = ICHECSMHI85_50_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECSMHI85_50_N_grid_areas)
    
    CRU_N_mean = CRU_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CRU_N_grid_areas)
    
    #for the baseline we don't need to average for each year, but the average for the whole time period, so collapse by time
    CCCmaCanRCM_b_N_mean = CCCmaCanRCM_past_N_mean.collapsed(['time'], iris.analysis.MEAN) 
    CCCmaSMHI_b_N_mean = CCCmaSMHI_past_N_mean.collapsed(['time'], iris.analysis.MEAN) 
    CNRM_b_N_mean = CNRM_past_N_mean.collapsed(['time'], iris.analysis.MEAN)                      
    CNRMSMHI_b_N_mean = CNRMSMHI_past_N_mean.collapsed(['time'], iris.analysis.MEAN)   
    CSIRO_b_N_mean = CSIRO_past_N_mean.collapsed(['time'], iris.analysis.MEAN)
    ICHECDMI_b_N_mean = ICHECDMI_past_N_mean.collapsed(['time'], iris.analysis.MEAN)  
    ICHECCCLM_b_N_mean = ICHECCCLM_past_N_mean.collapsed(['time'], iris.analysis.MEAN) 
    ICHECKNMI_b_N_mean = ICHECKNMI_past_N_mean.collapsed(['time'], iris.analysis.MEAN) 
    ICHECMPI_b_N_mean = ICHECMPI_past_N_mean.collapsed(['time'], iris.analysis.MEAN) 
    ICHECSMHI_b_N_mean = ICHECSMHI_past_N_mean.collapsed(['time'], iris.analysis.MEAN)  
    
    CRU_N_mean = CRU_N_mean.collapsed(['time'], iris.analysis.MEAN) 
    
    #create average of observed baseline data
    Obs_N = (CRU_N_mean)  
    
    #We want to see the change in temperature from the baseline
    CCCmaCanRCM_past_N_mean = (CCCmaCanRCM_past_N_mean.data - CCCmaCanRCM_b_N_mean.data + Obs_N.data)
    CCCmaSMHI_past_N_mean = (CCCmaSMHI_past_N_mean.data - CCCmaSMHI_b_N_mean.data + Obs_N.data)
    CNRM_past_N_mean = (CNRM_past_N_mean.data - CNRM_b_N_mean.data + Obs_N.data)
    CNRMSMHI_past_N_mean = (CNRMSMHI_past_N_mean.data - CNRMSMHI_b_N_mean.data + Obs_N.data)  
    CSIRO_past_N_mean = (CSIRO_past_N_mean.data - CSIRO_b_N_mean.data + Obs_N.data)
    ICHECDMI_past_N_mean = (ICHECDMI_past_N_mean.data - ICHECDMI_b_N_mean.data + Obs_N.data) 
    ICHECCCLM_past_N_mean = (ICHECCCLM_past_N_mean.data - ICHECCCLM_b_N_mean.data + Obs_N.data)
    ICHECKNMI_past_N_mean = (ICHECKNMI_past_N_mean.data - ICHECKNMI_b_N_mean.data + Obs_N.data)
    ICHECMPI_past_N_mean = (ICHECMPI_past_N_mean.data - ICHECMPI_b_N_mean.data + Obs_N.data)
    ICHECSMHI_past_N_mean = (ICHECSMHI_past_N_mean.data - ICHECSMHI_b_N_mean.data + Obs_N.data)
    
    CCCmaCanRCM_30_N_mean = (CCCmaCanRCM_30_N_mean.data - CCCmaCanRCM_b_N_mean.data + Obs_N.data)
    CCCmaSMHI_30_N_mean = (CCCmaSMHI_30_N_mean.data - CCCmaSMHI_b_N_mean.data + Obs_N.data)
    CNRM_30_N_mean = (CNRM_30_N_mean.data - CNRM_b_N_mean.data + Obs_N.data)
    CNRMSMHI_30_N_mean = (CNRMSMHI_30_N_mean.data - CNRMSMHI_b_N_mean.data + Obs_N.data)  
    CSIRO_30_N_mean = (CSIRO_30_N_mean.data - CSIRO_b_N_mean.data + Obs_N.data)
    ICHECDMI_30_N_mean = (ICHECDMI_30_N_mean.data - ICHECDMI_b_N_mean.data + Obs_N.data) 
    ICHECCCLM_30_N_mean = (ICHECCCLM_30_N_mean.data - ICHECCCLM_b_N_mean.data + Obs_N.data)
    ICHECKNMI_30_N_mean = (ICHECKNMI_30_N_mean.data - ICHECKNMI_b_N_mean.data + Obs_N.data)
    ICHECMPI_30_N_mean = (ICHECMPI_30_N_mean.data - ICHECMPI_b_N_mean.data + Obs_N.data)
    ICHECSMHI_30_N_mean = (ICHECSMHI_30_N_mean.data - ICHECSMHI_b_N_mean.data + Obs_N.data)
    
    CCCmaCanRCM85_30_N_mean = (CCCmaCanRCM85_30_N_mean.data - CCCmaCanRCM_b_N_mean.data + Obs_N.data)
    CCCmaSMHI85_30_N_mean = (CCCmaSMHI85_30_N_mean.data - CCCmaSMHI_b_N_mean.data + Obs_N.data)
    CNRM85_30_N_mean = (CNRM85_30_N_mean.data - CNRM_b_N_mean.data + Obs_N.data)
    CNRMSMHI85_30_N_mean = (CNRMSMHI85_30_N_mean.data - CNRMSMHI_b_N_mean.data + Obs_N.data)  
    CSIRO85_30_N_mean = (CSIRO85_30_N_mean.data - CSIRO_b_N_mean.data + Obs_N.data)
    ICHECDMI85_30_N_mean = (ICHECDMI85_30_N_mean.data - ICHECDMI_b_N_mean.data + Obs_N.data) 
    ICHECCCLM85_30_N_mean = (ICHECCCLM85_30_N_mean.data - ICHECCCLM_b_N_mean.data + Obs_N.data)
    ICHECKNMI85_30_N_mean = (ICHECKNMI85_30_N_mean.data - ICHECKNMI_b_N_mean.data + Obs_N.data)
    ICHECMPI85_30_N_mean = (ICHECMPI85_30_N_mean.data - ICHECMPI_b_N_mean.data + Obs_N.data)
    ICHECSMHI85_30_N_mean = (ICHECSMHI85_30_N_mean.data - ICHECSMHI_b_N_mean.data + Obs_N.data)
    
    CCCmaCanRCM_50_N_mean = (CCCmaCanRCM_50_N_mean.data - CCCmaCanRCM_b_N_mean.data + Obs_N.data)
    CCCmaSMHI_50_N_mean = (CCCmaSMHI_50_N_mean.data - CCCmaSMHI_b_N_mean.data + Obs_N.data)
    CNRM_50_N_mean = (CNRM_50_N_mean.data - CNRM_b_N_mean.data + Obs_N.data)
    CNRMSMHI_50_N_mean = (CNRMSMHI_50_N_mean.data - CNRMSMHI_b_N_mean.data + Obs_N.data)  
    CSIRO_50_N_mean = (CSIRO_50_N_mean.data - CSIRO_b_N_mean.data + Obs_N.data)
    ICHECDMI_50_N_mean = (ICHECDMI_50_N_mean.data - ICHECDMI_b_N_mean.data + Obs_N.data) 
    ICHECCCLM_50_N_mean = (ICHECCCLM_50_N_mean.data - ICHECCCLM_b_N_mean.data + Obs_N.data)
    ICHECKNMI_50_N_mean = (ICHECKNMI_50_N_mean.data - ICHECKNMI_b_N_mean.data + Obs_N.data)
    ICHECMPI_50_N_mean = (ICHECMPI_50_N_mean.data - ICHECMPI_b_N_mean.data + Obs_N.data)
    ICHECSMHI_50_N_mean = (ICHECSMHI_50_N_mean.data - ICHECSMHI_b_N_mean.data + Obs_N.data)
    
    CCCmaCanRCM85_50_N_mean = (CCCmaCanRCM85_50_N_mean.data - CCCmaCanRCM_b_N_mean.data + Obs_N.data)
    CCCmaSMHI85_50_N_mean = (CCCmaSMHI85_50_N_mean.data - CCCmaSMHI_b_N_mean.data + Obs_N.data)
    CNRM85_50_N_mean = (CNRM85_50_N_mean.data - CNRM_b_N_mean.data + Obs_N.data)
    CNRMSMHI85_50_N_mean = (CNRMSMHI85_50_N_mean.data - CNRMSMHI_b_N_mean.data + Obs_N.data)  
    CSIRO85_50_N_mean = (CSIRO85_50_N_mean.data - CSIRO_b_N_mean.data + Obs_N.data)
    ICHECDMI85_50_N_mean = (ICHECDMI85_50_N_mean.data - ICHECDMI_b_N_mean.data + Obs_N.data) 
    ICHECCCLM85_50_N_mean = (ICHECCCLM85_50_N_mean.data - ICHECCCLM_b_N_mean.data + Obs_N.data)
    ICHECKNMI85_50_N_mean = (ICHECKNMI85_50_N_mean.data - ICHECKNMI_b_N_mean.data + Obs_N.data)
    ICHECMPI85_50_N_mean = (ICHECMPI85_50_N_mean.data - ICHECMPI_b_N_mean.data + Obs_N.data)
    ICHECSMHI85_50_N_mean = (ICHECSMHI85_50_N_mean.data - ICHECSMHI_b_N_mean.data + Obs_N.data)
    
    
    #PART 5B: Central MALAWI
    #we are only interested in the latitude and longitude relevant to Central Malawi 
    Central_Malawi = iris.Constraint(longitude=lambda v: 32.5 <= v <= 35.5, latitude=lambda v: -15 <= v <= -11.5) 
    
    CCCmaCanRCM_past_C = CCCmaCanRCM_past.extract(Central_Malawi)
    CCCmaSMHI_past_C = CCCmaSMHI_past.extract(Central_Malawi)
    CNRM_past_C = CNRM_past.extract(Central_Malawi)
    CNRMSMHI_past_C = CNRMSMHI_past.extract(Central_Malawi)
    CSIRO_past_C = CSIRO_past.extract(Central_Malawi)
    ICHECDMI_past_C = ICHECDMI_past.extract(Central_Malawi)
    ICHECCCLM_past_C = ICHECCCLM_past.extract(Central_Malawi)
    ICHECKNMI_past_C = ICHECKNMI_past.extract(Central_Malawi)
    ICHECMPI_past_C = ICHECMPI_past.extract(Central_Malawi)
    ICHECSMHI_past_C = ICHECSMHI_past.extract(Central_Malawi)
    
    CCCmaCanRCM_30_C = CCCmaCanRCM_30.extract(Central_Malawi)
    CCCmaSMHI_30_C = CCCmaSMHI_30.extract(Central_Malawi)
    CNRM_30_C = CNRM_30.extract(Central_Malawi)
    CNRMSMHI_30_C = CNRMSMHI_30.extract(Central_Malawi)
    CSIRO_30_C = CSIRO_30.extract(Central_Malawi)
    ICHECDMI_30_C = ICHECDMI_30.extract(Central_Malawi)
    ICHECCCLM_30_C = ICHECCCLM_30.extract(Central_Malawi)
    ICHECKNMI_30_C = ICHECKNMI_30.extract(Central_Malawi)
    ICHECMPI_30_C = ICHECMPI_30.extract(Central_Malawi)
    ICHECSMHI_30_C = ICHECSMHI_30.extract(Central_Malawi)
    
    CCCmaCanRCM85_30_C = CCCmaCanRCM85_30.extract(Central_Malawi)
    CCCmaSMHI85_30_C = CCCmaSMHI85_30.extract(Central_Malawi)
    CNRM85_30_C = CNRM85_30.extract(Central_Malawi)
    CNRMSMHI85_30_C = CNRMSMHI85_30.extract(Central_Malawi)
    CSIRO85_30_C = CSIRO85_30.extract(Central_Malawi)
    ICHECDMI85_30_C = ICHECDMI85_30.extract(Central_Malawi)
    ICHECCCLM85_30_C = ICHECCCLM85_30.extract(Central_Malawi)
    ICHECKNMI85_30_C = ICHECKNMI85_30.extract(Central_Malawi)
    ICHECMPI85_30_C = ICHECMPI85_30.extract(Central_Malawi)
    ICHECSMHI85_30_C = ICHECSMHI85_30.extract(Central_Malawi)
    
    CCCmaCanRCM_50_C = CCCmaCanRCM_50.extract(Central_Malawi)
    CCCmaSMHI_50_C = CCCmaSMHI_50.extract(Central_Malawi)
    CNRM_50_C = CNRM_50.extract(Central_Malawi)
    CNRMSMHI_50_C = CNRMSMHI_50.extract(Central_Malawi)
    CSIRO_50_C = CSIRO_50.extract(Central_Malawi)
    ICHECDMI_50_C = ICHECDMI_50.extract(Central_Malawi)
    ICHECCCLM_50_C = ICHECCCLM_50.extract(Central_Malawi)
    ICHECKNMI_50_C = ICHECKNMI_50.extract(Central_Malawi)
    ICHECMPI_50_C = ICHECMPI_50.extract(Central_Malawi)
    ICHECSMHI_50_C = ICHECSMHI_50.extract(Central_Malawi)
    
    CCCmaCanRCM85_50_C = CCCmaCanRCM85_50.extract(Central_Malawi)
    CCCmaSMHI85_50_C = CCCmaSMHI85_50.extract(Central_Malawi)
    CNRM85_50_C = CNRM85_50.extract(Central_Malawi)
    CNRMSMHI85_50_C = CNRMSMHI85_50.extract(Central_Malawi)
    CSIRO85_50_C = CSIRO85_50.extract(Central_Malawi)
    ICHECDMI85_50_C = ICHECDMI85_50.extract(Central_Malawi)
    ICHECCCLM85_50_C = ICHECCCLM85_50.extract(Central_Malawi)
    ICHECKNMI85_50_C = ICHECKNMI85_50.extract(Central_Malawi)
    ICHECMPI85_50_C = ICHECMPI85_50.extract(Central_Malawi)
    ICHECSMHI85_50_C = ICHECSMHI85_50.extract(Central_Malawi)
    
    CRU_C = CRU.extract(Central_Malawi)
    
    #We are interested in plotting the data by date, so we need to take a mean of all the data by day of the year
    CCCmaCanRCM_past_C = CCCmaCanRCM_past_C.aggregated_by('day_of_year', iris.analysis.MEAN)
    CCCmaSMHI_past_C = CCCmaSMHI_past_C.aggregated_by('day_of_year', iris.analysis.MEAN)
    CNRM_past_C = CNRM_past_C.aggregated_by('day_of_year', iris.analysis.MEAN)
    CNRMSMHI_past_C = CNRMSMHI_past_C.aggregated_by('day_of_year', iris.analysis.MEAN)
    CSIRO_past_C = CSIRO_past_C.aggregated_by('day_of_year', iris.analysis.MEAN)
    ICHECDMI_past_C = ICHECDMI_past_C.aggregated_by('day_of_year', iris.analysis.MEAN)
    ICHECCCLM_past_C = ICHECCCLM_past_C.aggregated_by('day_of_year', iris.analysis.MEAN)
    ICHECKNMI_past_C = ICHECKNMI_past_C.aggregated_by('day_of_year', iris.analysis.MEAN)
    ICHECMPI_past_C = ICHECMPI_past_C.aggregated_by('day_of_year', iris.analysis.MEAN)
    ICHECSMHI_past_C = ICHECSMHI_past_C.aggregated_by('day_of_year', iris.analysis.MEAN)
    
    CCCmaCanRCM_30_C = CCCmaCanRCM_30_C.aggregated_by('day_of_year', iris.analysis.MEAN)
    CCCmaSMHI_30_C = CCCmaSMHI_30_C.aggregated_by('day_of_year', iris.analysis.MEAN)
    CNRM_30_C = CNRM_30_C.aggregated_by('day_of_year', iris.analysis.MEAN)
    CNRMSMHI_30_C = CNRMSMHI_30_C.aggregated_by('day_of_year', iris.analysis.MEAN)
    CSIRO_30_C = CSIRO_30_C.aggregated_by('day_of_year', iris.analysis.MEAN)
    ICHECDMI_30_C = ICHECDMI_30_C.aggregated_by('day_of_year', iris.analysis.MEAN)
    ICHECCCLM_30_C = ICHECCCLM_30_C.aggregated_by('day_of_year', iris.analysis.MEAN)
    ICHECKNMI_30_C = ICHECKNMI_30_C.aggregated_by('day_of_year', iris.analysis.MEAN)
    ICHECMPI_30_C = ICHECMPI_30_C.aggregated_by('day_of_year', iris.analysis.MEAN)
    ICHECSMHI_30_C = ICHECSMHI_30_C.aggregated_by('day_of_year', iris.analysis.MEAN)
    
    CCCmaCanRCM85_30_C = CCCmaCanRCM85_30_C.aggregated_by('day_of_year', iris.analysis.MEAN)
    CCCmaSMHI85_30_C = CCCmaSMHI85_30_C.aggregated_by('day_of_year', iris.analysis.MEAN)
    CNRM85_30_C = CNRM85_30_C.aggregated_by('day_of_year', iris.analysis.MEAN)
    CNRMSMHI85_30_C = CNRMSMHI85_30_C.aggregated_by('day_of_year', iris.analysis.MEAN)
    CSIRO85_30_C = CSIRO85_30_C.aggregated_by('day_of_year', iris.analysis.MEAN)
    ICHECDMI85_30_C = ICHECDMI85_30_C.aggregated_by('day_of_year', iris.analysis.MEAN)
    ICHECCCLM85_30_C = ICHECCCLM85_30_C.aggregated_by('day_of_year', iris.analysis.MEAN)
    ICHECKNMI85_30_C = ICHECKNMI85_30_C.aggregated_by('day_of_year', iris.analysis.MEAN)
    ICHECMPI85_30_C = ICHECMPI85_30_C.aggregated_by('day_of_year', iris.analysis.MEAN)
    ICHECSMHI85_30_C = ICHECSMHI85_30_C.aggregated_by('day_of_year', iris.analysis.MEAN)
    
    CCCmaCanRCM_50_C = CCCmaCanRCM_50_C.aggregated_by('day_of_year', iris.analysis.MEAN)
    CCCmaSMHI_50_C = CCCmaSMHI_50_C.aggregated_by('day_of_year', iris.analysis.MEAN)
    CNRM_50_C = CNRM_50_C.aggregated_by('day_of_year', iris.analysis.MEAN)
    CNRMSMHI_50_C = CNRMSMHI_50_C.aggregated_by('day_of_year', iris.analysis.MEAN)
    CSIRO_50_C = CSIRO_50_C.aggregated_by('day_of_year', iris.analysis.MEAN)
    ICHECDMI_50_C = ICHECDMI_50_C.aggregated_by('day_of_year', iris.analysis.MEAN)
    ICHECCCLM_50_C = ICHECCCLM_50_C.aggregated_by('day_of_year', iris.analysis.MEAN)
    ICHECKNMI_50_C = ICHECKNMI_50_C.aggregated_by('day_of_year', iris.analysis.MEAN)
    ICHECMPI_50_C = ICHECMPI_50_C.aggregated_by('day_of_year', iris.analysis.MEAN)
    ICHECSMHI_50_C = ICHECSMHI_50_C.aggregated_by('day_of_year', iris.analysis.MEAN)
    
    CCCmaCanRCM85_50_C = CCCmaCanRCM85_50_C.aggregated_by('day_of_year', iris.analysis.MEAN)
    CCCmaSMHI85_50_C = CCCmaSMHI85_50_C.aggregated_by('day_of_year', iris.analysis.MEAN)
    CNRM85_50_C = CNRM85_50_C.aggregated_by('day_of_year', iris.analysis.MEAN)
    CNRMSMHI85_50_C = CNRMSMHI85_50_C.aggregated_by('day_of_year', iris.analysis.MEAN)
    CSIRO85_50_C = CSIRO85_50_C.aggregated_by('day_of_year', iris.analysis.MEAN)
    ICHECDMI85_50_C = ICHECDMI85_50_C.aggregated_by('day_of_year', iris.analysis.MEAN)
    ICHECCCLM85_50_C = ICHECCCLM85_50_C.aggregated_by('day_of_year', iris.analysis.MEAN)
    ICHECKNMI85_50_C = ICHECKNMI85_50_C.aggregated_by('day_of_year', iris.analysis.MEAN)
    ICHECMPI85_50_C = ICHECMPI85_50_C.aggregated_by('day_of_year', iris.analysis.MEAN)
    ICHECSMHI85_50_C = ICHECSMHI85_50_C.aggregated_by('day_of_year', iris.analysis.MEAN)
    
    CRU_C = CRU_C.aggregated_by('day_of_year', iris.analysis.MEAN)
    
    #Returns an array of area weights, with the same dimensions as the cube
    CCCmaCanRCM_past_C_grid_areas = iris.analysis.cartography.area_weights(CCCmaCanRCM_past_C)
    CCCmaSMHI_past_C_grid_areas = iris.analysis.cartography.area_weights(CCCmaSMHI_past_C)
    CNRM_past_C_grid_areas = iris.analysis.cartography.area_weights(CNRM_past_C)
    CNRMSMHI_past_C_grid_areas = iris.analysis.cartography.area_weights(CNRMSMHI_past_C)
    CSIRO_past_C_grid_areas = iris.analysis.cartography.area_weights(CSIRO_past_C)
    ICHECDMI_past_C_grid_areas = iris.analysis.cartography.area_weights(ICHECDMI_past_C)
    ICHECCCLM_past_C_grid_areas = iris.analysis.cartography.area_weights(ICHECCCLM_past_C)
    ICHECKNMI_past_C_grid_areas = iris.analysis.cartography.area_weights(ICHECKNMI_past_C)
    ICHECMPI_past_C_grid_areas = iris.analysis.cartography.area_weights(ICHECMPI_past_C)
    ICHECSMHI_past_C_grid_areas = iris.analysis.cartography.area_weights(ICHECSMHI_past_C)
    
    CCCmaCanRCM_30_C_grid_areas = iris.analysis.cartography.area_weights(CCCmaCanRCM_30_C)
    CCCmaSMHI_30_C_grid_areas = iris.analysis.cartography.area_weights(CCCmaSMHI_30_C)
    CNRM_30_C_grid_areas = iris.analysis.cartography.area_weights(CNRM_30_C)
    CNRMSMHI_30_C_grid_areas = iris.analysis.cartography.area_weights(CNRMSMHI_30_C)
    CSIRO_30_C_grid_areas = iris.analysis.cartography.area_weights(CSIRO_30_C)
    ICHECDMI_30_C_grid_areas = iris.analysis.cartography.area_weights(ICHECDMI_30_C)
    ICHECCCLM_30_C_grid_areas = iris.analysis.cartography.area_weights(ICHECCCLM_30_C)
    ICHECKNMI_30_C_grid_areas = iris.analysis.cartography.area_weights(ICHECKNMI_30_C)
    ICHECMPI_30_C_grid_areas = iris.analysis.cartography.area_weights(ICHECMPI_30_C)
    ICHECSMHI_30_C_grid_areas = iris.analysis.cartography.area_weights(ICHECSMHI_30_C)
    
    CCCmaCanRCM85_30_C_grid_areas = iris.analysis.cartography.area_weights(CCCmaCanRCM85_30_C)
    CCCmaSMHI85_30_C_grid_areas = iris.analysis.cartography.area_weights(CCCmaSMHI85_30_C)
    CNRM85_30_C_grid_areas = iris.analysis.cartography.area_weights(CNRM85_30_C)
    CNRMSMHI85_30_C_grid_areas = iris.analysis.cartography.area_weights(CNRMSMHI85_30_C)
    CSIRO85_30_C_grid_areas = iris.analysis.cartography.area_weights(CSIRO85_30_C)
    ICHECDMI85_30_C_grid_areas = iris.analysis.cartography.area_weights(ICHECDMI85_30_C)
    ICHECCCLM85_30_C_grid_areas = iris.analysis.cartography.area_weights(ICHECCCLM85_30_C)
    ICHECKNMI85_30_C_grid_areas = iris.analysis.cartography.area_weights(ICHECKNMI85_30_C)
    ICHECMPI85_30_C_grid_areas = iris.analysis.cartography.area_weights(ICHECMPI85_30_C)
    ICHECSMHI85_30_C_grid_areas = iris.analysis.cartography.area_weights(ICHECSMHI85_30_C)
    
    CCCmaCanRCM_50_C_grid_areas = iris.analysis.cartography.area_weights(CCCmaCanRCM_50_C)
    CCCmaSMHI_50_C_grid_areas = iris.analysis.cartography.area_weights(CCCmaSMHI_50_C)
    CNRM_50_C_grid_areas = iris.analysis.cartography.area_weights(CNRM_50_C)
    CNRMSMHI_50_C_grid_areas = iris.analysis.cartography.area_weights(CNRMSMHI_50_C)
    CSIRO_50_C_grid_areas = iris.analysis.cartography.area_weights(CSIRO_50_C)
    ICHECDMI_50_C_grid_areas = iris.analysis.cartography.area_weights(ICHECDMI_50_C)
    ICHECCCLM_50_C_grid_areas = iris.analysis.cartography.area_weights(ICHECCCLM_50_C)
    ICHECKNMI_50_C_grid_areas = iris.analysis.cartography.area_weights(ICHECKNMI_50_C)
    ICHECMPI_50_C_grid_areas = iris.analysis.cartography.area_weights(ICHECMPI_50_C)
    ICHECSMHI_50_C_grid_areas = iris.analysis.cartography.area_weights(ICHECSMHI_50_C)
    
    CCCmaCanRCM85_50_C_grid_areas = iris.analysis.cartography.area_weights(CCCmaCanRCM85_50_C)
    CCCmaSMHI85_50_C_grid_areas = iris.analysis.cartography.area_weights(CCCmaSMHI85_50_C)
    CNRM85_50_C_grid_areas = iris.analysis.cartography.area_weights(CNRM85_50_C)
    CNRMSMHI85_50_C_grid_areas = iris.analysis.cartography.area_weights(CNRMSMHI85_50_C)
    CSIRO85_50_C_grid_areas = iris.analysis.cartography.area_weights(CSIRO85_50_C)
    ICHECDMI85_50_C_grid_areas = iris.analysis.cartography.area_weights(ICHECDMI85_50_C)
    ICHECCCLM85_50_C_grid_areas = iris.analysis.cartography.area_weights(ICHECCCLM85_50_C)
    ICHECKNMI85_50_C_grid_areas = iris.analysis.cartography.area_weights(ICHECKNMI85_50_C)
    ICHECMPI85_50_C_grid_areas = iris.analysis.cartography.area_weights(ICHECMPI85_50_C)
    ICHECSMHI85_50_C_grid_areas = iris.analysis.cartography.area_weights(ICHECSMHI85_50_C)
    
    CRU_C_grid_areas = iris.analysis.cartography.area_weights(CRU_C)
    
    #We want to plot the mean for the whole region so we need a mean of all the lats and lons
    CCCmaCanRCM_past_C_mean = CCCmaCanRCM_past_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CCCmaCanRCM_past_C_grid_areas) 
    CCCmaSMHI_past_C_mean = CCCmaSMHI_past_C.collapsed(['latitude', 'longitude'],iris.analysis.MEAN, weights=CCCmaSMHI_past_C_grid_areas)
    CNRM_past_C_mean = CNRM_past_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CNRM_past_C_grid_areas)                           
    CNRMSMHI_past_C_mean = CNRMSMHI_past_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CNRMSMHI_past_C_grid_areas)  
    CSIRO_past_C_mean = CSIRO_past_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CSIRO_past_C_grid_areas)
    ICHECDMI_past_C_mean = ICHECDMI_past_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECDMI_past_C_grid_areas) 
    ICHECCCLM_past_C_mean = ICHECCCLM_past_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECCCLM_past_C_grid_areas)
    ICHECKNMI_past_C_mean = ICHECKNMI_past_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECKNMI_past_C_grid_areas)
    ICHECMPI_past_C_mean = ICHECMPI_past_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECMPI_past_C_grid_areas)
    ICHECSMHI_past_C_mean = ICHECSMHI_past_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECSMHI_past_C_grid_areas)
    
    CCCmaCanRCM_30_C_mean = CCCmaCanRCM_30_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CCCmaCanRCM_30_C_grid_areas) 
    CCCmaSMHI_30_C_mean = CCCmaSMHI_30_C.collapsed(['latitude', 'longitude'],iris.analysis.MEAN, weights=CCCmaSMHI_30_C_grid_areas)
    CNRM_30_C_mean = CNRM_30_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CNRM_30_C_grid_areas)                           
    CNRMSMHI_30_C_mean = CNRMSMHI_30_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CNRMSMHI_30_C_grid_areas)  
    CSIRO_30_C_mean = CSIRO_30_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CSIRO_30_C_grid_areas)
    ICHECDMI_30_C_mean = ICHECDMI_30_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECDMI_30_C_grid_areas) 
    ICHECCCLM_30_C_mean = ICHECCCLM_30_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECCCLM_30_C_grid_areas)
    ICHECKNMI_30_C_mean = ICHECKNMI_30_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECKNMI_30_C_grid_areas)
    ICHECMPI_30_C_mean = ICHECMPI_30_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECMPI_30_C_grid_areas)
    ICHECSMHI_30_C_mean = ICHECSMHI_30_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECSMHI_30_C_grid_areas)
    
    CCCmaCanRCM85_30_C_mean = CCCmaCanRCM85_30_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CCCmaCanRCM85_30_C_grid_areas) 
    CCCmaSMHI85_30_C_mean = CCCmaSMHI85_30_C.collapsed(['latitude', 'longitude'],iris.analysis.MEAN, weights=CCCmaSMHI85_30_C_grid_areas)
    CNRM85_30_C_mean = CNRM85_30_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CNRM85_30_C_grid_areas)                           
    CNRMSMHI85_30_C_mean = CNRMSMHI85_30_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CNRMSMHI85_30_C_grid_areas)  
    CSIRO85_30_C_mean = CSIRO85_30_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CSIRO85_30_C_grid_areas)
    ICHECDMI85_30_C_mean = ICHECDMI85_30_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECDMI85_30_C_grid_areas) 
    ICHECCCLM85_30_C_mean = ICHECCCLM85_30_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECCCLM85_30_C_grid_areas)
    ICHECKNMI85_30_C_mean = ICHECKNMI85_30_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECKNMI85_30_C_grid_areas)
    ICHECMPI85_30_C_mean = ICHECMPI85_30_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECMPI85_30_C_grid_areas)
    ICHECSMHI85_30_C_mean = ICHECSMHI85_30_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECSMHI85_30_C_grid_areas)
    
    CCCmaCanRCM_50_C_mean = CCCmaCanRCM_50_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CCCmaCanRCM_50_C_grid_areas) 
    CCCmaSMHI_50_C_mean = CCCmaSMHI_50_C.collapsed(['latitude', 'longitude'],iris.analysis.MEAN, weights=CCCmaSMHI_50_C_grid_areas)
    CNRM_50_C_mean = CNRM_50_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CNRM_50_C_grid_areas)                           
    CNRMSMHI_50_C_mean = CNRMSMHI_50_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CNRMSMHI_50_C_grid_areas)  
    CSIRO_50_C_mean = CSIRO_50_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CSIRO_50_C_grid_areas)
    ICHECDMI_50_C_mean = ICHECDMI_50_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECDMI_50_C_grid_areas) 
    ICHECCCLM_50_C_mean = ICHECCCLM_50_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECCCLM_50_C_grid_areas)
    ICHECKNMI_50_C_mean = ICHECKNMI_50_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECKNMI_50_C_grid_areas)
    ICHECMPI_50_C_mean = ICHECMPI_50_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECMPI_50_C_grid_areas)
    ICHECSMHI_50_C_mean = ICHECSMHI_50_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECSMHI_50_C_grid_areas)
    
    CCCmaCanRCM85_50_C_mean = CCCmaCanRCM85_50_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CCCmaCanRCM85_50_C_grid_areas) 
    CCCmaSMHI85_50_C_mean = CCCmaSMHI85_50_C.collapsed(['latitude', 'longitude'],iris.analysis.MEAN, weights=CCCmaSMHI85_50_C_grid_areas)
    CNRM85_50_C_mean = CNRM85_50_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CNRM85_50_C_grid_areas)                           
    CNRMSMHI85_50_C_mean = CNRMSMHI85_50_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CNRMSMHI85_50_C_grid_areas)  
    CSIRO85_50_C_mean = CSIRO85_50_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CSIRO85_50_C_grid_areas)
    ICHECDMI85_50_C_mean = ICHECDMI85_50_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECDMI85_50_C_grid_areas) 
    ICHECCCLM85_50_C_mean = ICHECCCLM85_50_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECCCLM85_50_C_grid_areas)
    ICHECKNMI85_50_C_mean = ICHECKNMI85_50_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECKNMI85_50_C_grid_areas)
    ICHECMPI85_50_C_mean = ICHECMPI85_50_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECMPI85_50_C_grid_areas)
    ICHECSMHI85_50_C_mean = ICHECSMHI85_50_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECSMHI85_50_C_grid_areas)
    
    CRU_C_mean = CRU_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CRU_C_grid_areas)
    
    #for the baseline we don't need to average for each year, but the average for the whole time period, so collapse by time
    CCCmaCanRCM_b_C_mean = CCCmaCanRCM_past_C_mean.collapsed(['time'], iris.analysis.MEAN) 
    CCCmaSMHI_b_C_mean = CCCmaSMHI_past_C_mean.collapsed(['time'], iris.analysis.MEAN) 
    CNRM_b_C_mean = CNRM_past_C_mean.collapsed(['time'], iris.analysis.MEAN)                      
    CNRMSMHI_b_C_mean = CNRMSMHI_past_C_mean.collapsed(['time'], iris.analysis.MEAN)   
    CSIRO_b_C_mean = CSIRO_past_C_mean.collapsed(['time'], iris.analysis.MEAN)
    ICHECDMI_b_C_mean = ICHECDMI_past_C_mean.collapsed(['time'], iris.analysis.MEAN)  
    ICHECCCLM_b_C_mean = ICHECCCLM_past_C_mean.collapsed(['time'], iris.analysis.MEAN) 
    ICHECKNMI_b_C_mean = ICHECKNMI_past_C_mean.collapsed(['time'], iris.analysis.MEAN) 
    ICHECMPI_b_C_mean = ICHECMPI_past_C_mean.collapsed(['time'], iris.analysis.MEAN) 
    ICHECSMHI_b_C_mean = ICHECSMHI_past_C_mean.collapsed(['time'], iris.analysis.MEAN)  
    
    CRU_C_mean = CRU_C_mean.collapsed(['time'], iris.analysis.MEAN) 
    
    #create average of observed baseline data
    Obs_C = (CRU_C_mean)  
    
    #We want to see the change in temperature from the baseline
    CCCmaCanRCM_past_C_mean = (CCCmaCanRCM_past_C_mean.data - CCCmaCanRCM_b_C_mean.data + Obs_C.data)
    CCCmaSMHI_past_C_mean = (CCCmaSMHI_past_C_mean.data - CCCmaSMHI_b_C_mean.data + Obs_C.data)
    CNRM_past_C_mean = (CNRM_past_C_mean.data - CNRM_b_C_mean.data + Obs_C.data)
    CNRMSMHI_past_C_mean = (CNRMSMHI_past_C_mean.data - CNRMSMHI_b_C_mean.data + Obs_C.data)  
    CSIRO_past_C_mean = (CSIRO_past_C_mean.data - CSIRO_b_C_mean.data + Obs_C.data)
    ICHECDMI_past_C_mean = (ICHECDMI_past_C_mean.data - ICHECDMI_b_C_mean.data + Obs_C.data) 
    ICHECCCLM_past_C_mean = (ICHECCCLM_past_C_mean.data - ICHECCCLM_b_C_mean.data + Obs_C.data)
    ICHECKNMI_past_C_mean = (ICHECKNMI_past_C_mean.data - ICHECKNMI_b_C_mean.data + Obs_C.data)
    ICHECMPI_past_C_mean = (ICHECMPI_past_C_mean.data - ICHECMPI_b_C_mean.data + Obs_C.data)
    ICHECSMHI_past_C_mean = (ICHECSMHI_past_C_mean.data - ICHECSMHI_b_C_mean.data + Obs_C.data)
    
    CCCmaCanRCM_30_C_mean = (CCCmaCanRCM_30_C_mean.data - CCCmaCanRCM_b_C_mean.data + Obs_C.data)
    CCCmaSMHI_30_C_mean = (CCCmaSMHI_30_C_mean.data - CCCmaSMHI_b_C_mean.data + Obs_C.data)
    CNRM_30_C_mean = (CNRM_30_C_mean.data - CNRM_b_C_mean.data + Obs_C.data)
    CNRMSMHI_30_C_mean = (CNRMSMHI_30_C_mean.data - CNRMSMHI_b_C_mean.data + Obs_C.data)  
    CSIRO_30_C_mean = (CSIRO_30_C_mean.data - CSIRO_b_C_mean.data + Obs_C.data)
    ICHECDMI_30_C_mean = (ICHECDMI_30_C_mean.data - ICHECDMI_b_C_mean.data + Obs_C.data) 
    ICHECCCLM_30_C_mean = (ICHECCCLM_30_C_mean.data - ICHECCCLM_b_C_mean.data + Obs_C.data)
    ICHECKNMI_30_C_mean = (ICHECKNMI_30_C_mean.data - ICHECKNMI_b_C_mean.data + Obs_C.data)
    ICHECMPI_30_C_mean = (ICHECMPI_30_C_mean.data - ICHECMPI_b_C_mean.data + Obs_C.data)
    ICHECSMHI_30_C_mean = (ICHECSMHI_30_C_mean.data - ICHECSMHI_b_C_mean.data + Obs_C.data)
    
    CCCmaCanRCM85_30_C_mean = (CCCmaCanRCM85_30_C_mean.data - CCCmaCanRCM_b_C_mean.data + Obs_C.data)
    CCCmaSMHI85_30_C_mean = (CCCmaSMHI85_30_C_mean.data - CCCmaSMHI_b_C_mean.data + Obs_C.data)
    CNRM85_30_C_mean = (CNRM85_30_C_mean.data - CNRM_b_C_mean.data + Obs_C.data)
    CNRMSMHI85_30_C_mean = (CNRMSMHI85_30_C_mean.data - CNRMSMHI_b_C_mean.data + Obs_C.data)  
    CSIRO85_30_C_mean = (CSIRO85_30_C_mean.data - CSIRO_b_C_mean.data + Obs_C.data)
    ICHECDMI85_30_C_mean = (ICHECDMI85_30_C_mean.data - ICHECDMI_b_C_mean.data + Obs_C.data) 
    ICHECCCLM85_30_C_mean = (ICHECCCLM85_30_C_mean.data - ICHECCCLM_b_C_mean.data + Obs_C.data)
    ICHECKNMI85_30_C_mean = (ICHECKNMI85_30_C_mean.data - ICHECKNMI_b_C_mean.data + Obs_C.data)
    ICHECMPI85_30_C_mean = (ICHECMPI85_30_C_mean.data - ICHECMPI_b_C_mean.data + Obs_C.data)
    ICHECSMHI85_30_C_mean = (ICHECSMHI85_30_C_mean.data - ICHECSMHI_b_C_mean.data + Obs_C.data)
    
    CCCmaCanRCM_50_C_mean = (CCCmaCanRCM_50_C_mean.data - CCCmaCanRCM_b_C_mean.data + Obs_C.data)
    CCCmaSMHI_50_C_mean = (CCCmaSMHI_50_C_mean.data - CCCmaSMHI_b_C_mean.data + Obs_C.data)
    CNRM_50_C_mean = (CNRM_50_C_mean.data - CNRM_b_C_mean.data + Obs_C.data)
    CNRMSMHI_50_C_mean = (CNRMSMHI_50_C_mean.data - CNRMSMHI_b_C_mean.data + Obs_C.data)  
    CSIRO_50_C_mean = (CSIRO_50_C_mean.data - CSIRO_b_C_mean.data + Obs_C.data)
    ICHECDMI_50_C_mean = (ICHECDMI_50_C_mean.data - ICHECDMI_b_C_mean.data + Obs_C.data) 
    ICHECCCLM_50_C_mean = (ICHECCCLM_50_C_mean.data - ICHECCCLM_b_C_mean.data + Obs_C.data)
    ICHECKNMI_50_C_mean = (ICHECKNMI_50_C_mean.data - ICHECKNMI_b_C_mean.data + Obs_C.data)
    ICHECMPI_50_C_mean = (ICHECMPI_50_C_mean.data - ICHECMPI_b_C_mean.data + Obs_C.data)
    ICHECSMHI_50_C_mean = (ICHECSMHI_50_C_mean.data - ICHECSMHI_b_C_mean.data + Obs_C.data)
    
    CCCmaCanRCM85_50_C_mean = (CCCmaCanRCM85_50_C_mean.data - CCCmaCanRCM_b_C_mean.data + Obs_C.data)
    CCCmaSMHI85_50_C_mean = (CCCmaSMHI85_50_C_mean.data - CCCmaSMHI_b_C_mean.data + Obs_C.data)
    CNRM85_50_C_mean = (CNRM85_50_C_mean.data - CNRM_b_C_mean.data + Obs_C.data)
    CNRMSMHI85_50_C_mean = (CNRMSMHI85_50_C_mean.data - CNRMSMHI_b_C_mean.data + Obs_C.data)  
    CSIRO85_50_C_mean = (CSIRO85_50_C_mean.data - CSIRO_b_C_mean.data + Obs_C.data)
    ICHECDMI85_50_C_mean = (ICHECDMI85_50_C_mean.data - ICHECDMI_b_C_mean.data + Obs_C.data) 
    ICHECCCLM85_50_C_mean = (ICHECCCLM85_50_C_mean.data - ICHECCCLM_b_C_mean.data + Obs_C.data)
    ICHECKNMI85_50_C_mean = (ICHECKNMI85_50_C_mean.data - ICHECKNMI_b_C_mean.data + Obs_C.data)
    ICHECMPI85_50_C_mean = (ICHECMPI85_50_C_mean.data - ICHECMPI_b_C_mean.data + Obs_C.data)
    ICHECSMHI85_50_C_mean = (ICHECSMHI85_50_C_mean.data - ICHECSMHI_b_C_mean.data + Obs_C.data)
    
    
    #PART 5C: Southern MALAWI
    #we are only interested in the latitude and longitude relevant to Southern Malawi 
    Southern_Malawi = iris.Constraint(longitude=lambda v: 34 <= v <= 36.5, latitude=lambda v: -17.5 <= v <= -14) 
    
    CCCmaCanRCM_past_S = CCCmaCanRCM_past.extract(Southern_Malawi)
    CCCmaSMHI_past_S = CCCmaSMHI_past.extract(Southern_Malawi)
    CNRM_past_S = CNRM_past.extract(Southern_Malawi)
    CNRMSMHI_past_S = CNRMSMHI_past.extract(Southern_Malawi)
    CSIRO_past_S = CSIRO_past.extract(Southern_Malawi)
    ICHECDMI_past_S = ICHECDMI_past.extract(Southern_Malawi)
    ICHECCCLM_past_S = ICHECCCLM_past.extract(Southern_Malawi)
    ICHECKNMI_past_S = ICHECKNMI_past.extract(Southern_Malawi)
    ICHECMPI_past_S = ICHECMPI_past.extract(Southern_Malawi)
    ICHECSMHI_past_S = ICHECSMHI_past.extract(Southern_Malawi)
    
    CCCmaCanRCM_30_S = CCCmaCanRCM_30.extract(Southern_Malawi)
    CCCmaSMHI_30_S = CCCmaSMHI_30.extract(Southern_Malawi)
    CNRM_30_S = CNRM_30.extract(Southern_Malawi)
    CNRMSMHI_30_S = CNRMSMHI_30.extract(Southern_Malawi)
    CSIRO_30_S = CSIRO_30.extract(Southern_Malawi)
    ICHECDMI_30_S = ICHECDMI_30.extract(Southern_Malawi)
    ICHECCCLM_30_S = ICHECCCLM_30.extract(Southern_Malawi)
    ICHECKNMI_30_S = ICHECKNMI_30.extract(Southern_Malawi)
    ICHECMPI_30_S = ICHECMPI_30.extract(Southern_Malawi)
    ICHECSMHI_30_S = ICHECSMHI_30.extract(Southern_Malawi)
    
    CCCmaCanRCM85_30_S = CCCmaCanRCM85_30.extract(Southern_Malawi)
    CCCmaSMHI85_30_S = CCCmaSMHI85_30.extract(Southern_Malawi)
    CNRM85_30_S = CNRM85_30.extract(Southern_Malawi)
    CNRMSMHI85_30_S = CNRMSMHI85_30.extract(Southern_Malawi)
    CSIRO85_30_S = CSIRO85_30.extract(Southern_Malawi)
    ICHECDMI85_30_S = ICHECDMI85_30.extract(Southern_Malawi)
    ICHECCCLM85_30_S = ICHECCCLM85_30.extract(Southern_Malawi)
    ICHECKNMI85_30_S = ICHECKNMI85_30.extract(Southern_Malawi)
    ICHECMPI85_30_S = ICHECMPI85_30.extract(Southern_Malawi)
    ICHECSMHI85_30_S = ICHECSMHI85_30.extract(Southern_Malawi)
    
    CCCmaCanRCM_50_S = CCCmaCanRCM_50.extract(Southern_Malawi)
    CCCmaSMHI_50_S = CCCmaSMHI_50.extract(Southern_Malawi)
    CNRM_50_S = CNRM_50.extract(Southern_Malawi)
    CNRMSMHI_50_S = CNRMSMHI_50.extract(Southern_Malawi)
    CSIRO_50_S = CSIRO_50.extract(Southern_Malawi)
    ICHECDMI_50_S = ICHECDMI_50.extract(Southern_Malawi)
    ICHECCCLM_50_S = ICHECCCLM_50.extract(Southern_Malawi)
    ICHECKNMI_50_S = ICHECKNMI_50.extract(Southern_Malawi)
    ICHECMPI_50_S = ICHECMPI_50.extract(Southern_Malawi)
    ICHECSMHI_50_S = ICHECSMHI_50.extract(Southern_Malawi)
    
    CCCmaCanRCM85_50_S = CCCmaCanRCM85_50.extract(Southern_Malawi)
    CCCmaSMHI85_50_S = CCCmaSMHI85_50.extract(Southern_Malawi)
    CNRM85_50_S = CNRM85_50.extract(Southern_Malawi)
    CNRMSMHI85_50_S = CNRMSMHI85_50.extract(Southern_Malawi)
    CSIRO85_50_S = CSIRO85_50.extract(Southern_Malawi)
    ICHECDMI85_50_S = ICHECDMI85_50.extract(Southern_Malawi)
    ICHECCCLM85_50_S = ICHECCCLM85_50.extract(Southern_Malawi)
    ICHECKNMI85_50_S = ICHECKNMI85_50.extract(Southern_Malawi)
    ICHECMPI85_50_S = ICHECMPI85_50.extract(Southern_Malawi)
    ICHECSMHI85_50_S = ICHECSMHI85_50.extract(Southern_Malawi)
    
    CRU_S = CRU.extract(Southern_Malawi)
    
    #We are interested in plotting the data by date, so we need to take a mean of all the data by day of the year
    CCCmaCanRCM_past_S = CCCmaCanRCM_past_S.aggregated_by('day_of_year', iris.analysis.MEAN)
    CCCmaSMHI_past_S = CCCmaSMHI_past_S.aggregated_by('day_of_year', iris.analysis.MEAN)
    CNRM_past_S = CNRM_past_S.aggregated_by('day_of_year', iris.analysis.MEAN)
    CNRMSMHI_past_S = CNRMSMHI_past_S.aggregated_by('day_of_year', iris.analysis.MEAN)
    CSIRO_past_S = CSIRO_past_S.aggregated_by('day_of_year', iris.analysis.MEAN)
    ICHECDMI_past_S = ICHECDMI_past_S.aggregated_by('day_of_year', iris.analysis.MEAN)
    ICHECCCLM_past_S = ICHECCCLM_past_S.aggregated_by('day_of_year', iris.analysis.MEAN)
    ICHECKNMI_past_S = ICHECKNMI_past_S.aggregated_by('day_of_year', iris.analysis.MEAN)
    ICHECMPI_past_S = ICHECMPI_past_S.aggregated_by('day_of_year', iris.analysis.MEAN)
    ICHECSMHI_past_S = ICHECSMHI_past_S.aggregated_by('day_of_year', iris.analysis.MEAN)
    
    CCCmaCanRCM_30_S = CCCmaCanRCM_30_S.aggregated_by('day_of_year', iris.analysis.MEAN)
    CCCmaSMHI_30_S = CCCmaSMHI_30_S.aggregated_by('day_of_year', iris.analysis.MEAN)
    CNRM_30_S = CNRM_30_S.aggregated_by('day_of_year', iris.analysis.MEAN)
    CNRMSMHI_30_S = CNRMSMHI_30_S.aggregated_by('day_of_year', iris.analysis.MEAN)
    CSIRO_30_S = CSIRO_30_S.aggregated_by('day_of_year', iris.analysis.MEAN)
    ICHECDMI_30_S = ICHECDMI_30_S.aggregated_by('day_of_year', iris.analysis.MEAN)
    ICHECCCLM_30_S = ICHECCCLM_30_S.aggregated_by('day_of_year', iris.analysis.MEAN)
    ICHECKNMI_30_S = ICHECKNMI_30_S.aggregated_by('day_of_year', iris.analysis.MEAN)
    ICHECMPI_30_S = ICHECMPI_30_S.aggregated_by('day_of_year', iris.analysis.MEAN)
    ICHECSMHI_30_S = ICHECSMHI_30_S.aggregated_by('day_of_year', iris.analysis.MEAN)
    
    CCCmaCanRCM85_30_S = CCCmaCanRCM85_30_S.aggregated_by('day_of_year', iris.analysis.MEAN)
    CCCmaSMHI85_30_S = CCCmaSMHI85_30_S.aggregated_by('day_of_year', iris.analysis.MEAN)
    CNRM85_30_S = CNRM85_30_S.aggregated_by('day_of_year', iris.analysis.MEAN)
    CNRMSMHI85_30_S = CNRMSMHI85_30_S.aggregated_by('day_of_year', iris.analysis.MEAN)
    CSIRO85_30_S = CSIRO85_30_S.aggregated_by('day_of_year', iris.analysis.MEAN)
    ICHECDMI85_30_S = ICHECDMI85_30_S.aggregated_by('day_of_year', iris.analysis.MEAN)
    ICHECCCLM85_30_S = ICHECCCLM85_30_S.aggregated_by('day_of_year', iris.analysis.MEAN)
    ICHECKNMI85_30_S = ICHECKNMI85_30_S.aggregated_by('day_of_year', iris.analysis.MEAN)
    ICHECMPI85_30_S = ICHECMPI85_30_S.aggregated_by('day_of_year', iris.analysis.MEAN)
    ICHECSMHI85_30_S = ICHECSMHI85_30_S.aggregated_by('day_of_year', iris.analysis.MEAN)
    
    CCCmaCanRCM_50_S = CCCmaCanRCM_50_S.aggregated_by('day_of_year', iris.analysis.MEAN)
    CCCmaSMHI_50_S = CCCmaSMHI_50_S.aggregated_by('day_of_year', iris.analysis.MEAN)
    CNRM_50_S = CNRM_50_S.aggregated_by('day_of_year', iris.analysis.MEAN)
    CNRMSMHI_50_S = CNRMSMHI_50_S.aggregated_by('day_of_year', iris.analysis.MEAN)
    CSIRO_50_S = CSIRO_50_S.aggregated_by('day_of_year', iris.analysis.MEAN)
    ICHECDMI_50_S = ICHECDMI_50_S.aggregated_by('day_of_year', iris.analysis.MEAN)
    ICHECCCLM_50_S = ICHECCCLM_50_S.aggregated_by('day_of_year', iris.analysis.MEAN)
    ICHECKNMI_50_S = ICHECKNMI_50_S.aggregated_by('day_of_year', iris.analysis.MEAN)
    ICHECMPI_50_S = ICHECMPI_50_S.aggregated_by('day_of_year', iris.analysis.MEAN)
    ICHECSMHI_50_S = ICHECSMHI_50_S.aggregated_by('day_of_year', iris.analysis.MEAN)
    
    CCCmaCanRCM85_50_S = CCCmaCanRCM85_50_S.aggregated_by('day_of_year', iris.analysis.MEAN)
    CCCmaSMHI85_50_S = CCCmaSMHI85_50_S.aggregated_by('day_of_year', iris.analysis.MEAN)
    CNRM85_50_S = CNRM85_50_S.aggregated_by('day_of_year', iris.analysis.MEAN)
    CNRMSMHI85_50_S = CNRMSMHI85_50_S.aggregated_by('day_of_year', iris.analysis.MEAN)
    CSIRO85_50_S = CSIRO85_50_S.aggregated_by('day_of_year', iris.analysis.MEAN)
    ICHECDMI85_50_S = ICHECDMI85_50_S.aggregated_by('day_of_year', iris.analysis.MEAN)
    ICHECCCLM85_50_S = ICHECCCLM85_50_S.aggregated_by('day_of_year', iris.analysis.MEAN)
    ICHECKNMI85_50_S = ICHECKNMI85_50_S.aggregated_by('day_of_year', iris.analysis.MEAN)
    ICHECMPI85_50_S = ICHECMPI85_50_S.aggregated_by('day_of_year', iris.analysis.MEAN)
    ICHECSMHI85_50_S = ICHECSMHI85_50_S.aggregated_by('day_of_year', iris.analysis.MEAN)
    
    CRU_S = CRU_S.aggregated_by('day_of_year', iris.analysis.MEAN)
    
    #Returns an array of area weights, with the same dimensions as the cube
    CCCmaCanRCM_past_S_grid_areas = iris.analysis.cartography.area_weights(CCCmaCanRCM_past_S)
    CCCmaSMHI_past_S_grid_areas = iris.analysis.cartography.area_weights(CCCmaSMHI_past_S)
    CNRM_past_S_grid_areas = iris.analysis.cartography.area_weights(CNRM_past_S)
    CNRMSMHI_past_S_grid_areas = iris.analysis.cartography.area_weights(CNRMSMHI_past_S)
    CSIRO_past_S_grid_areas = iris.analysis.cartography.area_weights(CSIRO_past_S)
    ICHECDMI_past_S_grid_areas = iris.analysis.cartography.area_weights(ICHECDMI_past_S)
    ICHECCCLM_past_S_grid_areas = iris.analysis.cartography.area_weights(ICHECCCLM_past_S)
    ICHECKNMI_past_S_grid_areas = iris.analysis.cartography.area_weights(ICHECKNMI_past_S)
    ICHECMPI_past_S_grid_areas = iris.analysis.cartography.area_weights(ICHECMPI_past_S)
    ICHECSMHI_past_S_grid_areas = iris.analysis.cartography.area_weights(ICHECSMHI_past_S)
    
    CCCmaCanRCM_30_S_grid_areas = iris.analysis.cartography.area_weights(CCCmaCanRCM_30_S)
    CCCmaSMHI_30_S_grid_areas = iris.analysis.cartography.area_weights(CCCmaSMHI_30_S)
    CNRM_30_S_grid_areas = iris.analysis.cartography.area_weights(CNRM_30_S)
    CNRMSMHI_30_S_grid_areas = iris.analysis.cartography.area_weights(CNRMSMHI_30_S)
    CSIRO_30_S_grid_areas = iris.analysis.cartography.area_weights(CSIRO_30_S)
    ICHECDMI_30_S_grid_areas = iris.analysis.cartography.area_weights(ICHECDMI_30_S)
    ICHECCCLM_30_S_grid_areas = iris.analysis.cartography.area_weights(ICHECCCLM_30_S)
    ICHECKNMI_30_S_grid_areas = iris.analysis.cartography.area_weights(ICHECKNMI_30_S)
    ICHECMPI_30_S_grid_areas = iris.analysis.cartography.area_weights(ICHECMPI_30_S)
    ICHECSMHI_30_S_grid_areas = iris.analysis.cartography.area_weights(ICHECSMHI_30_S)
    
    CCCmaCanRCM85_30_S_grid_areas = iris.analysis.cartography.area_weights(CCCmaCanRCM85_30_S)
    CCCmaSMHI85_30_S_grid_areas = iris.analysis.cartography.area_weights(CCCmaSMHI85_30_S)
    CNRM85_30_S_grid_areas = iris.analysis.cartography.area_weights(CNRM85_30_S)
    CNRMSMHI85_30_S_grid_areas = iris.analysis.cartography.area_weights(CNRMSMHI85_30_S)
    CSIRO85_30_S_grid_areas = iris.analysis.cartography.area_weights(CSIRO85_30_S)
    ICHECDMI85_30_S_grid_areas = iris.analysis.cartography.area_weights(ICHECDMI85_30_S)
    ICHECCCLM85_30_S_grid_areas = iris.analysis.cartography.area_weights(ICHECCCLM85_30_S)
    ICHECKNMI85_30_S_grid_areas = iris.analysis.cartography.area_weights(ICHECKNMI85_30_S)
    ICHECMPI85_30_S_grid_areas = iris.analysis.cartography.area_weights(ICHECMPI85_30_S)
    ICHECSMHI85_30_S_grid_areas = iris.analysis.cartography.area_weights(ICHECSMHI85_30_S)
    
    CCCmaCanRCM_50_S_grid_areas = iris.analysis.cartography.area_weights(CCCmaCanRCM_50_S)
    CCCmaSMHI_50_S_grid_areas = iris.analysis.cartography.area_weights(CCCmaSMHI_50_S)
    CNRM_50_S_grid_areas = iris.analysis.cartography.area_weights(CNRM_50_S)
    CNRMSMHI_50_S_grid_areas = iris.analysis.cartography.area_weights(CNRMSMHI_50_S)
    CSIRO_50_S_grid_areas = iris.analysis.cartography.area_weights(CSIRO_50_S)
    ICHECDMI_50_S_grid_areas = iris.analysis.cartography.area_weights(ICHECDMI_50_S)
    ICHECCCLM_50_S_grid_areas = iris.analysis.cartography.area_weights(ICHECCCLM_50_S)
    ICHECKNMI_50_S_grid_areas = iris.analysis.cartography.area_weights(ICHECKNMI_50_S)
    ICHECMPI_50_S_grid_areas = iris.analysis.cartography.area_weights(ICHECMPI_50_S)
    ICHECSMHI_50_S_grid_areas = iris.analysis.cartography.area_weights(ICHECSMHI_50_S)
    
    CCCmaCanRCM85_50_S_grid_areas = iris.analysis.cartography.area_weights(CCCmaCanRCM85_50_S)
    CCCmaSMHI85_50_S_grid_areas = iris.analysis.cartography.area_weights(CCCmaSMHI85_50_S)
    CNRM85_50_S_grid_areas = iris.analysis.cartography.area_weights(CNRM85_50_S)
    CNRMSMHI85_50_S_grid_areas = iris.analysis.cartography.area_weights(CNRMSMHI85_50_S)
    CSIRO85_50_S_grid_areas = iris.analysis.cartography.area_weights(CSIRO85_50_S)
    ICHECDMI85_50_S_grid_areas = iris.analysis.cartography.area_weights(ICHECDMI85_50_S)
    ICHECCCLM85_50_S_grid_areas = iris.analysis.cartography.area_weights(ICHECCCLM85_50_S)
    ICHECKNMI85_50_S_grid_areas = iris.analysis.cartography.area_weights(ICHECKNMI85_50_S)
    ICHECMPI85_50_S_grid_areas = iris.analysis.cartography.area_weights(ICHECMPI85_50_S)
    ICHECSMHI85_50_S_grid_areas = iris.analysis.cartography.area_weights(ICHECSMHI85_50_S)
    
    CRU_S_grid_areas = iris.analysis.cartography.area_weights(CRU_S)
    
    #We want to plot the mean for the whole region so we need a mean of all the lats and lons
    CCCmaCanRCM_past_S_mean = CCCmaCanRCM_past_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CCCmaCanRCM_past_S_grid_areas) 
    CCCmaSMHI_past_S_mean = CCCmaSMHI_past_S.collapsed(['latitude', 'longitude'],iris.analysis.MEAN, weights=CCCmaSMHI_past_S_grid_areas)
    CNRM_past_S_mean = CNRM_past_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CNRM_past_S_grid_areas)                           
    CNRMSMHI_past_S_mean = CNRMSMHI_past_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CNRMSMHI_past_S_grid_areas)  
    CSIRO_past_S_mean = CSIRO_past_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CSIRO_past_S_grid_areas)
    ICHECDMI_past_S_mean = ICHECDMI_past_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECDMI_past_S_grid_areas) 
    ICHECCCLM_past_S_mean = ICHECCCLM_past_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECCCLM_past_S_grid_areas)
    ICHECKNMI_past_S_mean = ICHECKNMI_past_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECKNMI_past_S_grid_areas)
    ICHECMPI_past_S_mean = ICHECMPI_past_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECMPI_past_S_grid_areas)
    ICHECSMHI_past_S_mean = ICHECSMHI_past_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECSMHI_past_S_grid_areas)
    
    CCCmaCanRCM_30_S_mean = CCCmaCanRCM_30_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CCCmaCanRCM_30_S_grid_areas) 
    CCCmaSMHI_30_S_mean = CCCmaSMHI_30_S.collapsed(['latitude', 'longitude'],iris.analysis.MEAN, weights=CCCmaSMHI_30_S_grid_areas)
    CNRM_30_S_mean = CNRM_30_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CNRM_30_S_grid_areas)                           
    CNRMSMHI_30_S_mean = CNRMSMHI_30_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CNRMSMHI_30_S_grid_areas)  
    CSIRO_30_S_mean = CSIRO_30_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CSIRO_30_S_grid_areas)
    ICHECDMI_30_S_mean = ICHECDMI_30_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECDMI_30_S_grid_areas) 
    ICHECCCLM_30_S_mean = ICHECCCLM_30_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECCCLM_30_S_grid_areas)
    ICHECKNMI_30_S_mean = ICHECKNMI_30_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECKNMI_30_S_grid_areas)
    ICHECMPI_30_S_mean = ICHECMPI_30_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECMPI_30_S_grid_areas)
    ICHECSMHI_30_S_mean = ICHECSMHI_30_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECSMHI_30_S_grid_areas)
    
    CCCmaCanRCM85_30_S_mean = CCCmaCanRCM85_30_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CCCmaCanRCM85_30_S_grid_areas) 
    CCCmaSMHI85_30_S_mean = CCCmaSMHI85_30_S.collapsed(['latitude', 'longitude'],iris.analysis.MEAN, weights=CCCmaSMHI85_30_S_grid_areas)
    CNRM85_30_S_mean = CNRM85_30_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CNRM85_30_S_grid_areas)                           
    CNRMSMHI85_30_S_mean = CNRMSMHI85_30_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CNRMSMHI85_30_S_grid_areas)  
    CSIRO85_30_S_mean = CSIRO85_30_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CSIRO85_30_S_grid_areas)
    ICHECDMI85_30_S_mean = ICHECDMI85_30_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECDMI85_30_S_grid_areas) 
    ICHECCCLM85_30_S_mean = ICHECCCLM85_30_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECCCLM85_30_S_grid_areas)
    ICHECKNMI85_30_S_mean = ICHECKNMI85_30_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECKNMI85_30_S_grid_areas)
    ICHECMPI85_30_S_mean = ICHECMPI85_30_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECMPI85_30_S_grid_areas)
    ICHECSMHI85_30_S_mean = ICHECSMHI85_30_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECSMHI85_30_S_grid_areas)
    
    CCCmaCanRCM_50_S_mean = CCCmaCanRCM_50_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CCCmaCanRCM_50_S_grid_areas) 
    CCCmaSMHI_50_S_mean = CCCmaSMHI_50_S.collapsed(['latitude', 'longitude'],iris.analysis.MEAN, weights=CCCmaSMHI_50_S_grid_areas)
    CNRM_50_S_mean = CNRM_50_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CNRM_50_S_grid_areas)                           
    CNRMSMHI_50_S_mean = CNRMSMHI_50_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CNRMSMHI_50_S_grid_areas)  
    CSIRO_50_S_mean = CSIRO_50_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CSIRO_50_S_grid_areas)
    ICHECDMI_50_S_mean = ICHECDMI_50_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECDMI_50_S_grid_areas) 
    ICHECCCLM_50_S_mean = ICHECCCLM_50_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECCCLM_50_S_grid_areas)
    ICHECKNMI_50_S_mean = ICHECKNMI_50_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECKNMI_50_S_grid_areas)
    ICHECMPI_50_S_mean = ICHECMPI_50_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECMPI_50_S_grid_areas)
    ICHECSMHI_50_S_mean = ICHECSMHI_50_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECSMHI_50_S_grid_areas)
    
    CCCmaCanRCM85_50_S_mean = CCCmaCanRCM85_50_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CCCmaCanRCM85_50_S_grid_areas) 
    CCCmaSMHI85_50_S_mean = CCCmaSMHI85_50_S.collapsed(['latitude', 'longitude'],iris.analysis.MEAN, weights=CCCmaSMHI85_50_S_grid_areas)
    CNRM85_50_S_mean = CNRM85_50_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CNRM85_50_S_grid_areas)                           
    CNRMSMHI85_50_S_mean = CNRMSMHI85_50_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CNRMSMHI85_50_S_grid_areas)  
    CSIRO85_50_S_mean = CSIRO85_50_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CSIRO85_50_S_grid_areas)
    ICHECDMI85_50_S_mean = ICHECDMI85_50_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECDMI85_50_S_grid_areas) 
    ICHECCCLM85_50_S_mean = ICHECCCLM85_50_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECCCLM85_50_S_grid_areas)
    ICHECKNMI85_50_S_mean = ICHECKNMI85_50_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECKNMI85_50_S_grid_areas)
    ICHECMPI85_50_S_mean = ICHECMPI85_50_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECMPI85_50_S_grid_areas)
    ICHECSMHI85_50_S_mean = ICHECSMHI85_50_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECSMHI85_50_S_grid_areas)
    
    CRU_S_mean = CRU_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CRU_S_grid_areas)
    
    #for the baseline we don't need to average for each year, but the average for the whole time period, so collapse by time
    CCCmaCanRCM_b_S_mean = CCCmaCanRCM_past_S_mean.collapsed(['time'], iris.analysis.MEAN) 
    CCCmaSMHI_b_S_mean = CCCmaSMHI_past_S_mean.collapsed(['time'], iris.analysis.MEAN) 
    CNRM_b_S_mean = CNRM_past_S_mean.collapsed(['time'], iris.analysis.MEAN)                      
    CNRMSMHI_b_S_mean = CNRMSMHI_past_S_mean.collapsed(['time'], iris.analysis.MEAN)   
    CSIRO_b_S_mean = CSIRO_past_S_mean.collapsed(['time'], iris.analysis.MEAN)
    ICHECDMI_b_S_mean = ICHECDMI_past_S_mean.collapsed(['time'], iris.analysis.MEAN)  
    ICHECCCLM_b_S_mean = ICHECCCLM_past_S_mean.collapsed(['time'], iris.analysis.MEAN) 
    ICHECKNMI_b_S_mean = ICHECKNMI_past_S_mean.collapsed(['time'], iris.analysis.MEAN) 
    ICHECMPI_b_S_mean = ICHECMPI_past_S_mean.collapsed(['time'], iris.analysis.MEAN) 
    ICHECSMHI_b_S_mean = ICHECSMHI_past_S_mean.collapsed(['time'], iris.analysis.MEAN)  
    
    CRU_S_mean = CRU_S_mean.collapsed(['time'], iris.analysis.MEAN) 
    
    #create average of observed baseline data
    Obs_S = (CRU_S_mean)  
    
    #We want to see the change in temperature from the baseline
    CCCmaCanRCM_past_S_mean = (CCCmaCanRCM_past_S_mean.data - CCCmaCanRCM_b_S_mean.data + Obs_S.data)
    CCCmaSMHI_past_S_mean = (CCCmaSMHI_past_S_mean.data - CCCmaSMHI_b_S_mean.data + Obs_S.data)
    CNRM_past_S_mean = (CNRM_past_S_mean.data - CNRM_b_S_mean.data + Obs_S.data)
    CNRMSMHI_past_S_mean = (CNRMSMHI_past_S_mean.data - CNRMSMHI_b_S_mean.data + Obs_S.data)  
    CSIRO_past_S_mean = (CSIRO_past_S_mean.data - CSIRO_b_S_mean.data + Obs_S.data)
    ICHECDMI_past_S_mean = (ICHECDMI_past_S_mean.data - ICHECDMI_b_S_mean.data + Obs_S.data) 
    ICHECCCLM_past_S_mean = (ICHECCCLM_past_S_mean.data - ICHECCCLM_b_S_mean.data + Obs_S.data)
    ICHECKNMI_past_S_mean = (ICHECKNMI_past_S_mean.data - ICHECKNMI_b_S_mean.data + Obs_S.data)
    ICHECMPI_past_S_mean = (ICHECMPI_past_S_mean.data - ICHECMPI_b_S_mean.data + Obs_S.data)
    ICHECSMHI_past_S_mean = (ICHECSMHI_past_S_mean.data - ICHECSMHI_b_S_mean.data + Obs_S.data)
    
    CCCmaCanRCM_30_S_mean = (CCCmaCanRCM_30_S_mean.data - CCCmaCanRCM_b_S_mean.data + Obs_S.data)
    CCCmaSMHI_30_S_mean = (CCCmaSMHI_30_S_mean.data - CCCmaSMHI_b_S_mean.data + Obs_S.data)
    CNRM_30_S_mean = (CNRM_30_S_mean.data - CNRM_b_S_mean.data + Obs_S.data)
    CNRMSMHI_30_S_mean = (CNRMSMHI_30_S_mean.data - CNRMSMHI_b_S_mean.data + Obs_S.data)  
    CSIRO_30_S_mean = (CSIRO_30_S_mean.data - CSIRO_b_S_mean.data + Obs_S.data)
    ICHECDMI_30_S_mean = (ICHECDMI_30_S_mean.data - ICHECDMI_b_S_mean.data + Obs_S.data) 
    ICHECCCLM_30_S_mean = (ICHECCCLM_30_S_mean.data - ICHECCCLM_b_S_mean.data + Obs_S.data)
    ICHECKNMI_30_S_mean = (ICHECKNMI_30_S_mean.data - ICHECKNMI_b_S_mean.data + Obs_S.data)
    ICHECMPI_30_S_mean = (ICHECMPI_30_S_mean.data - ICHECMPI_b_S_mean.data + Obs_S.data)
    ICHECSMHI_30_S_mean = (ICHECSMHI_30_S_mean.data - ICHECSMHI_b_S_mean.data + Obs_S.data)
    
    CCCmaCanRCM85_30_S_mean = (CCCmaCanRCM85_30_S_mean.data - CCCmaCanRCM_b_S_mean.data + Obs_S.data)
    CCCmaSMHI85_30_S_mean = (CCCmaSMHI85_30_S_mean.data - CCCmaSMHI_b_S_mean.data + Obs_S.data)
    CNRM85_30_S_mean = (CNRM85_30_S_mean.data - CNRM_b_S_mean.data + Obs_S.data)
    CNRMSMHI85_30_S_mean = (CNRMSMHI85_30_S_mean.data - CNRMSMHI_b_S_mean.data + Obs_S.data)  
    CSIRO85_30_S_mean = (CSIRO85_30_S_mean.data - CSIRO_b_S_mean.data + Obs_S.data)
    ICHECDMI85_30_S_mean = (ICHECDMI85_30_S_mean.data - ICHECDMI_b_S_mean.data + Obs_S.data) 
    ICHECCCLM85_30_S_mean = (ICHECCCLM85_30_S_mean.data - ICHECCCLM_b_S_mean.data + Obs_S.data)
    ICHECKNMI85_30_S_mean = (ICHECKNMI85_30_S_mean.data - ICHECKNMI_b_S_mean.data + Obs_S.data)
    ICHECMPI85_30_S_mean = (ICHECMPI85_30_S_mean.data - ICHECMPI_b_S_mean.data + Obs_S.data)
    ICHECSMHI85_30_S_mean = (ICHECSMHI85_30_S_mean.data - ICHECSMHI_b_S_mean.data + Obs_S.data)
    
    CCCmaCanRCM_50_S_mean = (CCCmaCanRCM_50_S_mean.data - CCCmaCanRCM_b_S_mean.data + Obs_S.data)
    CCCmaSMHI_50_S_mean = (CCCmaSMHI_50_S_mean.data - CCCmaSMHI_b_S_mean.data + Obs_S.data)
    CNRM_50_S_mean = (CNRM_50_S_mean.data - CNRM_b_S_mean.data + Obs_S.data)
    CNRMSMHI_50_S_mean = (CNRMSMHI_50_S_mean.data - CNRMSMHI_b_S_mean.data + Obs_S.data)  
    CSIRO_50_S_mean = (CSIRO_50_S_mean.data - CSIRO_b_S_mean.data + Obs_S.data)
    ICHECDMI_50_S_mean = (ICHECDMI_50_S_mean.data - ICHECDMI_b_S_mean.data + Obs_S.data) 
    ICHECCCLM_50_S_mean = (ICHECCCLM_50_S_mean.data - ICHECCCLM_b_S_mean.data + Obs_S.data)
    ICHECKNMI_50_S_mean = (ICHECKNMI_50_S_mean.data - ICHECKNMI_b_S_mean.data + Obs_S.data)
    ICHECMPI_50_S_mean = (ICHECMPI_50_S_mean.data - ICHECMPI_b_S_mean.data + Obs_S.data)
    ICHECSMHI_50_S_mean = (ICHECSMHI_50_S_mean.data - ICHECSMHI_b_S_mean.data + Obs_S.data)
    
    CCCmaCanRCM85_50_S_mean = (CCCmaCanRCM85_50_S_mean.data - CCCmaCanRCM_b_S_mean.data + Obs_S.data)
    CCCmaSMHI85_50_S_mean = (CCCmaSMHI85_50_S_mean.data - CCCmaSMHI_b_S_mean.data + Obs_S.data)
    CNRM85_50_S_mean = (CNRM85_50_S_mean.data - CNRM_b_S_mean.data + Obs_S.data)
    CNRMSMHI85_50_S_mean = (CNRMSMHI85_50_S_mean.data - CNRMSMHI_b_S_mean.data + Obs_S.data)  
    CSIRO85_50_S_mean = (CSIRO85_50_S_mean.data - CSIRO_b_S_mean.data + Obs_S.data)
    ICHECDMI85_50_S_mean = (ICHECDMI85_50_S_mean.data - ICHECDMI_b_S_mean.data + Obs_S.data) 
    ICHECCCLM85_50_S_mean = (ICHECCCLM85_50_S_mean.data - ICHECCCLM_b_S_mean.data + Obs_S.data)
    ICHECKNMI85_50_S_mean = (ICHECKNMI85_50_S_mean.data - ICHECKNMI_b_S_mean.data + Obs_S.data)
    ICHECMPI85_50_S_mean = (ICHECMPI85_50_S_mean.data - ICHECMPI_b_S_mean.data + Obs_S.data)
    ICHECSMHI85_50_S_mean = (ICHECSMHI85_50_S_mean.data - ICHECSMHI_b_S_mean.data + Obs_S.data)
    
    
    #-------------------------------------------------------------------------
    #PART 6: PRINT DATA
    import csv
    with open('output_AquaCrop_Data_TasmaxA.csv', 'wb') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        
        writer.writerow(['Parameter', 'Means'])
        
        #PART 6A: WRITE NORTHERN DATA
        writer.writerow(["CCCmaCanRCM_past_N_mean"] + CCCmaCanRCM_past_N_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["CCCmaSMHI_past_N_mean"] + CCCmaSMHI_past_N_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["CNRM_past_N_mean"] + CNRM_past_N_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["CNRMSMHI_past_N_mean"] +CNRMSMHI_past_N_mean.data.flatten().astype(np.str).tolist())   
        writer.writerow(["CSIRO_past_N_mean"] +CSIRO_past_N_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["ICHECDMI_past_N_mean"] +ICHECDMI_past_N_mean.data.flatten().astype(np.str).tolist())       
        writer.writerow(["ICHECCCLM_past_N_mean"] +ICHECCCLM_past_N_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["ICHECKNMI_past_N_mean"] +ICHECKNMI_past_N_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["ICHECMPI_past_N_mean"] +ICHECMPI_past_N_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["ICHECSMHI_past_N_mean"] +ICHECSMHI_past_N_mean.data.flatten().astype(np.str).tolist())
        
        writer.writerow(["CCCmaCanRCM_30_N_mean"] + CCCmaCanRCM_30_N_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["CCCmaSMHI_30_N_mean"] + CCCmaSMHI_30_N_mean.data.flatten().astype(np.str).tolist())  
        writer.writerow(["CNRM_30_N_mean"] + CNRM_30_N_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["CNRMSMHI_30_N_mean"] +CNRMSMHI_30_N_mean.data.flatten().astype(np.str).tolist())   
        writer.writerow(["CSIRO_30_N_mean"] +CSIRO_30_N_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["ICHECDMI_30_N_mean"] +ICHECDMI_30_N_mean.data.flatten().astype(np.str).tolist())       
        writer.writerow(["ICHECCCLM_30_N_mean"] +ICHECCCLM_30_N_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["ICHECKNMI_30_N_mean"] +ICHECKNMI_30_N_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["ICHECMPI_30_N_mean"] +ICHECMPI_30_N_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["ICHECSMHI_30_N_mean"] +ICHECSMHI_30_N_mean.data.flatten().astype(np.str).tolist())
        
        writer.writerow(["CCCmaCanRCM85_30_N_mean"] + CCCmaCanRCM85_30_N_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["CCCmaSMHI85_30_N_mean"] + CCCmaSMHI85_30_N_mean.data.flatten().astype(np.str).tolist())           
        writer.writerow(["CNRM85_30_N_mean"] + CNRM85_30_N_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["CNRMSMHI85_30_N_mean"] +CNRMSMHI85_30_N_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["CSIRO85_30_N_mean"] +CSIRO85_30_N_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["ICHECDMI85_30_N_mean"] +ICHECDMI85_30_N_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["ICHECCCLM85_30_N_mean"] +ICHECCCLM85_30_N_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["ICHECKNMI85_30_N_mean"] +ICHECKNMI85_30_N_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["ICHECMPI85_30_N_mean"] +ICHECMPI85_30_N_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["ICHECSMHI85_30_N_mean"] +ICHECSMHI85_30_N_mean.data.flatten().astype(np.str).tolist())
        
        writer.writerow(["CCCmaCanRCM_50_N_mean"] + CCCmaCanRCM_50_N_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["CCCmaSMHI_50_N_mean"] + CCCmaSMHI_50_N_mean.data.flatten().astype(np.str).tolist())  
        writer.writerow(["CNRM_50_N_mean"] + CNRM_50_N_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["CNRMSMHI_50_N_mean"] +CNRMSMHI_50_N_mean.data.flatten().astype(np.str).tolist())   
        writer.writerow(["CSIRO_50_N_mean"] +CSIRO_50_N_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["ICHECDMI_50_N_mean"] +ICHECDMI_50_N_mean.data.flatten().astype(np.str).tolist())       
        writer.writerow(["ICHECCCLM_50_N_mean"] +ICHECCCLM_50_N_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["ICHECKNMI_50_N_mean"] +ICHECKNMI_50_N_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["ICHECMPI_50_N_mean"] +ICHECMPI_50_N_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["ICHECSMHI_50_N_mean"] +ICHECSMHI_50_N_mean.data.flatten().astype(np.str).tolist())
        
        writer.writerow(["CCCmaCanRCM85_50_N_mean"] + CCCmaCanRCM85_50_N_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["CCCmaSMHI85_50_N_mean"] + CCCmaSMHI85_50_N_mean.data.flatten().astype(np.str).tolist())           
        writer.writerow(["CNRM85_50_N_mean"] + CNRM85_50_N_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["CNRMSMHI85_50_N_mean"] +CNRMSMHI85_50_N_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["CSIRO85_50_N_mean"] +CSIRO85_50_N_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["ICHECDMI85_50_N_mean"] +ICHECDMI85_50_N_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["ICHECCCLM85_50_N_mean"] +ICHECCCLM85_50_N_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["ICHECKNMI85_50_N_mean"] +ICHECKNMI85_50_N_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["ICHECMPI85_50_N_mean"] +ICHECMPI85_50_N_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["ICHECSMHI85_50_N_mean"] +ICHECSMHI85_50_N_mean.data.flatten().astype(np.str).tolist())
        
    #PART 6B: WRITE CENTRAL DATA
        writer.writerow(["CCCmaCanRCM_past_C_mean"] + CCCmaCanRCM_past_C_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["CCCmaSMHI_past_C_mean"] + CCCmaSMHI_past_C_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["CNRM_past_C_mean"] + CNRM_past_C_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["CNRMSMHI_past_C_mean"] +CNRMSMHI_past_C_mean.data.flatten().astype(np.str).tolist())   
        writer.writerow(["CSIRO_past_C_mean"] +CSIRO_past_C_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["ICHECDMI_past_C_mean"] +ICHECDMI_past_C_mean.data.flatten().astype(np.str).tolist())       
        writer.writerow(["ICHECCCLM_past_C_mean"] +ICHECCCLM_past_C_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["ICHECKNMI_past_C_mean"] +ICHECKNMI_past_C_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["ICHECMPI_past_C_mean"] +ICHECMPI_past_C_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["ICHECSMHI_past_C_mean"] +ICHECSMHI_past_C_mean.data.flatten().astype(np.str).tolist())
        
        writer.writerow(["CCCmaCanRCM_30_C_mean"] + CCCmaCanRCM_30_C_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["CCCmaSMHI_30_C_mean"] + CCCmaSMHI_30_C_mean.data.flatten().astype(np.str).tolist())  
        writer.writerow(["CNRM_30_C_mean"] + CNRM_30_C_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["CNRMSMHI_30_C_mean"] +CNRMSMHI_30_C_mean.data.flatten().astype(np.str).tolist())   
        writer.writerow(["CSIRO_30_C_mean"] +CSIRO_30_C_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["ICHECDMI_30_C_mean"] +ICHECDMI_30_C_mean.data.flatten().astype(np.str).tolist())       
        writer.writerow(["ICHECCCLM_30_C_mean"] +ICHECCCLM_30_C_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["ICHECKNMI_30_C_mean"] +ICHECKNMI_30_C_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["ICHECMPI_30_C_mean"] +ICHECMPI_30_C_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["ICHECSMHI_30_C_mean"] +ICHECSMHI_30_C_mean.data.flatten().astype(np.str).tolist())
        
        writer.writerow(["CCCmaCanRCM85_30_C_mean"] + CCCmaCanRCM85_30_C_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["CCCmaSMHI85_30_C_mean"] + CCCmaSMHI85_30_C_mean.data.flatten().astype(np.str).tolist())           
        writer.writerow(["CNRM85_30_C_mean"] + CNRM85_30_C_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["CNRMSMHI85_30_C_mean"] +CNRMSMHI85_30_C_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["CSIRO85_30_C_mean"] +CSIRO85_30_C_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["ICHECDMI85_30_C_mean"] +ICHECDMI85_30_C_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["ICHECCCLM85_30_C_mean"] +ICHECCCLM85_30_C_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["ICHECKNMI85_30_C_mean"] +ICHECKNMI85_30_C_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["ICHECMPI85_30_C_mean"] +ICHECMPI85_30_C_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["ICHECSMHI85_30_C_mean"] +ICHECSMHI85_30_C_mean.data.flatten().astype(np.str).tolist())
        
        writer.writerow(["CCCmaCanRCM_50_C_mean"] + CCCmaCanRCM_50_C_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["CCCmaSMHI_50_C_mean"] + CCCmaSMHI_50_C_mean.data.flatten().astype(np.str).tolist())  
        writer.writerow(["CNRM_50_C_mean"] + CNRM_50_C_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["CNRMSMHI_50_C_mean"] +CNRMSMHI_50_C_mean.data.flatten().astype(np.str).tolist())   
        writer.writerow(["CSIRO_50_C_mean"] +CSIRO_50_C_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["ICHECDMI_50_C_mean"] +ICHECDMI_50_C_mean.data.flatten().astype(np.str).tolist())       
        writer.writerow(["ICHECCCLM_50_C_mean"] +ICHECCCLM_50_C_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["ICHECKNMI_50_C_mean"] +ICHECKNMI_50_C_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["ICHECMPI_50_C_mean"] +ICHECMPI_50_C_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["ICHECSMHI_50_C_mean"] +ICHECSMHI_50_C_mean.data.flatten().astype(np.str).tolist())
        
        writer.writerow(["CCCmaCanRCM85_50_C_mean"] + CCCmaCanRCM85_50_C_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["CCCmaSMHI85_50_C_mean"] + CCCmaSMHI85_50_C_mean.data.flatten().astype(np.str).tolist())           
        writer.writerow(["CNRM85_50_C_mean"] + CNRM85_50_C_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["CNRMSMHI85_50_C_mean"] +CNRMSMHI85_50_C_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["CSIRO85_50_C_mean"] +CSIRO85_50_C_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["ICHECDMI85_50_C_mean"] +ICHECDMI85_50_C_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["ICHECCCLM85_50_C_mean"] +ICHECCCLM85_50_C_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["ICHECKNMI85_50_C_mean"] +ICHECKNMI85_50_C_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["ICHECMPI85_50_C_mean"] +ICHECMPI85_50_C_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["ICHECSMHI85_50_C_mean"] +ICHECSMHI85_50_C_mean.data.flatten().astype(np.str).tolist())
        
    #PART 6C: WRITE SOUTHERN DATA
        writer.writerow(["CCCmaCanRCM_past_S_mean"] + CCCmaCanRCM_past_S_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["CCCmaSMHI_past_S_mean"] + CCCmaSMHI_past_S_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["CNRM_past_S_mean"] + CNRM_past_S_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["CNRMSMHI_past_S_mean"] +CNRMSMHI_past_S_mean.data.flatten().astype(np.str).tolist())   
        writer.writerow(["CSIRO_past_S_mean"] +CSIRO_past_S_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["ICHECDMI_past_S_mean"] +ICHECDMI_past_S_mean.data.flatten().astype(np.str).tolist())       
        writer.writerow(["ICHECCCLM_past_S_mean"] +ICHECCCLM_past_S_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["ICHECKNMI_past_S_mean"] +ICHECKNMI_past_S_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["ICHECMPI_past_S_mean"] +ICHECMPI_past_S_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["ICHECSMHI_past_S_mean"] +ICHECSMHI_past_S_mean.data.flatten().astype(np.str).tolist())
        
        writer.writerow(["CCCmaCanRCM_30_S_mean"] + CCCmaCanRCM_30_S_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["CCCmaSMHI_30_S_mean"] + CCCmaSMHI_30_S_mean.data.flatten().astype(np.str).tolist())  
        writer.writerow(["CNRM_30_S_mean"] + CNRM_30_S_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["CNRMSMHI_30_S_mean"] +CNRMSMHI_30_S_mean.data.flatten().astype(np.str).tolist())   
        writer.writerow(["CSIRO_30_S_mean"] +CSIRO_30_S_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["ICHECDMI_30_S_mean"] +ICHECDMI_30_S_mean.data.flatten().astype(np.str).tolist())       
        writer.writerow(["ICHECCCLM_30_S_mean"] +ICHECCCLM_30_S_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["ICHECKNMI_30_S_mean"] +ICHECKNMI_30_S_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["ICHECMPI_30_S_mean"] +ICHECMPI_30_S_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["ICHECSMHI_30_S_mean"] +ICHECSMHI_30_S_mean.data.flatten().astype(np.str).tolist())
        
        writer.writerow(["CCCmaCanRCM85_30_S_mean"] + CCCmaCanRCM85_30_S_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["CCCmaSMHI85_30_S_mean"] + CCCmaSMHI85_30_S_mean.data.flatten().astype(np.str).tolist())           
        writer.writerow(["CNRM85_30_S_mean"] + CNRM85_30_S_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["CNRMSMHI85_30_S_mean"] +CNRMSMHI85_30_S_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["CSIRO85_30_S_mean"] +CSIRO85_30_S_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["ICHECDMI85_30_S_mean"] +ICHECDMI85_30_S_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["ICHECCCLM85_30_S_mean"] +ICHECCCLM85_30_S_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["ICHECKNMI85_30_S_mean"] +ICHECKNMI85_30_S_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["ICHECMPI85_30_S_mean"] +ICHECMPI85_30_S_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["ICHECSMHI85_30_S_mean"] +ICHECSMHI85_30_S_mean.data.flatten().astype(np.str).tolist())
        
        writer.writerow(["CCCmaCanRCM_50_S_mean"] + CCCmaCanRCM_50_S_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["CCCmaSMHI_50_S_mean"] + CCCmaSMHI_50_S_mean.data.flatten().astype(np.str).tolist())  
        writer.writerow(["CNRM_50_S_mean"] + CNRM_50_S_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["CNRMSMHI_50_S_mean"] +CNRMSMHI_50_S_mean.data.flatten().astype(np.str).tolist())   
        writer.writerow(["CSIRO_50_S_mean"] +CSIRO_50_S_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["ICHECDMI_50_S_mean"] +ICHECDMI_50_S_mean.data.flatten().astype(np.str).tolist())       
        writer.writerow(["ICHECCCLM_50_S_mean"] +ICHECCCLM_50_S_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["ICHECKNMI_50_S_mean"] +ICHECKNMI_50_S_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["ICHECMPI_50_S_mean"] +ICHECMPI_50_S_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["ICHECSMHI_50_S_mean"] +ICHECSMHI_50_S_mean.data.flatten().astype(np.str).tolist())
        
        writer.writerow(["CCCmaCanRCM85_50_S_mean"] + CCCmaCanRCM85_50_S_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["CCCmaSMHI85_50_S_mean"] + CCCmaSMHI85_50_S_mean.data.flatten().astype(np.str).tolist())           
        writer.writerow(["CNRM85_50_S_mean"] + CNRM85_50_S_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["CNRMSMHI85_50_S_mean"] +CNRMSMHI85_50_S_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["CSIRO85_50_S_mean"] +CSIRO85_50_S_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["ICHECDMI85_50_S_mean"] +ICHECDMI85_50_S_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["ICHECCCLM85_50_S_mean"] +ICHECCCLM85_50_S_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["ICHECKNMI85_50_S_mean"] +ICHECKNMI85_50_S_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["ICHECMPI85_50_S_mean"] +ICHECMPI85_50_S_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["ICHECSMHI85_50_S_mean"] +ICHECSMHI85_50_S_mean.data.flatten().astype(np.str).tolist())
        
if __name__ == '__main__':
    main()     
    
    