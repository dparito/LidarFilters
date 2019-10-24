import numpy

RANGE_MIN = 0.03        # constant for lower limit on range filter
RANGE_MAX = 50          # constant for upper limit on range filter

'''
Abstract base class for all types of filters.
Contains an abstract method: update()
'''
class Filter:

    def __init__(self):
        pass

    def update(self, data):
        raise NotImplementedError("Subclass should implement abstract method")


'''
Filter to clip the data at pre-determined lower and upper limit. 
Derived class inheriting from base class Filter.
Overrides base class method: update
'''
class RangeFilter(Filter):

    # Public Method to clip incoming data at pre-determined lower and upper limit
    # Input: data array of float values of unknown length
    # Returns: modified data with values clipped at limits
    @classmethod
    def update(cls, data):
        data_size = len(data)                       # length of data
        modified_data = numpy.zeros(data_size)
        i = 0

        for point in data:
            if point < RANGE_MIN:
                modified_data[i] = RANGE_MIN        # values less than lower limit are replaced by lower limit
                i = i + 1
            elif point > RANGE_MAX:
                modified_data[i] = RANGE_MAX        # values less than lower limit are replaced by lower limit
                i = i + 1
            else:
                modified_data[i] = data[i]          # values within range are not modified
                i = i + 1
        return modified_data


'''
Filter to determine median of previous D values for every point in the data
Derived class inheriting from base class Filter.
Overrides base class method: update
'''
class MedianFilter(Filter):
    __median_len = 0            # PRIVATE VARIABLE: number of scans to consider to calculate median
    __data_counter = 0          # PRIVATE VARIABLE: number of data scans received
    __data_set = []             # PRIVATE VARIABLE: array of incoming data

    def __init__(self, median_length):
        self.__set_median_len(median_length)      # private variable value updated
        Filter.__init__(self)

    # Getter method for private variable
    @classmethod
    def get_median_len(cls):
        return cls.__median_len

    # PRIVATE SETTER method for private variable
    @classmethod
    def __set_median_len(cls, median_length):
        cls.__median_len = median_length

    # Getter method for private variable
    @classmethod
    def get_data_set(cls):
        return cls.__data_set

    # PRIVATE METHOD to calculate median for every point in the data
    # Input: 2d data array, length of every subarray
    # Returns: array of median values
    @classmethod
    def __calculate_median(cls, data_set, data_size):
        temp_arr = []
        for j in range(0, data_size):
            temp = []
            for i in range(0, len(data_set)):
                temp.append(data_set[i][j])         # creating arrays out of all values in a column
                i += 1
            temp_arr.insert(j, temp)
            j += 1

        median_arr = []
        for t in temp_arr:
            med = numpy.median(t)       # finding median of a column array
            median_arr.append(med)      # creating array of median values

        return median_arr               # returning array of median values

    # Public method called to calculate median of all points in a data set
    # Input: data array of unknown size
    # Returns: array of median values
    @classmethod
    def update(cls, data):

        # index for input data in local data set determined based of number of values considered to calculate median
        data_set_index = cls.__data_counter % cls.get_median_len()
        cls.__data_set.insert(data_set_index, data)                     # local data set populated

        # ensuring the size of local data set remains equal to number of values considered to calculate median
        if len(cls.get_data_set()) > cls.get_median_len():
            while len(cls.get_data_set()) != cls.get_median_len():
                cls.__data_set.pop(data_set_index+1)

        cls.__data_counter += 1     # counting the number of data sets updated

        # calling function to calculate median
        median_filtered_data = cls.__calculate_median(cls.get_data_set(), len(data))

        return median_filtered_data         # return array of median values
