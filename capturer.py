import autopy
from time import sleep

next_page_loc = (152.8, 836.0)
scroll_down_loc = (789.6, 808.8)

def activate_screen():
	autopy.mouse.move(452.0, 198.4)
	autopy.mouse.click()

def capture(i):
	autopy.bitmap.capture_screen().save('screenexpt/screen_%d.png' % i)

def page_down():
	autopy.key.tap(autopy.key.Code.PAGE_DOWN)

def crop(path,i=0):
	to_crop = autopy.bitmap.Bitmap.open(path)
	to_crop.cropped(((140, 165.0),(840.0,908))).save('screenexpt/screen_%d.png' % i)

def crop_routine():
	for i in range(13):
		crop()

def capture_routine():
	activate_screen()
	sleep(1)
	for i in range(13):
		capture(i)
		page_down()
		sleep(1)

def get_coordinates():
	while 1:
		loc = autopy.mouse.location()
		print(loc)
		sleep(1)


if __name__ == '__main__':
		
	b = crop('screenexpt/screen_0.png').save('cropped.png')



