import numpy

from Filters import RangeFilter, MedianFilter


'''
Calls function to range filter lidar scan data
Input: original data set
Returns: range modified data
'''
def use_range_filter(data):
    range_filter = RangeFilter()        # instantiating object of RangeFilter class
    i = 0

    # update function called for every subset of input data
    for reading in data:
        filtered_reading = range_filter.update(reading)
        data[i] = filtered_reading
        i += 1

    return data         # returns range modified data


'''
Calls function to calculate median of specified number of previous scans
Input: original data set
User Input: Number of samples to consider to calculate median
Returns: array of median values
'''
def use_median_filter(data):
    median_len = input("Enter number of samples to consider to calculate median = ")
    median_filter = MedianFilter(median_len)        # instantiating object of MedianFilter class
    i = 0

    # update function called for every subset of input data
    for reading in data:
        filtered_reading = median_filter.update(reading)
        data[i] = filtered_reading
        i += 1

    return data         # returns array of medain values


'''
Creates a 2-dimensional array based on the example provided
to be used as test lidar scans
Input: N/A
Returns: test data
'''
def test_data_1():
    test_data = [[0, 1, 2, 1, 3],
                 [1, 5, 7, 1, 3],
                 [2, 3, 4, 1, 0],
                 [3, 3, 3, 1, 3],
                 [10, 2, 4, 0, 0]]
    return test_data


'''
Generates a 2-dimensional array of floating point number
to be used as test lidar scans
Input: N/A
Returns: test data
'''
def test_data_2():
    test_data = numpy.linspace(0.01, 55, 300).reshape(25, 12)
    return test_data


def main():

    # lidar_data = test_data_1()        # test data 5x5
    lidar_data = test_data_2()          # test data 25x12
    print ("\nOriginal data --> \n")
    print (lidar_data)

    range_filtered_data = use_range_filter(lidar_data)
    print ("\nRange Filtered data --> \n")
    print (range_filtered_data)

    median_filtered_data = use_median_filter(lidar_data)
    print ("\nMedian Filtered data --> \n")
    print (median_filtered_data)


if __name__ == '__main__':
    main()
