
>output
>pred_output
for d in 1 2 3 4

do
		./svm-train -t 1 -d $d -c 64 -v 10 -q scaled_train_data >> output

done


for d in 1 2 3 4

do
		./svm-train -t 1 -d $d -c 64 -q scaled_train_data >> garbage
		./svm-predict scaled_test_data scaled_train_data.model predic_output >> pred_output

done

python plotter_2.py
