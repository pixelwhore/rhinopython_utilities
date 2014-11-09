import rhinoscriptsyntax as rs

p1 = rs.GetPoint("Select first point to measure...")
p2 = rs.GetPoint("Select second point to measure...")
dist = rs.Distance(p1,p2)
dec = dist%1

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

rs.AddTextDot(int(dist) + ndec,p2)