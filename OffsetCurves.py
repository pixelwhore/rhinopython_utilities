import rhinoscriptsyntax as rs

dist = rs.GetReal("Input offset distance: ")
enlrgCrv = rs.GetObjects("Select curves to offset: ",4,True,True)

for crv in enlrgCrv:
    if (rs.IsCurve(crv)):
        rs.OffsetCurve(crv, [1,0,0], dist)
        rs.DeleteObject(crv)
    else:
        print "not a curve"