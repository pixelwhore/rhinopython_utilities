import rhinoscriptsyntax as rs

strText = rs.GetObject("Select text to convert to dot", 512, True, True)
strCurve = rs.GetCurveObject("Select object to label")[0]
rs.AddTextDot(rs.LeaderText  (strText),rs.CurveAreaCentroid(strCurve)[0])