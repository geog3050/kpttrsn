#This function assumes arcpy has been installed, a workspace and folder have been defined, and 
def calculatePercentAreaOfPolygonAInPolygonB(input_geodatabase, fcPolygonA, fcPolygonB, idFieldPolygonB):
    fcFieldsA = arcpy.ListFields(fcPolygonA)#Defines the feature class fields for polygonA
    fcFieldsB = arcpy.ListFields(fcPolygonB)#Defines the feature class fields for ploygonB
    fields = ["Shape_Area"]#Defining the rows to be used as cursors
    bSum = 0#Defining the sum of the total PolygonB area as 0
    with arcpy.da.SearchCursor(fcPolygonB, fields) as cursor:
        for row in cursor:
            bSum += row[0]#Adding the value of each "Shape_Area" entry to the sum value
        print(bSum)
    fields.append("Fraction_of_Area")#Appending the new field to the fields list
    with arcpy.da.SearchCursor(fcPolygonA, fields) as cursor:
        for row in cursor:
            row[1] = row[0]/bSum#Defining the value for that new attribute as the Shape_Area of attribute A divided by the total area of attribute B
            cursor.updateRow(row)#Updating the attribute table with the value
