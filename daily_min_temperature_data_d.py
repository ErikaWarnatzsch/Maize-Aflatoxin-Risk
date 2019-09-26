"""
Created on Wednesday August 7th 2019

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
    MPICCLM_past = '/exports/csce/datastore/geos/users/s0899345/AFR_44_tasmin/Historical_daily/tasmin_AFR-44_MPI-M-MPI-ESM-LR_historical_r1i1p1_CLMcom-CCLM4-8-17_v1_day_19710101-20001231.nc'     
    MPIREMO_past = '/exports/csce/datastore/geos/users/s0899345/AFR_44_tasmin/Historical_daily/tasmin_AFR-44_MPI-M-MPI-ESM-LR_historical_r1i1p1_MPI-CSC-REMO2009_v1_day_19710101-20001231.nc'    
    MPISMHI_past = '/exports/csce/datastore/geos/users/s0899345/AFR_44_tasmin/Historical_daily/tasmin_AFR-44_MPI-M-MPI-ESM-LR_historical_r1i1p1_SMHI-RCA4_v1_day_19710101-20001231.nc'
    NCCSMHI_past = '/exports/csce/datastore/geos/users/s0899345/AFR_44_tasmin/Historical_daily/tasmin_AFR-44_NCC-NorESM1-M_historical_r1i1p1_SMHI-RCA4_v1_day_19710101-20001231.nc'   
    NOAA_past = '/exports/csce/datastore/geos/users/s0899345/AFR_44_tasmin/Historical_daily/tasmin_AFR-44_NOAA-GFDL-GFDL-ESM2M_historical_r1i1p1_SMHI-RCA4_v1_day_19710101-20001231.nc'   
    
    #Load exactly one cube from given file
    MPICCLM_past =  iris.load_cube(MPICCLM_past, 'air_temperature')
    MPIREMO_past =  iris.load_cube(MPIREMO_past)
    MPISMHI_past =  iris.load_cube(MPISMHI_past)
    NCCSMHI_past =  iris.load_cube(NCCSMHI_past)
    NOAA_past =  iris.load_cube(NOAA_past)
    
    #remove flat latitude and longitude and only use grid latitude and grid longitude to make consistent with the observed data, also make sure all of the longitudes are monotonic. 
    
    lats = iris.coords.DimCoord(MPICCLM_past.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = MPICCLM_past.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees')    
    
    MPICCLM_past.remove_coord('latitude')
    MPICCLM_past.remove_coord('longitude')
    MPICCLM_past.remove_coord('grid_latitude')
    MPICCLM_past.remove_coord('grid_longitude')
    MPICCLM_past.add_dim_coord(lats, 1)
    MPICCLM_past.add_dim_coord(lons, 2)
    
    lats = iris.coords.DimCoord(MPIREMO_past.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = MPIREMO_past.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees') 
    
    MPIREMO_past.remove_coord('latitude')
    MPIREMO_past.remove_coord('longitude')
    MPIREMO_past.remove_coord('grid_latitude')
    MPIREMO_past.remove_coord('grid_longitude')
    MPIREMO_past.add_dim_coord(lats, 1)
    MPIREMO_past.add_dim_coord(lons, 2)
    
    lats = iris.coords.DimCoord(MPISMHI_past.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = MPISMHI_past.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees') 
    
    MPISMHI_past.remove_coord('latitude')
    MPISMHI_past.remove_coord('longitude')
    MPISMHI_past.remove_coord('grid_latitude')
    MPISMHI_past.remove_coord('grid_longitude')
    MPISMHI_past.add_dim_coord(lats, 1)
    MPISMHI_past.add_dim_coord(lons, 2)
    
    lats = iris.coords.DimCoord(NCCSMHI_past.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = NCCSMHI_past.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees') 
    
    NCCSMHI_past.remove_coord('latitude')
    NCCSMHI_past.remove_coord('longitude')
    NCCSMHI_past.remove_coord('grid_latitude')
    NCCSMHI_past.remove_coord('grid_longitude')
    NCCSMHI_past.add_dim_coord(lats, 1)
    NCCSMHI_past.add_dim_coord(lons, 2)
    
    lats = iris.coords.DimCoord(NOAA_past.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = NOAA_past.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees')
    
    NOAA_past.remove_coord('latitude')
    NOAA_past.remove_coord('longitude')
    NOAA_past.remove_coord('grid_latitude')
    NOAA_past.remove_coord('grid_longitude')
    NOAA_past.add_dim_coord(lats, 1)
    NOAA_past.add_dim_coord(lons, 2)
    
    #guess bounds    
    MPICCLM_past.coord('latitude').guess_bounds()
    MPIREMO_past.coord('latitude').guess_bounds()
    MPISMHI_past.coord('latitude').guess_bounds()
    NCCSMHI_past.coord('latitude').guess_bounds()
    NOAA_past.coord('latitude').guess_bounds()
    
    MPICCLM_past.coord('longitude').guess_bounds()
    MPIREMO_past.coord('longitude').guess_bounds()
    MPISMHI_past.coord('longitude').guess_bounds()
    NCCSMHI_past.coord('longitude').guess_bounds()
    NOAA_past.coord('longitude').guess_bounds()
    
    
    #-------------------------------------------------------------------------
    #PART 2: LOAD and FORMAT PROJECTED MODELS   
    MPICCLM = '/exports/csce/datastore/geos/users/s0899345/AFR_44_tasmin/4.5/tasmin_AFR-44_MPI-M-MPI-ESM-LR_rcp45_r1i1p1_CLMcom-CCLM4-8-17_v1_day_20060101-20701231.nc'     
    MPIREMO = '/exports/csce/datastore/geos/users/s0899345/AFR_44_tasmin/4.5/tasmin_AFR-44_MPI-M-MPI-ESM-LR_rcp45_r1i1p1_MPI-CSC-REMO2009_v1_day_20060101-20701231.nc'    
    MPISMHI = '/exports/csce/datastore/geos/users/s0899345/AFR_44_tasmin/4.5/tasmin_AFR-44_MPI-M-MPI-ESM-LR_rcp45_r1i1p1_SMHI-RCA4_v1_day_20060101-20701231.nc'   
    NCCSMHI = '/exports/csce/datastore/geos/users/s0899345/AFR_44_tasmin/4.5/tasmin_AFR-44_NCC-NorESM1-M_rcp45_r1i1p1_SMHI-RCA4_v1_day_20060101-20701231.nc'   
    NOAA = '/exports/csce/datastore/geos/users/s0899345/AFR_44_tasmin/4.5/tasmin_AFR-44_NOAA-GFDL-GFDL-ESM2M_rcp45_r1i1p1_SMHI-RCA4_v1_day_20060101-20701231.nc'     
    
    MPICCLM85 = '/exports/csce/datastore/geos/users/s0899345/AFR_44_tasmin/8.5/tasmin_AFR-44_MPI-M-MPI-ESM-LR_rcp85_r1i1p1_CLMcom-CCLM4-8-17_v1_day_20060101-20701231.nc'     
    MPIREMO85 = '/exports/csce/datastore/geos/users/s0899345/AFR_44_tasmin/8.5/tasmin_AFR-44_MPI-M-MPI-ESM-LR_rcp85_r1i1p1_MPI-CSC-REMO2009_v1_day_20060101-20701231.nc'    
    MPISMHI85 = '/exports/csce/datastore/geos/users/s0899345/AFR_44_tasmin/8.5/tasmin_AFR-44_MPI-M-MPI-ESM-LR_rcp85_r1i1p1_SMHI-RCA4_v1_day_20060101-20701231.nc'
    NCCSMHI85 = '/exports/csce/datastore/geos/users/s0899345/AFR_44_tasmin/8.5/tasmin_AFR-44_NCC-NorESM1-M_rcp85_r1i1p1_SMHI-RCA4_v1_day_20060101-20701231.nc'   
    NOAA85 = '/exports/csce/datastore/geos/users/s0899345/AFR_44_tasmin/8.5/tasmin_AFR-44_NOAA-GFDL-GFDL-ESM2M_rcp85_r1i1p1_SMHI-RCA4_v1_day_20060101-20701231.nc' 
    
    #Load exactly one cube from given file
    MPICCLM = iris.load_cube(MPICCLM)
    MPIREMO = iris.load_cube(MPIREMO)
    MPISMHI = iris.load_cube(MPISMHI)
    NCCSMHI = iris.load_cube(NCCSMHI)
    NOAA = iris.load_cube(NOAA)
    
    MPICCLM85 = iris.load_cube(MPICCLM85)
    MPIREMO85 = iris.load_cube(MPIREMO85)
    MPISMHI85 = iris.load_cube(MPISMHI85)
    NCCSMHI85 = iris.load_cube(NCCSMHI85)
    NOAA85 = iris.load_cube(NOAA85)
    
    #remove flat latitude and longitude and only use grid latitude and grid longitude to make consistent with the observed data, also make sure all of the longitudes are monotonic.    
    lats = iris.coords.DimCoord(MPICCLM.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = MPICCLM.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees')    
    
    MPICCLM.remove_coord('latitude')
    MPICCLM.remove_coord('longitude')
    MPICCLM.remove_coord('grid_latitude')
    MPICCLM.remove_coord('grid_longitude')
    MPICCLM.add_dim_coord(lats, 1)
    MPICCLM.add_dim_coord(lons, 2)
    
    lats = iris.coords.DimCoord(MPIREMO.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = MPIREMO.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees') 
    
    MPIREMO.remove_coord('latitude')
    MPIREMO.remove_coord('longitude')
    MPIREMO.remove_coord('grid_latitude')
    MPIREMO.remove_coord('grid_longitude')
    MPIREMO.add_dim_coord(lats, 1)
    MPIREMO.add_dim_coord(lons, 2)
    
    lats = iris.coords.DimCoord(MPISMHI.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = MPISMHI.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees') 
    
    MPISMHI.remove_coord('latitude')
    MPISMHI.remove_coord('longitude')
    MPISMHI.remove_coord('grid_latitude')
    MPISMHI.remove_coord('grid_longitude')
    MPISMHI.add_dim_coord(lats, 1)
    MPISMHI.add_dim_coord(lons, 2)
    
    lats = iris.coords.DimCoord(NCCSMHI.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = NCCSMHI.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees') 
    
    NCCSMHI.remove_coord('latitude')
    NCCSMHI.remove_coord('longitude')
    NCCSMHI.remove_coord('grid_latitude')
    NCCSMHI.remove_coord('grid_longitude')
    NCCSMHI.add_dim_coord(lats, 1)
    NCCSMHI.add_dim_coord(lons, 2)
    
    lats = iris.coords.DimCoord(NOAA.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = NOAA.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees')
    
    NOAA.remove_coord('latitude')
    NOAA.remove_coord('longitude')
    NOAA.remove_coord('grid_latitude')
    NOAA.remove_coord('grid_longitude')
    NOAA.add_dim_coord(lats, 1)
    NOAA.add_dim_coord(lons, 2)
    
    lats = iris.coords.DimCoord(MPICCLM85.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = MPICCLM85.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees')    
    
    MPICCLM85.remove_coord('latitude')
    MPICCLM85.remove_coord('longitude')
    MPICCLM85.remove_coord('grid_latitude')
    MPICCLM85.remove_coord('grid_longitude')
    MPICCLM85.add_dim_coord(lats, 1)
    MPICCLM85.add_dim_coord(lons, 2)
    
    lats = iris.coords.DimCoord(MPIREMO85.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = MPIREMO85.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees') 
    
    MPIREMO85.remove_coord('latitude')
    MPIREMO85.remove_coord('longitude')
    MPIREMO85.remove_coord('grid_latitude')
    MPIREMO85.remove_coord('grid_longitude')
    MPIREMO85.add_dim_coord(lats, 1)
    MPIREMO85.add_dim_coord(lons, 2)
    
    lats = iris.coords.DimCoord(MPISMHI85.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = MPISMHI85.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees') 
    
    MPISMHI85.remove_coord('latitude')
    MPISMHI85.remove_coord('longitude')
    MPISMHI85.remove_coord('grid_latitude')
    MPISMHI85.remove_coord('grid_longitude')
    MPISMHI85.add_dim_coord(lats, 1)
    MPISMHI85.add_dim_coord(lons, 2)
    
    lats = iris.coords.DimCoord(NCCSMHI85.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = NCCSMHI85.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees') 
    
    NCCSMHI85.remove_coord('latitude')
    NCCSMHI85.remove_coord('longitude')
    NCCSMHI85.remove_coord('grid_latitude')
    NCCSMHI85.remove_coord('grid_longitude')
    NCCSMHI85.add_dim_coord(lats, 1)
    NCCSMHI85.add_dim_coord(lons, 2)
    
    lats = iris.coords.DimCoord(NOAA85.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = NOAA85.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees')
    
    NOAA85.remove_coord('latitude')
    NOAA85.remove_coord('longitude')
    NOAA85.remove_coord('grid_latitude')
    NOAA85.remove_coord('grid_longitude')
    NOAA85.add_dim_coord(lats, 1)
    NOAA85.add_dim_coord(lons, 2)
    
    #guess bounds   
    MPICCLM.coord('latitude').guess_bounds()
    MPIREMO.coord('latitude').guess_bounds()
    MPISMHI.coord('latitude').guess_bounds()
    NCCSMHI.coord('latitude').guess_bounds()
    NOAA.coord('latitude').guess_bounds()
    
    MPICCLM85.coord('latitude').guess_bounds()
    MPIREMO85.coord('latitude').guess_bounds()
    MPISMHI85.coord('latitude').guess_bounds()
    NCCSMHI85.coord('latitude').guess_bounds()
    NOAA85.coord('latitude').guess_bounds()
    
    MPICCLM.coord('longitude').guess_bounds()
    MPIREMO.coord('longitude').guess_bounds()
    MPISMHI.coord('longitude').guess_bounds()
    NCCSMHI.coord('longitude').guess_bounds()
    NOAA.coord('longitude').guess_bounds()
    
    MPICCLM85.coord('longitude').guess_bounds()
    MPIREMO85.coord('longitude').guess_bounds()
    MPISMHI85.coord('longitude').guess_bounds()
    NCCSMHI85.coord('longitude').guess_bounds()
    NOAA85.coord('longitude').guess_bounds()
    
    
    #-------------------------------------------------------------------------
    #PART 3: LOAD AND FORMAT OBSERVED DATA
    #bring in all the files we need and give them a name
    CRU= '/exports/csce/datastore/geos/users/s0899345/Actual_Data/cru_ts4.01.1901.2016.tmn.dat.nc'
    
    #Load exactly one cube from given file
    CRU = iris.load_cube(CRU, 'near-surface temperature minimum')
    
    #guess bounds  
    CRU.coord('latitude').guess_bounds()
    
    CRU.coord('longitude').guess_bounds()
    
    
    #-------------------------------------------------------------------------
    #PART 4: FORMAT DATA GENERAL
    #Convert units to match, CORDEX data is in Kelvin but Observed data in Celsius, we would like to show all data in Celsius
    MPICCLM_past.convert_units('Celsius')
    MPIREMO_past.convert_units('Celsius') 
    MPISMHI_past.convert_units('Celsius')
    NCCSMHI_past.convert_units('Celsius')
    NOAA_past.convert_units('Celsius')
    
    MPICCLM.convert_units('Celsius')
    MPIREMO.convert_units('Celsius') 
    MPISMHI.convert_units('Celsius')
    NCCSMHI.convert_units('Celsius')
    NOAA.convert_units('Celsius')
    
    MPICCLM85.convert_units('Celsius')
    MPIREMO85.convert_units('Celsius') 
    MPISMHI85.convert_units('Celsius')
    NCCSMHI85.convert_units('Celsius')
    NOAA85.convert_units('Celsius')
    
    #rename units to match
    CRU.units = Unit('Celsius') 
    
    #limit time series of data
    #time constraint to make past and obsered data only from 1971-2000 
    iris.FUTURE.cell_datetime_objects = True
    t_constraint_past = iris.Constraint(time=lambda cell: 1971 <= cell.point.year <= 2000)
    
    MPICCLM_past =  MPICCLM_past.extract(t_constraint_past)
    MPIREMO_past =  MPIREMO_past.extract(t_constraint_past)
    MPISMHI_past =  MPISMHI_past.extract(t_constraint_past)
    NCCSMHI_past =  NCCSMHI_past.extract(t_constraint_past)
    NOAA_past =  NOAA_past.extract(t_constraint_past)
    
    CRU = CRU.extract(t_constraint_past)
    
    #time constraint to make future data only from 2020-2049
    iris.FUTURE.cell_datetime_objects = True
    t_constraint_future = iris.Constraint(time=lambda cell: 2020 <= cell.point.year <= 2049)
    
    MPICCLM_30 = MPICCLM.extract(t_constraint_future)
    MPIREMO_30 = MPIREMO.extract(t_constraint_future)
    MPISMHI_30 = MPISMHI.extract(t_constraint_future)
    NCCSMHI_30 = NCCSMHI.extract(t_constraint_future)
    NOAA_30 = NOAA.extract(t_constraint_future)
    
    MPICCLM85_30 = MPICCLM85.extract(t_constraint_future)
    MPIREMO85_30 = MPIREMO85.extract(t_constraint_future)
    MPISMHI85_30 = MPISMHI85.extract(t_constraint_future)
    NCCSMHI85_30 = NCCSMHI85.extract(t_constraint_future)
    NOAA85_30 = NOAA85.extract(t_constraint_future)
    
    #time constraint to make future data only from 2040-2069
    iris.FUTURE.cell_datetime_objects = True
    t_constraint_future = iris.Constraint(time=lambda cell: 2040 <= cell.point.year <= 2069)
    
    MPICCLM_50 = MPICCLM.extract(t_constraint_future)
    MPIREMO_50 = MPIREMO.extract(t_constraint_future)
    MPISMHI_50 = MPISMHI.extract(t_constraint_future)
    NCCSMHI_50 = NCCSMHI.extract(t_constraint_future)
    NOAA_50 = NOAA.extract(t_constraint_future)
    
    MPICCLM85_50 = MPICCLM85.extract(t_constraint_future)
    MPIREMO85_50 = MPIREMO85.extract(t_constraint_future)
    MPISMHI85_50 = MPISMHI85.extract(t_constraint_future)
    NCCSMHI85_50 = NCCSMHI85.extract(t_constraint_future)
    NOAA85_50 = NOAA85.extract(t_constraint_future)
    
    
    #-------------------------------------------------------------------------
    #PART 5: FORMAT DATA TO GEOGRAPHICALLY SPECIFIC AND RE-BASELINE
    #PART 5A: NORTHERN MALAWI
    #we are only interested in the latitude and longitude relevant to Central Malawi 
    Northern_Malawi = iris.Constraint(longitude=lambda v: 32.5 <= v <= 35, latitude=lambda v: -12.5 <= v <= -8.5) 
    
    MPICCLM_past_N = MPICCLM_past.extract(Northern_Malawi)
    MPIREMO_past_N = MPIREMO_past.extract(Northern_Malawi)
    MPISMHI_past_N = MPISMHI_past.extract(Northern_Malawi)
    NCCSMHI_past_N = NCCSMHI_past.extract(Northern_Malawi)
    NOAA_past_N = NOAA_past.extract(Northern_Malawi)
    
    MPICCLM_30_N = MPICCLM_30.extract(Northern_Malawi)
    MPIREMO_30_N = MPIREMO_30.extract(Northern_Malawi)
    MPISMHI_30_N = MPISMHI_30.extract(Northern_Malawi)
    NCCSMHI_30_N = NCCSMHI_30.extract(Northern_Malawi)
    NOAA_30_N = NOAA_30.extract(Northern_Malawi)
    
    MPICCLM85_30_N = MPICCLM85_30.extract(Northern_Malawi)
    MPIREMO85_30_N = MPIREMO85_30.extract(Northern_Malawi)
    MPISMHI85_30_N = MPISMHI85_30.extract(Northern_Malawi)
    NCCSMHI85_30_N = NCCSMHI85_30.extract(Northern_Malawi)
    NOAA85_30_N = NOAA85_30.extract(Northern_Malawi)
    
    MPICCLM_50_N = MPICCLM_50.extract(Northern_Malawi)
    MPIREMO_50_N = MPIREMO_50.extract(Northern_Malawi)
    MPISMHI_50_N = MPISMHI_50.extract(Northern_Malawi)
    NCCSMHI_50_N = NCCSMHI_50.extract(Northern_Malawi)
    NOAA_50_N = NOAA_50.extract(Northern_Malawi)
    
    MPICCLM85_50_N = MPICCLM85_50.extract(Northern_Malawi)
    MPIREMO85_50_N = MPIREMO85_50.extract(Northern_Malawi)
    MPISMHI85_50_N = MPISMHI85_50.extract(Northern_Malawi)
    NCCSMHI85_50_N = NCCSMHI85_50.extract(Northern_Malawi)
    NOAA85_50_N = NOAA85_50.extract(Northern_Malawi)
    
    CRU_N = CRU.extract(Northern_Malawi)
    
    #Returns an array of area weights, with the same dimensions as the cube
    MPICCLM_past_N_grid_areas = iris.analysis.cartography.area_weights(MPICCLM_past_N)
    MPIREMO_past_N_grid_areas = iris.analysis.cartography.area_weights(MPIREMO_past_N)
    MPISMHI_past_N_grid_areas = iris.analysis.cartography.area_weights(MPISMHI_past_N)
    NCCSMHI_past_N_grid_areas = iris.analysis.cartography.area_weights(NCCSMHI_past_N)
    NOAA_past_N_grid_areas = iris.analysis.cartography.area_weights(NOAA_past_N)
    
    MPICCLM_30_N_grid_areas = iris.analysis.cartography.area_weights(MPICCLM_30_N)
    MPIREMO_30_N_grid_areas = iris.analysis.cartography.area_weights(MPIREMO_30_N)
    MPISMHI_30_N_grid_areas = iris.analysis.cartography.area_weights(MPISMHI_30_N)
    NCCSMHI_30_N_grid_areas = iris.analysis.cartography.area_weights(NCCSMHI_30_N)
    NOAA_30_N_grid_areas = iris.analysis.cartography.area_weights(NOAA_30_N)
    
    MPICCLM85_30_N_grid_areas = iris.analysis.cartography.area_weights(MPICCLM85_30_N)
    MPIREMO85_30_N_grid_areas = iris.analysis.cartography.area_weights(MPIREMO85_30_N)
    MPISMHI85_30_N_grid_areas = iris.analysis.cartography.area_weights(MPISMHI85_30_N)
    NCCSMHI85_30_N_grid_areas = iris.analysis.cartography.area_weights(NCCSMHI85_30_N)
    NOAA85_30_N_grid_areas = iris.analysis.cartography.area_weights(NOAA85_30_N)
    
    MPICCLM_50_N_grid_areas = iris.analysis.cartography.area_weights(MPICCLM_50_N)
    MPIREMO_50_N_grid_areas = iris.analysis.cartography.area_weights(MPIREMO_50_N)
    MPISMHI_50_N_grid_areas = iris.analysis.cartography.area_weights(MPISMHI_50_N)
    NCCSMHI_50_N_grid_areas = iris.analysis.cartography.area_weights(NCCSMHI_50_N)
    NOAA_50_N_grid_areas = iris.analysis.cartography.area_weights(NOAA_50_N)
    
    MPICCLM85_50_N_grid_areas = iris.analysis.cartography.area_weights(MPICCLM85_50_N)
    MPIREMO85_50_N_grid_areas = iris.analysis.cartography.area_weights(MPIREMO85_50_N)
    MPISMHI85_50_N_grid_areas = iris.analysis.cartography.area_weights(MPISMHI85_50_N)
    NCCSMHI85_50_N_grid_areas = iris.analysis.cartography.area_weights(NCCSMHI85_50_N)
    NOAA85_50_N_grid_areas = iris.analysis.cartography.area_weights(NOAA85_50_N)
    
    CRU_N_grid_areas = iris.analysis.cartography.area_weights(CRU_N)
    
    #We want to plot the mean for the whole region so we need a mean of all the lats and lons
    MPICCLM_past_N_mean = MPICCLM_past_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MPICCLM_past_N_grid_areas) 
    MPIREMO_past_N_mean = MPIREMO_past_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MPIREMO_past_N_grid_areas)
    MPISMHI_past_N_mean = MPISMHI_past_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MPISMHI_past_N_grid_areas)
    NCCSMHI_past_N_mean = NCCSMHI_past_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=NCCSMHI_past_N_grid_areas)
    NOAA_past_N_mean = NOAA_past_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=NOAA_past_N_grid_areas)
    
    MPICCLM_30_N_mean = MPICCLM_30_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MPICCLM_30_N_grid_areas) 
    MPIREMO_30_N_mean = MPIREMO_30_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MPIREMO_30_N_grid_areas)
    MPISMHI_30_N_mean = MPISMHI_30_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MPISMHI_30_N_grid_areas)
    NCCSMHI_30_N_mean = NCCSMHI_30_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=NCCSMHI_30_N_grid_areas)
    NOAA_30_N_mean = NOAA_30_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=NOAA_30_N_grid_areas)
    
    MPICCLM85_30_N_mean = MPICCLM85_30_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MPICCLM85_30_N_grid_areas) 
    MPIREMO85_30_N_mean = MPIREMO85_30_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MPIREMO85_30_N_grid_areas)
    MPISMHI85_30_N_mean = MPISMHI85_30_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MPISMHI85_30_N_grid_areas)
    NCCSMHI85_30_N_mean = NCCSMHI85_30_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=NCCSMHI85_30_N_grid_areas)
    NOAA85_30_N_mean = NOAA85_30_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=NOAA85_30_N_grid_areas)
    
    MPICCLM_50_N_mean = MPICCLM_50_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MPICCLM_50_N_grid_areas) 
    MPIREMO_50_N_mean = MPIREMO_50_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MPIREMO_50_N_grid_areas)
    MPISMHI_50_N_mean = MPISMHI_50_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MPISMHI_50_N_grid_areas)
    NCCSMHI_50_N_mean = NCCSMHI_50_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=NCCSMHI_50_N_grid_areas)
    NOAA_50_N_mean = NOAA_50_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=NOAA_50_N_grid_areas)
    
    MPICCLM85_50_N_mean = MPICCLM85_50_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MPICCLM85_50_N_grid_areas) 
    MPIREMO85_50_N_mean = MPIREMO85_50_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MPIREMO85_50_N_grid_areas)
    MPISMHI85_50_N_mean = MPISMHI85_50_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MPISMHI85_50_N_grid_areas)
    NCCSMHI85_50_N_mean = NCCSMHI85_50_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=NCCSMHI85_50_N_grid_areas)
    NOAA85_50_N_mean = NOAA85_50_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=NOAA85_50_N_grid_areas)
    
    CRU_N_mean = CRU_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CRU_N_grid_areas)
    
    #for the baseline we don't need to average for each year, but the average for the whole time period, so collapse by time
    MPICCLM_b_N_mean = MPICCLM_past_N_mean.collapsed(['time'], iris.analysis.MEAN)  
    MPIREMO_b_N_mean = MPIREMO_past_N_mean.collapsed(['time'], iris.analysis.MEAN) 
    MPISMHI_b_N_mean = MPISMHI_past_N_mean.collapsed(['time'], iris.analysis.MEAN) 
    NCCSMHI_b_N_mean = NCCSMHI_past_N_mean.collapsed(['time'], iris.analysis.MEAN) 
    NOAA_b_N_mean = NOAA_past_N_mean.collapsed(['time'], iris.analysis.MEAN)
    
    CRU_N_mean = CRU_N_mean.collapsed(['time'], iris.analysis.MEAN) 
    
    #create average of observed baseline data
    Obs_N = (CRU_N_mean)
    
    #We want to see the change in temperature from the baseline
    MPICCLM_past_N_mean = (MPICCLM_past_N_mean.data - MPICCLM_b_N_mean.data + Obs_N.data) 
    MPIREMO_past_N_mean = (MPIREMO_past_N_mean.data - MPIREMO_b_N_mean.data + Obs_N.data)
    MPISMHI_past_N_mean = (MPISMHI_past_N_mean.data - MPISMHI_b_N_mean.data + Obs_N.data)
    NCCSMHI_past_N_mean = (NCCSMHI_past_N_mean.data - NCCSMHI_b_N_mean.data + Obs_N.data)
    NOAA_past_N_mean = (NOAA_past_N_mean.data - NOAA_b_N_mean.data + Obs_N.data)
    
    MPICCLM_30_N_mean = (MPICCLM_30_N_mean.data - MPICCLM_b_N_mean.data + Obs_N.data) 
    MPIREMO_30_N_mean = (MPIREMO_30_N_mean.data - MPIREMO_b_N_mean.data + Obs_N.data)
    MPISMHI_30_N_mean = (MPISMHI_30_N_mean.data - MPISMHI_b_N_mean.data + Obs_N.data)
    NCCSMHI_30_N_mean = (NCCSMHI_30_N_mean.data - NCCSMHI_b_N_mean.data + Obs_N.data)
    NOAA_30_N_mean = (NOAA_30_N_mean.data - NOAA_b_N_mean.data + Obs_N.data)
    
    MPICCLM85_30_N_mean = (MPICCLM85_30_N_mean.data - MPICCLM_b_N_mean.data + Obs_N.data) 
    MPIREMO85_30_N_mean = (MPIREMO85_30_N_mean.data - MPIREMO_b_N_mean.data + Obs_N.data)
    MPISMHI85_30_N_mean = (MPISMHI85_30_N_mean.data - MPISMHI_b_N_mean.data + Obs_N.data)
    NCCSMHI85_30_N_mean = (NCCSMHI85_30_N_mean.data - NCCSMHI_b_N_mean.data + Obs_N.data)
    NOAA85_30_N_mean = (NOAA85_30_N_mean.data - NOAA_b_N_mean.data + Obs_N.data)
    
    MPICCLM_50_N_mean = (MPICCLM_50_N_mean.data - MPICCLM_b_N_mean.data + Obs_N.data) 
    MPIREMO_50_N_mean = (MPIREMO_50_N_mean.data - MPIREMO_b_N_mean.data + Obs_N.data)
    MPISMHI_50_N_mean = (MPISMHI_50_N_mean.data - MPISMHI_b_N_mean.data + Obs_N.data)
    NCCSMHI_50_N_mean = (NCCSMHI_50_N_mean.data - NCCSMHI_b_N_mean.data + Obs_N.data)
    NOAA_50_N_mean = (NOAA_50_N_mean.data - NOAA_b_N_mean.data + Obs_N.data)
    
    MPICCLM85_50_N_mean = (MPICCLM85_50_N_mean.data - MPICCLM_b_N_mean.data + Obs_N.data) 
    MPIREMO85_50_N_mean = (MPIREMO85_50_N_mean.data - MPIREMO_b_N_mean.data + Obs_N.data)
    MPISMHI85_50_N_mean = (MPISMHI85_50_N_mean.data - MPISMHI_b_N_mean.data + Obs_N.data)
    NCCSMHI85_50_N_mean = (NCCSMHI85_50_N_mean.data - NCCSMHI_b_N_mean.data + Obs_N.data)
    NOAA85_50_N_mean = (NOAA85_50_N_mean.data - NOAA_b_N_mean.data + Obs_N.data)
    
    
    #PART 5B: CENTRAL MALAWI
    #we are only interested in the latitude and longitude relevant to Central Malawi 
    Central_Malawi = iris.Constraint(longitude=lambda v: 32.5 <= v <= 35.5, latitude=lambda v: -15 <= v <= -11.5) 
    
    MPICCLM_past_C = MPICCLM_past.extract(Central_Malawi)
    MPIREMO_past_C = MPIREMO_past.extract(Central_Malawi)
    MPISMHI_past_C = MPISMHI_past.extract(Central_Malawi)
    NCCSMHI_past_C = NCCSMHI_past.extract(Central_Malawi)
    NOAA_past_C = NOAA_past.extract(Central_Malawi)
    
    MPICCLM_30_C = MPICCLM_30.extract(Central_Malawi)
    MPIREMO_30_C = MPIREMO_30.extract(Central_Malawi)
    MPISMHI_30_C = MPISMHI_30.extract(Central_Malawi)
    NCCSMHI_30_C = NCCSMHI_30.extract(Central_Malawi)
    NOAA_30_C = NOAA_30.extract(Central_Malawi)
    
    MPICCLM85_30_C = MPICCLM85_30.extract(Central_Malawi)
    MPIREMO85_30_C = MPIREMO85_30.extract(Central_Malawi)
    MPISMHI85_30_C = MPISMHI85_30.extract(Central_Malawi)
    NCCSMHI85_30_C = NCCSMHI85_30.extract(Central_Malawi)
    NOAA85_30_C = NOAA85_30.extract(Central_Malawi)
    
    MPICCLM_50_C = MPICCLM_50.extract(Central_Malawi)
    MPIREMO_50_C = MPIREMO_50.extract(Central_Malawi)
    MPISMHI_50_C = MPISMHI_50.extract(Central_Malawi)
    NCCSMHI_50_C = NCCSMHI_50.extract(Central_Malawi)
    NOAA_50_C = NOAA_50.extract(Central_Malawi)
    
    MPICCLM85_50_C = MPICCLM85_50.extract(Central_Malawi)
    MPIREMO85_50_C = MPIREMO85_50.extract(Central_Malawi)
    MPISMHI85_50_C = MPISMHI85_50.extract(Central_Malawi)
    NCCSMHI85_50_C = NCCSMHI85_50.extract(Central_Malawi)
    NOAA85_50_C = NOAA85_50.extract(Central_Malawi)
    
    CRU_C = CRU.extract(Central_Malawi)
    
    #Returns an array of area weights, with the same dimensions as the cube
    MPICCLM_past_C_grid_areas = iris.analysis.cartography.area_weights(MPICCLM_past_C)
    MPIREMO_past_C_grid_areas = iris.analysis.cartography.area_weights(MPIREMO_past_C)
    MPISMHI_past_C_grid_areas = iris.analysis.cartography.area_weights(MPISMHI_past_C)
    NCCSMHI_past_C_grid_areas = iris.analysis.cartography.area_weights(NCCSMHI_past_C)
    NOAA_past_C_grid_areas = iris.analysis.cartography.area_weights(NOAA_past_C)
    
    MPICCLM_30_C_grid_areas = iris.analysis.cartography.area_weights(MPICCLM_30_C)
    MPIREMO_30_C_grid_areas = iris.analysis.cartography.area_weights(MPIREMO_30_C)
    MPISMHI_30_C_grid_areas = iris.analysis.cartography.area_weights(MPISMHI_30_C)
    NCCSMHI_30_C_grid_areas = iris.analysis.cartography.area_weights(NCCSMHI_30_C)
    NOAA_30_C_grid_areas = iris.analysis.cartography.area_weights(NOAA_30_C)
    
    MPICCLM85_30_C_grid_areas = iris.analysis.cartography.area_weights(MPICCLM85_30_C)
    MPIREMO85_30_C_grid_areas = iris.analysis.cartography.area_weights(MPIREMO85_30_C)
    MPISMHI85_30_C_grid_areas = iris.analysis.cartography.area_weights(MPISMHI85_30_C)
    NCCSMHI85_30_C_grid_areas = iris.analysis.cartography.area_weights(NCCSMHI85_30_C)
    NOAA85_30_C_grid_areas = iris.analysis.cartography.area_weights(NOAA85_30_C)
    
    MPICCLM_50_C_grid_areas = iris.analysis.cartography.area_weights(MPICCLM_50_C)
    MPIREMO_50_C_grid_areas = iris.analysis.cartography.area_weights(MPIREMO_50_C)
    MPISMHI_50_C_grid_areas = iris.analysis.cartography.area_weights(MPISMHI_50_C)
    NCCSMHI_50_C_grid_areas = iris.analysis.cartography.area_weights(NCCSMHI_50_C)
    NOAA_50_C_grid_areas = iris.analysis.cartography.area_weights(NOAA_50_C)
    
    MPICCLM85_50_C_grid_areas = iris.analysis.cartography.area_weights(MPICCLM85_50_C)
    MPIREMO85_50_C_grid_areas = iris.analysis.cartography.area_weights(MPIREMO85_50_C)
    MPISMHI85_50_C_grid_areas = iris.analysis.cartography.area_weights(MPISMHI85_50_C)
    NCCSMHI85_50_C_grid_areas = iris.analysis.cartography.area_weights(NCCSMHI85_50_C)
    NOAA85_50_C_grid_areas = iris.analysis.cartography.area_weights(NOAA85_50_C)
    
    CRU_C_grid_areas = iris.analysis.cartography.area_weights(CRU_C)
    
    #We want to plot the mean for the whole region so we need a mean of all the lats and lons
    MPICCLM_past_C_mean = MPICCLM_past_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MPICCLM_past_C_grid_areas) 
    MPIREMO_past_C_mean = MPIREMO_past_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MPIREMO_past_C_grid_areas)
    MPISMHI_past_C_mean = MPISMHI_past_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MPISMHI_past_C_grid_areas)
    NCCSMHI_past_C_mean = NCCSMHI_past_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=NCCSMHI_past_C_grid_areas)
    NOAA_past_C_mean = NOAA_past_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=NOAA_past_C_grid_areas)
    
    MPICCLM_30_C_mean = MPICCLM_30_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MPICCLM_30_C_grid_areas) 
    MPIREMO_30_C_mean = MPIREMO_30_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MPIREMO_30_C_grid_areas)
    MPISMHI_30_C_mean = MPISMHI_30_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MPISMHI_30_C_grid_areas)
    NCCSMHI_30_C_mean = NCCSMHI_30_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=NCCSMHI_30_C_grid_areas)
    NOAA_30_C_mean = NOAA_30_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=NOAA_30_C_grid_areas)
    
    MPICCLM85_30_C_mean = MPICCLM85_30_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MPICCLM85_30_C_grid_areas) 
    MPIREMO85_30_C_mean = MPIREMO85_30_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MPIREMO85_30_C_grid_areas)
    MPISMHI85_30_C_mean = MPISMHI85_30_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MPISMHI85_30_C_grid_areas)
    NCCSMHI85_30_C_mean = NCCSMHI85_30_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=NCCSMHI85_30_C_grid_areas)
    NOAA85_30_C_mean = NOAA85_30_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=NOAA85_30_C_grid_areas)
    
    MPICCLM_50_C_mean = MPICCLM_50_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MPICCLM_50_C_grid_areas) 
    MPIREMO_50_C_mean = MPIREMO_50_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MPIREMO_50_C_grid_areas)
    MPISMHI_50_C_mean = MPISMHI_50_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MPISMHI_50_C_grid_areas)
    NCCSMHI_50_C_mean = NCCSMHI_50_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=NCCSMHI_50_C_grid_areas)
    NOAA_50_C_mean = NOAA_50_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=NOAA_50_C_grid_areas)
    
    MPICCLM85_50_C_mean = MPICCLM85_50_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MPICCLM85_50_C_grid_areas) 
    MPIREMO85_50_C_mean = MPIREMO85_50_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MPIREMO85_50_C_grid_areas)
    MPISMHI85_50_C_mean = MPISMHI85_50_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MPISMHI85_50_C_grid_areas)
    NCCSMHI85_50_C_mean = NCCSMHI85_50_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=NCCSMHI85_50_C_grid_areas)
    NOAA85_50_C_mean = NOAA85_50_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=NOAA85_50_C_grid_areas)
    
    CRU_C_mean = CRU_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CRU_C_grid_areas)
    
    #for the baseline we don't need to average for each year, but the average for the whole time period, so collapse by time
    MPICCLM_b_C_mean = MPICCLM_past_C_mean.collapsed(['time'], iris.analysis.MEAN)  
    MPIREMO_b_C_mean = MPIREMO_past_C_mean.collapsed(['time'], iris.analysis.MEAN) 
    MPISMHI_b_C_mean = MPISMHI_past_C_mean.collapsed(['time'], iris.analysis.MEAN) 
    NCCSMHI_b_C_mean = NCCSMHI_past_C_mean.collapsed(['time'], iris.analysis.MEAN) 
    NOAA_b_C_mean = NOAA_past_C_mean.collapsed(['time'], iris.analysis.MEAN)
    
    CRU_C_mean = CRU_C_mean.collapsed(['time'], iris.analysis.MEAN) 
    
    #create average of observed baseline data
    Obs_C = (CRU_C_mean)
    
    #We want to see the change in temperature from the baseline
    MPICCLM_past_C_mean = (MPICCLM_past_C_mean.data - MPICCLM_b_C_mean.data + Obs_C.data) 
    MPIREMO_past_C_mean = (MPIREMO_past_C_mean.data - MPIREMO_b_C_mean.data + Obs_C.data)
    MPISMHI_past_C_mean = (MPISMHI_past_C_mean.data - MPISMHI_b_C_mean.data + Obs_C.data)
    NCCSMHI_past_C_mean = (NCCSMHI_past_C_mean.data - NCCSMHI_b_C_mean.data + Obs_C.data)
    NOAA_past_C_mean = (NOAA_past_C_mean.data - NOAA_b_C_mean.data + Obs_C.data)
    
    MPICCLM_30_C_mean = (MPICCLM_30_C_mean.data - MPICCLM_b_C_mean.data + Obs_C.data) 
    MPIREMO_30_C_mean = (MPIREMO_30_C_mean.data - MPIREMO_b_C_mean.data + Obs_C.data)
    MPISMHI_30_C_mean = (MPISMHI_30_C_mean.data - MPISMHI_b_C_mean.data + Obs_C.data)
    NCCSMHI_30_C_mean = (NCCSMHI_30_C_mean.data - NCCSMHI_b_C_mean.data + Obs_C.data)
    NOAA_30_C_mean = (NOAA_30_C_mean.data - NOAA_b_C_mean.data + Obs_C.data)
    
    MPICCLM85_30_C_mean = (MPICCLM85_30_C_mean.data - MPICCLM_b_C_mean.data + Obs_C.data) 
    MPIREMO85_30_C_mean = (MPIREMO85_30_C_mean.data - MPIREMO_b_C_mean.data + Obs_C.data)
    MPISMHI85_30_C_mean = (MPISMHI85_30_C_mean.data - MPISMHI_b_C_mean.data + Obs_C.data)
    NCCSMHI85_30_C_mean = (NCCSMHI85_30_C_mean.data - NCCSMHI_b_C_mean.data + Obs_C.data)
    NOAA85_30_C_mean = (NOAA85_30_C_mean.data - NOAA_b_C_mean.data + Obs_C.data)
    
    MPICCLM_50_C_mean = (MPICCLM_50_C_mean.data - MPICCLM_b_C_mean.data + Obs_C.data) 
    MPIREMO_50_C_mean = (MPIREMO_50_C_mean.data - MPIREMO_b_C_mean.data + Obs_C.data)
    MPISMHI_50_C_mean = (MPISMHI_50_C_mean.data - MPISMHI_b_C_mean.data + Obs_C.data)
    NCCSMHI_50_C_mean = (NCCSMHI_50_C_mean.data - NCCSMHI_b_C_mean.data + Obs_C.data)
    NOAA_50_C_mean = (NOAA_50_C_mean.data - NOAA_b_C_mean.data + Obs_C.data)
    
    MPICCLM85_50_C_mean = (MPICCLM85_50_C_mean.data - MPICCLM_b_C_mean.data + Obs_C.data) 
    MPIREMO85_50_C_mean = (MPIREMO85_50_C_mean.data - MPIREMO_b_C_mean.data + Obs_C.data)
    MPISMHI85_50_C_mean = (MPISMHI85_50_C_mean.data - MPISMHI_b_C_mean.data + Obs_C.data)
    NCCSMHI85_50_C_mean = (NCCSMHI85_50_C_mean.data - NCCSMHI_b_C_mean.data + Obs_C.data)
    NOAA85_50_C_mean = (NOAA85_50_C_mean.data - NOAA_b_C_mean.data + Obs_C.data)
    
            
    #PART 5C: SOUTHERN MALAWI
    #we are only interested in the latitude and longitude relevant to Southern Malawi 
    Southern_Malawi = iris.Constraint(longitude=lambda v: 34 <= v <= 36.5, latitude=lambda v: -17.5 <= v <= -14) 
    
    MPICCLM_past_S = MPICCLM_past.extract(Southern_Malawi)
    MPIREMO_past_S = MPIREMO_past.extract(Southern_Malawi)
    MPISMHI_past_S = MPISMHI_past.extract(Southern_Malawi)
    NCCSMHI_past_S = NCCSMHI_past.extract(Southern_Malawi)
    NOAA_past_S = NOAA_past.extract(Southern_Malawi)
    
    MPICCLM_30_S = MPICCLM_30.extract(Southern_Malawi)
    MPIREMO_30_S = MPIREMO_30.extract(Southern_Malawi)
    MPISMHI_30_S = MPISMHI_30.extract(Southern_Malawi)
    NCCSMHI_30_S = NCCSMHI_30.extract(Southern_Malawi)
    NOAA_30_S = NOAA_30.extract(Southern_Malawi)
    
    MPICCLM85_30_S = MPICCLM85_30.extract(Southern_Malawi)
    MPIREMO85_30_S = MPIREMO85_30.extract(Southern_Malawi)
    MPISMHI85_30_S = MPISMHI85_30.extract(Southern_Malawi)
    NCCSMHI85_30_S = NCCSMHI85_30.extract(Southern_Malawi)
    NOAA85_30_S = NOAA85_30.extract(Southern_Malawi)
    
    MPICCLM_50_S = MPICCLM_50.extract(Southern_Malawi)
    MPIREMO_50_S = MPIREMO_50.extract(Southern_Malawi)
    MPISMHI_50_S = MPISMHI_50.extract(Southern_Malawi)
    NCCSMHI_50_S = NCCSMHI_50.extract(Southern_Malawi)
    NOAA_50_S = NOAA_50.extract(Southern_Malawi)
    
    MPICCLM85_50_S = MPICCLM85_50.extract(Southern_Malawi)
    MPIREMO85_50_S = MPIREMO85_50.extract(Southern_Malawi)
    MPISMHI85_50_S = MPISMHI85_50.extract(Southern_Malawi)
    NCCSMHI85_50_S = NCCSMHI85_50.extract(Southern_Malawi)
    NOAA85_50_S = NOAA85_50.extract(Southern_Malawi)
    
    CRU_S = CRU.extract(Southern_Malawi)
    
    #Returns an array of area weights, with the same dimensions as the cube
    MPICCLM_past_S_grid_areas = iris.analysis.cartography.area_weights(MPICCLM_past_S)
    MPIREMO_past_S_grid_areas = iris.analysis.cartography.area_weights(MPIREMO_past_S)
    MPISMHI_past_S_grid_areas = iris.analysis.cartography.area_weights(MPISMHI_past_S)
    NCCSMHI_past_S_grid_areas = iris.analysis.cartography.area_weights(NCCSMHI_past_S)
    NOAA_past_S_grid_areas = iris.analysis.cartography.area_weights(NOAA_past_S)
    
    MPICCLM_30_S_grid_areas = iris.analysis.cartography.area_weights(MPICCLM_30_S)
    MPIREMO_30_S_grid_areas = iris.analysis.cartography.area_weights(MPIREMO_30_S)
    MPISMHI_30_S_grid_areas = iris.analysis.cartography.area_weights(MPISMHI_30_S)
    NCCSMHI_30_S_grid_areas = iris.analysis.cartography.area_weights(NCCSMHI_30_S)
    NOAA_30_S_grid_areas = iris.analysis.cartography.area_weights(NOAA_30_S)
    
    MPICCLM85_30_S_grid_areas = iris.analysis.cartography.area_weights(MPICCLM85_30_S)
    MPIREMO85_30_S_grid_areas = iris.analysis.cartography.area_weights(MPIREMO85_30_S)
    MPISMHI85_30_S_grid_areas = iris.analysis.cartography.area_weights(MPISMHI85_30_S)
    NCCSMHI85_30_S_grid_areas = iris.analysis.cartography.area_weights(NCCSMHI85_30_S)
    NOAA85_30_S_grid_areas = iris.analysis.cartography.area_weights(NOAA85_30_S)
    
    MPICCLM_50_S_grid_areas = iris.analysis.cartography.area_weights(MPICCLM_50_S)
    MPIREMO_50_S_grid_areas = iris.analysis.cartography.area_weights(MPIREMO_50_S)
    MPISMHI_50_S_grid_areas = iris.analysis.cartography.area_weights(MPISMHI_50_S)
    NCCSMHI_50_S_grid_areas = iris.analysis.cartography.area_weights(NCCSMHI_50_S)
    NOAA_50_S_grid_areas = iris.analysis.cartography.area_weights(NOAA_50_S)
    
    MPICCLM85_50_S_grid_areas = iris.analysis.cartography.area_weights(MPICCLM85_50_S)
    MPIREMO85_50_S_grid_areas = iris.analysis.cartography.area_weights(MPIREMO85_50_S)
    MPISMHI85_50_S_grid_areas = iris.analysis.cartography.area_weights(MPISMHI85_50_S)
    NCCSMHI85_50_S_grid_areas = iris.analysis.cartography.area_weights(NCCSMHI85_50_S)
    NOAA85_50_S_grid_areas = iris.analysis.cartography.area_weights(NOAA85_50_S)
    
    CRU_S_grid_areas = iris.analysis.cartography.area_weights(CRU_S)
    
    #We want to plot the mean for the whole region so we need a mean of all the lats and lons
    MPICCLM_past_S_mean = MPICCLM_past_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MPICCLM_past_S_grid_areas) 
    MPIREMO_past_S_mean = MPIREMO_past_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MPIREMO_past_S_grid_areas)
    MPISMHI_past_S_mean = MPISMHI_past_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MPISMHI_past_S_grid_areas)
    NCCSMHI_past_S_mean = NCCSMHI_past_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=NCCSMHI_past_S_grid_areas)
    NOAA_past_S_mean = NOAA_past_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=NOAA_past_S_grid_areas)
    
    MPICCLM_30_S_mean = MPICCLM_30_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MPICCLM_30_S_grid_areas) 
    MPIREMO_30_S_mean = MPIREMO_30_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MPIREMO_30_S_grid_areas)
    MPISMHI_30_S_mean = MPISMHI_30_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MPISMHI_30_S_grid_areas)
    NCCSMHI_30_S_mean = NCCSMHI_30_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=NCCSMHI_30_S_grid_areas)
    NOAA_30_S_mean = NOAA_30_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=NOAA_30_S_grid_areas)
    
    MPICCLM85_30_S_mean = MPICCLM85_30_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MPICCLM85_30_S_grid_areas) 
    MPIREMO85_30_S_mean = MPIREMO85_30_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MPIREMO85_30_S_grid_areas)
    MPISMHI85_30_S_mean = MPISMHI85_30_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MPISMHI85_30_S_grid_areas)
    NCCSMHI85_30_S_mean = NCCSMHI85_30_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=NCCSMHI85_30_S_grid_areas)
    NOAA85_30_S_mean = NOAA85_30_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=NOAA85_30_S_grid_areas)
    
    MPICCLM_50_S_mean = MPICCLM_50_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MPICCLM_50_S_grid_areas) 
    MPIREMO_50_S_mean = MPIREMO_50_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MPIREMO_50_S_grid_areas)
    MPISMHI_50_S_mean = MPISMHI_50_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MPISMHI_50_S_grid_areas)
    NCCSMHI_50_S_mean = NCCSMHI_50_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=NCCSMHI_50_S_grid_areas)
    NOAA_50_S_mean = NOAA_50_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=NOAA_50_S_grid_areas)
    
    MPICCLM85_50_S_mean = MPICCLM85_50_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MPICCLM85_50_S_grid_areas) 
    MPIREMO85_50_S_mean = MPIREMO85_50_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MPIREMO85_50_S_grid_areas)
    MPISMHI85_50_S_mean = MPISMHI85_50_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MPISMHI85_50_S_grid_areas)
    NCCSMHI85_50_S_mean = NCCSMHI85_50_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=NCCSMHI85_50_S_grid_areas)
    NOAA85_50_S_mean = NOAA85_50_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=NOAA85_50_S_grid_areas)
    
    CRU_S_mean = CRU_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CRU_S_grid_areas)
    
    #for the baseline we don't need to average for each year, but the average for the whole time period, so collapse by time
    MPICCLM_b_S_mean = MPICCLM_past_S_mean.collapsed(['time'], iris.analysis.MEAN)  
    MPIREMO_b_S_mean = MPIREMO_past_S_mean.collapsed(['time'], iris.analysis.MEAN) 
    MPISMHI_b_S_mean = MPISMHI_past_S_mean.collapsed(['time'], iris.analysis.MEAN) 
    NCCSMHI_b_S_mean = NCCSMHI_past_S_mean.collapsed(['time'], iris.analysis.MEAN) 
    NOAA_b_S_mean = NOAA_past_S_mean.collapsed(['time'], iris.analysis.MEAN)
    
    CRU_S_mean = CRU_S_mean.collapsed(['time'], iris.analysis.MEAN) 
    
    #create average of observed baseline data
    Obs_S = (CRU_S_mean)
    
    #We want to see the change in temperature from the baseline
    MPICCLM_past_S_mean = (MPICCLM_past_S_mean.data - MPICCLM_b_S_mean.data + Obs_S.data) 
    MPIREMO_past_S_mean = (MPIREMO_past_S_mean.data - MPIREMO_b_S_mean.data + Obs_S.data)
    MPISMHI_past_S_mean = (MPISMHI_past_S_mean.data - MPISMHI_b_S_mean.data + Obs_S.data)
    NCCSMHI_past_S_mean = (NCCSMHI_past_S_mean.data - NCCSMHI_b_S_mean.data + Obs_S.data)
    NOAA_past_S_mean = (NOAA_past_S_mean.data - NOAA_b_S_mean.data + Obs_S.data)
    
    MPICCLM_30_S_mean = (MPICCLM_30_S_mean.data - MPICCLM_b_S_mean.data + Obs_S.data) 
    MPIREMO_30_S_mean = (MPIREMO_30_S_mean.data - MPIREMO_b_S_mean.data + Obs_S.data)
    MPISMHI_30_S_mean = (MPISMHI_30_S_mean.data - MPISMHI_b_S_mean.data + Obs_S.data)
    NCCSMHI_30_S_mean = (NCCSMHI_30_S_mean.data - NCCSMHI_b_S_mean.data + Obs_S.data)
    NOAA_30_S_mean = (NOAA_30_S_mean.data - NOAA_b_S_mean.data + Obs_S.data)
    
    MPICCLM85_30_S_mean = (MPICCLM85_30_S_mean.data - MPICCLM_b_S_mean.data + Obs_S.data) 
    MPIREMO85_30_S_mean = (MPIREMO85_30_S_mean.data - MPIREMO_b_S_mean.data + Obs_S.data)
    MPISMHI85_30_S_mean = (MPISMHI85_30_S_mean.data - MPISMHI_b_S_mean.data + Obs_S.data)
    NCCSMHI85_30_S_mean = (NCCSMHI85_30_S_mean.data - NCCSMHI_b_S_mean.data + Obs_S.data)
    NOAA85_30_S_mean = (NOAA85_30_S_mean.data - NOAA_b_S_mean.data + Obs_S.data)
    
    MPICCLM_50_S_mean = (MPICCLM_50_S_mean.data - MPICCLM_b_S_mean.data + Obs_S.data) 
    MPIREMO_50_S_mean = (MPIREMO_50_S_mean.data - MPIREMO_b_S_mean.data + Obs_S.data)
    MPISMHI_50_S_mean = (MPISMHI_50_S_mean.data - MPISMHI_b_S_mean.data + Obs_S.data)
    NCCSMHI_50_S_mean = (NCCSMHI_50_S_mean.data - NCCSMHI_b_S_mean.data + Obs_S.data)
    NOAA_50_S_mean = (NOAA_50_S_mean.data - NOAA_b_S_mean.data + Obs_S.data)
    
    MPICCLM85_50_S_mean = (MPICCLM85_50_S_mean.data - MPICCLM_b_S_mean.data + Obs_S.data) 
    MPIREMO85_50_S_mean = (MPIREMO85_50_S_mean.data - MPIREMO_b_S_mean.data + Obs_S.data)
    MPISMHI85_50_S_mean = (MPISMHI85_50_S_mean.data - MPISMHI_b_S_mean.data + Obs_S.data)
    NCCSMHI85_50_S_mean = (NCCSMHI85_50_S_mean.data - NCCSMHI_b_S_mean.data + Obs_S.data)
    NOAA85_50_S_mean = (NOAA85_50_S_mean.data - NOAA_b_S_mean.data + Obs_S.data)  
    
    
    #-------------------------------------------------------------------------
    #PART 6: PRINT DATA
    import csv
    with open('output_DailyTasMINdata_d.csv', 'wb') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        
        writer.writerow(['Parameter', 'Means'])
        
    #PART 6A: WRITE NORTHERN DATA     
        writer.writerow(["MPICCLM_past_N_mean"] +MPICCLM_past_N_mean.data.flatten().astype(np.str).tolist())       
        writer.writerow(["MPIREMO_past_N_mean"] +MPIREMO_past_N_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["MPISMHI_past_N_mean"] +MPISMHI_past_N_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["NCCSMHI_past_N_mean"] +NCCSMHI_past_N_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["NOAA_past_N_mean"] +NOAA_past_N_mean.data.flatten().astype(np.str).tolist())
            
        writer.writerow(["MPICCLM_30_N_mean"] +MPICCLM_30_N_mean.data.flatten().astype(np.str).tolist())       
        writer.writerow(["MPIREMO_30_N_mean"] +MPIREMO_30_N_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["MPISMHI_30_N_mean"] +MPISMHI_30_N_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["NCCSMHI_30_N_mean"] +NCCSMHI_30_N_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["NOAA_30_N_mean"] +NOAA_30_N_mean.data.flatten().astype(np.str).tolist()) 
              
        writer.writerow(["MPICCLM85_30_N_mean"] +MPICCLM85_30_N_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["MPIREMO85_30_N_mean"] +MPIREMO85_30_N_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["MPISMHI85_30_N_mean"] +MPISMHI85_30_N_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["NCCSMHI85_30_N_mean"] +NCCSMHI85_30_N_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["NOAA85_30_N_mean"] +NOAA85_30_N_mean.data.flatten().astype(np.str).tolist())
              
        writer.writerow(["MPICCLM_50_N_mean"] +MPICCLM_50_N_mean.data.flatten().astype(np.str).tolist())       
        writer.writerow(["MPIREMO_50_N_mean"] +MPIREMO_50_N_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["MPISMHI_50_N_mean"] +MPISMHI_50_N_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["NCCSMHI_50_N_mean"] +NCCSMHI_50_N_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["NOAA_50_N_mean"] +NOAA_50_N_mean.data.flatten().astype(np.str).tolist()) 
             
        writer.writerow(["MPICCLM85_50_N_mean"] +MPICCLM85_50_N_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["MPIREMO85_50_N_mean"] +MPIREMO85_50_N_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["MPISMHI85_50_N_mean"] +MPISMHI85_50_N_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["NCCSMHI85_50_N_mean"] +NCCSMHI85_50_N_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["NOAA85_50_N_mean"] +NOAA85_50_N_mean.data.flatten().astype(np.str).tolist())
        
    #PART 6B: WRITE CENTRAL DATA      
        writer.writerow(["MPICCLM_past_C_mean"] +MPICCLM_past_C_mean.data.flatten().astype(np.str).tolist())       
        writer.writerow(["MPIREMO_past_C_mean"] +MPIREMO_past_C_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["MPISMHI_past_C_mean"] +MPISMHI_past_C_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["NCCSMHI_past_C_mean"] +NCCSMHI_past_C_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["NOAA_past_C_mean"] +NOAA_past_C_mean.data.flatten().astype(np.str).tolist())
             
        writer.writerow(["MPICCLM_30_C_mean"] +MPICCLM_30_C_mean.data.flatten().astype(np.str).tolist())       
        writer.writerow(["MPIREMO_30_C_mean"] +MPIREMO_30_C_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["MPISMHI_30_C_mean"] +MPISMHI_30_C_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["NCCSMHI_30_C_mean"] +NCCSMHI_30_C_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["NOAA_30_C_mean"] +NOAA_30_C_mean.data.flatten().astype(np.str).tolist()) 
              
        writer.writerow(["MPICCLM85_30_C_mean"] +MPICCLM85_30_C_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["MPIREMO85_30_C_mean"] +MPIREMO85_30_C_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["MPISMHI85_30_C_mean"] +MPISMHI85_30_C_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["NCCSMHI85_30_C_mean"] +NCCSMHI85_30_C_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["NOAA85_30_C_mean"] +NOAA85_30_C_mean.data.flatten().astype(np.str).tolist())
             
        writer.writerow(["MPICCLM_50_C_mean"] +MPICCLM_50_C_mean.data.flatten().astype(np.str).tolist())       
        writer.writerow(["MPIREMO_50_C_mean"] +MPIREMO_50_C_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["MPISMHI_50_C_mean"] +MPISMHI_50_C_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["NCCSMHI_50_C_mean"] +NCCSMHI_50_C_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["NOAA_50_C_mean"] +NOAA_50_C_mean.data.flatten().astype(np.str).tolist()) 
              
        writer.writerow(["MPICCLM85_50_C_mean"] +MPICCLM85_50_C_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["MPIREMO85_50_C_mean"] +MPIREMO85_50_C_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["MPISMHI85_50_C_mean"] +MPISMHI85_50_C_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["NCCSMHI85_50_C_mean"] +NCCSMHI85_50_C_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["NOAA85_50_C_mean"] +NOAA85_50_C_mean.data.flatten().astype(np.str).tolist())
        
    #PART 6C: WRITE SOUTHERN DATA     
        writer.writerow(["MPICCLM_past_S_mean"] +MPICCLM_past_S_mean.data.flatten().astype(np.str).tolist())       
        writer.writerow(["MPIREMO_past_S_mean"] +MPIREMO_past_S_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["MPISMHI_past_S_mean"] +MPISMHI_past_S_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["NCCSMHI_past_S_mean"] +NCCSMHI_past_S_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["NOAA_past_S_mean"] +NOAA_past_S_mean.data.flatten().astype(np.str).tolist())
              
        writer.writerow(["MPICCLM_30_S_mean"] +MPICCLM_30_S_mean.data.flatten().astype(np.str).tolist())       
        writer.writerow(["MPIREMO_30_S_mean"] +MPIREMO_30_S_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["MPISMHI_30_S_mean"] +MPISMHI_30_S_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["NCCSMHI_30_S_mean"] +NCCSMHI_30_S_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["NOAA_30_S_mean"] +NOAA_30_S_mean.data.flatten().astype(np.str).tolist()) 
            
        writer.writerow(["MPICCLM85_30_S_mean"] +MPICCLM85_30_S_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["MPIREMO85_30_S_mean"] +MPIREMO85_30_S_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["MPISMHI85_30_S_mean"] +MPISMHI85_30_S_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["NCCSMHI85_30_S_mean"] +NCCSMHI85_30_S_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["NOAA85_30_S_mean"] +NOAA85_30_S_mean.data.flatten().astype(np.str).tolist())
              
        writer.writerow(["MPICCLM_50_S_mean"] +MPICCLM_50_S_mean.data.flatten().astype(np.str).tolist())       
        writer.writerow(["MPIREMO_50_S_mean"] +MPIREMO_50_S_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["MPISMHI_50_S_mean"] +MPISMHI_50_S_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["NCCSMHI_50_S_mean"] +NCCSMHI_50_S_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["NOAA_50_S_mean"] +NOAA_50_S_mean.data.flatten().astype(np.str).tolist()) 
              
        writer.writerow(["MPICCLM85_50_S_mean"] +MPICCLM85_50_S_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["MPIREMO85_50_S_mean"] +MPIREMO85_50_S_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["MPISMHI85_50_S_mean"] +MPISMHI85_50_S_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["NCCSMHI85_50_S_mean"] +NCCSMHI85_50_S_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["NOAA85_50_S_mean"] +NOAA85_50_S_mean.data.flatten().astype(np.str).tolist())   
        

if __name__ == '__main__':
    main()
        
        