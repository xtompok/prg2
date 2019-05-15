import re

results = []
regex = "^Max[^0-9.]*([0-9.]*)[^0-9.]*([0-9.]*)"
lat = None
lon = None
err = None
with open("out.txt") as f:
	for line in f:
		m = re.search("Lon.*\[ ([0-9.]*) \]",line)
		if m:
			lon = float(m.group(1))
		m = re.search("Lat.*\[ ([0-9.]*) \]",line)
		if m:
			lat = float(m.group(1))

		m = re.search(regex,line)
		if m:
			err = (float(m.group(1)),float(m.group(2)))
			results.append((lon,lat,err))

print(results)
	

