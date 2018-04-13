import csv
import json
from pprint import pprint
import os
#outpusts data for heat map


def readCityData(filename, txt_file):
	print("helloworld")
	
	data = json.load(open(filename))
	pprint(data['region'])
	pprint(data['total'])
	businesses = data['businesses']
	#txt_f = filename.strip('.json')+".txt"

	#{location: new google.maps.LatLng(46.97091,-123.8261),weight=44},
	
	for b in businesses:
		coords =  b['coordinates']
		lat = coords['latitude']
		longi = coords['longitude']
		review_count = b['review_count']
		#print(lat)
		#print(longi)
		#print('coords', b['coordinates'])
		x = "{location: new google.maps.LatLng("+str(lat)+","+str(longi)+"),weight:"+str(review_count)+"},"
		#print('#reviews', b['review_count'])
		txt_file.write(x)
		txt_file.write('\n')

if __name__ == '__main__':
	filename = "city_yelp_jsons/WA/Aberdeen Gardens, WA_data.json"
	state = 'WA'
	os.chdir("..")
	directory = 'city_yelp_jsons/'+state+'/'
	print(directory)
	exists = os.path.exists(directory)
	txtdir = "state_yelp_txts/"
	state_file = state+"_heatmap.txt"
	f = open(txtdir+state_file,"wb")
	if exists:
		for i,filename in enumerate(os.listdir(directory)):
			print(filename)
			if(False):
				print("break for now")
				break

			readCityData(directory + filename, f)