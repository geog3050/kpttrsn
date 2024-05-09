import arcpy

print(arcpy.env.workspace)

folder = "C:/Users/kpttrsn/OneDrive - University of Iowa/Documents/ArcGIS/Projects/FinalProject-Testing/Chicago/"
arcpy.env.workspace=folder

#Check folder path is correct and contains shapefiles
fcList=arcpy.ListFeatureClasses()
print(fcList)

#display the fields present in the shapefile
fc=fcList[0]
fcFields = arcpy.ListFields(fc)
for field in fcFields:
    print(field.name)

#Add a new field for the percent of heat converted to sensible heat
arcpy.management.AddField(fc, "PercentQh", "FLOAT")

pIm = "MEAN" #Defines the name of the percent impervious area field
pQh = "PercentQh" #Defines the name of the precent sensible heat flux field
pDn = "MEAN_1" #Defines the name of the population density field
pImR2 = 0.7623 #Defines the R-squared correlation for the percent impervious relationship with percent sensible heat
pDnR2 = 0.6032 #Defines the R-squared correlation for the population density relationship with percent sensible heat
sumR2 = pImR2+pDnR2 #sums those values

#Weights the contribution to percent sensible heat based on the relative strength of the correlation
pImWeight = pImR2/sumR2 
pDnWeight = pDnR2/sumR2
print(pImWeight)
print(pDnWeight)

with arcpy.da.UpdateCursor(fc, [pIm, pQh, pDn]) as cursor:
    for row in cursor:
        Qh_imp = pImWeight*((row[0]*0.429)+0.3467)#Uses the equation linking impervious area to sensible heat fraction and its weight to find the sensible heat fraction correlated to impervious area
        Qh_pop = pDnWeight*100*((row[2]*0.0165*0.001)+0.4632) #Uses the equation linking pop density to sensible heat fraction and its weight to find the sensible heat fraction correlated to popuation density
        print(Qh_imp, Qh_pop, row) #Displays the individual components and the row for quality checking 
        row[1] = Qh_imp + Qh_pop #Sums the weighted contributions from each factor to create a total percent sensible heat value (pQh)
        cursor.updateRow(row) #Updates the row in the attribute table.


