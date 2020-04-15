import autopy, sys
from time import sleep

next_page_loc = (152.8, 836.0)
scroll_down_loc = (789.6, 808.8)

TL = (109.0,146.0)
MR = (977.0, 1075.0)
BR = (977.0, 1194.0)

rect = (TL,(MR[0]-TL[0],MR[1]-TL[1]))
last_rect = (TL,(BR[0]-TL[0],BR[1]-TL[1]))

# rect = ((111.0,218.0),(1793.0, 967.0))


def activate_screen():
	autopy.mouse.move(565.0,167.0)
	autopy.mouse.click()

def capture(rect):
	return autopy.bitmap.capture_screen(rect)
	
def page_down():
	autopy.key.tap(autopy.key.Code.PAGE_DOWN)

def page_flip():
	autopy.key.tap(autopy.key.Code.RIGHT_ARROW)

def crop(path,i=0):
	to_crop = autopy.bitmap.Bitmap.open(path)
	to_crop.cropped(((140, 165.0),(840.0,908))).save('screenexpt/screen_%d.png' % i)

def crop_routine():
	for i in range(13):
		crop()

def capture_routine(page_num=0):
	prev=None
	i = 0
	while(True):
		scr = capture(rect)
		if i > 0:
			if scr.is_bitmap_equal(prev):
				scr = capture(last_rect)
				scr.save('screenexpt/screen_%d.png' % (page_num - 1))
				return page_num
		scr.save('screenexpt/screen_%d.png' % page_num)
		prev = scr
		page_down()
		sleep(1)
		page_num += 1
		i+=1

def get_coordinates():
	while 1:
		loc = autopy.mouse.location()
		
		timestr = '\r%.1f,%.1f\t' % (loc[0],loc[1])
		sys.stdout.write(timestr)
		sys.stdout.flush()
		sleep(0.1)


if __name__ == '__main__':
	sleep(7)
	i=0
	for _ in range(4):
		activate_screen()
		i = capture_routine(i)
		page_flip()
		sleep(5)





	# autopy.bitmap.capture_screen(rect).save('screen.png')
	# b = crop('screenexpt/screen_0.png').save('cropped.png')
	# get_coordinates()





