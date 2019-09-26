"""
Created on Monday June 27th 2019

@author: s0899345
"""

import numpy as np
import iris
import iris.coord_categorisation as iriscc
import iris.analysis.cartography
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
    
    #PART 1: LOAD and FORMAT PAST MODELS 
    CCCmaCanRCM_past = '/exports/csce/datastore/geos/users/s0899345/AFR_44_tas/Historical_daily/tas_AFR-44_CCCma-CanESM2_historical_r1i1p1_CCCma-CanRCM4_r2_day_19710101-20001231.nc'
    CCCmaSMHI_past = '/exports/csce/datastore/geos/users/s0899345/AFR_44_tas/Historical_daily/tas_AFR-44_CCCma-CanESM2_historical_r1i1p1_SMHI-RCA4_v1_day_19710101-20001231.nc'   
    CNRM_past = '/exports/csce/datastore/geos/users/s0899345/AFR_44_tas/Historical_daily/tas_AFR-44_CNRM-CERFACS-CNRM-CM5_historical_r1i1p1_CLMcom-CCLM4-8-17_v1_day_19710101-20001231.nc'
    CNRMSMHI_past = '/exports/csce/datastore/geos/users/s0899345/AFR_44_tas/Historical_daily/tas_AFR-44_CNRM-CERFACS-CNRM-CM5_historical_r1i1p1_SMHI-RCA4_v1_day_19710101-20001231.nc'
    CSIRO_past = '/exports/csce/datastore/geos/users/s0899345/AFR_44_tas/Historical_daily/tas_AFR-44_CSIRO-QCCCE-CSIRO-Mk3-6-0_historical_r1i1p1_SMHI-RCA4_v1_day_19710101-20001231.nc'
    
    #Load exactly one cube from given file
    CCCmaCanRCM_past =  iris.load_cube(CCCmaCanRCM_past)
    CCCmaSMHI_past =  iris.load_cube(CCCmaSMHI_past)
    CNRM_past =  iris.load_cube(CNRM_past)
    CNRMSMHI_past =  iris.load_cube(CNRMSMHI_past)
    CSIRO_past =  iris.load_cube(CSIRO_past)
    
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
    
    #guess bounds    
    CCCmaCanRCM_past.coord('latitude').guess_bounds()
    CCCmaSMHI_past.coord('latitude').guess_bounds()
    CNRM_past.coord('latitude').guess_bounds()
    CNRMSMHI_past.coord('latitude').guess_bounds()
    CSIRO_past.coord('latitude').guess_bounds()
    
    CCCmaCanRCM_past.coord('longitude').guess_bounds()
    CCCmaSMHI_past.coord('longitude').guess_bounds()
    CNRM_past.coord('longitude').guess_bounds()
    CNRMSMHI_past.coord('longitude').guess_bounds()
    CSIRO_past.coord('longitude').guess_bounds()
    
    
    #-------------------------------------------------------------------------
    #PART 2: LOAD and FORMAT PROJECTED MODELS   
    CCCmaCanRCM= '/exports/csce/datastore/geos/users/s0899345/AFR_44_tas/4.5/tas_AFR-44_CCCma-CanESM2_rcp45_r1i1p1_CCCma-CanRCM4_r2_day_20060101-20701231.nc'
    CCCmaSMHI= '/exports/csce/datastore/geos/users/s0899345/AFR_44_tas/4.5/tas_AFR-44_CCCma-CanESM2_rcp45_r1i1p1_SMHI-RCA4_v1_day_20060101-20701231.nc'   
    CNRM= '/exports/csce/datastore/geos/users/s0899345/AFR_44_tas/4.5/tas_AFR-44_CNRM-CERFACS-CNRM-CM5_rcp45_r1i1p1_CLMcom-CCLM4-8-17_v1_day_20060101-20701231.nc'
    CNRMSMHI= '/exports/csce/datastore/geos/users/s0899345/AFR_44_tas/4.5/tas_AFR-44_CNRM-CERFACS-CNRM-CM5_rcp45_r1i1p1_SMHI-RCA4_v1_day_20060101-20701231.nc'
    CSIRO = '/exports/csce/datastore/geos/users/s0899345/AFR_44_tas/4.5/tas_AFR-44_CSIRO-QCCCE-CSIRO-Mk3-6-0_rcp45_r1i1p1_SMHI-RCA4_v1_day_20060101-20701231.nc'
    
    CCCmaCanRCM85 = '/exports/csce/datastore/geos/users/s0899345/AFR_44_tas/8.5/tas_AFR-44_CCCma-CanESM2_rcp85_r1i1p1_CCCma-CanRCM4_r2_day_20060101-20701231.nc'
    CCCmaSMHI85 = '/exports/csce/datastore/geos/users/s0899345/AFR_44_tas/8.5/tas_AFR-44_CCCma-CanESM2_rcp85_r1i1p1_SMHI-RCA4_v1_day_20060101-20701231.nc'   
    CNRM85 = '/exports/csce/datastore/geos/users/s0899345/AFR_44_tas/8.5/tas_AFR-44_CNRM-CERFACS-CNRM-CM5_rcp85_r1i1p1_CLMcom-CCLM4-8-17_v1_day_20060101-20701231.nc'
    CNRMSMHI85 = '/exports/csce/datastore/geos/users/s0899345/AFR_44_tas/8.5/tas_AFR-44_CNRM-CERFACS-CNRM-CM5_rcp85_r1i1p1_SMHI-RCA4_v1_day_20060101-20701231.nc'
    CSIRO85 = '/exports/csce/datastore/geos/users/s0899345/AFR_44_tas/8.5/tas_AFR-44_CSIRO-QCCCE-CSIRO-Mk3-6-0_rcp85_r1i1p1_SMHI-RCA4_v1_day_20060101-20701231.nc'
    
    #Load exactly one cube from given file
    CCCmaCanRCM = iris.load_cube(CCCmaCanRCM)
    CCCmaSMHI = iris.load_cube(CCCmaSMHI)
    CNRM = iris.load_cube(CNRM)
    CNRMSMHI = iris.load_cube(CNRMSMHI)
    CSIRO = iris.load_cube(CSIRO)
    
    CCCmaCanRCM85 = iris.load_cube(CCCmaCanRCM85)
    CCCmaSMHI85 = iris.load_cube(CCCmaSMHI85)
    CNRM85 = iris.load_cube(CNRM85)
    CNRMSMHI85 = iris.load_cube(CNRMSMHI85)
    CSIRO85 = iris.load_cube(CSIRO85)
    
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
    
    #guess bounds   
    CCCmaCanRCM.coord('latitude').guess_bounds()
    CCCmaSMHI.coord('latitude').guess_bounds()
    CNRM.coord('latitude').guess_bounds()
    CNRMSMHI.coord('latitude').guess_bounds()
    CSIRO.coord('latitude').guess_bounds()
    
    CCCmaCanRCM85.coord('latitude').guess_bounds()
    CCCmaSMHI85.coord('latitude').guess_bounds()
    CNRM85.coord('latitude').guess_bounds()
    CNRMSMHI85.coord('latitude').guess_bounds()
    CSIRO85.coord('latitude').guess_bounds()
    
    CCCmaCanRCM.coord('longitude').guess_bounds()
    CCCmaSMHI.coord('longitude').guess_bounds()
    CNRM.coord('longitude').guess_bounds()
    CNRMSMHI.coord('longitude').guess_bounds()
    CSIRO.coord('longitude').guess_bounds()
    
    CCCmaCanRCM85.coord('longitude').guess_bounds()
    CCCmaSMHI85.coord('longitude').guess_bounds()
    CNRM85.coord('longitude').guess_bounds()
    CNRMSMHI85.coord('longitude').guess_bounds()
    CSIRO85.coord('longitude').guess_bounds()
    
    
    #-------------------------------------------------------------------------
    #PART 3: LOAD AND FORMAT OBSERVED DATA
    #bring in all the files we need and give them a name
    CRU= '/exports/csce/datastore/geos/users/s0899345/Actual_Data/cru_ts4.00.1901.2015.tmp.dat.nc'
    UDel= '/exports/csce/datastore/geos/users/s0899345/Actual_Data/UDel_air.mon.mean.v401.nc'
    
    #Load exactly one cube from given file
    CRU = iris.load_cube(CRU, 'near-surface temperature')
    UDel = iris.load_cube(UDel)
    
    #guess bounds  
    CRU.coord('latitude').guess_bounds()
    UDel.coord('latitude').guess_bounds()
    
    CRU.coord('longitude').guess_bounds()
    UDel.coord('longitude').guess_bounds()
    
    
    #-------------------------------------------------------------------------
    #PART 4: FORMAT DATA GENERAL
    #Convert units to match, CORDEX data is in Kelvin but Observed data in Celsius, we would like to show all data in Celsius
    CCCmaCanRCM_past.convert_units('Celsius')
    CCCmaSMHI_past.convert_units('Celsius')
    CNRM_past.convert_units('Celsius')
    CNRMSMHI_past.convert_units('Celsius')
    CSIRO_past.convert_units('Celsius')
    
    CCCmaCanRCM.convert_units('Celsius')
    CCCmaSMHI.convert_units('Celsius')
    CNRM.convert_units('Celsius')
    CNRMSMHI.convert_units('Celsius')
    CSIRO.convert_units('Celsius')
    
    CCCmaCanRCM85.convert_units('Celsius')
    CCCmaSMHI85.convert_units('Celsius')
    CNRM85.convert_units('Celsius')
    CNRMSMHI85.convert_units('Celsius')
    CSIRO85.convert_units('Celsius')
    
    #rename units to match
    CRU.units = Unit('Celsius') 
    UDel.units = Unit('Celsius') 
    
    #limit time series of data
    #time constraint to make past and obsered data only from 1971-2000 
    iris.FUTURE.cell_datetime_objects = True
    t_constraint_past = iris.Constraint(time=lambda cell: 1971 <= cell.point.year <= 2000)
    
    CCCmaCanRCM_past =  CCCmaCanRCM_past.extract(t_constraint_past)
    CCCmaSMHI_past =  CCCmaSMHI_past.extract(t_constraint_past)
    CNRM_past =  CNRM_past.extract(t_constraint_past)
    CNRMSMHI_past =  CNRMSMHI_past.extract(t_constraint_past)
    CSIRO_past =  CSIRO_past.extract(t_constraint_past)
    
    CRU = CRU.extract(t_constraint_past)
    UDel = UDel.extract(t_constraint_past)
    
    #time constraint to make future data only from 2020-2049
    iris.FUTURE.cell_datetime_objects = True
    t_constraint_future = iris.Constraint(time=lambda cell: 2020 <= cell.point.year <= 2049)
    
    CCCmaCanRCM_30 = CCCmaCanRCM.extract(t_constraint_future)
    CCCmaSMHI_30 = CCCmaSMHI.extract(t_constraint_future)
    CNRM_30 = CNRM.extract(t_constraint_future)
    CNRMSMHI_30 = CNRMSMHI.extract(t_constraint_future)
    CSIRO_30 = CSIRO.extract(t_constraint_future)
    
    CCCmaCanRCM85_30 = CCCmaCanRCM85.extract(t_constraint_future)
    CCCmaSMHI85_30 = CCCmaSMHI85.extract(t_constraint_future)
    CNRM85_30 = CNRM85.extract(t_constraint_future)
    CNRMSMHI85_30 = CNRMSMHI85.extract(t_constraint_future)
    CSIRO85_30 = CSIRO85.extract(t_constraint_future)
    
    #time constraint to make future data only from 2040-2069
    iris.FUTURE.cell_datetime_objects = True
    t_constraint_future = iris.Constraint(time=lambda cell: 2040 <= cell.point.year <= 2069)
    
    CCCmaCanRCM_50 = CCCmaCanRCM.extract(t_constraint_future)
    CCCmaSMHI_50 = CCCmaSMHI.extract(t_constraint_future)
    CNRM_50 = CNRM.extract(t_constraint_future)
    CNRMSMHI_50 = CNRMSMHI.extract(t_constraint_future)
    CSIRO_50 = CSIRO.extract(t_constraint_future)
    
    CCCmaCanRCM85_50 = CCCmaCanRCM85.extract(t_constraint_future)
    CCCmaSMHI85_50 = CCCmaSMHI85.extract(t_constraint_future)
    CNRM85_50 = CNRM85.extract(t_constraint_future)
    CNRMSMHI85_50 = CNRMSMHI85.extract(t_constraint_future)
    CSIRO85_50 = CSIRO85.extract(t_constraint_future)
    
    
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
    
    CCCmaCanRCM_30_N = CCCmaCanRCM_30.extract(Northern_Malawi)
    CCCmaSMHI_30_N = CCCmaSMHI_30.extract(Northern_Malawi)
    CNRM_30_N = CNRM_30.extract(Northern_Malawi)
    CNRMSMHI_30_N = CNRMSMHI_30.extract(Northern_Malawi)
    CSIRO_30_N = CSIRO_30.extract(Northern_Malawi)
    
    CCCmaCanRCM85_30_N = CCCmaCanRCM85_30.extract(Northern_Malawi)
    CCCmaSMHI85_30_N = CCCmaSMHI85_30.extract(Northern_Malawi)
    CNRM85_30_N = CNRM85_30.extract(Northern_Malawi)
    CNRMSMHI85_30_N = CNRMSMHI85_30.extract(Northern_Malawi)
    CSIRO85_30_N = CSIRO85_30.extract(Northern_Malawi)
    
    CCCmaCanRCM_50_N = CCCmaCanRCM_50.extract(Northern_Malawi)
    CCCmaSMHI_50_N = CCCmaSMHI_50.extract(Northern_Malawi)
    CNRM_50_N = CNRM_50.extract(Northern_Malawi)
    CNRMSMHI_50_N = CNRMSMHI_50.extract(Northern_Malawi)
    CSIRO_50_N = CSIRO_50.extract(Northern_Malawi)
    
    CCCmaCanRCM85_50_N = CCCmaCanRCM85_50.extract(Northern_Malawi)
    CCCmaSMHI85_50_N = CCCmaSMHI85_50.extract(Northern_Malawi)
    CNRM85_50_N = CNRM85_50.extract(Northern_Malawi)
    CNRMSMHI85_50_N = CNRMSMHI85_50.extract(Northern_Malawi)
    CSIRO85_50_N = CSIRO85_50.extract(Northern_Malawi)
    
    CRU_N = CRU.extract(Northern_Malawi)
    UDel_N = UDel.extract(Northern_Malawi)
    
    #Returns an array of area weights, with the same dimensions as the cube
    CCCmaCanRCM_past_N_grid_areas = iris.analysis.cartography.area_weights(CCCmaCanRCM_past_N)
    CCCmaSMHI_past_N_grid_areas = iris.analysis.cartography.area_weights(CCCmaSMHI_past_N)
    CNRM_past_N_grid_areas = iris.analysis.cartography.area_weights(CNRM_past_N)
    CNRMSMHI_past_N_grid_areas = iris.analysis.cartography.area_weights(CNRMSMHI_past_N)
    CSIRO_past_N_grid_areas = iris.analysis.cartography.area_weights(CSIRO_past_N)
    
    CCCmaCanRCM_30_N_grid_areas = iris.analysis.cartography.area_weights(CCCmaCanRCM_30_N)
    CCCmaSMHI_30_N_grid_areas = iris.analysis.cartography.area_weights(CCCmaSMHI_30_N)
    CNRM_30_N_grid_areas = iris.analysis.cartography.area_weights(CNRM_30_N)
    CNRMSMHI_30_N_grid_areas = iris.analysis.cartography.area_weights(CNRMSMHI_30_N)
    CSIRO_30_N_grid_areas = iris.analysis.cartography.area_weights(CSIRO_30_N)
    
    CCCmaCanRCM85_30_N_grid_areas = iris.analysis.cartography.area_weights(CCCmaCanRCM85_30_N)
    CCCmaSMHI85_30_N_grid_areas = iris.analysis.cartography.area_weights(CCCmaSMHI85_30_N)
    CNRM85_30_N_grid_areas = iris.analysis.cartography.area_weights(CNRM85_30_N)
    CNRMSMHI85_30_N_grid_areas = iris.analysis.cartography.area_weights(CNRMSMHI85_30_N)
    CSIRO85_30_N_grid_areas = iris.analysis.cartography.area_weights(CSIRO85_30_N)
    
    CCCmaCanRCM_50_N_grid_areas = iris.analysis.cartography.area_weights(CCCmaCanRCM_50_N)
    CCCmaSMHI_50_N_grid_areas = iris.analysis.cartography.area_weights(CCCmaSMHI_50_N)
    CNRM_50_N_grid_areas = iris.analysis.cartography.area_weights(CNRM_50_N)
    CNRMSMHI_50_N_grid_areas = iris.analysis.cartography.area_weights(CNRMSMHI_50_N)
    CSIRO_50_N_grid_areas = iris.analysis.cartography.area_weights(CSIRO_50_N)
    
    CCCmaCanRCM85_50_N_grid_areas = iris.analysis.cartography.area_weights(CCCmaCanRCM85_50_N)
    CCCmaSMHI85_50_N_grid_areas = iris.analysis.cartography.area_weights(CCCmaSMHI85_50_N)
    CNRM85_50_N_grid_areas = iris.analysis.cartography.area_weights(CNRM85_50_N)
    CNRMSMHI85_50_N_grid_areas = iris.analysis.cartography.area_weights(CNRMSMHI85_50_N)
    CSIRO85_50_N_grid_areas = iris.analysis.cartography.area_weights(CSIRO85_50_N)
    
    CRU_N_grid_areas = iris.analysis.cartography.area_weights(CRU_N)
    UDel_N_grid_areas = iris.analysis.cartography.area_weights (UDel_N)
    
    #We want to plot the mean for the whole region so we need a mean of all the lats and lons
    CCCmaCanRCM_past_N_mean = CCCmaCanRCM_past_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CCCmaCanRCM_past_N_grid_areas) 
    CCCmaSMHI_past_N_mean = CCCmaSMHI_past_N.collapsed(['latitude', 'longitude'],iris.analysis.MEAN, weights=CCCmaSMHI_past_N_grid_areas)
    CNRM_past_N_mean = CNRM_past_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CNRM_past_N_grid_areas)                           
    CNRMSMHI_past_N_mean = CNRMSMHI_past_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CNRMSMHI_past_N_grid_areas)  
    CSIRO_past_N_mean = CSIRO_past_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CSIRO_past_N_grid_areas)
    
    CCCmaCanRCM_30_N_mean = CCCmaCanRCM_30_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CCCmaCanRCM_30_N_grid_areas) 
    CCCmaSMHI_30_N_mean = CCCmaSMHI_30_N.collapsed(['latitude', 'longitude'],iris.analysis.MEAN, weights=CCCmaSMHI_30_N_grid_areas)
    CNRM_30_N_mean = CNRM_30_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CNRM_30_N_grid_areas)                           
    CNRMSMHI_30_N_mean = CNRMSMHI_30_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CNRMSMHI_30_N_grid_areas)  
    CSIRO_30_N_mean = CSIRO_30_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CSIRO_30_N_grid_areas)
    
    CCCmaCanRCM85_30_N_mean = CCCmaCanRCM85_30_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CCCmaCanRCM85_30_N_grid_areas) 
    CCCmaSMHI85_30_N_mean = CCCmaSMHI85_30_N.collapsed(['latitude', 'longitude'],iris.analysis.MEAN, weights=CCCmaSMHI85_30_N_grid_areas)
    CNRM85_30_N_mean = CNRM85_30_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CNRM85_30_N_grid_areas)                           
    CNRMSMHI85_30_N_mean = CNRMSMHI85_30_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CNRMSMHI85_30_N_grid_areas)  
    CSIRO85_30_N_mean = CSIRO85_30_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CSIRO85_30_N_grid_areas)
    
    CCCmaCanRCM_50_N_mean = CCCmaCanRCM_50_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CCCmaCanRCM_50_N_grid_areas) 
    CCCmaSMHI_50_N_mean = CCCmaSMHI_50_N.collapsed(['latitude', 'longitude'],iris.analysis.MEAN, weights=CCCmaSMHI_50_N_grid_areas)
    CNRM_50_N_mean = CNRM_50_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CNRM_50_N_grid_areas)                           
    CNRMSMHI_50_N_mean = CNRMSMHI_50_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CNRMSMHI_50_N_grid_areas)  
    CSIRO_50_N_mean = CSIRO_50_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CSIRO_50_N_grid_areas)
    
    CCCmaCanRCM85_50_N_mean = CCCmaCanRCM85_50_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CCCmaCanRCM85_50_N_grid_areas) 
    CCCmaSMHI85_50_N_mean = CCCmaSMHI85_50_N.collapsed(['latitude', 'longitude'],iris.analysis.MEAN, weights=CCCmaSMHI85_50_N_grid_areas)
    CNRM85_50_N_mean = CNRM85_50_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CNRM85_50_N_grid_areas)                           
    CNRMSMHI85_50_N_mean = CNRMSMHI85_50_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CNRMSMHI85_50_N_grid_areas)  
    CSIRO85_50_N_mean = CSIRO85_50_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CSIRO85_50_N_grid_areas)
    
    CRU_N_mean = CRU_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CRU_N_grid_areas)
    UDel_N_mean = UDel_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=UDel_N_grid_areas)
    
    #for the baseline we don't need to average for each year, but the average for the whole time period, so collapse by time
    CCCmaCanRCM_b_N_mean = CCCmaCanRCM_past_N_mean.collapsed(['time'], iris.analysis.MEAN) 
    CCCmaSMHI_b_N_mean = CCCmaSMHI_past_N_mean.collapsed(['time'], iris.analysis.MEAN) 
    CNRM_b_N_mean = CNRM_past_N_mean.collapsed(['time'], iris.analysis.MEAN)                      
    CNRMSMHI_b_N_mean = CNRMSMHI_past_N_mean.collapsed(['time'], iris.analysis.MEAN)   
    CSIRO_b_N_mean = CSIRO_past_N_mean.collapsed(['time'], iris.analysis.MEAN)
    
    CRU_N_mean = CRU_N_mean.collapsed(['time'], iris.analysis.MEAN)     
    UDel_N_mean = UDel_N_mean.collapsed(['time'], iris.analysis.MEAN)
    
    #create average of observed baseline data
    Obs_N = (CRU_N_mean + UDel_N_mean)/2
    
    #We want to see the change in temperature from the baseline
    CCCmaCanRCM_past_N_mean = (CCCmaCanRCM_past_N_mean.data - CCCmaCanRCM_b_N_mean.data + Obs_N.data)
    CCCmaSMHI_past_N_mean = (CCCmaSMHI_past_N_mean.data - CCCmaSMHI_b_N_mean.data + Obs_N.data)
    CNRM_past_N_mean = (CNRM_past_N_mean.data - CNRM_b_N_mean.data + Obs_N.data)
    CNRMSMHI_past_N_mean = (CNRMSMHI_past_N_mean.data - CNRMSMHI_b_N_mean.data + Obs_N.data)  
    CSIRO_past_N_mean = (CSIRO_past_N_mean.data - CSIRO_b_N_mean.data + Obs_N.data)
    
    CCCmaCanRCM_30_N_mean = (CCCmaCanRCM_30_N_mean.data - CCCmaCanRCM_b_N_mean.data + Obs_N.data)
    CCCmaSMHI_30_N_mean = (CCCmaSMHI_30_N_mean.data - CCCmaSMHI_b_N_mean.data + Obs_N.data)
    CNRM_30_N_mean = (CNRM_30_N_mean.data - CNRM_b_N_mean.data + Obs_N.data)
    CNRMSMHI_30_N_mean = (CNRMSMHI_30_N_mean.data - CNRMSMHI_b_N_mean.data + Obs_N.data)  
    CSIRO_30_N_mean = (CSIRO_30_N_mean.data - CSIRO_b_N_mean.data + Obs_N.data)
    
    CCCmaCanRCM85_30_N_mean = (CCCmaCanRCM85_30_N_mean.data - CCCmaCanRCM_b_N_mean.data + Obs_N.data)
    CCCmaSMHI85_30_N_mean = (CCCmaSMHI85_30_N_mean.data - CCCmaSMHI_b_N_mean.data + Obs_N.data)
    CNRM85_30_N_mean = (CNRM85_30_N_mean.data - CNRM_b_N_mean.data + Obs_N.data)
    CNRMSMHI85_30_N_mean = (CNRMSMHI85_30_N_mean.data - CNRMSMHI_b_N_mean.data + Obs_N.data)  
    CSIRO85_30_N_mean = (CSIRO85_30_N_mean.data - CSIRO_b_N_mean.data + Obs_N.data)
    
    CCCmaCanRCM_50_N_mean = (CCCmaCanRCM_50_N_mean.data - CCCmaCanRCM_b_N_mean.data + Obs_N.data)
    CCCmaSMHI_50_N_mean = (CCCmaSMHI_50_N_mean.data - CCCmaSMHI_b_N_mean.data + Obs_N.data)
    CNRM_50_N_mean = (CNRM_50_N_mean.data - CNRM_b_N_mean.data + Obs_N.data)
    CNRMSMHI_50_N_mean = (CNRMSMHI_50_N_mean.data - CNRMSMHI_b_N_mean.data + Obs_N.data)  
    CSIRO_50_N_mean = (CSIRO_50_N_mean.data - CSIRO_b_N_mean.data + Obs_N.data)
    
    CCCmaCanRCM85_50_N_mean = (CCCmaCanRCM85_50_N_mean.data - CCCmaCanRCM_b_N_mean.data + Obs_N.data)
    CCCmaSMHI85_50_N_mean = (CCCmaSMHI85_50_N_mean.data - CCCmaSMHI_b_N_mean.data + Obs_N.data)
    CNRM85_50_N_mean = (CNRM85_50_N_mean.data - CNRM_b_N_mean.data + Obs_N.data)
    CNRMSMHI85_50_N_mean = (CNRMSMHI85_50_N_mean.data - CNRMSMHI_b_N_mean.data + Obs_N.data)  
    CSIRO85_50_N_mean = (CSIRO85_50_N_mean.data - CSIRO_b_N_mean.data + Obs_N.data)
    
    
    #PART 5B: CENTRAL MALAWI
    #we are only interested in the latitude and longitude relevant to Central Malawi 
    Central_Malawi = iris.Constraint(longitude=lambda v: 32.5 <= v <= 35.5, latitude=lambda v: -15 <= v <= -11.5) 
    
    CCCmaCanRCM_past_C = CCCmaCanRCM_past.extract(Central_Malawi)
    CCCmaSMHI_past_C = CCCmaSMHI_past.extract(Central_Malawi)
    CNRM_past_C = CNRM_past.extract(Central_Malawi)
    CNRMSMHI_past_C = CNRMSMHI_past.extract(Central_Malawi)
    CSIRO_past_C = CSIRO_past.extract(Central_Malawi)
    
    CCCmaCanRCM_30_C = CCCmaCanRCM_30.extract(Central_Malawi)
    CCCmaSMHI_30_C = CCCmaSMHI_30.extract(Central_Malawi)
    CNRM_30_C = CNRM_30.extract(Central_Malawi)
    CNRMSMHI_30_C = CNRMSMHI_30.extract(Central_Malawi)
    CSIRO_30_C = CSIRO_30.extract(Central_Malawi)
    
    CCCmaCanRCM85_30_C = CCCmaCanRCM85_30.extract(Central_Malawi)
    CCCmaSMHI85_30_C = CCCmaSMHI85_30.extract(Central_Malawi)
    CNRM85_30_C = CNRM85_30.extract(Central_Malawi)
    CNRMSMHI85_30_C = CNRMSMHI85_30.extract(Central_Malawi)
    CSIRO85_30_C = CSIRO85_30.extract(Central_Malawi)
    
    CCCmaCanRCM_50_C = CCCmaCanRCM_50.extract(Central_Malawi)
    CCCmaSMHI_50_C = CCCmaSMHI_50.extract(Central_Malawi)
    CNRM_50_C = CNRM_50.extract(Central_Malawi)
    CNRMSMHI_50_C = CNRMSMHI_50.extract(Central_Malawi)
    CSIRO_50_C = CSIRO_50.extract(Central_Malawi)
    
    CCCmaCanRCM85_50_C = CCCmaCanRCM85_50.extract(Central_Malawi)
    CCCmaSMHI85_50_C = CCCmaSMHI85_50.extract(Central_Malawi)
    CNRM85_50_C = CNRM85_50.extract(Central_Malawi)
    CNRMSMHI85_50_C = CNRMSMHI85_50.extract(Central_Malawi)
    CSIRO85_50_C = CSIRO85_50.extract(Central_Malawi)
    
    CRU_C = CRU.extract(Central_Malawi)
    UDel_C = UDel.extract(Central_Malawi)
    
    #Returns an array of area weights, with the same dimensions as the cube
    CCCmaCanRCM_past_C_grid_areas = iris.analysis.cartography.area_weights(CCCmaCanRCM_past_C)
    CCCmaSMHI_past_C_grid_areas = iris.analysis.cartography.area_weights(CCCmaSMHI_past_C)
    CNRM_past_C_grid_areas = iris.analysis.cartography.area_weights(CNRM_past_C)
    CNRMSMHI_past_C_grid_areas = iris.analysis.cartography.area_weights(CNRMSMHI_past_C)
    CSIRO_past_C_grid_areas = iris.analysis.cartography.area_weights(CSIRO_past_C)
    
    CCCmaCanRCM_30_C_grid_areas = iris.analysis.cartography.area_weights(CCCmaCanRCM_30_C)
    CCCmaSMHI_30_C_grid_areas = iris.analysis.cartography.area_weights(CCCmaSMHI_30_C)
    CNRM_30_C_grid_areas = iris.analysis.cartography.area_weights(CNRM_30_C)
    CNRMSMHI_30_C_grid_areas = iris.analysis.cartography.area_weights(CNRMSMHI_30_C)
    CSIRO_30_C_grid_areas = iris.analysis.cartography.area_weights(CSIRO_30_C)
    
    CCCmaCanRCM85_30_C_grid_areas = iris.analysis.cartography.area_weights(CCCmaCanRCM85_30_C)
    CCCmaSMHI85_30_C_grid_areas = iris.analysis.cartography.area_weights(CCCmaSMHI85_30_C)
    CNRM85_30_C_grid_areas = iris.analysis.cartography.area_weights(CNRM85_30_C)
    CNRMSMHI85_30_C_grid_areas = iris.analysis.cartography.area_weights(CNRMSMHI85_30_C)
    CSIRO85_30_C_grid_areas = iris.analysis.cartography.area_weights(CSIRO85_30_C)
    
    CCCmaCanRCM_50_C_grid_areas = iris.analysis.cartography.area_weights(CCCmaCanRCM_50_C)
    CCCmaSMHI_50_C_grid_areas = iris.analysis.cartography.area_weights(CCCmaSMHI_50_C)
    CNRM_50_C_grid_areas = iris.analysis.cartography.area_weights(CNRM_50_C)
    CNRMSMHI_50_C_grid_areas = iris.analysis.cartography.area_weights(CNRMSMHI_50_C)
    CSIRO_50_C_grid_areas = iris.analysis.cartography.area_weights(CSIRO_50_C)
    
    CCCmaCanRCM85_50_C_grid_areas = iris.analysis.cartography.area_weights(CCCmaCanRCM85_50_C)
    CCCmaSMHI85_50_C_grid_areas = iris.analysis.cartography.area_weights(CCCmaSMHI85_50_C)
    CNRM85_50_C_grid_areas = iris.analysis.cartography.area_weights(CNRM85_50_C)
    CNRMSMHI85_50_C_grid_areas = iris.analysis.cartography.area_weights(CNRMSMHI85_50_C)
    CSIRO85_50_C_grid_areas = iris.analysis.cartography.area_weights(CSIRO85_50_C)
    
    CRU_C_grid_areas = iris.analysis.cartography.area_weights(CRU_C)
    UDel_C_grid_areas = iris.analysis.cartography.area_weights (UDel_C)
    
    #We want to plot the mean for the whole region so we need a mean of all the lats and lons
    CCCmaCanRCM_past_C_mean = CCCmaCanRCM_past_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CCCmaCanRCM_past_C_grid_areas) 
    CCCmaSMHI_past_C_mean = CCCmaSMHI_past_C.collapsed(['latitude', 'longitude'],iris.analysis.MEAN, weights=CCCmaSMHI_past_C_grid_areas)
    CNRM_past_C_mean = CNRM_past_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CNRM_past_C_grid_areas)                           
    CNRMSMHI_past_C_mean = CNRMSMHI_past_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CNRMSMHI_past_C_grid_areas)  
    CSIRO_past_C_mean = CSIRO_past_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CSIRO_past_C_grid_areas)
    
    CCCmaCanRCM_30_C_mean = CCCmaCanRCM_30_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CCCmaCanRCM_30_C_grid_areas) 
    CCCmaSMHI_30_C_mean = CCCmaSMHI_30_C.collapsed(['latitude', 'longitude'],iris.analysis.MEAN, weights=CCCmaSMHI_30_C_grid_areas)
    CNRM_30_C_mean = CNRM_30_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CNRM_30_C_grid_areas)                           
    CNRMSMHI_30_C_mean = CNRMSMHI_30_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CNRMSMHI_30_C_grid_areas)  
    CSIRO_30_C_mean = CSIRO_30_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CSIRO_30_C_grid_areas)
    
    CCCmaCanRCM85_30_C_mean = CCCmaCanRCM85_30_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CCCmaCanRCM85_30_C_grid_areas) 
    CCCmaSMHI85_30_C_mean = CCCmaSMHI85_30_C.collapsed(['latitude', 'longitude'],iris.analysis.MEAN, weights=CCCmaSMHI85_30_C_grid_areas)
    CNRM85_30_C_mean = CNRM85_30_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CNRM85_30_C_grid_areas)                           
    CNRMSMHI85_30_C_mean = CNRMSMHI85_30_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CNRMSMHI85_30_C_grid_areas)  
    CSIRO85_30_C_mean = CSIRO85_30_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CSIRO85_30_C_grid_areas)
    
    CCCmaCanRCM_50_C_mean = CCCmaCanRCM_50_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CCCmaCanRCM_50_C_grid_areas) 
    CCCmaSMHI_50_C_mean = CCCmaSMHI_50_C.collapsed(['latitude', 'longitude'],iris.analysis.MEAN, weights=CCCmaSMHI_50_C_grid_areas)
    CNRM_50_C_mean = CNRM_50_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CNRM_50_C_grid_areas)                           
    CNRMSMHI_50_C_mean = CNRMSMHI_50_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CNRMSMHI_50_C_grid_areas)  
    CSIRO_50_C_mean = CSIRO_50_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CSIRO_50_C_grid_areas)
    
    CCCmaCanRCM85_50_C_mean = CCCmaCanRCM85_50_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CCCmaCanRCM85_50_C_grid_areas) 
    CCCmaSMHI85_50_C_mean = CCCmaSMHI85_50_C.collapsed(['latitude', 'longitude'],iris.analysis.MEAN, weights=CCCmaSMHI85_50_C_grid_areas)
    CNRM85_50_C_mean = CNRM85_50_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CNRM85_50_C_grid_areas)                           
    CNRMSMHI85_50_C_mean = CNRMSMHI85_50_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CNRMSMHI85_50_C_grid_areas)  
    CSIRO85_50_C_mean = CSIRO85_50_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CSIRO85_50_C_grid_areas)
    
    CRU_C_mean = CRU_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CRU_C_grid_areas)
    UDel_C_mean = UDel_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=UDel_C_grid_areas)
    
    #for the baseline we don't need to average for each year, but the average for the whole time period, so collapse by time
    CCCmaCanRCM_b_C_mean = CCCmaCanRCM_past_C_mean.collapsed(['time'], iris.analysis.MEAN) 
    CCCmaSMHI_b_C_mean = CCCmaSMHI_past_C_mean.collapsed(['time'], iris.analysis.MEAN) 
    CNRM_b_C_mean = CNRM_past_C_mean.collapsed(['time'], iris.analysis.MEAN)                      
    CNRMSMHI_b_C_mean = CNRMSMHI_past_C_mean.collapsed(['time'], iris.analysis.MEAN)   
    CSIRO_b_C_mean = CSIRO_past_C_mean.collapsed(['time'], iris.analysis.MEAN)
    
    CRU_C_mean = CRU_C_mean.collapsed(['time'], iris.analysis.MEAN)     
    UDel_C_mean = UDel_C_mean.collapsed(['time'], iris.analysis.MEAN)
    
    #create average of observed baseline data
    Obs_C = (CRU_C_mean + UDel_C_mean)/2
    
    #We want to see the change in temperature from the baseline
    CCCmaCanRCM_past_C_mean = (CCCmaCanRCM_past_C_mean.data - CCCmaCanRCM_b_C_mean.data + Obs_C.data)
    CCCmaSMHI_past_C_mean = (CCCmaSMHI_past_C_mean.data - CCCmaSMHI_b_C_mean.data + Obs_C.data)
    CNRM_past_C_mean = (CNRM_past_C_mean.data - CNRM_b_C_mean.data + Obs_C.data)
    CNRMSMHI_past_C_mean = (CNRMSMHI_past_C_mean.data - CNRMSMHI_b_C_mean.data + Obs_C.data)  
    CSIRO_past_C_mean = (CSIRO_past_C_mean.data - CSIRO_b_C_mean.data + Obs_C.data)
    
    CCCmaCanRCM_30_C_mean = (CCCmaCanRCM_30_C_mean.data - CCCmaCanRCM_b_C_mean.data + Obs_C.data)
    CCCmaSMHI_30_C_mean = (CCCmaSMHI_30_C_mean.data - CCCmaSMHI_b_C_mean.data + Obs_C.data)
    CNRM_30_C_mean = (CNRM_30_C_mean.data - CNRM_b_C_mean.data + Obs_C.data)
    CNRMSMHI_30_C_mean = (CNRMSMHI_30_C_mean.data - CNRMSMHI_b_C_mean.data + Obs_C.data)  
    CSIRO_30_C_mean = (CSIRO_30_C_mean.data - CSIRO_b_C_mean.data + Obs_C.data)
    
    CCCmaCanRCM85_30_C_mean = (CCCmaCanRCM85_30_C_mean.data - CCCmaCanRCM_b_C_mean.data + Obs_C.data)
    CCCmaSMHI85_30_C_mean = (CCCmaSMHI85_30_C_mean.data - CCCmaSMHI_b_C_mean.data + Obs_C.data)
    CNRM85_30_C_mean = (CNRM85_30_C_mean.data - CNRM_b_C_mean.data + Obs_C.data)
    CNRMSMHI85_30_C_mean = (CNRMSMHI85_30_C_mean.data - CNRMSMHI_b_C_mean.data + Obs_C.data)  
    CSIRO85_30_C_mean = (CSIRO85_30_C_mean.data - CSIRO_b_C_mean.data + Obs_C.data)
    
    CCCmaCanRCM_50_C_mean = (CCCmaCanRCM_50_C_mean.data - CCCmaCanRCM_b_C_mean.data + Obs_C.data)
    CCCmaSMHI_50_C_mean = (CCCmaSMHI_50_C_mean.data - CCCmaSMHI_b_C_mean.data + Obs_C.data)
    CNRM_50_C_mean = (CNRM_50_C_mean.data - CNRM_b_C_mean.data + Obs_C.data)
    CNRMSMHI_50_C_mean = (CNRMSMHI_50_C_mean.data - CNRMSMHI_b_C_mean.data + Obs_C.data)  
    CSIRO_50_C_mean = (CSIRO_50_C_mean.data - CSIRO_b_C_mean.data + Obs_C.data)
    
    CCCmaCanRCM85_50_C_mean = (CCCmaCanRCM85_50_C_mean.data - CCCmaCanRCM_b_C_mean.data + Obs_C.data)
    CCCmaSMHI85_50_C_mean = (CCCmaSMHI85_50_C_mean.data - CCCmaSMHI_b_C_mean.data + Obs_C.data)
    CNRM85_50_C_mean = (CNRM85_50_C_mean.data - CNRM_b_C_mean.data + Obs_C.data)
    CNRMSMHI85_50_C_mean = (CNRMSMHI85_50_C_mean.data - CNRMSMHI_b_C_mean.data + Obs_C.data)  
    CSIRO85_50_C_mean = (CSIRO85_50_C_mean.data - CSIRO_b_C_mean.data + Obs_C.data)
    
            
    #PART 5C: SOUTHERN MALAWI
    #we are only interested in the latitude and longitude relevant to Southern Malawi 
    Southern_Malawi = iris.Constraint(longitude=lambda v: 34 <= v <= 36.5, latitude=lambda v: -17.5 <= v <= -14) 
    
    CCCmaCanRCM_past_S = CCCmaCanRCM_past.extract(Southern_Malawi)
    CCCmaSMHI_past_S = CCCmaSMHI_past.extract(Southern_Malawi)
    CNRM_past_S = CNRM_past.extract(Southern_Malawi)
    CNRMSMHI_past_S = CNRMSMHI_past.extract(Southern_Malawi)
    CSIRO_past_S = CSIRO_past.extract(Southern_Malawi)
    
    CCCmaCanRCM_30_S = CCCmaCanRCM_30.extract(Southern_Malawi)
    CCCmaSMHI_30_S = CCCmaSMHI_30.extract(Southern_Malawi)
    CNRM_30_S = CNRM_30.extract(Southern_Malawi)
    CNRMSMHI_30_S = CNRMSMHI_30.extract(Southern_Malawi)
    CSIRO_30_S = CSIRO_30.extract(Southern_Malawi)
    
    CCCmaCanRCM85_30_S = CCCmaCanRCM85_30.extract(Southern_Malawi)
    CCCmaSMHI85_30_S = CCCmaSMHI85_30.extract(Southern_Malawi)
    CNRM85_30_S = CNRM85_30.extract(Southern_Malawi)
    CNRMSMHI85_30_S = CNRMSMHI85_30.extract(Southern_Malawi)
    CSIRO85_30_S = CSIRO85_30.extract(Southern_Malawi)
    
    CCCmaCanRCM_50_S = CCCmaCanRCM_50.extract(Southern_Malawi)
    CCCmaSMHI_50_S = CCCmaSMHI_50.extract(Southern_Malawi)
    CNRM_50_S = CNRM_50.extract(Southern_Malawi)
    CNRMSMHI_50_S = CNRMSMHI_50.extract(Southern_Malawi)
    CSIRO_50_S = CSIRO_50.extract(Southern_Malawi)
    
    CCCmaCanRCM85_50_S = CCCmaCanRCM85_50.extract(Southern_Malawi)
    CCCmaSMHI85_50_S = CCCmaSMHI85_50.extract(Southern_Malawi)
    CNRM85_50_S = CNRM85_50.extract(Southern_Malawi)
    CNRMSMHI85_50_S = CNRMSMHI85_50.extract(Southern_Malawi)
    CSIRO85_50_S = CSIRO85_50.extract(Southern_Malawi)
    
    CRU_S = CRU.extract(Southern_Malawi)
    UDel_S = UDel.extract(Southern_Malawi)
    
    #Returns an array of area weights, with the same dimensions as the cube
    CCCmaCanRCM_past_S_grid_areas = iris.analysis.cartography.area_weights(CCCmaCanRCM_past_S)
    CCCmaSMHI_past_S_grid_areas = iris.analysis.cartography.area_weights(CCCmaSMHI_past_S)
    CNRM_past_S_grid_areas = iris.analysis.cartography.area_weights(CNRM_past_S)
    CNRMSMHI_past_S_grid_areas = iris.analysis.cartography.area_weights(CNRMSMHI_past_S)
    CSIRO_past_S_grid_areas = iris.analysis.cartography.area_weights(CSIRO_past_S)
    
    CCCmaCanRCM_30_S_grid_areas = iris.analysis.cartography.area_weights(CCCmaCanRCM_30_S)
    CCCmaSMHI_30_S_grid_areas = iris.analysis.cartography.area_weights(CCCmaSMHI_30_S)
    CNRM_30_S_grid_areas = iris.analysis.cartography.area_weights(CNRM_30_S)
    CNRMSMHI_30_S_grid_areas = iris.analysis.cartography.area_weights(CNRMSMHI_30_S)
    CSIRO_30_S_grid_areas = iris.analysis.cartography.area_weights(CSIRO_30_S)
    
    CCCmaCanRCM85_30_S_grid_areas = iris.analysis.cartography.area_weights(CCCmaCanRCM85_30_S)
    CCCmaSMHI85_30_S_grid_areas = iris.analysis.cartography.area_weights(CCCmaSMHI85_30_S)
    CNRM85_30_S_grid_areas = iris.analysis.cartography.area_weights(CNRM85_30_S)
    CNRMSMHI85_30_S_grid_areas = iris.analysis.cartography.area_weights(CNRMSMHI85_30_S)
    CSIRO85_30_S_grid_areas = iris.analysis.cartography.area_weights(CSIRO85_30_S)
    
    CCCmaCanRCM_50_S_grid_areas = iris.analysis.cartography.area_weights(CCCmaCanRCM_50_S)
    CCCmaSMHI_50_S_grid_areas = iris.analysis.cartography.area_weights(CCCmaSMHI_50_S)
    CNRM_50_S_grid_areas = iris.analysis.cartography.area_weights(CNRM_50_S)
    CNRMSMHI_50_S_grid_areas = iris.analysis.cartography.area_weights(CNRMSMHI_50_S)
    CSIRO_50_S_grid_areas = iris.analysis.cartography.area_weights(CSIRO_50_S)
    
    CCCmaCanRCM85_50_S_grid_areas = iris.analysis.cartography.area_weights(CCCmaCanRCM85_50_S)
    CCCmaSMHI85_50_S_grid_areas = iris.analysis.cartography.area_weights(CCCmaSMHI85_50_S)
    CNRM85_50_S_grid_areas = iris.analysis.cartography.area_weights(CNRM85_50_S)
    CNRMSMHI85_50_S_grid_areas = iris.analysis.cartography.area_weights(CNRMSMHI85_50_S)
    CSIRO85_50_S_grid_areas = iris.analysis.cartography.area_weights(CSIRO85_50_S)
    
    CRU_S_grid_areas = iris.analysis.cartography.area_weights(CRU_S)
    UDel_S_grid_areas = iris.analysis.cartography.area_weights (UDel_S)
    
    #We want to plot the mean for the whole region so we need a mean of all the lats and lons
    CCCmaCanRCM_past_S_mean = CCCmaCanRCM_past_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CCCmaCanRCM_past_S_grid_areas) 
    CCCmaSMHI_past_S_mean = CCCmaSMHI_past_S.collapsed(['latitude', 'longitude'],iris.analysis.MEAN, weights=CCCmaSMHI_past_S_grid_areas)
    CNRM_past_S_mean = CNRM_past_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CNRM_past_S_grid_areas)                           
    CNRMSMHI_past_S_mean = CNRMSMHI_past_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CNRMSMHI_past_S_grid_areas)  
    CSIRO_past_S_mean = CSIRO_past_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CSIRO_past_S_grid_areas)
    
    CCCmaCanRCM_30_S_mean = CCCmaCanRCM_30_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CCCmaCanRCM_30_S_grid_areas) 
    CCCmaSMHI_30_S_mean = CCCmaSMHI_30_S.collapsed(['latitude', 'longitude'],iris.analysis.MEAN, weights=CCCmaSMHI_30_S_grid_areas)
    CNRM_30_S_mean = CNRM_30_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CNRM_30_S_grid_areas)                           
    CNRMSMHI_30_S_mean = CNRMSMHI_30_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CNRMSMHI_30_S_grid_areas)  
    CSIRO_30_S_mean = CSIRO_30_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CSIRO_30_S_grid_areas)
    
    CCCmaCanRCM85_30_S_mean = CCCmaCanRCM85_30_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CCCmaCanRCM85_30_S_grid_areas) 
    CCCmaSMHI85_30_S_mean = CCCmaSMHI85_30_S.collapsed(['latitude', 'longitude'],iris.analysis.MEAN, weights=CCCmaSMHI85_30_S_grid_areas)
    CNRM85_30_S_mean = CNRM85_30_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CNRM85_30_S_grid_areas)                           
    CNRMSMHI85_30_S_mean = CNRMSMHI85_30_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CNRMSMHI85_30_S_grid_areas)  
    CSIRO85_30_S_mean = CSIRO85_30_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CSIRO85_30_S_grid_areas)
    
    CCCmaCanRCM_50_S_mean = CCCmaCanRCM_50_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CCCmaCanRCM_50_S_grid_areas) 
    CCCmaSMHI_50_S_mean = CCCmaSMHI_50_S.collapsed(['latitude', 'longitude'],iris.analysis.MEAN, weights=CCCmaSMHI_50_S_grid_areas)
    CNRM_50_S_mean = CNRM_50_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CNRM_50_S_grid_areas)                           
    CNRMSMHI_50_S_mean = CNRMSMHI_50_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CNRMSMHI_50_S_grid_areas)  
    CSIRO_50_S_mean = CSIRO_50_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CSIRO_50_S_grid_areas)
    
    CCCmaCanRCM85_50_S_mean = CCCmaCanRCM85_50_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CCCmaCanRCM85_50_S_grid_areas) 
    CCCmaSMHI85_50_S_mean = CCCmaSMHI85_50_S.collapsed(['latitude', 'longitude'],iris.analysis.MEAN, weights=CCCmaSMHI85_50_S_grid_areas)
    CNRM85_50_S_mean = CNRM85_50_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CNRM85_50_S_grid_areas)                           
    CNRMSMHI85_50_S_mean = CNRMSMHI85_50_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CNRMSMHI85_50_S_grid_areas)  
    CSIRO85_50_S_mean = CSIRO85_50_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CSIRO85_50_S_grid_areas)
    
    CRU_S_mean = CRU_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CRU_S_grid_areas)
    UDel_S_mean = UDel_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=UDel_S_grid_areas)
    
    #for the baseline we don't need to average for each year, but the average for the whole time period, so collapse by time
    CCCmaCanRCM_b_S_mean = CCCmaCanRCM_past_S_mean.collapsed(['time'], iris.analysis.MEAN) 
    CCCmaSMHI_b_S_mean = CCCmaSMHI_past_S_mean.collapsed(['time'], iris.analysis.MEAN) 
    CNRM_b_S_mean = CNRM_past_S_mean.collapsed(['time'], iris.analysis.MEAN)                      
    CNRMSMHI_b_S_mean = CNRMSMHI_past_S_mean.collapsed(['time'], iris.analysis.MEAN)   
    CSIRO_b_S_mean = CSIRO_past_S_mean.collapsed(['time'], iris.analysis.MEAN)
    
    CRU_S_mean = CRU_S_mean.collapsed(['time'], iris.analysis.MEAN)     
    UDel_S_mean = UDel_S_mean.collapsed(['time'], iris.analysis.MEAN)
    
    #create average of observed baseline data
    Obs_S = (CRU_S_mean + UDel_S_mean)/2
    
    #We want to see the change in temperature from the baseline
    CCCmaCanRCM_past_S_mean = (CCCmaCanRCM_past_S_mean.data - CCCmaCanRCM_b_S_mean.data + Obs_S.data)
    CCCmaSMHI_past_S_mean = (CCCmaSMHI_past_S_mean.data - CCCmaSMHI_b_S_mean.data + Obs_S.data)
    CNRM_past_S_mean = (CNRM_past_S_mean.data - CNRM_b_S_mean.data + Obs_S.data)
    CNRMSMHI_past_S_mean = (CNRMSMHI_past_S_mean.data - CNRMSMHI_b_S_mean.data + Obs_S.data)  
    CSIRO_past_S_mean = (CSIRO_past_S_mean.data - CSIRO_b_S_mean.data + Obs_S.data)
    
    CCCmaCanRCM_30_S_mean = (CCCmaCanRCM_30_S_mean.data - CCCmaCanRCM_b_S_mean.data + Obs_S.data)
    CCCmaSMHI_30_S_mean = (CCCmaSMHI_30_S_mean.data - CCCmaSMHI_b_S_mean.data + Obs_S.data)
    CNRM_30_S_mean = (CNRM_30_S_mean.data - CNRM_b_S_mean.data + Obs_S.data)
    CNRMSMHI_30_S_mean = (CNRMSMHI_30_S_mean.data - CNRMSMHI_b_S_mean.data + Obs_S.data)  
    CSIRO_30_S_mean = (CSIRO_30_S_mean.data - CSIRO_b_S_mean.data + Obs_S.data)
    
    CCCmaCanRCM85_30_S_mean = (CCCmaCanRCM85_30_S_mean.data - CCCmaCanRCM_b_S_mean.data + Obs_S.data)
    CCCmaSMHI85_30_S_mean = (CCCmaSMHI85_30_S_mean.data - CCCmaSMHI_b_S_mean.data + Obs_S.data)
    CNRM85_30_S_mean = (CNRM85_30_S_mean.data - CNRM_b_S_mean.data + Obs_S.data)
    CNRMSMHI85_30_S_mean = (CNRMSMHI85_30_S_mean.data - CNRMSMHI_b_S_mean.data + Obs_S.data)  
    CSIRO85_30_S_mean = (CSIRO85_30_S_mean.data - CSIRO_b_S_mean.data + Obs_S.data)
    
    CCCmaCanRCM_50_S_mean = (CCCmaCanRCM_50_S_mean.data - CCCmaCanRCM_b_S_mean.data + Obs_S.data)
    CCCmaSMHI_50_S_mean = (CCCmaSMHI_50_S_mean.data - CCCmaSMHI_b_S_mean.data + Obs_S.data)
    CNRM_50_S_mean = (CNRM_50_S_mean.data - CNRM_b_S_mean.data + Obs_S.data)
    CNRMSMHI_50_S_mean = (CNRMSMHI_50_S_mean.data - CNRMSMHI_b_S_mean.data + Obs_S.data)  
    CSIRO_50_S_mean = (CSIRO_50_S_mean.data - CSIRO_b_S_mean.data + Obs_S.data)
    
    CCCmaCanRCM85_50_S_mean = (CCCmaCanRCM85_50_S_mean.data - CCCmaCanRCM_b_S_mean.data + Obs_S.data)
    CCCmaSMHI85_50_S_mean = (CCCmaSMHI85_50_S_mean.data - CCCmaSMHI_b_S_mean.data + Obs_S.data)
    CNRM85_50_S_mean = (CNRM85_50_S_mean.data - CNRM_b_S_mean.data + Obs_S.data)
    CNRMSMHI85_50_S_mean = (CNRMSMHI85_50_S_mean.data - CNRMSMHI_b_S_mean.data + Obs_S.data)  
    CSIRO85_50_S_mean = (CSIRO85_50_S_mean.data - CSIRO_b_S_mean.data + Obs_S.data)   
    
    
    #-------------------------------------------------------------------------
    #PART 6: PRINT DATAtasmi
    import csv
    with open('output_DailyTasdataV3a.csv', 'wb') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        
        writer.writerow(['Parameter', 'Means'])
        
    #PART 6A: WRITE NORTHERN DATA
        writer.writerow(["CCCmaCanRCM_past_N_mean"] + CCCmaCanRCM_past_N_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["CCCmaSMHI_past_N_mean"] + CCCmaSMHI_past_N_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["CNRM_past_N_mean"] + CNRM_past_N_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["CNRMSMHI_past_N_mean"] +CNRMSMHI_past_N_mean.data.flatten().astype(np.str).tolist())   
        writer.writerow(["CSIRO_past_N_mean"] +CSIRO_past_N_mean.data.flatten().astype(np.str).tolist()) 
        
        writer.writerow(["CCCmaCanRCM_30_N_mean"] + CCCmaCanRCM_30_N_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["CCCmaSMHI_30_N_mean"] + CCCmaSMHI_30_N_mean.data.flatten().astype(np.str).tolist())  
        writer.writerow(["CNRM_30_N_mean"] + CNRM_30_N_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["CNRMSMHI_30_N_mean"] +CNRMSMHI_30_N_mean.data.flatten().astype(np.str).tolist())   
        writer.writerow(["CSIRO_30_N_mean"] +CSIRO_30_N_mean.data.flatten().astype(np.str).tolist())   
        
        writer.writerow(["CCCmaCanRCM85_30_N_mean"] + CCCmaCanRCM85_30_N_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["CCCmaSMHI85_30_N_mean"] + CCCmaSMHI85_30_N_mean.data.flatten().astype(np.str).tolist())           
        writer.writerow(["CNRM85_30_N_mean"] + CNRM85_30_N_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["CNRMSMHI85_30_N_mean"] +CNRMSMHI85_30_N_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["CSIRO85_30_N_mean"] +CSIRO85_30_N_mean.data.flatten().astype(np.str).tolist())  
        
        writer.writerow(["CCCmaCanRCM_50_N_mean"] + CCCmaCanRCM_50_N_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["CCCmaSMHI_50_N_mean"] + CCCmaSMHI_50_N_mean.data.flatten().astype(np.str).tolist())  
        writer.writerow(["CNRM_50_N_mean"] + CNRM_50_N_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["CNRMSMHI_50_N_mean"] +CNRMSMHI_50_N_mean.data.flatten().astype(np.str).tolist())   
        writer.writerow(["CSIRO_50_N_mean"] +CSIRO_50_N_mean.data.flatten().astype(np.str).tolist())   
        
        writer.writerow(["CCCmaCanRCM85_50_N_mean"] + CCCmaCanRCM85_50_N_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["CCCmaSMHI85_50_N_mean"] + CCCmaSMHI85_50_N_mean.data.flatten().astype(np.str).tolist())           
        writer.writerow(["CNRM85_50_N_mean"] + CNRM85_50_N_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["CNRMSMHI85_50_N_mean"] +CNRMSMHI85_50_N_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["CSIRO85_50_N_mean"] +CSIRO85_50_N_mean.data.flatten().astype(np.str).tolist())   
        
    #PART 6B: WRITE CENTRAL DATA
        writer.writerow(["CCCmaCanRCM_past_C_mean"] + CCCmaCanRCM_past_C_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["CCCmaSMHI_past_C_mean"] + CCCmaSMHI_past_C_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["CNRM_past_C_mean"] + CNRM_past_C_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["CNRMSMHI_past_C_mean"] +CNRMSMHI_past_C_mean.data.flatten().astype(np.str).tolist())   
        writer.writerow(["CSIRO_past_C_mean"] +CSIRO_past_C_mean.data.flatten().astype(np.str).tolist())    
        
        writer.writerow(["CCCmaCanRCM_30_C_mean"] + CCCmaCanRCM_30_C_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["CCCmaSMHI_30_C_mean"] + CCCmaSMHI_30_C_mean.data.flatten().astype(np.str).tolist())  
        writer.writerow(["CNRM_30_C_mean"] + CNRM_30_C_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["CNRMSMHI_30_C_mean"] +CNRMSMHI_30_C_mean.data.flatten().astype(np.str).tolist())   
        writer.writerow(["CSIRO_30_C_mean"] +CSIRO_30_C_mean.data.flatten().astype(np.str).tolist()) 
        
        writer.writerow(["CCCmaCanRCM85_30_C_mean"] + CCCmaCanRCM85_30_C_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["CCCmaSMHI85_30_C_mean"] + CCCmaSMHI85_30_C_mean.data.flatten().astype(np.str).tolist())           
        writer.writerow(["CNRM85_30_C_mean"] + CNRM85_30_C_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["CNRMSMHI85_30_C_mean"] +CNRMSMHI85_30_C_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["CSIRO85_30_C_mean"] +CSIRO85_30_C_mean.data.flatten().astype(np.str).tolist())
        
        writer.writerow(["CCCmaCanRCM_50_C_mean"] + CCCmaCanRCM_50_C_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["CCCmaSMHI_50_C_mean"] + CCCmaSMHI_50_C_mean.data.flatten().astype(np.str).tolist())  
        writer.writerow(["CNRM_50_C_mean"] + CNRM_50_C_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["CNRMSMHI_50_C_mean"] +CNRMSMHI_50_C_mean.data.flatten().astype(np.str).tolist())   
        writer.writerow(["CSIRO_50_C_mean"] +CSIRO_50_C_mean.data.flatten().astype(np.str).tolist())     
        
        writer.writerow(["CCCmaCanRCM85_50_C_mean"] + CCCmaCanRCM85_50_C_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["CCCmaSMHI85_50_C_mean"] + CCCmaSMHI85_50_C_mean.data.flatten().astype(np.str).tolist())           
        writer.writerow(["CNRM85_50_C_mean"] + CNRM85_50_C_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["CNRMSMHI85_50_C_mean"] +CNRMSMHI85_50_C_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["CSIRO85_50_C_mean"] +CSIRO85_50_C_mean.data.flatten().astype(np.str).tolist())  
        
    #PART 6C: WRITE SOUTHERN DATA
        writer.writerow(["CCCmaCanRCM_past_S_mean"] + CCCmaCanRCM_past_S_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["CCCmaSMHI_past_S_mean"] + CCCmaSMHI_past_S_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["CNRM_past_S_mean"] + CNRM_past_S_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["CNRMSMHI_past_S_mean"] +CNRMSMHI_past_S_mean.data.flatten().astype(np.str).tolist())   
        writer.writerow(["CSIRO_past_S_mean"] +CSIRO_past_S_mean.data.flatten().astype(np.str).tolist())   
        
        writer.writerow(["CCCmaCanRCM_30_S_mean"] + CCCmaCanRCM_30_S_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["CCCmaSMHI_30_S_mean"] + CCCmaSMHI_30_S_mean.data.flatten().astype(np.str).tolist())  
        writer.writerow(["CNRM_30_S_mean"] + CNRM_30_S_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["CNRMSMHI_30_S_mean"] +CNRMSMHI_30_S_mean.data.flatten().astype(np.str).tolist())   
        writer.writerow(["CSIRO_30_S_mean"] +CSIRO_30_S_mean.data.flatten().astype(np.str).tolist())     
        
        writer.writerow(["CCCmaCanRCM85_30_S_mean"] + CCCmaCanRCM85_30_S_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["CCCmaSMHI85_30_S_mean"] + CCCmaSMHI85_30_S_mean.data.flatten().astype(np.str).tolist())           
        writer.writerow(["CNRM85_30_S_mean"] + CNRM85_30_S_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["CNRMSMHI85_30_S_mean"] +CNRMSMHI85_30_S_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["CSIRO85_30_S_mean"] +CSIRO85_30_S_mean.data.flatten().astype(np.str).tolist())    
        
        writer.writerow(["CCCmaCanRCM_50_S_mean"] + CCCmaCanRCM_50_S_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["CCCmaSMHI_50_S_mean"] + CCCmaSMHI_50_S_mean.data.flatten().astype(np.str).tolist())  
        writer.writerow(["CNRM_50_S_mean"] + CNRM_50_S_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["CNRMSMHI_50_S_mean"] +CNRMSMHI_50_S_mean.data.flatten().astype(np.str).tolist())   
        writer.writerow(["CSIRO_50_S_mean"] +CSIRO_50_S_mean.data.flatten().astype(np.str).tolist())      
        
        writer.writerow(["CCCmaCanRCM85_50_S_mean"] + CCCmaCanRCM85_50_S_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["CCCmaSMHI85_50_S_mean"] + CCCmaSMHI85_50_S_mean.data.flatten().astype(np.str).tolist())           
        writer.writerow(["CNRM85_50_S_mean"] + CNRM85_50_S_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["CNRMSMHI85_50_S_mean"] +CNRMSMHI85_50_S_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["CSIRO85_50_S_mean"] +CSIRO85_50_S_mean.data.flatten().astype(np.str).tolist())        
        

if __name__ == '__main__':
    main()
        
        