import rhinoscriptsyntax as rs

dblDiameter = rs.GetReal('Input circle diameter', 0.1,0.05,0.2)
ptsPoints = rs.GetObjects('Select points to populate', 1)

rs.EnableRedraw(False)

for point in ptsPoints:
    rs.AddCircle(point,dblDiameter/2)
    
rs.EnableRedraw(True)