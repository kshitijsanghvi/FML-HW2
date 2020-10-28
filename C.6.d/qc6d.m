
[labels, X] = libsvmread('../scaled_train_data');
[labels_test, X_test] = libsvmread('../scaled_test_data');

 
[m,n] = size(X);

[m_test,n_test] = size(X_test);


accuracy_cv_list = [];
accuracy_test_list = [];

for d=1:4
% 1
new_x = []
for i=1:m
    temp = kernel(X(i,:),X,d);
    new_x = [new_x; temp];
end


new_x_test = []
for i=1:m_test
    temp = kernel(X_test(i,:),X_test,d);
    new_x_test = [new_x_test; temp];
end

model= svmtrain(labels, new_x,'-t 0 -c 64 -v 10');
accuracy_cv_list = [accuracy_cv_list,model];
model= svmtrain(labels, new_x,'-t 0 -c 64');
[predicted_label, accuracy, prob_estimates] = svmpredict(labels_test, new_x_test, model);
accuracy_test_list =[accuracy_test_list,accuracy];
end
% Test accuracy = [70.9770114942529,56.4176245210728,69.9233716475096,70.4022988505747] 
% Cross Validation Accuracy = [78.9658474305777,79.4446217682732,78.4551548037025,77.1784232365145]
