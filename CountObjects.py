import rhinoscriptsyntax as rs

objs = rs.GetObjects("select objects to count...")
rs.MessageBox("Object count: " + str(len(objs)), 16)