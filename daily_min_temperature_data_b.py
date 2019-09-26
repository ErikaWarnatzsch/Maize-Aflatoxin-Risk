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
    ICHECDMI_past = '/exports/csce/datastore/geos/users/s0899345/AFR_44_tasmin/Historical_daily/tasmin_AFR-44_ICHEC-EC-EARTH_historical_r3i1p1_DMI-HIRHAM5_v2_day_19710101-20001231.nc'   
    ICHECCCLM_past = '/exports/csce/datastore/geos/users/s0899345/AFR_44_tasmin/Historical_daily/tasmin_AFR-44_ICHEC-EC-EARTH_historical_r12i1p1_CLMcom-CCLM4-8-17_v1_day_19710101-20001231.nc'    
    ICHECKNMI_past = '/exports/csce/datastore/geos/users/s0899345/AFR_44_tasmin/Historical_daily/tasmin_AFR-44_ICHEC-EC-EARTH_historical_r1i1p1_KNMI-RACMO22T_v1_day_19710101-20001231.nc'
    ICHECMPI_past = '/exports/csce/datastore/geos/users/s0899345/AFR_44_tasmin/Historical_daily/tasmin_AFR-44_ICHEC-EC-EARTH_historical_r12i1p1_MPI-CSC-REMO2009_v1_day_19710101-20001231.nc'
    ICHECSMHI_past = '/exports/csce/datastore/geos/users/s0899345/AFR_44_tasmin/Historical_daily/tasmin_AFR-44_ICHEC-EC-EARTH_historical_r12i1p1_SMHI-RCA4_v1_day_19710101-20001231.nc'
    
    #Load exactly one cube from given file
    ICHECDMI_past =  iris.load_cube(ICHECDMI_past, 'air_temperature')
    ICHECCCLM_past =  iris.load_cube(ICHECCCLM_past)
    ICHECKNMI_past =  iris.load_cube(ICHECKNMI_past)
    ICHECMPI_past =  iris.load_cube(ICHECMPI_past)
    ICHECSMHI_past =  iris.load_cube(ICHECSMHI_past)
    
    #remove flat latitude and longitude and only use grid latitude and grid longitude to make consistent with the observed data, also make sure all of the longitudes are monotonic. 
    
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
    ICHECDMI_past.coord('latitude').guess_bounds()
    ICHECCCLM_past.coord('latitude').guess_bounds()
    ICHECKNMI_past.coord('latitude').guess_bounds()
    ICHECMPI_past.coord('latitude').guess_bounds()
    ICHECSMHI_past.coord('latitude').guess_bounds()
    
    ICHECDMI_past.coord('longitude').guess_bounds()
    ICHECCCLM_past.coord('longitude').guess_bounds()
    ICHECKNMI_past.coord('longitude').guess_bounds()
    ICHECMPI_past.coord('longitude').guess_bounds()
    ICHECSMHI_past.coord('longitude').guess_bounds()
    
    
    #-------------------------------------------------------------------------
    #PART 2: LOAD and FORMAT PROJECTED MODELS 
    ICHECDMI = '/exports/csce/datastore/geos/users/s0899345/AFR_44_tasmin/4.5/tasmin_AFR-44_ICHEC-EC-EARTH_rcp45_r3i1p1_DMI-HIRHAM5_v2_day_20060101-20701231.nc'   
    ICHECCCLM = '/exports/csce/datastore/geos/users/s0899345/AFR_44_tasmin/4.5/tasmin_AFR-44_ICHEC-EC-EARTH_rcp45_r12i1p1_CLMcom-CCLM4-8-17_v1_day_20060101-20701231.nc'    
    ICHECKNMI = '/exports/csce/datastore/geos/users/s0899345/AFR_44_tasmin/4.5/tasmin_AFR-44_ICHEC-EC-EARTH_rcp45_r1i1p1_KNMI-RACMO22T_v1_day_20060101-20701231.nc'
    ICHECMPI = '/exports/csce/datastore/geos/users/s0899345/AFR_44_tasmin/4.5/tasmin_AFR-44_ICHEC-EC-EARTH_rcp45_r12i1p1_MPI-CSC-REMO2009_v1_day_20060101-20701231.nc'
    ICHECSMHI = '/exports/csce/datastore/geos/users/s0899345/AFR_44_tasmin/4.5/tasmin_AFR-44_ICHEC-EC-EARTH_rcp45_r12i1p1_SMHI-RCA4_v1_day_20060101-20701231.nc' 
    
    ICHECDMI85 = '/exports/csce/datastore/geos/users/s0899345/AFR_44_tasmin/8.5/tasmin_AFR-44_ICHEC-EC-EARTH_rcp85_r3i1p1_DMI-HIRHAM5_v2_day_20060101-20701231.nc'   
    ICHECCCLM85 = '/exports/csce/datastore/geos/users/s0899345/AFR_44_tasmin/8.5/tasmin_AFR-44_ICHEC-EC-EARTH_rcp85_r12i1p1_CLMcom-CCLM4-8-17_v1_day_20060101-20701231.nc'    
    ICHECKNMI85 = '/exports/csce/datastore/geos/users/s0899345/AFR_44_tasmin/8.5/tasmin_AFR-44_ICHEC-EC-EARTH_rcp85_r1i1p1_KNMI-RACMO22T_v1_day_20060101-20701231.nc'
    ICHECMPI85 = '/exports/csce/datastore/geos/users/s0899345/AFR_44_tasmin/8.5/tasmin_AFR-44_ICHEC-EC-EARTH_rcp85_r12i1p1_MPI-CSC-REMO2009_v1_day_20060101-20701231.nc'
    ICHECSMHI85 = '/exports/csce/datastore/geos/users/s0899345/AFR_44_tasmin/8.5/tasmin_AFR-44_ICHEC-EC-EARTH_rcp85_r12i1p1_SMHI-RCA4_v1_day_20060101-20701231.nc' 
    
    #Load exactly one cube from given file
    ICHECDMI = iris.load_cube(ICHECDMI, 'air_temperature')
    ICHECCCLM = iris.load_cube(ICHECCCLM)
    ICHECKNMI = iris.load_cube(ICHECKNMI)
    ICHECMPI = iris.load_cube(ICHECMPI)
    ICHECSMHI = iris.load_cube(ICHECSMHI)
    
    ICHECDMI85 = iris.load_cube(ICHECDMI85, 'air_temperature')
    ICHECCCLM85 = iris.load_cube(ICHECCCLM85)
    ICHECKNMI85 = iris.load_cube(ICHECKNMI85)
    ICHECMPI85 = iris.load_cube(ICHECMPI85)
    ICHECSMHI85 = iris.load_cube(ICHECSMHI85)
    
    #remove flat latitude and longitude and only use grid latitude and grid longitude to make consistent with the observed data, also make sure all of the longitudes are monotonic. 
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
    ICHECDMI.coord('latitude').guess_bounds()
    ICHECCCLM.coord('latitude').guess_bounds()
    ICHECKNMI.coord('latitude').guess_bounds()
    ICHECMPI.coord('latitude').guess_bounds()
    ICHECSMHI.coord('latitude').guess_bounds()
    
    ICHECDMI85.coord('latitude').guess_bounds()
    ICHECCCLM85.coord('latitude').guess_bounds()
    ICHECKNMI85.coord('latitude').guess_bounds()
    ICHECMPI85.coord('latitude').guess_bounds()
    ICHECSMHI85.coord('latitude').guess_bounds()
    
    ICHECDMI.coord('longitude').guess_bounds()
    ICHECCCLM.coord('longitude').guess_bounds()
    ICHECKNMI.coord('longitude').guess_bounds()
    ICHECMPI.coord('longitude').guess_bounds()
    ICHECSMHI.coord('longitude').guess_bounds()
    
    ICHECDMI85.coord('longitude').guess_bounds()
    ICHECCCLM85.coord('longitude').guess_bounds()
    ICHECKNMI85.coord('longitude').guess_bounds()
    ICHECMPI85.coord('longitude').guess_bounds()
    ICHECSMHI85.coord('longitude').guess_bounds()
    
    
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
    ICHECDMI_past.convert_units('Celsius')
    ICHECCCLM_past.convert_units('Celsius') 
    ICHECKNMI_past.convert_units('Celsius')
    ICHECMPI_past.convert_units('Celsius')
    ICHECSMHI_past.convert_units('Celsius')
    
    ICHECDMI.convert_units('Celsius')
    ICHECCCLM.convert_units('Celsius') 
    ICHECKNMI.convert_units('Celsius')
    ICHECMPI.convert_units('Celsius')
    ICHECSMHI.convert_units('Celsius')
    
    ICHECDMI85.convert_units('Celsius')
    ICHECCCLM85.convert_units('Celsius') 
    ICHECKNMI85.convert_units('Celsius')
    ICHECMPI85.convert_units('Celsius')
    ICHECSMHI85.convert_units('Celsius')
    
    #rename units to match
    CRU.units = Unit('Celsius') 
    
    #limit time series of data
    #time constraint to make past and obsered data only from 1971-2000 
    iris.FUTURE.cell_datetime_objects = True
    t_constraint_past = iris.Constraint(time=lambda cell: 1971 <= cell.point.year <= 2000)
    
    ICHECDMI_past =  ICHECDMI_past.extract(t_constraint_past)
    ICHECCCLM_past =  ICHECCCLM_past.extract(t_constraint_past)
    ICHECKNMI_past =  ICHECKNMI_past.extract(t_constraint_past)
    ICHECMPI_past =  ICHECMPI_past.extract(t_constraint_past)
    ICHECSMHI_past =  ICHECSMHI_past.extract(t_constraint_past)
    
    CRU = CRU.extract(t_constraint_past)
    
    #time constraint to make future data only from 2020-2049
    iris.FUTURE.cell_datetime_objects = True
    t_constraint_future = iris.Constraint(time=lambda cell: 2020 <= cell.point.year <= 2049)
    
    ICHECDMI_30 = ICHECDMI.extract(t_constraint_future)
    ICHECCCLM_30 = ICHECCCLM.extract(t_constraint_future)
    ICHECKNMI_30 = ICHECKNMI.extract(t_constraint_future)
    ICHECMPI_30 = ICHECMPI.extract(t_constraint_future)
    ICHECSMHI_30 = ICHECSMHI.extract(t_constraint_future)
    
    ICHECDMI85_30 = ICHECDMI85.extract(t_constraint_future)
    ICHECCCLM85_30 = ICHECCCLM85.extract(t_constraint_future)
    ICHECKNMI85_30 = ICHECKNMI85.extract(t_constraint_future)
    ICHECMPI85_30 = ICHECMPI85.extract(t_constraint_future)
    ICHECSMHI85_30 = ICHECSMHI85.extract(t_constraint_future)
    
    #time constraint to make future data only from 2040-2069
    iris.FUTURE.cell_datetime_objects = True
    t_constraint_future = iris.Constraint(time=lambda cell: 2040 <= cell.point.year <= 2069)
    
    ICHECDMI_50 = ICHECDMI.extract(t_constraint_future)
    ICHECCCLM_50 = ICHECCCLM.extract(t_constraint_future)
    ICHECKNMI_50 = ICHECKNMI.extract(t_constraint_future)
    ICHECMPI_50 = ICHECMPI.extract(t_constraint_future)
    ICHECSMHI_50 = ICHECSMHI.extract(t_constraint_future)
    
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
    
    ICHECDMI_past_N = ICHECDMI_past.extract(Northern_Malawi)
    ICHECCCLM_past_N = ICHECCCLM_past.extract(Northern_Malawi)
    ICHECKNMI_past_N = ICHECKNMI_past.extract(Northern_Malawi)
    ICHECMPI_past_N = ICHECMPI_past.extract(Northern_Malawi)
    ICHECSMHI_past_N = ICHECSMHI_past.extract(Northern_Malawi)
    
    ICHECDMI_30_N = ICHECDMI_30.extract(Northern_Malawi)
    ICHECCCLM_30_N = ICHECCCLM_30.extract(Northern_Malawi)
    ICHECKNMI_30_N = ICHECKNMI_30.extract(Northern_Malawi)
    ICHECMPI_30_N = ICHECMPI_30.extract(Northern_Malawi)
    ICHECSMHI_30_N = ICHECSMHI_30.extract(Northern_Malawi)
    
    ICHECDMI85_30_N = ICHECDMI85_30.extract(Northern_Malawi)
    ICHECCCLM85_30_N = ICHECCCLM85_30.extract(Northern_Malawi)
    ICHECKNMI85_30_N = ICHECKNMI85_30.extract(Northern_Malawi)
    ICHECMPI85_30_N = ICHECMPI85_30.extract(Northern_Malawi)
    ICHECSMHI85_30_N = ICHECSMHI85_30.extract(Northern_Malawi)
    
    ICHECDMI_50_N = ICHECDMI_50.extract(Northern_Malawi)
    ICHECCCLM_50_N = ICHECCCLM_50.extract(Northern_Malawi)
    ICHECKNMI_50_N = ICHECKNMI_50.extract(Northern_Malawi)
    ICHECMPI_50_N = ICHECMPI_50.extract(Northern_Malawi)
    ICHECSMHI_50_N = ICHECSMHI_50.extract(Northern_Malawi)
    
    ICHECDMI85_50_N = ICHECDMI85_50.extract(Northern_Malawi)
    ICHECCCLM85_50_N = ICHECCCLM85_50.extract(Northern_Malawi)
    ICHECKNMI85_50_N = ICHECKNMI85_50.extract(Northern_Malawi)
    ICHECMPI85_50_N = ICHECMPI85_50.extract(Northern_Malawi)
    ICHECSMHI85_50_N = ICHECSMHI85_50.extract(Northern_Malawi)
    
    CRU_N = CRU.extract(Northern_Malawi)
    
    #Returns an array of area weights, with the same dimensions as the cube
    ICHECDMI_past_N_grid_areas = iris.analysis.cartography.area_weights(ICHECDMI_past_N)
    ICHECCCLM_past_N_grid_areas = iris.analysis.cartography.area_weights(ICHECCCLM_past_N)
    ICHECKNMI_past_N_grid_areas = iris.analysis.cartography.area_weights(ICHECKNMI_past_N)
    ICHECMPI_past_N_grid_areas = iris.analysis.cartography.area_weights(ICHECMPI_past_N)
    ICHECSMHI_past_N_grid_areas = iris.analysis.cartography.area_weights(ICHECSMHI_past_N)
    
    ICHECDMI_30_N_grid_areas = iris.analysis.cartography.area_weights(ICHECDMI_30_N)
    ICHECCCLM_30_N_grid_areas = iris.analysis.cartography.area_weights(ICHECCCLM_30_N)
    ICHECKNMI_30_N_grid_areas = iris.analysis.cartography.area_weights(ICHECKNMI_30_N)
    ICHECMPI_30_N_grid_areas = iris.analysis.cartography.area_weights(ICHECMPI_30_N)
    ICHECSMHI_30_N_grid_areas = iris.analysis.cartography.area_weights(ICHECSMHI_30_N)
    
    ICHECDMI85_30_N_grid_areas = iris.analysis.cartography.area_weights(ICHECDMI85_30_N)
    ICHECCCLM85_30_N_grid_areas = iris.analysis.cartography.area_weights(ICHECCCLM85_30_N)
    ICHECKNMI85_30_N_grid_areas = iris.analysis.cartography.area_weights(ICHECKNMI85_30_N)
    ICHECMPI85_30_N_grid_areas = iris.analysis.cartography.area_weights(ICHECMPI85_30_N)
    ICHECSMHI85_30_N_grid_areas = iris.analysis.cartography.area_weights(ICHECSMHI85_30_N)
    
    ICHECDMI_50_N_grid_areas = iris.analysis.cartography.area_weights(ICHECDMI_50_N)
    ICHECCCLM_50_N_grid_areas = iris.analysis.cartography.area_weights(ICHECCCLM_50_N)
    ICHECKNMI_50_N_grid_areas = iris.analysis.cartography.area_weights(ICHECKNMI_50_N)
    ICHECMPI_50_N_grid_areas = iris.analysis.cartography.area_weights(ICHECMPI_50_N)
    ICHECSMHI_50_N_grid_areas = iris.analysis.cartography.area_weights(ICHECSMHI_50_N)
    
    ICHECDMI85_50_N_grid_areas = iris.analysis.cartography.area_weights(ICHECDMI85_50_N)
    ICHECCCLM85_50_N_grid_areas = iris.analysis.cartography.area_weights(ICHECCCLM85_50_N)
    ICHECKNMI85_50_N_grid_areas = iris.analysis.cartography.area_weights(ICHECKNMI85_50_N)
    ICHECMPI85_50_N_grid_areas = iris.analysis.cartography.area_weights(ICHECMPI85_50_N)
    ICHECSMHI85_50_N_grid_areas = iris.analysis.cartography.area_weights(ICHECSMHI85_50_N)
    
    CRU_N_grid_areas = iris.analysis.cartography.area_weights(CRU_N)
    
    #We want to plot the mean for the whole region so we need a mean of all the lats and lons
    ICHECDMI_past_N_mean = ICHECDMI_past_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECDMI_past_N_grid_areas) 
    ICHECCCLM_past_N_mean = ICHECCCLM_past_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECCCLM_past_N_grid_areas)
    ICHECKNMI_past_N_mean = ICHECKNMI_past_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECKNMI_past_N_grid_areas)
    ICHECMPI_past_N_mean = ICHECMPI_past_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECMPI_past_N_grid_areas)
    ICHECSMHI_past_N_mean = ICHECSMHI_past_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECSMHI_past_N_grid_areas)
    
    ICHECDMI_30_N_mean = ICHECDMI_30_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECDMI_30_N_grid_areas) 
    ICHECCCLM_30_N_mean = ICHECCCLM_30_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECCCLM_30_N_grid_areas)
    ICHECKNMI_30_N_mean = ICHECKNMI_30_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECKNMI_30_N_grid_areas)
    ICHECMPI_30_N_mean = ICHECMPI_30_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECMPI_30_N_grid_areas)
    ICHECSMHI_30_N_mean = ICHECSMHI_30_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECSMHI_30_N_grid_areas)
    
    ICHECDMI85_30_N_mean = ICHECDMI85_30_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECDMI85_30_N_grid_areas) 
    ICHECCCLM85_30_N_mean = ICHECCCLM85_30_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECCCLM85_30_N_grid_areas)
    ICHECKNMI85_30_N_mean = ICHECKNMI85_30_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECKNMI85_30_N_grid_areas)
    ICHECMPI85_30_N_mean = ICHECMPI85_30_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECMPI85_30_N_grid_areas)
    ICHECSMHI85_30_N_mean = ICHECSMHI85_30_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECSMHI85_30_N_grid_areas)
    
    ICHECDMI_50_N_mean = ICHECDMI_50_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECDMI_50_N_grid_areas) 
    ICHECCCLM_50_N_mean = ICHECCCLM_50_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECCCLM_50_N_grid_areas)
    ICHECKNMI_50_N_mean = ICHECKNMI_50_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECKNMI_50_N_grid_areas)
    ICHECMPI_50_N_mean = ICHECMPI_50_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECMPI_50_N_grid_areas)
    ICHECSMHI_50_N_mean = ICHECSMHI_50_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECSMHI_50_N_grid_areas)
    
    ICHECDMI85_50_N_mean = ICHECDMI85_50_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECDMI85_50_N_grid_areas) 
    ICHECCCLM85_50_N_mean = ICHECCCLM85_50_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECCCLM85_50_N_grid_areas)
    ICHECKNMI85_50_N_mean = ICHECKNMI85_50_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECKNMI85_50_N_grid_areas)
    ICHECMPI85_50_N_mean = ICHECMPI85_50_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECMPI85_50_N_grid_areas)
    ICHECSMHI85_50_N_mean = ICHECSMHI85_50_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECSMHI85_50_N_grid_areas)
    
    CRU_N_mean = CRU_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CRU_N_grid_areas)
    
    #for the baseline we don't need to average for each year, but the average for the whole time period, so collapse by time
    ICHECDMI_b_N_mean = ICHECDMI_past_N_mean.collapsed(['time'], iris.analysis.MEAN)  
    ICHECCCLM_b_N_mean = ICHECCCLM_past_N_mean.collapsed(['time'], iris.analysis.MEAN) 
    ICHECKNMI_b_N_mean = ICHECKNMI_past_N_mean.collapsed(['time'], iris.analysis.MEAN) 
    ICHECMPI_b_N_mean = ICHECMPI_past_N_mean.collapsed(['time'], iris.analysis.MEAN) 
    ICHECSMHI_b_N_mean = ICHECSMHI_past_N_mean.collapsed(['time'], iris.analysis.MEAN)
    
    CRU_N_mean = CRU_N_mean.collapsed(['time'], iris.analysis.MEAN) 
    
    #create average of observed baseline data
    Obs_N = (CRU_N_mean)
    
    #We want to see the change in temperature from the baseline
    ICHECDMI_past_N_mean = (ICHECDMI_past_N_mean.data - ICHECDMI_b_N_mean.data + Obs_N.data) 
    ICHECCCLM_past_N_mean = (ICHECCCLM_past_N_mean.data - ICHECCCLM_b_N_mean.data + Obs_N.data)
    ICHECKNMI_past_N_mean = (ICHECKNMI_past_N_mean.data - ICHECKNMI_b_N_mean.data + Obs_N.data)
    ICHECMPI_past_N_mean = (ICHECMPI_past_N_mean.data - ICHECMPI_b_N_mean.data + Obs_N.data)
    ICHECSMHI_past_N_mean = (ICHECSMHI_past_N_mean.data - ICHECSMHI_b_N_mean.data + Obs_N.data)
    
    ICHECDMI_30_N_mean = (ICHECDMI_30_N_mean.data - ICHECDMI_b_N_mean.data + Obs_N.data) 
    ICHECCCLM_30_N_mean = (ICHECCCLM_30_N_mean.data - ICHECCCLM_b_N_mean.data + Obs_N.data)
    ICHECKNMI_30_N_mean = (ICHECKNMI_30_N_mean.data - ICHECKNMI_b_N_mean.data + Obs_N.data)
    ICHECMPI_30_N_mean = (ICHECMPI_30_N_mean.data - ICHECMPI_b_N_mean.data + Obs_N.data)
    ICHECSMHI_30_N_mean = (ICHECSMHI_30_N_mean.data - ICHECSMHI_b_N_mean.data + Obs_N.data)
    
    ICHECDMI85_30_N_mean = (ICHECDMI85_30_N_mean.data - ICHECDMI_b_N_mean.data + Obs_N.data) 
    ICHECCCLM85_30_N_mean = (ICHECCCLM85_30_N_mean.data - ICHECCCLM_b_N_mean.data + Obs_N.data)
    ICHECKNMI85_30_N_mean = (ICHECKNMI85_30_N_mean.data - ICHECKNMI_b_N_mean.data + Obs_N.data)
    ICHECMPI85_30_N_mean = (ICHECMPI85_30_N_mean.data - ICHECMPI_b_N_mean.data + Obs_N.data)
    ICHECSMHI85_30_N_mean = (ICHECSMHI85_30_N_mean.data - ICHECSMHI_b_N_mean.data + Obs_N.data)
    
    ICHECDMI_50_N_mean = (ICHECDMI_50_N_mean.data - ICHECDMI_b_N_mean.data + Obs_N.data) 
    ICHECCCLM_50_N_mean = (ICHECCCLM_50_N_mean.data - ICHECCCLM_b_N_mean.data + Obs_N.data)
    ICHECKNMI_50_N_mean = (ICHECKNMI_50_N_mean.data - ICHECKNMI_b_N_mean.data + Obs_N.data)
    ICHECMPI_50_N_mean = (ICHECMPI_50_N_mean.data - ICHECMPI_b_N_mean.data + Obs_N.data)
    ICHECSMHI_50_N_mean = (ICHECSMHI_50_N_mean.data - ICHECSMHI_b_N_mean.data + Obs_N.data)
    
    ICHECDMI85_50_N_mean = (ICHECDMI85_50_N_mean.data - ICHECDMI_b_N_mean.data + Obs_N.data) 
    ICHECCCLM85_50_N_mean = (ICHECCCLM85_50_N_mean.data - ICHECCCLM_b_N_mean.data + Obs_N.data)
    ICHECKNMI85_50_N_mean = (ICHECKNMI85_50_N_mean.data - ICHECKNMI_b_N_mean.data + Obs_N.data)
    ICHECMPI85_50_N_mean = (ICHECMPI85_50_N_mean.data - ICHECMPI_b_N_mean.data + Obs_N.data)
    ICHECSMHI85_50_N_mean = (ICHECSMHI85_50_N_mean.data - ICHECSMHI_b_N_mean.data + Obs_N.data)
    
    
    #PART 5B: CENTRAL MALAWI
    #we are only interested in the latitude and longitude relevant to Central Malawi 
    Central_Malawi = iris.Constraint(longitude=lambda v: 32.5 <= v <= 35.5, latitude=lambda v: -15 <= v <= -11.5) 
    
    ICHECDMI_past_C = ICHECDMI_past.extract(Central_Malawi)
    ICHECCCLM_past_C = ICHECCCLM_past.extract(Central_Malawi)
    ICHECKNMI_past_C = ICHECKNMI_past.extract(Central_Malawi)
    ICHECMPI_past_C = ICHECMPI_past.extract(Central_Malawi)
    ICHECSMHI_past_C = ICHECSMHI_past.extract(Central_Malawi)
    
    ICHECDMI_30_C = ICHECDMI_30.extract(Central_Malawi)
    ICHECCCLM_30_C = ICHECCCLM_30.extract(Central_Malawi)
    ICHECKNMI_30_C = ICHECKNMI_30.extract(Central_Malawi)
    ICHECMPI_30_C = ICHECMPI_30.extract(Central_Malawi)
    ICHECSMHI_30_C = ICHECSMHI_30.extract(Central_Malawi)
    
    ICHECDMI85_30_C = ICHECDMI85_30.extract(Central_Malawi)
    ICHECCCLM85_30_C = ICHECCCLM85_30.extract(Central_Malawi)
    ICHECKNMI85_30_C = ICHECKNMI85_30.extract(Central_Malawi)
    ICHECMPI85_30_C = ICHECMPI85_30.extract(Central_Malawi)
    ICHECSMHI85_30_C = ICHECSMHI85_30.extract(Central_Malawi)
    
    ICHECDMI_50_C = ICHECDMI_50.extract(Central_Malawi)
    ICHECCCLM_50_C = ICHECCCLM_50.extract(Central_Malawi)
    ICHECKNMI_50_C = ICHECKNMI_50.extract(Central_Malawi)
    ICHECMPI_50_C = ICHECMPI_50.extract(Central_Malawi)
    ICHECSMHI_50_C = ICHECSMHI_50.extract(Central_Malawi)
    
    ICHECDMI85_50_C = ICHECDMI85_50.extract(Central_Malawi)
    ICHECCCLM85_50_C = ICHECCCLM85_50.extract(Central_Malawi)
    ICHECKNMI85_50_C = ICHECKNMI85_50.extract(Central_Malawi)
    ICHECMPI85_50_C = ICHECMPI85_50.extract(Central_Malawi)
    ICHECSMHI85_50_C = ICHECSMHI85_50.extract(Central_Malawi)
    
    CRU_C = CRU.extract(Central_Malawi)
    
    #Returns an array of area weights, with the same dimensions as the cube
    ICHECDMI_past_C_grid_areas = iris.analysis.cartography.area_weights(ICHECDMI_past_C)
    ICHECCCLM_past_C_grid_areas = iris.analysis.cartography.area_weights(ICHECCCLM_past_C)
    ICHECKNMI_past_C_grid_areas = iris.analysis.cartography.area_weights(ICHECKNMI_past_C)
    ICHECMPI_past_C_grid_areas = iris.analysis.cartography.area_weights(ICHECMPI_past_C)
    ICHECSMHI_past_C_grid_areas = iris.analysis.cartography.area_weights(ICHECSMHI_past_C)
    
    ICHECDMI_30_C_grid_areas = iris.analysis.cartography.area_weights(ICHECDMI_30_C)
    ICHECCCLM_30_C_grid_areas = iris.analysis.cartography.area_weights(ICHECCCLM_30_C)
    ICHECKNMI_30_C_grid_areas = iris.analysis.cartography.area_weights(ICHECKNMI_30_C)
    ICHECMPI_30_C_grid_areas = iris.analysis.cartography.area_weights(ICHECMPI_30_C)
    ICHECSMHI_30_C_grid_areas = iris.analysis.cartography.area_weights(ICHECSMHI_30_C)
    
    ICHECDMI85_30_C_grid_areas = iris.analysis.cartography.area_weights(ICHECDMI85_30_C)
    ICHECCCLM85_30_C_grid_areas = iris.analysis.cartography.area_weights(ICHECCCLM85_30_C)
    ICHECKNMI85_30_C_grid_areas = iris.analysis.cartography.area_weights(ICHECKNMI85_30_C)
    ICHECMPI85_30_C_grid_areas = iris.analysis.cartography.area_weights(ICHECMPI85_30_C)
    ICHECSMHI85_30_C_grid_areas = iris.analysis.cartography.area_weights(ICHECSMHI85_30_C)
    
    ICHECDMI_50_C_grid_areas = iris.analysis.cartography.area_weights(ICHECDMI_50_C)
    ICHECCCLM_50_C_grid_areas = iris.analysis.cartography.area_weights(ICHECCCLM_50_C)
    ICHECKNMI_50_C_grid_areas = iris.analysis.cartography.area_weights(ICHECKNMI_50_C)
    ICHECMPI_50_C_grid_areas = iris.analysis.cartography.area_weights(ICHECMPI_50_C)
    ICHECSMHI_50_C_grid_areas = iris.analysis.cartography.area_weights(ICHECSMHI_50_C)
    
    ICHECDMI85_50_C_grid_areas = iris.analysis.cartography.area_weights(ICHECDMI85_50_C)
    ICHECCCLM85_50_C_grid_areas = iris.analysis.cartography.area_weights(ICHECCCLM85_50_C)
    ICHECKNMI85_50_C_grid_areas = iris.analysis.cartography.area_weights(ICHECKNMI85_50_C)
    ICHECMPI85_50_C_grid_areas = iris.analysis.cartography.area_weights(ICHECMPI85_50_C)
    ICHECSMHI85_50_C_grid_areas = iris.analysis.cartography.area_weights(ICHECSMHI85_50_C)
    
    CRU_C_grid_areas = iris.analysis.cartography.area_weights(CRU_C) 
    
    #We want to plot the mean for the whole region so we need a mean of all the lats and lons
    ICHECDMI_past_C_mean = ICHECDMI_past_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECDMI_past_C_grid_areas) 
    ICHECCCLM_past_C_mean = ICHECCCLM_past_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECCCLM_past_C_grid_areas)
    ICHECKNMI_past_C_mean = ICHECKNMI_past_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECKNMI_past_C_grid_areas)
    ICHECMPI_past_C_mean = ICHECMPI_past_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECMPI_past_C_grid_areas)
    ICHECSMHI_past_C_mean = ICHECSMHI_past_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECSMHI_past_C_grid_areas)
    
    ICHECDMI_30_C_mean = ICHECDMI_30_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECDMI_30_C_grid_areas) 
    ICHECCCLM_30_C_mean = ICHECCCLM_30_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECCCLM_30_C_grid_areas)
    ICHECKNMI_30_C_mean = ICHECKNMI_30_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECKNMI_30_C_grid_areas)
    ICHECMPI_30_C_mean = ICHECMPI_30_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECMPI_30_C_grid_areas)
    ICHECSMHI_30_C_mean = ICHECSMHI_30_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECSMHI_30_C_grid_areas)
    
    ICHECDMI85_30_C_mean = ICHECDMI85_30_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECDMI85_30_C_grid_areas) 
    ICHECCCLM85_30_C_mean = ICHECCCLM85_30_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECCCLM85_30_C_grid_areas)
    ICHECKNMI85_30_C_mean = ICHECKNMI85_30_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECKNMI85_30_C_grid_areas)
    ICHECMPI85_30_C_mean = ICHECMPI85_30_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECMPI85_30_C_grid_areas)
    ICHECSMHI85_30_C_mean = ICHECSMHI85_30_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECSMHI85_30_C_grid_areas)
    
    ICHECDMI_50_C_mean = ICHECDMI_50_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECDMI_50_C_grid_areas) 
    ICHECCCLM_50_C_mean = ICHECCCLM_50_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECCCLM_50_C_grid_areas)
    ICHECKNMI_50_C_mean = ICHECKNMI_50_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECKNMI_50_C_grid_areas)
    ICHECMPI_50_C_mean = ICHECMPI_50_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECMPI_50_C_grid_areas)
    ICHECSMHI_50_C_mean = ICHECSMHI_50_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECSMHI_50_C_grid_areas)
    
    ICHECDMI85_50_C_mean = ICHECDMI85_50_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECDMI85_50_C_grid_areas) 
    ICHECCCLM85_50_C_mean = ICHECCCLM85_50_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECCCLM85_50_C_grid_areas)
    ICHECKNMI85_50_C_mean = ICHECKNMI85_50_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECKNMI85_50_C_grid_areas)
    ICHECMPI85_50_C_mean = ICHECMPI85_50_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECMPI85_50_C_grid_areas)
    ICHECSMHI85_50_C_mean = ICHECSMHI85_50_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECSMHI85_50_C_grid_areas)
    
    CRU_C_mean = CRU_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CRU_C_grid_areas)
    
    #for the baseline we don't need to average for each year, but the average for the whole time period, so collapse by time
    ICHECDMI_b_C_mean = ICHECDMI_past_C_mean.collapsed(['time'], iris.analysis.MEAN)  
    ICHECCCLM_b_C_mean = ICHECCCLM_past_C_mean.collapsed(['time'], iris.analysis.MEAN) 
    ICHECKNMI_b_C_mean = ICHECKNMI_past_C_mean.collapsed(['time'], iris.analysis.MEAN) 
    ICHECMPI_b_C_mean = ICHECMPI_past_C_mean.collapsed(['time'], iris.analysis.MEAN) 
    ICHECSMHI_b_C_mean = ICHECSMHI_past_C_mean.collapsed(['time'], iris.analysis.MEAN)
    
    CRU_C_mean = CRU_C_mean.collapsed(['time'], iris.analysis.MEAN) 
    
    #create average of observed baseline data
    Obs_C = (CRU_C_mean)
    
    #We want to see the change in temperature from the baseline
    ICHECDMI_past_C_mean = (ICHECDMI_past_C_mean.data - ICHECDMI_b_C_mean.data + Obs_C.data) 
    ICHECCCLM_past_C_mean = (ICHECCCLM_past_C_mean.data - ICHECCCLM_b_C_mean.data + Obs_C.data)
    ICHECKNMI_past_C_mean = (ICHECKNMI_past_C_mean.data - ICHECKNMI_b_C_mean.data + Obs_C.data)
    ICHECMPI_past_C_mean = (ICHECMPI_past_C_mean.data - ICHECMPI_b_C_mean.data + Obs_C.data)
    ICHECSMHI_past_C_mean = (ICHECSMHI_past_C_mean.data - ICHECSMHI_b_C_mean.data + Obs_C.data)
    
    ICHECDMI_30_C_mean = (ICHECDMI_30_C_mean.data - ICHECDMI_b_C_mean.data + Obs_C.data) 
    ICHECCCLM_30_C_mean = (ICHECCCLM_30_C_mean.data - ICHECCCLM_b_C_mean.data + Obs_C.data)
    ICHECKNMI_30_C_mean = (ICHECKNMI_30_C_mean.data - ICHECKNMI_b_C_mean.data + Obs_C.data)
    ICHECMPI_30_C_mean = (ICHECMPI_30_C_mean.data - ICHECMPI_b_C_mean.data + Obs_C.data)
    ICHECSMHI_30_C_mean = (ICHECSMHI_30_C_mean.data - ICHECSMHI_b_C_mean.data + Obs_C.data)
    
    ICHECDMI85_30_C_mean = (ICHECDMI85_30_C_mean.data - ICHECDMI_b_C_mean.data + Obs_C.data) 
    ICHECCCLM85_30_C_mean = (ICHECCCLM85_30_C_mean.data - ICHECCCLM_b_C_mean.data + Obs_C.data)
    ICHECKNMI85_30_C_mean = (ICHECKNMI85_30_C_mean.data - ICHECKNMI_b_C_mean.data + Obs_C.data)
    ICHECMPI85_30_C_mean = (ICHECMPI85_30_C_mean.data - ICHECMPI_b_C_mean.data + Obs_C.data)
    ICHECSMHI85_30_C_mean = (ICHECSMHI85_30_C_mean.data - ICHECSMHI_b_C_mean.data + Obs_C.data)
    
    ICHECDMI_50_C_mean = (ICHECDMI_50_C_mean.data - ICHECDMI_b_C_mean.data + Obs_C.data) 
    ICHECCCLM_50_C_mean = (ICHECCCLM_50_C_mean.data - ICHECCCLM_b_C_mean.data + Obs_C.data)
    ICHECKNMI_50_C_mean = (ICHECKNMI_50_C_mean.data - ICHECKNMI_b_C_mean.data + Obs_C.data)
    ICHECMPI_50_C_mean = (ICHECMPI_50_C_mean.data - ICHECMPI_b_C_mean.data + Obs_C.data)
    ICHECSMHI_50_C_mean = (ICHECSMHI_50_C_mean.data - ICHECSMHI_b_C_mean.data + Obs_C.data)
    
    ICHECDMI85_50_C_mean = (ICHECDMI85_50_C_mean.data - ICHECDMI_b_C_mean.data + Obs_C.data) 
    ICHECCCLM85_50_C_mean = (ICHECCCLM85_50_C_mean.data - ICHECCCLM_b_C_mean.data + Obs_C.data)
    ICHECKNMI85_50_C_mean = (ICHECKNMI85_50_C_mean.data - ICHECKNMI_b_C_mean.data + Obs_C.data)
    ICHECMPI85_50_C_mean = (ICHECMPI85_50_C_mean.data - ICHECMPI_b_C_mean.data + Obs_C.data)
    ICHECSMHI85_50_C_mean = (ICHECSMHI85_50_C_mean.data - ICHECSMHI_b_C_mean.data + Obs_C.data)
    
            
    #PART 5C: SOUTHERN MALAWI
    #we are only interested in the latitude and longitude relevant to Southern Malawi 
    Southern_Malawi = iris.Constraint(longitude=lambda v: 34 <= v <= 36.5, latitude=lambda v: -17.5 <= v <= -14) 
    
    ICHECDMI_past_S = ICHECDMI_past.extract(Southern_Malawi)
    ICHECCCLM_past_S = ICHECCCLM_past.extract(Southern_Malawi)
    ICHECKNMI_past_S = ICHECKNMI_past.extract(Southern_Malawi)
    ICHECMPI_past_S = ICHECMPI_past.extract(Southern_Malawi)
    ICHECSMHI_past_S = ICHECSMHI_past.extract(Southern_Malawi)
    
    ICHECDMI_30_S = ICHECDMI_30.extract(Southern_Malawi)
    ICHECCCLM_30_S = ICHECCCLM_30.extract(Southern_Malawi)
    ICHECKNMI_30_S = ICHECKNMI_30.extract(Southern_Malawi)
    ICHECMPI_30_S = ICHECMPI_30.extract(Southern_Malawi)
    ICHECSMHI_30_S = ICHECSMHI_30.extract(Southern_Malawi)
    
    ICHECDMI85_30_S = ICHECDMI85_30.extract(Southern_Malawi)
    ICHECCCLM85_30_S = ICHECCCLM85_30.extract(Southern_Malawi)
    ICHECKNMI85_30_S = ICHECKNMI85_30.extract(Southern_Malawi)
    ICHECMPI85_30_S = ICHECMPI85_30.extract(Southern_Malawi)
    ICHECSMHI85_30_S = ICHECSMHI85_30.extract(Southern_Malawi)
    
    ICHECDMI_50_S = ICHECDMI_50.extract(Southern_Malawi)
    ICHECCCLM_50_S = ICHECCCLM_50.extract(Southern_Malawi)
    ICHECKNMI_50_S = ICHECKNMI_50.extract(Southern_Malawi)
    ICHECMPI_50_S = ICHECMPI_50.extract(Southern_Malawi)
    ICHECSMHI_50_S = ICHECSMHI_50.extract(Southern_Malawi)
    
    ICHECDMI85_50_S = ICHECDMI85_50.extract(Southern_Malawi)
    ICHECCCLM85_50_S = ICHECCCLM85_50.extract(Southern_Malawi)
    ICHECKNMI85_50_S = ICHECKNMI85_50.extract(Southern_Malawi)
    ICHECMPI85_50_S = ICHECMPI85_50.extract(Southern_Malawi)
    ICHECSMHI85_50_S = ICHECSMHI85_50.extract(Southern_Malawi)
    
    CRU_S = CRU.extract(Southern_Malawi)
    
    #Returns an array of area weights, with the same dimensions as the cube
    ICHECDMI_past_S_grid_areas = iris.analysis.cartography.area_weights(ICHECDMI_past_S)
    ICHECCCLM_past_S_grid_areas = iris.analysis.cartography.area_weights(ICHECCCLM_past_S)
    ICHECKNMI_past_S_grid_areas = iris.analysis.cartography.area_weights(ICHECKNMI_past_S)
    ICHECMPI_past_S_grid_areas = iris.analysis.cartography.area_weights(ICHECMPI_past_S)
    ICHECSMHI_past_S_grid_areas = iris.analysis.cartography.area_weights(ICHECSMHI_past_S)
    
    ICHECDMI_30_S_grid_areas = iris.analysis.cartography.area_weights(ICHECDMI_30_S)
    ICHECCCLM_30_S_grid_areas = iris.analysis.cartography.area_weights(ICHECCCLM_30_S)
    ICHECKNMI_30_S_grid_areas = iris.analysis.cartography.area_weights(ICHECKNMI_30_S)
    ICHECMPI_30_S_grid_areas = iris.analysis.cartography.area_weights(ICHECMPI_30_S)
    ICHECSMHI_30_S_grid_areas = iris.analysis.cartography.area_weights(ICHECSMHI_30_S)
    
    ICHECDMI85_30_S_grid_areas = iris.analysis.cartography.area_weights(ICHECDMI85_30_S)
    ICHECCCLM85_30_S_grid_areas = iris.analysis.cartography.area_weights(ICHECCCLM85_30_S)
    ICHECKNMI85_30_S_grid_areas = iris.analysis.cartography.area_weights(ICHECKNMI85_30_S)
    ICHECMPI85_30_S_grid_areas = iris.analysis.cartography.area_weights(ICHECMPI85_30_S)
    ICHECSMHI85_30_S_grid_areas = iris.analysis.cartography.area_weights(ICHECSMHI85_30_S)
    
    ICHECDMI_50_S_grid_areas = iris.analysis.cartography.area_weights(ICHECDMI_50_S)
    ICHECCCLM_50_S_grid_areas = iris.analysis.cartography.area_weights(ICHECCCLM_50_S)
    ICHECKNMI_50_S_grid_areas = iris.analysis.cartography.area_weights(ICHECKNMI_50_S)
    ICHECMPI_50_S_grid_areas = iris.analysis.cartography.area_weights(ICHECMPI_50_S)
    ICHECSMHI_50_S_grid_areas = iris.analysis.cartography.area_weights(ICHECSMHI_50_S)
    
    ICHECDMI85_50_S_grid_areas = iris.analysis.cartography.area_weights(ICHECDMI85_50_S)
    ICHECCCLM85_50_S_grid_areas = iris.analysis.cartography.area_weights(ICHECCCLM85_50_S)
    ICHECKNMI85_50_S_grid_areas = iris.analysis.cartography.area_weights(ICHECKNMI85_50_S)
    ICHECMPI85_50_S_grid_areas = iris.analysis.cartography.area_weights(ICHECMPI85_50_S)
    ICHECSMHI85_50_S_grid_areas = iris.analysis.cartography.area_weights(ICHECSMHI85_50_S)
    
    CRU_S_grid_areas = iris.analysis.cartography.area_weights(CRU_S)
    
    #We want to plot the mean for the whole region so we need a mean of all the lats and lons
    ICHECDMI_past_S_mean = ICHECDMI_past_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECDMI_past_S_grid_areas) 
    ICHECCCLM_past_S_mean = ICHECCCLM_past_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECCCLM_past_S_grid_areas)
    ICHECKNMI_past_S_mean = ICHECKNMI_past_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECKNMI_past_S_grid_areas)
    ICHECMPI_past_S_mean = ICHECMPI_past_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECMPI_past_S_grid_areas)
    ICHECSMHI_past_S_mean = ICHECSMHI_past_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECSMHI_past_S_grid_areas)
    
    ICHECDMI_30_S_mean = ICHECDMI_30_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECDMI_30_S_grid_areas) 
    ICHECCCLM_30_S_mean = ICHECCCLM_30_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECCCLM_30_S_grid_areas)
    ICHECKNMI_30_S_mean = ICHECKNMI_30_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECKNMI_30_S_grid_areas)
    ICHECMPI_30_S_mean = ICHECMPI_30_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECMPI_30_S_grid_areas)
    ICHECSMHI_30_S_mean = ICHECSMHI_30_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECSMHI_30_S_grid_areas)
    
    ICHECDMI85_30_S_mean = ICHECDMI85_30_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECDMI85_30_S_grid_areas) 
    ICHECCCLM85_30_S_mean = ICHECCCLM85_30_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECCCLM85_30_S_grid_areas)
    ICHECKNMI85_30_S_mean = ICHECKNMI85_30_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECKNMI85_30_S_grid_areas)
    ICHECMPI85_30_S_mean = ICHECMPI85_30_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECMPI85_30_S_grid_areas)
    ICHECSMHI85_30_S_mean = ICHECSMHI85_30_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECSMHI85_30_S_grid_areas)
    
    ICHECDMI_50_S_mean = ICHECDMI_50_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECDMI_50_S_grid_areas) 
    ICHECCCLM_50_S_mean = ICHECCCLM_50_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECCCLM_50_S_grid_areas)
    ICHECKNMI_50_S_mean = ICHECKNMI_50_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECKNMI_50_S_grid_areas)
    ICHECMPI_50_S_mean = ICHECMPI_50_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECMPI_50_S_grid_areas)
    ICHECSMHI_50_S_mean = ICHECSMHI_50_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECSMHI_50_S_grid_areas)
    
    ICHECDMI85_50_S_mean = ICHECDMI85_50_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECDMI85_50_S_grid_areas) 
    ICHECCCLM85_50_S_mean = ICHECCCLM85_50_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECCCLM85_50_S_grid_areas)
    ICHECKNMI85_50_S_mean = ICHECKNMI85_50_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECKNMI85_50_S_grid_areas)
    ICHECMPI85_50_S_mean = ICHECMPI85_50_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECMPI85_50_S_grid_areas)
    ICHECSMHI85_50_S_mean = ICHECSMHI85_50_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECSMHI85_50_S_grid_areas)
    
    CRU_S_mean = CRU_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CRU_S_grid_areas)
    
    #for the baseline we don't need to average for each year, but the average for the whole time period, so collapse by time
    ICHECDMI_b_S_mean = ICHECDMI_past_S_mean.collapsed(['time'], iris.analysis.MEAN)  
    ICHECCCLM_b_S_mean = ICHECCCLM_past_S_mean.collapsed(['time'], iris.analysis.MEAN) 
    ICHECKNMI_b_S_mean = ICHECKNMI_past_S_mean.collapsed(['time'], iris.analysis.MEAN) 
    ICHECMPI_b_S_mean = ICHECMPI_past_S_mean.collapsed(['time'], iris.analysis.MEAN) 
    ICHECSMHI_b_S_mean = ICHECSMHI_past_S_mean.collapsed(['time'], iris.analysis.MEAN)
    
    CRU_S_mean = CRU_S_mean.collapsed(['time'], iris.analysis.MEAN)  
    
    #create average of observed baseline data
    Obs_S = (CRU_S_mean)
    
    #We want to see the change in temperature from the baseline
    ICHECDMI_past_S_mean = (ICHECDMI_past_S_mean.data - ICHECDMI_b_S_mean.data + Obs_S.data) 
    ICHECCCLM_past_S_mean = (ICHECCCLM_past_S_mean.data - ICHECCCLM_b_S_mean.data + Obs_S.data)
    ICHECKNMI_past_S_mean = (ICHECKNMI_past_S_mean.data - ICHECKNMI_b_S_mean.data + Obs_S.data)
    ICHECMPI_past_S_mean = (ICHECMPI_past_S_mean.data - ICHECMPI_b_S_mean.data + Obs_S.data)
    ICHECSMHI_past_S_mean = (ICHECSMHI_past_S_mean.data - ICHECSMHI_b_S_mean.data + Obs_S.data)
    
    ICHECDMI_30_S_mean = (ICHECDMI_30_S_mean.data - ICHECDMI_b_S_mean.data + Obs_S.data) 
    ICHECCCLM_30_S_mean = (ICHECCCLM_30_S_mean.data - ICHECCCLM_b_S_mean.data + Obs_S.data)
    ICHECKNMI_30_S_mean = (ICHECKNMI_30_S_mean.data - ICHECKNMI_b_S_mean.data + Obs_S.data)
    ICHECMPI_30_S_mean = (ICHECMPI_30_S_mean.data - ICHECMPI_b_S_mean.data + Obs_S.data)
    ICHECSMHI_30_S_mean = (ICHECSMHI_30_S_mean.data - ICHECSMHI_b_S_mean.data + Obs_S.data)
    
    ICHECDMI85_30_S_mean = (ICHECDMI85_30_S_mean.data - ICHECDMI_b_S_mean.data + Obs_S.data) 
    ICHECCCLM85_30_S_mean = (ICHECCCLM85_30_S_mean.data - ICHECCCLM_b_S_mean.data + Obs_S.data)
    ICHECKNMI85_30_S_mean = (ICHECKNMI85_30_S_mean.data - ICHECKNMI_b_S_mean.data + Obs_S.data)
    ICHECMPI85_30_S_mean = (ICHECMPI85_30_S_mean.data - ICHECMPI_b_S_mean.data + Obs_S.data)
    ICHECSMHI85_30_S_mean = (ICHECSMHI85_30_S_mean.data - ICHECSMHI_b_S_mean.data + Obs_S.data)
    
    ICHECDMI_50_S_mean = (ICHECDMI_50_S_mean.data - ICHECDMI_b_S_mean.data + Obs_S.data) 
    ICHECCCLM_50_S_mean = (ICHECCCLM_50_S_mean.data - ICHECCCLM_b_S_mean.data + Obs_S.data)
    ICHECKNMI_50_S_mean = (ICHECKNMI_50_S_mean.data - ICHECKNMI_b_S_mean.data + Obs_S.data)
    ICHECMPI_50_S_mean = (ICHECMPI_50_S_mean.data - ICHECMPI_b_S_mean.data + Obs_S.data)
    ICHECSMHI_50_S_mean = (ICHECSMHI_50_S_mean.data - ICHECSMHI_b_S_mean.data + Obs_S.data)
    
    ICHECDMI85_50_S_mean = (ICHECDMI85_50_S_mean.data - ICHECDMI_b_S_mean.data + Obs_S.data) 
    ICHECCCLM85_50_S_mean = (ICHECCCLM85_50_S_mean.data - ICHECCCLM_b_S_mean.data + Obs_S.data)
    ICHECKNMI85_50_S_mean = (ICHECKNMI85_50_S_mean.data - ICHECKNMI_b_S_mean.data + Obs_S.data)
    ICHECMPI85_50_S_mean = (ICHECMPI85_50_S_mean.data - ICHECMPI_b_S_mean.data + Obs_S.data)
    ICHECSMHI85_50_S_mean = (ICHECSMHI85_50_S_mean.data - ICHECSMHI_b_S_mean.data + Obs_S.data)  
    
    
    #-------------------------------------------------------------------------
    #PART 6: PRINT DATA
    import csv
    with open('output_DailyTasMINdata_b.csv', 'wb') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        
        writer.writerow(['Parameter', 'Means'])
        
    #PART 6A: WRITE NORTHERN DATA
        writer.writerow(["ICHECDMI_past_N_mean"] +ICHECDMI_past_N_mean.data.flatten().astype(np.str).tolist())       
        writer.writerow(["ICHECCCLM_past_N_mean"] +ICHECCCLM_past_N_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["ICHECKNMI_past_N_mean"] +ICHECKNMI_past_N_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["ICHECMPI_past_N_mean"] +ICHECMPI_past_N_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["ICHECSMHI_past_N_mean"] +ICHECSMHI_past_N_mean.data.flatten().astype(np.str).tolist())
        
        writer.writerow(["ICHECDMI_30_N_mean"] +ICHECDMI_30_N_mean.data.flatten().astype(np.str).tolist())       
        writer.writerow(["ICHECCCLM_30_N_mean"] +ICHECCCLM_30_N_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["ICHECKNMI_30_N_mean"] +ICHECKNMI_30_N_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["ICHECMPI_30_N_mean"] +ICHECMPI_30_N_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["ICHECSMHI_30_N_mean"] +ICHECSMHI_30_N_mean.data.flatten().astype(np.str).tolist()) 
          
        writer.writerow(["ICHECDMI85_30_N_mean"] +ICHECDMI85_30_N_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["ICHECCCLM85_30_N_mean"] +ICHECCCLM85_30_N_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["ICHECKNMI85_30_N_mean"] +ICHECKNMI85_30_N_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["ICHECMPI85_30_N_mean"] +ICHECMPI85_30_N_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["ICHECSMHI85_30_N_mean"] +ICHECSMHI85_30_N_mean.data.flatten().astype(np.str).tolist())
              
        writer.writerow(["ICHECDMI_50_N_mean"] +ICHECDMI_50_N_mean.data.flatten().astype(np.str).tolist())       
        writer.writerow(["ICHECCCLM_50_N_mean"] +ICHECCCLM_50_N_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["ICHECKNMI_50_N_mean"] +ICHECKNMI_50_N_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["ICHECMPI_50_N_mean"] +ICHECMPI_50_N_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["ICHECSMHI_50_N_mean"] +ICHECSMHI_50_N_mean.data.flatten().astype(np.str).tolist()) 
        
        writer.writerow(["ICHECDMI85_50_N_mean"] +ICHECDMI85_50_N_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["ICHECCCLM85_50_N_mean"] +ICHECCCLM85_50_N_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["ICHECKNMI85_50_N_mean"] +ICHECKNMI85_50_N_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["ICHECMPI85_50_N_mean"] +ICHECMPI85_50_N_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["ICHECSMHI85_50_N_mean"] +ICHECSMHI85_50_N_mean.data.flatten().astype(np.str).tolist())
        
    #PART 6B: WRITE CENTRAL DATA  
        writer.writerow(["ICHECDMI_past_C_mean"] +ICHECDMI_past_C_mean.data.flatten().astype(np.str).tolist())       
        writer.writerow(["ICHECCCLM_past_C_mean"] +ICHECCCLM_past_C_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["ICHECKNMI_past_C_mean"] +ICHECKNMI_past_C_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["ICHECMPI_past_C_mean"] +ICHECMPI_past_C_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["ICHECSMHI_past_C_mean"] +ICHECSMHI_past_C_mean.data.flatten().astype(np.str).tolist())
         
        writer.writerow(["ICHECDMI_30_C_mean"] +ICHECDMI_30_C_mean.data.flatten().astype(np.str).tolist())       
        writer.writerow(["ICHECCCLM_30_C_mean"] +ICHECCCLM_30_C_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["ICHECKNMI_30_C_mean"] +ICHECKNMI_30_C_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["ICHECMPI_30_C_mean"] +ICHECMPI_30_C_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["ICHECSMHI_30_C_mean"] +ICHECSMHI_30_C_mean.data.flatten().astype(np.str).tolist()) 
          
        writer.writerow(["ICHECDMI85_30_C_mean"] +ICHECDMI85_30_C_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["ICHECCCLM85_30_C_mean"] +ICHECCCLM85_30_C_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["ICHECKNMI85_30_C_mean"] +ICHECKNMI85_30_C_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["ICHECMPI85_30_C_mean"] +ICHECMPI85_30_C_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["ICHECSMHI85_30_C_mean"] +ICHECSMHI85_30_C_mean.data.flatten().astype(np.str).tolist())
              
        writer.writerow(["ICHECDMI_50_C_mean"] +ICHECDMI_50_C_mean.data.flatten().astype(np.str).tolist())       
        writer.writerow(["ICHECCCLM_50_C_mean"] +ICHECCCLM_50_C_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["ICHECKNMI_50_C_mean"] +ICHECKNMI_50_C_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["ICHECMPI_50_C_mean"] +ICHECMPI_50_C_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["ICHECSMHI_50_C_mean"] +ICHECSMHI_50_C_mean.data.flatten().astype(np.str).tolist()) 
          
        writer.writerow(["ICHECDMI85_50_C_mean"] +ICHECDMI85_50_C_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["ICHECCCLM85_50_C_mean"] +ICHECCCLM85_50_C_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["ICHECKNMI85_50_C_mean"] +ICHECKNMI85_50_C_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["ICHECMPI85_50_C_mean"] +ICHECMPI85_50_C_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["ICHECSMHI85_50_C_mean"] +ICHECSMHI85_50_C_mean.data.flatten().astype(np.str).tolist())
        
    #PART 6C: WRITE SOUTHERN DATA 
        writer.writerow(["ICHECDMI_past_S_mean"] +ICHECDMI_past_S_mean.data.flatten().astype(np.str).tolist())       
        writer.writerow(["ICHECCCLM_past_S_mean"] +ICHECCCLM_past_S_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["ICHECKNMI_past_S_mean"] +ICHECKNMI_past_S_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["ICHECMPI_past_S_mean"] +ICHECMPI_past_S_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["ICHECSMHI_past_S_mean"] +ICHECSMHI_past_S_mean.data.flatten().astype(np.str).tolist())
        
        writer.writerow(["ICHECDMI_30_S_mean"] +ICHECDMI_30_S_mean.data.flatten().astype(np.str).tolist())       
        writer.writerow(["ICHECCCLM_30_S_mean"] +ICHECCCLM_30_S_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["ICHECKNMI_30_S_mean"] +ICHECKNMI_30_S_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["ICHECMPI_30_S_mean"] +ICHECMPI_30_S_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["ICHECSMHI_30_S_mean"] +ICHECSMHI_30_S_mean.data.flatten().astype(np.str).tolist()) 
         
        writer.writerow(["ICHECDMI85_30_S_mean"] +ICHECDMI85_30_S_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["ICHECCCLM85_30_S_mean"] +ICHECCCLM85_30_S_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["ICHECKNMI85_30_S_mean"] +ICHECKNMI85_30_S_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["ICHECMPI85_30_S_mean"] +ICHECMPI85_30_S_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["ICHECSMHI85_30_S_mean"] +ICHECSMHI85_30_S_mean.data.flatten().astype(np.str).tolist())
          
        writer.writerow(["ICHECDMI_50_S_mean"] +ICHECDMI_50_S_mean.data.flatten().astype(np.str).tolist())       
        writer.writerow(["ICHECCCLM_50_S_mean"] +ICHECCCLM_50_S_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["ICHECKNMI_50_S_mean"] +ICHECKNMI_50_S_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["ICHECMPI_50_S_mean"] +ICHECMPI_50_S_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["ICHECSMHI_50_S_mean"] +ICHECSMHI_50_S_mean.data.flatten().astype(np.str).tolist()) 
        
        writer.writerow(["ICHECDMI85_50_S_mean"] +ICHECDMI85_50_S_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["ICHECCCLM85_50_S_mean"] +ICHECCCLM85_50_S_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["ICHECKNMI85_50_S_mean"] +ICHECKNMI85_50_S_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["ICHECMPI85_50_S_mean"] +ICHECMPI85_50_S_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["ICHECSMHI85_50_S_mean"] +ICHECSMHI85_50_S_mean.data.flatten().astype(np.str).tolist())   
        

if __name__ == '__main__':
    main()
        
        