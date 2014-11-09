"""
Simple script for 'normalizing' values in a TextDot object.
Takes the smallest value from all the TextDots and subtracts it from them all.

Code distributed under the GNU GPL v3.0
http://www.gnu.org/licenses/gpl-3.0.txt

Aaron M Willette
www.pixelwhore.com
"""

import rhinoscriptsyntax as rs

if (__name__ == "__main__"):
    
    selected_dots = rs.GetObjects("select text dots to average...")
    min_val = 10000.0
    error_count = 0
    new_dots = []
    
    for dot in selected_dots:
        try:
            temp_val = float(rs.TextDotText(dot))
            if temp_val < min_val:
                min_val = temp_val
            new_dots.append(dot)
        except Exception:
            error_count = error_count + 1
            
    for dot in new_dots:
        temp_loc = rs.TextDotPoint(dot)
        rs.AddTextDot((float(rs.TextDotText(dot))-min_val),temp_loc)
        rs.DeleteObject(dot)
        
    if error_count > 0:
        print("Error casting " + str(error_count) + " TextDot strings to float")