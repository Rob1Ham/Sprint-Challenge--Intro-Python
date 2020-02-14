### Test Solution script to replicate functionality of unit test script
from cityreader import City, cityreader, cityreader_stretch

cities = []

cities = cityreader(cities)

stretch_answer = cityreader_stretch(32, -120, 45, -100, cities)

for ans in stretch_answer:
    print (ans.name)