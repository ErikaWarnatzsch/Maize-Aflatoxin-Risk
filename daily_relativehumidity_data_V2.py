"""
Created on Monday July 1st 2019

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
    #PART 3: Format Data General
    #PART 4: Format Data to be Geographically Specific 
    #PART 5: print data

def main():
    #PART 1: LOAD and FORMAT PROJECTED MODELS 
    CCCmaSMHI_past = '/exports/csce/datastore/geos/users/s0899345/AFR_44_hurs/hurs_AFR-44_CCCma-CanESM2_historical_r1i1p1_SMHI-RCA4_v1_day_19710101-20001231.nc'
    CNRMSMHI_past = '/exports/csce/datastore/geos/users/s0899345/AFR_44_hurs/hurs_AFR-44_CNRM-CERFACS-CNRM-CM5_historical_r1i1p1_SMHI-RCA4_v1_day_19710101-20001231.nc'
    CSIRO_past = '/exports/csce/datastore/geos/users/s0899345/AFR_44_hurs/hurs_AFR-44_CSIRO-QCCCE-CSIRO-Mk3-6-0_historical_r1i1p1_SMHI-RCA4_v1_day_19710101-20001231.nc'
    ICHECDMI_past = '/exports/csce/datastore/geos/users/s0899345/AFR_44_hurs/hurs_AFR-44_ICHEC-EC-EARTH_historical_r3i1p1_DMI-HIRHAM5_v2_day_19710101-20001231.nc'       
    ICHECKNMI_past = '/exports/csce/datastore/geos/users/s0899345/AFR_44_hurs/hurs_AFR-44_ICHEC-EC-EARTH_historical_r1i1p1_KNMI-RACMO22T_v1_day_19710101-20001231.nc'
    ICHECSMHI_past = '/exports/csce/datastore/geos/users/s0899345/AFR_44_hurs/hurs_AFR-44_ICHEC-EC-EARTH_historical_r12i1p1_SMHI-RCA4_v1_day_19710101-20001231.nc'
    IPSL_past = '/exports/csce/datastore/geos/users/s0899345/AFR_44_hurs/hurs_AFR-44_IPSL-IPSL-CM5A-MR_historical_r1i1p1_SMHI-RCA4_v1_day_19710101-20001231.nc'
    MIROC_past =  '/exports/csce/datastore/geos/users/s0899345/AFR_44_hurs/hurs_AFR-44_MIROC-MIROC5_historical_r1i1p1_SMHI-RCA4_v1_day_19710101-20001231.nc' 
    MOHCKNMI_past = '/exports/csce/datastore/geos/users/s0899345/AFR_44_hurs/hurs_AFR-44_MOHC-HadGEM2-ES_historical_r1i1p1_KNMI-RACMO22T_v2_day_19710101-20001230.nc'
    MOHCSMHI_past = '/exports/csce/datastore/geos/users/s0899345/AFR_44_hurs/hurs_AFR-44_MOHC-HadGEM2-ES_historical_r1i1p1_SMHI-RCA4_v1_day_19710101-20001230.nc'
    MPISMHI_past = '/exports/csce/datastore/geos/users/s0899345/AFR_44_hurs/hurs_AFR-44_MPI-M-MPI-ESM-LR_historical_r1i1p1_SMHI-RCA4_v1_day_19710101-20001231.nc'
    NCCSMHI_past = '/exports/csce/datastore/geos/users/s0899345/AFR_44_hurs/hurs_AFR-44_NCC-NorESM1-M_historical_r1i1p1_SMHI-RCA4_v1_day_19710101-20001231.nc'   
    NOAA_past = '/exports/csce/datastore/geos/users/s0899345/AFR_44_hurs/hurs_AFR-44_NOAA-GFDL-GFDL-ESM2M_historical_r1i1p1_SMHI-RCA4_v1_day_19710101-20001231.nc'   
    
    #Load exactly one cube from given file
    CCCmaSMHI_past =  iris.load_cube(CCCmaSMHI_past)
    CNRMSMHI_past =  iris.load_cube(CNRMSMHI_past)
    CSIRO_past =  iris.load_cube(CSIRO_past)
    ICHECDMI_past =  iris.load_cube(ICHECDMI_past, 'relative_humidity')
    ICHECKNMI_past =  iris.load_cube(ICHECKNMI_past)
    ICHECSMHI_past =  iris.load_cube(ICHECSMHI_past)
    IPSL_past =  iris.load_cube(IPSL_past)
    MIROC_past =  iris.load_cube(MIROC_past)
    MOHCKNMI_past =  iris.load_cube(MOHCKNMI_past)
    MOHCSMHI_past =  iris.load_cube(MOHCSMHI_past)
    MPISMHI_past =  iris.load_cube(MPISMHI_past)
    NCCSMHI_past =  iris.load_cube(NCCSMHI_past)
    NOAA_past =  iris.load_cube(NOAA_past)
    
    #remove flat latitude and longitude and only use grid latitude and grid longitude to make consistent with the observed data, also make sure all of the longitudes are monotonic. 
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
    CCCmaSMHI_past.coord('latitude').guess_bounds()
    CNRMSMHI_past.coord('latitude').guess_bounds()
    CSIRO_past.coord('latitude').guess_bounds()
    ICHECDMI_past.coord('latitude').guess_bounds()
    ICHECKNMI_past.coord('latitude').guess_bounds()
    ICHECSMHI_past.coord('latitude').guess_bounds()
    IPSL_past.coord('latitude').guess_bounds()
    MIROC_past.coord('latitude').guess_bounds()
    MOHCKNMI_past.coord('latitude').guess_bounds() 
    MOHCSMHI_past.coord('latitude').guess_bounds()
    MPISMHI_past.coord('latitude').guess_bounds()
    NCCSMHI_past.coord('latitude').guess_bounds()
    NOAA_past.coord('latitude').guess_bounds()
    
    CCCmaSMHI_past.coord('longitude').guess_bounds()
    CNRMSMHI_past.coord('longitude').guess_bounds()
    CSIRO_past.coord('longitude').guess_bounds()
    ICHECDMI_past.coord('longitude').guess_bounds()
    ICHECKNMI_past.coord('longitude').guess_bounds()
    ICHECSMHI_past.coord('longitude').guess_bounds()
    IPSL_past.coord('longitude').guess_bounds()
    MIROC_past.coord('longitude').guess_bounds()
    MOHCKNMI_past.coord('longitude').guess_bounds() 
    MOHCSMHI_past.coord('longitude').guess_bounds()
    MPISMHI_past.coord('longitude').guess_bounds()
    NCCSMHI_past.coord('longitude').guess_bounds()
    NOAA_past.coord('longitude').guess_bounds()
    
    
    #-------------------------------------------------------------------------
    #PART 2: LOAD and FORMAT PROJECTED MODELS   
    CCCmaSMHI= '/exports/csce/datastore/geos/users/s0899345/AFR_44_hurs/hurs_AFR-44_CCCma-CanESM2_rcp45_r1i1p1_SMHI-RCA4_v1_day_20060101-20701231.nc'
    CNRMSMHI= '/exports/csce/datastore/geos/users/s0899345/AFR_44_hurs/hurs_AFR-44_CNRM-CERFACS-CNRM-CM5_rcp45_r1i1p1_SMHI-RCA4_v1_day_20060101-20701231.nc'
    CSIRO = '/exports/csce/datastore/geos/users/s0899345/AFR_44_hurs/hurs_AFR-44_CSIRO-QCCCE-CSIRO-Mk3-6-0_rcp45_r1i1p1_SMHI-RCA4_v1_day_20060101-20701231.nc'  
    ICHECDMI = '/exports/csce/datastore/geos/users/s0899345/AFR_44_hurs/hurs_AFR-44_ICHEC-EC-EARTH_rcp45_r3i1p1_DMI-HIRHAM5_v2_day_20060101-20701231.nc'       
    ICHECKNMI = '/exports/csce/datastore/geos/users/s0899345/AFR_44_hurs/hurs_AFR-44_ICHEC-EC-EARTH_rcp45_r1i1p1_KNMI-RACMO22T_v1_day_20060101-20701231.nc'
    ICHECSMHI = '/exports/csce/datastore/geos/users/s0899345/AFR_44_hurs/hurs_AFR-44_ICHEC-EC-EARTH_rcp45_r12i1p1_SMHI-RCA4_v1_day_20060101-20701231.nc'
    IPSL = '/exports/csce/datastore/geos/users/s0899345/AFR_44_hurs/hurs_AFR-44_IPSL-IPSL-CM5A-MR_rcp45_r1i1p1_SMHI-RCA4_v1_day_20060101-20701231.nc'
    MIROC =  '/exports/csce/datastore/geos/users/s0899345/AFR_44_hurs/hurs_AFR-44_MIROC-MIROC5_rcp45_r1i1p1_SMHI-RCA4_v1_day_20060101-20701231.nc' 
    MOHCKNMI = '/exports/csce/datastore/geos/users/s0899345/AFR_44_hurs/hurs_AFR-44_MOHC-HadGEM2-ES_rcp45_r1i1p1_KNMI-RACMO22T_v2_day_20060101-20701230.nc'
    MOHCSMHI = '/exports/csce/datastore/geos/users/s0899345/AFR_44_hurs/hurs_AFR-44_MOHC-HadGEM2-ES_rcp45_r1i1p1_SMHI-RCA4_v1_day_20060101-20701230.nc' 
    MPISMHI = '/exports/csce/datastore/geos/users/s0899345/AFR_44_hurs/hurs_AFR-44_MPI-M-MPI-ESM-LR_rcp45_r1i1p1_SMHI-RCA4_v1_day_20060101-20701231.nc'   
    NCCSMHI = '/exports/csce/datastore/geos/users/s0899345/AFR_44_hurs/hurs_AFR-44_NCC-NorESM1-M_rcp45_r1i1p1_SMHI-RCA4_v1_day_20060101-20701231.nc'   
    NOAA = '/exports/csce/datastore/geos/users/s0899345/AFR_44_hurs/hurs_AFR-44_NOAA-GFDL-GFDL-ESM2M_rcp45_r1i1p1_SMHI-RCA4_v1_day_20060101-20701231.nc'   
    
    CCCmaSMHI85 = '/exports/csce/datastore/geos/users/s0899345/AFR_44_hurs/hurs_AFR-44_CCCma-CanESM2_rcp85_r1i1p1_SMHI-RCA4_v1_day_20060101-20701231.nc'
    CNRMSMHI85 = '/exports/csce/datastore/geos/users/s0899345/AFR_44_hurs/hurs_AFR-44_CNRM-CERFACS-CNRM-CM5_rcp85_r1i1p1_SMHI-RCA4_v1_day_20060101-20701231.nc'
    CSIRO85 = '/exports/csce/datastore/geos/users/s0899345/AFR_44_hurs/hurs_AFR-44_CSIRO-QCCCE-CSIRO-Mk3-6-0_rcp85_r1i1p1_SMHI-RCA4_v1_day_20060101-20701231.nc'
    ICHECDMI85 = '/exports/csce/datastore/geos/users/s0899345/AFR_44_hurs/hurs_AFR-44_ICHEC-EC-EARTH_rcp85_r3i1p1_DMI-HIRHAM5_v2_day_20060101-20701231.nc'       
    ICHECKNMI85 = '/exports/csce/datastore/geos/users/s0899345/AFR_44_hurs/hurs_AFR-44_ICHEC-EC-EARTH_rcp85_r1i1p1_KNMI-RACMO22T_v1_day_20060101-20701231.nc'
    ICHECSMHI85 = '/exports/csce/datastore/geos/users/s0899345/AFR_44_hurs/hurs_AFR-44_ICHEC-EC-EARTH_rcp85_r12i1p1_SMHI-RCA4_v1_day_20060101-20701231.nc'
    IPSL85 = '/exports/csce/datastore/geos/users/s0899345/AFR_44_hurs/hurs_AFR-44_IPSL-IPSL-CM5A-MR_rcp85_r1i1p1_SMHI-RCA4_v1_day_20060101-20701231.nc'
    MIROC85 =  '/exports/csce/datastore/geos/users/s0899345/AFR_44_hurs/hurs_AFR-44_MIROC-MIROC5_rcp85_r1i1p1_SMHI-RCA4_v1_day_20060101-20701231.nc' 
    MOHCKNMI85 = '/exports/csce/datastore/geos/users/s0899345/AFR_44_hurs/hurs_AFR-44_MOHC-HadGEM2-ES_rcp85_r1i1p1_KNMI-RACMO22T_v2_day_20060101-20701230.nc'
    MOHCSMHI85 = '/exports/csce/datastore/geos/users/s0899345/AFR_44_hurs/hurs_AFR-44_MOHC-HadGEM2-ES_rcp85_r1i1p1_SMHI-RCA4_v1_day_20060101-20701230.nc'  
    MPISMHI85 = '/exports/csce/datastore/geos/users/s0899345/AFR_44_hurs/hurs_AFR-44_MPI-M-MPI-ESM-LR_rcp85_r1i1p1_SMHI-RCA4_v1_day_20060101-20701231.nc'
    NCCSMHI85 = '/exports/csce/datastore/geos/users/s0899345/AFR_44_hurs/hurs_AFR-44_NCC-NorESM1-M_rcp85_r1i1p1_SMHI-RCA4_v1_day_20060101-20701231.nc'   
    NOAA85 = '/exports/csce/datastore/geos/users/s0899345/AFR_44_hurs/hurs_AFR-44_NOAA-GFDL-GFDL-ESM2M_rcp85_r1i1p1_SMHI-RCA4_v1_day_20060101-20701231.nc'  
    
    #Load exactly one cube from given file
    CCCmaSMHI = iris.load_cube(CCCmaSMHI)
    CNRMSMHI = iris.load_cube(CNRMSMHI)
    CSIRO = iris.load_cube(CSIRO)
    ICHECDMI = iris.load_cube(ICHECDMI, 'relative_humidity')
    ICHECKNMI = iris.load_cube(ICHECKNMI)
    ICHECSMHI = iris.load_cube(ICHECSMHI)
    IPSL = iris.load_cube(IPSL)
    MIROC = iris.load_cube(MIROC)
    MOHCKNMI = iris.load_cube(MOHCKNMI)
    MOHCSMHI = iris.load_cube(MOHCSMHI)
    MPISMHI = iris.load_cube(MPISMHI)
    NCCSMHI = iris.load_cube(NCCSMHI)
    NOAA = iris.load_cube(NOAA)
    
    CCCmaSMHI85 = iris.load_cube(CCCmaSMHI85)
    CNRMSMHI85 = iris.load_cube(CNRMSMHI85)
    CSIRO85 = iris.load_cube(CSIRO85)
    ICHECDMI85 = iris.load_cube(ICHECDMI85, 'relative_humidity')
    ICHECKNMI85 = iris.load_cube(ICHECKNMI85)
    ICHECSMHI85 = iris.load_cube(ICHECSMHI85)
    IPSL85 = iris.load_cube(IPSL85)
    MIROC85 = iris.load_cube(MIROC85)
    MOHCKNMI85 = iris.load_cube(MOHCKNMI85)
    MOHCSMHI85 = iris.load_cube(MOHCSMHI85)
    MPISMHI85 = iris.load_cube(MPISMHI85)
    NCCSMHI85 = iris.load_cube(NCCSMHI85)
    NOAA85 = iris.load_cube(NOAA85)
    
    #remove flat latitude and longitude and only use grid latitude and grid longitude to make consistent with the observed data, also make sure all of the longitudes are monotonic. 
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
    CCCmaSMHI.coord('latitude').guess_bounds()
    CNRMSMHI.coord('latitude').guess_bounds()
    CSIRO.coord('latitude').guess_bounds()
    ICHECDMI.coord('latitude').guess_bounds()
    ICHECKNMI.coord('latitude').guess_bounds()
    ICHECSMHI.coord('latitude').guess_bounds()
    IPSL.coord('latitude').guess_bounds()
    MIROC.coord('latitude').guess_bounds()
    MOHCKNMI.coord('latitude').guess_bounds() 
    MOHCSMHI.coord('latitude').guess_bounds()
    MPISMHI.coord('latitude').guess_bounds()
    NCCSMHI.coord('latitude').guess_bounds()
    NOAA.coord('latitude').guess_bounds()
    
    CCCmaSMHI85.coord('latitude').guess_bounds()
    CNRMSMHI85.coord('latitude').guess_bounds()
    CSIRO85.coord('latitude').guess_bounds()
    ICHECDMI85.coord('latitude').guess_bounds()
    ICHECKNMI85.coord('latitude').guess_bounds()
    ICHECSMHI85.coord('latitude').guess_bounds()
    IPSL85.coord('latitude').guess_bounds()
    MIROC85.coord('latitude').guess_bounds()
    MOHCKNMI85.coord('latitude').guess_bounds() 
    MOHCSMHI85.coord('latitude').guess_bounds()
    MPISMHI85.coord('latitude').guess_bounds()
    NCCSMHI85.coord('latitude').guess_bounds()
    NOAA85.coord('latitude').guess_bounds()
    
    CCCmaSMHI.coord('longitude').guess_bounds()
    CNRMSMHI.coord('longitude').guess_bounds()
    CSIRO.coord('longitude').guess_bounds()
    ICHECDMI.coord('longitude').guess_bounds()
    ICHECKNMI.coord('longitude').guess_bounds()
    ICHECSMHI.coord('longitude').guess_bounds()
    IPSL.coord('longitude').guess_bounds()
    MIROC.coord('longitude').guess_bounds()
    MOHCKNMI.coord('longitude').guess_bounds() 
    MOHCSMHI.coord('longitude').guess_bounds()
    MPISMHI.coord('longitude').guess_bounds()
    NCCSMHI.coord('longitude').guess_bounds()
    NOAA.coord('longitude').guess_bounds()
    
    CCCmaSMHI85.coord('longitude').guess_bounds()
    CNRMSMHI85.coord('longitude').guess_bounds()
    CSIRO85.coord('longitude').guess_bounds()
    ICHECDMI85.coord('longitude').guess_bounds()
    ICHECKNMI85.coord('longitude').guess_bounds()
    ICHECSMHI85.coord('longitude').guess_bounds()
    IPSL85.coord('longitude').guess_bounds()
    MIROC85.coord('longitude').guess_bounds()
    MOHCKNMI85.coord('longitude').guess_bounds() 
    MOHCSMHI85.coord('longitude').guess_bounds()
    MPISMHI85.coord('longitude').guess_bounds()
    NCCSMHI85.coord('longitude').guess_bounds()
    NOAA85.coord('longitude').guess_bounds()
    
    
    #-------------------------------------------------------------------------
    #PART 3: FORMAT DATA GENERAL
    #limit time series of data
    #time constraint to make past and obsered data only from 1971-2000 
    iris.FUTURE.cell_datetime_objects = True
    t_constraint_past = iris.Constraint(time=lambda cell: 1971 <= cell.point.year <= 2000)
    
    CCCmaSMHI_past =  CCCmaSMHI_past.extract(t_constraint_past)
    CNRMSMHI_past =  CNRMSMHI_past.extract(t_constraint_past)
    CSIRO_past =  CSIRO_past.extract(t_constraint_past)
    ICHECDMI_past =  ICHECDMI_past.extract(t_constraint_past)
    ICHECKNMI_past =  ICHECKNMI_past.extract(t_constraint_past)
    ICHECSMHI_past =  ICHECSMHI_past.extract(t_constraint_past)
    IPSL_past =  IPSL_past.extract(t_constraint_past)
    MIROC_past =  MIROC_past.extract(t_constraint_past)
    MOHCKNMI_past =  MOHCKNMI_past.extract(t_constraint_past)
    MOHCSMHI_past =  MOHCSMHI_past.extract(t_constraint_past)
    MPISMHI_past =  MPISMHI_past.extract(t_constraint_past)
    NCCSMHI_past =  NCCSMHI_past.extract(t_constraint_past)
    NOAA_past =  NOAA_past.extract(t_constraint_past)
    
    #time constraint to make future data only from 2020-2049
    iris.FUTURE.cell_datetime_objects = True
    t_constraint_future = iris.Constraint(time=lambda cell: 2020 <= cell.point.year <= 2049)
    
    CCCmaSMHI_30 = CCCmaSMHI.extract(t_constraint_future)
    CNRMSMHI_30 = CNRMSMHI.extract(t_constraint_future)
    CSIRO_30 = CSIRO.extract(t_constraint_future)
    ICHECDMI_30 = ICHECDMI.extract(t_constraint_future)
    ICHECKNMI_30 = ICHECKNMI.extract(t_constraint_future)
    ICHECSMHI_30 = ICHECSMHI.extract(t_constraint_future)
    IPSL_30 = IPSL.extract(t_constraint_future)
    MIROC_30 = MIROC.extract(t_constraint_future)
    MOHCKNMI_30 = MOHCKNMI.extract(t_constraint_future)
    MOHCSMHI_30 = MOHCSMHI.extract(t_constraint_future)
    MPISMHI_30 = MPISMHI.extract(t_constraint_future)
    NCCSMHI_30 = NCCSMHI.extract(t_constraint_future)
    NOAA_30 = NOAA.extract(t_constraint_future) 
    
    CCCmaSMHI85_30 = CCCmaSMHI85.extract(t_constraint_future)
    CNRMSMHI85_30 = CNRMSMHI85.extract(t_constraint_future)
    CSIRO85_30 = CSIRO85.extract(t_constraint_future)
    ICHECDMI85_30 = ICHECDMI85.extract(t_constraint_future)
    ICHECKNMI85_30 = ICHECKNMI85.extract(t_constraint_future)
    ICHECSMHI85_30 = ICHECSMHI85.extract(t_constraint_future)
    IPSL85_30 = IPSL85.extract(t_constraint_future)
    MIROC85_30 = MIROC85.extract(t_constraint_future)
    MOHCKNMI85_30 = MOHCKNMI85.extract(t_constraint_future)
    MOHCSMHI85_30 = MOHCSMHI85.extract(t_constraint_future)
    MPISMHI85_30 = MPISMHI85.extract(t_constraint_future)
    NCCSMHI85_30 = NCCSMHI85.extract(t_constraint_future)
    NOAA85_30 = NOAA85.extract(t_constraint_future) 
    
    #time constraint to make future data only from 2040-2069
    iris.FUTURE.cell_datetime_objects = True
    t_constraint_future = iris.Constraint(time=lambda cell: 2040 <= cell.point.year <= 2069)
    
    CCCmaSMHI_50 = CCCmaSMHI.extract(t_constraint_future)
    CNRMSMHI_50 = CNRMSMHI.extract(t_constraint_future)
    CSIRO_50 = CSIRO.extract(t_constraint_future)
    ICHECDMI_50 = ICHECDMI.extract(t_constraint_future)
    ICHECKNMI_50 = ICHECKNMI.extract(t_constraint_future)
    ICHECSMHI_50 = ICHECSMHI.extract(t_constraint_future)
    IPSL_50 = IPSL.extract(t_constraint_future)
    MIROC_50 = MIROC.extract(t_constraint_future)
    MOHCKNMI_50 = MOHCKNMI.extract(t_constraint_future)
    MOHCSMHI_50 = MOHCSMHI.extract(t_constraint_future)
    MPISMHI_50 = MPISMHI.extract(t_constraint_future)
    NCCSMHI_50 = NCCSMHI.extract(t_constraint_future)
    NOAA_50 = NOAA.extract(t_constraint_future) 
    
    CCCmaSMHI85_50 = CCCmaSMHI85.extract(t_constraint_future)
    CNRMSMHI85_50 = CNRMSMHI85.extract(t_constraint_future)
    CSIRO85_50 = CSIRO85.extract(t_constraint_future)
    ICHECDMI85_50 = ICHECDMI85.extract(t_constraint_future)
    ICHECKNMI85_50 = ICHECKNMI85.extract(t_constraint_future)
    ICHECSMHI85_50 = ICHECSMHI85.extract(t_constraint_future)
    IPSL85_50 = IPSL85.extract(t_constraint_future)
    MIROC85_50 = MIROC85.extract(t_constraint_future)
    MOHCKNMI85_50 = MOHCKNMI85.extract(t_constraint_future)
    MOHCSMHI85_50 = MOHCSMHI85.extract(t_constraint_future)
    MPISMHI85_50 = MPISMHI85.extract(t_constraint_future)
    NCCSMHI85_50 = NCCSMHI85.extract(t_constraint_future)
    NOAA85_50 = NOAA85.extract(t_constraint_future) 
    
    
    #-------------------------------------------------------------------------
    #PART 4: FORMAT DATA TO GEOGRAPHICALLY SPECIFIC 
    #PART 4A: NORTHERN MALAWI
    #we are only interested in the latitude and longitude relevant to Central Malawi 
    Northern_Malawi = iris.Constraint(longitude=lambda v: 32.5 <= v <= 35, latitude=lambda v: -12.5 <= v <= -8.5) 
    
    CCCmaSMHI_past_N = CCCmaSMHI_past.extract(Northern_Malawi)
    CNRMSMHI_past_N = CNRMSMHI_past.extract(Northern_Malawi)
    CSIRO_past_N = CSIRO_past.extract(Northern_Malawi)
    ICHECDMI_past_N = ICHECDMI_past.extract(Northern_Malawi)
    ICHECKNMI_past_N = ICHECKNMI_past.extract(Northern_Malawi)
    ICHECSMHI_past_N = ICHECSMHI_past.extract(Northern_Malawi)
    IPSL_past_N = IPSL_past.extract(Northern_Malawi)
    MIROC_past_N = MIROC_past.extract(Northern_Malawi)
    MOHCKNMI_past_N = MOHCKNMI_past.extract(Northern_Malawi)
    MOHCSMHI_past_N = MOHCSMHI_past.extract(Northern_Malawi)
    MPISMHI_past_N = MPISMHI_past.extract(Northern_Malawi)
    NCCSMHI_past_N = NCCSMHI_past.extract(Northern_Malawi)
    NOAA_past_N = NOAA_past.extract(Northern_Malawi)
    
    CCCmaSMHI_30_N = CCCmaSMHI_30.extract(Northern_Malawi)
    CNRMSMHI_30_N = CNRMSMHI_30.extract(Northern_Malawi)
    CSIRO_30_N = CSIRO_30.extract(Northern_Malawi)
    ICHECDMI_30_N = ICHECDMI_30.extract(Northern_Malawi)
    ICHECKNMI_30_N = ICHECKNMI_30.extract(Northern_Malawi)
    ICHECSMHI_30_N = ICHECSMHI_30.extract(Northern_Malawi)
    IPSL_30_N = IPSL_30.extract(Northern_Malawi)
    MIROC_30_N = MIROC_30.extract(Northern_Malawi)
    MOHCKNMI_30_N = MOHCKNMI_30.extract(Northern_Malawi)
    MOHCSMHI_30_N = MOHCSMHI_30.extract(Northern_Malawi)
    MPISMHI_30_N = MPISMHI_30.extract(Northern_Malawi)
    NCCSMHI_30_N = NCCSMHI_30.extract(Northern_Malawi)
    NOAA_30_N = NOAA_30.extract(Northern_Malawi)
    
    CCCmaSMHI85_30_N = CCCmaSMHI85_30.extract(Northern_Malawi)
    CNRMSMHI85_30_N = CNRMSMHI85_30.extract(Northern_Malawi)
    CSIRO85_30_N = CSIRO85_30.extract(Northern_Malawi)
    ICHECDMI85_30_N = ICHECDMI85_30.extract(Northern_Malawi)
    ICHECKNMI85_30_N = ICHECKNMI85_30.extract(Northern_Malawi)
    ICHECSMHI85_30_N = ICHECSMHI85_30.extract(Northern_Malawi)
    IPSL85_30_N = IPSL85_30.extract(Northern_Malawi)
    MIROC85_30_N = MIROC85_30.extract(Northern_Malawi)
    MOHCKNMI85_30_N = MOHCKNMI85_30.extract(Northern_Malawi)
    MOHCSMHI85_30_N = MOHCSMHI85_30.extract(Northern_Malawi)
    MPISMHI85_30_N = MPISMHI85_30.extract(Northern_Malawi)
    NCCSMHI85_30_N = NCCSMHI85_30.extract(Northern_Malawi)
    NOAA85_30_N = NOAA85_30.extract(Northern_Malawi)
    
    CCCmaSMHI_50_N = CCCmaSMHI_50.extract(Northern_Malawi)
    CNRMSMHI_50_N = CNRMSMHI_50.extract(Northern_Malawi)
    CSIRO_50_N = CSIRO_50.extract(Northern_Malawi)
    ICHECDMI_50_N = ICHECDMI_50.extract(Northern_Malawi)
    ICHECKNMI_50_N = ICHECKNMI_50.extract(Northern_Malawi)
    ICHECSMHI_50_N = ICHECSMHI_50.extract(Northern_Malawi)
    IPSL_50_N = IPSL_50.extract(Northern_Malawi)
    MIROC_50_N = MIROC_50.extract(Northern_Malawi)
    MOHCKNMI_50_N = MOHCKNMI_50.extract(Northern_Malawi)
    MOHCSMHI_50_N = MOHCSMHI_50.extract(Northern_Malawi)
    MPISMHI_50_N = MPISMHI_50.extract(Northern_Malawi)
    NCCSMHI_50_N = NCCSMHI_50.extract(Northern_Malawi)
    NOAA_50_N = NOAA_50.extract(Northern_Malawi)
    
    CCCmaSMHI85_50_N = CCCmaSMHI85_50.extract(Northern_Malawi)
    CNRMSMHI85_50_N = CNRMSMHI85_50.extract(Northern_Malawi)
    CSIRO85_50_N = CSIRO85_50.extract(Northern_Malawi)
    ICHECDMI85_50_N = ICHECDMI85_50.extract(Northern_Malawi)
    ICHECKNMI85_50_N = ICHECKNMI85_50.extract(Northern_Malawi)
    ICHECSMHI85_50_N = ICHECSMHI85_50.extract(Northern_Malawi)
    IPSL85_50_N = IPSL85_50.extract(Northern_Malawi)
    MIROC85_50_N = MIROC85_50.extract(Northern_Malawi)
    MOHCKNMI85_50_N = MOHCKNMI85_50.extract(Northern_Malawi)
    MOHCSMHI85_50_N = MOHCSMHI85_50.extract(Northern_Malawi)
    MPISMHI85_50_N = MPISMHI85_50.extract(Northern_Malawi)
    NCCSMHI85_50_N = NCCSMHI85_50.extract(Northern_Malawi)
    NOAA85_50_N = NOAA85_50.extract(Northern_Malawi)
    
    #Returns an array of area weights, with the same dimensions as the cube
    CCCmaSMHI_past_N_grid_areas = iris.analysis.cartography.area_weights(CCCmaSMHI_past_N)
    CNRMSMHI_past_N_grid_areas = iris.analysis.cartography.area_weights(CNRMSMHI_past_N)
    CSIRO_past_N_grid_areas = iris.analysis.cartography.area_weights(CSIRO_past_N)
    ICHECDMI_past_N_grid_areas = iris.analysis.cartography.area_weights(ICHECDMI_past_N)
    ICHECKNMI_past_N_grid_areas = iris.analysis.cartography.area_weights(ICHECKNMI_past_N)
    ICHECSMHI_past_N_grid_areas = iris.analysis.cartography.area_weights(ICHECSMHI_past_N)
    IPSL_past_N_grid_areas = iris.analysis.cartography.area_weights(IPSL_past_N)
    MIROC_past_N_grid_areas = iris.analysis.cartography.area_weights(MIROC_past_N)
    MOHCKNMI_past_N_grid_areas = iris.analysis.cartography.area_weights(MOHCKNMI_past_N)
    MOHCSMHI_past_N_grid_areas = iris.analysis.cartography.area_weights(MOHCSMHI_past_N)
    MPISMHI_past_N_grid_areas = iris.analysis.cartography.area_weights(MPISMHI_past_N)
    NCCSMHI_past_N_grid_areas = iris.analysis.cartography.area_weights(NCCSMHI_past_N)
    NOAA_past_N_grid_areas = iris.analysis.cartography.area_weights(NOAA_past_N)
    
    CCCmaSMHI_30_N_grid_areas = iris.analysis.cartography.area_weights(CCCmaSMHI_30_N)
    CNRMSMHI_30_N_grid_areas = iris.analysis.cartography.area_weights(CNRMSMHI_30_N)
    CSIRO_30_N_grid_areas = iris.analysis.cartography.area_weights(CSIRO_30_N)
    ICHECDMI_30_N_grid_areas = iris.analysis.cartography.area_weights(ICHECDMI_30_N)
    ICHECKNMI_30_N_grid_areas = iris.analysis.cartography.area_weights(ICHECKNMI_30_N)
    ICHECSMHI_30_N_grid_areas = iris.analysis.cartography.area_weights(ICHECSMHI_30_N)
    IPSL_30_N_grid_areas = iris.analysis.cartography.area_weights(IPSL_30_N)
    MIROC_30_N_grid_areas = iris.analysis.cartography.area_weights(MIROC_30_N)
    MOHCKNMI_30_N_grid_areas = iris.analysis.cartography.area_weights(MOHCKNMI_30_N)
    MOHCSMHI_30_N_grid_areas = iris.analysis.cartography.area_weights(MOHCSMHI_30_N)
    MPISMHI_30_N_grid_areas = iris.analysis.cartography.area_weights(MPISMHI_30_N)
    NCCSMHI_30_N_grid_areas = iris.analysis.cartography.area_weights(NCCSMHI_30_N)
    NOAA_30_N_grid_areas = iris.analysis.cartography.area_weights(NOAA_30_N)
    
    CCCmaSMHI85_30_N_grid_areas = iris.analysis.cartography.area_weights(CCCmaSMHI85_30_N)
    CNRMSMHI85_30_N_grid_areas = iris.analysis.cartography.area_weights(CNRMSMHI85_30_N)
    CSIRO85_30_N_grid_areas = iris.analysis.cartography.area_weights(CSIRO85_30_N)
    ICHECDMI85_30_N_grid_areas = iris.analysis.cartography.area_weights(ICHECDMI85_30_N)
    ICHECKNMI85_30_N_grid_areas = iris.analysis.cartography.area_weights(ICHECKNMI85_30_N)
    ICHECSMHI85_30_N_grid_areas = iris.analysis.cartography.area_weights(ICHECSMHI85_30_N)
    IPSL85_30_N_grid_areas = iris.analysis.cartography.area_weights(IPSL85_30_N)
    MIROC85_30_N_grid_areas = iris.analysis.cartography.area_weights(MIROC85_30_N)
    MOHCKNMI85_30_N_grid_areas = iris.analysis.cartography.area_weights(MOHCKNMI85_30_N)
    MOHCSMHI85_30_N_grid_areas = iris.analysis.cartography.area_weights(MOHCSMHI85_30_N)
    MPISMHI85_30_N_grid_areas = iris.analysis.cartography.area_weights(MPISMHI85_30_N)
    NCCSMHI85_30_N_grid_areas = iris.analysis.cartography.area_weights(NCCSMHI85_30_N)
    NOAA85_30_N_grid_areas = iris.analysis.cartography.area_weights(NOAA85_30_N)
    
    CCCmaSMHI_50_N_grid_areas = iris.analysis.cartography.area_weights(CCCmaSMHI_50_N)
    CNRMSMHI_50_N_grid_areas = iris.analysis.cartography.area_weights(CNRMSMHI_50_N)
    CSIRO_50_N_grid_areas = iris.analysis.cartography.area_weights(CSIRO_50_N)
    ICHECDMI_50_N_grid_areas = iris.analysis.cartography.area_weights(ICHECDMI_50_N)
    ICHECKNMI_50_N_grid_areas = iris.analysis.cartography.area_weights(ICHECKNMI_50_N)
    ICHECSMHI_50_N_grid_areas = iris.analysis.cartography.area_weights(ICHECSMHI_50_N)
    IPSL_50_N_grid_areas = iris.analysis.cartography.area_weights(IPSL_50_N)
    MIROC_50_N_grid_areas = iris.analysis.cartography.area_weights(MIROC_50_N)
    MOHCKNMI_50_N_grid_areas = iris.analysis.cartography.area_weights(MOHCKNMI_50_N)
    MOHCSMHI_50_N_grid_areas = iris.analysis.cartography.area_weights(MOHCSMHI_50_N)
    MPISMHI_50_N_grid_areas = iris.analysis.cartography.area_weights(MPISMHI_50_N)
    NCCSMHI_50_N_grid_areas = iris.analysis.cartography.area_weights(NCCSMHI_50_N)
    NOAA_50_N_grid_areas = iris.analysis.cartography.area_weights(NOAA_50_N)
    
    CCCmaSMHI85_50_N_grid_areas = iris.analysis.cartography.area_weights(CCCmaSMHI85_50_N)
    CNRMSMHI85_50_N_grid_areas = iris.analysis.cartography.area_weights(CNRMSMHI85_50_N)
    CSIRO85_50_N_grid_areas = iris.analysis.cartography.area_weights(CSIRO85_50_N)
    ICHECDMI85_50_N_grid_areas = iris.analysis.cartography.area_weights(ICHECDMI85_50_N)
    ICHECKNMI85_50_N_grid_areas = iris.analysis.cartography.area_weights(ICHECKNMI85_50_N)
    ICHECSMHI85_50_N_grid_areas = iris.analysis.cartography.area_weights(ICHECSMHI85_50_N)
    IPSL85_50_N_grid_areas = iris.analysis.cartography.area_weights(IPSL85_50_N)
    MIROC85_50_N_grid_areas = iris.analysis.cartography.area_weights(MIROC85_50_N)
    MOHCKNMI85_50_N_grid_areas = iris.analysis.cartography.area_weights(MOHCKNMI85_50_N)
    MOHCSMHI85_50_N_grid_areas = iris.analysis.cartography.area_weights(MOHCSMHI85_50_N)
    MPISMHI85_50_N_grid_areas = iris.analysis.cartography.area_weights(MPISMHI85_50_N)
    NCCSMHI85_50_N_grid_areas = iris.analysis.cartography.area_weights(NCCSMHI85_50_N)
    NOAA85_50_N_grid_areas = iris.analysis.cartography.area_weights(NOAA85_50_N)

    #We want to plot the mean for the whole region so we need a mean of all the lats and lons
    CCCmaSMHI_past_N_mean = CCCmaSMHI_past_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CCCmaSMHI_past_N_grid_areas) 
    CNRMSMHI_past_N_mean = CNRMSMHI_past_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CNRMSMHI_past_N_grid_areas)  
    CSIRO_past_N_mean = CSIRO_past_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CSIRO_past_N_grid_areas)
    ICHECDMI_past_N_mean = ICHECDMI_past_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECDMI_past_N_grid_areas) 
    ICHECKNMI_past_N_mean = ICHECKNMI_past_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECKNMI_past_N_grid_areas)
    ICHECSMHI_past_N_mean = ICHECSMHI_past_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECSMHI_past_N_grid_areas)
    IPSL_past_N_mean = IPSL_past_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=IPSL_past_N_grid_areas)
    MIROC_past_N_mean = MIROC_past_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MIROC_past_N_grid_areas)
    MOHCKNMI_past_N_mean = MOHCKNMI_past_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCKNMI_past_N_grid_areas)
    MOHCSMHI_past_N_mean = MOHCSMHI_past_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCSMHI_past_N_grid_areas)
    MPISMHI_past_N_mean = MPISMHI_past_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MPISMHI_past_N_grid_areas)
    NCCSMHI_past_N_mean = NCCSMHI_past_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=NCCSMHI_past_N_grid_areas) 
    NOAA_past_N_mean = NOAA_past_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=NOAA_past_N_grid_areas)
    
    CCCmaSMHI_30_N_mean = CCCmaSMHI_30_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CCCmaSMHI_30_N_grid_areas) 
    CNRMSMHI_30_N_mean = CNRMSMHI_30_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CNRMSMHI_30_N_grid_areas)  
    CSIRO_30_N_mean = CSIRO_30_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CSIRO_30_N_grid_areas)
    ICHECDMI_30_N_mean = ICHECDMI_30_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECDMI_30_N_grid_areas) 
    ICHECKNMI_30_N_mean = ICHECKNMI_30_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECKNMI_30_N_grid_areas)
    ICHECSMHI_30_N_mean = ICHECSMHI_30_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECSMHI_30_N_grid_areas)
    IPSL_30_N_mean = IPSL_30_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=IPSL_30_N_grid_areas)
    MIROC_30_N_mean = MIROC_30_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MIROC_30_N_grid_areas)
    MOHCKNMI_30_N_mean = MOHCKNMI_30_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCKNMI_30_N_grid_areas)
    MOHCSMHI_30_N_mean = MOHCSMHI_30_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCSMHI_30_N_grid_areas)
    MPISMHI_30_N_mean = MPISMHI_30_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MPISMHI_30_N_grid_areas)
    NCCSMHI_30_N_mean = NCCSMHI_30_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=NCCSMHI_30_N_grid_areas) 
    NOAA_30_N_mean = NOAA_30_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=NOAA_30_N_grid_areas)
    
    CCCmaSMHI85_30_N_mean = CCCmaSMHI85_30_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CCCmaSMHI85_30_N_grid_areas) 
    CNRMSMHI85_30_N_mean = CNRMSMHI85_30_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CNRMSMHI85_30_N_grid_areas)  
    CSIRO85_30_N_mean = CSIRO85_30_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CSIRO85_30_N_grid_areas)
    ICHECDMI85_30_N_mean = ICHECDMI85_30_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECDMI85_30_N_grid_areas) 
    ICHECKNMI85_30_N_mean = ICHECKNMI85_30_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECKNMI85_30_N_grid_areas)
    ICHECSMHI85_30_N_mean = ICHECSMHI85_30_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECSMHI85_30_N_grid_areas)
    IPSL85_30_N_mean = IPSL85_30_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=IPSL85_30_N_grid_areas)
    MIROC85_30_N_mean = MIROC85_30_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MIROC85_30_N_grid_areas)
    MOHCKNMI85_30_N_mean = MOHCKNMI85_30_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCKNMI85_30_N_grid_areas)
    MOHCSMHI85_30_N_mean = MOHCSMHI85_30_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCSMHI85_30_N_grid_areas)
    MPISMHI85_30_N_mean = MPISMHI85_30_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MPISMHI85_30_N_grid_areas)
    NCCSMHI85_30_N_mean = NCCSMHI85_30_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=NCCSMHI85_30_N_grid_areas) 
    NOAA85_30_N_mean = NOAA85_30_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=NOAA85_30_N_grid_areas)
    
    CCCmaSMHI_50_N_mean = CCCmaSMHI_50_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CCCmaSMHI_50_N_grid_areas) 
    CNRMSMHI_50_N_mean = CNRMSMHI_50_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CNRMSMHI_50_N_grid_areas)  
    CSIRO_50_N_mean = CSIRO_50_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CSIRO_50_N_grid_areas)
    ICHECDMI_50_N_mean = ICHECDMI_50_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECDMI_50_N_grid_areas) 
    ICHECKNMI_50_N_mean = ICHECKNMI_50_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECKNMI_50_N_grid_areas)
    ICHECSMHI_50_N_mean = ICHECSMHI_50_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECSMHI_50_N_grid_areas)
    IPSL_50_N_mean = IPSL_50_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=IPSL_50_N_grid_areas)
    MIROC_50_N_mean = MIROC_50_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MIROC_50_N_grid_areas)
    MOHCKNMI_50_N_mean = MOHCKNMI_50_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCKNMI_50_N_grid_areas)
    MOHCSMHI_50_N_mean = MOHCSMHI_50_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCSMHI_50_N_grid_areas)
    MPISMHI_50_N_mean = MPISMHI_50_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MPISMHI_50_N_grid_areas)
    NCCSMHI_50_N_mean = NCCSMHI_50_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=NCCSMHI_50_N_grid_areas) 
    NOAA_50_N_mean = NOAA_50_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=NOAA_50_N_grid_areas)
    
    CCCmaSMHI85_50_N_mean = CCCmaSMHI85_50_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CCCmaSMHI85_50_N_grid_areas) 
    CNRMSMHI85_50_N_mean = CNRMSMHI85_50_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CNRMSMHI85_50_N_grid_areas)  
    CSIRO85_50_N_mean = CSIRO85_50_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CSIRO85_50_N_grid_areas)
    ICHECDMI85_50_N_mean = ICHECDMI85_50_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECDMI85_50_N_grid_areas) 
    ICHECKNMI85_50_N_mean = ICHECKNMI85_50_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECKNMI85_50_N_grid_areas)
    ICHECSMHI85_50_N_mean = ICHECSMHI85_50_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECSMHI85_50_N_grid_areas)
    IPSL85_50_N_mean = IPSL85_50_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=IPSL85_50_N_grid_areas)
    MIROC85_50_N_mean = MIROC85_50_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MIROC85_50_N_grid_areas)
    MOHCKNMI85_50_N_mean = MOHCKNMI85_50_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCKNMI85_50_N_grid_areas)
    MOHCSMHI85_50_N_mean = MOHCSMHI85_50_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCSMHI85_50_N_grid_areas)
    MPISMHI85_50_N_mean = MPISMHI85_50_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MPISMHI85_50_N_grid_areas)
    NCCSMHI85_50_N_mean = NCCSMHI85_50_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=NCCSMHI85_50_N_grid_areas) 
    NOAA85_50_N_mean = NOAA85_50_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=NOAA85_50_N_grid_areas)
    
    
    #PART 4B: CENTRAL MALAWI
    #we are only interested in the latitude and longitude relevant to Central Malawi 
    Central_Malawi = iris.Constraint(longitude=lambda v: 32.5 <= v <= 35.5, latitude=lambda v: -15 <= v <= -11.5) 
    
    CCCmaSMHI_past_C = CCCmaSMHI_past.extract(Central_Malawi)
    CNRMSMHI_past_C = CNRMSMHI_past.extract(Central_Malawi)
    CSIRO_past_C = CSIRO_past.extract(Central_Malawi)
    ICHECDMI_past_C = ICHECDMI_past.extract(Central_Malawi)
    ICHECKNMI_past_C = ICHECKNMI_past.extract(Central_Malawi)
    ICHECSMHI_past_C = ICHECSMHI_past.extract(Central_Malawi)
    IPSL_past_C = IPSL_past.extract(Central_Malawi)
    MIROC_past_C = MIROC_past.extract(Central_Malawi)
    MOHCKNMI_past_C = MOHCKNMI_past.extract(Central_Malawi)
    MOHCSMHI_past_C = MOHCSMHI_past.extract(Central_Malawi)
    MPISMHI_past_C = MPISMHI_past.extract(Central_Malawi)
    NCCSMHI_past_C = NCCSMHI_past.extract(Central_Malawi)
    NOAA_past_C = NOAA_past.extract(Central_Malawi)
    
    CCCmaSMHI_30_C = CCCmaSMHI_30.extract(Central_Malawi)
    CNRMSMHI_30_C = CNRMSMHI_30.extract(Central_Malawi)
    CSIRO_30_C = CSIRO_30.extract(Central_Malawi)
    ICHECDMI_30_C = ICHECDMI_30.extract(Central_Malawi)
    ICHECKNMI_30_C = ICHECKNMI_30.extract(Central_Malawi)
    ICHECSMHI_30_C = ICHECSMHI_30.extract(Central_Malawi)
    IPSL_30_C = IPSL_30.extract(Central_Malawi)
    MIROC_30_C = MIROC_30.extract(Central_Malawi)
    MOHCKNMI_30_C = MOHCKNMI_30.extract(Central_Malawi)
    MOHCSMHI_30_C = MOHCSMHI_30.extract(Central_Malawi)
    MPISMHI_30_C = MPISMHI_30.extract(Central_Malawi)
    NCCSMHI_30_C = NCCSMHI_30.extract(Central_Malawi)
    NOAA_30_C = NOAA_30.extract(Central_Malawi)
    
    CCCmaSMHI85_30_C = CCCmaSMHI85_30.extract(Central_Malawi)
    CNRMSMHI85_30_C = CNRMSMHI85_30.extract(Central_Malawi)
    CSIRO85_30_C = CSIRO85_30.extract(Central_Malawi)
    ICHECDMI85_30_C = ICHECDMI85_30.extract(Central_Malawi)
    ICHECKNMI85_30_C = ICHECKNMI85_30.extract(Central_Malawi)
    ICHECSMHI85_30_C = ICHECSMHI85_30.extract(Central_Malawi)
    IPSL85_30_C = IPSL85_30.extract(Central_Malawi)
    MIROC85_30_C = MIROC85_30.extract(Central_Malawi)
    MOHCKNMI85_30_C = MOHCKNMI85_30.extract(Central_Malawi)
    MOHCSMHI85_30_C = MOHCSMHI85_30.extract(Central_Malawi)
    MPISMHI85_30_C = MPISMHI85_30.extract(Central_Malawi)
    NCCSMHI85_30_C = NCCSMHI85_30.extract(Central_Malawi)
    NOAA85_30_C = NOAA85_30.extract(Central_Malawi)
    
    CCCmaSMHI_50_C = CCCmaSMHI_50.extract(Central_Malawi)
    CNRMSMHI_50_C = CNRMSMHI_50.extract(Central_Malawi)
    CSIRO_50_C = CSIRO_50.extract(Central_Malawi)
    ICHECDMI_50_C = ICHECDMI_50.extract(Central_Malawi)
    ICHECKNMI_50_C = ICHECKNMI_50.extract(Central_Malawi)
    ICHECSMHI_50_C = ICHECSMHI_50.extract(Central_Malawi)
    IPSL_50_C = IPSL_50.extract(Central_Malawi)
    MIROC_50_C = MIROC_50.extract(Central_Malawi)
    MOHCKNMI_50_C = MOHCKNMI_50.extract(Central_Malawi)
    MOHCSMHI_50_C = MOHCSMHI_50.extract(Central_Malawi)
    MPISMHI_50_C = MPISMHI_50.extract(Central_Malawi)
    NCCSMHI_50_C = NCCSMHI_50.extract(Central_Malawi)
    NOAA_50_C = NOAA_50.extract(Central_Malawi)
    
    CCCmaSMHI85_50_C = CCCmaSMHI85_50.extract(Central_Malawi)
    CNRMSMHI85_50_C = CNRMSMHI85_50.extract(Central_Malawi)
    CSIRO85_50_C = CSIRO85_50.extract(Central_Malawi)
    ICHECDMI85_50_C = ICHECDMI85_50.extract(Central_Malawi)
    ICHECKNMI85_50_C = ICHECKNMI85_50.extract(Central_Malawi)
    ICHECSMHI85_50_C = ICHECSMHI85_50.extract(Central_Malawi)
    IPSL85_50_C = IPSL85_50.extract(Central_Malawi)
    MIROC85_50_C = MIROC85_50.extract(Central_Malawi)
    MOHCKNMI85_50_C = MOHCKNMI85_50.extract(Central_Malawi)
    MOHCSMHI85_50_C = MOHCSMHI85_50.extract(Central_Malawi)
    MPISMHI85_50_C = MPISMHI85_50.extract(Central_Malawi)
    NCCSMHI85_50_C = NCCSMHI85_50.extract(Central_Malawi)
    NOAA85_50_C = NOAA85_50.extract(Central_Malawi)
    
    #Returns an array of area weights, with the same dimensions as the cube
    CCCmaSMHI_past_C_grid_areas = iris.analysis.cartography.area_weights(CCCmaSMHI_past_C)
    CNRMSMHI_past_C_grid_areas = iris.analysis.cartography.area_weights(CNRMSMHI_past_C)
    CSIRO_past_C_grid_areas = iris.analysis.cartography.area_weights(CSIRO_past_C)
    ICHECDMI_past_C_grid_areas = iris.analysis.cartography.area_weights(ICHECDMI_past_C)
    ICHECKNMI_past_C_grid_areas = iris.analysis.cartography.area_weights(ICHECKNMI_past_C)
    ICHECSMHI_past_C_grid_areas = iris.analysis.cartography.area_weights(ICHECSMHI_past_C)
    IPSL_past_C_grid_areas = iris.analysis.cartography.area_weights(IPSL_past_C)
    MIROC_past_C_grid_areas = iris.analysis.cartography.area_weights(MIROC_past_C)
    MOHCKNMI_past_C_grid_areas = iris.analysis.cartography.area_weights(MOHCKNMI_past_C)
    MOHCSMHI_past_C_grid_areas = iris.analysis.cartography.area_weights(MOHCSMHI_past_C)
    MPISMHI_past_C_grid_areas = iris.analysis.cartography.area_weights(MPISMHI_past_C)
    NCCSMHI_past_C_grid_areas = iris.analysis.cartography.area_weights(NCCSMHI_past_C)
    NOAA_past_C_grid_areas = iris.analysis.cartography.area_weights(NOAA_past_C)
    
    CCCmaSMHI_30_C_grid_areas = iris.analysis.cartography.area_weights(CCCmaSMHI_30_C)
    CNRMSMHI_30_C_grid_areas = iris.analysis.cartography.area_weights(CNRMSMHI_30_C)
    CSIRO_30_C_grid_areas = iris.analysis.cartography.area_weights(CSIRO_30_C)
    ICHECDMI_30_C_grid_areas = iris.analysis.cartography.area_weights(ICHECDMI_30_C)
    ICHECKNMI_30_C_grid_areas = iris.analysis.cartography.area_weights(ICHECKNMI_30_C)
    ICHECSMHI_30_C_grid_areas = iris.analysis.cartography.area_weights(ICHECSMHI_30_C)
    IPSL_30_C_grid_areas = iris.analysis.cartography.area_weights(IPSL_30_C)
    MIROC_30_C_grid_areas = iris.analysis.cartography.area_weights(MIROC_30_C)
    MOHCKNMI_30_C_grid_areas = iris.analysis.cartography.area_weights(MOHCKNMI_30_C)
    MOHCSMHI_30_C_grid_areas = iris.analysis.cartography.area_weights(MOHCSMHI_30_C)
    MPISMHI_30_C_grid_areas = iris.analysis.cartography.area_weights(MPISMHI_30_C)
    NCCSMHI_30_C_grid_areas = iris.analysis.cartography.area_weights(NCCSMHI_30_C)
    NOAA_30_C_grid_areas = iris.analysis.cartography.area_weights(NOAA_30_C)
    
    CCCmaSMHI85_30_C_grid_areas = iris.analysis.cartography.area_weights(CCCmaSMHI85_30_C)
    CNRMSMHI85_30_C_grid_areas = iris.analysis.cartography.area_weights(CNRMSMHI85_30_C)
    CSIRO85_30_C_grid_areas = iris.analysis.cartography.area_weights(CSIRO85_30_C)
    ICHECDMI85_30_C_grid_areas = iris.analysis.cartography.area_weights(ICHECDMI85_30_C)
    ICHECKNMI85_30_C_grid_areas = iris.analysis.cartography.area_weights(ICHECKNMI85_30_C)
    ICHECSMHI85_30_C_grid_areas = iris.analysis.cartography.area_weights(ICHECSMHI85_30_C)
    IPSL85_30_C_grid_areas = iris.analysis.cartography.area_weights(IPSL85_30_C)
    MIROC85_30_C_grid_areas = iris.analysis.cartography.area_weights(MIROC85_30_C)
    MOHCKNMI85_30_C_grid_areas = iris.analysis.cartography.area_weights(MOHCKNMI85_30_C)
    MOHCSMHI85_30_C_grid_areas = iris.analysis.cartography.area_weights(MOHCSMHI85_30_C)
    MPISMHI85_30_C_grid_areas = iris.analysis.cartography.area_weights(MPISMHI85_30_C)
    NCCSMHI85_30_C_grid_areas = iris.analysis.cartography.area_weights(NCCSMHI85_30_C)
    NOAA85_30_C_grid_areas = iris.analysis.cartography.area_weights(NOAA85_30_C)
    
    CCCmaSMHI_50_C_grid_areas = iris.analysis.cartography.area_weights(CCCmaSMHI_50_C)
    CNRMSMHI_50_C_grid_areas = iris.analysis.cartography.area_weights(CNRMSMHI_50_C)
    CSIRO_50_C_grid_areas = iris.analysis.cartography.area_weights(CSIRO_50_C)
    ICHECDMI_50_C_grid_areas = iris.analysis.cartography.area_weights(ICHECDMI_50_C)
    ICHECKNMI_50_C_grid_areas = iris.analysis.cartography.area_weights(ICHECKNMI_50_C)
    ICHECSMHI_50_C_grid_areas = iris.analysis.cartography.area_weights(ICHECSMHI_50_C)
    IPSL_50_C_grid_areas = iris.analysis.cartography.area_weights(IPSL_50_C)
    MIROC_50_C_grid_areas = iris.analysis.cartography.area_weights(MIROC_50_C)
    MOHCKNMI_50_C_grid_areas = iris.analysis.cartography.area_weights(MOHCKNMI_50_C)
    MOHCSMHI_50_C_grid_areas = iris.analysis.cartography.area_weights(MOHCSMHI_50_C)
    MPISMHI_50_C_grid_areas = iris.analysis.cartography.area_weights(MPISMHI_50_C)
    NCCSMHI_50_C_grid_areas = iris.analysis.cartography.area_weights(NCCSMHI_50_C)
    NOAA_50_C_grid_areas = iris.analysis.cartography.area_weights(NOAA_50_C)
    
    CCCmaSMHI85_50_C_grid_areas = iris.analysis.cartography.area_weights(CCCmaSMHI85_50_C)
    CNRMSMHI85_50_C_grid_areas = iris.analysis.cartography.area_weights(CNRMSMHI85_50_C)
    CSIRO85_50_C_grid_areas = iris.analysis.cartography.area_weights(CSIRO85_50_C)
    ICHECDMI85_50_C_grid_areas = iris.analysis.cartography.area_weights(ICHECDMI85_50_C)
    ICHECKNMI85_50_C_grid_areas = iris.analysis.cartography.area_weights(ICHECKNMI85_50_C)
    ICHECSMHI85_50_C_grid_areas = iris.analysis.cartography.area_weights(ICHECSMHI85_50_C)
    IPSL85_50_C_grid_areas = iris.analysis.cartography.area_weights(IPSL85_50_C)
    MIROC85_50_C_grid_areas = iris.analysis.cartography.area_weights(MIROC85_50_C)
    MOHCKNMI85_50_C_grid_areas = iris.analysis.cartography.area_weights(MOHCKNMI85_50_C)
    MOHCSMHI85_50_C_grid_areas = iris.analysis.cartography.area_weights(MOHCSMHI85_50_C)
    MPISMHI85_50_C_grid_areas = iris.analysis.cartography.area_weights(MPISMHI85_50_C)
    NCCSMHI85_50_C_grid_areas = iris.analysis.cartography.area_weights(NCCSMHI85_50_C)
    NOAA85_50_C_grid_areas = iris.analysis.cartography.area_weights(NOAA85_50_C)

    #We want to plot the mean for the whole region so we need a mean of all the lats and lons
    CCCmaSMHI_past_C_mean = CCCmaSMHI_past_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CCCmaSMHI_past_C_grid_areas) 
    CNRMSMHI_past_C_mean = CNRMSMHI_past_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CNRMSMHI_past_C_grid_areas)  
    CSIRO_past_C_mean = CSIRO_past_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CSIRO_past_C_grid_areas)
    ICHECDMI_past_C_mean = ICHECDMI_past_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECDMI_past_C_grid_areas) 
    ICHECKNMI_past_C_mean = ICHECKNMI_past_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECKNMI_past_C_grid_areas)
    ICHECSMHI_past_C_mean = ICHECSMHI_past_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECSMHI_past_C_grid_areas)
    IPSL_past_C_mean = IPSL_past_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=IPSL_past_C_grid_areas)
    MIROC_past_C_mean = MIROC_past_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MIROC_past_C_grid_areas)
    MOHCKNMI_past_C_mean = MOHCKNMI_past_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCKNMI_past_C_grid_areas)
    MOHCSMHI_past_C_mean = MOHCSMHI_past_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCSMHI_past_C_grid_areas)
    MPISMHI_past_C_mean = MPISMHI_past_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MPISMHI_past_C_grid_areas)
    NCCSMHI_past_C_mean = NCCSMHI_past_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=NCCSMHI_past_C_grid_areas) 
    NOAA_past_C_mean = NOAA_past_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=NOAA_past_C_grid_areas)
    
    CCCmaSMHI_30_C_mean = CCCmaSMHI_30_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CCCmaSMHI_30_C_grid_areas) 
    CNRMSMHI_30_C_mean = CNRMSMHI_30_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CNRMSMHI_30_C_grid_areas)  
    CSIRO_30_C_mean = CSIRO_30_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CSIRO_30_C_grid_areas)
    ICHECDMI_30_C_mean = ICHECDMI_30_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECDMI_30_C_grid_areas) 
    ICHECKNMI_30_C_mean = ICHECKNMI_30_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECKNMI_30_C_grid_areas)
    ICHECSMHI_30_C_mean = ICHECSMHI_30_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECSMHI_30_C_grid_areas)
    IPSL_30_C_mean = IPSL_30_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=IPSL_30_C_grid_areas)
    MIROC_30_C_mean = MIROC_30_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MIROC_30_C_grid_areas)
    MOHCKNMI_30_C_mean = MOHCKNMI_30_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCKNMI_30_C_grid_areas)
    MOHCSMHI_30_C_mean = MOHCSMHI_30_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCSMHI_30_C_grid_areas)
    MPISMHI_30_C_mean = MPISMHI_30_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MPISMHI_30_C_grid_areas)
    NCCSMHI_30_C_mean = NCCSMHI_30_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=NCCSMHI_30_C_grid_areas) 
    NOAA_30_C_mean = NOAA_30_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=NOAA_30_C_grid_areas)
    
    CCCmaSMHI85_30_C_mean = CCCmaSMHI85_30_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CCCmaSMHI85_30_C_grid_areas) 
    CNRMSMHI85_30_C_mean = CNRMSMHI85_30_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CNRMSMHI85_30_C_grid_areas)  
    CSIRO85_30_C_mean = CSIRO85_30_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CSIRO85_30_C_grid_areas)
    ICHECDMI85_30_C_mean = ICHECDMI85_30_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECDMI85_30_C_grid_areas) 
    ICHECKNMI85_30_C_mean = ICHECKNMI85_30_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECKNMI85_30_C_grid_areas)
    ICHECSMHI85_30_C_mean = ICHECSMHI85_30_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECSMHI85_30_C_grid_areas)
    IPSL85_30_C_mean = IPSL85_30_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=IPSL85_30_C_grid_areas)
    MIROC85_30_C_mean = MIROC85_30_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MIROC85_30_C_grid_areas)
    MOHCKNMI85_30_C_mean = MOHCKNMI85_30_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCKNMI85_30_C_grid_areas)
    MOHCSMHI85_30_C_mean = MOHCSMHI85_30_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCSMHI85_30_C_grid_areas)
    MPISMHI85_30_C_mean = MPISMHI85_30_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MPISMHI85_30_C_grid_areas)
    NCCSMHI85_30_C_mean = NCCSMHI85_30_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=NCCSMHI85_30_C_grid_areas) 
    NOAA85_30_C_mean = NOAA85_30_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=NOAA85_30_C_grid_areas)
    
    CCCmaSMHI_50_C_mean = CCCmaSMHI_50_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CCCmaSMHI_50_C_grid_areas) 
    CNRMSMHI_50_C_mean = CNRMSMHI_50_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CNRMSMHI_50_C_grid_areas)  
    CSIRO_50_C_mean = CSIRO_50_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CSIRO_50_C_grid_areas)
    ICHECDMI_50_C_mean = ICHECDMI_50_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECDMI_50_C_grid_areas) 
    ICHECKNMI_50_C_mean = ICHECKNMI_50_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECKNMI_50_C_grid_areas)
    ICHECSMHI_50_C_mean = ICHECSMHI_50_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECSMHI_50_C_grid_areas)
    IPSL_50_C_mean = IPSL_50_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=IPSL_50_C_grid_areas)
    MIROC_50_C_mean = MIROC_50_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MIROC_50_C_grid_areas)
    MOHCKNMI_50_C_mean = MOHCKNMI_50_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCKNMI_50_C_grid_areas)
    MOHCSMHI_50_C_mean = MOHCSMHI_50_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCSMHI_50_C_grid_areas)
    MPISMHI_50_C_mean = MPISMHI_50_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MPISMHI_50_C_grid_areas)
    NCCSMHI_50_C_mean = NCCSMHI_50_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=NCCSMHI_50_C_grid_areas) 
    NOAA_50_C_mean = NOAA_50_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=NOAA_50_C_grid_areas)
    
    CCCmaSMHI85_50_C_mean = CCCmaSMHI85_50_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CCCmaSMHI85_50_C_grid_areas) 
    CNRMSMHI85_50_C_mean = CNRMSMHI85_50_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CNRMSMHI85_50_C_grid_areas)  
    CSIRO85_50_C_mean = CSIRO85_50_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CSIRO85_50_C_grid_areas)
    ICHECDMI85_50_C_mean = ICHECDMI85_50_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECDMI85_50_C_grid_areas) 
    ICHECKNMI85_50_C_mean = ICHECKNMI85_50_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECKNMI85_50_C_grid_areas)
    ICHECSMHI85_50_C_mean = ICHECSMHI85_50_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECSMHI85_50_C_grid_areas)
    IPSL85_50_C_mean = IPSL85_50_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=IPSL85_50_C_grid_areas)
    MIROC85_50_C_mean = MIROC85_50_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MIROC85_50_C_grid_areas)
    MOHCKNMI85_50_C_mean = MOHCKNMI85_50_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCKNMI85_50_C_grid_areas)
    MOHCSMHI85_50_C_mean = MOHCSMHI85_50_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCSMHI85_50_C_grid_areas)
    MPISMHI85_50_C_mean = MPISMHI85_50_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MPISMHI85_50_C_grid_areas)
    NCCSMHI85_50_C_mean = NCCSMHI85_50_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=NCCSMHI85_50_C_grid_areas) 
    NOAA85_50_C_mean = NOAA85_50_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=NOAA85_50_C_grid_areas)

    
            
    #PART 4C: SOUTHERN MALAWI
    #we are only interested in the latitude and longitude relevant to Southern Malawi 
    Southern_Malawi = iris.Constraint(longitude=lambda v: 34 <= v <= 36.5, latitude=lambda v: -17.5 <= v <= -14) 
    
    CCCmaSMHI_past_S = CCCmaSMHI_past.extract(Southern_Malawi)
    CNRMSMHI_past_S = CNRMSMHI_past.extract(Southern_Malawi)
    CSIRO_past_S = CSIRO_past.extract(Southern_Malawi)
    ICHECDMI_past_S = ICHECDMI_past.extract(Southern_Malawi)
    ICHECKNMI_past_S = ICHECKNMI_past.extract(Southern_Malawi)
    ICHECSMHI_past_S = ICHECSMHI_past.extract(Southern_Malawi)
    IPSL_past_S = IPSL_past.extract(Southern_Malawi)
    MIROC_past_S = MIROC_past.extract(Southern_Malawi)
    MOHCKNMI_past_S = MOHCKNMI_past.extract(Southern_Malawi)
    MOHCSMHI_past_S = MOHCSMHI_past.extract(Southern_Malawi)
    MPISMHI_past_S = MPISMHI_past.extract(Southern_Malawi)
    NCCSMHI_past_S = NCCSMHI_past.extract(Southern_Malawi)
    NOAA_past_S = NOAA_past.extract(Southern_Malawi)
    
    CCCmaSMHI_30_S = CCCmaSMHI_30.extract(Southern_Malawi)
    CNRMSMHI_30_S = CNRMSMHI_30.extract(Southern_Malawi)
    CSIRO_30_S = CSIRO_30.extract(Southern_Malawi)
    ICHECDMI_30_S = ICHECDMI_30.extract(Southern_Malawi)
    ICHECKNMI_30_S = ICHECKNMI_30.extract(Southern_Malawi)
    ICHECSMHI_30_S = ICHECSMHI_30.extract(Southern_Malawi)
    IPSL_30_S = IPSL_30.extract(Southern_Malawi)
    MIROC_30_S = MIROC_30.extract(Southern_Malawi)
    MOHCKNMI_30_S = MOHCKNMI_30.extract(Southern_Malawi)
    MOHCSMHI_30_S = MOHCSMHI_30.extract(Southern_Malawi)
    MPISMHI_30_S = MPISMHI_30.extract(Southern_Malawi)
    NCCSMHI_30_S = NCCSMHI_30.extract(Southern_Malawi)
    NOAA_30_S = NOAA_30.extract(Southern_Malawi)
    
    CCCmaSMHI85_30_S = CCCmaSMHI85_30.extract(Southern_Malawi)
    CNRMSMHI85_30_S = CNRMSMHI85_30.extract(Southern_Malawi)
    CSIRO85_30_S = CSIRO85_30.extract(Southern_Malawi)
    ICHECDMI85_30_S = ICHECDMI85_30.extract(Southern_Malawi)
    ICHECKNMI85_30_S = ICHECKNMI85_30.extract(Southern_Malawi)
    ICHECSMHI85_30_S = ICHECSMHI85_30.extract(Southern_Malawi)
    IPSL85_30_S = IPSL85_30.extract(Southern_Malawi)
    MIROC85_30_S = MIROC85_30.extract(Southern_Malawi)
    MOHCKNMI85_30_S = MOHCKNMI85_30.extract(Southern_Malawi)
    MOHCSMHI85_30_S = MOHCSMHI85_30.extract(Southern_Malawi)
    MPISMHI85_30_S = MPISMHI85_30.extract(Southern_Malawi)
    NCCSMHI85_30_S = NCCSMHI85_30.extract(Southern_Malawi)
    NOAA85_30_S = NOAA85_30.extract(Southern_Malawi)
    
    CCCmaSMHI_50_S = CCCmaSMHI_50.extract(Southern_Malawi)
    CNRMSMHI_50_S = CNRMSMHI_50.extract(Southern_Malawi)
    CSIRO_50_S = CSIRO_50.extract(Southern_Malawi)
    ICHECDMI_50_S = ICHECDMI_50.extract(Southern_Malawi)
    ICHECKNMI_50_S = ICHECKNMI_50.extract(Southern_Malawi)
    ICHECSMHI_50_S = ICHECSMHI_50.extract(Southern_Malawi)
    IPSL_50_S = IPSL_50.extract(Southern_Malawi)
    MIROC_50_S = MIROC_50.extract(Southern_Malawi)
    MOHCKNMI_50_S = MOHCKNMI_50.extract(Southern_Malawi)
    MOHCSMHI_50_S = MOHCSMHI_50.extract(Southern_Malawi)
    MPISMHI_50_S = MPISMHI_50.extract(Southern_Malawi)
    NCCSMHI_50_S = NCCSMHI_50.extract(Southern_Malawi)
    NOAA_50_S = NOAA_50.extract(Southern_Malawi)
    
    CCCmaSMHI85_50_S = CCCmaSMHI85_50.extract(Southern_Malawi)
    CNRMSMHI85_50_S = CNRMSMHI85_50.extract(Southern_Malawi)
    CSIRO85_50_S = CSIRO85_50.extract(Southern_Malawi)
    ICHECDMI85_50_S = ICHECDMI85_50.extract(Southern_Malawi)
    ICHECKNMI85_50_S = ICHECKNMI85_50.extract(Southern_Malawi)
    ICHECSMHI85_50_S = ICHECSMHI85_50.extract(Southern_Malawi)
    IPSL85_50_S = IPSL85_50.extract(Southern_Malawi)
    MIROC85_50_S = MIROC85_50.extract(Southern_Malawi)
    MOHCKNMI85_50_S = MOHCKNMI85_50.extract(Southern_Malawi)
    MOHCSMHI85_50_S = MOHCSMHI85_50.extract(Southern_Malawi)
    MPISMHI85_50_S = MPISMHI85_50.extract(Southern_Malawi)
    NCCSMHI85_50_S = NCCSMHI85_50.extract(Southern_Malawi)
    NOAA85_50_S = NOAA85_50.extract(Southern_Malawi)
    
    #Returns an array of area weights, with the same dimensions as the cube
    CCCmaSMHI_past_S_grid_areas = iris.analysis.cartography.area_weights(CCCmaSMHI_past_S)
    CNRMSMHI_past_S_grid_areas = iris.analysis.cartography.area_weights(CNRMSMHI_past_S)
    CSIRO_past_S_grid_areas = iris.analysis.cartography.area_weights(CSIRO_past_S)
    ICHECDMI_past_S_grid_areas = iris.analysis.cartography.area_weights(ICHECDMI_past_S)
    ICHECKNMI_past_S_grid_areas = iris.analysis.cartography.area_weights(ICHECKNMI_past_S)
    ICHECSMHI_past_S_grid_areas = iris.analysis.cartography.area_weights(ICHECSMHI_past_S)
    IPSL_past_S_grid_areas = iris.analysis.cartography.area_weights(IPSL_past_S)
    MIROC_past_S_grid_areas = iris.analysis.cartography.area_weights(MIROC_past_S)
    MOHCKNMI_past_S_grid_areas = iris.analysis.cartography.area_weights(MOHCKNMI_past_S)
    MOHCSMHI_past_S_grid_areas = iris.analysis.cartography.area_weights(MOHCSMHI_past_S)
    MPISMHI_past_S_grid_areas = iris.analysis.cartography.area_weights(MPISMHI_past_S)
    NCCSMHI_past_S_grid_areas = iris.analysis.cartography.area_weights(NCCSMHI_past_S)
    NOAA_past_S_grid_areas = iris.analysis.cartography.area_weights(NOAA_past_S)
    
    CCCmaSMHI_30_S_grid_areas = iris.analysis.cartography.area_weights(CCCmaSMHI_30_S)
    CNRMSMHI_30_S_grid_areas = iris.analysis.cartography.area_weights(CNRMSMHI_30_S)
    CSIRO_30_S_grid_areas = iris.analysis.cartography.area_weights(CSIRO_30_S)
    ICHECDMI_30_S_grid_areas = iris.analysis.cartography.area_weights(ICHECDMI_30_S)
    ICHECKNMI_30_S_grid_areas = iris.analysis.cartography.area_weights(ICHECKNMI_30_S)
    ICHECSMHI_30_S_grid_areas = iris.analysis.cartography.area_weights(ICHECSMHI_30_S)
    IPSL_30_S_grid_areas = iris.analysis.cartography.area_weights(IPSL_30_S)
    MIROC_30_S_grid_areas = iris.analysis.cartography.area_weights(MIROC_30_S)
    MOHCKNMI_30_S_grid_areas = iris.analysis.cartography.area_weights(MOHCKNMI_30_S)
    MOHCSMHI_30_S_grid_areas = iris.analysis.cartography.area_weights(MOHCSMHI_30_S)
    MPISMHI_30_S_grid_areas = iris.analysis.cartography.area_weights(MPISMHI_30_S)
    NCCSMHI_30_S_grid_areas = iris.analysis.cartography.area_weights(NCCSMHI_30_S)
    NOAA_30_S_grid_areas = iris.analysis.cartography.area_weights(NOAA_30_S)
    
    CCCmaSMHI85_30_S_grid_areas = iris.analysis.cartography.area_weights(CCCmaSMHI85_30_S)
    CNRMSMHI85_30_S_grid_areas = iris.analysis.cartography.area_weights(CNRMSMHI85_30_S)
    CSIRO85_30_S_grid_areas = iris.analysis.cartography.area_weights(CSIRO85_30_S)
    ICHECDMI85_30_S_grid_areas = iris.analysis.cartography.area_weights(ICHECDMI85_30_S)
    ICHECKNMI85_30_S_grid_areas = iris.analysis.cartography.area_weights(ICHECKNMI85_30_S)
    ICHECSMHI85_30_S_grid_areas = iris.analysis.cartography.area_weights(ICHECSMHI85_30_S)
    IPSL85_30_S_grid_areas = iris.analysis.cartography.area_weights(IPSL85_30_S)
    MIROC85_30_S_grid_areas = iris.analysis.cartography.area_weights(MIROC85_30_S)
    MOHCKNMI85_30_S_grid_areas = iris.analysis.cartography.area_weights(MOHCKNMI85_30_S)
    MOHCSMHI85_30_S_grid_areas = iris.analysis.cartography.area_weights(MOHCSMHI85_30_S)
    MPISMHI85_30_S_grid_areas = iris.analysis.cartography.area_weights(MPISMHI85_30_S)
    NCCSMHI85_30_S_grid_areas = iris.analysis.cartography.area_weights(NCCSMHI85_30_S)
    NOAA85_30_S_grid_areas = iris.analysis.cartography.area_weights(NOAA85_30_S)
    
    CCCmaSMHI_50_S_grid_areas = iris.analysis.cartography.area_weights(CCCmaSMHI_50_S)
    CNRMSMHI_50_S_grid_areas = iris.analysis.cartography.area_weights(CNRMSMHI_50_S)
    CSIRO_50_S_grid_areas = iris.analysis.cartography.area_weights(CSIRO_50_S)
    ICHECDMI_50_S_grid_areas = iris.analysis.cartography.area_weights(ICHECDMI_50_S)
    ICHECKNMI_50_S_grid_areas = iris.analysis.cartography.area_weights(ICHECKNMI_50_S)
    ICHECSMHI_50_S_grid_areas = iris.analysis.cartography.area_weights(ICHECSMHI_50_S)
    IPSL_50_S_grid_areas = iris.analysis.cartography.area_weights(IPSL_50_S)
    MIROC_50_S_grid_areas = iris.analysis.cartography.area_weights(MIROC_50_S)
    MOHCKNMI_50_S_grid_areas = iris.analysis.cartography.area_weights(MOHCKNMI_50_S)
    MOHCSMHI_50_S_grid_areas = iris.analysis.cartography.area_weights(MOHCSMHI_50_S)
    MPISMHI_50_S_grid_areas = iris.analysis.cartography.area_weights(MPISMHI_50_S)
    NCCSMHI_50_S_grid_areas = iris.analysis.cartography.area_weights(NCCSMHI_50_S)
    NOAA_50_S_grid_areas = iris.analysis.cartography.area_weights(NOAA_50_S)
    
    CCCmaSMHI85_50_S_grid_areas = iris.analysis.cartography.area_weights(CCCmaSMHI85_50_S)
    CNRMSMHI85_50_S_grid_areas = iris.analysis.cartography.area_weights(CNRMSMHI85_50_S)
    CSIRO85_50_S_grid_areas = iris.analysis.cartography.area_weights(CSIRO85_50_S)
    ICHECDMI85_50_S_grid_areas = iris.analysis.cartography.area_weights(ICHECDMI85_50_S)
    ICHECKNMI85_50_S_grid_areas = iris.analysis.cartography.area_weights(ICHECKNMI85_50_S)
    ICHECSMHI85_50_S_grid_areas = iris.analysis.cartography.area_weights(ICHECSMHI85_50_S)
    IPSL85_50_S_grid_areas = iris.analysis.cartography.area_weights(IPSL85_50_S)
    MIROC85_50_S_grid_areas = iris.analysis.cartography.area_weights(MIROC85_50_S)
    MOHCKNMI85_50_S_grid_areas = iris.analysis.cartography.area_weights(MOHCKNMI85_50_S)
    MOHCSMHI85_50_S_grid_areas = iris.analysis.cartography.area_weights(MOHCSMHI85_50_S)
    MPISMHI85_50_S_grid_areas = iris.analysis.cartography.area_weights(MPISMHI85_50_S)
    NCCSMHI85_50_S_grid_areas = iris.analysis.cartography.area_weights(NCCSMHI85_50_S)
    NOAA85_50_S_grid_areas = iris.analysis.cartography.area_weights(NOAA85_50_S)

    #We want to plot the mean for the whole region so we need a mean of all the lats and lons
    CCCmaSMHI_past_S_mean = CCCmaSMHI_past_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CCCmaSMHI_past_S_grid_areas) 
    CNRMSMHI_past_S_mean = CNRMSMHI_past_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CNRMSMHI_past_S_grid_areas)  
    CSIRO_past_S_mean = CSIRO_past_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CSIRO_past_S_grid_areas)
    ICHECDMI_past_S_mean = ICHECDMI_past_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECDMI_past_S_grid_areas) 
    ICHECKNMI_past_S_mean = ICHECKNMI_past_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECKNMI_past_S_grid_areas)
    ICHECSMHI_past_S_mean = ICHECSMHI_past_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECSMHI_past_S_grid_areas)
    IPSL_past_S_mean = IPSL_past_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=IPSL_past_S_grid_areas)
    MIROC_past_S_mean = MIROC_past_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MIROC_past_S_grid_areas)
    MOHCKNMI_past_S_mean = MOHCKNMI_past_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCKNMI_past_S_grid_areas)
    MOHCSMHI_past_S_mean = MOHCSMHI_past_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCSMHI_past_S_grid_areas)
    MPISMHI_past_S_mean = MPISMHI_past_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MPISMHI_past_S_grid_areas)
    NCCSMHI_past_S_mean = NCCSMHI_past_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=NCCSMHI_past_S_grid_areas) 
    NOAA_past_S_mean = NOAA_past_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=NOAA_past_S_grid_areas)
    
    CCCmaSMHI_30_S_mean = CCCmaSMHI_30_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CCCmaSMHI_30_S_grid_areas) 
    CNRMSMHI_30_S_mean = CNRMSMHI_30_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CNRMSMHI_30_S_grid_areas)  
    CSIRO_30_S_mean = CSIRO_30_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CSIRO_30_S_grid_areas)
    ICHECDMI_30_S_mean = ICHECDMI_30_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECDMI_30_S_grid_areas) 
    ICHECKNMI_30_S_mean = ICHECKNMI_30_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECKNMI_30_S_grid_areas)
    ICHECSMHI_30_S_mean = ICHECSMHI_30_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECSMHI_30_S_grid_areas)
    IPSL_30_S_mean = IPSL_30_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=IPSL_30_S_grid_areas)
    MIROC_30_S_mean = MIROC_30_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MIROC_30_S_grid_areas)
    MOHCKNMI_30_S_mean = MOHCKNMI_30_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCKNMI_30_S_grid_areas)
    MOHCSMHI_30_S_mean = MOHCSMHI_30_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCSMHI_30_S_grid_areas)
    MPISMHI_30_S_mean = MPISMHI_30_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MPISMHI_30_S_grid_areas)
    NCCSMHI_30_S_mean = NCCSMHI_30_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=NCCSMHI_30_S_grid_areas) 
    NOAA_30_S_mean = NOAA_30_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=NOAA_30_S_grid_areas)
    
    CCCmaSMHI85_30_S_mean = CCCmaSMHI85_30_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CCCmaSMHI85_30_S_grid_areas) 
    CNRMSMHI85_30_S_mean = CNRMSMHI85_30_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CNRMSMHI85_30_S_grid_areas)  
    CSIRO85_30_S_mean = CSIRO85_30_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CSIRO85_30_S_grid_areas)
    ICHECDMI85_30_S_mean = ICHECDMI85_30_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECDMI85_30_S_grid_areas) 
    ICHECKNMI85_30_S_mean = ICHECKNMI85_30_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECKNMI85_30_S_grid_areas)
    ICHECSMHI85_30_S_mean = ICHECSMHI85_30_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECSMHI85_30_S_grid_areas)
    IPSL85_30_S_mean = IPSL85_30_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=IPSL85_30_S_grid_areas)
    MIROC85_30_S_mean = MIROC85_30_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MIROC85_30_S_grid_areas)
    MOHCKNMI85_30_S_mean = MOHCKNMI85_30_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCKNMI85_30_S_grid_areas)
    MOHCSMHI85_30_S_mean = MOHCSMHI85_30_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCSMHI85_30_S_grid_areas)
    MPISMHI85_30_S_mean = MPISMHI85_30_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MPISMHI85_30_S_grid_areas)
    NCCSMHI85_30_S_mean = NCCSMHI85_30_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=NCCSMHI85_30_S_grid_areas) 
    NOAA85_30_S_mean = NOAA85_30_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=NOAA85_30_S_grid_areas)
    
    CCCmaSMHI_50_S_mean = CCCmaSMHI_50_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CCCmaSMHI_50_S_grid_areas) 
    CNRMSMHI_50_S_mean = CNRMSMHI_50_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CNRMSMHI_50_S_grid_areas)  
    CSIRO_50_S_mean = CSIRO_50_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CSIRO_50_S_grid_areas)
    ICHECDMI_50_S_mean = ICHECDMI_50_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECDMI_50_S_grid_areas) 
    ICHECKNMI_50_S_mean = ICHECKNMI_50_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECKNMI_50_S_grid_areas)
    ICHECSMHI_50_S_mean = ICHECSMHI_50_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECSMHI_50_S_grid_areas)
    IPSL_50_S_mean = IPSL_50_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=IPSL_50_S_grid_areas)
    MIROC_50_S_mean = MIROC_50_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MIROC_50_S_grid_areas)
    MOHCKNMI_50_S_mean = MOHCKNMI_50_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCKNMI_50_S_grid_areas)
    MOHCSMHI_50_S_mean = MOHCSMHI_50_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCSMHI_50_S_grid_areas)
    MPISMHI_50_S_mean = MPISMHI_50_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MPISMHI_50_S_grid_areas)
    NCCSMHI_50_S_mean = NCCSMHI_50_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=NCCSMHI_50_S_grid_areas) 
    NOAA_50_S_mean = NOAA_50_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=NOAA_50_S_grid_areas)
    
    CCCmaSMHI85_50_S_mean = CCCmaSMHI85_50_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CCCmaSMHI85_50_S_grid_areas) 
    CNRMSMHI85_50_S_mean = CNRMSMHI85_50_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CNRMSMHI85_50_S_grid_areas)  
    CSIRO85_50_S_mean = CSIRO85_50_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CSIRO85_50_S_grid_areas)
    ICHECDMI85_50_S_mean = ICHECDMI85_50_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECDMI85_50_S_grid_areas) 
    ICHECKNMI85_50_S_mean = ICHECKNMI85_50_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECKNMI85_50_S_grid_areas)
    ICHECSMHI85_50_S_mean = ICHECSMHI85_50_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECSMHI85_50_S_grid_areas)
    IPSL85_50_S_mean = IPSL85_50_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=IPSL85_50_S_grid_areas)
    MIROC85_50_S_mean = MIROC85_50_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MIROC85_50_S_grid_areas)
    MOHCKNMI85_50_S_mean = MOHCKNMI85_50_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCKNMI85_50_S_grid_areas)
    MOHCSMHI85_50_S_mean = MOHCSMHI85_50_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCSMHI85_50_S_grid_areas)
    MPISMHI85_50_S_mean = MPISMHI85_50_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MPISMHI85_50_S_grid_areas)
    NCCSMHI85_50_S_mean = NCCSMHI85_50_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=NCCSMHI85_50_S_grid_areas) 
    NOAA85_50_S_mean = NOAA85_50_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=NOAA85_50_S_grid_areas)    

   
    
    #-------------------------------------------------------------------------
    #PART 5: PRINT DATA
    import csv
    with open('output_DailyHursdataV2.csv', 'wb') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        
        writer.writerow(['Parameter', 'Means'])
        
    #PART 5A: WRITE NORTHERN DATA
        writer.writerow(["CCCmaSMHI_past_N_mean"] + CCCmaSMHI_past_N_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["CNRMSMHI_past_N_mean"] +CNRMSMHI_past_N_mean.data.flatten().astype(np.str).tolist())   
        writer.writerow(["CSIRO_past_N_mean"] +CSIRO_past_N_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["ICHECDMI_past_N_mean"] +ICHECDMI_past_N_mean.data.flatten().astype(np.str).tolist())       
        writer.writerow(["ICHECKNMI_past_N_mean"] +ICHECKNMI_past_N_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["ICHECSMHI_past_N_mean"] +ICHECSMHI_past_N_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["IPSL_past_N_mean"] +IPSL_past_N_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MIROC_past_N_mean"] +MIROC_past_N_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MOHCKNMI_past_N_mean"] +MOHCKNMI_past_N_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MOHCSMHI_past_N_mean"] +MOHCSMHI_past_N_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MPISMHI_past_N_mean"] +MPISMHI_past_N_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["NCCSMHI_past_N_mean"] +NCCSMHI_past_N_mean.data.flatten().astype(np.str).tolist())       
        writer.writerow(["NOAA_past_N_mean"] +NOAA_past_N_mean.data.flatten().astype(np.str).tolist())     
        
        writer.writerow(["CCCmaSMHI_30_N_mean"] + CCCmaSMHI_30_N_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["CNRMSMHI_30_N_mean"] +CNRMSMHI_30_N_mean.data.flatten().astype(np.str).tolist())   
        writer.writerow(["CSIRO_30_N_mean"] +CSIRO_30_N_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["ICHECDMI_30_N_mean"] +ICHECDMI_30_N_mean.data.flatten().astype(np.str).tolist())       
        writer.writerow(["ICHECKNMI_30_N_mean"] +ICHECKNMI_30_N_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["ICHECSMHI_30_N_mean"] +ICHECSMHI_30_N_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["IPSL_30_N_mean"] +IPSL_30_N_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MIROC_30_N_mean"] +MIROC_30_N_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MOHCKNMI_30_N_mean"] +MOHCKNMI_30_N_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MOHCSMHI_30_N_mean"] +MOHCSMHI_30_N_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MPISMHI_30_N_mean"] +MPISMHI_30_N_mean.data.flatten().astype(np.str).tolist())        
        writer.writerow(["NCCSMHI_30_N_mean"] +NCCSMHI_30_N_mean.data.flatten().astype(np.str).tolist())       
        writer.writerow(["NOAA_30_N_mean"] +NOAA_30_N_mean.data.flatten().astype(np.str).tolist()) 
        
        writer.writerow(["CCCmaSMHI85_30_N_mean"] + CCCmaSMHI85_30_N_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["CNRMSMHI85_30_N_mean"] +CNRMSMHI85_30_N_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["CSIRO85_30_N_mean"] +CSIRO85_30_N_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["ICHECDMI85_30_N_mean"] +ICHECDMI85_30_N_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["ICHECKNMI85_30_N_mean"] +ICHECKNMI85_30_N_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["ICHECSMHI85_30_N_mean"] +ICHECSMHI85_30_N_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["IPSL85_30_N_mean"] +IPSL85_30_N_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MIROC85_30_N_mean"] +MIROC85_30_N_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MOHCKNMI85_30_N_mean"] +MOHCKNMI85_30_N_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["MOHCSMHI85_30_N_mean"] +MOHCSMHI85_30_N_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["MPISMHI85_30_N_mean"] +MPISMHI85_30_N_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["NCCSMHI85_30_N_mean"] +NCCSMHI85_30_N_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["NOAA85_30_N_mean"] +NOAA85_30_N_mean.data.flatten().astype(np.str).tolist())
        
        writer.writerow(["CCCmaSMHI_50_N_mean"] + CCCmaSMHI_50_N_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["CNRMSMHI_50_N_mean"] +CNRMSMHI_50_N_mean.data.flatten().astype(np.str).tolist())   
        writer.writerow(["CSIRO_50_N_mean"] +CSIRO_50_N_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["ICHECDMI_50_N_mean"] +ICHECDMI_50_N_mean.data.flatten().astype(np.str).tolist())       
        writer.writerow(["ICHECKNMI_50_N_mean"] +ICHECKNMI_50_N_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["ICHECSMHI_50_N_mean"] +ICHECSMHI_50_N_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["IPSL_50_N_mean"] +IPSL_50_N_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MIROC_50_N_mean"] +MIROC_50_N_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MOHCKNMI_50_N_mean"] +MOHCKNMI_50_N_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MOHCSMHI_50_N_mean"] +MOHCSMHI_50_N_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MPISMHI_50_N_mean"] +MPISMHI_50_N_mean.data.flatten().astype(np.str).tolist())        
        writer.writerow(["NCCSMHI_50_N_mean"] +NCCSMHI_50_N_mean.data.flatten().astype(np.str).tolist())       
        writer.writerow(["NOAA_50_N_mean"] +NOAA_50_N_mean.data.flatten().astype(np.str).tolist()) 
        
        writer.writerow(["CCCmaSMHI85_50_N_mean"] + CCCmaSMHI85_50_N_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["CNRMSMHI85_50_N_mean"] +CNRMSMHI85_50_N_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["CSIRO85_50_N_mean"] +CSIRO85_50_N_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["ICHECDMI85_50_N_mean"] +ICHECDMI85_50_N_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["ICHECKNMI85_50_N_mean"] +ICHECKNMI85_50_N_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["ICHECSMHI85_50_N_mean"] +ICHECSMHI85_50_N_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["IPSL85_50_N_mean"] +IPSL85_50_N_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MIROC85_50_N_mean"] +MIROC85_50_N_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MOHCKNMI85_50_N_mean"] +MOHCKNMI85_50_N_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["MOHCSMHI85_50_N_mean"] +MOHCSMHI85_50_N_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["MPISMHI85_50_N_mean"] +MPISMHI85_50_N_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["NCCSMHI85_50_N_mean"] +NCCSMHI85_50_N_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["NOAA85_50_N_mean"] +NOAA85_50_N_mean.data.flatten().astype(np.str).tolist())
        
    #PART 5B: WRITE CENTRAL DATA
        writer.writerow(["CCCmaSMHI_past_C_mean"] + CCCmaSMHI_past_C_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["CNRMSMHI_past_C_mean"] +CNRMSMHI_past_C_mean.data.flatten().astype(np.str).tolist())   
        writer.writerow(["CSIRO_past_C_mean"] +CSIRO_past_C_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["ICHECDMI_past_C_mean"] +ICHECDMI_past_C_mean.data.flatten().astype(np.str).tolist())       
        writer.writerow(["ICHECKNMI_past_C_mean"] +ICHECKNMI_past_C_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["ICHECSMHI_past_C_mean"] +ICHECSMHI_past_C_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["IPSL_past_C_mean"] +IPSL_past_C_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MIROC_past_C_mean"] +MIROC_past_C_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MOHCKNMI_past_C_mean"] +MOHCKNMI_past_C_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MOHCSMHI_past_C_mean"] +MOHCSMHI_past_C_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MPISMHI_past_C_mean"] +MPISMHI_past_C_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["NCCSMHI_past_C_mean"] +NCCSMHI_past_C_mean.data.flatten().astype(np.str).tolist())       
        writer.writerow(["NOAA_past_C_mean"] +NOAA_past_C_mean.data.flatten().astype(np.str).tolist())     
        
        writer.writerow(["CCCmaSMHI_30_C_mean"] + CCCmaSMHI_30_C_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["CNRMSMHI_30_C_mean"] +CNRMSMHI_30_C_mean.data.flatten().astype(np.str).tolist())   
        writer.writerow(["CSIRO_30_C_mean"] +CSIRO_30_C_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["ICHECDMI_30_C_mean"] +ICHECDMI_30_C_mean.data.flatten().astype(np.str).tolist())       
        writer.writerow(["ICHECKNMI_30_C_mean"] +ICHECKNMI_30_C_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["ICHECSMHI_30_C_mean"] +ICHECSMHI_30_C_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["IPSL_30_C_mean"] +IPSL_30_C_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MIROC_30_C_mean"] +MIROC_30_C_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MOHCKNMI_30_C_mean"] +MOHCKNMI_30_C_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MOHCSMHI_30_C_mean"] +MOHCSMHI_30_C_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MPISMHI_30_C_mean"] +MPISMHI_30_C_mean.data.flatten().astype(np.str).tolist())        
        writer.writerow(["NCCSMHI_30_C_mean"] +NCCSMHI_30_C_mean.data.flatten().astype(np.str).tolist())       
        writer.writerow(["NOAA_30_C_mean"] +NOAA_30_C_mean.data.flatten().astype(np.str).tolist()) 
        
        writer.writerow(["CCCmaSMHI85_30_C_mean"] + CCCmaSMHI85_30_C_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["CNRMSMHI85_30_C_mean"] +CNRMSMHI85_30_C_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["CSIRO85_30_C_mean"] +CSIRO85_30_C_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["ICHECDMI85_30_C_mean"] +ICHECDMI85_30_C_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["ICHECKNMI85_30_C_mean"] +ICHECKNMI85_30_C_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["ICHECSMHI85_30_C_mean"] +ICHECSMHI85_30_C_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["IPSL85_30_C_mean"] +IPSL85_30_C_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MIROC85_30_C_mean"] +MIROC85_30_C_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MOHCKNMI85_30_C_mean"] +MOHCKNMI85_30_C_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["MOHCSMHI85_30_C_mean"] +MOHCSMHI85_30_C_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["MPISMHI85_30_C_mean"] +MPISMHI85_30_C_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["NCCSMHI85_30_C_mean"] +NCCSMHI85_30_C_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["NOAA85_30_C_mean"] +NOAA85_30_C_mean.data.flatten().astype(np.str).tolist())
        
        writer.writerow(["CCCmaSMHI_50_C_mean"] + CCCmaSMHI_50_C_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["CNRMSMHI_50_C_mean"] +CNRMSMHI_50_C_mean.data.flatten().astype(np.str).tolist())   
        writer.writerow(["CSIRO_50_C_mean"] +CSIRO_50_C_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["ICHECDMI_50_C_mean"] +ICHECDMI_50_C_mean.data.flatten().astype(np.str).tolist())       
        writer.writerow(["ICHECKNMI_50_C_mean"] +ICHECKNMI_50_C_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["ICHECSMHI_50_C_mean"] +ICHECSMHI_50_C_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["IPSL_50_C_mean"] +IPSL_50_C_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MIROC_50_C_mean"] +MIROC_50_C_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MOHCKNMI_50_C_mean"] +MOHCKNMI_50_C_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MOHCSMHI_50_C_mean"] +MOHCSMHI_50_C_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MPISMHI_50_C_mean"] +MPISMHI_50_C_mean.data.flatten().astype(np.str).tolist())        
        writer.writerow(["NCCSMHI_50_C_mean"] +NCCSMHI_50_C_mean.data.flatten().astype(np.str).tolist())       
        writer.writerow(["NOAA_50_C_mean"] +NOAA_50_C_mean.data.flatten().astype(np.str).tolist()) 
        
        writer.writerow(["CCCmaSMHI85_50_C_mean"] + CCCmaSMHI85_50_C_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["CNRMSMHI85_50_C_mean"] +CNRMSMHI85_50_C_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["CSIRO85_50_C_mean"] +CSIRO85_50_C_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["ICHECDMI85_50_C_mean"] +ICHECDMI85_50_C_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["ICHECKNMI85_50_C_mean"] +ICHECKNMI85_50_C_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["ICHECSMHI85_50_C_mean"] +ICHECSMHI85_50_C_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["IPSL85_50_C_mean"] +IPSL85_50_C_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MIROC85_50_C_mean"] +MIROC85_50_C_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MOHCKNMI85_50_C_mean"] +MOHCKNMI85_50_C_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["MOHCSMHI85_50_C_mean"] +MOHCSMHI85_50_C_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["MPISMHI85_50_C_mean"] +MPISMHI85_50_C_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["NCCSMHI85_50_C_mean"] +NCCSMHI85_50_C_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["NOAA85_50_C_mean"] +NOAA85_50_C_mean.data.flatten().astype(np.str).tolist())  
        
    #PART 5C: WRITE SOUTHERN DATA
        writer.writerow(["CCCmaSMHI_past_S_mean"] + CCCmaSMHI_past_S_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["CNRMSMHI_past_S_mean"] +CNRMSMHI_past_S_mean.data.flatten().astype(np.str).tolist())   
        writer.writerow(["CSIRO_past_S_mean"] +CSIRO_past_S_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["ICHECDMI_past_S_mean"] +ICHECDMI_past_S_mean.data.flatten().astype(np.str).tolist())       
        writer.writerow(["ICHECKNMI_past_S_mean"] +ICHECKNMI_past_S_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["ICHECSMHI_past_S_mean"] +ICHECSMHI_past_S_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["IPSL_past_S_mean"] +IPSL_past_S_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MIROC_past_S_mean"] +MIROC_past_S_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MOHCKNMI_past_S_mean"] +MOHCKNMI_past_S_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MOHCSMHI_past_S_mean"] +MOHCSMHI_past_S_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MPISMHI_past_S_mean"] +MPISMHI_past_S_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["NCCSMHI_past_S_mean"] +NCCSMHI_past_S_mean.data.flatten().astype(np.str).tolist())       
        writer.writerow(["NOAA_past_S_mean"] +NOAA_past_S_mean.data.flatten().astype(np.str).tolist())     
        
        writer.writerow(["CCCmaSMHI_30_S_mean"] + CCCmaSMHI_30_S_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["CNRMSMHI_30_S_mean"] +CNRMSMHI_30_S_mean.data.flatten().astype(np.str).tolist())   
        writer.writerow(["CSIRO_30_S_mean"] +CSIRO_30_S_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["ICHECDMI_30_S_mean"] +ICHECDMI_30_S_mean.data.flatten().astype(np.str).tolist())       
        writer.writerow(["ICHECKNMI_30_S_mean"] +ICHECKNMI_30_S_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["ICHECSMHI_30_S_mean"] +ICHECSMHI_30_S_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["IPSL_30_S_mean"] +IPSL_30_S_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MIROC_30_S_mean"] +MIROC_30_S_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MOHCKNMI_30_S_mean"] +MOHCKNMI_30_S_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MOHCSMHI_30_S_mean"] +MOHCSMHI_30_S_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MPISMHI_30_S_mean"] +MPISMHI_30_S_mean.data.flatten().astype(np.str).tolist())        
        writer.writerow(["NCCSMHI_30_S_mean"] +NCCSMHI_30_S_mean.data.flatten().astype(np.str).tolist())       
        writer.writerow(["NOAA_30_S_mean"] +NOAA_30_S_mean.data.flatten().astype(np.str).tolist()) 
        
        writer.writerow(["CCCmaSMHI85_30_S_mean"] + CCCmaSMHI85_30_S_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["CNRMSMHI85_30_S_mean"] +CNRMSMHI85_30_S_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["CSIRO85_30_S_mean"] +CSIRO85_30_S_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["ICHECDMI85_30_S_mean"] +ICHECDMI85_30_S_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["ICHECKNMI85_30_S_mean"] +ICHECKNMI85_30_S_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["ICHECSMHI85_30_S_mean"] +ICHECSMHI85_30_S_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["IPSL85_30_S_mean"] +IPSL85_30_S_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MIROC85_30_S_mean"] +MIROC85_30_S_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MOHCKNMI85_30_S_mean"] +MOHCKNMI85_30_S_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["MOHCSMHI85_30_S_mean"] +MOHCSMHI85_30_S_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["MPISMHI85_30_S_mean"] +MPISMHI85_30_S_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["NCCSMHI85_30_S_mean"] +NCCSMHI85_30_S_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["NOAA85_30_S_mean"] +NOAA85_30_S_mean.data.flatten().astype(np.str).tolist())
        
        writer.writerow(["CCCmaSMHI_50_S_mean"] + CCCmaSMHI_50_S_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["CNRMSMHI_50_S_mean"] +CNRMSMHI_50_S_mean.data.flatten().astype(np.str).tolist())   
        writer.writerow(["CSIRO_50_S_mean"] +CSIRO_50_S_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["ICHECDMI_50_S_mean"] +ICHECDMI_50_S_mean.data.flatten().astype(np.str).tolist())       
        writer.writerow(["ICHECKNMI_50_S_mean"] +ICHECKNMI_50_S_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["ICHECSMHI_50_S_mean"] +ICHECSMHI_50_S_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["IPSL_50_S_mean"] +IPSL_50_S_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MIROC_50_S_mean"] +MIROC_50_S_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MOHCKNMI_50_S_mean"] +MOHCKNMI_50_S_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MOHCSMHI_50_S_mean"] +MOHCSMHI_50_S_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MPISMHI_50_S_mean"] +MPISMHI_50_S_mean.data.flatten().astype(np.str).tolist())        
        writer.writerow(["NCCSMHI_50_S_mean"] +NCCSMHI_50_S_mean.data.flatten().astype(np.str).tolist())       
        writer.writerow(["NOAA_50_S_mean"] +NOAA_50_S_mean.data.flatten().astype(np.str).tolist()) 
        
        writer.writerow(["CCCmaSMHI85_50_S_mean"] + CCCmaSMHI85_50_S_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["CNRMSMHI85_50_S_mean"] +CNRMSMHI85_50_S_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["CSIRO85_50_S_mean"] +CSIRO85_50_S_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["ICHECDMI85_50_S_mean"] +ICHECDMI85_50_S_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["ICHECKNMI85_50_S_mean"] +ICHECKNMI85_50_S_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["ICHECSMHI85_50_S_mean"] +ICHECSMHI85_50_S_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["IPSL85_50_S_mean"] +IPSL85_50_S_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MIROC85_50_S_mean"] +MIROC85_50_S_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MOHCKNMI85_50_S_mean"] +MOHCKNMI85_50_S_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["MOHCSMHI85_50_S_mean"] +MOHCSMHI85_50_S_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["MPISMHI85_50_S_mean"] +MPISMHI85_50_S_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["NCCSMHI85_50_S_mean"] +NCCSMHI85_50_S_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["NOAA85_50_S_mean"] +NOAA85_50_S_mean.data.flatten().astype(np.str).tolist())
        

if __name__ == '__main__':
    main()
        
        