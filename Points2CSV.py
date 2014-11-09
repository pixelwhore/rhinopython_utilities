import rhinoscriptsyntax as rs

lstPoints = rs.GetObjects("Select points to convert to CSV...", 1, False,True)
file = open('test.csv', 'w')

for point in lstPoints:
    pt = rs.PointCoordinates(point)
    line = str(pt[0]) + ',' + str(pt[1]) + ',' + str(pt[2])
    file.write(line)
    file.write('\n')
    
file.close()
print("CSV file written successfully")
