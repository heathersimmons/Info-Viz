import urllib2
from bs4 import BeautifulSoup
 
# Create/open a file called wunder-data.csv (which will be a comma-delimited file)
f = open('wunder-data.csv', 'w')

f.write( ',' + 'Toronto Daily Temperature' + '\n')
 
# Iterate through months and day
for m in range(1, 13):
    for d in range(1, 32):
 
      # Check if already gone through month
      if (m == 2 and d > 28):
        break
      elif (m in [4, 6, 9, 11] and d > 30):
        break
 
      # Open wunderground.com url
      url = "http://www.wunderground.com/history/airport/YYZ/2013/" + str(m) + "/" + str(d) + "/DailyHistory.html"
      page = urllib2.urlopen(url)
 
      # Get temperature from page
      soup = BeautifulSoup(page)
      # dayTemp = soup.body.nobr.b.string
      dayTemp = soup.findAll(attrs={"class":"nobr"})[3].span.string
 
      # Format month for timestamp
      if len(str(m)) < 2:
        mStamp = '0' + str(m)
      else:
        mStamp = str(m)
 
      # Format day for timestamp
      if len(str(d)) < 2:
        dStamp = '0' + str(d)
      else:
        dStamp = str(d)
 
      # Build timestamp
      timestamp = '2013' + mStamp + dStamp
 
      # Write timestamp and temperature to file
      f.write(timestamp + ',' + dayTemp + '\n')
 
# Done getting data! Close file.
f.close()
