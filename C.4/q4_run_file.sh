> output_1
> output_2
> output_3
> output_4
for d in 1 2 3 4
do
	echo -e -n "Degree : $d ["
	for c in 0.0009765625 0.001953125 0.00390625 0.0078125 0.015625 0.03125 0.0625 0.125 0.25 0.5 1 2 4 8 16 32 64 128 256 512 1024
	do
		echo -e -n "#"
		./svm-train -t 1 -d $d -c $c -v 10 -q scaled_train_data >> output_$d
	done
	echo -e "#]"
done

python plotter.py
