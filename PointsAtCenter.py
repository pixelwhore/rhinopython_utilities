import rhinoscriptsyntax as rs

lstCircles = rs.GetObjects("Select circles to add center points to...",4)

rs.EnableRedraw(False)
for circle in lstCircles:
    rs.AddPoint(rs.CircleCenterPoint(circle))
rs.EnableRedraw(True)    