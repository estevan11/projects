import csv

# test data is first entry in iris dataset

distance = {}
test = ['1', 5.1, 3.5, 1.4, 0.2,]
with open('Iris.csv', 'r') as file:
  test_data = csv.reader(file)
  next(test_data, None)
  next(test_data, None)
  for vector in test_data:
    sum = 0
    for i in range(1, 5):
      sum += pow(float(vector[i]) - test[i], 2)
    distance[pow(sum, 0.5)] = vector[5]

sorted(distance)

s = 0
ve = 0
v = 0

for index, key in enumerate(distance.keys()):
  if index == 38:
    break
  if distance[key] == 'Iris-setosa':
    s += 1
  if distance[key] == 'Iris-versicolor':
    ve += 1
  if distance[key] == 'Iris-virginica':
    v += 1

print('setosa confidence', s / (s + ve + v))
print('versicolor confidence', ve / (s + ve + v))
print('virginica confidence', v / (s + ve + v))
