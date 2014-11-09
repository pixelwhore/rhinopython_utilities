import rhinoscriptsyntax as rs
from System.Drawing import Color

def funcRound(val):
    dec = val%1
    
    if 0 <= dec < .0625:
        ndec = 0
    elif .0625 <= dec < .1875:
        ndec = .125
    elif .1875 <= dec < .3125:
        ndec = .25
    elif .3125 <= dec < .4375:
        ndec = .375
    elif .4375 <= dec < .5625:
        ndec = .50
    elif .5625 <= dec < .6875:
        ndec = .625
    elif .6875 <= dec < .8125:
        ndec = .750
    elif .8125 <= dec < .9375:
        ndec = .875
    elif .9375 <= dec < 1:
        ndec = 1
        
    outval = int(val) + ndec
    return outval

#GET INPUT
lSet = rs.GetObjects("Select lines to measure...")
ptSet = rs.GetObjects("Select intersect points...")

#SET UP NECESSARY INFO
ct = 0
ml = 0
tl = 0
addL = 12

rs.AddLayer("CableInfo")

#DO THE WORK
rs.EnableRedraw(False)

for line in lSet:
    p1 = rs.CurveStartPoint(line)
    p2 = rs.CurveEndPoint(line)
    for pt in ptSet:
        if rs.IsPointOnCurve(line, pt):
            thisPt = pt
    
    dist = rs.Distance(p1,p2)
    val = funcRound(dist)
    dist2 = rs.Distance(p2,thisPt)
    val2 = funcRound(dist2)
    
    rs.AddLayer(str(ct), parent = "CableInfo")
    rs.AddLayer("OAL_" + str(ct), Color.Teal, parent = str(ct))
    rs.AddLayer("2BTM_" + str(ct), Color.CornflowerBlue, parent = str(ct))
    rs.AddLayer("2TOP_"+ str(ct), Color.Goldenrod, parent = str(ct))
    
    rs.ObjectLayer(line,str(ct))
    rs.CurrentLayer("OAL_" + str(ct))
    rs.AddTextDot("ID " + str(ct) + ": " + str(val+addL), p2)
    rs.CurrentLayer("2BTM_" + str(ct))
    rs.AddTextDot("BTM: " + str(val),p1)
    rs.CurrentLayer("2TOP_" + str(ct))
    rs.AddTextDot("TOP: " + str(val2),thisPt)
    
    ct = ct + 1
    ml = ml + val + addL
    
    if (val + addL) > tl:
        tl = val + addL

rs.EnableRedraw(True)

#REPORT BACK NECESSARY INFO
print("Number of cables: " + str(ct+1))
print("Total length of cables: " + str(ml))
print("Longest cable length: " + str(tl))