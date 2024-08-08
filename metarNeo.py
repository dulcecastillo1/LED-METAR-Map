import neopixel 
import board
import requests 
from fractions import Fraction 

#set up the neopixels 
pixels = neopixel.NeoPixel(board.D10, 6, brightness = 0.01, pixel_order = neopixel.RGBW) 

#list the urls for bay area airports 
url1 = 'https://aviationweather.gov/api/data/metar?ids=KCVH'
url2 = 'https://aviationweather.gov/api/data/metar?ids=KTCY'
url3 = 'https://aviationweather.gov/api/data/metar?ids=KSJC'
url4 = 'https://aviationweather.gov/api/data/metar?ids=KSFO'
url5 = 'https://aviationweather.gov/api/data/metar?ids=KOAK'
url6 = 'https://aviationweather.gov/api/data/metar?ids=KAPC'


def run():
	#requests
	r1 = requests.get(url1)
	r2 = requests.get(url2) 
	r3 = requests.get(url3) 
	r4 = requests.get(url4) 
	r5 = requests.get(url5) 
	r6 = requests.get(url6)
	 
	text1 = r1.text
	text2 = r2.text 
	text3 = r3.text
	text4 = r4.text
	text5 = r5.text
	text6 = r6.text 

	#split each of the metars into lists/arrays
	list1 = text1.split() 
	list2 = text2.split() 
	list3 = text3.split() 
	list4 = text4.split() 
	list5 = text5.split() 
	list6 = text6.split() 
	
	#variables for visibility 
	num_vis1 = 0
	num_vis2 = 0
	num_vis3 = 0
	num_vis4 = 0
	num_vis5 = 0
	num_vis6 = 0
	
	
	vis1 = ''
	vis2 = ''
	vis3 = ''
	vis4 = ''
	vis5 = ''
	vis6 = ''
	
	listNum = ''
	
	
	#function for finding visibility 
	def searchVis(x): 
		if x == 1: 
			listNum = list1 
		elif x == 2: 
			listNum = list2 
		elif x == 3: 
			listNum = list3 
		elif x == 4: 
			listNum = list4
		elif x == 5: 
			listNum = list5 
		elif x == 6: 
			listNum = list6 
		
		i = 0 
		vis = listNum[i]
		while i < (len(listNum)): 
			if((listNum[i]).find("SM")) != -1: 
				vis = listNum[i]
				if (vis[0]) != '1' and (vis[1]) == 'S': 
					num_vis = int(vis[0])
					return (num_vis)
				#check if the visibility is in the form of a fraction 
				elif(vis.find('/')) != -1: 
					num = int(vis[0])
					den = int(vis[2])
					num_vis = float(Fraction(num, den))
					if (len(listNum[i-1])) == 1 or (len(listNum[i-1])) == 2: 
						num_vis += (float(listNum[i-1]))
						vis = listNum[i-1] + " " + listNum[i]
						return (num_vis)
					return (num_vis)
				elif (vis[0]) == '1' and (vis[1]) == 'S': 
					num_vis = 1 
					return (num_vis)
				else: 
					num_vis = (int((vis[0] + vis[1])))
					return (num_vis)
			else: 
				i += 1
				
		
	#search for visibility 
	num_vis1 = searchVis(1)
	num_vis2 = searchVis(2)
	num_vis3 = searchVis(3)
	num_vis4 = searchVis(4)
	num_vis5 = searchVis(5)
	num_vis6 = searchVis(6)
	
	
	#find ceiling within the diffferent reports
	#list1 
	n = 0 
	ceiling1 = ''
	while n < (len(list1)): 
		if ((list1[n]).find('BKN')) != -1 or ((list1[n]).find('OVC')) != -1: 
			ceiling1 = list1[n]
			#find the type of ceiling 
			ceilingString1 = ceiling1[0] + ceiling1[1] + ceiling1[2]
			#find the height of the ceiling and convert it into an int 
			height1 = ceiling1[3] + ceiling1[4] + ceiling1[5] 
			#removes any extra zeros before the number
			if ceiling1[3] == '0': 
				height1 = ceiling1[4] + ceiling1[5]
				if ceiling1[4] == '0': 
					height1 = ceiling1[5]
			height1 = height1 + '00'
			num_height1 = int(height1) 
			n = 100
		elif ((list1[n]).find('VV')) != -1: 
			ceiling1 = list1[n]
			ceilingString1 = ceiling1[0] + ceiling1[1]
			height1 = ceiling1[2] + ceiling1[3] + ceiling1[4] 
			#removes any extra zeros before the number
			if ceiling1[2] == '0': 
				height1 = ceiling1[3] + ceiling1[4]
				if ceiling1[3] == '0': 
					height1 = ceiling1[4]
			height1 = height1 + '00'
			num_height1 = int(height1)
			n = 100
		else: 
			n += 1
	#check if no ceiling is found in the report 
	if ceiling1 == '': 
		ceiling1 = "No ceiling"
		ceilingString1 = ''
		height1 = ''
		num_height1 = 0
		
	#list2 
	n = 0 
	ceiling2 = ''
	while n < (len(list2)): 
		if ((list2[n]).find('BKN')) != -1 or ((list2[n]).find('OVC')) != -1: 
			ceiling2 = list2[n]
			ceilingString2 = ceiling2[0] + ceiling2[1] + ceiling2[2]
			height2 = ceiling2[3] + ceiling2[4] + ceiling2[5] 
			#removes any extra zeros before the number
			if ceiling2[3] == '0': 
				height2 = ceiling2[4] + ceiling2[5]
				if ceiling2[4] == '0': 
					height2 = ceiling2[5]
			height2 = height2 + '00'
			num_height2 = int(height2) 
			n = 100
		elif ((list2[n]).find('VV')) != -1: 
			ceiling2 = list2[n]
			ceilingString2 = ceiling2[0] + ceiling2[1]
			height2 = ceiling2[2] + ceiling2[3] + ceiling2[4] 
			#removes any extra zeros before the number
			if ceiling2[2] == '0': 
				height2 = ceiling2[3] + ceiling2[4]
				if ceiling2[3] == '0': 
					height2 = ceiling2[4]
			height2 = height2 + '00'
			num_height2 = int(height2)
			n = 100
		else: 
			n += 1
	if ceiling2 == '': 
		ceiling2 = "No ceiling"
		ceilingString2 = ''
		height2 = ''
		num_height2 = 0
		

	#list3
	n = 0 
	ceiling3 = ''
	while n < (len(list3)): 
		if ((list3[n]).find('BKN')) != -1 or ((list3[n]).find('OVC')) != -1: 
			ceiling3 = list3[n]
			ceilingString3 = ceiling3[0] + ceiling3[1] + ceiling3[2]
			height3 = ceiling3[3] + ceiling3[4] + ceiling3[5] 
			#removes any extra zeros before the number
			if ceiling3[3] == '0': 
				height3 = ceiling3[4] + ceiling3[5]
				if ceiling3[4] == '0': 
					height3 = ceiling3[5]
			height3 = height3 + '00'
			num_height3 = int(height3) 
			n = 100
		elif ((list3[n]).find('VV')) != -1: 
			ceiling3 = list3[n]
			ceilingString3 = ceiling3[0] + ceiling3[1]
			height3 = ceiling3[2] + ceiling3[3] + ceiling3[4] 
			#removes any extra zeros before the number
			if ceiling3[2] == '0': 
				height3 = ceiling3[3] + ceiling3[4]
				if ceiling3[3] == '0': 
					height3 = ceiling3[4]
			height3 = height3 + '00'
			num_height3 = int(height3)
			n = 100
		else: 
			n += 1
	if ceiling3 == '': 
		ceiling3 = "No ceiling"
		ceilingString3 = ''
		height3 = ''
		num_height3 = 0
		
		
	#list4
	n = 0 
	ceiling4 = ''
	while n < (len(list4)): 
		if ((list4[n]).find('BKN')) != -1 or ((list4[n]).find('OVC')) != -1: 
			ceiling4 = list4[n]
			#find the type of ceiling 
			ceilingString4 = ceiling4[0] + ceiling4[1] + ceiling4[2]
			#find the height of the ceiling and convert it into an int 
			height4 = ceiling4[3] + ceiling4[4] + ceiling4[5] 
			#removes any extra zeros before the number
			if ceiling4[3] == '0': 
				height4 = ceiling4[4] + ceiling4[5]
				if ceiling4[4] == '0': 
					height4 = ceiling4[5]
			height4 = height4 + '00'
			num_height4 = int(height4) 
			n = 100
		elif ((list4[n]).find('VV')) != -1: 
			ceiling4 = list4[n]
			ceilingString4 = ceiling4[0] + ceiling4[1]
			height4 = ceiling4[2] + ceiling4[3] + ceiling4[4] 
			#removes any extra zeros before the number
			if ceiling4[2] == '0': 
				height4 = ceiling4[3] + ceiling4[4]
				if ceiling4[3] == '0': 
					height4 = ceiling4[4]
			height4 = height4 + '00'
			num_height4 = int(height4)
			n = 100
		else: 
			n += 1
	#check if no ceiling is found in the report 
	if ceiling4 == '': 
		ceiling4 = "No ceiling"
		ceilingString4 = ''
		height4 = ''
		num_height4 = 0
		
	#list5
	n = 0 
	ceiling5 = ''
	while n < (len(list5)): 
		if ((list5[n]).find('BKN')) != -1 or ((list5[n]).find('OVC')) != -1: 
			ceiling5 = list5[n]
			#find the type of ceiling 
			ceilingString5 = ceiling5[0] + ceiling5[1] + ceiling5[2]
			#find the height of the ceiling and convert it into an int 
			height5 = ceiling5[3] + ceiling5[4] + ceiling5[5] 
			#removes any extra zeros before the number
			if ceiling5[3] == '0': 
				height5 = ceiling5[4] + ceiling5[5]
				if ceiling5[4] == '0': 
					height5 = ceiling5[5]
			height5 = height5 + '00'
			num_height5 = int(height5) 
			n = 100
		elif ((list5[n]).find('VV')) != -1: 
			ceiling5 = list5[n]
			ceilingString5 = ceiling5[0] + ceiling5[1]
			height5 = ceiling5[2] + ceiling5[3] + ceiling5[4] 
			#removes any extra zeros before the number
			if ceiling5[2] == '0': 
				height5 = ceiling5[3] + ceiling5[4]
				if ceiling5[3] == '0': 
					height5 = ceiling5[4]
			height5 = height5 + '00'
			num_height5 = int(height5)
			n = 100
		else: 
			n += 1
	#check if no ceiling is found in the report 
	if ceiling5 == '': 
		ceiling5 = "No ceiling"
		ceilingString5 = ''
		height5 = ''
		num_height5 = 0



	#list6 
	n = 0 
	ceiling6 = ''
	while n < (len(list6)): 
		if ((list6[n]).find('BKN')) != -1 or ((list6[n]).find('OVC')) != -1: 
			ceiling6 = list6[n]
			#find the type of ceiling 
			ceilingString6 = ceiling6[0] + ceiling6[1] + ceiling6[2]
			#find the height of the ceiling and convert it into an int 
			height6 = ceiling6[3] + ceiling6[4] + ceiling6[5] 
			#removes any extra zeros before the number
			if ceiling6[3] == '0': 
				height6 = ceiling6[4] + ceiling6[5]
				if ceiling6[4] == '0': 
					height6 = ceiling6[5]
			height6 = height6 + '00'
			num_height6 = int(height6) 
			n = 100
		elif ((list6[n]).find('VV')) != -1: 
			ceiling6 = list6[n]
			ceilingString6 = ceiling6[0] + ceiling6[1]
			height6 = ceiling6[2] + ceiling6[3] + ceiling6[4] 
			#removes any extra zeros before the number
			if ceiling6[2] == '0': 
				height6 = ceiling6[3] + ceiling6[4]
				if ceiling6[3] == '0': 
					height6 = ceiling6[4]
			height6 = height6 + '00'
			num_height6 = int(height6)
			n = 100
		else: 
			n += 1
	#check if no ceiling is found in the report 
	if ceiling6 == '': 
		ceiling6 = "No ceiling"
		ceilingString6 = ''
		height6 = ''
		num_height6 = 0
		
		


	#neopixel colors 
	def green(x): 
		pixels[x] = ((0, 127, 0, 0))
		
	def blue(x): 
		pixels[x] = ((0, 0, 127, 0))
		
	def red(x): 
		pixels[x] = ((127, 0, 0, 0))
		
	def purple(x):
		pixels[x] = ((127, 0, 127, 0))
		
	def white(x): 
		pixels[x] = ((0, 0, 0, 127))

	def check(x): 
		#check for the different visibility and ceiling conditions
		#neopixel 0 
		print('') 
		ceiling = ''
		ceilingString = ''
		height = ''
		num_vis = 0
		num_height = 0
		
		if x == 1: 
			print("KCVH")
			ceiling = ceiling1 
			ceilingString = ceilingString1 
			height = height1 
			num_vis = num_vis1
			num_height = num_height1
		elif x == 2: 
			print("KTCY")
			ceiling = ceiling2
			ceilingString = ceilingString2 
			height = height2
			num_vis = num_vis2
			num_height = num_height2
		elif x == 3: 
			print("KSJC")
			ceiling = ceiling3
			ceilingString = ceilingString3
			height = height3
			num_vis = num_vis3
			num_height = num_height3
		elif x == 4: 
			print("KSFO")
			ceiling = ceiling4
			ceilingString = ceilingString4
			height = height4
			num_vis = num_vis4
			num_height = num_height4
		elif x == 5: 
			print("KOAK")
			ceiling = ceiling5
			ceilingString = ceilingString5
			height = height5
			num_vis = num_vis5
			num_height = num_height5
		elif x == 6: 
			print("KAPC")
			ceiling = ceiling6
			ceilingString = ceilingString6
			height = height6
			num_vis = num_vis6
			num_height = num_height6

			
		if num_vis < 1: 
			if ceiling == "No ceiling": 
				print("Ceiling: " + ceiling)
			else: 
				print("Ceiling: " + ceilingString + " at " + height + " ft")
			print("Visibility:" , num_vis, "SM")
			purple(x-1)
			
		elif num_vis < 3: 
			if ceiling == "No ceiling": 
				print("Ceiling: " + ceiling) 
				print("Visibility:" , num_vis, "SM")
				red(x-1)
			else: 
				if num_height < 500: 
					print("Ceiling: " + ceilingString + " at " + height + " ft")
					print("Visibility:" , num_vis, "SM")
					purple(x-1)
				else: 
					print("Ceiling: " + ceilingString + " at " + height + " ft")
					print("Visibility:" , num_vis, "SM")
					red(x-1)
				
		elif num_vis < 5: 
			if ceiling == "No ceiling": 
				print("Ceiling: " + ceiling) 
				print("Visibility:" , num_vis, "SM")
				blue(x-1)
			else: 
				if num_height < 500: 
					print("Ceiling: " + ceilingString + " at " + height + " ft")
					print("Visibility:" , num_vis, "SM")
					purple(x-1)
				elif num_height < 1000: 
					print("Ceiling: " + ceilingString + " at " + height + " ft")
					print("Visibility:" , num_vis, "SM")
					red(x-1)
				else: 
					print("Ceiling: " + ceilingString + " at " + height + " ft")
					print("Visibility:" , num_vis, "SM")
					blue(x-1)
			
		elif num_vis >= 5:
			if ceiling == "No ceiling": 
				print("Ceiling: " + ceiling) 
				print("Visibility:" , num_vis, "SM")
				green(x-1)
			else: 
				if num_height < 500: 
					print("Ceiling: " + ceilingString + " at " + height + " ft")
					print("Visibility:" , num_vis, "SM")
					purple(x-1)
				elif num_height < 1000: 
					print("Ceiling: " + ceilingString + " at " + height + " ft")
					print("Visibility:" , num_vis, "SM")
					red(x-1)
				elif num_height <= 3000: 
					print("Ceiling: " + ceilingString + " at " + height + " ft")
					print("Visibility:" , num_vis, "SM")
					blue(x-1)
				elif num_height > 3000: 
					print("Ceiling: " + ceilingString + " at " + height + " ft")
					print("Visibility:" , num_vis, "SM")
					green(x-1)
		
	#check the flight conditions of the airports 
	check(1)
	check(2)
	check(3)
	check(4)
	check(5)
	check(6)
	
	#print a key for the viewer 
	print('')
	print("Flight Categories: ") 
	print("VFR  - Green   (Best) ")
	print("MVFR - Blue") 
	print("IFR  - Red") 
	print("LIFR - Purple  (Worst) ") 

#refresh every 5 minutes
while True:
	run()
	import time
	time.sleep(300)






