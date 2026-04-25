try:
	import Image
except ImportError:
	from PIL import Image 
import pytesseract
import cv2
import lta_api
import numpy as np
import urllib #for Python 3.x use urlib.request
import os

global visited
global img 
global height 
global width 

def getHSB(r,g,b):

	maxc = max(r,g,b)
	minc = min(r,g,b)

	brightness = (maxc/255)*100
	saturation = 0
	if (maxc != 0):
		saturation = ((maxc-minc)/maxc)*100

	hue = 10

	if maxc - minc != 0:
		if maxc == r:
			hue = (g-b)/(maxc-minc)
		elif maxc == g:
			hue = 2.0 + (b-r)/(maxc-minc)
		else:
			hue = 4.0 + (r-g)/(maxc-minc)
	
	hue *= 60 #600 denotes white
	if hue < 0:	
		hue += 360

	return hue,saturation,brightness

def ocr(image,preprocess):
	print("OCR START")

	gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

	if preprocess == "thresh":
		gray = cv2.threshold(gray,0,255,
			cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

	#make a check to see if median blurring should be done to remove noise
	if preprocess == "blur":
		gray = cv2.medianBlur(gray,3)
	
	print("USING PIL")
	formatted = Image.fromarray(gray)
	print("DOING IMAGE TO STRING")
	text = pytesseract.image_to_string(formatted,config = "-c tessedit_char_whitelist=0123456789 -psm 6") #specifying to only recognise digits
	print("IMAGE TO STRING DONE")
	return text

	#show the output images
	#cv2.imshow("Image",image)
	#cv2.waitKey(0)
	#cv2.imshow("Output",gray)
	#cv2.waitKey(0)


def bfs(start,HSB): #start is a tuple representing start position, HSB is the HSB value of the start position

	global img,width,height,visited

	queue = [start] #list with pop function

	dx = [0,1,1,1,0,-1,-1,-1]
	dy = [1,1,0,-1,-1,-1,0,1]

	top = start[0]
	bottom = start[0]+1
	left = start[1]
	right = start[1]+1

	while queue: #not empty
		square = queue.pop(0)
		r = square[0]
		c = square[1]
		if (r,c) not in visited:
			visited.add((r,c))

			for i in range(0,8):
				ny = r + dy[i]
				nx = c + dx[i]
				if (nx < 0 or nx >= width or ny < 0 or ny >= height):
					continue
				elif ((ny,nx) in visited):
					continue
				else:
					nextH,nextS,nextB = getHSB(float(img[ny][nx][2]),float(img[ny][nx][1]),float(img[ny][nx][0])) #gets HSB values of next pixel
					if (abs(nextH-HSB[0]) <= 3 and abs(nextS-HSB[1]) <= 10): #and abs(nextB-HSB[2]) <= 5): #checks how similar the next pixel is to the original start pixel
						
						queue.append((ny,nx))
						top = min(top,ny)
						bottom = max(bottom,ny)
						left = min(left,nx)
						right = max(right,nx)
						
	return top,left,bottom,right

def findcoderect(URL):

	global img
	
	print("findcoderect START")
	url_response = urllib.urlopen(URL) #for Python 3.x use urllib.request.urlopen()
	print("OPENED URL")
	img = np.array(bytearray(url_response.read()), dtype=np.uint8)
	print("MADE NUMPY ARRAY")
	img =  cv2.imdecode(img,-1)
	print("DECODED TO ORIGINAL")

	print (img.shape)

	r = 1050.0/img.shape[1]
	dim = (1050,int(img.shape[0]*r))

	img = cv2.resize(img,dim,interpolation = cv2.INTER_AREA) #resizes image so width is 1050

	global width,height,visited #to refer to the same width, height and visited set as in bfs()

	width = img.shape[1] #columns
	height = img.shape[0] #rows

	visited = set() 

	text = False
	b = False
	r_factor = int(height/100) #assumes that proportion of height of bus stop code in picture is at most 100 times smaller than image width
	c_factor = int(width/30) #assumes that proportion of width of bus stop code in picture is at most 30 times smaller than image width
	
	for R in range(0,int(height/r_factor)): #loops through every (height/100)-th pixel from top to bottom
		for C in range(0,int(width/c_factor)): #loops through every (width/30)-th pixel from left to reight
			r = R*r_factor
			c = C*c_factor
			
			if (r,c) not in visited:
				hue,saturation,brightness = getHSB(float(img[r][c][2]),float(img[r][c][1]),float(img[r][c][0]))
				if (hue >= 195 and hue <= 215 and saturation >= 60 and saturation <= 90 and brightness <= 80): #performs bfs to attempt to crop a rectangle when pixel color is similar to this range of bus panel colors
					top,left,bottom,right= bfs((r,c),(hue,saturation,brightness))
					area = (right-left)*(bottom-top)
					if (area > 1500): #removes the need to check when cropped areas are small (obvious errors)
						print("Area > 1500, checking for bus stop code...")
						cropped = img[top:bottom,left:right]
						text = ocr(cropped,'thresh') #puts attempted crops into ocr to check for a code

						#cv2.imshow(str(r)+","+str(c),cropped)
						#print(str(r)+","+str(c),text)
						#cv2.waitKey(0) 

						cropped = [] #reduce memory usage
					
						text = lta_api.iscode(text) #checks if it is, or contains a bus code. If not, it will return False.
						if (text):
							b = True
							break
						print("Not a bus stop code, looping...")

		if (b):
			break

	return text


if __name__ == "__main__":
	text = findcoderect('https://scontent-ort2-1.xx.fbcdn.net/v/t35.0-12/27329809_1800323166667633_926103453_o.jpg?_nc_ad=z-m&_nc_cid=0&oh=935f57e0ffdbe2d56bc8e4a47f0779bd&oe=5A6C9156')
	print(text)


