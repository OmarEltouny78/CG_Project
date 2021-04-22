import glob
from PIL import Image

#Retriving all image names and it's path with .jpg extension from given directory path in imageNames list
imageNames = glob.glob(r"C:\Users\omart\PycharmProjects\pythonProject5\images\*.jpg")

#Defining width and height of image
new_width  = 256
new_height = 256

#Count variable to show the progress of image resized
count=0

#Creating for loop to take one image from imageNames list and resize
for i in imageNames:
	#opening image for editing
	img = Image.open(i).convert('RGB')
	#using resize() to resize image
	img = img.resize((new_width, new_height), Image.ANTIALIAS)
	#save() to save image at given path and count is the name of image eg. first image name will be 0.jpg
	img.save(r"C:\Users\omart\PycharmProjects\pythonProject5\images\test\\"+str(count)+".jpg")
	#incrementing count value
	count+=1
	#showing image resize progress
	print("Images Resized " +str(count)+"/"+str(len(imageNames)),end='\r')
