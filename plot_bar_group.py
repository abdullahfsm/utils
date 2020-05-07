import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import matplotlib as mpl
import matplotlib.font_manager as font_manager
'''
Script plots a bar plot for a given data file for a
maximum of 4 scheme comparison. The first line in 
data file is the title of the plot. The second line
contains xlable and ylable respectively seperated by
a space. The third line contains group count followed
by group lables, each seperated by a space. The fourth
line has information about axis limits (min max). For 
x-axis we cannot specify limits in this type of graph 
therefore, these are set to 0. The y-limits are required.

Following lines, each has information about one type of a
scheme. Each scheme result has a scheme name followed by
stdev, mean, 90th, 95th, 99th and 99.9th percentile values
'''



def multi_line(groups):
	new_groups = []
	for g in groups:
		g = g.replace("_"," ")
		a = g.split("\\n")
		new_groups.append("\n".join(a))
	return new_groups[:]

def set_style():
	#plt.style.use(['seaborn-ticks', 'seaborn-paper'])
	
	plt.style.use('seaborn-paper')
	# mpl.rc("font", family="monospace")
	mpl.rcParams['pdf.fonttype'] = 42
	mpl.rcParams['ps.fonttype'] = 42


def set_frame(ax):
	ax.spines['top'].set_visible(False)
	ax.spines['right'].set_visible(False)
	#ax.spines['top'].set_linewidth(2)
	#ax.spines['right'].set_linewidth(2)
	ax.spines['bottom'].set_linewidth(2)
	ax.spines['left'].set_linewidth(2)
	ax.xaxis.set_label_position('top')

def plot(filename):

	set_style()
	with open(filename,'r') as fileHandle:
		count = 0
		scheme_count = 0
		scheme_name = []
		row = 0
		title = ""
		group_count = 0
		scheme_count = 0
		groups = []
		data = []
		stdev = []

		for line in fileHandle:
			if line.startswith("#"):
				continue
			if count == 0:
				title = line.rstrip()
			elif count == 1:
				x_label, y_label = line.rstrip().split(' ')
				if (x_label == "_"):
					x_label = " "
				else:
					x_label = x_label.replace("_"," ")
				if (y_label == "_"):
					y_label = ""
				else:
					y_label = y_label.replace("_"," ")

			elif count == 2:
				groups = line.rstrip().split(' ')[1:]
				group_count = len(groups)
				scheme_count = line.split(' ')[0]
			elif count == 3:
				xmin, xmax, ymin, ymax = line.rstrip().split(' ')
			else:
				line = line.strip().split(' ')
					
				scheme_name.append(line[0].replace("_"," "))
				data.append(line[1:])
			count = count + 1

		fig, ax = plt.subplots()		
		#grp_ind = np.arange(int(group_count))
		grp_ind = np.arange(0,2,1)
		# grp_ind = np.arange(0,2,0.5)
		offset = 10
		width = 0.2
		opacity = 0.8

		# clr = ['grey', 'cyan', 'mediumspringgreen', 'r', 'lightsalmon', 'r', 'k']
		clr = ['b', 'k','r','k', 'k']
		# pat = ["..", "///", "o" , "--", "...", "\\\\\\", "o","--"]
		pat = ["", "","", "o" , "--" ]
		
		i = 0
		rects = []
		grp_ind += offset

		for line in data:
			#print line 
			error = []
			line = map(float, line)
			if i == 1:
				rects = plt.bar(grp_ind, line, width, alpha=opacity, color='w', edgecolor='w', hatch=pat[i], label="_nolegend")
			else:
				rects = plt.bar(grp_ind, line, width, alpha=opacity, color=clr[i], edgecolor='w', hatch=pat[i], label=scheme_name[i])
			grp_ind = grp_ind + width
			i = i+1

		set_frame(ax)



		#x-axis Setup 
		plt.xlabel(x_label, fontsize=20)
		ax.xaxis.set_label_coords(0.5, -0.22)

		groups = multi_line(groups)

		# print(str(groups))

		plt.xticks(0.1 + grp_ind-2*width, groups)
		for tick in ax.get_xticklabels():
				tick.set_fontsize(20)
		
		#y-axis Setup 
		plt.ylabel(y_label, fontsize=20)
		# plt.yticks([0, 10, 20, 30, 40, 50, 55, 60, 65, 70])
		# plt.yticks(range(0,100,20))
		plt.yticks(range(0,4,1))
		plt.ylim(float(0),float(ymax))
		for tick in ax.get_yticklabels():
				tick.set_fontsize(20)
		
		# plt.legend(loc="upper left", fontsize=12,frameon=True, ncol=3)		
		plt.legend(loc="upper center", fontsize=20,frameon=True, ncol=3)		
		plt.tight_layout()
	
		plt.savefig(title+".png", bbox_inches='tight')
	fileHandle.close()

if __name__ == "__main__":
	if len(sys.argv) < 2:
		print "Usage: python plot_bar.py <filename>"
		exit(0)
	if sys.argv[1] == "--help" or sys.argv[1] == "-Help":
		print "Usage: python plot_bar.py <filename>"
		exit(0)
	filename = sys.argv[1]
	plot(filename)
