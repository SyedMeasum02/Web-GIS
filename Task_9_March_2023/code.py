import arcpy
from arcpy import env
env.overwriteOutput=True
env.workspace = "D:\6th semester\Exercise05"
arcpy.Buffer_analysis("facilities.shp", "Results/facilities_buffer.shp", "500 METERS")
print("Completed")
