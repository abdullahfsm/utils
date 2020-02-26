set terminal pdf truecolor size 200,150 enhanced font "Times-Roman,1000"
set border lw 150 front
set grid lw 75
set border lw 100 back

#KEYS
set key font "Times-Roman,800"
set key bottom right
#set key samplen 2
#unset key

set output "acc_history.pdf"

#set logscale x

#RANGES
set yr[0.1:0.8]
set xr[0:20]

#YLABEL
set ylabel 'Test Acc'
set ylabel offset 2.5
#set ylabel rotate by 0

#YTICS
set ytics 0,0.2,1.0
set ytics offset 0.5,0

#XLABEL
set xlabel 'Minutes'
set xlabel offset 0,0.75

#XTICS
#set xtics 0,200,10000000
set xtics offset 0,0.5


set style line 1 lt 2 lw 200 pt 2 ps 50 pi 10 lc rgb "#6495ED"
set style line 2 lt 2 lw 200 pt 3 ps 50 pi 10 lc rgb "#303030"
set style line 3 lt 2 lw 200 pt 4 ps 50 pi 10 lc rgb "#ff5050"
set style line 4 lt 2 lw 200 pt 5 ps 50 pi 10 lc rgb "#cc0099"
set style line 5 lt 2 lw 200 pt 6 ps 40 pi 10 lc rgb "#021bba"
set style line 6 lt 2 lw 200 pt 7 ps 40 pi 10 lc rgb "#1eba02"

#plot \
"acc_history_resnet34_w=1_r=0" u 2:3 t "resnet34-1" w linespoints ls 1, \
"acc_history_resnet34_w=1_r=1" u 2:3 notitle w linespoints ls 1, \
"acc_history_resnet34_w=1_r=2" u 2:3 notitle w linespoints ls 1, \
"acc_history_resnet34_w=1_r=3" u 2:3 notitle w linespoints ls 1, \
"acc_history_resnet34_w=1_r=4" u 2:3 notitle w linespoints ls 1, \
"acc_history_resnet34_w=1_r=5" u 2:3 notitle w linespoints ls 1, \
"acc_history_resnet34_w=1_r=6" u 2:3 notitle w linespoints ls 1, \
"acc_history_resnet34_w=1_r=7" u 2:3 notitle w linespoints ls 1, \
"acc_history_resnet34_w=4_r=0" u 2:3 t "resnet34-4" w linespoints ls 2, \
"acc_history_resnet34_w=4_r=1" u 2:3 notitle w linespoints ls 2, \
"acc_history_resnet34_w=4_r=2" u 2:3 notitle w linespoints ls 2, \
"acc_history_resnet34_w=4_r=3" u 2:3 notitle w linespoints ls 2, \
"acc_history_resnet34_w=4_r=4" u 2:3 notitle w linespoints ls 2, \
"acc_history_resnet34_w=4_r=5" u 2:3 notitle w linespoints ls 2, \
"acc_history_resnet34_w=4_r=6" u 2:3 notitle w linespoints ls 2, \
"acc_history_resnet34_w=4_r=7" u 2:3 notitle w linespoints ls 2, \

#plot \
"compiled_acc_history_resnet18_w=1" u 2:3 t "resnet18-1" w linespoints ls 1, \
"compiled_acc_history_resnet18_w=4" u 2:3 t "resnet18-4" w linespoints ls 2, \
"compiled_acc_history_resnet34_w=1" u 2:3 t "resnet34-1" w linespoints ls 3, \
"compiled_acc_history_resnet34_w=4" u 2:3 t "resnet34-4" w linespoints ls 4


plot \
"compiled_acc_history_vgg16_w=4" u 2:3 t "Baseline" w linespoints ls 4, \
"compiled_acc_history_vgg16_w=1" u 2:3 t "GPU scaling" w linespoints ls 3, \
"compiled_acc_history_vgg11_w=1" u 2:3 t "Resource Adaptation" w linespoints ls 1, \
