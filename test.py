import statistics
import sys
import numpy as np
# data = [[10.2, 8.9, 9.9], [10.3, 11, 8.9]]
# all_data = []
# average_data = []
# for item in data:
#     average_data.append(statistics.mean(item))
# print(average_data)
#
# print(statistics.median(average_data)) #x
# # 計算總平均 = 中心線 = cl
# print(format(statistics.mean(average_data), '.3f')) #.3f小數點第三位
# x = statistics.mean(average_data)
# #計算全距 = R
# print(format(np.max(average_data) - np.min(average_data), '.3f'))
# r = np.max(average_data) - np.min(average_data)
# #UCL = x + A2*R
# A2 = float(0.483)
# x_ucl = x + r * A2
# x_lcl = x - r * A2
# print(x_ucl, x_lcl, x)
x= [10.1, 10.3, 10.2]
print(max(x) - min(x))
print(np.min(x))
