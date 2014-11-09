"""
Script for adding a single Real to a collection of TextDot objects. 
If the TextDot contains a String that cannot be cast as a Real, it is counted as
an error and reported at the end of th script.

Code distributed under the GNU GPL v3.0
http://www.gnu.org/licenses/gpl-3.0.txt

Aaron M Willette
www.pixelwhore.com
"""

import rhinoscriptsyntax as rs

if (__name__ == "__main__"):
    
    selected_dots = rs.GetObjects("Select text dots to adjust...")
    adjust_val = rs.GetReal("Input adjust amount...")
    error_count = 0
    
    for dot in selected_dots:
        temp_loc = rs.TextDotPoint(dot)
        try:
            rs.AddTextDot(float(rs.TextDotText(dot))+adjust_val,temp_loc)
            rs.DeleteObject(dot)
        except Exception:
            error_count = error_count + 1
            
    if error_count > 0:
        print("Error casting " + str(error_count) + " TextDot strings to float")
