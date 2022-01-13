"""
Simple Numpy Exercise

I am sure that you were already familiar with all the concepts presented above,
but a short recap is always welcomed.
Now let's do a very simple exercise with numpy arrays.
In a (4, 7) numpy array we store the statistics about coronavirus cases in the
last week in our country. The rows specify the number of tests with a positive
test result, the number of tests with a negative test result (first testing for
the subject), the number of inconclusive tests and the number of fatalities, respectively.
The columns specify the day of the week for which the statistics were reported.

Compute the following (without using any explicitly for loop):
- the total number of tests performed each day
- the percentage of daily positive tests and the percentage of daily inconclusive
tests (as an array with 2 rows and 7 columns)
- the day in which the maximum number of deaths occurred
- the sum of daily deaths and positive test results for each working day (the result
with be an array with 5 elements)
- the number of positive tests results, the number of tests with a negative test result,
- the number of inconclusive tests and the number of fatalities for the week as a (1, 4) array

"""

import numpy as np

# the total number of tests performed each day
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
statistics = np.array([
                      [1200, 1234, 1580, 1468, 1300, 1367, 800], # positive test results
                      [24356, 24136, 22656, 22111, 22346, 18900, 14000], # negative test results
                      [134, 100, 491, 500, 301, 200, 300],  # inconclusive tests
                      [23, 14, 15, 16, 7, 5, 1]]) # number of fatalities

# compute the sum of positive, negative and inconclusive tests(:3 = first 3 rows of array) for each day of the week
totalNumberOfTests = np.array([
    [days[0], np.sum(statistics[:3, 0])],
    [days[1], np.sum(statistics[:3, 1])],
    [days[2], np.sum(statistics[:3, 2])],
    [days[3], np.sum(statistics[:3, 3])],
    [days[4], np.sum(statistics[:3, 4])],
    [days[5], np.sum(statistics[:3, 5])],
    [days[6], np.sum(statistics[:3, 6])]
])
# other way to solve the problem
totalNumberOfTestsSecond = np.add(np.add(statistics[0, :], statistics[1, :]), statistics[2, :])
print("The total number of tests performed each day is: \n", totalNumberOfTests)
print("The total number of tests performed each day is (second way): \n", totalNumberOfTestsSecond)

# the percentage of daily positive tests and the percentage of daily inconclusive
# tests (as an array with 2 rows and 7 columns)
# get an array of total tests made for each day of the week in order to compute easier the percentage
totalTestsArray = np.array([
    np.sum(statistics[:3, 0]),
    np.sum(statistics[:3, 1]),
    np.sum(statistics[:3, 2]),
    np.sum(statistics[:3, 3]),
    np.sum(statistics[:3, 4]),
    np.sum(statistics[:3, 5]),
    np.sum(statistics[:3, 6])
])
# get an array with all positive tests
positiveTests = statistics[0, :]
# get an array with all inconclusive tests
inconclusiveTests = statistics[2, :]
# multiply each array element with 100, in order to compute the average
positiveTests = np.multiply(positiveTests,  np.array(100))
inconclusiveTests = np.multiply(inconclusiveTests, np.array(100))
# divide each value by total number of tests => (positiveNoOfTests*100)/totalNoOfTests
thePercentageOfPositiveTests = np.divide(positiveTests, totalTestsArray)
thePercentageOfInconclusiveTests = np.divide(inconclusiveTests, totalTestsArray)
# print the result as an array with 2 rows and 7 columns
print("The percentage of daily positive tests and the percentage of daily inconclusive tests: ",
      np.array([thePercentageOfPositiveTests, thePercentageOfInconclusiveTests]))

# the day in which the maximum number of deaths occurred
# np.argmax - returns the index of the max value from array
# optional when the array has rank 2 or grater the axe should be provided
maxValueIndex =  np.argmax(statistics[3, :])
print("The day in which the maximum number of deaths occurred is: " , days[maxValueIndex])

# the sum of daily deaths and positive test results for each working day (the result
# with be an array with 5 elements)
# we perform an element wise add operation between the array of daily positive test (position
# 0 in statistics) results and daily deaths (position 3 in statistics), and we go until :5 -
# only working days
sumeResult =  np.array([
    np.add(statistics[0, :5], statistics[3, :5])
])
print("The sum of daily deaths and positive test results for each working day is: ", sumeResult)

# the number of positive tests results, the number of tests with a negative test result, the number
# of inconclusive tests and the number of fatalities for the week as a (1, 4) array
totalWeekResult = np.array([
    np.sum(statistics[0, :]),
    np.sum(statistics[1, :]),
    np.sum(statistics[2, :]),
    np.sum(statistics[3, :])
])
print("The number of positive tests results, the number of tests with a negative test result, "
      "the number of inconclusive tests and the number of fatalities for the week: ", totalWeekResult)