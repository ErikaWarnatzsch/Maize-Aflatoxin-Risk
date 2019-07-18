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
    #-------------------------------------------------------------------------
    #PART 1: LOAD and FORMAT ALL PAST MODELS   
    CCCmaCanRCM_past = '/exports/csce/datastore/geos/users/s0899345/AFR_44_pr/Historical_daily/pr_AFR-44_CCCma-CanESM2_historical_r1i1p1_CCCma-CanRCM4_r2_day_19710101-20001231.nc'
    CCCmaSMHI_past = '/exports/csce/datastore/geos/users/s0899345/AFR_44_pr/Historical_daily/pr_AFR-44_CCCma-CanESM2_historical_r1i1p1_SMHI-RCA4_v1_day_19710101-20001231.nc'   
    CNRM_past = '/exports/csce/datastore/geos/users/s0899345/AFR_44_pr/Historical_daily/pr_AFR-44_CNRM-CERFACS-CNRM-CM5_historical_r1i1p1_CLMcom-CCLM4-8-17_v1_day_19710101-20001231.nc'
    CNRMSMHI_past = '/exports/csce/datastore/geos/users/s0899345/AFR_44_pr/Historical_daily/pr_AFR-44_CNRM-CERFACS-CNRM-CM5_historical_r1i1p1_SMHI-RCA4_v1_day_19710101-20001231.nc'
    CSIRO_past = '/exports/csce/datastore/geos/users/s0899345/AFR_44_pr/Historical_daily/pr_AFR-44_CSIRO-QCCCE-CSIRO-Mk3-6-0_historical_r1i1p1_SMHI-RCA4_v1_day_19710101-20001231.nc'
    ICHECDMI_past = '/exports/csce/datastore/geos/users/s0899345/AFR_44_pr/Historical_daily/pr_AFR-44_ICHEC-EC-EARTH_historical_r3i1p1_DMI-HIRHAM5_v2_day_19710101-20001231.nc'   
    ICHECCCLM_past = '/exports/csce/datastore/geos/users/s0899345/AFR_44_pr/Historical_daily/pr_AFR-44_ICHEC-EC-EARTH_historical_r12i1p1_CLMcom-CCLM4-8-17_v1_day_19710101-20001231.nc'    
    ICHECKNMI_past = '/exports/csce/datastore/geos/users/s0899345/AFR_44_pr/Historical_daily/pr_AFR-44_ICHEC-EC-EARTH_historical_r1i1p1_KNMI-RACMO22T_v1_day_19710101-20001231.nc'
    ICHECMPI_past = '/exports/csce/datastore/geos/users/s0899345/AFR_44_pr/Historical_daily/pr_AFR-44_ICHEC-EC-EARTH_historical_r12i1p1_MPI-CSC-REMO2009_v1_day_19710101-20001231.nc'
    ICHECSMHI_past = '/exports/csce/datastore/geos/users/s0899345/AFR_44_pr/Historical_daily/pr_AFR-44_ICHEC-EC-EARTH_historical_r12i1p1_SMHI-RCA4_v1_day_19710101-20001231.nc'
    IPSL_past = '/exports/csce/datastore/geos/users/s0899345/AFR_44_pr/Historical_daily/pr_AFR-44_IPSL-IPSL-CM5A-MR_historical_r1i1p1_SMHI-RCA4_v1_day_19710101-20001231.nc'
    MIROC_past =  '/exports/csce/datastore/geos/users/s0899345/AFR_44_pr/Historical_daily/pr_AFR-44_MIROC-MIROC5_historical_r1i1p1_SMHI-RCA4_v1_day_19710101-20001231.nc' 
    MOHCCCLM_past = '/exports/csce/datastore/geos/users/s0899345/AFR_44_pr/Historical_daily/pr_AFR-44_MOHC-HadGEM2-ES_historical_r1i1p1_CLMcom-CCLM4-8-17_v1_day_19710101-20001231.nc' 
    MOHCKNMI_past = '/exports/csce/datastore/geos/users/s0899345/AFR_44_pr/Historical_daily/pr_AFR-44_MOHC-HadGEM2-ES_historical_r1i1p1_KNMI-RACMO22T_v2_day_19710101-20001231.nc'
    MOHCSMHI_past = '/exports/csce/datastore/geos/users/s0899345/AFR_44_pr/Historical_daily/pr_AFR-44_MOHC-HadGEM2-ES_historical_r1i1p1_SMHI-RCA4_v1_day_19710101-20001231.nc'
    MPICCLM_past = '/exports/csce/datastore/geos/users/s0899345/AFR_44_pr/Historical_daily/pr_AFR-44_MPI-M-MPI-ESM-LR_historical_r1i1p1_CLMcom-CCLM4-8-17_v1_day_19710101-20001231.nc'     
    MPIREMO_past = '/exports/csce/datastore/geos/users/s0899345/AFR_44_pr/Historical_daily/pr_AFR-44_MPI-M-MPI-ESM-LR_historical_r1i1p1_MPI-CSC-REMO2009_v1_day_19710101-20001231.nc'    
    MPISMHI_past = '/exports/csce/datastore/geos/users/s0899345/AFR_44_pr/Historical_daily/pr_AFR-44_MPI-M-MPI-ESM-LR_historical_r1i1p1_SMHI-RCA4_v1_day_19710101-20001231.nc'
    NCCSMHI_past = '/exports/csce/datastore/geos/users/s0899345/AFR_44_pr/Historical_daily/pr_AFR-44_NCC-NorESM1-M_historical_r1i1p1_SMHI-RCA4_v1_day_19710101-20001231.nc'   
    NOAA_past = '/exports/csce/datastore/geos/users/s0899345/AFR_44_pr/Historical_daily/pr_AFR-44_NOAA-GFDL-GFDL-ESM2M_historical_r1i1p1_SMHI-RCA4_v1_day_19710101-20001231.nc'   
    
    #Load exactly one cube from given file
    CCCmaCanRCM_past =  iris.load_cube(CCCmaCanRCM_past)
    CCCmaSMHI_past =  iris.load_cube(CCCmaSMHI_past)
    CNRM_past =  iris.load_cube(CNRM_past)
    CNRMSMHI_past =  iris.load_cube(CNRMSMHI_past)
    CSIRO_past =  iris.load_cube(CSIRO_past)
    ICHECDMI_past =  iris.load_cube(ICHECDMI_past, 'precipitation_flux')
    ICHECCCLM_past =  iris.load_cube(ICHECCCLM_past)
    ICHECKNMI_past =  iris.load_cube(ICHECKNMI_past)
    ICHECMPI_past =  iris.load_cube(ICHECMPI_past)
    ICHECSMHI_past =  iris.load_cube(ICHECSMHI_past)
    IPSL_past =  iris.load_cube(IPSL_past)
    MIROC_past =  iris.load_cube(MIROC_past)
    MOHCCCLM_past =  iris.load_cube(MOHCCCLM_past)
    MOHCKNMI_past =  iris.load_cube(MOHCKNMI_past)
    MOHCSMHI_past =  iris.load_cube(MOHCSMHI_past)
    MPICCLM_past =  iris.load_cube(MPICCLM_past)
    MPIREMO_past =  iris.load_cube(MPIREMO_past)
    MPISMHI_past =  iris.load_cube(MPISMHI_past)
    NCCSMHI_past =  iris.load_cube(NCCSMHI_past)
    NOAA_past =  iris.load_cube(NOAA_past)
    
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
    IPSL_past.coord('latitude').guess_bounds()
    MIROC_past.coord('latitude').guess_bounds()
    MOHCCCLM_past.coord('latitude').guess_bounds()
    MOHCKNMI_past.coord('latitude').guess_bounds() 
    MOHCSMHI_past.coord('latitude').guess_bounds()
    MPICCLM_past.coord('latitude').guess_bounds()
    MPIREMO_past.coord('latitude').guess_bounds()
    MPISMHI_past.coord('latitude').guess_bounds()
    NCCSMHI_past.coord('latitude').guess_bounds()
    NOAA_past.coord('latitude').guess_bounds()
    
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
    IPSL_past.coord('longitude').guess_bounds()
    MIROC_past.coord('longitude').guess_bounds()
    MOHCCCLM_past.coord('longitude').guess_bounds()
    MOHCKNMI_past.coord('longitude').guess_bounds() 
    MOHCSMHI_past.coord('longitude').guess_bounds()
    MPICCLM_past.coord('longitude').guess_bounds()
    MPIREMO_past.coord('longitude').guess_bounds()
    MPISMHI_past.coord('longitude').guess_bounds()
    NCCSMHI_past.coord('longitude').guess_bounds()
    NOAA_past.coord('longitude').guess_bounds()
    
    
    #-------------------------------------------------------------------------
    #PART 2: LOAD and FORMAT PROJECTED MODELS   
    CCCmaCanRCM= '/exports/csce/datastore/geos/users/s0899345/AFR_44_pr/RCP_4.5/pr_AFR-44_CCCma-CanESM2_rcp45_r1i1p1_CCCma-CanRCM4_r2_day_20060101-20701231.nc'
    CCCmaSMHI= '/exports/csce/datastore/geos/users/s0899345/AFR_44_pr/RCP_4.5/pr_AFR-44_CCCma-CanESM2_rcp45_r1i1p1_SMHI-RCA4_v1_day_20060101-20701231.nc'   
    CNRM= '/exports/csce/datastore/geos/users/s0899345/AFR_44_pr/RCP_4.5/pr_AFR-44_CNRM-CERFACS-CNRM-CM5_rcp45_r1i1p1_CLMcom-CCLM4-8-17_v1_day_20060101-20701231.nc'
    CNRMSMHI= '/exports/csce/datastore/geos/users/s0899345/AFR_44_pr/RCP_4.5/pr_AFR-44_CNRM-CERFACS-CNRM-CM5_rcp45_r1i1p1_SMHI-RCA4_v1_day_20060101-20701231.nc'
    CSIRO = '/exports/csce/datastore/geos/users/s0899345/AFR_44_pr/RCP_4.5/pr_AFR-44_CSIRO-QCCCE-CSIRO-Mk3-6-0_rcp45_r1i1p1_SMHI-RCA4_v1_day_20060101-20701231.nc'
    ICHECDMI = '/exports/csce/datastore/geos/users/s0899345/AFR_44_pr/RCP_4.5/pr_AFR-44_ICHEC-EC-EARTH_rcp45_r3i1p1_DMI-HIRHAM5_v2_day_20060101-20701231.nc'   
    ICHECCCLM = '/exports/csce/datastore/geos/users/s0899345/AFR_44_pr/RCP_4.5/pr_AFR-44_ICHEC-EC-EARTH_rcp45_r12i1p1_CLMcom-CCLM4-8-17_v1_day_20060101-20701231.nc'    
    ICHECKNMI = '/exports/csce/datastore/geos/users/s0899345/AFR_44_pr/RCP_4.5/pr_AFR-44_ICHEC-EC-EARTH_rcp45_r1i1p1_KNMI-RACMO22T_v1_day_20060101-20701231.nc'
    ICHECMPI = '/exports/csce/datastore/geos/users/s0899345/AFR_44_pr/RCP_4.5/pr_AFR-44_ICHEC-EC-EARTH_rcp45_r12i1p1_MPI-CSC-REMO2009_v1_day_20060101-20701231.nc'
    ICHECSMHI = '/exports/csce/datastore/geos/users/s0899345/AFR_44_pr/RCP_4.5/pr_AFR-44_ICHEC-EC-EARTH_rcp45_r12i1p1_SMHI-RCA4_v1_day_20060101-20701231.nc'
    IPSL = '/exports/csce/datastore/geos/users/s0899345/AFR_44_pr/RCP_4.5/pr_AFR-44_IPSL-IPSL-CM5A-MR_rcp45_r1i1p1_SMHI-RCA4_v1_day_20060101-20701231.nc'
    MIROC =  '/exports/csce/datastore/geos/users/s0899345/AFR_44_pr/RCP_4.5/pr_AFR-44_MIROC-MIROC5_rcp45_r1i1p1_SMHI-RCA4_v1_day_20060101-20701231.nc' 
    MOHCCCLM = '/exports/csce/datastore/geos/users/s0899345/AFR_44_pr/RCP_4.5/pr_AFR-44_MOHC-HadGEM2-ES_rcp45_r1i1p1_CLMcom-CCLM4-8-17_v1_day_20060101-20701231.nc' 
    MOHCKNMI = '/exports/csce/datastore/geos/users/s0899345/AFR_44_pr/RCP_4.5/pr_AFR-44_MOHC-HadGEM2-ES_rcp45_r1i1p1_KNMI-RACMO22T_v2_day_20060101-20701231.nc'
    MOHCSMHI = '/exports/csce/datastore/geos/users/s0899345/AFR_44_pr/RCP_4.5/pr_AFR-44_MOHC-HadGEM2-ES_rcp45_r1i1p1_SMHI-RCA4_v1_day_20060101-20701231.nc'
    MPICCLM = '/exports/csce/datastore/geos/users/s0899345/AFR_44_pr/RCP_4.5/pr_AFR-44_MPI-M-MPI-ESM-LR_rcp45_r1i1p1_CLMcom-CCLM4-8-17_v1_day_20060101-20701231.nc'     
    MPIREMO = '/exports/csce/datastore/geos/users/s0899345/AFR_44_pr/RCP_4.5/pr_AFR-44_MPI-M-MPI-ESM-LR_rcp45_r1i1p1_MPI-CSC-REMO2009_v1_day_20060101-20701231.nc'    
    MPISMHI = '/exports/csce/datastore/geos/users/s0899345/AFR_44_pr/RCP_4.5/pr_AFR-44_MPI-M-MPI-ESM-LR_rcp45_r1i1p1_SMHI-RCA4_v1_day_20060101-20701231.nc'   
    NCCSMHI = '/exports/csce/datastore/geos/users/s0899345/AFR_44_pr/RCP_4.5/pr_AFR-44_NCC-NorESM1-M_rcp45_r1i1p1_SMHI-RCA4_v1_day_20060101-20701231.nc'   
    NOAA = '/exports/csce/datastore/geos/users/s0899345/AFR_44_pr/RCP_4.5/pr_AFR-44_NOAA-GFDL-GFDL-ESM2M_rcp45_r1i1p1_SMHI-RCA4_v1_day_20060101-20701231.nc'   
    
    CCCmaCanRCM85 = '/exports/csce/datastore/geos/users/s0899345/AFR_44_pr/RCP_8.5/pr_AFR-44_CCCma-CanESM2_rcp85_r1i1p1_CCCma-CanRCM4_r2_day_20060101-20701231.nc'
    CCCmaSMHI85 = '/exports/csce/datastore/geos/users/s0899345/AFR_44_pr/RCP_8.5/pr_AFR-44_CCCma-CanESM2_rcp85_r1i1p1_SMHI-RCA4_v1_day_20060101-20701231.nc'   
    CNRM85 = '/exports/csce/datastore/geos/users/s0899345/AFR_44_pr/RCP_8.5/pr_AFR-44_CNRM-CERFACS-CNRM-CM5_rcp85_r1i1p1_CLMcom-CCLM4-8-17_v1_day_20060101-20701231.nc'
    CNRMSMHI85 = '/exports/csce/datastore/geos/users/s0899345/AFR_44_pr/RCP_8.5/pr_AFR-44_CNRM-CERFACS-CNRM-CM5_rcp85_r1i1p1_SMHI-RCA4_v1_day_20060101-20701231.nc'
    CSIRO85 = '/exports/csce/datastore/geos/users/s0899345/AFR_44_pr/RCP_8.5/pr_AFR-44_CSIRO-QCCCE-CSIRO-Mk3-6-0_rcp85_r1i1p1_SMHI-RCA4_v1_day_20060101-20701231.nc'
    ICHECDMI85 = '/exports/csce/datastore/geos/users/s0899345/AFR_44_pr/RCP_8.5/pr_AFR-44_ICHEC-EC-EARTH_rcp85_r3i1p1_DMI-HIRHAM5_v2_day_20060101-20701231.nc'   
    ICHECCCLM85 = '/exports/csce/datastore/geos/users/s0899345/AFR_44_pr/RCP_8.5/pr_AFR-44_ICHEC-EC-EARTH_rcp85_r12i1p1_CLMcom-CCLM4-8-17_v1_day_20060101-20701231.nc'    
    ICHECKNMI85 = '/exports/csce/datastore/geos/users/s0899345/AFR_44_pr/RCP_8.5/pr_AFR-44_ICHEC-EC-EARTH_rcp85_r1i1p1_KNMI-RACMO22T_v1_day_20060101-20701231.nc'
    ICHECMPI85 = '/exports/csce/datastore/geos/users/s0899345/AFR_44_pr/RCP_8.5/pr_AFR-44_ICHEC-EC-EARTH_rcp85_r12i1p1_MPI-CSC-REMO2009_v1_day_20060101-20701231.nc'
    ICHECSMHI85 = '/exports/csce/datastore/geos/users/s0899345/AFR_44_pr/RCP_8.5/pr_AFR-44_ICHEC-EC-EARTH_rcp85_r12i1p1_SMHI-RCA4_v1_day_20060101-20701231.nc'
    IPSL85 = '/exports/csce/datastore/geos/users/s0899345/AFR_44_pr/RCP_8.5/pr_AFR-44_IPSL-IPSL-CM5A-MR_rcp85_r1i1p1_SMHI-RCA4_v1_day_20060101-20701231.nc'
    MIROC85 =  '/exports/csce/datastore/geos/users/s0899345/AFR_44_pr/RCP_8.5/pr_AFR-44_MIROC-MIROC5_rcp85_r1i1p1_SMHI-RCA4_v1_day_20060101-20701231.nc' 
    MOHCCCLM85 = '/exports/csce/datastore/geos/users/s0899345/AFR_44_pr/RCP_8.5/pr_AFR-44_MOHC-HadGEM2-ES_rcp85_r1i1p1_CLMcom-CCLM4-8-17_v1_day_20060101-20701231.nc' 
    MOHCKNMI85 = '/exports/csce/datastore/geos/users/s0899345/AFR_44_pr/RCP_8.5/pr_AFR-44_MOHC-HadGEM2-ES_rcp85_r1i1p1_KNMI-RACMO22T_v2_day_20060101-20701231.nc'
    MOHCSMHI85 = '/exports/csce/datastore/geos/users/s0899345/AFR_44_pr/RCP_8.5/pr_AFR-44_MOHC-HadGEM2-ES_rcp85_r1i1p1_SMHI-RCA4_v1_day_20060101-20701231.nc'
    MPICCLM85 = '/exports/csce/datastore/geos/users/s0899345/AFR_44_pr/RCP_8.5/pr_AFR-44_MPI-M-MPI-ESM-LR_rcp85_r1i1p1_CLMcom-CCLM4-8-17_v1_day_20060101-20701231.nc'     
    MPIREMO85 = '/exports/csce/datastore/geos/users/s0899345/AFR_44_pr/RCP_8.5/pr_AFR-44_MPI-M-MPI-ESM-LR_rcp85_r1i1p1_MPI-CSC-REMO2009_v1_day_20060101-20701231.nc'    
    MPISMHI85 = '/exports/csce/datastore/geos/users/s0899345/AFR_44_pr/RCP_8.5/pr_AFR-44_MPI-M-MPI-ESM-LR_rcp85_r1i1p1_SMHI-RCA4_v1_day_20060101-20701231.nc'
    NCCSMHI85 = '/exports/csce/datastore/geos/users/s0899345/AFR_44_pr/RCP_8.5/pr_AFR-44_NCC-NorESM1-M_rcp85_r1i1p1_SMHI-RCA4_v1_day_20060101-20701231.nc'   
    NOAA85 = '/exports/csce/datastore/geos/users/s0899345/AFR_44_pr/RCP_8.5/pr_AFR-44_NOAA-GFDL-GFDL-ESM2M_rcp85_r1i1p1_SMHI-RCA4_v1_day_20060101-20701231.nc'  
    
    #Load exactly one cube from given file
    CCCmaCanRCM = iris.load_cube(CCCmaCanRCM)
    CCCmaSMHI = iris.load_cube(CCCmaSMHI)
    CNRM = iris.load_cube(CNRM)
    CNRMSMHI = iris.load_cube(CNRMSMHI)
    CSIRO = iris.load_cube(CSIRO)
    ICHECDMI = iris.load_cube(ICHECDMI, 'precipitation_flux')
    ICHECCCLM = iris.load_cube(ICHECCCLM)
    ICHECKNMI = iris.load_cube(ICHECKNMI)
    ICHECMPI = iris.load_cube(ICHECMPI)
    ICHECSMHI = iris.load_cube(ICHECSMHI)
    IPSL = iris.load_cube(IPSL)
    MIROC = iris.load_cube(MIROC)
    MOHCCCLM = iris.load_cube(MOHCCCLM)
    MOHCKNMI = iris.load_cube(MOHCKNMI)
    MOHCSMHI = iris.load_cube(MOHCSMHI)
    MPICCLM = iris.load_cube(MPICCLM)
    MPIREMO = iris.load_cube(MPIREMO)
    MPISMHI = iris.load_cube(MPISMHI)
    NCCSMHI = iris.load_cube(NCCSMHI)
    NOAA = iris.load_cube(NOAA)
    
    CCCmaCanRCM85 = iris.load_cube(CCCmaCanRCM85)
    CCCmaSMHI85 = iris.load_cube(CCCmaSMHI85)
    CNRM85 = iris.load_cube(CNRM85)
    CNRMSMHI85 = iris.load_cube(CNRMSMHI85)
    CSIRO85 = iris.load_cube(CSIRO85)
    ICHECDMI85 = iris.load_cube(ICHECDMI85, 'precipitation_flux')
    ICHECCCLM85 = iris.load_cube(ICHECCCLM85)
    ICHECKNMI85 = iris.load_cube(ICHECKNMI85)
    ICHECMPI85 = iris.load_cube(ICHECMPI85)
    ICHECSMHI85 = iris.load_cube(ICHECSMHI85)
    IPSL85 = iris.load_cube(IPSL85)
    MIROC85 = iris.load_cube(MIROC85)
    MOHCCCLM85 = iris.load_cube(MOHCCCLM85)
    MOHCKNMI85 = iris.load_cube(MOHCKNMI85)
    MOHCSMHI85 = iris.load_cube(MOHCSMHI85)
    MPICCLM85 = iris.load_cube(MPICCLM85)
    MPIREMO85 = iris.load_cube(MPIREMO85)
    MPISMHI85 = iris.load_cube(MPISMHI85)
    NCCSMHI85 = iris.load_cube(NCCSMHI85)
    NOAA85 = iris.load_cube(NOAA85)
    
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
    IPSL.coord('latitude').guess_bounds()
    MIROC.coord('latitude').guess_bounds()
    MOHCCCLM.coord('latitude').guess_bounds()
    MOHCKNMI.coord('latitude').guess_bounds() 
    MOHCSMHI.coord('latitude').guess_bounds()
    MPICCLM.coord('latitude').guess_bounds()
    MPIREMO.coord('latitude').guess_bounds()
    MPISMHI.coord('latitude').guess_bounds()
    NCCSMHI.coord('latitude').guess_bounds()
    NOAA.coord('latitude').guess_bounds()
    
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
    IPSL85.coord('latitude').guess_bounds()
    MIROC85.coord('latitude').guess_bounds()
    MOHCCCLM85.coord('latitude').guess_bounds()
    MOHCKNMI85.coord('latitude').guess_bounds() 
    MOHCSMHI85.coord('latitude').guess_bounds()
    MPICCLM85.coord('latitude').guess_bounds()
    MPIREMO85.coord('latitude').guess_bounds()
    MPISMHI85.coord('latitude').guess_bounds()
    NCCSMHI85.coord('latitude').guess_bounds()
    NOAA85.coord('latitude').guess_bounds()
    
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
    IPSL.coord('longitude').guess_bounds()
    MIROC.coord('longitude').guess_bounds()
    MOHCCCLM.coord('longitude').guess_bounds()
    MOHCKNMI.coord('longitude').guess_bounds() 
    MOHCSMHI.coord('longitude').guess_bounds()
    MPICCLM.coord('longitude').guess_bounds()
    MPIREMO.coord('longitude').guess_bounds()
    MPISMHI.coord('longitude').guess_bounds()
    NCCSMHI.coord('longitude').guess_bounds()
    NOAA.coord('longitude').guess_bounds()
    
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
    IPSL85.coord('longitude').guess_bounds()
    MIROC85.coord('longitude').guess_bounds()
    MOHCCCLM85.coord('longitude').guess_bounds()
    MOHCKNMI85.coord('longitude').guess_bounds() 
    MOHCSMHI85.coord('longitude').guess_bounds()
    MPICCLM85.coord('longitude').guess_bounds()
    MPIREMO85.coord('longitude').guess_bounds()
    MPISMHI85.coord('longitude').guess_bounds()
    NCCSMHI85.coord('longitude').guess_bounds()
    NOAA85.coord('longitude').guess_bounds()
    
    
    #-------------------------------------------------------------------------
    #PART 3: LOAD AND FORMAT OBSERVED DATA
    #bring in all the files we need and give them a name
    CRU= '/exports/csce/datastore/geos/users/s0899345/Actual_Data/cru_ts4.00.1901.2015.pre.dat.nc'
    UDel= '/exports/csce/datastore/geos/users/s0899345/Actual_Data/UDel_precip.mon.total.v401.nc'
    GPCC= '/exports/csce/datastore/geos/users/s0899345/Actual_Data/ESRL_PSD_GPCC_precip.mon.combined.total.v7.nc'
    
    #Load exactly one cube from given file
    CRU = iris.load_cube(CRU, 'precipitation')
    UDel = iris.load_cube(UDel)
    GPCC = iris.load_cube(GPCC)
    
    #guess bounds  
    CRU.coord('latitude').guess_bounds()
    UDel.coord('latitude').guess_bounds()
    GPCC.coord('latitude').guess_bounds()
    
    CRU.coord('longitude').guess_bounds()
    UDel.coord('longitude').guess_bounds()
    GPCC.coord('longitude').guess_bounds()
    
    
    #-------------------------------------------------------------------------
    #PART 4: FORMAT DATA GENERAL
    #Convert units to match, CORDEX data in precipitation_flux (kg m-2 s-1) but want all data in precipitation rate per day (mm day-1). Not all of the CORDEX models use the same calendar, so they have been split by calendar type
    #Since 1 kg of rain spread over 1 m of surface is 1mm in thickness, and there are 60*60*24*365.25=31557600 seconds in a year and 365 days in the year, the conversion is:
    Convert=31557600/365
       
    CCCmaCanRCM_past = CCCmaCanRCM_past*Convert
    CCCmaSMHI_past = CCCmaSMHI_past*Convert
    CSIRO_past = CSIRO_past*Convert
    IPSL_past = IPSL_past*Convert
    MIROC_past = MIROC_past*Convert
    NCCSMHI_past = NCCSMHI_past*Convert
    NOAA_past = NOAA_past*Convert
    
    CCCmaCanRCM = CCCmaCanRCM*Convert
    CCCmaSMHI = CCCmaSMHI*Convert
    CSIRO = CSIRO*Convert
    IPSL = IPSL*Convert
    MIROC = MIROC*Convert
    NCCSMHI = NCCSMHI*Convert
    NOAA = NOAA*Convert
    
    CCCmaCanRCM85 = CCCmaCanRCM85*Convert
    CCCmaSMHI85 = CCCmaSMHI85*Convert
    CSIRO85 = CSIRO85*Convert
    IPSL85 = IPSL85*Convert
    MIROC85 = MIROC85*Convert
    NCCSMHI85 = NCCSMHI85*Convert
    NOAA85 = NOAA85*Convert
    
    #Since 1 kg of rain spread over 1 m of surface is 1mm in thickness, and there are 60*60*24*365.25=31557600 seconds in a year and 365.25 days in the year, the conversion is:
    Convert=31557600/365.25
    
    CNRM_past = CNRM_past*Convert
    CNRMSMHI_past = CNRMSMHI_past*Convert 
    ICHECDMI_past = ICHECDMI_past*Convert
    ICHECCCLM_past = ICHECCCLM_past*Convert
    ICHECKNMI_past = ICHECKNMI_past*Convert
    ICHECMPI_past = ICHECMPI_past*Convert
    ICHECSMHI_past = ICHECSMHI_past*Convert
    MPICCLM_past = MPICCLM_past*Convert
    MPIREMO_past = MPIREMO_past*Convert
    MPISMHI_past = MPISMHI_past*Convert
    
    CNRM = CNRM*Convert
    CNRMSMHI = CNRMSMHI*Convert
    ICHECDMI = ICHECDMI*Convert
    ICHECCCLM = ICHECCCLM*Convert
    ICHECKNMI = ICHECKNMI*Convert
    ICHECMPI = ICHECMPI*Convert
    ICHECSMHI = ICHECSMHI*Convert
    MPICCLM = MPICCLM*Convert
    MPIREMO = MPIREMO*Convert
    MPISMHI = MPISMHI*Convert
    
    CNRM85 = CNRM85*Convert
    CNRMSMHI85 = CNRMSMHI85*Convert
    ICHECDMI85 = ICHECDMI85*Convert
    ICHECCCLM85 = ICHECCCLM85*Convert
    ICHECKNMI85 = ICHECKNMI85*Convert
    ICHECMPI85 = ICHECMPI85*Convert
    ICHECSMHI85 = ICHECSMHI85*Convert
    MPICCLM85 = MPICCLM85*Convert
    MPIREMO85 = MPIREMO85*Convert
    MPISMHI85 = MPISMHI85*Convert
    
    #Since 1 kg of rain spread over 1 m of surface is 1mm in thickness, and there are 60*60*24*365.25=31557600 seconds in a year and 360 days in the year, the conversion is:
    Convert=31557600/360
    
    MOHCCCLM_past = MOHCCCLM_past*Convert
    MOHCKNMI_past = MOHCKNMI_past*Convert
    MOHCSMHI_past = MOHCSMHI_past*Convert
    
    MOHCCCLM = MOHCCCLM*Convert
    MOHCKNMI = MOHCKNMI*Convert
    MOHCSMHI = MOHCSMHI*Convert
    
    MOHCCCLM85 = MOHCCCLM85*Convert
    MOHCKNMI85 = MOHCKNMI85*Convert
    MOHCSMHI85 = MOHCSMHI85*Convert
    
    #Convert units to match, UDel data in cm per month, but want precipitation rate in mm per day.
    #Since there are 10mm in a cm, 12 months in a year and 365 days in a year, the conversion is:
    Convert=(10*12)/365
    UDel = UDel*Convert
 
    #Convert units to match, CRU and GPCC data are in mm/month, but want precipitation rate in mm per day. 
    #Since there are 12 months in the year and 365 days in a year, the conversion is:
    Convert=12/365
    CRU = CRU*Convert
    GPCC = GPCC*Convert
    
    #rename units to match
    CRU.units = Unit('mm day-1') 
    UDel.units = Unit('mm day-1') 
    GPCC.units = Unit('mm day-1') 
    
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
    iriscc.add_day_of_year(IPSL_past, 'time')
    iriscc.add_day_of_year(MIROC_past, 'time')
    iriscc.add_day_of_year(MOHCCCLM_past, 'time')
    iriscc.add_day_of_year(MOHCKNMI_past, 'time')
    iriscc.add_day_of_year(MOHCSMHI_past, 'time')
    iriscc.add_day_of_year(MPICCLM_past, 'time')
    iriscc.add_day_of_year(MPIREMO_past, 'time')
    iriscc.add_day_of_year(MPISMHI_past, 'time')
    iriscc.add_day_of_year(NCCSMHI_past, 'time')
    iriscc.add_day_of_year(NOAA_past, 'time')
    
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
    iriscc.add_day_of_year(IPSL, 'time')
    iriscc.add_day_of_year(MIROC, 'time')
    iriscc.add_day_of_year(MOHCCCLM, 'time')
    iriscc.add_day_of_year(MOHCKNMI, 'time')
    iriscc.add_day_of_year(MOHCSMHI, 'time')
    iriscc.add_day_of_year(MPICCLM, 'time')
    iriscc.add_day_of_year(MPIREMO, 'time')
    iriscc.add_day_of_year(MPISMHI, 'time')
    iriscc.add_day_of_year(NCCSMHI, 'time')
    iriscc.add_day_of_year(NOAA, 'time')
    
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
    iriscc.add_day_of_year(IPSL85, 'time')
    iriscc.add_day_of_year(MIROC85, 'time')
    iriscc.add_day_of_year(MOHCCCLM85, 'time')
    iriscc.add_day_of_year(MOHCKNMI85, 'time')
    iriscc.add_day_of_year(MOHCSMHI85, 'time')
    iriscc.add_day_of_year(MPICCLM85, 'time')
    iriscc.add_day_of_year(MPIREMO85, 'time')
    iriscc.add_day_of_year(MPISMHI85, 'time')
    iriscc.add_day_of_year(NCCSMHI85, 'time')
    iriscc.add_day_of_year(NOAA85, 'time')
    
    iriscc.add_day_of_year(CRU, 'time')
    iriscc.add_day_of_year(UDel, 'time')
    iriscc.add_day_of_year(GPCC, 'time')
    
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
    iriscc.add_year(IPSL_past, 'time')
    iriscc.add_year(MIROC_past, 'time')
    iriscc.add_year(MOHCCCLM_past, 'time')
    iriscc.add_year(MOHCKNMI_past, 'time')
    iriscc.add_year(MOHCSMHI_past, 'time')
    iriscc.add_year(MPICCLM_past, 'time')
    iriscc.add_year(MPIREMO_past, 'time')
    iriscc.add_year(MPISMHI_past, 'time')
    iriscc.add_year(NCCSMHI_past, 'time')
    iriscc.add_year(NOAA_past, 'time')
    
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
    iriscc.add_year(IPSL, 'time')
    iriscc.add_year(MIROC, 'time')
    iriscc.add_year(MOHCCCLM, 'time')
    iriscc.add_year(MOHCKNMI, 'time')
    iriscc.add_year(MOHCSMHI, 'time')
    iriscc.add_year(MPICCLM, 'time')
    iriscc.add_year(MPIREMO, 'time')
    iriscc.add_year(MPISMHI, 'time')
    iriscc.add_year(NCCSMHI, 'time')
    iriscc.add_year(NOAA, 'time')
    
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
    iriscc.add_year(IPSL85, 'time')
    iriscc.add_year(MIROC85, 'time')
    iriscc.add_year(MOHCCCLM85, 'time')
    iriscc.add_year(MOHCKNMI85, 'time')
    iriscc.add_year(MOHCSMHI85, 'time')
    iriscc.add_year(MPICCLM85, 'time')
    iriscc.add_year(MPIREMO85, 'time')
    iriscc.add_year(MPISMHI85, 'time')
    iriscc.add_year(NCCSMHI85, 'time')
    iriscc.add_year(NOAA85, 'time')

    iriscc.add_year(CRU, 'time')
    iriscc.add_year(UDel, 'time')
    iriscc.add_year(GPCC, 'time')
    
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
    IPSL_past =  IPSL_past.extract(t_constraint_past)
    MIROC_past =  MIROC_past.extract(t_constraint_past)
    MOHCCCLM_past =  MOHCCCLM_past.extract(t_constraint_past)
    MOHCKNMI_past =  MOHCKNMI_past.extract(t_constraint_past)
    MOHCSMHI_past =  MOHCSMHI_past.extract(t_constraint_past)
    MPICCLM_past =  MPICCLM_past.extract(t_constraint_past)
    MPIREMO_past =  MPIREMO_past.extract(t_constraint_past)
    MPISMHI_past =  MPISMHI_past.extract(t_constraint_past)
    NCCSMHI_past =  NCCSMHI_past.extract(t_constraint_past)
    NOAA_past =  NOAA_past.extract(t_constraint_past)
    
    CRU = CRU.extract(t_constraint_past)
    UDel = UDel.extract(t_constraint_past)
    GPCC = GPCC.extract(t_constraint_past)
    
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
    IPSL_30 = IPSL.extract(t_constraint_future)
    MIROC_30 = MIROC.extract(t_constraint_future)
    MOHCCCLM_30 = MOHCCCLM.extract(t_constraint_future)
    MOHCKNMI_30 = MOHCKNMI.extract(t_constraint_future)
    MOHCSMHI_30 = MOHCSMHI.extract(t_constraint_future)
    MPICCLM_30 = MPICCLM.extract(t_constraint_future)
    MPIREMO_30 = MPIREMO.extract(t_constraint_future)
    MPISMHI_30 = MPISMHI.extract(t_constraint_future)
    NCCSMHI_30 = NCCSMHI.extract(t_constraint_future)
    NOAA_30 = NOAA.extract(t_constraint_future) 
    
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
    IPSL85_30 = IPSL85.extract(t_constraint_future)
    MIROC85_30 = MIROC85.extract(t_constraint_future)
    MOHCCCLM85_30 = MOHCCCLM85.extract(t_constraint_future)
    MOHCKNMI85_30 = MOHCKNMI85.extract(t_constraint_future)
    MOHCSMHI85_30 = MOHCSMHI85.extract(t_constraint_future)
    MPICCLM85_30 = MPICCLM85.extract(t_constraint_future)
    MPIREMO85_30 = MPIREMO85.extract(t_constraint_future)
    MPISMHI85_30 = MPISMHI85.extract(t_constraint_future)
    NCCSMHI85_30 = NCCSMHI85.extract(t_constraint_future)
    NOAA85_30 = NOAA85.extract(t_constraint_future) 
    
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
    IPSL_50 = IPSL.extract(t_constraint_future)
    MIROC_50 = MIROC.extract(t_constraint_future)
    MOHCCCLM_50 = MOHCCCLM.extract(t_constraint_future)
    MOHCKNMI_50 = MOHCKNMI.extract(t_constraint_future)
    MOHCSMHI_50 = MOHCSMHI.extract(t_constraint_future)
    MPICCLM_50 = MPICCLM.extract(t_constraint_future)
    MPIREMO_50 = MPIREMO.extract(t_constraint_future)
    MPISMHI_50 = MPISMHI.extract(t_constraint_future)
    NCCSMHI_50 = NCCSMHI.extract(t_constraint_future)
    NOAA_50 = NOAA.extract(t_constraint_future) 
    
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
    IPSL85_50 = IPSL85.extract(t_constraint_future)
    MIROC85_50 = MIROC85.extract(t_constraint_future)
    MOHCCCLM85_50 = MOHCCCLM85.extract(t_constraint_future)
    MOHCKNMI85_50 = MOHCKNMI85.extract(t_constraint_future)
    MOHCSMHI85_50 = MOHCSMHI85.extract(t_constraint_future)
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
    IPSL_past_N = IPSL_past.extract(Northern_Malawi)
    MIROC_past_N = MIROC_past.extract(Northern_Malawi)
    MOHCCCLM_past_N = MOHCCCLM_past.extract(Northern_Malawi)
    MOHCKNMI_past_N = MOHCKNMI_past.extract(Northern_Malawi)
    MOHCSMHI_past_N = MOHCSMHI_past.extract(Northern_Malawi)
    MPICCLM_past_N = MPICCLM_past.extract(Northern_Malawi)
    MPIREMO_past_N = MPIREMO_past.extract(Northern_Malawi)
    MPISMHI_past_N = MPISMHI_past.extract(Northern_Malawi)
    NCCSMHI_past_N = NCCSMHI_past.extract(Northern_Malawi)
    NOAA_past_N = NOAA_past.extract(Northern_Malawi)
    
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
    IPSL_30_N = IPSL_30.extract(Northern_Malawi)
    MIROC_30_N = MIROC_30.extract(Northern_Malawi)
    MOHCCCLM_30_N = MOHCCCLM_30.extract(Northern_Malawi)
    MOHCKNMI_30_N = MOHCKNMI_30.extract(Northern_Malawi)
    MOHCSMHI_30_N = MOHCSMHI_30.extract(Northern_Malawi)
    MPICCLM_30_N = MPICCLM_30.extract(Northern_Malawi)
    MPIREMO_30_N = MPIREMO_30.extract(Northern_Malawi)
    MPISMHI_30_N = MPISMHI_30.extract(Northern_Malawi)
    NCCSMHI_30_N = NCCSMHI_30.extract(Northern_Malawi)
    NOAA_30_N = NOAA_30.extract(Northern_Malawi)
    
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
    IPSL85_30_N = IPSL85_30.extract(Northern_Malawi)
    MIROC85_30_N = MIROC85_30.extract(Northern_Malawi)
    MOHCCCLM85_30_N = MOHCCCLM85_30.extract(Northern_Malawi)
    MOHCKNMI85_30_N = MOHCKNMI85_30.extract(Northern_Malawi)
    MOHCSMHI85_30_N = MOHCSMHI85_30.extract(Northern_Malawi)
    MPICCLM85_30_N = MPICCLM85_30.extract(Northern_Malawi)
    MPIREMO85_30_N = MPIREMO85_30.extract(Northern_Malawi)
    MPISMHI85_30_N = MPISMHI85_30.extract(Northern_Malawi)
    NCCSMHI85_30_N = NCCSMHI85_30.extract(Northern_Malawi)
    NOAA85_30_N = NOAA85_30.extract(Northern_Malawi)
    
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
    IPSL_50_N = IPSL_50.extract(Northern_Malawi)
    MIROC_50_N = MIROC_50.extract(Northern_Malawi)
    MOHCCCLM_50_N = MOHCCCLM_50.extract(Northern_Malawi)
    MOHCKNMI_50_N = MOHCKNMI_50.extract(Northern_Malawi)
    MOHCSMHI_50_N = MOHCSMHI_50.extract(Northern_Malawi)
    MPICCLM_50_N = MPICCLM_50.extract(Northern_Malawi)
    MPIREMO_50_N = MPIREMO_50.extract(Northern_Malawi)
    MPISMHI_50_N = MPISMHI_50.extract(Northern_Malawi)
    NCCSMHI_50_N = NCCSMHI_50.extract(Northern_Malawi)
    NOAA_50_N = NOAA_50.extract(Northern_Malawi)
    
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
    IPSL85_50_N = IPSL85_50.extract(Northern_Malawi)
    MIROC85_50_N = MIROC85_50.extract(Northern_Malawi)
    MOHCCCLM85_50_N = MOHCCCLM85_50.extract(Northern_Malawi)
    MOHCKNMI85_50_N = MOHCKNMI85_50.extract(Northern_Malawi)
    MOHCSMHI85_50_N = MOHCSMHI85_50.extract(Northern_Malawi)
    MPICCLM85_50_N = MPICCLM85_50.extract(Northern_Malawi)
    MPIREMO85_50_N = MPIREMO85_50.extract(Northern_Malawi)
    MPISMHI85_50_N = MPISMHI85_50.extract(Northern_Malawi)
    NCCSMHI85_50_N = NCCSMHI85_50.extract(Northern_Malawi)
    NOAA85_50_N = NOAA85_50.extract(Northern_Malawi)
    
    CRU_N = CRU.extract(Northern_Malawi)
    UDel_N = UDel.extract(Northern_Malawi)
    GPCC_N = GPCC.extract(Northern_Malawi)
    
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
    IPSL_past_N = IPSL_past_N.aggregated_by('day_of_year', iris.analysis.MEAN)
    MIROC_past_N = MIROC_past_N.aggregated_by('day_of_year', iris.analysis.MEAN)
    MOHCCCLM_past_N = MOHCCCLM_past_N.aggregated_by('day_of_year', iris.analysis.MEAN)
    MOHCKNMI_past_N = MOHCKNMI_past_N.aggregated_by('day_of_year', iris.analysis.MEAN)
    MOHCSMHI_past_N = MOHCSMHI_past_N.aggregated_by('day_of_year', iris.analysis.MEAN)
    MPICCLM_past_N = MPICCLM_past_N.aggregated_by('day_of_year', iris.analysis.MEAN)
    MPIREMO_past_N = MPIREMO_past_N.aggregated_by('day_of_year', iris.analysis.MEAN)
    MPISMHI_past_N = MPISMHI_past_N.aggregated_by('day_of_year', iris.analysis.MEAN)
    NCCSMHI_past_N = NCCSMHI_past_N.aggregated_by('day_of_year', iris.analysis.MEAN)
    NOAA_past_N = NOAA_past_N.aggregated_by('day_of_year', iris.analysis.MEAN)
    
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
    IPSL_30_N = IPSL_30_N.aggregated_by('day_of_year', iris.analysis.MEAN)
    MIROC_30_N = MIROC_30_N.aggregated_by('day_of_year', iris.analysis.MEAN)
    MOHCCCLM_30_N = MOHCCCLM_30_N.aggregated_by('day_of_year', iris.analysis.MEAN)
    MOHCKNMI_30_N = MOHCKNMI_30_N.aggregated_by('day_of_year', iris.analysis.MEAN)
    MOHCSMHI_30_N = MOHCSMHI_30_N.aggregated_by('day_of_year', iris.analysis.MEAN)
    MPICCLM_30_N = MPICCLM_30_N.aggregated_by('day_of_year', iris.analysis.MEAN)
    MPIREMO_30_N = MPIREMO_30_N.aggregated_by('day_of_year', iris.analysis.MEAN)
    MPISMHI_30_N = MPISMHI_30_N.aggregated_by('day_of_year', iris.analysis.MEAN)
    NCCSMHI_30_N = NCCSMHI_30_N.aggregated_by('day_of_year', iris.analysis.MEAN)
    NOAA_30_N = NOAA_30_N.aggregated_by('day_of_year', iris.analysis.MEAN)
    
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
    IPSL85_30_N = IPSL85_30_N.aggregated_by('day_of_year', iris.analysis.MEAN)
    MIROC85_30_N = MIROC85_30_N.aggregated_by('day_of_year', iris.analysis.MEAN)
    MOHCCCLM85_30_N = MOHCCCLM85_30_N.aggregated_by('day_of_year', iris.analysis.MEAN)
    MOHCKNMI85_30_N = MOHCKNMI85_30_N.aggregated_by('day_of_year', iris.analysis.MEAN)
    MOHCSMHI85_30_N = MOHCSMHI85_30_N.aggregated_by('day_of_year', iris.analysis.MEAN)
    MPICCLM85_30_N = MPICCLM85_30_N.aggregated_by('day_of_year', iris.analysis.MEAN)
    MPIREMO85_30_N = MPIREMO85_30_N.aggregated_by('day_of_year', iris.analysis.MEAN)
    MPISMHI85_30_N = MPISMHI85_30_N.aggregated_by('day_of_year', iris.analysis.MEAN)
    NCCSMHI85_30_N = NCCSMHI85_30_N.aggregated_by('day_of_year', iris.analysis.MEAN)
    NOAA85_30_N = NOAA85_30_N.aggregated_by('day_of_year', iris.analysis.MEAN)
    
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
    IPSL_50_N = IPSL_50_N.aggregated_by('day_of_year', iris.analysis.MEAN)
    MIROC_50_N = MIROC_50_N.aggregated_by('day_of_year', iris.analysis.MEAN)
    MOHCCCLM_50_N = MOHCCCLM_50_N.aggregated_by('day_of_year', iris.analysis.MEAN)
    MOHCKNMI_50_N = MOHCKNMI_50_N.aggregated_by('day_of_year', iris.analysis.MEAN)
    MOHCSMHI_50_N = MOHCSMHI_50_N.aggregated_by('day_of_year', iris.analysis.MEAN)
    MPICCLM_50_N = MPICCLM_50_N.aggregated_by('day_of_year', iris.analysis.MEAN)
    MPIREMO_50_N = MPIREMO_50_N.aggregated_by('day_of_year', iris.analysis.MEAN)
    MPISMHI_50_N = MPISMHI_50_N.aggregated_by('day_of_year', iris.analysis.MEAN)
    NCCSMHI_50_N = NCCSMHI_50_N.aggregated_by('day_of_year', iris.analysis.MEAN)
    NOAA_50_N = NOAA_50_N.aggregated_by('day_of_year', iris.analysis.MEAN)
    
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
    IPSL85_50_N = IPSL85_50_N.aggregated_by('day_of_year', iris.analysis.MEAN)
    MIROC85_50_N = MIROC85_50_N.aggregated_by('day_of_year', iris.analysis.MEAN)
    MOHCCCLM85_50_N = MOHCCCLM85_50_N.aggregated_by('day_of_year', iris.analysis.MEAN)
    MOHCKNMI85_50_N = MOHCKNMI85_50_N.aggregated_by('day_of_year', iris.analysis.MEAN)
    MOHCSMHI85_50_N = MOHCSMHI85_50_N.aggregated_by('day_of_year', iris.analysis.MEAN)
    MPICCLM85_50_N = MPICCLM85_50_N.aggregated_by('day_of_year', iris.analysis.MEAN)
    MPIREMO85_50_N = MPIREMO85_50_N.aggregated_by('day_of_year', iris.analysis.MEAN)
    MPISMHI85_50_N = MPISMHI85_50_N.aggregated_by('day_of_year', iris.analysis.MEAN)
    NCCSMHI85_50_N = NCCSMHI85_50_N.aggregated_by('day_of_year', iris.analysis.MEAN)
    NOAA85_50_N = NOAA85_50_N.aggregated_by('day_of_year', iris.analysis.MEAN)
    
    CRU_N = CRU_N.aggregated_by('day_of_year', iris.analysis.MEAN)
    UDel_N = UDel_N.aggregated_by('day_of_year', iris.analysis.MEAN)
    GPCC_N = GPCC_N.aggregated_by('day_of_year', iris.analysis.MEAN)
    
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
    IPSL_past_N_grid_areas = iris.analysis.cartography.area_weights(IPSL_past_N)
    MIROC_past_N_grid_areas = iris.analysis.cartography.area_weights(MIROC_past_N)
    MOHCCCLM_past_N_grid_areas = iris.analysis.cartography.area_weights(MOHCCCLM_past_N)
    MOHCKNMI_past_N_grid_areas = iris.analysis.cartography.area_weights(MOHCKNMI_past_N)
    MOHCSMHI_past_N_grid_areas = iris.analysis.cartography.area_weights(MOHCSMHI_past_N)
    MPICCLM_past_N_grid_areas = iris.analysis.cartography.area_weights(MPICCLM_past_N)
    MPIREMO_past_N_grid_areas = iris.analysis.cartography.area_weights(MPIREMO_past_N)
    MPISMHI_past_N_grid_areas = iris.analysis.cartography.area_weights(MPISMHI_past_N)
    NCCSMHI_past_N_grid_areas = iris.analysis.cartography.area_weights(NCCSMHI_past_N)
    NOAA_past_N_grid_areas = iris.analysis.cartography.area_weights(NOAA_past_N)
    
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
    IPSL_30_N_grid_areas = iris.analysis.cartography.area_weights(IPSL_30_N)
    MIROC_30_N_grid_areas = iris.analysis.cartography.area_weights(MIROC_30_N)
    MOHCCCLM_30_N_grid_areas = iris.analysis.cartography.area_weights(MOHCCCLM_30_N)
    MOHCKNMI_30_N_grid_areas = iris.analysis.cartography.area_weights(MOHCKNMI_30_N)
    MOHCSMHI_30_N_grid_areas = iris.analysis.cartography.area_weights(MOHCSMHI_30_N)
    MPICCLM_30_N_grid_areas = iris.analysis.cartography.area_weights(MPICCLM_30_N)
    MPIREMO_30_N_grid_areas = iris.analysis.cartography.area_weights(MPIREMO_30_N)
    MPISMHI_30_N_grid_areas = iris.analysis.cartography.area_weights(MPISMHI_30_N)
    NCCSMHI_30_N_grid_areas = iris.analysis.cartography.area_weights(NCCSMHI_30_N)
    NOAA_30_N_grid_areas = iris.analysis.cartography.area_weights(NOAA_30_N)
    
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
    IPSL85_30_N_grid_areas = iris.analysis.cartography.area_weights(IPSL85_30_N)
    MIROC85_30_N_grid_areas = iris.analysis.cartography.area_weights(MIROC85_30_N)
    MOHCCCLM85_30_N_grid_areas = iris.analysis.cartography.area_weights(MOHCCCLM85_30_N)
    MOHCKNMI85_30_N_grid_areas = iris.analysis.cartography.area_weights(MOHCKNMI85_30_N)
    MOHCSMHI85_30_N_grid_areas = iris.analysis.cartography.area_weights(MOHCSMHI85_30_N)
    MPICCLM85_30_N_grid_areas = iris.analysis.cartography.area_weights(MPICCLM85_30_N)
    MPIREMO85_30_N_grid_areas = iris.analysis.cartography.area_weights(MPIREMO85_30_N)
    MPISMHI85_30_N_grid_areas = iris.analysis.cartography.area_weights(MPISMHI85_30_N)
    NCCSMHI85_30_N_grid_areas = iris.analysis.cartography.area_weights(NCCSMHI85_30_N)
    NOAA85_30_N_grid_areas = iris.analysis.cartography.area_weights(NOAA85_30_N)
    
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
    IPSL_50_N_grid_areas = iris.analysis.cartography.area_weights(IPSL_50_N)
    MIROC_50_N_grid_areas = iris.analysis.cartography.area_weights(MIROC_50_N)
    MOHCCCLM_50_N_grid_areas = iris.analysis.cartography.area_weights(MOHCCCLM_50_N)
    MOHCKNMI_50_N_grid_areas = iris.analysis.cartography.area_weights(MOHCKNMI_50_N)
    MOHCSMHI_50_N_grid_areas = iris.analysis.cartography.area_weights(MOHCSMHI_50_N)
    MPICCLM_50_N_grid_areas = iris.analysis.cartography.area_weights(MPICCLM_50_N)
    MPIREMO_50_N_grid_areas = iris.analysis.cartography.area_weights(MPIREMO_50_N)
    MPISMHI_50_N_grid_areas = iris.analysis.cartography.area_weights(MPISMHI_50_N)
    NCCSMHI_50_N_grid_areas = iris.analysis.cartography.area_weights(NCCSMHI_50_N)
    NOAA_50_N_grid_areas = iris.analysis.cartography.area_weights(NOAA_50_N)
    
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
    IPSL85_50_N_grid_areas = iris.analysis.cartography.area_weights(IPSL85_50_N)
    MIROC85_50_N_grid_areas = iris.analysis.cartography.area_weights(MIROC85_50_N)
    MOHCCCLM85_50_N_grid_areas = iris.analysis.cartography.area_weights(MOHCCCLM85_50_N)
    MOHCKNMI85_50_N_grid_areas = iris.analysis.cartography.area_weights(MOHCKNMI85_50_N)
    MOHCSMHI85_50_N_grid_areas = iris.analysis.cartography.area_weights(MOHCSMHI85_50_N)
    MPICCLM85_50_N_grid_areas = iris.analysis.cartography.area_weights(MPICCLM85_50_N)
    MPIREMO85_50_N_grid_areas = iris.analysis.cartography.area_weights(MPIREMO85_50_N)
    MPISMHI85_50_N_grid_areas = iris.analysis.cartography.area_weights(MPISMHI85_50_N)
    NCCSMHI85_50_N_grid_areas = iris.analysis.cartography.area_weights(NCCSMHI85_50_N)
    NOAA85_50_N_grid_areas = iris.analysis.cartography.area_weights(NOAA85_50_N)
    
    CRU_N_grid_areas = iris.analysis.cartography.area_weights(CRU_N)
    UDel_N_grid_areas = iris.analysis.cartography.area_weights (UDel_N)
    GPCC_N_grid_areas = iris.analysis.cartography.area_weights (GPCC_N)
    
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
    IPSL_past_N_mean = IPSL_past_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=IPSL_past_N_grid_areas)
    MIROC_past_N_mean = MIROC_past_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MIROC_past_N_grid_areas)
    MOHCCCLM_past_N_mean = MOHCCCLM_past_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCCCLM_past_N_grid_areas)
    MOHCKNMI_past_N_mean = MOHCKNMI_past_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCKNMI_past_N_grid_areas)
    MOHCSMHI_past_N_mean = MOHCSMHI_past_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCSMHI_past_N_grid_areas)
    MPICCLM_past_N_mean = MPICCLM_past_N.collapsed(['latitude', 'longitude'],iris.analysis.MEAN, weights=MPICCLM_past_N_grid_areas)        
    MPIREMO_past_N_mean = MPIREMO_past_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MPIREMO_past_N_grid_areas)          
    MPISMHI_past_N_mean = MPISMHI_past_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MPISMHI_past_N_grid_areas)
    NCCSMHI_past_N_mean = NCCSMHI_past_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=NCCSMHI_past_N_grid_areas) 
    NOAA_past_N_mean = NOAA_past_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=NOAA_past_N_grid_areas)
    
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
    IPSL_30_N_mean = IPSL_30_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=IPSL_30_N_grid_areas)
    MIROC_30_N_mean = MIROC_30_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MIROC_30_N_grid_areas)
    MOHCCCLM_30_N_mean = MOHCCCLM_30_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCCCLM_30_N_grid_areas)
    MOHCKNMI_30_N_mean = MOHCKNMI_30_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCKNMI_30_N_grid_areas)
    MOHCSMHI_30_N_mean = MOHCSMHI_30_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCSMHI_30_N_grid_areas)
    MPICCLM_30_N_mean = MPICCLM_30_N.collapsed(['latitude', 'longitude'],iris.analysis.MEAN, weights=MPICCLM_30_N_grid_areas)        
    MPIREMO_30_N_mean = MPIREMO_30_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MPIREMO_30_N_grid_areas)                         
    MPISMHI_30_N_mean = MPISMHI_30_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MPISMHI_30_N_grid_areas)
    NCCSMHI_30_N_mean = NCCSMHI_30_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=NCCSMHI_30_N_grid_areas) 
    NOAA_30_N_mean = NOAA_30_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=NOAA_30_N_grid_areas)
    
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
    IPSL85_30_N_mean = IPSL85_30_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=IPSL85_30_N_grid_areas)
    MIROC85_30_N_mean = MIROC85_30_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MIROC85_30_N_grid_areas)
    MOHCCCLM85_30_N_mean = MOHCCCLM85_30_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCCCLM85_30_N_grid_areas)
    MOHCKNMI85_30_N_mean = MOHCKNMI85_30_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCKNMI85_30_N_grid_areas)
    MOHCSMHI85_30_N_mean = MOHCSMHI85_30_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCSMHI85_30_N_grid_areas)
    MPICCLM85_30_N_mean = MPICCLM85_30_N.collapsed(['latitude', 'longitude'],iris.analysis.MEAN, weights=MPICCLM85_30_N_grid_areas)        
    MPIREMO85_30_N_mean = MPIREMO85_30_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MPIREMO85_30_N_grid_areas)                         
    MPISMHI85_30_N_mean = MPISMHI85_30_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MPISMHI85_30_N_grid_areas)
    NCCSMHI85_30_N_mean = NCCSMHI85_30_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=NCCSMHI85_30_N_grid_areas) 
    NOAA85_30_N_mean = NOAA85_30_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=NOAA85_30_N_grid_areas)
    
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
    IPSL_50_N_mean = IPSL_50_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=IPSL_50_N_grid_areas)
    MIROC_50_N_mean = MIROC_50_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MIROC_50_N_grid_areas)
    MOHCCCLM_50_N_mean = MOHCCCLM_50_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCCCLM_50_N_grid_areas)
    MOHCKNMI_50_N_mean = MOHCKNMI_50_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCKNMI_50_N_grid_areas)
    MOHCSMHI_50_N_mean = MOHCSMHI_50_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCSMHI_50_N_grid_areas)
    MPICCLM_50_N_mean = MPICCLM_50_N.collapsed(['latitude', 'longitude'],iris.analysis.MEAN, weights=MPICCLM_50_N_grid_areas)        
    MPIREMO_50_N_mean = MPIREMO_50_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MPIREMO_50_N_grid_areas)                         
    MPISMHI_50_N_mean = MPISMHI_50_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MPISMHI_50_N_grid_areas)
    NCCSMHI_50_N_mean = NCCSMHI_50_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=NCCSMHI_50_N_grid_areas) 
    NOAA_50_N_mean = NOAA_50_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=NOAA_50_N_grid_areas)
    
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
    IPSL85_50_N_mean = IPSL85_50_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=IPSL85_50_N_grid_areas)
    MIROC85_50_N_mean = MIROC85_50_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MIROC85_50_N_grid_areas)
    MOHCCCLM85_50_N_mean = MOHCCCLM85_50_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCCCLM85_50_N_grid_areas)
    MOHCKNMI85_50_N_mean = MOHCKNMI85_50_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCKNMI85_50_N_grid_areas)
    MOHCSMHI85_50_N_mean = MOHCSMHI85_50_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCSMHI85_50_N_grid_areas)
    MPICCLM85_50_N_mean = MPICCLM85_50_N.collapsed(['latitude', 'longitude'],iris.analysis.MEAN, weights=MPICCLM85_50_N_grid_areas)        
    MPIREMO85_50_N_mean = MPIREMO85_50_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MPIREMO85_50_N_grid_areas)                         
    MPISMHI85_50_N_mean = MPISMHI85_50_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MPISMHI85_50_N_grid_areas)
    NCCSMHI85_50_N_mean = NCCSMHI85_50_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=NCCSMHI85_50_N_grid_areas) 
    NOAA85_50_N_mean = NOAA85_50_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=NOAA85_50_N_grid_areas)
    
    CRU_N_mean = CRU_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CRU_N_grid_areas)
    UDel_N_mean = UDel_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=UDel_N_grid_areas)
    GPCC_N_mean = GPCC_N.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=GPCC_N_grid_areas)
    
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
    IPSL_b_N_mean = IPSL_past_N_mean.collapsed(['time'], iris.analysis.MEAN) 
    MIROC_b_N_mean = MIROC_past_N_mean.collapsed(['time'], iris.analysis.MEAN) 
    MOHCCCLM_b_N_mean = MOHCCCLM_past_N_mean.collapsed(['time'], iris.analysis.MEAN) 
    MOHCKNMI_b_N_mean = MOHCKNMI_past_N_mean.collapsed(['time'], iris.analysis.MEAN) 
    MOHCSMHI_b_N_mean = MOHCSMHI_past_N_mean.collapsed(['time'], iris.analysis.MEAN) 
    MPICCLM_b_N_mean = MPICCLM_past_N_mean.collapsed(['time'], iris.analysis.MEAN)        
    MPIREMO_b_N_mean = MPIREMO_past_N_mean.collapsed(['time'], iris.analysis.MEAN)           
    MPISMHI_b_N_mean = MPISMHI_past_N_mean.collapsed(['time'], iris.analysis.MEAN) 
    NCCSMHI_b_N_mean = NCCSMHI_past_N_mean.collapsed(['time'], iris.analysis.MEAN)  
    NOAA_b_N_mean = NOAA_past_N_mean.collapsed(['time'], iris.analysis.MEAN)     
    
    CRU_N_mean = CRU_N_mean.collapsed(['time'], iris.analysis.MEAN)     
    UDel_N_mean = UDel_N_mean.collapsed(['time'], iris.analysis.MEAN) 
    GPCC_N_mean = GPCC_N_mean.collapsed(['time'], iris.analysis.MEAN)
    
    #create average of observed baseline data
    Obs_N = (CRU_N_mean + UDel_N_mean + GPCC_N_mean)/3  
    
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
    IPSL_past_N_mean = (IPSL_past_N_mean.data - IPSL_b_N_mean.data + Obs_N.data)
    MIROC_past_N_mean = (MIROC_past_N_mean.data - MIROC_b_N_mean.data + Obs_N.data)
    MOHCCCLM_past_N_mean = (MOHCCCLM_past_N_mean.data - MOHCCCLM_b_N_mean.data + Obs_N.data)
    MOHCKNMI_past_N_mean = (MOHCKNMI_past_N_mean.data - MOHCKNMI_b_N_mean.data + Obs_N.data)
    MOHCSMHI_past_N_mean = (MOHCSMHI_past_N_mean.data - MOHCSMHI_b_N_mean.data + Obs_N.data)
    MPICCLM_past_N_mean = (MPICCLM_past_N_mean.data - MPICCLM_b_N_mean.data + Obs_N.data)      
    MPIREMO_past_N_mean = (MPIREMO_past_N_mean.data - MPIREMO_b_N_mean.data + Obs_N.data)                         
    MPISMHI_past_N_mean = (MPISMHI_past_N_mean.data - MPISMHI_b_N_mean.data + Obs_N.data)
    NCCSMHI_past_N_mean = (NCCSMHI_past_N_mean.data - NCCSMHI_b_N_mean.data + Obs_N.data) 
    NOAA_past_N_mean = (NOAA_past_N_mean.data - NOAA_b_N_mean.data + Obs_N.data)
    
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
    IPSL_30_N_mean = (IPSL_30_N_mean.data - IPSL_b_N_mean.data + Obs_N.data)
    MIROC_30_N_mean = (MIROC_30_N_mean.data - MIROC_b_N_mean.data + Obs_N.data)
    MOHCCCLM_30_N_mean = (MOHCCCLM_30_N_mean.data - MOHCCCLM_b_N_mean.data + Obs_N.data)
    MOHCKNMI_30_N_mean = (MOHCKNMI_30_N_mean.data - MOHCKNMI_b_N_mean.data + Obs_N.data)
    MOHCSMHI_30_N_mean = (MOHCSMHI_30_N_mean.data - MOHCSMHI_b_N_mean.data + Obs_N.data)
    MPICCLM_30_N_mean = (MPICCLM_30_N_mean.data - MPICCLM_b_N_mean.data + Obs_N.data)      
    MPIREMO_30_N_mean = (MPIREMO_30_N_mean.data - MPIREMO_b_N_mean.data + Obs_N.data)                         
    MPISMHI_30_N_mean = (MPISMHI_30_N_mean.data - MPISMHI_b_N_mean.data + Obs_N.data)
    NCCSMHI_30_N_mean = (NCCSMHI_30_N_mean.data - NCCSMHI_b_N_mean.data + Obs_N.data) 
    NOAA_30_N_mean = (NOAA_30_N_mean.data - NOAA_b_N_mean.data + Obs_N.data)
    
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
    IPSL85_30_N_mean = (IPSL85_30_N_mean.data - IPSL_b_N_mean.data + Obs_N.data)
    MIROC85_30_N_mean = (MIROC85_30_N_mean.data - MIROC_b_N_mean.data + Obs_N.data)
    MOHCCCLM85_30_N_mean = (MOHCCCLM85_30_N_mean.data - MOHCCCLM_b_N_mean.data + Obs_N.data)
    MOHCKNMI85_30_N_mean = (MOHCKNMI85_30_N_mean.data - MOHCKNMI_b_N_mean.data + Obs_N.data)
    MOHCSMHI85_30_N_mean = (MOHCSMHI85_30_N_mean.data - MOHCSMHI_b_N_mean.data + Obs_N.data)
    MPICCLM85_30_N_mean = (MPICCLM85_30_N_mean.data - MPICCLM_b_N_mean.data + Obs_N.data)      
    MPIREMO85_30_N_mean = (MPIREMO85_30_N_mean.data - MPIREMO_b_N_mean.data + Obs_N.data)                         
    MPISMHI85_30_N_mean = (MPISMHI85_30_N_mean.data - MPISMHI_b_N_mean.data + Obs_N.data)
    NCCSMHI85_30_N_mean = (NCCSMHI85_30_N_mean.data - NCCSMHI_b_N_mean.data + Obs_N.data) 
    NOAA85_30_N_mean = (NOAA85_30_N_mean.data - NOAA_b_N_mean.data + Obs_N.data)
    
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
    IPSL_50_N_mean = (IPSL_50_N_mean.data - IPSL_b_N_mean.data + Obs_N.data)
    MIROC_50_N_mean = (MIROC_50_N_mean.data - MIROC_b_N_mean.data + Obs_N.data)
    MOHCCCLM_50_N_mean = (MOHCCCLM_50_N_mean.data - MOHCCCLM_b_N_mean.data + Obs_N.data)
    MOHCKNMI_50_N_mean = (MOHCKNMI_50_N_mean.data - MOHCKNMI_b_N_mean.data + Obs_N.data)
    MOHCSMHI_50_N_mean = (MOHCSMHI_50_N_mean.data - MOHCSMHI_b_N_mean.data + Obs_N.data)
    MPICCLM_50_N_mean = (MPICCLM_50_N_mean.data - MPICCLM_b_N_mean.data + Obs_N.data)      
    MPIREMO_50_N_mean = (MPIREMO_50_N_mean.data - MPIREMO_b_N_mean.data + Obs_N.data)                         
    MPISMHI_50_N_mean = (MPISMHI_50_N_mean.data - MPISMHI_b_N_mean.data + Obs_N.data)
    NCCSMHI_50_N_mean = (NCCSMHI_50_N_mean.data - NCCSMHI_b_N_mean.data + Obs_N.data) 
    NOAA_50_N_mean = (NOAA_50_N_mean.data - NOAA_b_N_mean.data + Obs_N.data)
    
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
    IPSL85_50_N_mean = (IPSL85_50_N_mean.data - IPSL_b_N_mean.data + Obs_N.data)
    MIROC85_50_N_mean = (MIROC85_50_N_mean.data - MIROC_b_N_mean.data + Obs_N.data)
    MOHCCCLM85_50_N_mean = (MOHCCCLM85_50_N_mean.data - MOHCCCLM_b_N_mean.data + Obs_N.data)
    MOHCKNMI85_50_N_mean = (MOHCKNMI85_50_N_mean.data - MOHCKNMI_b_N_mean.data + Obs_N.data)
    MOHCSMHI85_50_N_mean = (MOHCSMHI85_50_N_mean.data - MOHCSMHI_b_N_mean.data + Obs_N.data)
    MPICCLM85_50_N_mean = (MPICCLM85_50_N_mean.data - MPICCLM_b_N_mean.data + Obs_N.data)      
    MPIREMO85_50_N_mean = (MPIREMO85_50_N_mean.data - MPIREMO_b_N_mean.data + Obs_N.data)                         
    MPISMHI85_50_N_mean = (MPISMHI85_50_N_mean.data - MPISMHI_b_N_mean.data + Obs_N.data)
    NCCSMHI85_50_N_mean = (NCCSMHI85_50_N_mean.data - NCCSMHI_b_N_mean.data + Obs_N.data) 
    NOAA85_50_N_mean = (NOAA85_50_N_mean.data - NOAA_b_N_mean.data + Obs_N.data)
    
    
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
    IPSL_past_C = IPSL_past.extract(Central_Malawi)
    MIROC_past_C = MIROC_past.extract(Central_Malawi)
    MOHCCCLM_past_C = MOHCCCLM_past.extract(Central_Malawi)
    MOHCKNMI_past_C = MOHCKNMI_past.extract(Central_Malawi)
    MOHCSMHI_past_C = MOHCSMHI_past.extract(Central_Malawi)
    MPICCLM_past_C = MPICCLM_past.extract(Central_Malawi)
    MPIREMO_past_C = MPIREMO_past.extract(Central_Malawi)
    MPISMHI_past_C = MPISMHI_past.extract(Central_Malawi)
    NCCSMHI_past_C = NCCSMHI_past.extract(Central_Malawi)
    NOAA_past_C = NOAA_past.extract(Central_Malawi)
    
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
    IPSL_30_C = IPSL_30.extract(Central_Malawi)
    MIROC_30_C = MIROC_30.extract(Central_Malawi)
    MOHCCCLM_30_C = MOHCCCLM_30.extract(Central_Malawi)
    MOHCKNMI_30_C = MOHCKNMI_30.extract(Central_Malawi)
    MOHCSMHI_30_C = MOHCSMHI_30.extract(Central_Malawi)
    MPICCLM_30_C = MPICCLM_30.extract(Central_Malawi)
    MPIREMO_30_C = MPIREMO_30.extract(Central_Malawi)
    MPISMHI_30_C = MPISMHI_30.extract(Central_Malawi)
    NCCSMHI_30_C = NCCSMHI_30.extract(Central_Malawi)
    NOAA_30_C = NOAA_30.extract(Central_Malawi)
    
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
    IPSL85_30_C = IPSL85_30.extract(Central_Malawi)
    MIROC85_30_C = MIROC85_30.extract(Central_Malawi)
    MOHCCCLM85_30_C = MOHCCCLM85_30.extract(Central_Malawi)
    MOHCKNMI85_30_C = MOHCKNMI85_30.extract(Central_Malawi)
    MOHCSMHI85_30_C = MOHCSMHI85_30.extract(Central_Malawi)
    MPICCLM85_30_C = MPICCLM85_30.extract(Central_Malawi)
    MPIREMO85_30_C = MPIREMO85_30.extract(Central_Malawi)
    MPISMHI85_30_C = MPISMHI85_30.extract(Central_Malawi)
    NCCSMHI85_30_C = NCCSMHI85_30.extract(Central_Malawi)
    NOAA85_30_C = NOAA85_30.extract(Central_Malawi)
    
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
    IPSL_50_C = IPSL_50.extract(Central_Malawi)
    MIROC_50_C = MIROC_50.extract(Central_Malawi)
    MOHCCCLM_50_C = MOHCCCLM_50.extract(Central_Malawi)
    MOHCKNMI_50_C = MOHCKNMI_50.extract(Central_Malawi)
    MOHCSMHI_50_C = MOHCSMHI_50.extract(Central_Malawi)
    MPICCLM_50_C = MPICCLM_50.extract(Central_Malawi)
    MPIREMO_50_C = MPIREMO_50.extract(Central_Malawi)
    MPISMHI_50_C = MPISMHI_50.extract(Central_Malawi)
    NCCSMHI_50_C = NCCSMHI_50.extract(Central_Malawi)
    NOAA_50_C = NOAA_50.extract(Central_Malawi)
    
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
    IPSL85_50_C = IPSL85_50.extract(Central_Malawi)
    MIROC85_50_C = MIROC85_50.extract(Central_Malawi)
    MOHCCCLM85_50_C = MOHCCCLM85_50.extract(Central_Malawi)
    MOHCKNMI85_50_C = MOHCKNMI85_50.extract(Central_Malawi)
    MOHCSMHI85_50_C = MOHCSMHI85_50.extract(Central_Malawi)
    MPICCLM85_50_C = MPICCLM85_50.extract(Central_Malawi)
    MPIREMO85_50_C = MPIREMO85_50.extract(Central_Malawi)
    MPISMHI85_50_C = MPISMHI85_50.extract(Central_Malawi)
    NCCSMHI85_50_C = NCCSMHI85_50.extract(Central_Malawi)
    NOAA85_50_C = NOAA85_50.extract(Central_Malawi)
    
    CRU_C = CRU.extract(Central_Malawi)
    UDel_C = UDel.extract(Central_Malawi)
    GPCC_C = GPCC.extract(Central_Malawi)
    
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
    IPSL_past_C = IPSL_past_C.aggregated_by('day_of_year', iris.analysis.MEAN)
    MIROC_past_C = MIROC_past_C.aggregated_by('day_of_year', iris.analysis.MEAN)
    MOHCCCLM_past_C = MOHCCCLM_past_C.aggregated_by('day_of_year', iris.analysis.MEAN)
    MOHCKNMI_past_C = MOHCKNMI_past_C.aggregated_by('day_of_year', iris.analysis.MEAN)
    MOHCSMHI_past_C = MOHCSMHI_past_C.aggregated_by('day_of_year', iris.analysis.MEAN)
    MPICCLM_past_C = MPICCLM_past_C.aggregated_by('day_of_year', iris.analysis.MEAN)
    MPIREMO_past_C = MPIREMO_past_C.aggregated_by('day_of_year', iris.analysis.MEAN)
    MPISMHI_past_C = MPISMHI_past_C.aggregated_by('day_of_year', iris.analysis.MEAN)
    NCCSMHI_past_C = NCCSMHI_past_C.aggregated_by('day_of_year', iris.analysis.MEAN)
    NOAA_past_C = NOAA_past_C.aggregated_by('day_of_year', iris.analysis.MEAN)
    
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
    IPSL_30_C = IPSL_30_C.aggregated_by('day_of_year', iris.analysis.MEAN)
    MIROC_30_C = MIROC_30_C.aggregated_by('day_of_year', iris.analysis.MEAN)
    MOHCCCLM_30_C = MOHCCCLM_30_C.aggregated_by('day_of_year', iris.analysis.MEAN)
    MOHCKNMI_30_C = MOHCKNMI_30_C.aggregated_by('day_of_year', iris.analysis.MEAN)
    MOHCSMHI_30_C = MOHCSMHI_30_C.aggregated_by('day_of_year', iris.analysis.MEAN)
    MPICCLM_30_C = MPICCLM_30_C.aggregated_by('day_of_year', iris.analysis.MEAN)
    MPIREMO_30_C = MPIREMO_30_C.aggregated_by('day_of_year', iris.analysis.MEAN)
    MPISMHI_30_C = MPISMHI_30_C.aggregated_by('day_of_year', iris.analysis.MEAN)
    NCCSMHI_30_C = NCCSMHI_30_C.aggregated_by('day_of_year', iris.analysis.MEAN)
    NOAA_30_C = NOAA_30_C.aggregated_by('day_of_year', iris.analysis.MEAN)
    
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
    IPSL85_30_C = IPSL85_30_C.aggregated_by('day_of_year', iris.analysis.MEAN)
    MIROC85_30_C = MIROC85_30_C.aggregated_by('day_of_year', iris.analysis.MEAN)
    MOHCCCLM85_30_C = MOHCCCLM85_30_C.aggregated_by('day_of_year', iris.analysis.MEAN)
    MOHCKNMI85_30_C = MOHCKNMI85_30_C.aggregated_by('day_of_year', iris.analysis.MEAN)
    MOHCSMHI85_30_C = MOHCSMHI85_30_C.aggregated_by('day_of_year', iris.analysis.MEAN)
    MPICCLM85_30_C = MPICCLM85_30_C.aggregated_by('day_of_year', iris.analysis.MEAN)
    MPIREMO85_30_C = MPIREMO85_30_C.aggregated_by('day_of_year', iris.analysis.MEAN)
    MPISMHI85_30_C = MPISMHI85_30_C.aggregated_by('day_of_year', iris.analysis.MEAN)
    NCCSMHI85_30_C = NCCSMHI85_30_C.aggregated_by('day_of_year', iris.analysis.MEAN)
    NOAA85_30_C = NOAA85_30_C.aggregated_by('day_of_year', iris.analysis.MEAN)
    
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
    IPSL_50_C = IPSL_50_C.aggregated_by('day_of_year', iris.analysis.MEAN)
    MIROC_50_C = MIROC_50_C.aggregated_by('day_of_year', iris.analysis.MEAN)
    MOHCCCLM_50_C = MOHCCCLM_50_C.aggregated_by('day_of_year', iris.analysis.MEAN)
    MOHCKNMI_50_C = MOHCKNMI_50_C.aggregated_by('day_of_year', iris.analysis.MEAN)
    MOHCSMHI_50_C = MOHCSMHI_50_C.aggregated_by('day_of_year', iris.analysis.MEAN)
    MPICCLM_50_C = MPICCLM_50_C.aggregated_by('day_of_year', iris.analysis.MEAN)
    MPIREMO_50_C = MPIREMO_50_C.aggregated_by('day_of_year', iris.analysis.MEAN)
    MPISMHI_50_C = MPISMHI_50_C.aggregated_by('day_of_year', iris.analysis.MEAN)
    NCCSMHI_50_C = NCCSMHI_50_C.aggregated_by('day_of_year', iris.analysis.MEAN)
    NOAA_50_C = NOAA_50_C.aggregated_by('day_of_year', iris.analysis.MEAN)
    
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
    IPSL85_50_C = IPSL85_50_C.aggregated_by('day_of_year', iris.analysis.MEAN)
    MIROC85_50_C = MIROC85_50_C.aggregated_by('day_of_year', iris.analysis.MEAN)
    MOHCCCLM85_50_C = MOHCCCLM85_50_C.aggregated_by('day_of_year', iris.analysis.MEAN)
    MOHCKNMI85_50_C = MOHCKNMI85_50_C.aggregated_by('day_of_year', iris.analysis.MEAN)
    MOHCSMHI85_50_C = MOHCSMHI85_50_C.aggregated_by('day_of_year', iris.analysis.MEAN)
    MPICCLM85_50_C = MPICCLM85_50_C.aggregated_by('day_of_year', iris.analysis.MEAN)
    MPIREMO85_50_C = MPIREMO85_50_C.aggregated_by('day_of_year', iris.analysis.MEAN)
    MPISMHI85_50_C = MPISMHI85_50_C.aggregated_by('day_of_year', iris.analysis.MEAN)
    NCCSMHI85_50_C = NCCSMHI85_50_C.aggregated_by('day_of_year', iris.analysis.MEAN)
    NOAA85_50_C = NOAA85_50_C.aggregated_by('day_of_year', iris.analysis.MEAN)
    
    CRU_C = CRU_C.aggregated_by('day_of_year', iris.analysis.MEAN)
    UDel_C = UDel_C.aggregated_by('day_of_year', iris.analysis.MEAN)
    GPCC_C = GPCC_C.aggregated_by('day_of_year', iris.analysis.MEAN)
    
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
    IPSL_past_C_grid_areas = iris.analysis.cartography.area_weights(IPSL_past_C)
    MIROC_past_C_grid_areas = iris.analysis.cartography.area_weights(MIROC_past_C)
    MOHCCCLM_past_C_grid_areas = iris.analysis.cartography.area_weights(MOHCCCLM_past_C)
    MOHCKNMI_past_C_grid_areas = iris.analysis.cartography.area_weights(MOHCKNMI_past_C)
    MOHCSMHI_past_C_grid_areas = iris.analysis.cartography.area_weights(MOHCSMHI_past_C)
    MPICCLM_past_C_grid_areas = iris.analysis.cartography.area_weights(MPICCLM_past_C)
    MPIREMO_past_C_grid_areas = iris.analysis.cartography.area_weights(MPIREMO_past_C)
    MPISMHI_past_C_grid_areas = iris.analysis.cartography.area_weights(MPISMHI_past_C)
    NCCSMHI_past_C_grid_areas = iris.analysis.cartography.area_weights(NCCSMHI_past_C)
    NOAA_past_C_grid_areas = iris.analysis.cartography.area_weights(NOAA_past_C)
    
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
    IPSL_30_C_grid_areas = iris.analysis.cartography.area_weights(IPSL_30_C)
    MIROC_30_C_grid_areas = iris.analysis.cartography.area_weights(MIROC_30_C)
    MOHCCCLM_30_C_grid_areas = iris.analysis.cartography.area_weights(MOHCCCLM_30_C)
    MOHCKNMI_30_C_grid_areas = iris.analysis.cartography.area_weights(MOHCKNMI_30_C)
    MOHCSMHI_30_C_grid_areas = iris.analysis.cartography.area_weights(MOHCSMHI_30_C)
    MPICCLM_30_C_grid_areas = iris.analysis.cartography.area_weights(MPICCLM_30_C)
    MPIREMO_30_C_grid_areas = iris.analysis.cartography.area_weights(MPIREMO_30_C)
    MPISMHI_30_C_grid_areas = iris.analysis.cartography.area_weights(MPISMHI_30_C)
    NCCSMHI_30_C_grid_areas = iris.analysis.cartography.area_weights(NCCSMHI_30_C)
    NOAA_30_C_grid_areas = iris.analysis.cartography.area_weights(NOAA_30_C)
    
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
    IPSL85_30_C_grid_areas = iris.analysis.cartography.area_weights(IPSL85_30_C)
    MIROC85_30_C_grid_areas = iris.analysis.cartography.area_weights(MIROC85_30_C)
    MOHCCCLM85_30_C_grid_areas = iris.analysis.cartography.area_weights(MOHCCCLM85_30_C)
    MOHCKNMI85_30_C_grid_areas = iris.analysis.cartography.area_weights(MOHCKNMI85_30_C)
    MOHCSMHI85_30_C_grid_areas = iris.analysis.cartography.area_weights(MOHCSMHI85_30_C)
    MPICCLM85_30_C_grid_areas = iris.analysis.cartography.area_weights(MPICCLM85_30_C)
    MPIREMO85_30_C_grid_areas = iris.analysis.cartography.area_weights(MPIREMO85_30_C)
    MPISMHI85_30_C_grid_areas = iris.analysis.cartography.area_weights(MPISMHI85_30_C)
    NCCSMHI85_30_C_grid_areas = iris.analysis.cartography.area_weights(NCCSMHI85_30_C)
    NOAA85_30_C_grid_areas = iris.analysis.cartography.area_weights(NOAA85_30_C)
    
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
    IPSL_50_C_grid_areas = iris.analysis.cartography.area_weights(IPSL_50_C)
    MIROC_50_C_grid_areas = iris.analysis.cartography.area_weights(MIROC_50_C)
    MOHCCCLM_50_C_grid_areas = iris.analysis.cartography.area_weights(MOHCCCLM_50_C)
    MOHCKNMI_50_C_grid_areas = iris.analysis.cartography.area_weights(MOHCKNMI_50_C)
    MOHCSMHI_50_C_grid_areas = iris.analysis.cartography.area_weights(MOHCSMHI_50_C)
    MPICCLM_50_C_grid_areas = iris.analysis.cartography.area_weights(MPICCLM_50_C)
    MPIREMO_50_C_grid_areas = iris.analysis.cartography.area_weights(MPIREMO_50_C)
    MPISMHI_50_C_grid_areas = iris.analysis.cartography.area_weights(MPISMHI_50_C)
    NCCSMHI_50_C_grid_areas = iris.analysis.cartography.area_weights(NCCSMHI_50_C)
    NOAA_50_C_grid_areas = iris.analysis.cartography.area_weights(NOAA_50_C)
    
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
    IPSL85_50_C_grid_areas = iris.analysis.cartography.area_weights(IPSL85_50_C)
    MIROC85_50_C_grid_areas = iris.analysis.cartography.area_weights(MIROC85_50_C)
    MOHCCCLM85_50_C_grid_areas = iris.analysis.cartography.area_weights(MOHCCCLM85_50_C)
    MOHCKNMI85_50_C_grid_areas = iris.analysis.cartography.area_weights(MOHCKNMI85_50_C)
    MOHCSMHI85_50_C_grid_areas = iris.analysis.cartography.area_weights(MOHCSMHI85_50_C)
    MPICCLM85_50_C_grid_areas = iris.analysis.cartography.area_weights(MPICCLM85_50_C)
    MPIREMO85_50_C_grid_areas = iris.analysis.cartography.area_weights(MPIREMO85_50_C)
    MPISMHI85_50_C_grid_areas = iris.analysis.cartography.area_weights(MPISMHI85_50_C)
    NCCSMHI85_50_C_grid_areas = iris.analysis.cartography.area_weights(NCCSMHI85_50_C)
    NOAA85_50_C_grid_areas = iris.analysis.cartography.area_weights(NOAA85_50_C)
    
    CRU_C_grid_areas = iris.analysis.cartography.area_weights(CRU_C)
    UDel_C_grid_areas = iris.analysis.cartography.area_weights (UDel_C)
    GPCC_C_grid_areas = iris.analysis.cartography.area_weights (GPCC_C)
    
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
    IPSL_past_C_mean = IPSL_past_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=IPSL_past_C_grid_areas)
    MIROC_past_C_mean = MIROC_past_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MIROC_past_C_grid_areas)
    MOHCCCLM_past_C_mean = MOHCCCLM_past_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCCCLM_past_C_grid_areas)
    MOHCKNMI_past_C_mean = MOHCKNMI_past_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCKNMI_past_C_grid_areas)
    MOHCSMHI_past_C_mean = MOHCSMHI_past_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCSMHI_past_C_grid_areas)
    MPICCLM_past_C_mean = MPICCLM_past_C.collapsed(['latitude', 'longitude'],iris.analysis.MEAN, weights=MPICCLM_past_C_grid_areas)        
    MPIREMO_past_C_mean = MPIREMO_past_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MPIREMO_past_C_grid_areas)          
    MPISMHI_past_C_mean = MPISMHI_past_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MPISMHI_past_C_grid_areas)
    NCCSMHI_past_C_mean = NCCSMHI_past_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=NCCSMHI_past_C_grid_areas) 
    NOAA_past_C_mean = NOAA_past_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=NOAA_past_C_grid_areas)
    
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
    IPSL_30_C_mean = IPSL_30_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=IPSL_30_C_grid_areas)
    MIROC_30_C_mean = MIROC_30_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MIROC_30_C_grid_areas)
    MOHCCCLM_30_C_mean = MOHCCCLM_30_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCCCLM_30_C_grid_areas)
    MOHCKNMI_30_C_mean = MOHCKNMI_30_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCKNMI_30_C_grid_areas)
    MOHCSMHI_30_C_mean = MOHCSMHI_30_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCSMHI_30_C_grid_areas)
    MPICCLM_30_C_mean = MPICCLM_30_C.collapsed(['latitude', 'longitude'],iris.analysis.MEAN, weights=MPICCLM_30_C_grid_areas)        
    MPIREMO_30_C_mean = MPIREMO_30_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MPIREMO_30_C_grid_areas)                         
    MPISMHI_30_C_mean = MPISMHI_30_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MPISMHI_30_C_grid_areas)
    NCCSMHI_30_C_mean = NCCSMHI_30_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=NCCSMHI_30_C_grid_areas) 
    NOAA_30_C_mean = NOAA_30_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=NOAA_30_C_grid_areas)
    
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
    IPSL85_30_C_mean = IPSL85_30_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=IPSL85_30_C_grid_areas)
    MIROC85_30_C_mean = MIROC85_30_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MIROC85_30_C_grid_areas)
    MOHCCCLM85_30_C_mean = MOHCCCLM85_30_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCCCLM85_30_C_grid_areas)
    MOHCKNMI85_30_C_mean = MOHCKNMI85_30_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCKNMI85_30_C_grid_areas)
    MOHCSMHI85_30_C_mean = MOHCSMHI85_30_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCSMHI85_30_C_grid_areas)
    MPICCLM85_30_C_mean = MPICCLM85_30_C.collapsed(['latitude', 'longitude'],iris.analysis.MEAN, weights=MPICCLM85_30_C_grid_areas)        
    MPIREMO85_30_C_mean = MPIREMO85_30_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MPIREMO85_30_C_grid_areas)                         
    MPISMHI85_30_C_mean = MPISMHI85_30_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MPISMHI85_30_C_grid_areas)
    NCCSMHI85_30_C_mean = NCCSMHI85_30_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=NCCSMHI85_30_C_grid_areas) 
    NOAA85_30_C_mean = NOAA85_30_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=NOAA85_30_C_grid_areas)
    
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
    IPSL_50_C_mean = IPSL_50_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=IPSL_50_C_grid_areas)
    MIROC_50_C_mean = MIROC_50_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MIROC_50_C_grid_areas)
    MOHCCCLM_50_C_mean = MOHCCCLM_50_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCCCLM_50_C_grid_areas)
    MOHCKNMI_50_C_mean = MOHCKNMI_50_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCKNMI_50_C_grid_areas)
    MOHCSMHI_50_C_mean = MOHCSMHI_50_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCSMHI_50_C_grid_areas)
    MPICCLM_50_C_mean = MPICCLM_50_C.collapsed(['latitude', 'longitude'],iris.analysis.MEAN, weights=MPICCLM_50_C_grid_areas)        
    MPIREMO_50_C_mean = MPIREMO_50_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MPIREMO_50_C_grid_areas)                         
    MPISMHI_50_C_mean = MPISMHI_50_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MPISMHI_50_C_grid_areas)
    NCCSMHI_50_C_mean = NCCSMHI_50_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=NCCSMHI_50_C_grid_areas) 
    NOAA_50_C_mean = NOAA_50_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=NOAA_50_C_grid_areas)
    
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
    IPSL85_50_C_mean = IPSL85_50_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=IPSL85_50_C_grid_areas)
    MIROC85_50_C_mean = MIROC85_50_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MIROC85_50_C_grid_areas)
    MOHCCCLM85_50_C_mean = MOHCCCLM85_50_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCCCLM85_50_C_grid_areas)
    MOHCKNMI85_50_C_mean = MOHCKNMI85_50_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCKNMI85_50_C_grid_areas)
    MOHCSMHI85_50_C_mean = MOHCSMHI85_50_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCSMHI85_50_C_grid_areas)
    MPICCLM85_50_C_mean = MPICCLM85_50_C.collapsed(['latitude', 'longitude'],iris.analysis.MEAN, weights=MPICCLM85_50_C_grid_areas)        
    MPIREMO85_50_C_mean = MPIREMO85_50_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MPIREMO85_50_C_grid_areas)                         
    MPISMHI85_50_C_mean = MPISMHI85_50_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MPISMHI85_50_C_grid_areas)
    NCCSMHI85_50_C_mean = NCCSMHI85_50_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=NCCSMHI85_50_C_grid_areas) 
    NOAA85_50_C_mean = NOAA85_50_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=NOAA85_50_C_grid_areas)
    
    CRU_C_mean = CRU_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CRU_C_grid_areas)
    UDel_C_mean = UDel_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=UDel_C_grid_areas)
    GPCC_C_mean = GPCC_C.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=GPCC_C_grid_areas)
    
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
    IPSL_b_C_mean = IPSL_past_C_mean.collapsed(['time'], iris.analysis.MEAN) 
    MIROC_b_C_mean = MIROC_past_C_mean.collapsed(['time'], iris.analysis.MEAN) 
    MOHCCCLM_b_C_mean = MOHCCCLM_past_C_mean.collapsed(['time'], iris.analysis.MEAN) 
    MOHCKNMI_b_C_mean = MOHCKNMI_past_C_mean.collapsed(['time'], iris.analysis.MEAN) 
    MOHCSMHI_b_C_mean = MOHCSMHI_past_C_mean.collapsed(['time'], iris.analysis.MEAN) 
    MPICCLM_b_C_mean = MPICCLM_past_C_mean.collapsed(['time'], iris.analysis.MEAN)        
    MPIREMO_b_C_mean = MPIREMO_past_C_mean.collapsed(['time'], iris.analysis.MEAN)           
    MPISMHI_b_C_mean = MPISMHI_past_C_mean.collapsed(['time'], iris.analysis.MEAN) 
    NCCSMHI_b_C_mean = NCCSMHI_past_C_mean.collapsed(['time'], iris.analysis.MEAN)  
    NOAA_b_C_mean = NOAA_past_C_mean.collapsed(['time'], iris.analysis.MEAN)     
    
    CRU_C_mean = CRU_C_mean.collapsed(['time'], iris.analysis.MEAN)     
    UDel_C_mean = UDel_C_mean.collapsed(['time'], iris.analysis.MEAN) 
    GPCC_C_mean = GPCC_C_mean.collapsed(['time'], iris.analysis.MEAN)
    
    #create average of observed baseline data
    Obs_C = (CRU_C_mean + UDel_C_mean + GPCC_C_mean)/3  
    
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
    IPSL_past_C_mean = (IPSL_past_C_mean.data - IPSL_b_C_mean.data + Obs_C.data)
    MIROC_past_C_mean = (MIROC_past_C_mean.data - MIROC_b_C_mean.data + Obs_C.data)
    MOHCCCLM_past_C_mean = (MOHCCCLM_past_C_mean.data - MOHCCCLM_b_C_mean.data + Obs_C.data)
    MOHCKNMI_past_C_mean = (MOHCKNMI_past_C_mean.data - MOHCKNMI_b_C_mean.data + Obs_C.data)
    MOHCSMHI_past_C_mean = (MOHCSMHI_past_C_mean.data - MOHCSMHI_b_C_mean.data + Obs_C.data)
    MPICCLM_past_C_mean = (MPICCLM_past_C_mean.data - MPICCLM_b_C_mean.data + Obs_C.data)      
    MPIREMO_past_C_mean = (MPIREMO_past_C_mean.data - MPIREMO_b_C_mean.data + Obs_C.data)                         
    MPISMHI_past_C_mean = (MPISMHI_past_C_mean.data - MPISMHI_b_C_mean.data + Obs_C.data)
    NCCSMHI_past_C_mean = (NCCSMHI_past_C_mean.data - NCCSMHI_b_C_mean.data + Obs_C.data) 
    NOAA_past_C_mean = (NOAA_past_C_mean.data - NOAA_b_C_mean.data + Obs_C.data)
    
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
    IPSL_30_C_mean = (IPSL_30_C_mean.data - IPSL_b_C_mean.data + Obs_C.data)
    MIROC_30_C_mean = (MIROC_30_C_mean.data - MIROC_b_C_mean.data + Obs_C.data)
    MOHCCCLM_30_C_mean = (MOHCCCLM_30_C_mean.data - MOHCCCLM_b_C_mean.data + Obs_C.data)
    MOHCKNMI_30_C_mean = (MOHCKNMI_30_C_mean.data - MOHCKNMI_b_C_mean.data + Obs_C.data)
    MOHCSMHI_30_C_mean = (MOHCSMHI_30_C_mean.data - MOHCSMHI_b_C_mean.data + Obs_C.data)
    MPICCLM_30_C_mean = (MPICCLM_30_C_mean.data - MPICCLM_b_C_mean.data + Obs_C.data)      
    MPIREMO_30_C_mean = (MPIREMO_30_C_mean.data - MPIREMO_b_C_mean.data + Obs_C.data)                         
    MPISMHI_30_C_mean = (MPISMHI_30_C_mean.data - MPISMHI_b_C_mean.data + Obs_C.data)
    NCCSMHI_30_C_mean = (NCCSMHI_30_C_mean.data - NCCSMHI_b_C_mean.data + Obs_C.data) 
    NOAA_30_C_mean = (NOAA_30_C_mean.data - NOAA_b_C_mean.data + Obs_C.data)
    
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
    IPSL85_30_C_mean = (IPSL85_30_C_mean.data - IPSL_b_C_mean.data + Obs_C.data)
    MIROC85_30_C_mean = (MIROC85_30_C_mean.data - MIROC_b_C_mean.data + Obs_C.data)
    MOHCCCLM85_30_C_mean = (MOHCCCLM85_30_C_mean.data - MOHCCCLM_b_C_mean.data + Obs_C.data)
    MOHCKNMI85_30_C_mean = (MOHCKNMI85_30_C_mean.data - MOHCKNMI_b_C_mean.data + Obs_C.data)
    MOHCSMHI85_30_C_mean = (MOHCSMHI85_30_C_mean.data - MOHCSMHI_b_C_mean.data + Obs_C.data)
    MPICCLM85_30_C_mean = (MPICCLM85_30_C_mean.data - MPICCLM_b_C_mean.data + Obs_C.data)      
    MPIREMO85_30_C_mean = (MPIREMO85_30_C_mean.data - MPIREMO_b_C_mean.data + Obs_C.data)                         
    MPISMHI85_30_C_mean = (MPISMHI85_30_C_mean.data - MPISMHI_b_C_mean.data + Obs_C.data)
    NCCSMHI85_30_C_mean = (NCCSMHI85_30_C_mean.data - NCCSMHI_b_C_mean.data + Obs_C.data) 
    NOAA85_30_C_mean = (NOAA85_30_C_mean.data - NOAA_b_C_mean.data + Obs_C.data)
    
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
    IPSL_50_C_mean = (IPSL_50_C_mean.data - IPSL_b_C_mean.data + Obs_C.data)
    MIROC_50_C_mean = (MIROC_50_C_mean.data - MIROC_b_C_mean.data + Obs_C.data)
    MOHCCCLM_50_C_mean = (MOHCCCLM_50_C_mean.data - MOHCCCLM_b_C_mean.data + Obs_C.data)
    MOHCKNMI_50_C_mean = (MOHCKNMI_50_C_mean.data - MOHCKNMI_b_C_mean.data + Obs_C.data)
    MOHCSMHI_50_C_mean = (MOHCSMHI_50_C_mean.data - MOHCSMHI_b_C_mean.data + Obs_C.data)
    MPICCLM_50_C_mean = (MPICCLM_50_C_mean.data - MPICCLM_b_C_mean.data + Obs_C.data)      
    MPIREMO_50_C_mean = (MPIREMO_50_C_mean.data - MPIREMO_b_C_mean.data + Obs_C.data)                         
    MPISMHI_50_C_mean = (MPISMHI_50_C_mean.data - MPISMHI_b_C_mean.data + Obs_C.data)
    NCCSMHI_50_C_mean = (NCCSMHI_50_C_mean.data - NCCSMHI_b_C_mean.data + Obs_C.data) 
    NOAA_50_C_mean = (NOAA_50_C_mean.data - NOAA_b_C_mean.data + Obs_C.data)
    
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
    IPSL85_50_C_mean = (IPSL85_50_C_mean.data - IPSL_b_C_mean.data + Obs_C.data)
    MIROC85_50_C_mean = (MIROC85_50_C_mean.data - MIROC_b_C_mean.data + Obs_C.data)
    MOHCCCLM85_50_C_mean = (MOHCCCLM85_50_C_mean.data - MOHCCCLM_b_C_mean.data + Obs_C.data)
    MOHCKNMI85_50_C_mean = (MOHCKNMI85_50_C_mean.data - MOHCKNMI_b_C_mean.data + Obs_C.data)
    MOHCSMHI85_50_C_mean = (MOHCSMHI85_50_C_mean.data - MOHCSMHI_b_C_mean.data + Obs_C.data)
    MPICCLM85_50_C_mean = (MPICCLM85_50_C_mean.data - MPICCLM_b_C_mean.data + Obs_C.data)      
    MPIREMO85_50_C_mean = (MPIREMO85_50_C_mean.data - MPIREMO_b_C_mean.data + Obs_C.data)                         
    MPISMHI85_50_C_mean = (MPISMHI85_50_C_mean.data - MPISMHI_b_C_mean.data + Obs_C.data)
    NCCSMHI85_50_C_mean = (NCCSMHI85_50_C_mean.data - NCCSMHI_b_C_mean.data + Obs_C.data) 
    NOAA85_50_C_mean = (NOAA85_50_C_mean.data - NOAA_b_C_mean.data + Obs_C.data)
    
    
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
    IPSL_past_S = IPSL_past.extract(Southern_Malawi)
    MIROC_past_S = MIROC_past.extract(Southern_Malawi)
    MOHCCCLM_past_S = MOHCCCLM_past.extract(Southern_Malawi)
    MOHCKNMI_past_S = MOHCKNMI_past.extract(Southern_Malawi)
    MOHCSMHI_past_S = MOHCSMHI_past.extract(Southern_Malawi)
    MPICCLM_past_S = MPICCLM_past.extract(Southern_Malawi)
    MPIREMO_past_S = MPIREMO_past.extract(Southern_Malawi)
    MPISMHI_past_S = MPISMHI_past.extract(Southern_Malawi)
    NCCSMHI_past_S = NCCSMHI_past.extract(Southern_Malawi)
    NOAA_past_S = NOAA_past.extract(Southern_Malawi)
    
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
    IPSL_30_S = IPSL_30.extract(Southern_Malawi)
    MIROC_30_S = MIROC_30.extract(Southern_Malawi)
    MOHCCCLM_30_S = MOHCCCLM_30.extract(Southern_Malawi)
    MOHCKNMI_30_S = MOHCKNMI_30.extract(Southern_Malawi)
    MOHCSMHI_30_S = MOHCSMHI_30.extract(Southern_Malawi)
    MPICCLM_30_S = MPICCLM_30.extract(Southern_Malawi)
    MPIREMO_30_S = MPIREMO_30.extract(Southern_Malawi)
    MPISMHI_30_S = MPISMHI_30.extract(Southern_Malawi)
    NCCSMHI_30_S = NCCSMHI_30.extract(Southern_Malawi)
    NOAA_30_S = NOAA_30.extract(Southern_Malawi)
    
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
    IPSL85_30_S = IPSL85_30.extract(Southern_Malawi)
    MIROC85_30_S = MIROC85_30.extract(Southern_Malawi)
    MOHCCCLM85_30_S = MOHCCCLM85_30.extract(Southern_Malawi)
    MOHCKNMI85_30_S = MOHCKNMI85_30.extract(Southern_Malawi)
    MOHCSMHI85_30_S = MOHCSMHI85_30.extract(Southern_Malawi)
    MPICCLM85_30_S = MPICCLM85_30.extract(Southern_Malawi)
    MPIREMO85_30_S = MPIREMO85_30.extract(Southern_Malawi)
    MPISMHI85_30_S = MPISMHI85_30.extract(Southern_Malawi)
    NCCSMHI85_30_S = NCCSMHI85_30.extract(Southern_Malawi)
    NOAA85_30_S = NOAA85_30.extract(Southern_Malawi)
    
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
    IPSL_50_S = IPSL_50.extract(Southern_Malawi)
    MIROC_50_S = MIROC_50.extract(Southern_Malawi)
    MOHCCCLM_50_S = MOHCCCLM_50.extract(Southern_Malawi)
    MOHCKNMI_50_S = MOHCKNMI_50.extract(Southern_Malawi)
    MOHCSMHI_50_S = MOHCSMHI_50.extract(Southern_Malawi)
    MPICCLM_50_S = MPICCLM_50.extract(Southern_Malawi)
    MPIREMO_50_S = MPIREMO_50.extract(Southern_Malawi)
    MPISMHI_50_S = MPISMHI_50.extract(Southern_Malawi)
    NCCSMHI_50_S = NCCSMHI_50.extract(Southern_Malawi)
    NOAA_50_S = NOAA_50.extract(Southern_Malawi)
    
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
    IPSL85_50_S = IPSL85_50.extract(Southern_Malawi)
    MIROC85_50_S = MIROC85_50.extract(Southern_Malawi)
    MOHCCCLM85_50_S = MOHCCCLM85_50.extract(Southern_Malawi)
    MOHCKNMI85_50_S = MOHCKNMI85_50.extract(Southern_Malawi)
    MOHCSMHI85_50_S = MOHCSMHI85_50.extract(Southern_Malawi)
    MPICCLM85_50_S = MPICCLM85_50.extract(Southern_Malawi)
    MPIREMO85_50_S = MPIREMO85_50.extract(Southern_Malawi)
    MPISMHI85_50_S = MPISMHI85_50.extract(Southern_Malawi)
    NCCSMHI85_50_S = NCCSMHI85_50.extract(Southern_Malawi)
    NOAA85_50_S = NOAA85_50.extract(Southern_Malawi)
    
    CRU_S = CRU.extract(Southern_Malawi)
    UDel_S = UDel.extract(Southern_Malawi)
    GPCC_S = GPCC.extract(Southern_Malawi)
    
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
    IPSL_past_S = IPSL_past_S.aggregated_by('day_of_year', iris.analysis.MEAN)
    MIROC_past_S = MIROC_past_S.aggregated_by('day_of_year', iris.analysis.MEAN)
    MOHCCCLM_past_S = MOHCCCLM_past_S.aggregated_by('day_of_year', iris.analysis.MEAN)
    MOHCKNMI_past_S = MOHCKNMI_past_S.aggregated_by('day_of_year', iris.analysis.MEAN)
    MOHCSMHI_past_S = MOHCSMHI_past_S.aggregated_by('day_of_year', iris.analysis.MEAN)
    MPICCLM_past_S = MPICCLM_past_S.aggregated_by('day_of_year', iris.analysis.MEAN)
    MPIREMO_past_S = MPIREMO_past_S.aggregated_by('day_of_year', iris.analysis.MEAN)
    MPISMHI_past_S = MPISMHI_past_S.aggregated_by('day_of_year', iris.analysis.MEAN)
    NCCSMHI_past_S = NCCSMHI_past_S.aggregated_by('day_of_year', iris.analysis.MEAN)
    NOAA_past_S = NOAA_past_S.aggregated_by('day_of_year', iris.analysis.MEAN)
    
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
    IPSL_30_S = IPSL_30_S.aggregated_by('day_of_year', iris.analysis.MEAN)
    MIROC_30_S = MIROC_30_S.aggregated_by('day_of_year', iris.analysis.MEAN)
    MOHCCCLM_30_S = MOHCCCLM_30_S.aggregated_by('day_of_year', iris.analysis.MEAN)
    MOHCKNMI_30_S = MOHCKNMI_30_S.aggregated_by('day_of_year', iris.analysis.MEAN)
    MOHCSMHI_30_S = MOHCSMHI_30_S.aggregated_by('day_of_year', iris.analysis.MEAN)
    MPICCLM_30_S = MPICCLM_30_S.aggregated_by('day_of_year', iris.analysis.MEAN)
    MPIREMO_30_S = MPIREMO_30_S.aggregated_by('day_of_year', iris.analysis.MEAN)
    MPISMHI_30_S = MPISMHI_30_S.aggregated_by('day_of_year', iris.analysis.MEAN)
    NCCSMHI_30_S = NCCSMHI_30_S.aggregated_by('day_of_year', iris.analysis.MEAN)
    NOAA_30_S = NOAA_30_S.aggregated_by('day_of_year', iris.analysis.MEAN)
    
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
    IPSL85_30_S = IPSL85_30_S.aggregated_by('day_of_year', iris.analysis.MEAN)
    MIROC85_30_S = MIROC85_30_S.aggregated_by('day_of_year', iris.analysis.MEAN)
    MOHCCCLM85_30_S = MOHCCCLM85_30_S.aggregated_by('day_of_year', iris.analysis.MEAN)
    MOHCKNMI85_30_S = MOHCKNMI85_30_S.aggregated_by('day_of_year', iris.analysis.MEAN)
    MOHCSMHI85_30_S = MOHCSMHI85_30_S.aggregated_by('day_of_year', iris.analysis.MEAN)
    MPICCLM85_30_S = MPICCLM85_30_S.aggregated_by('day_of_year', iris.analysis.MEAN)
    MPIREMO85_30_S = MPIREMO85_30_S.aggregated_by('day_of_year', iris.analysis.MEAN)
    MPISMHI85_30_S = MPISMHI85_30_S.aggregated_by('day_of_year', iris.analysis.MEAN)
    NCCSMHI85_30_S = NCCSMHI85_30_S.aggregated_by('day_of_year', iris.analysis.MEAN)
    NOAA85_30_S = NOAA85_30_S.aggregated_by('day_of_year', iris.analysis.MEAN)
    
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
    IPSL_50_S = IPSL_50_S.aggregated_by('day_of_year', iris.analysis.MEAN)
    MIROC_50_S = MIROC_50_S.aggregated_by('day_of_year', iris.analysis.MEAN)
    MOHCCCLM_50_S = MOHCCCLM_50_S.aggregated_by('day_of_year', iris.analysis.MEAN)
    MOHCKNMI_50_S = MOHCKNMI_50_S.aggregated_by('day_of_year', iris.analysis.MEAN)
    MOHCSMHI_50_S = MOHCSMHI_50_S.aggregated_by('day_of_year', iris.analysis.MEAN)
    MPICCLM_50_S = MPICCLM_50_S.aggregated_by('day_of_year', iris.analysis.MEAN)
    MPIREMO_50_S = MPIREMO_50_S.aggregated_by('day_of_year', iris.analysis.MEAN)
    MPISMHI_50_S = MPISMHI_50_S.aggregated_by('day_of_year', iris.analysis.MEAN)
    NCCSMHI_50_S = NCCSMHI_50_S.aggregated_by('day_of_year', iris.analysis.MEAN)
    NOAA_50_S = NOAA_50_S.aggregated_by('day_of_year', iris.analysis.MEAN)
    
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
    IPSL85_50_S = IPSL85_50_S.aggregated_by('day_of_year', iris.analysis.MEAN)
    MIROC85_50_S = MIROC85_50_S.aggregated_by('day_of_year', iris.analysis.MEAN)
    MOHCCCLM85_50_S = MOHCCCLM85_50_S.aggregated_by('day_of_year', iris.analysis.MEAN)
    MOHCKNMI85_50_S = MOHCKNMI85_50_S.aggregated_by('day_of_year', iris.analysis.MEAN)
    MOHCSMHI85_50_S = MOHCSMHI85_50_S.aggregated_by('day_of_year', iris.analysis.MEAN)
    MPICCLM85_50_S = MPICCLM85_50_S.aggregated_by('day_of_year', iris.analysis.MEAN)
    MPIREMO85_50_S = MPIREMO85_50_S.aggregated_by('day_of_year', iris.analysis.MEAN)
    MPISMHI85_50_S = MPISMHI85_50_S.aggregated_by('day_of_year', iris.analysis.MEAN)
    NCCSMHI85_50_S = NCCSMHI85_50_S.aggregated_by('day_of_year', iris.analysis.MEAN)
    NOAA85_50_S = NOAA85_50_S.aggregated_by('day_of_year', iris.analysis.MEAN)
    
    CRU_S = CRU_S.aggregated_by('day_of_year', iris.analysis.MEAN)
    UDel_S = UDel_S.aggregated_by('day_of_year', iris.analysis.MEAN)
    GPCC_S = GPCC_S.aggregated_by('day_of_year', iris.analysis.MEAN)
    
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
    IPSL_past_S_grid_areas = iris.analysis.cartography.area_weights(IPSL_past_S)
    MIROC_past_S_grid_areas = iris.analysis.cartography.area_weights(MIROC_past_S)
    MOHCCCLM_past_S_grid_areas = iris.analysis.cartography.area_weights(MOHCCCLM_past_S)
    MOHCKNMI_past_S_grid_areas = iris.analysis.cartography.area_weights(MOHCKNMI_past_S)
    MOHCSMHI_past_S_grid_areas = iris.analysis.cartography.area_weights(MOHCSMHI_past_S)
    MPICCLM_past_S_grid_areas = iris.analysis.cartography.area_weights(MPICCLM_past_S)
    MPIREMO_past_S_grid_areas = iris.analysis.cartography.area_weights(MPIREMO_past_S)
    MPISMHI_past_S_grid_areas = iris.analysis.cartography.area_weights(MPISMHI_past_S)
    NCCSMHI_past_S_grid_areas = iris.analysis.cartography.area_weights(NCCSMHI_past_S)
    NOAA_past_S_grid_areas = iris.analysis.cartography.area_weights(NOAA_past_S)
    
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
    IPSL_30_S_grid_areas = iris.analysis.cartography.area_weights(IPSL_30_S)
    MIROC_30_S_grid_areas = iris.analysis.cartography.area_weights(MIROC_30_S)
    MOHCCCLM_30_S_grid_areas = iris.analysis.cartography.area_weights(MOHCCCLM_30_S)
    MOHCKNMI_30_S_grid_areas = iris.analysis.cartography.area_weights(MOHCKNMI_30_S)
    MOHCSMHI_30_S_grid_areas = iris.analysis.cartography.area_weights(MOHCSMHI_30_S)
    MPICCLM_30_S_grid_areas = iris.analysis.cartography.area_weights(MPICCLM_30_S)
    MPIREMO_30_S_grid_areas = iris.analysis.cartography.area_weights(MPIREMO_30_S)
    MPISMHI_30_S_grid_areas = iris.analysis.cartography.area_weights(MPISMHI_30_S)
    NCCSMHI_30_S_grid_areas = iris.analysis.cartography.area_weights(NCCSMHI_30_S)
    NOAA_30_S_grid_areas = iris.analysis.cartography.area_weights(NOAA_30_S)
    
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
    IPSL85_30_S_grid_areas = iris.analysis.cartography.area_weights(IPSL85_30_S)
    MIROC85_30_S_grid_areas = iris.analysis.cartography.area_weights(MIROC85_30_S)
    MOHCCCLM85_30_S_grid_areas = iris.analysis.cartography.area_weights(MOHCCCLM85_30_S)
    MOHCKNMI85_30_S_grid_areas = iris.analysis.cartography.area_weights(MOHCKNMI85_30_S)
    MOHCSMHI85_30_S_grid_areas = iris.analysis.cartography.area_weights(MOHCSMHI85_30_S)
    MPICCLM85_30_S_grid_areas = iris.analysis.cartography.area_weights(MPICCLM85_30_S)
    MPIREMO85_30_S_grid_areas = iris.analysis.cartography.area_weights(MPIREMO85_30_S)
    MPISMHI85_30_S_grid_areas = iris.analysis.cartography.area_weights(MPISMHI85_30_S)
    NCCSMHI85_30_S_grid_areas = iris.analysis.cartography.area_weights(NCCSMHI85_30_S)
    NOAA85_30_S_grid_areas = iris.analysis.cartography.area_weights(NOAA85_30_S)
    
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
    IPSL_50_S_grid_areas = iris.analysis.cartography.area_weights(IPSL_50_S)
    MIROC_50_S_grid_areas = iris.analysis.cartography.area_weights(MIROC_50_S)
    MOHCCCLM_50_S_grid_areas = iris.analysis.cartography.area_weights(MOHCCCLM_50_S)
    MOHCKNMI_50_S_grid_areas = iris.analysis.cartography.area_weights(MOHCKNMI_50_S)
    MOHCSMHI_50_S_grid_areas = iris.analysis.cartography.area_weights(MOHCSMHI_50_S)
    MPICCLM_50_S_grid_areas = iris.analysis.cartography.area_weights(MPICCLM_50_S)
    MPIREMO_50_S_grid_areas = iris.analysis.cartography.area_weights(MPIREMO_50_S)
    MPISMHI_50_S_grid_areas = iris.analysis.cartography.area_weights(MPISMHI_50_S)
    NCCSMHI_50_S_grid_areas = iris.analysis.cartography.area_weights(NCCSMHI_50_S)
    NOAA_50_S_grid_areas = iris.analysis.cartography.area_weights(NOAA_50_S)
    
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
    IPSL85_50_S_grid_areas = iris.analysis.cartography.area_weights(IPSL85_50_S)
    MIROC85_50_S_grid_areas = iris.analysis.cartography.area_weights(MIROC85_50_S)
    MOHCCCLM85_50_S_grid_areas = iris.analysis.cartography.area_weights(MOHCCCLM85_50_S)
    MOHCKNMI85_50_S_grid_areas = iris.analysis.cartography.area_weights(MOHCKNMI85_50_S)
    MOHCSMHI85_50_S_grid_areas = iris.analysis.cartography.area_weights(MOHCSMHI85_50_S)
    MPICCLM85_50_S_grid_areas = iris.analysis.cartography.area_weights(MPICCLM85_50_S)
    MPIREMO85_50_S_grid_areas = iris.analysis.cartography.area_weights(MPIREMO85_50_S)
    MPISMHI85_50_S_grid_areas = iris.analysis.cartography.area_weights(MPISMHI85_50_S)
    NCCSMHI85_50_S_grid_areas = iris.analysis.cartography.area_weights(NCCSMHI85_50_S)
    NOAA85_50_S_grid_areas = iris.analysis.cartography.area_weights(NOAA85_50_S)
    
    CRU_S_grid_areas = iris.analysis.cartography.area_weights(CRU_S)
    UDel_S_grid_areas = iris.analysis.cartography.area_weights (UDel_S)
    GPCC_S_grid_areas = iris.analysis.cartography.area_weights (GPCC_S)
    
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
    IPSL_past_S_mean = IPSL_past_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=IPSL_past_S_grid_areas)
    MIROC_past_S_mean = MIROC_past_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MIROC_past_S_grid_areas)
    MOHCCCLM_past_S_mean = MOHCCCLM_past_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCCCLM_past_S_grid_areas)
    MOHCKNMI_past_S_mean = MOHCKNMI_past_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCKNMI_past_S_grid_areas)
    MOHCSMHI_past_S_mean = MOHCSMHI_past_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCSMHI_past_S_grid_areas)
    MPICCLM_past_S_mean = MPICCLM_past_S.collapsed(['latitude', 'longitude'],iris.analysis.MEAN, weights=MPICCLM_past_S_grid_areas)        
    MPIREMO_past_S_mean = MPIREMO_past_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MPIREMO_past_S_grid_areas)          
    MPISMHI_past_S_mean = MPISMHI_past_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MPISMHI_past_S_grid_areas)
    NCCSMHI_past_S_mean = NCCSMHI_past_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=NCCSMHI_past_S_grid_areas) 
    NOAA_past_S_mean = NOAA_past_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=NOAA_past_S_grid_areas)
    
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
    IPSL_30_S_mean = IPSL_30_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=IPSL_30_S_grid_areas)
    MIROC_30_S_mean = MIROC_30_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MIROC_30_S_grid_areas)
    MOHCCCLM_30_S_mean = MOHCCCLM_30_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCCCLM_30_S_grid_areas)
    MOHCKNMI_30_S_mean = MOHCKNMI_30_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCKNMI_30_S_grid_areas)
    MOHCSMHI_30_S_mean = MOHCSMHI_30_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCSMHI_30_S_grid_areas)
    MPICCLM_30_S_mean = MPICCLM_30_S.collapsed(['latitude', 'longitude'],iris.analysis.MEAN, weights=MPICCLM_30_S_grid_areas)        
    MPIREMO_30_S_mean = MPIREMO_30_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MPIREMO_30_S_grid_areas)                         
    MPISMHI_30_S_mean = MPISMHI_30_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MPISMHI_30_S_grid_areas)
    NCCSMHI_30_S_mean = NCCSMHI_30_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=NCCSMHI_30_S_grid_areas) 
    NOAA_30_S_mean = NOAA_30_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=NOAA_30_S_grid_areas)
    
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
    IPSL85_30_S_mean = IPSL85_30_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=IPSL85_30_S_grid_areas)
    MIROC85_30_S_mean = MIROC85_30_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MIROC85_30_S_grid_areas)
    MOHCCCLM85_30_S_mean = MOHCCCLM85_30_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCCCLM85_30_S_grid_areas)
    MOHCKNMI85_30_S_mean = MOHCKNMI85_30_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCKNMI85_30_S_grid_areas)
    MOHCSMHI85_30_S_mean = MOHCSMHI85_30_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCSMHI85_30_S_grid_areas)
    MPICCLM85_30_S_mean = MPICCLM85_30_S.collapsed(['latitude', 'longitude'],iris.analysis.MEAN, weights=MPICCLM85_30_S_grid_areas)        
    MPIREMO85_30_S_mean = MPIREMO85_30_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MPIREMO85_30_S_grid_areas)                         
    MPISMHI85_30_S_mean = MPISMHI85_30_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MPISMHI85_30_S_grid_areas)
    NCCSMHI85_30_S_mean = NCCSMHI85_30_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=NCCSMHI85_30_S_grid_areas) 
    NOAA85_30_S_mean = NOAA85_30_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=NOAA85_30_S_grid_areas)
    
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
    IPSL_50_S_mean = IPSL_50_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=IPSL_50_S_grid_areas)
    MIROC_50_S_mean = MIROC_50_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MIROC_50_S_grid_areas)
    MOHCCCLM_50_S_mean = MOHCCCLM_50_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCCCLM_50_S_grid_areas)
    MOHCKNMI_50_S_mean = MOHCKNMI_50_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCKNMI_50_S_grid_areas)
    MOHCSMHI_50_S_mean = MOHCSMHI_50_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCSMHI_50_S_grid_areas)
    MPICCLM_50_S_mean = MPICCLM_50_S.collapsed(['latitude', 'longitude'],iris.analysis.MEAN, weights=MPICCLM_50_S_grid_areas)        
    MPIREMO_50_S_mean = MPIREMO_50_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MPIREMO_50_S_grid_areas)                         
    MPISMHI_50_S_mean = MPISMHI_50_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MPISMHI_50_S_grid_areas)
    NCCSMHI_50_S_mean = NCCSMHI_50_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=NCCSMHI_50_S_grid_areas) 
    NOAA_50_S_mean = NOAA_50_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=NOAA_50_S_grid_areas)
    
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
    IPSL85_50_S_mean = IPSL85_50_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=IPSL85_50_S_grid_areas)
    MIROC85_50_S_mean = MIROC85_50_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MIROC85_50_S_grid_areas)
    MOHCCCLM85_50_S_mean = MOHCCCLM85_50_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCCCLM85_50_S_grid_areas)
    MOHCKNMI85_50_S_mean = MOHCKNMI85_50_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCKNMI85_50_S_grid_areas)
    MOHCSMHI85_50_S_mean = MOHCSMHI85_50_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCSMHI85_50_S_grid_areas)
    MPICCLM85_50_S_mean = MPICCLM85_50_S.collapsed(['latitude', 'longitude'],iris.analysis.MEAN, weights=MPICCLM85_50_S_grid_areas)        
    MPIREMO85_50_S_mean = MPIREMO85_50_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MPIREMO85_50_S_grid_areas)                         
    MPISMHI85_50_S_mean = MPISMHI85_50_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MPISMHI85_50_S_grid_areas)
    NCCSMHI85_50_S_mean = NCCSMHI85_50_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=NCCSMHI85_50_S_grid_areas) 
    NOAA85_50_S_mean = NOAA85_50_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=NOAA85_50_S_grid_areas)
    
    CRU_S_mean = CRU_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CRU_S_grid_areas)
    UDel_S_mean = UDel_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=UDel_S_grid_areas)
    GPCC_S_mean = GPCC_S.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=GPCC_S_grid_areas)
    
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
    IPSL_b_S_mean = IPSL_past_S_mean.collapsed(['time'], iris.analysis.MEAN) 
    MIROC_b_S_mean = MIROC_past_S_mean.collapsed(['time'], iris.analysis.MEAN) 
    MOHCCCLM_b_S_mean = MOHCCCLM_past_S_mean.collapsed(['time'], iris.analysis.MEAN) 
    MOHCKNMI_b_S_mean = MOHCKNMI_past_S_mean.collapsed(['time'], iris.analysis.MEAN) 
    MOHCSMHI_b_S_mean = MOHCSMHI_past_S_mean.collapsed(['time'], iris.analysis.MEAN) 
    MPICCLM_b_S_mean = MPICCLM_past_S_mean.collapsed(['time'], iris.analysis.MEAN)        
    MPIREMO_b_S_mean = MPIREMO_past_S_mean.collapsed(['time'], iris.analysis.MEAN)           
    MPISMHI_b_S_mean = MPISMHI_past_S_mean.collapsed(['time'], iris.analysis.MEAN) 
    NCCSMHI_b_S_mean = NCCSMHI_past_S_mean.collapsed(['time'], iris.analysis.MEAN)  
    NOAA_b_S_mean = NOAA_past_S_mean.collapsed(['time'], iris.analysis.MEAN)     
    
    CRU_S_mean = CRU_S_mean.collapsed(['time'], iris.analysis.MEAN)     
    UDel_S_mean = UDel_S_mean.collapsed(['time'], iris.analysis.MEAN) 
    GPCC_S_mean = GPCC_S_mean.collapsed(['time'], iris.analysis.MEAN)
    
    #create average of observed baseline data
    Obs_S = (CRU_S_mean + UDel_S_mean + GPCC_S_mean)/3  
    
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
    IPSL_past_S_mean = (IPSL_past_S_mean.data - IPSL_b_S_mean.data + Obs_S.data)
    MIROC_past_S_mean = (MIROC_past_S_mean.data - MIROC_b_S_mean.data + Obs_S.data)
    MOHCCCLM_past_S_mean = (MOHCCCLM_past_S_mean.data - MOHCCCLM_b_S_mean.data + Obs_S.data)
    MOHCKNMI_past_S_mean = (MOHCKNMI_past_S_mean.data - MOHCKNMI_b_S_mean.data + Obs_S.data)
    MOHCSMHI_past_S_mean = (MOHCSMHI_past_S_mean.data - MOHCSMHI_b_S_mean.data + Obs_S.data)
    MPICCLM_past_S_mean = (MPICCLM_past_S_mean.data - MPICCLM_b_S_mean.data + Obs_S.data)      
    MPIREMO_past_S_mean = (MPIREMO_past_S_mean.data - MPIREMO_b_S_mean.data + Obs_S.data)                         
    MPISMHI_past_S_mean = (MPISMHI_past_S_mean.data - MPISMHI_b_S_mean.data + Obs_S.data)
    NCCSMHI_past_S_mean = (NCCSMHI_past_S_mean.data - NCCSMHI_b_S_mean.data + Obs_S.data) 
    NOAA_past_S_mean = (NOAA_past_S_mean.data - NOAA_b_S_mean.data + Obs_S.data)
    
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
    IPSL_30_S_mean = (IPSL_30_S_mean.data - IPSL_b_S_mean.data + Obs_S.data)
    MIROC_30_S_mean = (MIROC_30_S_mean.data - MIROC_b_S_mean.data + Obs_S.data)
    MOHCCCLM_30_S_mean = (MOHCCCLM_30_S_mean.data - MOHCCCLM_b_S_mean.data + Obs_S.data)
    MOHCKNMI_30_S_mean = (MOHCKNMI_30_S_mean.data - MOHCKNMI_b_S_mean.data + Obs_S.data)
    MOHCSMHI_30_S_mean = (MOHCSMHI_30_S_mean.data - MOHCSMHI_b_S_mean.data + Obs_S.data)
    MPICCLM_30_S_mean = (MPICCLM_30_S_mean.data - MPICCLM_b_S_mean.data + Obs_S.data)      
    MPIREMO_30_S_mean = (MPIREMO_30_S_mean.data - MPIREMO_b_S_mean.data + Obs_S.data)                         
    MPISMHI_30_S_mean = (MPISMHI_30_S_mean.data - MPISMHI_b_S_mean.data + Obs_S.data)
    NCCSMHI_30_S_mean = (NCCSMHI_30_S_mean.data - NCCSMHI_b_S_mean.data + Obs_S.data) 
    NOAA_30_S_mean = (NOAA_30_S_mean.data - NOAA_b_S_mean.data + Obs_S.data)
    
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
    IPSL85_30_S_mean = (IPSL85_30_S_mean.data - IPSL_b_S_mean.data + Obs_S.data)
    MIROC85_30_S_mean = (MIROC85_30_S_mean.data - MIROC_b_S_mean.data + Obs_S.data)
    MOHCCCLM85_30_S_mean = (MOHCCCLM85_30_S_mean.data - MOHCCCLM_b_S_mean.data + Obs_S.data)
    MOHCKNMI85_30_S_mean = (MOHCKNMI85_30_S_mean.data - MOHCKNMI_b_S_mean.data + Obs_S.data)
    MOHCSMHI85_30_S_mean = (MOHCSMHI85_30_S_mean.data - MOHCSMHI_b_S_mean.data + Obs_S.data)
    MPICCLM85_30_S_mean = (MPICCLM85_30_S_mean.data - MPICCLM_b_S_mean.data + Obs_S.data)      
    MPIREMO85_30_S_mean = (MPIREMO85_30_S_mean.data - MPIREMO_b_S_mean.data + Obs_S.data)                         
    MPISMHI85_30_S_mean = (MPISMHI85_30_S_mean.data - MPISMHI_b_S_mean.data + Obs_S.data)
    NCCSMHI85_30_S_mean = (NCCSMHI85_30_S_mean.data - NCCSMHI_b_S_mean.data + Obs_S.data) 
    NOAA85_30_S_mean = (NOAA85_30_S_mean.data - NOAA_b_S_mean.data + Obs_S.data)
    
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
    IPSL_50_S_mean = (IPSL_50_S_mean.data - IPSL_b_S_mean.data + Obs_S.data)
    MIROC_50_S_mean = (MIROC_50_S_mean.data - MIROC_b_S_mean.data + Obs_S.data)
    MOHCCCLM_50_S_mean = (MOHCCCLM_50_S_mean.data - MOHCCCLM_b_S_mean.data + Obs_S.data)
    MOHCKNMI_50_S_mean = (MOHCKNMI_50_S_mean.data - MOHCKNMI_b_S_mean.data + Obs_S.data)
    MOHCSMHI_50_S_mean = (MOHCSMHI_50_S_mean.data - MOHCSMHI_b_S_mean.data + Obs_S.data)
    MPICCLM_50_S_mean = (MPICCLM_50_S_mean.data - MPICCLM_b_S_mean.data + Obs_S.data)      
    MPIREMO_50_S_mean = (MPIREMO_50_S_mean.data - MPIREMO_b_S_mean.data + Obs_S.data)                         
    MPISMHI_50_S_mean = (MPISMHI_50_S_mean.data - MPISMHI_b_S_mean.data + Obs_S.data)
    NCCSMHI_50_S_mean = (NCCSMHI_50_S_mean.data - NCCSMHI_b_S_mean.data + Obs_S.data) 
    NOAA_50_S_mean = (NOAA_50_S_mean.data - NOAA_b_S_mean.data + Obs_S.data)
    
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
    IPSL85_50_S_mean = (IPSL85_50_S_mean.data - IPSL_b_S_mean.data + Obs_S.data)
    MIROC85_50_S_mean = (MIROC85_50_S_mean.data - MIROC_b_S_mean.data + Obs_S.data)
    MOHCCCLM85_50_S_mean = (MOHCCCLM85_50_S_mean.data - MOHCCCLM_b_S_mean.data + Obs_S.data)
    MOHCKNMI85_50_S_mean = (MOHCKNMI85_50_S_mean.data - MOHCKNMI_b_S_mean.data + Obs_S.data)
    MOHCSMHI85_50_S_mean = (MOHCSMHI85_50_S_mean.data - MOHCSMHI_b_S_mean.data + Obs_S.data)
    MPICCLM85_50_S_mean = (MPICCLM85_50_S_mean.data - MPICCLM_b_S_mean.data + Obs_S.data)      
    MPIREMO85_50_S_mean = (MPIREMO85_50_S_mean.data - MPIREMO_b_S_mean.data + Obs_S.data)                         
    MPISMHI85_50_S_mean = (MPISMHI85_50_S_mean.data - MPISMHI_b_S_mean.data + Obs_S.data)
    NCCSMHI85_50_S_mean = (NCCSMHI85_50_S_mean.data - NCCSMHI_b_S_mean.data + Obs_S.data) 
    NOAA85_50_S_mean = (NOAA85_50_S_mean.data - NOAA_b_S_mean.data + Obs_S.data)
    
    
    #-------------------------------------------------------------------------
    #PART 6: PRINT DATA
    import csv
    with open('output_AquaCrop_Data_Pr.csv', 'wb') as csvfile:
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
        writer.writerow(["IPSL_past_N_mean"] +IPSL_past_N_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MIROC_past_N_mean"] +MIROC_past_N_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MOHCCCLM_past_N_mean"] +MOHCCCLM_past_N_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MOHCKNMI_past_N_mean"] +MOHCKNMI_past_N_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MOHCSMHI_past_N_mean"] +MOHCSMHI_past_N_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MPICCLM_past_N_mean"] +MPICCLM_past_N_mean.data.flatten().astype(np.str).tolist())    
        writer.writerow(["MPIREMO_past_N_mean"] +MPIREMO_past_N_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["MPISMHI_past_N_mean"] +MPISMHI_past_N_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["NCCSMHI_past_N_mean"] +NCCSMHI_past_N_mean.data.flatten().astype(np.str).tolist())       
        writer.writerow(["NOAA_past_N_mean"] +NOAA_past_N_mean.data.flatten().astype(np.str).tolist())     
        
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
        writer.writerow(["IPSL_30_N_mean"] +IPSL_30_N_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MIROC_30_N_mean"] +MIROC_30_N_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MOHCCCLM_30_N_mean"] +MOHCCCLM_30_N_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MOHCKNMI_30_N_mean"] +MOHCKNMI_30_N_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MOHCSMHI_30_N_mean"] +MOHCSMHI_30_N_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MPICCLM_30_N_mean"] +MPICCLM_30_N_mean.data.flatten().astype(np.str).tolist())    
        writer.writerow(["MPIREMO_30_N_mean"] +MPIREMO_30_N_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["MPISMHI_30_N_mean"] +MPISMHI_30_N_mean.data.flatten().astype(np.str).tolist())        
        writer.writerow(["NCCSMHI_30_N_mean"] +NCCSMHI_30_N_mean.data.flatten().astype(np.str).tolist())       
        writer.writerow(["NOAA_30_N_mean"] +NOAA_30_N_mean.data.flatten().astype(np.str).tolist()) 
        
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
        writer.writerow(["IPSL85_30_N_mean"] +IPSL85_30_N_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MIROC85_30_N_mean"] +MIROC85_30_N_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MOHCCCLM85_30_N_mean"] +MOHCCCLM85_30_N_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["MOHCKNMI85_30_N_mean"] +MOHCKNMI85_30_N_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["MOHCSMHI85_30_N_mean"] +MOHCSMHI85_30_N_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["MPICCLM85_30_N_mean"] +MPICCLM85_30_N_mean.data.flatten().astype(np.str).tolist())    
        writer.writerow(["MPIREMO85_30_N_mean"] +MPIREMO85_30_N_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["MPISMHI85_30_N_mean"] +MPISMHI85_30_N_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["NCCSMHI85_30_N_mean"] +NCCSMHI85_30_N_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["NOAA85_30_N_mean"] +NOAA85_30_N_mean.data.flatten().astype(np.str).tolist())  
        
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
        writer.writerow(["IPSL_50_N_mean"] +IPSL_50_N_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MIROC_50_N_mean"] +MIROC_50_N_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MOHCCCLM_50_N_mean"] +MOHCCCLM_50_N_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MOHCKNMI_50_N_mean"] +MOHCKNMI_50_N_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MOHCSMHI_50_N_mean"] +MOHCSMHI_50_N_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MPICCLM_50_N_mean"] +MPICCLM_50_N_mean.data.flatten().astype(np.str).tolist())    
        writer.writerow(["MPIREMO_50_N_mean"] +MPIREMO_50_N_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["MPISMHI_50_N_mean"] +MPISMHI_50_N_mean.data.flatten().astype(np.str).tolist())        
        writer.writerow(["NCCSMHI_50_N_mean"] +NCCSMHI_50_N_mean.data.flatten().astype(np.str).tolist())       
        writer.writerow(["NOAA_50_N_mean"] +NOAA_50_N_mean.data.flatten().astype(np.str).tolist()) 
        
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
        writer.writerow(["IPSL85_50_N_mean"] +IPSL85_50_N_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MIROC85_50_N_mean"] +MIROC85_50_N_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MOHCCCLM85_50_N_mean"] +MOHCCCLM85_50_N_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["MOHCKNMI85_50_N_mean"] +MOHCKNMI85_50_N_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["MOHCSMHI85_50_N_mean"] +MOHCSMHI85_50_N_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["MPICCLM85_50_N_mean"] +MPICCLM85_50_N_mean.data.flatten().astype(np.str).tolist())    
        writer.writerow(["MPIREMO85_50_N_mean"] +MPIREMO85_50_N_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["MPISMHI85_50_N_mean"] +MPISMHI85_50_N_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["NCCSMHI85_50_N_mean"] +NCCSMHI85_50_N_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["NOAA85_50_N_mean"] +NOAA85_50_N_mean.data.flatten().astype(np.str).tolist())
        
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
        writer.writerow(["IPSL_past_C_mean"] +IPSL_past_C_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MIROC_past_C_mean"] +MIROC_past_C_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MOHCCCLM_past_C_mean"] +MOHCCCLM_past_C_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MOHCKNMI_past_C_mean"] +MOHCKNMI_past_C_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MOHCSMHI_past_C_mean"] +MOHCSMHI_past_C_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MPICCLM_past_C_mean"] +MPICCLM_past_C_mean.data.flatten().astype(np.str).tolist())    
        writer.writerow(["MPIREMO_past_C_mean"] +MPIREMO_past_C_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["MPISMHI_past_C_mean"] +MPISMHI_past_C_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["NCCSMHI_past_C_mean"] +NCCSMHI_past_C_mean.data.flatten().astype(np.str).tolist())       
        writer.writerow(["NOAA_past_C_mean"] +NOAA_past_C_mean.data.flatten().astype(np.str).tolist())     
        
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
        writer.writerow(["IPSL_30_C_mean"] +IPSL_30_C_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MIROC_30_C_mean"] +MIROC_30_C_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MOHCCCLM_30_C_mean"] +MOHCCCLM_30_C_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MOHCKNMI_30_C_mean"] +MOHCKNMI_30_C_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MOHCSMHI_30_C_mean"] +MOHCSMHI_30_C_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MPICCLM_30_C_mean"] +MPICCLM_30_C_mean.data.flatten().astype(np.str).tolist())    
        writer.writerow(["MPIREMO_30_C_mean"] +MPIREMO_30_C_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["MPISMHI_30_C_mean"] +MPISMHI_30_C_mean.data.flatten().astype(np.str).tolist())        
        writer.writerow(["NCCSMHI_30_C_mean"] +NCCSMHI_30_C_mean.data.flatten().astype(np.str).tolist())       
        writer.writerow(["NOAA_30_C_mean"] +NOAA_30_C_mean.data.flatten().astype(np.str).tolist()) 
        
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
        writer.writerow(["IPSL85_30_C_mean"] +IPSL85_30_C_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MIROC85_30_C_mean"] +MIROC85_30_C_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MOHCCCLM85_30_C_mean"] +MOHCCCLM85_30_C_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["MOHCKNMI85_30_C_mean"] +MOHCKNMI85_30_C_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["MOHCSMHI85_30_C_mean"] +MOHCSMHI85_30_C_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["MPICCLM85_30_C_mean"] +MPICCLM85_30_C_mean.data.flatten().astype(np.str).tolist())    
        writer.writerow(["MPIREMO85_30_C_mean"] +MPIREMO85_30_C_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["MPISMHI85_30_C_mean"] +MPISMHI85_30_C_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["NCCSMHI85_30_C_mean"] +NCCSMHI85_30_C_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["NOAA85_30_C_mean"] +NOAA85_30_C_mean.data.flatten().astype(np.str).tolist())  
        
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
        writer.writerow(["IPSL_50_C_mean"] +IPSL_50_C_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MIROC_50_C_mean"] +MIROC_50_C_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MOHCCCLM_50_C_mean"] +MOHCCCLM_50_C_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MOHCKNMI_50_C_mean"] +MOHCKNMI_50_C_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MOHCSMHI_50_C_mean"] +MOHCSMHI_50_C_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MPICCLM_50_C_mean"] +MPICCLM_50_C_mean.data.flatten().astype(np.str).tolist())    
        writer.writerow(["MPIREMO_50_C_mean"] +MPIREMO_50_C_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["MPISMHI_50_C_mean"] +MPISMHI_50_C_mean.data.flatten().astype(np.str).tolist())        
        writer.writerow(["NCCSMHI_50_C_mean"] +NCCSMHI_50_C_mean.data.flatten().astype(np.str).tolist())       
        writer.writerow(["NOAA_50_C_mean"] +NOAA_50_C_mean.data.flatten().astype(np.str).tolist()) 
        
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
        writer.writerow(["IPSL85_50_C_mean"] +IPSL85_50_C_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MIROC85_50_C_mean"] +MIROC85_50_C_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MOHCCCLM85_50_C_mean"] +MOHCCCLM85_50_C_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["MOHCKNMI85_50_C_mean"] +MOHCKNMI85_50_C_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["MOHCSMHI85_50_C_mean"] +MOHCSMHI85_50_C_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["MPICCLM85_50_C_mean"] +MPICCLM85_50_C_mean.data.flatten().astype(np.str).tolist())    
        writer.writerow(["MPIREMO85_50_C_mean"] +MPIREMO85_50_C_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["MPISMHI85_50_C_mean"] +MPISMHI85_50_C_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["NCCSMHI85_50_C_mean"] +NCCSMHI85_50_C_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["NOAA85_50_C_mean"] +NOAA85_50_C_mean.data.flatten().astype(np.str).tolist())
        
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
        writer.writerow(["IPSL_past_S_mean"] +IPSL_past_S_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MIROC_past_S_mean"] +MIROC_past_S_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MOHCCCLM_past_S_mean"] +MOHCCCLM_past_S_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MOHCKNMI_past_S_mean"] +MOHCKNMI_past_S_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MOHCSMHI_past_S_mean"] +MOHCSMHI_past_S_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MPICCLM_past_S_mean"] +MPICCLM_past_S_mean.data.flatten().astype(np.str).tolist())    
        writer.writerow(["MPIREMO_past_S_mean"] +MPIREMO_past_S_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["MPISMHI_past_S_mean"] +MPISMHI_past_S_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["NCCSMHI_past_S_mean"] +NCCSMHI_past_S_mean.data.flatten().astype(np.str).tolist())       
        writer.writerow(["NOAA_past_S_mean"] +NOAA_past_S_mean.data.flatten().astype(np.str).tolist())     
        
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
        writer.writerow(["IPSL_30_S_mean"] +IPSL_30_S_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MIROC_30_S_mean"] +MIROC_30_S_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MOHCCCLM_30_S_mean"] +MOHCCCLM_30_S_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MOHCKNMI_30_S_mean"] +MOHCKNMI_30_S_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MOHCSMHI_30_S_mean"] +MOHCSMHI_30_S_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MPICCLM_30_S_mean"] +MPICCLM_30_S_mean.data.flatten().astype(np.str).tolist())    
        writer.writerow(["MPIREMO_30_S_mean"] +MPIREMO_30_S_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["MPISMHI_30_S_mean"] +MPISMHI_30_S_mean.data.flatten().astype(np.str).tolist())        
        writer.writerow(["NCCSMHI_30_S_mean"] +NCCSMHI_30_S_mean.data.flatten().astype(np.str).tolist())       
        writer.writerow(["NOAA_30_S_mean"] +NOAA_30_S_mean.data.flatten().astype(np.str).tolist()) 
        
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
        writer.writerow(["IPSL85_30_S_mean"] +IPSL85_30_S_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MIROC85_30_S_mean"] +MIROC85_30_S_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MOHCCCLM85_30_S_mean"] +MOHCCCLM85_30_S_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["MOHCKNMI85_30_S_mean"] +MOHCKNMI85_30_S_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["MOHCSMHI85_30_S_mean"] +MOHCSMHI85_30_S_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["MPICCLM85_30_S_mean"] +MPICCLM85_30_S_mean.data.flatten().astype(np.str).tolist())    
        writer.writerow(["MPIREMO85_30_S_mean"] +MPIREMO85_30_S_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["MPISMHI85_30_S_mean"] +MPISMHI85_30_S_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["NCCSMHI85_30_S_mean"] +NCCSMHI85_30_S_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["NOAA85_30_S_mean"] +NOAA85_30_S_mean.data.flatten().astype(np.str).tolist())  
        
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
        writer.writerow(["IPSL_50_S_mean"] +IPSL_50_S_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MIROC_50_S_mean"] +MIROC_50_S_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MOHCCCLM_50_S_mean"] +MOHCCCLM_50_S_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MOHCKNMI_50_S_mean"] +MOHCKNMI_50_S_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MOHCSMHI_50_S_mean"] +MOHCSMHI_50_S_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MPICCLM_50_S_mean"] +MPICCLM_50_S_mean.data.flatten().astype(np.str).tolist())    
        writer.writerow(["MPIREMO_50_S_mean"] +MPIREMO_50_S_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["MPISMHI_50_S_mean"] +MPISMHI_50_S_mean.data.flatten().astype(np.str).tolist())        
        writer.writerow(["NCCSMHI_50_S_mean"] +NCCSMHI_50_S_mean.data.flatten().astype(np.str).tolist())       
        writer.writerow(["NOAA_50_S_mean"] +NOAA_50_S_mean.data.flatten().astype(np.str).tolist()) 
        
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
        writer.writerow(["IPSL85_50_S_mean"] +IPSL85_50_S_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MIROC85_50_S_mean"] +MIROC85_50_S_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MOHCCCLM85_50_S_mean"] +MOHCCCLM85_50_S_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["MOHCKNMI85_50_S_mean"] +MOHCKNMI85_50_S_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["MOHCSMHI85_50_S_mean"] +MOHCSMHI85_50_S_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["MPICCLM85_50_S_mean"] +MPICCLM85_50_S_mean.data.flatten().astype(np.str).tolist())    
        writer.writerow(["MPIREMO85_50_S_mean"] +MPIREMO85_50_S_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["MPISMHI85_50_S_mean"] +MPISMHI85_50_S_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["NCCSMHI85_50_S_mean"] +NCCSMHI85_50_S_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["NOAA85_50_S_mean"] +NOAA85_50_S_mean.data.flatten().astype(np.str).tolist()) 
        
if __name__ == '__main__':
    main()     
    
    