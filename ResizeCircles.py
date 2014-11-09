import rhinoscriptsyntax as rs

enlrgCirc = rs.GetObjects("Select circles to resize: ",4,True,True)
dist = rs.GetReal("Input new circle diameter: ")

for circ in enlrgCirc:
    if (rs.IsCircle(circ)):
        rad = rs.CircleRadius(circ)
        rs.OffsetCurve(circ, [1,0,0], ((dist/2) - rad))
        rs.DeleteObject(circ)
