import re

line = "xxx出生于2011年8月6日"
line1 = "xxx出生于2011-8-6"
line2 = "xxx出生于2011-08-06"
line3 = "xxx出生于2011/08/06"
line4 = "xxx出生于2011/8/6"
line5 = "xxx出生于2011-08"
regex = ".*出生于(\d{4}[年/-]\d{1,2}([月/-]\d{1,2}|[月/-]$|$))"
zz = re.match(regex,line3)
if zz:
   print(zz.group(1))