import rhinoscriptsyntax as rs

listLines = rs.GetObjects("Select curves to test length of...",4)
correctCount = 0

for curve in listLines:
    length = rs.CurveLength(curve)
    if length == 0:
        rs.DeleteObject(curve)
        correctCount = correctCount + 1

print correctCount