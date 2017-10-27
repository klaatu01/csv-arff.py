#!/usr/bin/python
import sys
import csv
import random

amount = 0
printnum = 0
if len(sys.argv) >= 4:
	amount = int(sys.argv[2])
	printnum = int(sys.argv[3])
else:
	amount = 100000
	printnum = 100000

def convert(x):
	dict = {'0' : "'Angry'", '1' : "'Disgust'", '2' : "'Fear'", '3' : "'Happy'", '4' : "'Sad'", '5' : "'Suprise'", '6' : "'Neutral'"}
	return dict[x]

def print_headers():
	print '@RELATION faces'
	header = ["@ATTRIBUTE 'emotion' {'Angry', 'Disgust', 'Fear', 'Happy', 'Sad', 'Suprise', 'Neutral'}"]
	for x in range(2304):
		header.append("@ATTRIBUTE 'pixel"+str(x)+"' numeric")
	header.reverse()
	print "\n".join(header)
	print '@DATA'

def get_faces():
	faces = []
	with open(sys.argv[1], 'rb') as csvfile:
		spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
		firstline = True
		count = 0
		for row in spamreader:
			if firstline:
				firstline = False
				continue
			row[0] = convert(row[0])
			line = row[1]
			del row[1]
			array = line.split(' ')
			for pixel in array:
				row.append(pixel)
			#print len(array)
			row.reverse()
			faces.append(row)
			count = count + 1
			if count == amount:
				break
	return faces

print_headers()
faces = get_faces()
random.shuffle(faces)
if printnum > len(faces):
	printnum = len(faces)
for line in range(0,int(printnum)):
	print ",".join(faces[line])
