import rhinoscriptsyntax as rs

dots = rs.GetObjects("select text dots to sum...")
sumVal = 0.0

#find lowest value for collection of dots
for dot in dots:
    tempVal = float(rs.TextDotText(dot))
    sumVal = sumVal + tempVal

rs.MessageBox("Dot sum: " + str(sumVal), 16, "Results")