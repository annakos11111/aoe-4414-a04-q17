# ymdhms_to_jd.py
#
# Usage: python3 ymdhms_to_jd.py year month day hour minute second
# Converts year, month, day, hour, minute, second to fractional Julian date
# Parameters: year, month, day, hour, minute, second
# Output: fractional julilan date
#
# Written by Anna Kosnic
#
import sys # argv

# initialize script arguments
year   = 0
month  = 0
day    = 0
hour   = 0
minute = 0
second = 0.0

# parse script arguments
if len(sys.argv)==7:
    year   = int(sys.argv[1])
    month  = int(sys.argv[2])
    day    = int(sys.argv[3])
    hour   = int(sys.argv[4])
    minute = int(sys.argv[5])
    second = float(sys.argv[6])
else:
    print(\
        'Usage: '\
            'python3 ymdhms_to_jd.py year month day hour minute second'\
                )
    exit()

# script below
jd = day - 32075 + \
    int(1461*(year + 4800 + int((month - 14)/12))/4) + \
    int(367*(month - 2 - (int((month - 14)/12)*12))/12) - \
    int(3*int((year + 4900 + int((month - 14)/12))/100)/4)

jd_mid = jd - 0.5
d_frac = (second + 60*(minute + 60*hour))/86400
jd_frac = jd_mid + d_frac
print(jd_frac)
