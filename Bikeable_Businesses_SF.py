#Script to create a shapefile of bikeable businesses in SF
import os
import arcpy

#Set environmental workspace
arcpy.env.workspace = r"C:\Users\ian.conroy\Desktop\Bay Geo Classes\Python Class\GIS_Data\SF_SHPs"

#Set location for output of geoprocessing tools
output_folder = r"C:\Users\ian.conroy\Desktop\Bay Geo Classes\Python Class\Output_Folder"

#Create buffer of bike network
print('Creating buffer')
#Because we set our environmental workspace to the SF_SHPs folder, we don't have to specifiy the full file path to the input we used SF_Bike_Network.shp, arcpy is adding the env workspace in front for us
#our output folder is not our current workspace, so we need to use the full file path for the output shapefile
arcpy.Buffer_analysis("SF_Bike_Network.shp", os.path.join(output_folder, 'SF_Bike_Network.shp'), "25 Feet", "FULL", "ROUND")

#Create shapefile of businesses along bike routes
print('Clipping businesses by bike route buffer')
arcpy.Clip_analysis("SF_Businesses.shp", os.path.join(output_folder, 'SF_Bike_Network.shp'), os.path.join(output_folder, 'Bikeable_Businesses.shp'))
