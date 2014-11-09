import rhinoscriptsyntax as rs

dist = rs.GetReal("Input offset distance: ")
enlrgCirc = rs.GetObjects("Select circles to enlarge: ",4,True,True)

for circ in enlrgCirc:
    if (rs.IsCircle(circ)):
        rs.OffsetCurve(circ, [1,0,0], dist)
        rs.DeleteObject(circ)
    else:
        print "not a circle"
