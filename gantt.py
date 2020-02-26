import matplotlib.pyplot as plt
from scanf import scanf

def timelines(y, timeline, colors):
    """Plot timelines at y from xstart to xstop with given color."""   
    
    submit = timeline[0]
    start = timeline[1]
    end = timeline[2]

    plt.hlines(y, submit, start, colors[0], lw=20)
    plt.hlines(y, start, end, colors[1], lw=20)
    # plt.vlines(xstart, y+0.04, y-0.04, 'g', lw=2)
    # plt.vlines(xstop, y+0.05, y-0.05, color, lw=2)




# files=["flows.txt"]
# files=["flow0.txt","flow1.txt"]
# files=["flow0_0.txt","flow1_0.txt","flow2_0.txt"]
# files=["fifo_fct"]


file="jobsim_jct"

tf = open(file,'r')
ft = tf.readlines()
tf.close()


# ft = ft[:12]


job_data = []
y = []
for f in ft:
	f_split = f.split(' ')
	
	size = float(f_split[3])
	submit = float(f_split[5])
	start = float(f_split[7])
	end = start + size

	y.append(int(f_split[1]))
	job_data.append([submit,start,end])
	

clr = [['lightcoral','red'],['lightsteelblue','darkblue'],['lightgreen','darkgreen']]


for j in range(0,len(job_data)):
	timelines(y[j],job_data[j],clr[j%len(clr)])


ax = plt.gca()
ax.grid(color='k', linestyle='dashed', linewidth=0.5)

#To adjust the xlimits a timedelta is needed.
# delta = (max(stops) - min(starts))/10

# plt.ylim(0,1)
# plt.xlim(min(starts)-delta, max(stops)+delta)
plt.xlabel('Time')
plt.savefig('foo.pdf', dpi = 300)