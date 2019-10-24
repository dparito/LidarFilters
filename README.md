# LidarFilters
Range filter and temporal median filter for LIDAR scan data


# Filters
Base abstract class containing abstract method "update()"


## Range Filter
- Derived class inheriting from base class FILTERS.
- Overrides abstract method from base class "update()"
- Crops all the values below a specified RANGE_MIN and above a specified RANGE_MAX, and replace them with the RANGE_MIN and RANGE_MAX respectively
  - RANGE_MIN = 0.03
  - RANGE_MAX = 50
- Operates on 1 subset of lidar data set at a time


## Temporal Median Filter
- Derived class inheriting from base class FILTERS.
- Overrides abstract method from base class "update()"
- Returns median of current and previous D scans, where D is a USER INPUT during instantiation. 
- Operates on 1 subset of lidar data set at a time


# Test Cases
Test.py contains 2 test cases:
1. Given Example:
  - Data set with 5 scans, each scan of size 5 as provided in the problem statement

2. Randomized Data Set;
  - Completely randomized 2-dimensional array generated using NumPy library
  - Array consists for 300 elements arranged in 25 rows of 12 elements each
  - Values range from 0.01 to 55
