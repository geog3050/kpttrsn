#importing arcpy
import arcpy

#Checking the workspace location
print(arcpy.env.workspace)

#saving the folder variable as the work filepath
folder = "C:/Users/kylej/OneDrive/Documents/00-School/s10/Geospatial Programming/Quiz 5"
print(folder)

#setting the filepath as the official workspace
arcpy.env.workspace = folder

#Defining the feature class as the airpots shapefile
fc = 'airports'

#Checking the variable names in the attribute table of the shapefile
fcFields = arcpy.ListFields(fc)
for field in fcFields:
    print(field.name)

#adding the 'buffer' field to the attribute table
arcpy.management.AddField(fc, "buffer", "LONG")

#Checking to see if I can use the search cursor function properly
fields = ["FEATURE", "TOT_ENP"]
countA = 0
countS = 0
with arcpy.da.SearchCursor(fc, fields) as cursor:
    for row in cursor:
        
        if row[0] == 'Airport':
            countA = countA + 1
        elif row[0] == 'Seaplane Base':
            countS += 1
print(f'Number of Airports is {countA}')
print(f'Number of Seaplane Bases is {countS}')

#appending the 'buffer' attribute to the list of selected fields
fields.append("buffer")
print(fields)

#Applying the assigned filters of 10,000 and 1,000 people per day for the buffer size 
with arcpy.da.UpdateCursor(fc, fields) as cursor:
    for row in cursor:
        
        if row[0] == 'Airport':
            if row[1] >= 10000:
                row[2] = 15000
        elif row[0] == 'Seaplane Base':
            if row[1] >= 1000:
                row[2] = 7500
        #Adding the updated buffer sizes to the attribute table
        cursor.updateRow(row)

#arcpy.analysis.Buffer(in_features, out_feature_class, buffer_distance_or_field)
print(fields[2])

#Naming the output feature and converting it to a shapefile
outputFeature = 'Buffers'
arcpy.analysis.Buffer(fc, outputFeature, fields[2])


