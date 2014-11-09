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
        
    outval = int(dist) + ndec
    return outval

#GET INPUT
lSet = rs.GetObjects("Select lines to measure...")
ptSet = rs.GetObjects("Select intersect points...")

#SET UP NECESSARY INFO
ct = 0
ml = 0
tl = 0

rs.AddLayer("CableInfo")
rs.AddLayer("OAL", Color.Teal, parent = "CableInfo")
rs.AddLayer("2BTM", Color.CornflowerBlue, parent = "CableInfo")
rs.AddLayer("2TOP", Color.Goldenrod, parent = "CableInfo")

#DO THE WORK

rs.EnableRedraw(False)

for line in lSet:
    p1 = rs.CurveStartPoint(line)
    p2 = rs.CurveEndPoint(line)
    dist = rs.Distance(p1,p2)
    val = funcRound(dist)
    
    for pt in ptSet:
        if rs.IsPointOnCurve(line, pt):
            thisPt = pt
    
    dist2 = rs.Distance(p2,thisPt)
    val2 = funcRound(dist2)
    
    rs.CurrentLayer("OAL")
    rs.AddTextDot("ID " + str(ct) + ": " + str(val+4), p2)
    rs.CurrentLayer("2BTM")
    rs.AddTextDot("BTM: " + str(val),p1)
    rs.CurrentLayer("2TOP")
    rs.AddTextDot("TOP: " + str(val2),thisPt)
    
    ct = ct + 1
    ml = ml + val
    
    if val > tl:
        tl = val
        
        

rs.EnableRedraw(True)

print(ct)
print(ml)
print(tl)