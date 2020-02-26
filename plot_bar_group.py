import sys
import matplotlib
matplotlib.use('Agg')
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
def set_size(fig):
	width = 5.0  # in
	height = 3.0   # in
	fig.set_size_inches(width, height)
	plt.tight_layout()

def set_style():
    	#plt.style.use(['seaborn-ticks', 'seaborn-paper'])
    	plt.style.use('seaborn-white')
	mpl.rc("font", family="monospace")
	mpl.rcParams['pdf.fonttype'] = 42

def get_error_style():
	style_dict=dict()
	style_dict['elinewidth']=4
	style_dict['ecolor']='black'
	style_dict['capstyle']='butt'
	return style_dict

scheme_dict={
	"Large": 0,
	"Large-high": 0,
	"Large-low": 5,
	"Small": 8
}
# scheme_dict["Standalone"]=0
# scheme_dict["Primary"]=1
# scheme_dict["DAS"]=2


def plot(filename):


	fig, ax = plt.subplots()

	
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

		clr = ['grey', 'cyan', 'mediumspringgreen', 'red', 'lightsalmon', 'k', 'white', 'blue', 'magenta']
		pat = ["..", "///", "o" , "--", "xx", "\\\\\\", "**","+","O"]

		font = font_manager.FontProperties(family='monospace')
		fig, ax = plt.subplots()		
		width = 0.24
		opacity = 0.8
		set_size(fig)
		set_style()
		error_style = get_error_style()
	
		
		# ax.set_yscale('log')
		i=0
		for line in fileHandle:
			if line.startswith("#"):
				continue
			key, val = line.split(":")
			if key == "title":
				title = val.rstrip()
			elif key == "axis_labels":
				x_label, y_label = val.rstrip().split(' ')
				x_label = x_label.replace("_"," ")
				y_label = y_label.replace("_"," ")
			elif key == "groups_labels":
				groups = val.rstrip().split(' ')
				group_count = len(groups)
				grp_ind = np.arange(int(group_count))
			elif key == "axis_values":
				xmin, xmax, xstep, ymin, ymax, ystep = map(float, (val.rstrip().split(' ')))
				#xmin, xmax, ymin, ymax = val.rstrip().split(' ')
			elif key == "data":
				avg_val=[]
				max_val=[]
				min_val=[]
				val = val.rstrip().split(' ')
				scheme = val[0]
				data = val[1:]
				# print data
				for info in data:
					values = info.split(",")
					values = map(float, values)
					# values = [v for v in values]
					avg_val.append(values[0])
					max_val.append(values[1]-values[0])
					min_val.append(values[0]-values[2])


				error = [min_val, max_val]
				grp_ind = grp_ind + width
				# i = get_key(scheme)

				i = scheme_dict[scheme]


				rects = plt.bar(grp_ind, values, width, alpha=opacity, color=clr[i], edgecolor='k', hatch=pat[i], label=scheme, zorder=3)
				# rects = plt.bar(grp_ind, avg_val, width, alpha=opacity, color=clr[i], edgecolor='k', hatch=pat[i], label=scheme, yerr=error, error_kw=error_style, zorder=3)
			
				#grp_ind = grp_ind + width
				i = i+1


	        #plt.xlabel(x_label, fontsize=20, family='seaborn-paper')

	        plt.xlabel(x_label, fontsize=20)
        	plt.ylabel(y_label, fontsize=20)
	
		plt.ylim(float(ymin),float(ymax))
		plt.legend(loc="best",fontsize=15,frameon=False)
		
		plt.xticks(grp_ind-1*width, groups)
		plt.yticks(np.arange(ymin,ymax,ystep))
		
		plt.tight_layout()
		# plt.grid()
		# plt.grid(color='k', linestyle='--', linewidth=0.5, zorder=0)
		# ax.xaxis.grid(False)



		for tick in ax.get_xticklabels():
    			tick.set_fontsize(14)
		for tick in ax.get_yticklabels():
    			tick.set_fontsize(14)
			#tick.set_family('serif')
	
		#box = ax.get_position()
		#ax.set_position([box.x0, box.y0 + box.height * 0.1, box.width, box.height * 0.9])	
	

		plt.savefig(title+".pdf", bbox_inches='tight')
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
