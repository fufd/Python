import re

line = "xxx������2011��8��6��"
line1 = "xxx������2011-8-6"
line2 = "xxx������2011-08-06"
line3 = "xxx������2011/08/06"
line4 = "xxx������2011/8/6"
line5 = "xxx������2011-08"
regex = ".*������(\d{4}[��/-]\d{1,2}([��/-]\d{1,2}|[��/-]$|$))"
zz = re.match(regex,line3)
if zz:
   print(zz.group(1))