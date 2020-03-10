import statistics, sys, os, argparse

def plogic_util(ft):
	results = []
	for f in ft:
		mu = float(f.split(",")[1].rstrip())
		results.append(mu)

	time = 0

	compiled_fnames.append("compiled_%s"% (fname))

	print("compiled_%s"% (fname))
	print(statistics.median(results))
	print(statistics.mean(results))

	tf = open("compiled_%s"% (fname),'w')
	for r in results:
		tf.write("%d %0.3f\n" % (time,r))
		time += 250
	tf.close()	


def plogic_perf(ft):
	results = []
	for f in ft:
		mu = float(f.split(" ")[3].rstrip())
		results.append(mu)

	results = sorted(results)
	N = len(results)
	
	cdf = 1.0/N

	compiled_fnames.append("compiled_%s"% (fname))

	print("compiled_%s"% (fname))
	print(statistics.median(results))
	print(statistics.mean(results))

	tf = open("compiled_%s"% (fname),'w')
	for r in results:
		tf.write("%0.3f %0.3f\n" % (r,cdf))
		cdf += 1.0/N
	tf.close()	

if __name__ == '__main__':

	parser = argparse.ArgumentParser()
	parser.add_argument('-fnames', help = "comma seperated list of files to parse", type=str)
	parser.add_argument('-ftype', help = "util/perf", type=str)
	args = parser.parse_args()

	compiled_fnames = []
	for fname in args.fname.split(","):
		tf = open(fname,'r')
		ft = tf.readlines()
		tf.close()

		if ftype == "perf":
			plogic_perf(ft)
		elif ftype == "util":
			plogic_util(ft)
		else:
			sys.exit(1)