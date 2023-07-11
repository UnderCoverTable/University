from more_itertools import sample
import pandas as pd
import numpy


TrainData = pd.read_csv('trainNaive.csv')
label = pd.read_csv('trainNaiveLabels.csv')

TrainData.drop('Id', inplace=True, axis=1) # Dropped ID coloumn
lb = label.loc[:,"label1"] # Got label1 coloumn from trainNaiveLabel file




def prior_probability(df_coloumn):
	df_coloumn_list = df_coloumn.tolist()
	size_coloumn = len(df_coloumn_list)
	one_count = 0
	zero_count = 0

	for i in df_coloumn_list:
		if i == 1:
			one_count += 1
		else:
			zero_count += 1

	prior0 = zero_count/size_coloumn
	prior1 = one_count/size_coloumn

	return (prior0,prior1)

def feature_probability(feature):


	feature = feature.tolist()
	feature_size = len(feature)
	one_count = 0
	zero_count = 0

	for n in feature:
		if n == 1:
			one_count += 1
		else:
			zero_count += 1

	prob0 = zero_count / feature_size
	prob1 = one_count / feature_size

	return [prob0,prob1]

def test_data(feats):
	

	sample_row = (TrainData.sample())
	sample_index = sample_row.index.tolist()[0] + 1

	if sample_index == 1700:
			sample_index = sample_row.index.tolist()[0] - 1


	sample_row = sample_row.values
	sample_row = sample_row.tolist()[0]

	it = 0
	one_probs = 1
	zero_probs = 1

	for i in sample_row:
		current_feat = feats[it]
		it += 1

		if i == 1:
			one_probs = one_probs * current_feat[1]
		else:
			zero_probs = zero_probs * current_feat[0]

	return zero_probs,one_probs,sample_index

	





def main():




	priors = prior_probability(lb)

	f1 = feature_probability(TrainData.loc[:,"feat1"])
	f2 = feature_probability(TrainData.loc[:,"feat2"])
	f3 = feature_probability(TrainData.loc[:,"feat3"])
	f4 = feature_probability(TrainData.loc[:,"feat4"])
	f5 = feature_probability(TrainData.loc[:,"feat5"])
	f6 = feature_probability(TrainData.loc[:,"feat6"])
	f7 = feature_probability(TrainData.loc[:,"feat7"])
	f8 = feature_probability(TrainData.loc[:,"feat8"])
	f9 = feature_probability(TrainData.loc[:,"feat9"])
	f10 = feature_probability(TrainData.loc[:,"feat10"])

	feats = [f1,f2,f3,f4,f5,f6,f7,f8,f9,f10]

	all_accuracies = []
	accuracy_check = []
	n = 10

	for j in range(n):
		accuracy = 0

		nn = n*100
		for i in range(nn):


			test_data_probs = test_data(feats)
			# print(test_data_probs)

			temp_zero_label = test_data_probs[0] / priors[0]
			temp_one_label = test_data_probs[1] / priors[1]

			new_label = max(temp_zero_label,temp_one_label)
			if new_label == temp_one_label:
				new_label = 1
			else:
				new_label = 0

			new_label_index = test_data_probs[2] 

			orignal_label = lb.tolist()[new_label_index]

			if orignal_label == new_label:
				accuracy += 1

		accuracy_check.append(accuracy)
		accuracy = (accuracy / nn) * 100
		all_accuracies.append(accuracy)

	#print(all_accuracies)

	for n in range(0,len(accuracy_check)):
		print(f"Iter {n+1} --> {accuracy_check[n]}	/ {nn} correct")

	print(f"Accuracy : {round(sum(all_accuracies) / len(all_accuracies))}%")

main()


