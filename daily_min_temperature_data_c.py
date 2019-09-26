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
    IPSL_past = '/exports/csce/datastore/geos/users/s0899345/AFR_44_tasmin/Historical_daily/tasmin_AFR-44_IPSL-IPSL-CM5A-MR_historical_r1i1p1_SMHI-RCA4_v1_day_19710101-20001231.nc'
    MIROC_past =  '/exports/csce/datastore/geos/users/s0899345/AFR_44_tasmin/Historical_daily/tasmin_AFR-44_MIROC-MIROC5_historical_r1i1p1_SMHI-RCA4_v1_day_19710101-20001231.nc' 
    MOHCCCLM_past = '/exports/csce/datastore/geos/users/s0899345/AFR_44_tasmin/Historical_daily/tasmin_AFR-44_MOHC-HadGEM2-ES_historical_r1i1p1_CLMcom-CCLM4-8-17_v1_day_19710101-20001231.nc' 
    MOHCKNMI_past = '/exports/csce/datastore/geos/users/s0899345/AFR_44_tasmin/Historical_daily/tasmin_AFR-44_MOHC-HadGEM2-ES_historical_r1i1p1_KNMI-RACMO22T_v2_day_19710101-20001231.nc'
    MOHCSMHI_past = '/exports/csce/datastore/geos/users/s0899345/AFR_44_tasmin/Historical_daily/tasmin_AFR-44_MOHC-HadGEM2-ES_historical_r1i1p1_SMHI-RCA4_v1_day_19710101-20001231.nc'
    
    #Load exactly one cube from given file
    IPSL_past =  iris.load_cube(IPSL_past)
    MIROC_past =  iris.load_cube(MIROC_past)
    MOHCCCLM_past =  iris.load_cube(MOHCCCLM_past)
    MOHCKNMI_past =  iris.load_cube(MOHCKNMI_past)
    MOHCSMHI_past =  iris.load_cube(MOHCSMHI_past)
    
    #remove flat latitude and longitude and only use grid latitude and grid longitude to make consistent with the observed data, also make sure all of the longitudes are monotonic. 
    lats = iris.coords.DimCoord(IPSL_past.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = IPSL_past.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees')
                              
    IPSL_past.remove_coord('latitude')
    IPSL_past.remove_coord('longitude')
    IPSL_past.remove_coord('grid_latitude')
    IPSL_past.remove_coord('grid_longitude')
    IPSL_past.add_dim_coord(lats, 1)
    IPSL_past.add_dim_coord(lons, 2)
    
    lats = iris.coords.DimCoord(MIROC_past.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = MIROC_past.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees')
    
    MIROC_past.remove_coord('latitude')
    MIROC_past.remove_coord('longitude')
    MIROC_past.remove_coord('grid_latitude')
    MIROC_past.remove_coord('grid_longitude')
    MIROC_past.add_dim_coord(lats, 1)
    MIROC_past.add_dim_coord(lons, 2)  
    
    lats = iris.coords.DimCoord(MOHCCCLM_past.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = MOHCCCLM_past.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees')
                                
    MOHCCCLM_past.remove_coord('latitude')
    MOHCCCLM_past.remove_coord('longitude')
    MOHCCCLM_past.remove_coord('grid_latitude')
    MOHCCCLM_past.remove_coord('grid_longitude')
    MOHCCCLM_past.add_dim_coord(lats, 1)
    MOHCCCLM_past.add_dim_coord(lons, 2) 
    
    lats = iris.coords.DimCoord(MOHCKNMI_past.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = MOHCKNMI_past.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees')
    
    MOHCKNMI_past.remove_coord('latitude')
    MOHCKNMI_past.remove_coord('longitude')
    MOHCKNMI_past.remove_coord('grid_latitude')
    MOHCKNMI_past.remove_coord('grid_longitude')
    MOHCKNMI_past.add_dim_coord(lats, 1)
    MOHCKNMI_past.add_dim_coord(lons, 2) 
    
    lats = iris.coords.DimCoord(MOHCSMHI_past.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = MOHCSMHI_past.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees')
    
    MOHCSMHI_past.remove_coord('latitude')
    MOHCSMHI_past.remove_coord('longitude')
    MOHCSMHI_past.remove_coord('grid_latitude')
    MOHCSMHI_past.remove_coord('grid_longitude')
    MOHCSMHI_past.add_dim_coord(lats, 1)
    MOHCSMHI_past.add_dim_coord(lons, 2) 
    
    #guess bounds    
    IPSL_past.coord('latitude').guess_bounds()
    MIROC_past.coord('latitude').guess_bounds()
    MOHCCCLM_past.coord('latitude').guess_bounds()
    MOHCKNMI_past.coord('latitude').guess_bounds()
    MOHCSMHI_past.coord('latitude').guess_bounds()
    
    IPSL_past.coord('longitude').guess_bounds()
    MIROC_past.coord('longitude').guess_bounds()
    MOHCCCLM_past.coord('longitude').guess_bounds()
    MOHCKNMI_past.coord('longitude').guess_bounds()
    MOHCSMHI_past.coord('longitude').guess_bounds()
    
    
    #-------------------------------------------------------------------------
    #PART 2: LOAD and FORMAT PROJECTED MODELS   
    IPSL = '/exports/csce/datastore/geos/users/s0899345/AFR_44_tasmin/4.5/tasmin_AFR-44_IPSL-IPSL-CM5A-MR_rcp45_r1i1p1_SMHI-RCA4_v1_day_20060101-20701231.nc'
    MIROC =  '/exports/csce/datastore/geos/users/s0899345/AFR_44_tasmin/4.5/tasmin_AFR-44_MIROC-MIROC5_rcp45_r1i1p1_SMHI-RCA4_v1_day_20060101-20701231.nc' 
    MOHCCCLM = '/exports/csce/datastore/geos/users/s0899345/AFR_44_tasmin/4.5/tasmin_AFR-44_MOHC-HadGEM2-ES_rcp45_r1i1p1_CLMcom-CCLM4-8-17_v1_day_20060101-20701231.nc' 
    MOHCKNMI = '/exports/csce/datastore/geos/users/s0899345/AFR_44_tasmin/4.5/tasmin_AFR-44_MOHC-HadGEM2-ES_rcp45_r1i1p1_KNMI-RACMO22T_v2_day_20060101-20701231.nc'
    MOHCSMHI = '/exports/csce/datastore/geos/users/s0899345/AFR_44_tasmin/4.5/tasmin_AFR-44_MOHC-HadGEM2-ES_rcp45_r1i1p1_SMHI-RCA4_v1_day_20060101-20701231.nc'
    
    IPSL85 = '/exports/csce/datastore/geos/users/s0899345/AFR_44_tasmin/8.5/tasmin_AFR-44_IPSL-IPSL-CM5A-MR_rcp85_r1i1p1_SMHI-RCA4_v1_day_20060101-20701231.nc'
    MIROC85 =  '/exports/csce/datastore/geos/users/s0899345/AFR_44_tasmin/8.5/tasmin_AFR-44_MIROC-MIROC5_rcp85_r1i1p1_SMHI-RCA4_v1_day_20060101-20701231.nc' 
    MOHCCCLM85 = '/exports/csce/datastore/geos/users/s0899345/AFR_44_tasmin/8.5/tasmin_AFR-44_MOHC-HadGEM2-ES_rcp85_r1i1p1_CLMcom-CCLM4-8-17_v1_day_20060101-20701231.nc' 
    MOHCKNMI85 = '/exports/csce/datastore/geos/users/s0899345/AFR_44_tasmin/8.5/tasmin_AFR-44_MOHC-HadGEM2-ES_rcp85_r1i1p1_KNMI-RACMO22T_v2_day_20060101-20701231.nc'
    MOHCSMHI85 = '/exports/csce/datastore/geos/users/s0899345/AFR_44_tasmin/8.5/tasmin_AFR-44_MOHC-HadGEM2-ES_rcp85_r1i1p1_SMHI-RCA4_v1_day_20060101-20701231.nc'
    
    #Load exactly one cube from given file
    IPSL = iris.load_cube(IPSL)
    MIROC = iris.load_cube(MIROC)
    MOHCCCLM = iris.load_cube(MOHCCCLM)
    MOHCKNMI = iris.load_cube(MOHCKNMI)
    MOHCSMHI = iris.load_cube(MOHCSMHI)
    
    IPSL85 = iris.load_cube(IPSL85)
    MIROC85 = iris.load_cube(MIROC85)
    MOHCCCLM85 = iris.load_cube(MOHCCCLM85)
    MOHCKNMI85 = iris.load_cube(MOHCKNMI85)
    MOHCSMHI85 = iris.load_cube(MOHCSMHI85)
    
    #remove flat latitude and longitude and only use grid latitude and grid longitude to make consistent with the observed data, also make sure all of the longitudes are monotonic. 
    lats = iris.coords.DimCoord(IPSL.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = IPSL.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees')
                              
    IPSL.remove_coord('latitude')
    IPSL.remove_coord('longitude')
    IPSL.remove_coord('grid_latitude')
    IPSL.remove_coord('grid_longitude')
    IPSL.add_dim_coord(lats, 1)
    IPSL.add_dim_coord(lons, 2)
    
    lats = iris.coords.DimCoord(MIROC.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = MIROC.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees')
    
    MIROC.remove_coord('latitude')
    MIROC.remove_coord('longitude')
    MIROC.remove_coord('grid_latitude')
    MIROC.remove_coord('grid_longitude')
    MIROC.add_dim_coord(lats, 1)
    MIROC.add_dim_coord(lons, 2)  
    
    lats = iris.coords.DimCoord(MOHCCCLM.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = MOHCCCLM.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees')
                                
    MOHCCCLM.remove_coord('latitude')
    MOHCCCLM.remove_coord('longitude')
    MOHCCCLM.remove_coord('grid_latitude')
    MOHCCCLM.remove_coord('grid_longitude')
    MOHCCCLM.add_dim_coord(lats, 1)
    MOHCCCLM.add_dim_coord(lons, 2) 
    
    lats = iris.coords.DimCoord(MOHCKNMI.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = MOHCKNMI.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees')
    
    MOHCKNMI.remove_coord('latitude')
    MOHCKNMI.remove_coord('longitude')
    MOHCKNMI.remove_coord('grid_latitude')
    MOHCKNMI.remove_coord('grid_longitude')
    MOHCKNMI.add_dim_coord(lats, 1)
    MOHCKNMI.add_dim_coord(lons, 2) 
    
    lats = iris.coords.DimCoord(MOHCSMHI.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = MOHCSMHI.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees')
    
    MOHCSMHI.remove_coord('latitude')
    MOHCSMHI.remove_coord('longitude')
    MOHCSMHI.remove_coord('grid_latitude')
    MOHCSMHI.remove_coord('grid_longitude')
    MOHCSMHI.add_dim_coord(lats, 1)
    MOHCSMHI.add_dim_coord(lons, 2) 
    
    lats = iris.coords.DimCoord(IPSL85.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = IPSL85.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees')
                              
    IPSL85.remove_coord('latitude')
    IPSL85.remove_coord('longitude')
    IPSL85.remove_coord('grid_latitude')
    IPSL85.remove_coord('grid_longitude')
    IPSL85.add_dim_coord(lats, 1)
    IPSL85.add_dim_coord(lons, 2)
    
    lats = iris.coords.DimCoord(MIROC85.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = MIROC85.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees')
    
    MIROC85.remove_coord('latitude')
    MIROC85.remove_coord('longitude')
    MIROC85.remove_coord('grid_latitude')
    MIROC85.remove_coord('grid_longitude')
    MIROC85.add_dim_coord(lats, 1)
    MIROC85.add_dim_coord(lons, 2)  
    
    lats = iris.coords.DimCoord(MOHCCCLM85.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = MOHCCCLM85.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees')
                                
    MOHCCCLM85.remove_coord('latitude')
    MOHCCCLM85.remove_coord('longitude')
    MOHCCCLM85.remove_coord('grid_latitude')
    MOHCCCLM85.remove_coord('grid_longitude')
    MOHCCCLM85.add_dim_coord(lats, 1)
    MOHCCCLM85.add_dim_coord(lons, 2) 
    
    lats = iris.coords.DimCoord(MOHCKNMI85.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = MOHCKNMI85.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees')
    
    MOHCKNMI85.remove_coord('latitude')
    MOHCKNMI85.remove_coord('longitude')
    MOHCKNMI85.remove_coord('grid_latitude')
    MOHCKNMI85.remove_coord('grid_longitude')
    MOHCKNMI85.add_dim_coord(lats, 1)
    MOHCKNMI85.add_dim_coord(lons, 2) 
    
    lats = iris.coords.DimCoord(MOHCSMHI85.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = MOHCSMHI85.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees')
    
    MOHCSMHI85.remove_coord('latitude')
    MOHCSMHI85.remove_coord('longitude')
    MOHCSMHI85.remove_coord('grid_latitude')
    MOHCSMHI85.remove_coord('grid_longitude')
    MOHCSMHI85.add_dim_coord(lats, 1)
    MOHCSMHI85.add_dim_coord(lons, 2) 
    
    #guess bounds   
    IPSL.coord('latitude').guess_bounds()
    MIROC.coord('latitude').guess_bounds()
    MOHCCCLM.coord('latitude').guess_bounds()
    MOHCKNMI.coord('latitude').guess_bounds()
    MOHCSMHI.coord('latitude').guess_bounds()
    
    IPSL85.coord('latitude').guess_bounds()
    MIROC85.coord('latitude').guess_bounds()
    MOHCCCLM85.coord('latitude').guess_bounds()
    MOHCKNMI85.coord('latitude').guess_bounds()
    MOHCSMHI85.coord('latitude').guess_bounds()
    
    IPSL.coord('longitude').guess_bounds()
    MIROC.coord('longitude').guess_bounds()
    MOHCCCLM.coord('longitude').guess_bounds()
    MOHCKNMI.coord('longitude').guess_bounds()
    MOHCSMHI.coord('longitude').guess_bounds()
    
    IPSL85.coord('longitude').guess_bounds()
    MIROC85.coord('longitude').guess_bounds()
    MOHCCCLM85.coord('longitude').guess_bounds()
    MOHCKNMI85.coord('longitude').guess_bounds()
    MOHCSMHI85.coord('longitude').guess_bounds()
    
    
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
    IPSL_past.convert_units('Celsius')
    MIROC_past.convert_units('Celsius')
    MOHCCCLM_past.convert_units('Celsius')
    MOHCKNMI_past.convert_units('Celsius')
    MOHCSMHI_past.convert_units('Celsius')
    
    IPSL.convert_units('Celsius')
    MIROC.convert_units('Celsius')
    MOHCCCLM.convert_units('Celsius')
    MOHCKNMI.convert_units('Celsius')
    MOHCSMHI.convert_units('Celsius')
    
    IPSL85.convert_units('Celsius')
    MIROC85.convert_units('Celsius')
    MOHCCCLM85.convert_units('Celsius')
    MOHCKNMI85.convert_units('Celsius')
    MOHCSMHI85.convert_units('Celsius')
    
    #rename units to match
    CRU.units = Unit('Celsius')  
    
    #limit time series of data
    #time constraint to make past and obsered data only from 1971-2000 
    iris.FUTURE.cell_datetime_objects = True
    t_constraint_past = iris.Constraint(time=lambda cell: 1971 <= cell.point.year <= 2000)
    
    IPSL_past =  IPSL_past.extract(t_constraint_past)
    MIROC_past =  MIROC_past.extract(t_constraint_past)
    MOHCCCLM_past =  MOHCCCLM_past.extract(t_constraint_past)
    MOHCKNMI_past =  MOHCKNMI_past.extract(t_constraint_past)
    MOHCSMHI_past =  MOHCSMHI_past.extract(t_constraint_past)
    
    CRU = CRU.extract(t_constraint_past)
    
    #time constraint to make future data only from 2020-2049
    iris.FUTURE.cell_datetime_objects = True
    t_constraint_future = iris.Constraint(time=lambda cell: 2020 <= cell.point.year <= 2049)
    
    IPSL_30 = IPSL.extract(t_constraint_future)
    MIROC_30 = MIROC.extract(t_constraint_future)
    MOHCCCLM_30 = MOHCCCLM.extract(t_constraint_future)
    MOHCKNMI_30 = MOHCKNMI.extract(t_constraint_future)
    MOHCSMHI_30 = MOHCSMHI.extract(t_constraint_future)
    
    IPSL85_30 = IPSL85.extract(t_constraint_future)
    MIROC85_30 = MIROC85.extract(t_constraint_future)
    MOHCCCLM85_30 = MOHCCCLM85.extract(t_constraint_future)
    MOHCKNMI85_30 = MOHCKNMI85.extract(t_constraint_future)
    MOHCSMHI85_30 = MOHCSMHI85.extract(t_constraint_future)
    
    #time constraint to make future data only from 2040-2069
    iris.FUTURE.cell_datetime_objects = True
    t_constraint_future = iris.Constraint(time=lambda cell: 2040 <= cell.point.year <= 2069)
    
    IPSL_50 = IPSL.extract(t_constraint_future)
    MIROC_50 = MIROC.extract(t_constraint_future)
    MOHCCCLM_50 = MOHCCCLM.extract(t_constraint_future)
    MOHCKNMI_50 = MOHCKNMI.extract(t_constraint_future)
    MOHCSMHI_50 = MOHCSMHI.extract(t_constraint_future)
    
    IPSL85_50 = IPSL85.extract(t_constraint_future)
    MIROC85_50 = MIROC85.extract(t_constraint_future)
    MOHCCCLM85_50 = MOHCCCLM85.extract(t_constraint_future)
    MOHCKNMI85_50 = MOHCKNMI85.extract(t_constraint_future)
    MOHCSMHI85_50 = MOHCSMHI85.extract(t_constraint_future)
    
    
    #-------------------------------------------------------------------------
    #PART 5: FORMAT DATA TO GEOGRAPHICALLY SPECIFIC AND RE-BASELINE
    #PART 5A: NORTHERN MALAWI
    #we are only interested in the latitude and longitude relevant to Central Malawi 
    Northern_Malawi = iris.Constraint(longitude=lambda v: 32.5 <= v <= 35, latitude=lambda v: -12.5 <= v <= -8.5) 
    
    IPSL_past_N = IPSL_past.extract(Northern_Malawi)
    MIROC_past_N = MIROC_past.extract(Northern_Malawi)
    MOHCCCLM_past_N = MOHCCCLM_past.extract(Northern_Malawi)
    MOHCKNMI_past_N = MOHCKNMI_past.extract(Northern_Malawi)
    MOHCSMHI_past_N = MOHCSMHI_past.extract(Northern_Malawi)
    
    IPSL_30_N = IPSL_30.extract(Northern_Malawi)
    MIROC_30_N = MIROC_30.extract(Northern_Malawi)
    MOHCCCLM_30_N = MOHCCCLM_30.extract(Northern_Malawi)
    MOHCKNMI_30_N = MOHCKNMI_30.extract(Northern_Malawi)
    MOHCSMHI_30_N = MOHCSMHI_30.extract(Northern_Malawi)
    
    IPSL85_30_N = IPSL85_30.extract(Northern_Malawi)
    MIROC85_30_N = MIROC85_30.extract(Northern_Malawi)
    MOHCCCLM85_30_N = MOHCCCLM85_30.extract(Northern_Malawi)
    MOHCKNMI85_30_N = MOHCKNMI85_30.extract(Northern_Malawi)
    MOHCSMHI85_30_N = MOHCSMHI85_30.extract(Northern_Malawi)
    
    IPSL_50_N = IPSL_50.extract(Northern_Malawi)
    MIROC_50_N = MIROC_50.extract(Northern_Malawi)
    MOHCCCLM_50_N = MOHCCCLM_50.extract(Northern_Malawi)
    MOHCKNMI_50_N = MOHCKNMI_50.extract(Northern_Malawi)
    MOHCSMHI_50_N = MOHCSMHI_50.extract(Northern_Malawi)
    
    IPSL85_50_N = IPSL85_50.extract(Northern_Malawi)
    MIROC85_50_N = MIROC85_50.extract(Northern_Malawi)
    MOHCCCLM85_50_N = MOHCCCLM85_50.extract(Northern_Malawi)
    MOHCKNMI85_50_N = MOHCKNMI85_50.extract(Northern_Malawi)
    MOHCSMHI85_50_N = MOHCSMHI85_50.extract(Northern_Malawi)
    
    CRU_N = CRU.extract(Northern_Malawi)
    
    #Returns an array of area weights, with the same dimensions as the cube
    IPSL_past_N_grid_areas = iris.analysis.cartography.area_weights(IPSL_past_N)
    MIROC_past_N_grid_areas = iris.analysis.cartography.area_weights(MIROC_past_N)
    MOHCCCLM_past_N_grid_areas = iris.analysis.cartography.area_weights(MOHCCCLM_past_N)
    MOHCKNMI_past_N_grid_areas = iris.analysis.cartography.area_weights(MOHCKNMI_past_N)
    MOHCSMHI_past_N_grid_areas = iris.analysis.cartography.area_weights(MOHCSMHI_past_N)
    
    IPSL_30_N_grid_areas = iris.analysis.cartography.area_weights(IPSL_30_N)
    MIROC_30_N_grid_areas = iris.analysis.cartography.area_weights(MIROC_30_N)
    MOHCCCLM_30_N_grid_areas = iris.analysis.cartography.area_weights(MOHCCCLM_30_N)
    MOHCKNMI_30_N_grid_areas = iris.analysis.cartography.area_weights(MOHCKNMI_30_N)
    MOHCSMHI_30_N_grid_areas = iris.analysis.cartography.area_weights(MOHCSMHI_30_N)
    
    IPSL85_30_N_grid_areas = iris.analysis.cartography.area_weights(IPSL85_30_N)
    MIROC85_30_N_grid_areas = iris.analysis.cartography.area_weights(MIROC85_30_N)
    MOHCCCLM85_30_N_grid_areas = iris.analysis.cartography.area_weights(MOHCCCLM85_30_N)
    MOHCKNMI85_30_N_grid_areas = iris.analysis.cartography.area_weights(MOHCKNMI85_30_N)
    MOHCSMHI85_30_N_grid_areas = iris.analysis.cartography.area_weights(MOHCSMHI85_30_N)
    
    IPSL_50_N_grid_areas = iris.analysis.cartography.area_weights(IPSL_50_N)
    MIROC_50_N_grid_areas = iris.analysis.cartography.area_weights(MIROC_50_N)
    MOHCCCLM_50_N_grid_areas = iris.analysis.cartography.area_weights(MOHCCCLM_50_N)
    MOHCKNMI_50_N_grid_areas = iris.analysis.cartography.area_weights(MOHCKNMI_50_N)
    MOHCSMHI_50_N_grid_areas = iris.analysis.cartography.area_weights(MOHCSMHI_50_N)
    
    IPSL85_50_N_grid_areas = iris.analysis.cartography.area_weights(IPSL85_50_N)
    MIROC85_50_N_grid_areas = iris.analysis.cartography.area_weights(MIROC85_50_N)
    MOHCCCLM85_50_N_grid_areas = iris.analysis.cartography.area_weights(MOHCCCLM85_50_N)
    MOHCKNMI85_50_N_grid_areas = iris.analysis.cartography.area_weights(MOHCKNMI85_50_N)
    MOHCSMHI85_50_N_grid_areas = iris.analysis.cartography.area_weights(MOHCSMHI85_50_N)
    
    CRU_N_grid_areas = iris.analysis.cartography.area_weights(CRU_N)
    
    #We want to plot the mean for the whole region so we need a mean of all the lats and lons
    IPSL_past_N_mean = IPSL_past_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=IPSL_past_N_grid_areas) 
    MIROC_past_N_mean = MIROC_past_N.collapsed(['latitude', 'longitude'],iris.analysis.MEAN, weights=MIROC_past_N_grid_areas)
    MOHCCCLM_past_N_mean = MOHCCCLM_past_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCCCLM_past_N_grid_areas) 
    MOHCKNMI_past_N_mean = MOHCKNMI_past_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCKNMI_past_N_grid_areas)  
    MOHCSMHI_past_N_mean = MOHCSMHI_past_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCSMHI_past_N_grid_areas)
    
    IPSL_30_N_mean = IPSL_30_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=IPSL_30_N_grid_areas) 
    MIROC_30_N_mean = MIROC_30_N.collapsed(['latitude', 'longitude'],iris.analysis.MEAN, weights=MIROC_30_N_grid_areas)
    MOHCCCLM_30_N_mean = MOHCCCLM_30_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCCCLM_30_N_grid_areas)
    MOHCKNMI_30_N_mean = MOHCKNMI_30_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCKNMI_30_N_grid_areas)  
    MOHCSMHI_30_N_mean = MOHCSMHI_30_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCSMHI_30_N_grid_areas)
    
    IPSL85_30_N_mean = IPSL85_30_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=IPSL85_30_N_grid_areas) 
    MIROC85_30_N_mean = MIROC85_30_N.collapsed(['latitude', 'longitude'],iris.analysis.MEAN, weights=MIROC85_30_N_grid_areas)
    MOHCCCLM85_30_N_mean = MOHCCCLM85_30_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCCCLM85_30_N_grid_areas)
    MOHCKNMI85_30_N_mean = MOHCKNMI85_30_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCKNMI85_30_N_grid_areas)  
    MOHCSMHI85_30_N_mean = MOHCSMHI85_30_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCSMHI85_30_N_grid_areas)
    
    IPSL_50_N_mean = IPSL_50_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=IPSL_50_N_grid_areas) 
    MIROC_50_N_mean = MIROC_50_N.collapsed(['latitude', 'longitude'],iris.analysis.MEAN, weights=MIROC_50_N_grid_areas)
    MOHCCCLM_50_N_mean = MOHCCCLM_50_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCCCLM_50_N_grid_areas)
    MOHCKNMI_50_N_mean = MOHCKNMI_50_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCKNMI_50_N_grid_areas)  
    MOHCSMHI_50_N_mean = MOHCSMHI_50_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCSMHI_50_N_grid_areas)
    
    IPSL85_50_N_mean = IPSL85_50_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=IPSL85_50_N_grid_areas) 
    MIROC85_50_N_mean = MIROC85_50_N.collapsed(['latitude', 'longitude'],iris.analysis.MEAN, weights=MIROC85_50_N_grid_areas)
    MOHCCCLM85_50_N_mean = MOHCCCLM85_50_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCCCLM85_50_N_grid_areas)
    MOHCKNMI85_50_N_mean = MOHCKNMI85_50_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCKNMI85_50_N_grid_areas)  
    MOHCSMHI85_50_N_mean = MOHCSMHI85_50_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCSMHI85_50_N_grid_areas)
    
    CRU_N_mean = CRU_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CRU_N_grid_areas)
    
    #for the baseline we don't need to average for each year, but the average for the whole time period, so collapse by time
    IPSL_b_N_mean = IPSL_past_N_mean.collapsed(['time'], iris.analysis.MEAN) 
    MIROC_b_N_mean = MIROC_past_N_mean.collapsed(['time'], iris.analysis.MEAN) 
    MOHCCCLM_b_N_mean = MOHCCCLM_past_N_mean.collapsed(['time'], iris.analysis.MEAN)                      
    MOHCKNMI_b_N_mean = MOHCKNMI_past_N_mean.collapsed(['time'], iris.analysis.MEAN)   
    MOHCSMHI_b_N_mean = MOHCSMHI_past_N_mean.collapsed(['time'], iris.analysis.MEAN)
    
    CRU_N_mean = CRU_N_mean.collapsed(['time'], iris.analysis.MEAN) 
    
    #create average of observed baseline data
    Obs_N = (CRU_N_mean)
    
    #We want to see the change in temperature from the baseline
    IPSL_past_N_mean = (IPSL_past_N_mean.data - IPSL_b_N_mean.data + Obs_N.data)
    MIROC_past_N_mean = (MIROC_past_N_mean.data - MIROC_b_N_mean.data + Obs_N.data)
    MOHCCCLM_past_N_mean = (MOHCCCLM_past_N_mean.data - MOHCCCLM_b_N_mean.data + Obs_N.data)
    MOHCKNMI_past_N_mean = (MOHCKNMI_past_N_mean.data - MOHCKNMI_b_N_mean.data + Obs_N.data)  
    MOHCSMHI_past_N_mean = (MOHCSMHI_past_N_mean.data - MOHCSMHI_b_N_mean.data + Obs_N.data)
    
    IPSL_30_N_mean = (IPSL_30_N_mean.data - IPSL_b_N_mean.data + Obs_N.data)
    MIROC_30_N_mean = (MIROC_30_N_mean.data - MIROC_b_N_mean.data + Obs_N.data)
    MOHCCCLM_30_N_mean = (MOHCCCLM_30_N_mean.data - MOHCCCLM_b_N_mean.data + Obs_N.data)
    MOHCKNMI_30_N_mean = (MOHCKNMI_30_N_mean.data - MOHCKNMI_b_N_mean.data + Obs_N.data)  
    MOHCSMHI_30_N_mean = (MOHCSMHI_30_N_mean.data - MOHCSMHI_b_N_mean.data + Obs_N.data)
    
    IPSL85_30_N_mean = (IPSL85_30_N_mean.data - IPSL_b_N_mean.data + Obs_N.data)
    MIROC85_30_N_mean = (MIROC85_30_N_mean.data - MIROC_b_N_mean.data + Obs_N.data)
    MOHCCCLM85_30_N_mean = (MOHCCCLM85_30_N_mean.data - MOHCCCLM_b_N_mean.data + Obs_N.data)
    MOHCKNMI85_30_N_mean = (MOHCKNMI85_30_N_mean.data - MOHCKNMI_b_N_mean.data + Obs_N.data)  
    MOHCSMHI85_30_N_mean = (MOHCSMHI85_30_N_mean.data - MOHCSMHI_b_N_mean.data + Obs_N.data)
    
    IPSL_50_N_mean = (IPSL_50_N_mean.data - IPSL_b_N_mean.data + Obs_N.data)
    MIROC_50_N_mean = (MIROC_50_N_mean.data - MIROC_b_N_mean.data + Obs_N.data)
    MOHCCCLM_50_N_mean = (MOHCCCLM_50_N_mean.data - MOHCCCLM_b_N_mean.data + Obs_N.data)
    MOHCKNMI_50_N_mean = (MOHCKNMI_50_N_mean.data - MOHCKNMI_b_N_mean.data + Obs_N.data)  
    MOHCSMHI_50_N_mean = (MOHCSMHI_50_N_mean.data - MOHCSMHI_b_N_mean.data + Obs_N.data)
    
    IPSL85_50_N_mean = (IPSL85_50_N_mean.data - IPSL_b_N_mean.data + Obs_N.data)
    MIROC85_50_N_mean = (MIROC85_50_N_mean.data - MIROC_b_N_mean.data + Obs_N.data)
    MOHCCCLM85_50_N_mean = (MOHCCCLM85_50_N_mean.data - MOHCCCLM_b_N_mean.data + Obs_N.data)
    MOHCKNMI85_50_N_mean = (MOHCKNMI85_50_N_mean.data - MOHCKNMI_b_N_mean.data + Obs_N.data)  
    MOHCSMHI85_50_N_mean = (MOHCSMHI85_50_N_mean.data - MOHCSMHI_b_N_mean.data + Obs_N.data)
    
    
    #PART 5B: CENTRAL MALAWI
    #we are only interested in the latitude and longitude relevant to Central Malawi 
    Central_Malawi = iris.Constraint(longitude=lambda v: 32.5 <= v <= 35.5, latitude=lambda v: -15 <= v <= -11.5) 
    
    IPSL_past_C = IPSL_past.extract(Central_Malawi)
    MIROC_past_C = MIROC_past.extract(Central_Malawi)
    MOHCCCLM_past_C = MOHCCCLM_past.extract(Central_Malawi)
    MOHCKNMI_past_C = MOHCKNMI_past.extract(Central_Malawi)
    MOHCSMHI_past_C = MOHCSMHI_past.extract(Central_Malawi)
    
    IPSL_30_C = IPSL_30.extract(Central_Malawi)
    MIROC_30_C = MIROC_30.extract(Central_Malawi)
    MOHCCCLM_30_C = MOHCCCLM_30.extract(Central_Malawi)
    MOHCKNMI_30_C = MOHCKNMI_30.extract(Central_Malawi)
    MOHCSMHI_30_C = MOHCSMHI_30.extract(Central_Malawi)
    
    IPSL85_30_C = IPSL85_30.extract(Central_Malawi)
    MIROC85_30_C = MIROC85_30.extract(Central_Malawi)
    MOHCCCLM85_30_C = MOHCCCLM85_30.extract(Central_Malawi)
    MOHCKNMI85_30_C = MOHCKNMI85_30.extract(Central_Malawi)
    MOHCSMHI85_30_C = MOHCSMHI85_30.extract(Central_Malawi)
    
    IPSL_50_C = IPSL_50.extract(Central_Malawi)
    MIROC_50_C = MIROC_50.extract(Central_Malawi)
    MOHCCCLM_50_C = MOHCCCLM_50.extract(Central_Malawi)
    MOHCKNMI_50_C = MOHCKNMI_50.extract(Central_Malawi)
    MOHCSMHI_50_C = MOHCSMHI_50.extract(Central_Malawi)
    
    IPSL85_50_C = IPSL85_50.extract(Central_Malawi)
    MIROC85_50_C = MIROC85_50.extract(Central_Malawi)
    MOHCCCLM85_50_C = MOHCCCLM85_50.extract(Central_Malawi)
    MOHCKNMI85_50_C = MOHCKNMI85_50.extract(Central_Malawi)
    MOHCSMHI85_50_C = MOHCSMHI85_50.extract(Central_Malawi)
    
    CRU_C = CRU.extract(Central_Malawi)
    
    #Returns an array of area weights, with the same dimensions as the cube
    IPSL_past_C_grid_areas = iris.analysis.cartography.area_weights(IPSL_past_C)
    MIROC_past_C_grid_areas = iris.analysis.cartography.area_weights(MIROC_past_C)
    MOHCCCLM_past_C_grid_areas = iris.analysis.cartography.area_weights(MOHCCCLM_past_C)
    MOHCKNMI_past_C_grid_areas = iris.analysis.cartography.area_weights(MOHCKNMI_past_C)
    MOHCSMHI_past_C_grid_areas = iris.analysis.cartography.area_weights(MOHCSMHI_past_C)
    
    IPSL_30_C_grid_areas = iris.analysis.cartography.area_weights(IPSL_30_C)
    MIROC_30_C_grid_areas = iris.analysis.cartography.area_weights(MIROC_30_C)
    MOHCCCLM_30_C_grid_areas = iris.analysis.cartography.area_weights(MOHCCCLM_30_C)
    MOHCKNMI_30_C_grid_areas = iris.analysis.cartography.area_weights(MOHCKNMI_30_C)
    MOHCSMHI_30_C_grid_areas = iris.analysis.cartography.area_weights(MOHCSMHI_30_C)
    
    IPSL85_30_C_grid_areas = iris.analysis.cartography.area_weights(IPSL85_30_C)
    MIROC85_30_C_grid_areas = iris.analysis.cartography.area_weights(MIROC85_30_C)
    MOHCCCLM85_30_C_grid_areas = iris.analysis.cartography.area_weights(MOHCCCLM85_30_C)
    MOHCKNMI85_30_C_grid_areas = iris.analysis.cartography.area_weights(MOHCKNMI85_30_C)
    MOHCSMHI85_30_C_grid_areas = iris.analysis.cartography.area_weights(MOHCSMHI85_30_C)
    
    IPSL_50_C_grid_areas = iris.analysis.cartography.area_weights(IPSL_50_C)
    MIROC_50_C_grid_areas = iris.analysis.cartography.area_weights(MIROC_50_C)
    MOHCCCLM_50_C_grid_areas = iris.analysis.cartography.area_weights(MOHCCCLM_50_C)
    MOHCKNMI_50_C_grid_areas = iris.analysis.cartography.area_weights(MOHCKNMI_50_C)
    MOHCSMHI_50_C_grid_areas = iris.analysis.cartography.area_weights(MOHCSMHI_50_C)
    
    IPSL85_50_C_grid_areas = iris.analysis.cartography.area_weights(IPSL85_50_C)
    MIROC85_50_C_grid_areas = iris.analysis.cartography.area_weights(MIROC85_50_C)
    MOHCCCLM85_50_C_grid_areas = iris.analysis.cartography.area_weights(MOHCCCLM85_50_C)
    MOHCKNMI85_50_C_grid_areas = iris.analysis.cartography.area_weights(MOHCKNMI85_50_C)
    MOHCSMHI85_50_C_grid_areas = iris.analysis.cartography.area_weights(MOHCSMHI85_50_C)
    
    CRU_C_grid_areas = iris.analysis.cartography.area_weights(CRU_C)
    
    #We want to plot the mean for the whole region so we need a mean of all the lats and lons
    IPSL_past_C_mean = IPSL_past_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=IPSL_past_C_grid_areas) 
    MIROC_past_C_mean = MIROC_past_C.collapsed(['latitude', 'longitude'],iris.analysis.MEAN, weights=MIROC_past_C_grid_areas)
    MOHCCCLM_past_C_mean = MOHCCCLM_past_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCCCLM_past_C_grid_areas) 
    MOHCKNMI_past_C_mean = MOHCKNMI_past_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCKNMI_past_C_grid_areas)  
    MOHCSMHI_past_C_mean = MOHCSMHI_past_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCSMHI_past_C_grid_areas)
    
    IPSL_30_C_mean = IPSL_30_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=IPSL_30_C_grid_areas) 
    MIROC_30_C_mean = MIROC_30_C.collapsed(['latitude', 'longitude'],iris.analysis.MEAN, weights=MIROC_30_C_grid_areas)
    MOHCCCLM_30_C_mean = MOHCCCLM_30_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCCCLM_30_C_grid_areas)
    MOHCKNMI_30_C_mean = MOHCKNMI_30_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCKNMI_30_C_grid_areas)  
    MOHCSMHI_30_C_mean = MOHCSMHI_30_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCSMHI_30_C_grid_areas)
    
    IPSL85_30_C_mean = IPSL85_30_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=IPSL85_30_C_grid_areas) 
    MIROC85_30_C_mean = MIROC85_30_C.collapsed(['latitude', 'longitude'],iris.analysis.MEAN, weights=MIROC85_30_C_grid_areas)
    MOHCCCLM85_30_C_mean = MOHCCCLM85_30_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCCCLM85_30_C_grid_areas)
    MOHCKNMI85_30_C_mean = MOHCKNMI85_30_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCKNMI85_30_C_grid_areas)  
    MOHCSMHI85_30_C_mean = MOHCSMHI85_30_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCSMHI85_30_C_grid_areas)
    
    IPSL_50_C_mean = IPSL_50_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=IPSL_50_C_grid_areas) 
    MIROC_50_C_mean = MIROC_50_C.collapsed(['latitude', 'longitude'],iris.analysis.MEAN, weights=MIROC_50_C_grid_areas)
    MOHCCCLM_50_C_mean = MOHCCCLM_50_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCCCLM_50_C_grid_areas)
    MOHCKNMI_50_C_mean = MOHCKNMI_50_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCKNMI_50_C_grid_areas)  
    MOHCSMHI_50_C_mean = MOHCSMHI_50_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCSMHI_50_C_grid_areas)
    
    IPSL85_50_C_mean = IPSL85_50_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=IPSL85_50_C_grid_areas) 
    MIROC85_50_C_mean = MIROC85_50_C.collapsed(['latitude', 'longitude'],iris.analysis.MEAN, weights=MIROC85_50_C_grid_areas)
    MOHCCCLM85_50_C_mean = MOHCCCLM85_50_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCCCLM85_50_C_grid_areas)
    MOHCKNMI85_50_C_mean = MOHCKNMI85_50_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCKNMI85_50_C_grid_areas)  
    MOHCSMHI85_50_C_mean = MOHCSMHI85_50_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCSMHI85_50_C_grid_areas)
    
    CRU_C_mean = CRU_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CRU_C_grid_areas)
    
    #for the baseline we don't need to average for each year, but the average for the whole time period, so collapse by time
    IPSL_b_C_mean = IPSL_past_C_mean.collapsed(['time'], iris.analysis.MEAN) 
    MIROC_b_C_mean = MIROC_past_C_mean.collapsed(['time'], iris.analysis.MEAN) 
    MOHCCCLM_b_C_mean = MOHCCCLM_past_C_mean.collapsed(['time'], iris.analysis.MEAN)                      
    MOHCKNMI_b_C_mean = MOHCKNMI_past_C_mean.collapsed(['time'], iris.analysis.MEAN)   
    MOHCSMHI_b_C_mean = MOHCSMHI_past_C_mean.collapsed(['time'], iris.analysis.MEAN)
    
    CRU_C_mean = CRU_C_mean.collapsed(['time'], iris.analysis.MEAN) 
    
    #create average of observed baseline data
    Obs_C = (CRU_C_mean)
    
    #We want to see the change in temperature from the baseline
    IPSL_past_C_mean = (IPSL_past_C_mean.data - IPSL_b_C_mean.data + Obs_C.data)
    MIROC_past_C_mean = (MIROC_past_C_mean.data - MIROC_b_C_mean.data + Obs_C.data)
    MOHCCCLM_past_C_mean = (MOHCCCLM_past_C_mean.data - MOHCCCLM_b_C_mean.data + Obs_C.data)
    MOHCKNMI_past_C_mean = (MOHCKNMI_past_C_mean.data - MOHCKNMI_b_C_mean.data + Obs_C.data)  
    MOHCSMHI_past_C_mean = (MOHCSMHI_past_C_mean.data - MOHCSMHI_b_C_mean.data + Obs_C.data)
    
    IPSL_30_C_mean = (IPSL_30_C_mean.data - IPSL_b_C_mean.data + Obs_C.data)
    MIROC_30_C_mean = (MIROC_30_C_mean.data - MIROC_b_C_mean.data + Obs_C.data)
    MOHCCCLM_30_C_mean = (MOHCCCLM_30_C_mean.data - MOHCCCLM_b_C_mean.data + Obs_C.data)
    MOHCKNMI_30_C_mean = (MOHCKNMI_30_C_mean.data - MOHCKNMI_b_C_mean.data + Obs_C.data)  
    MOHCSMHI_30_C_mean = (MOHCSMHI_30_C_mean.data - MOHCSMHI_b_C_mean.data + Obs_C.data)
    
    IPSL85_30_C_mean = (IPSL85_30_C_mean.data - IPSL_b_C_mean.data + Obs_C.data)
    MIROC85_30_C_mean = (MIROC85_30_C_mean.data - MIROC_b_C_mean.data + Obs_C.data)
    MOHCCCLM85_30_C_mean = (MOHCCCLM85_30_C_mean.data - MOHCCCLM_b_C_mean.data + Obs_C.data)
    MOHCKNMI85_30_C_mean = (MOHCKNMI85_30_C_mean.data - MOHCKNMI_b_C_mean.data + Obs_C.data)  
    MOHCSMHI85_30_C_mean = (MOHCSMHI85_30_C_mean.data - MOHCSMHI_b_C_mean.data + Obs_C.data)
    
    IPSL_50_C_mean = (IPSL_50_C_mean.data - IPSL_b_C_mean.data + Obs_C.data)
    MIROC_50_C_mean = (MIROC_50_C_mean.data - MIROC_b_C_mean.data + Obs_C.data)
    MOHCCCLM_50_C_mean = (MOHCCCLM_50_C_mean.data - MOHCCCLM_b_C_mean.data + Obs_C.data)
    MOHCKNMI_50_C_mean = (MOHCKNMI_50_C_mean.data - MOHCKNMI_b_C_mean.data + Obs_C.data)  
    MOHCSMHI_50_C_mean = (MOHCSMHI_50_C_mean.data - MOHCSMHI_b_C_mean.data + Obs_C.data)
    
    IPSL85_50_C_mean = (IPSL85_50_C_mean.data - IPSL_b_C_mean.data + Obs_C.data)
    MIROC85_50_C_mean = (MIROC85_50_C_mean.data - MIROC_b_C_mean.data + Obs_C.data)
    MOHCCCLM85_50_C_mean = (MOHCCCLM85_50_C_mean.data - MOHCCCLM_b_C_mean.data + Obs_C.data)
    MOHCKNMI85_50_C_mean = (MOHCKNMI85_50_C_mean.data - MOHCKNMI_b_C_mean.data + Obs_C.data)  
    MOHCSMHI85_50_C_mean = (MOHCSMHI85_50_C_mean.data - MOHCSMHI_b_C_mean.data + Obs_C.data)
    
            
    #PART 5C: SOUTHERN MALAWI
    #we are only interested in the latitude and longitude relevant to Southern Malawi 
    Southern_Malawi = iris.Constraint(longitude=lambda v: 34 <= v <= 36.5, latitude=lambda v: -17.5 <= v <= -14) 
    
    IPSL_past_S = IPSL_past.extract(Southern_Malawi)
    MIROC_past_S = MIROC_past.extract(Southern_Malawi)
    MOHCCCLM_past_S = MOHCCCLM_past.extract(Southern_Malawi)
    MOHCKNMI_past_S = MOHCKNMI_past.extract(Southern_Malawi)
    MOHCSMHI_past_S = MOHCSMHI_past.extract(Southern_Malawi)
    
    IPSL_30_S = IPSL_30.extract(Southern_Malawi)
    MIROC_30_S = MIROC_30.extract(Southern_Malawi)
    MOHCCCLM_30_S = MOHCCCLM_30.extract(Southern_Malawi)
    MOHCKNMI_30_S = MOHCKNMI_30.extract(Southern_Malawi)
    MOHCSMHI_30_S = MOHCSMHI_30.extract(Southern_Malawi)
    
    IPSL85_30_S = IPSL85_30.extract(Southern_Malawi)
    MIROC85_30_S = MIROC85_30.extract(Southern_Malawi)
    MOHCCCLM85_30_S = MOHCCCLM85_30.extract(Southern_Malawi)
    MOHCKNMI85_30_S = MOHCKNMI85_30.extract(Southern_Malawi)
    MOHCSMHI85_30_S = MOHCSMHI85_30.extract(Southern_Malawi)
    
    IPSL_50_S = IPSL_50.extract(Southern_Malawi)
    MIROC_50_S = MIROC_50.extract(Southern_Malawi)
    MOHCCCLM_50_S = MOHCCCLM_50.extract(Southern_Malawi)
    MOHCKNMI_50_S = MOHCKNMI_50.extract(Southern_Malawi)
    MOHCSMHI_50_S = MOHCSMHI_50.extract(Southern_Malawi)
    
    IPSL85_50_S = IPSL85_50.extract(Southern_Malawi)
    MIROC85_50_S = MIROC85_50.extract(Southern_Malawi)
    MOHCCCLM85_50_S = MOHCCCLM85_50.extract(Southern_Malawi)
    MOHCKNMI85_50_S = MOHCKNMI85_50.extract(Southern_Malawi)
    MOHCSMHI85_50_S = MOHCSMHI85_50.extract(Southern_Malawi)
    
    CRU_S = CRU.extract(Southern_Malawi)
    
    #Returns an array of area weights, with the same dimensions as the cube
    IPSL_past_S_grid_areas = iris.analysis.cartography.area_weights(IPSL_past_S)
    MIROC_past_S_grid_areas = iris.analysis.cartography.area_weights(MIROC_past_S)
    MOHCCCLM_past_S_grid_areas = iris.analysis.cartography.area_weights(MOHCCCLM_past_S)
    MOHCKNMI_past_S_grid_areas = iris.analysis.cartography.area_weights(MOHCKNMI_past_S)
    MOHCSMHI_past_S_grid_areas = iris.analysis.cartography.area_weights(MOHCSMHI_past_S)
    
    IPSL_30_S_grid_areas = iris.analysis.cartography.area_weights(IPSL_30_S)
    MIROC_30_S_grid_areas = iris.analysis.cartography.area_weights(MIROC_30_S)
    MOHCCCLM_30_S_grid_areas = iris.analysis.cartography.area_weights(MOHCCCLM_30_S)
    MOHCKNMI_30_S_grid_areas = iris.analysis.cartography.area_weights(MOHCKNMI_30_S)
    MOHCSMHI_30_S_grid_areas = iris.analysis.cartography.area_weights(MOHCSMHI_30_S)
    
    IPSL85_30_S_grid_areas = iris.analysis.cartography.area_weights(IPSL85_30_S)
    MIROC85_30_S_grid_areas = iris.analysis.cartography.area_weights(MIROC85_30_S)
    MOHCCCLM85_30_S_grid_areas = iris.analysis.cartography.area_weights(MOHCCCLM85_30_S)
    MOHCKNMI85_30_S_grid_areas = iris.analysis.cartography.area_weights(MOHCKNMI85_30_S)
    MOHCSMHI85_30_S_grid_areas = iris.analysis.cartography.area_weights(MOHCSMHI85_30_S)
    
    IPSL_50_S_grid_areas = iris.analysis.cartography.area_weights(IPSL_50_S)
    MIROC_50_S_grid_areas = iris.analysis.cartography.area_weights(MIROC_50_S)
    MOHCCCLM_50_S_grid_areas = iris.analysis.cartography.area_weights(MOHCCCLM_50_S)
    MOHCKNMI_50_S_grid_areas = iris.analysis.cartography.area_weights(MOHCKNMI_50_S)
    MOHCSMHI_50_S_grid_areas = iris.analysis.cartography.area_weights(MOHCSMHI_50_S)
    
    IPSL85_50_S_grid_areas = iris.analysis.cartography.area_weights(IPSL85_50_S)
    MIROC85_50_S_grid_areas = iris.analysis.cartography.area_weights(MIROC85_50_S)
    MOHCCCLM85_50_S_grid_areas = iris.analysis.cartography.area_weights(MOHCCCLM85_50_S)
    MOHCKNMI85_50_S_grid_areas = iris.analysis.cartography.area_weights(MOHCKNMI85_50_S)
    MOHCSMHI85_50_S_grid_areas = iris.analysis.cartography.area_weights(MOHCSMHI85_50_S)
    
    CRU_S_grid_areas = iris.analysis.cartography.area_weights(CRU_S)
    
    #We want to plot the mean for the whole region so we need a mean of all the lats and lons
    IPSL_past_S_mean = IPSL_past_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=IPSL_past_S_grid_areas) 
    MIROC_past_S_mean = MIROC_past_S.collapsed(['latitude', 'longitude'],iris.analysis.MEAN, weights=MIROC_past_S_grid_areas)
    MOHCCCLM_past_S_mean = MOHCCCLM_past_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCCCLM_past_S_grid_areas) 
    MOHCKNMI_past_S_mean = MOHCKNMI_past_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCKNMI_past_S_grid_areas)  
    MOHCSMHI_past_S_mean = MOHCSMHI_past_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCSMHI_past_S_grid_areas)
    
    IPSL_30_S_mean = IPSL_30_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=IPSL_30_S_grid_areas) 
    MIROC_30_S_mean = MIROC_30_S.collapsed(['latitude', 'longitude'],iris.analysis.MEAN, weights=MIROC_30_S_grid_areas)
    MOHCCCLM_30_S_mean = MOHCCCLM_30_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCCCLM_30_S_grid_areas)
    MOHCKNMI_30_S_mean = MOHCKNMI_30_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCKNMI_30_S_grid_areas)  
    MOHCSMHI_30_S_mean = MOHCSMHI_30_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCSMHI_30_S_grid_areas)
    
    IPSL85_30_S_mean = IPSL85_30_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=IPSL85_30_S_grid_areas) 
    MIROC85_30_S_mean = MIROC85_30_S.collapsed(['latitude', 'longitude'],iris.analysis.MEAN, weights=MIROC85_30_S_grid_areas)
    MOHCCCLM85_30_S_mean = MOHCCCLM85_30_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCCCLM85_30_S_grid_areas)
    MOHCKNMI85_30_S_mean = MOHCKNMI85_30_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCKNMI85_30_S_grid_areas)  
    MOHCSMHI85_30_S_mean = MOHCSMHI85_30_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCSMHI85_30_S_grid_areas)
    
    IPSL_50_S_mean = IPSL_50_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=IPSL_50_S_grid_areas) 
    MIROC_50_S_mean = MIROC_50_S.collapsed(['latitude', 'longitude'],iris.analysis.MEAN, weights=MIROC_50_S_grid_areas)
    MOHCCCLM_50_S_mean = MOHCCCLM_50_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCCCLM_50_S_grid_areas)
    MOHCKNMI_50_S_mean = MOHCKNMI_50_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCKNMI_50_S_grid_areas)  
    MOHCSMHI_50_S_mean = MOHCSMHI_50_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCSMHI_50_S_grid_areas)
    
    IPSL85_50_S_mean = IPSL85_50_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=IPSL85_50_S_grid_areas) 
    MIROC85_50_S_mean = MIROC85_50_S.collapsed(['latitude', 'longitude'],iris.analysis.MEAN, weights=MIROC85_50_S_grid_areas)
    MOHCCCLM85_50_S_mean = MOHCCCLM85_50_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCCCLM85_50_S_grid_areas)
    MOHCKNMI85_50_S_mean = MOHCKNMI85_50_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCKNMI85_50_S_grid_areas)  
    MOHCSMHI85_50_S_mean = MOHCSMHI85_50_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCSMHI85_50_S_grid_areas)
    
    CRU_S_mean = CRU_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CRU_S_grid_areas)
    
    #for the baseline we don't need to average for each year, but the average for the whole time period, so collapse by time
    IPSL_b_S_mean = IPSL_past_S_mean.collapsed(['time'], iris.analysis.MEAN) 
    MIROC_b_S_mean = MIROC_past_S_mean.collapsed(['time'], iris.analysis.MEAN) 
    MOHCCCLM_b_S_mean = MOHCCCLM_past_S_mean.collapsed(['time'], iris.analysis.MEAN)                      
    MOHCKNMI_b_S_mean = MOHCKNMI_past_S_mean.collapsed(['time'], iris.analysis.MEAN)   
    MOHCSMHI_b_S_mean = MOHCSMHI_past_S_mean.collapsed(['time'], iris.analysis.MEAN)
    
    CRU_S_mean = CRU_S_mean.collapsed(['time'], iris.analysis.MEAN)
    
    #create average of observed baseline data
    Obs_S = (CRU_S_mean)
    
    #We want to see the change in temperature from the baseline
    IPSL_past_S_mean = (IPSL_past_S_mean.data - IPSL_b_S_mean.data + Obs_S.data)
    MIROC_past_S_mean = (MIROC_past_S_mean.data - MIROC_b_S_mean.data + Obs_S.data)
    MOHCCCLM_past_S_mean = (MOHCCCLM_past_S_mean.data - MOHCCCLM_b_S_mean.data + Obs_S.data)
    MOHCKNMI_past_S_mean = (MOHCKNMI_past_S_mean.data - MOHCKNMI_b_S_mean.data + Obs_S.data)  
    MOHCSMHI_past_S_mean = (MOHCSMHI_past_S_mean.data - MOHCSMHI_b_S_mean.data + Obs_S.data)
    
    IPSL_30_S_mean = (IPSL_30_S_mean.data - IPSL_b_S_mean.data + Obs_S.data)
    MIROC_30_S_mean = (MIROC_30_S_mean.data - MIROC_b_S_mean.data + Obs_S.data)
    MOHCCCLM_30_S_mean = (MOHCCCLM_30_S_mean.data - MOHCCCLM_b_S_mean.data + Obs_S.data)
    MOHCKNMI_30_S_mean = (MOHCKNMI_30_S_mean.data - MOHCKNMI_b_S_mean.data + Obs_S.data)  
    MOHCSMHI_30_S_mean = (MOHCSMHI_30_S_mean.data - MOHCSMHI_b_S_mean.data + Obs_S.data)
    
    IPSL85_30_S_mean = (IPSL85_30_S_mean.data - IPSL_b_S_mean.data + Obs_S.data)
    MIROC85_30_S_mean = (MIROC85_30_S_mean.data - MIROC_b_S_mean.data + Obs_S.data)
    MOHCCCLM85_30_S_mean = (MOHCCCLM85_30_S_mean.data - MOHCCCLM_b_S_mean.data + Obs_S.data)
    MOHCKNMI85_30_S_mean = (MOHCKNMI85_30_S_mean.data - MOHCKNMI_b_S_mean.data + Obs_S.data)  
    MOHCSMHI85_30_S_mean = (MOHCSMHI85_30_S_mean.data - MOHCSMHI_b_S_mean.data + Obs_S.data)
    
    IPSL_50_S_mean = (IPSL_50_S_mean.data - IPSL_b_S_mean.data + Obs_S.data)
    MIROC_50_S_mean = (MIROC_50_S_mean.data - MIROC_b_S_mean.data + Obs_S.data)
    MOHCCCLM_50_S_mean = (MOHCCCLM_50_S_mean.data - MOHCCCLM_b_S_mean.data + Obs_S.data)
    MOHCKNMI_50_S_mean = (MOHCKNMI_50_S_mean.data - MOHCKNMI_b_S_mean.data + Obs_S.data)  
    MOHCSMHI_50_S_mean = (MOHCSMHI_50_S_mean.data - MOHCSMHI_b_S_mean.data + Obs_S.data)
    
    IPSL85_50_S_mean = (IPSL85_50_S_mean.data - IPSL_b_S_mean.data + Obs_S.data)
    MIROC85_50_S_mean = (MIROC85_50_S_mean.data - MIROC_b_S_mean.data + Obs_S.data)
    MOHCCCLM85_50_S_mean = (MOHCCCLM85_50_S_mean.data - MOHCCCLM_b_S_mean.data + Obs_S.data)
    MOHCKNMI85_50_S_mean = (MOHCKNMI85_50_S_mean.data - MOHCKNMI_b_S_mean.data + Obs_S.data)  
    MOHCSMHI85_50_S_mean = (MOHCSMHI85_50_S_mean.data - MOHCSMHI_b_S_mean.data + Obs_S.data)  
    
    
    #-------------------------------------------------------------------------
    #PART 6: PRINT DATA
    import csv
    with open('output_DailyTasMINdata_c.csv', 'wb') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        
        writer.writerow(['Parameter', 'Means'])
        
    #PART 6A: WRITE NORTHERN DATA
        writer.writerow(["IPSL_past_N_mean"] + IPSL_past_N_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["MIROC_past_N_mean"] + MIROC_past_N_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["MOHCCCLM_past_N_mean"] + MOHCCCLM_past_N_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["MOHCKNMI_past_N_mean"] +MOHCKNMI_past_N_mean.data.flatten().astype(np.str).tolist())   
        writer.writerow(["MOHCSMHI_past_N_mean"] +MOHCSMHI_past_N_mean.data.flatten().astype(np.str).tolist()) 
        
        writer.writerow(["IPSL_30_N_mean"] + IPSL_30_N_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["MIROC_30_N_mean"] + MIROC_30_N_mean.data.flatten().astype(np.str).tolist())  
        writer.writerow(["MOHCCCLM_30_N_mean"] + MOHCCCLM_30_N_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["MOHCKNMI_30_N_mean"] +MOHCKNMI_30_N_mean.data.flatten().astype(np.str).tolist())   
        writer.writerow(["MOHCSMHI_30_N_mean"] +MOHCSMHI_30_N_mean.data.flatten().astype(np.str).tolist())
        
        writer.writerow(["IPSL85_30_N_mean"] + IPSL85_30_N_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["MIROC85_30_N_mean"] + MIROC85_30_N_mean.data.flatten().astype(np.str).tolist())           
        writer.writerow(["MOHCCCLM85_30_N_mean"] + MOHCCCLM85_30_N_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["MOHCKNMI85_30_N_mean"] +MOHCKNMI85_30_N_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["MOHCSMHI85_30_N_mean"] +MOHCSMHI85_30_N_mean.data.flatten().astype(np.str).tolist()) 
        
        writer.writerow(["IPSL_50_N_mean"] + IPSL_50_N_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["MIROC_50_N_mean"] + MIROC_50_N_mean.data.flatten().astype(np.str).tolist())  
        writer.writerow(["MOHCCCLM_50_N_mean"] + MOHCCCLM_50_N_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["MOHCKNMI_50_N_mean"] +MOHCKNMI_50_N_mean.data.flatten().astype(np.str).tolist())   
        writer.writerow(["MOHCSMHI_50_N_mean"] +MOHCSMHI_50_N_mean.data.flatten().astype(np.str).tolist())
        
        writer.writerow(["IPSL85_50_N_mean"] + IPSL85_50_N_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["MIROC85_50_N_mean"] + MIROC85_50_N_mean.data.flatten().astype(np.str).tolist())           
        writer.writerow(["MOHCCCLM85_50_N_mean"] + MOHCCCLM85_50_N_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["MOHCKNMI85_50_N_mean"] +MOHCKNMI85_50_N_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["MOHCSMHI85_50_N_mean"] +MOHCSMHI85_50_N_mean.data.flatten().astype(np.str).tolist())
        
    #PART 6B: WRITE CENTRAL DATA
        writer.writerow(["IPSL_past_C_mean"] + IPSL_past_C_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["MIROC_past_C_mean"] + MIROC_past_C_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["MOHCCCLM_past_C_mean"] + MOHCCCLM_past_C_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["MOHCKNMI_past_C_mean"] +MOHCKNMI_past_C_mean.data.flatten().astype(np.str).tolist())   
        writer.writerow(["MOHCSMHI_past_C_mean"] +MOHCSMHI_past_C_mean.data.flatten().astype(np.str).tolist()) 
        
        writer.writerow(["IPSL_30_C_mean"] + IPSL_30_C_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["MIROC_30_C_mean"] + MIROC_30_C_mean.data.flatten().astype(np.str).tolist())  
        writer.writerow(["MOHCCCLM_30_C_mean"] + MOHCCCLM_30_C_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["MOHCKNMI_30_C_mean"] +MOHCKNMI_30_C_mean.data.flatten().astype(np.str).tolist())   
        writer.writerow(["MOHCSMHI_30_C_mean"] +MOHCSMHI_30_C_mean.data.flatten().astype(np.str).tolist())
        
        writer.writerow(["IPSL85_30_C_mean"] + IPSL85_30_C_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["MIROC85_30_C_mean"] + MIROC85_30_C_mean.data.flatten().astype(np.str).tolist())           
        writer.writerow(["MOHCCCLM85_30_C_mean"] + MOHCCCLM85_30_C_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["MOHCKNMI85_30_C_mean"] +MOHCKNMI85_30_C_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["MOHCSMHI85_30_C_mean"] +MOHCSMHI85_30_C_mean.data.flatten().astype(np.str).tolist())
        
        writer.writerow(["IPSL_50_C_mean"] + IPSL_50_C_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["MIROC_50_C_mean"] + MIROC_50_C_mean.data.flatten().astype(np.str).tolist())  
        writer.writerow(["MOHCCCLM_50_C_mean"] + MOHCCCLM_50_C_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["MOHCKNMI_50_C_mean"] +MOHCKNMI_50_C_mean.data.flatten().astype(np.str).tolist())   
        writer.writerow(["MOHCSMHI_50_C_mean"] +MOHCSMHI_50_C_mean.data.flatten().astype(np.str).tolist())
        
        writer.writerow(["IPSL85_50_C_mean"] + IPSL85_50_C_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["MIROC85_50_C_mean"] + MIROC85_50_C_mean.data.flatten().astype(np.str).tolist())           
        writer.writerow(["MOHCCCLM85_50_C_mean"] + MOHCCCLM85_50_C_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["MOHCKNMI85_50_C_mean"] +MOHCKNMI85_50_C_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["MOHCSMHI85_50_C_mean"] +MOHCSMHI85_50_C_mean.data.flatten().astype(np.str).tolist())
        
    #PART 6C: WRITE SOUTHERN DATA
        writer.writerow(["IPSL_past_S_mean"] + IPSL_past_S_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["MIROC_past_S_mean"] + MIROC_past_S_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["MOHCCCLM_past_S_mean"] + MOHCCCLM_past_S_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["MOHCKNMI_past_S_mean"] +MOHCKNMI_past_S_mean.data.flatten().astype(np.str).tolist())   
        writer.writerow(["MOHCSMHI_past_S_mean"] +MOHCSMHI_past_S_mean.data.flatten().astype(np.str).tolist())
        
        writer.writerow(["IPSL_30_S_mean"] + IPSL_30_S_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["MIROC_30_S_mean"] + MIROC_30_S_mean.data.flatten().astype(np.str).tolist())  
        writer.writerow(["MOHCCCLM_30_S_mean"] + MOHCCCLM_30_S_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["MOHCKNMI_30_S_mean"] +MOHCKNMI_30_S_mean.data.flatten().astype(np.str).tolist())   
        writer.writerow(["MOHCSMHI_30_S_mean"] +MOHCSMHI_30_S_mean.data.flatten().astype(np.str).tolist())
        
        writer.writerow(["IPSL85_30_S_mean"] + IPSL85_30_S_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["MIROC85_30_S_mean"] + MIROC85_30_S_mean.data.flatten().astype(np.str).tolist())           
        writer.writerow(["MOHCCCLM85_30_S_mean"] + MOHCCCLM85_30_S_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["MOHCKNMI85_30_S_mean"] +MOHCKNMI85_30_S_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["MOHCSMHI85_30_S_mean"] +MOHCSMHI85_30_S_mean.data.flatten().astype(np.str).tolist())
        
        writer.writerow(["IPSL_50_S_mean"] + IPSL_50_S_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["MIROC_50_S_mean"] + MIROC_50_S_mean.data.flatten().astype(np.str).tolist())  
        writer.writerow(["MOHCCCLM_50_S_mean"] + MOHCCCLM_50_S_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["MOHCKNMI_50_S_mean"] +MOHCKNMI_50_S_mean.data.flatten().astype(np.str).tolist())   
        writer.writerow(["MOHCSMHI_50_S_mean"] +MOHCSMHI_50_S_mean.data.flatten().astype(np.str).tolist()) 
        
        writer.writerow(["IPSL85_50_S_mean"] + IPSL85_50_S_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["MIROC85_50_S_mean"] + MIROC85_50_S_mean.data.flatten().astype(np.str).tolist())           
        writer.writerow(["MOHCCCLM85_50_S_mean"] + MOHCCCLM85_50_S_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["MOHCKNMI85_50_S_mean"] +MOHCKNMI85_50_S_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["MOHCSMHI85_50_S_mean"] +MOHCSMHI85_50_S_mean.data.flatten().astype(np.str).tolist())
        

if __name__ == '__main__':
    main()
        
        