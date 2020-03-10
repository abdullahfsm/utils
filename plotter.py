import statistics, sys, os, argparse

def gen_gnuplot_file(fnames, oname="outs", xr="-1", yr="-1"):

	fd = open("pdf_plotter.plt",'w')
	fd.write("set terminal pdf truecolor size 200,150 enhanced font \"Times-Roman,1000\"\n")
	fd.write("set border lw 150 front\n")
	fd.write("set grid lw 75\n")
	fd.write("set border lw 100 back\n")

	fd.write("\n")
	fd.write("\n")

	#KEYS
	fd.write("set key font \"Times-Roman,800\"\n")
	fd.write("set key bottom right\n")

	fd.write("\n")
	fd.write("\n")


	#OUTPUT
	fd.write("set output \"%s.pdf\"\n"%oname)

	fd.write("\n")
	fd.write("\n")


	#RANGES
	if xr != "-1":
		fd.write("set xr[%s]\n" % xr)
	if yr != "-1":
		fd.write("set yr[%s]\n" % yr)

	fd.write("\n")
	fd.write("\n")


	#YLABEL
	fd.write("set ylabel \'CDF\'\n")
	fd.write("set ylabel offset 2.5\n")
	#set ylabel rotate by 0

	fd.write("\n")
	fd.write("\n")


	#YTICS
	fd.write("#set ytics 0,0.2,1.0\n")
	fd.write("set ytics offset 0.5,0\n")

	fd.write("\n")
	fd.write("\n")

	
	#XLABEL
	fd.write("set xlabel \'us\'\n")
	fd.write("set xlabel offset 0,0.75\n")

	fd.write("\n")
	fd.write("\n")


	#XTICS
	fd.write("#set logscale x\n")
	fd.write("#set xtics 0,200,10000000\n")
	fd.write("set xtics offset 0,0.5\n")

	fd.write("\n")
	fd.write("\n")

	fd.write("set style line 1 lt 2 lw 200 pt 2 ps 50 pi 2000 lc rgb \"#6495ED\"\n")
	fd.write("set style line 2 lt 2 lw 200 pt 3 ps 50 pi 2000 lc rgb \"#303030\"\n")
	fd.write("set style line 3 lt 2 lw 200 pt 4 ps 50 pi 2000 lc rgb \"#ff5050\"\n")
	fd.write("set style line 4 lt 2 lw 200 pt 5 ps 50 pi 2000 lc rgb \"#cc0099\"\n")
	fd.write("set style line 5 lt 2 lw 200 pt 6 ps 40 pi 2000 lc rgb \"#021bba\"\n")
	fd.write("set style line 6 lt 2 lw 200 pt 7 ps 40 pi 2000 lc rgb \"#1eba02\"\n")

	fd.write("plot \\\n")
	i = 0
	for fname in fnames:
		fd.write("\"%s\" u 1:2 t \"%s\" w linespoints ls %d, \\\n" % (fname, fname.split("_")[1], i+1))
		i+=1
		i = i % 6
	fd.close()

	os.system("gnuplot pdf_plotter.plt")



if __name__ == '__main__':

	parser = argparse.ArgumentParser()
	parser.add_argument('-fnames', help = "comma seperated list of files to plot", type=str)
	parser.add_argument('-oname', help = "comma seperated list of files to plot", type=str, default="outs")
	parser.add_argument('-xr', help="x range", default="-1", type=str)
	parser.add_argument('-yr', help="x range", default="-1", type=str)
	args = parser.parse_args()

	gen_gnuplot_file(args.fnames.split(","), args.oname, xr=args.xr, yr=args.yr)