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
# x= [10.1, 10.3, 10.2]
# print(max(x) - min(x))
# print(np.min(x))
x = 0.1509090909090909
y = [10.5, 11]
print(np.linspace(9.77, 11.43, num=12))
data = np.linspace(9.77, 11.43, num=12)
data_range = []
old_data = []
new_data = []
for item in data:
    a = round(item, 2)
    old_data.append(a)
print(old_data)
for i in range(0, 11, 1):
    new_data.append([old_data[i], old_data[i + 1]])
print(new_data)
Input = [12.8, .178, 1.8, 782.7, 99.8, 8.7]

# 用lambda进行排序
Output = sorted(Input, key=lambda x: float(x))

# 打印输出
print(Output)
x = [10.03, 10.44, 10.3, 9.92, 10.41, 10.49, 10.58, 10.81, 10.3, 10.72, 10.09, 10.12, 10.37, 10.48, 10.77, 10.78, 10.52,
     10.84, 9.99, 10.12, 10.36, 10.86, 10.4, 9.77, 10.06, 10.16, 10.34, 10.53, 10.76, 10.93, 10.74, 10.57, 10.52, 10.67,
     11.04, 11.43, 10.79, 10.64, 10.39, 10.56, 10.76, 11.03, 10.4, 9.85, 10.16, 10.43, 10.55, 10.36, 10.35, 10.86,
     10.64, 10.95, 10.79, 10.74, 10.7, 10.57, 10.54, 10.54, 10.8, 10.65, 10.71, 10.59, 10.44, 10.43, 10.32, 10.17,
     10.17, 10.14, 10.12, 10.23, 10.17, 10.21, 10.09, 10.48, 10.54, 10.65, 10.65, 10.9, 10.86, 10.79, 10.75, 10.65,
     10.65, 10.58, 10.34, 10.34, 10.39, 10.48, 10.35, 10.99]
# x.pop()
z = [[9.77, 9.85, 9.92], [9.99, 10.03, 10.06],
     [10.09, 10.09, 10.12, 10.12, 10.12, 10.14, 10.16, 10.16, 10.17, 10.17, 10.17, 10.21],
     [10.23, 10.3, 10.3, 10.32, 10.34, 10.34, 10.34, 10.35, 10.35, 10.36, 10.36, 10.37],
     [10.39, 10.39, 10.4, 10.4, 10.41, 10.43, 10.43, 10.44, 10.44, 10.48, 10.48, 10.48, 10.49, 10.52, 10.52],
     [10.53, 10.54, 10.54, 10.54, 10.55, 10.56, 10.57, 10.57, 10.58, 10.58, 10.59, 10.64, 10.64, 10.65, 10.65, 10.65,
      10.65, 10.65, 10.67],
     [10.7, 10.71, 10.72, 10.74, 10.74, 10.75, 10.76, 10.76, 10.77, 10.78, 10.79, 10.79, 10.79, 10.8, 10.81],
     [10.84, 10.86, 10.86, 10.86, 10.9, 10.93, 10.95], [10.99, 11.03, 11.04], [], [11.43]]
number = 0
for i in z:
    for i_2 in i:
        number = number + 1
print(number)
x = [1, 1, 2, 3]
for i in x:
    x.remove(i)
print(x)

ca = 0.11
cp = 0.22
cpk = 0.3
color = {
    'A+': "color: whitesmoke; background-color:pink",
    'A': "color: whitesmoke; background-color:orange",
    'B': "color: whitesmoke; background-color:dodgerblue",
    'C': "color: whitesmoke; background-color:seagreen",
    'D': "color: white; background-color:mediumseagreen;"
}

if abs(ca) <= float(0.125):
    ca_color = color['A']
elif abs(ca) > float(0.125) and abs(ca) <= float(0.25):
    ca_color = color['B']
elif abs(ca) > float(0.25) and abs(ca) <= float(0.5):
    ca_color = color['C']
elif abs(ca) > float(0.5):
    ca_color = color['D']

if abs(cp) >= 1.67:
    cp_color = color['A+']
elif abs(cp) >= 1.33 and abs(cp) < 1.67:
    cp_color = color['A']
elif abs(cp) >= 1.0 and abs(cp) < 1.33:
    cp_color = color['B']
elif abs(cp) >= 0.67 and abs(cp) < 1.0:
    cp_color = color['C']
elif abs(cp) < 0.67:
    cp_color = color['D']

if abs(cpk) >= 1.67:
    cpk_color = color['A+']
elif abs(cpk) >= 1.33 and abs(cpk) < 1.67:
    cpk_color = color['A']
elif abs(cpk) >= 1.0 and abs(cpk) < 1.33:
    cpk_colork = color['B']
elif abs(cpk) >= 0.67 and abs(cpk) < 1.0:
    cpk_colork = color['C']
elif abs(cpk) < 0.67:
    cpk_colork = color['D']

print(ca_color)
print(cpk_color)
print(cp_color)
a = [{'x_name': '76_x', 'x_title': '17.LengthX-bar', 'x_x_data': [1, 2, 3, 4, 5, 6],
  'x_y_data': [66.397, 66.403, 66.417, 66.447, 66.417, 66.45], 'x_x_cl_data': [1, 6, '', 1, 6],
  'x_y_cl_data': [66.459, 66.459, '', 66.384, 66.384], 'x_x_viol_data': [], 'x_y_viol_data': [],
  'x_x_center_data': [1, 6], 'x_y_center_data': [66.422, 66.422], 'x_y_range': [66.359, 66.48400000000001],
  'r_name': '76_r', 'r_title': '17.LengthR-bar', 'r_x_data': [1, 2, 3, 4, 5, 6],
  'r_y_data': [0.01999999999999602, 0.05000000000001137, 0.04999999999999716, 0.03999999999999204, 0.020000000000010232,
               0.03999999999999204], 'r_x_cl_data': [1, 6, '', 1, 6], 'r_y_cl_data': [0.095, 0.095, '', 0.0, 0.0],
  'r_x_viol_data': [], 'r_y_viol_data': [], 'r_x_center_data': [1, 6], 'r_y_center_data': [0, 0],
  'r_y_range': [0, 0.1045], 'c_name': '76_c', 'c_title': '   17.Length管制圖',
  'c_x_data': ['1 - 1', '1 - 2', '1 - 3', '2 - 1', '2 - 2', '2 - 3', '3 - 1', '3 - 2', '3 - 3', '4 - 1', '4 - 2',
               '4 - 3', '5 - 1', '5 - 2', '5 - 3', '6 - 1', '6 - 2', '6 - 3'],
  'c_y_data': [66.41, 66.39, 66.39, 66.38, 66.4, 66.43, 66.44, 66.42, 66.39, 66.47, 66.44, 66.43, 66.41, 66.41, 66.43,
               66.43, 66.45, 66.47], 'c_x_viol_data': ['4 - 1', '6 - 3'], 'c_y_viol_data': [66.47, 66.47],
  'c_x_center_data': ['1 - 1', '6 - 3'], 'c_y_center_data': [66.4, 66.4],
  'c_x_cl_data': ['1 - 1', '6 - 3', '', '1 - 1', '6 - 3'], 'c_y_cl_data': [66.45, 66.45, '', 66.375, 66.375],
  'c_x_range': [66.3625, 66.4625], 'data': '量測數值', 'cl': '規格上限/規格下限', 'center': '規格中心', 'vol': '超出',
  'h_t_x_data': ['66.38', '66.39', '66.4', '66.41', '66.42', '66.43', '66.43', '66.44', '66.45', '66.46', '66.47'],
  'h_t_y_data': [1, 3, 1, 3, 1, 0, 4, 2, 1, 0, 2], 'h_chart_name': '17.Length_直方圖', 'h_y_range': [0, 6.0],
  'h_name': '76_h'}, {'x_name': '77_x', 'x_title': '18.WidthX-bar', 'x_x_data': [1, 2, 3, 4, 5, 6],
                      'x_y_data': [49.013, 49.01, 49.033, 49.053, 48.993, 48.993], 'x_x_cl_data': [1, 6, '', 1, 6],
                      'x_y_cl_data': [49.035, 49.035, '', 48.997, 48.997], 'x_x_viol_data': [4, 5, 5],
                      'x_y_viol_data': [49.053, 48.993, 48.993], 'x_x_center_data': [1, 6],
                      'x_y_center_data': [49.016, 49.016], 'x_y_range': [48.98433333333333, 49.047666666666665],
                      'r_name': '77_r', 'r_title': '18.WidthR-bar', 'r_x_data': [1, 2, 3, 4, 5, 6],
                      'r_y_data': [0.07000000000000028, 0.0, 0.00999999999999801, 0.010000000000005116,
                                   0.00999999999999801, 0.00999999999999801], 'r_x_cl_data': [1, 6, '', 1, 6],
                      'r_y_cl_data': [0.046, 0.046, '', 0.0, 0.0], 'r_x_viol_data': [1],
                      'r_y_viol_data': [0.07000000000000028], 'r_x_center_data': [1, 6], 'r_y_center_data': [0, 0],
                      'r_y_range': [0, 0.0506], 'c_name': '77_c', 'c_title': '   18.Width管制圖',
                      'c_x_data': ['1 - 1', '1 - 2', '1 - 3', '2 - 1', '2 - 2', '2 - 3', '3 - 1', '3 - 2', '3 - 3',
                                   '4 - 1', '4 - 2', '4 - 3', '5 - 1', '5 - 2', '5 - 3', '6 - 1', '6 - 2', '6 - 3'],
                      'c_y_data': [48.97, 49.04, 49.03, 49.01, 49.01, 49.01, 49.03, 49.03, 49.04, 49.06, 49.05, 49.05,
                                   49.0, 48.99, 48.99, 48.99, 48.99, 49.0], 'c_x_viol_data': ['1 - 1', '4 - 1'],
                      'c_y_viol_data': [48.97, 49.06], 'c_x_center_data': ['1 - 1', '6 - 3'],
                      'c_y_center_data': [49.0, 49.0], 'c_x_cl_data': ['1 - 1', '6 - 3', '', '1 - 1', '6 - 3'],
                      'c_y_cl_data': [49.05, 49.05, '', 48.975, 48.975], 'c_x_range': [48.962500000000006, 49.0625],
                      'data': '量測數值', 'cl': '規格上限/規格下限', 'center': '規格中心', 'vol': '超出',
                      'h_t_x_data': ['48.97', '48.98', '48.99', '49.0', '49.01', '49.02', '49.02', '49.03', '49.04',
                                     '49.05', '49.06'], 'h_t_y_data': [1, 0, 4, 2, 3, 0, 0, 3, 2, 2, 1],
                      'h_chart_name': '18.Width_直方圖', 'h_y_range': [0, 6.0], 'h_name': '77_h'},
 {'x_name': '78_x', 'x_title': '6.Length(Top)X-bar', 'x_x_data': [1, 2, 3, 4, 5, 6],
  'x_y_data': [67.85, 67.89, 67.91, 67.887, 67.91, 67.92], 'x_x_cl_data': [1, 6, '', 1, 6],
  'x_y_cl_data': [67.92, 67.92, '', 67.869, 67.869], 'x_x_viol_data': [1], 'x_y_viol_data': [67.85],
  'x_x_center_data': [1, 6], 'x_y_center_data': [67.894, 67.894], 'x_y_range': [67.852, 67.937], 'r_name': '78_r',
  'r_title': '6.Length(Top)R-bar', 'r_x_data': [1, 2, 3, 4, 5, 6],
  'r_y_data': [0.060000000000002274, 0.020000000000010232, 0.01999999999999602, 0.010000000000005116,
               0.01999999999999602, 0.020000000000010232], 'r_x_cl_data': [1, 6, '', 1, 6],
  'r_y_cl_data': [0.064, 0.064, '', 0.0, 0.0], 'r_x_viol_data': [], 'r_y_viol_data': [], 'r_x_center_data': [1, 6],
  'r_y_center_data': [0, 0], 'r_y_range': [0, 0.0704], 'c_name': '78_c', 'c_title': '   6.Length(Top)管制圖',
  'c_x_data': ['1 - 1', '1 - 2', '1 - 3', '2 - 1', '2 - 2', '2 - 3', '3 - 1', '3 - 2', '3 - 3', '4 - 1', '4 - 2',
               '4 - 3', '5 - 1', '5 - 2', '5 - 3', '6 - 1', '6 - 2', '6 - 3'],
  'c_y_data': [67.85, 67.88, 67.82, 67.9, 67.89, 67.88, 67.9, 67.91, 67.92, 67.88, 67.89, 67.89, 67.9, 67.92, 67.91,
               67.92, 67.91, 67.93], 'c_x_viol_data': ['1 - 3', '6 - 3'], 'c_y_viol_data': [67.82, 67.93],
  'c_x_center_data': ['1 - 1', '6 - 3'], 'c_y_center_data': [67.9, 67.9],
  'c_x_cl_data': ['1 - 1', '6 - 3', '', '1 - 1', '6 - 3'], 'c_y_cl_data': [67.925, 67.925, '', 67.85, 67.85],
  'c_x_range': [67.83749999999999, 67.9375], 'data': '量測數值', 'cl': '規格上限/規格下限', 'center': '規格中心', 'vol': '超出',
  'h_t_x_data': ['67.82', '67.84', '67.84', '67.85', '67.87', '67.88', '67.88', '67.9', '67.9', '67.91', '67.93'],
  'h_t_y_data': [1, 0, 1, 1, 0, 3, 6, 6, 6, 6, 4], 'h_chart_name': '6.Length(Top)_直方圖', 'h_y_range': [0, 9.0],
  'h_name': '78_h'}, {'x_name': '79_x', 'x_title': '4.Width(Top)X-bar', 'x_x_data': [1, 2, 3, 4, 5, 6],
                      'x_y_data': [51.01, 50.99, 50.973, 50.967, 51.01, 51.01], 'x_x_cl_data': [1, 6, '', 1, 6],
                      'x_y_cl_data': [51.022, 51.022, '', 50.964, 50.964], 'x_x_viol_data': [], 'x_y_viol_data': [],
                      'x_x_center_data': [1, 6], 'x_y_center_data': [50.993, 50.993],
                      'x_y_range': [50.94466666666666, 51.041333333333334], 'r_name': '79_r',
                      'r_title': '4.Width(Top)R-bar', 'r_x_data': [1, 2, 3, 4, 5, 6],
                      'r_y_data': [0.020000000000003126, 0.020000000000003126, 0.030000000000001137,
                                   0.060000000000002274, 0.020000000000003126, 0.020000000000003126],
                      'r_x_cl_data': [1, 6, '', 1, 6], 'r_y_cl_data': [0.072, 0.072, '', 0.0, 0.0], 'r_x_viol_data': [],
                      'r_y_viol_data': [], 'r_x_center_data': [1, 6], 'r_y_center_data': [0, 0],
                      'r_y_range': [0, 0.07919999999999999], 'c_name': '79_c', 'c_title': '   4.Width(Top)管制圖',
                      'c_x_data': ['1 - 1', '1 - 2', '1 - 3', '2 - 1', '2 - 2', '2 - 3', '3 - 1', '3 - 2', '3 - 3',
                                   '4 - 1', '4 - 2', '4 - 3', '5 - 1', '5 - 2', '5 - 3', '6 - 1', '6 - 2', '6 - 3'],
                      'c_y_data': [51.0, 51.01, 51.02, 51.0, 50.99, 50.98, 50.96, 50.99, 50.97, 50.93, 50.99, 50.98,
                                   51.0, 51.01, 51.02, 51.0, 51.02, 51.01], 'c_x_viol_data': ['4 - 1'],
                      'c_y_viol_data': [50.93], 'c_x_center_data': ['1 - 1', '6 - 3'], 'c_y_center_data': [51.0, 51.0],
                      'c_x_cl_data': ['1 - 1', '6 - 3', '', '1 - 1', '6 - 3'],
                      'c_y_cl_data': [51.025, 51.025, '', 50.95, 50.95], 'c_x_range': [50.9375, 51.037499999999994],
                      'data': '量測數值', 'cl': '規格上限/規格下限', 'center': '規格中心', 'vol': '超出',
                      'h_t_x_data': ['50.93', '50.94', '50.95', '50.96', '50.97', '50.97', '50.98', '50.99', '51.0',
                                     '51.01', '51.02'], 'h_t_y_data': [1, 0, 0, 1, 1, 0, 2, 3, 4, 3, 3],
                      'h_chart_name': '4.Width(Top)_直方圖', 'h_y_range': [0, 6.0], 'h_name': '79_h'},
 {'x_name': '80_x', 'x_title': '5.Length(Bot)X-bar', 'x_x_data': [1, 2, 3, 4, 5, 6],
  'x_y_data': [71.897, 71.897, 71.897, 71.873, 71.9, 71.897], 'x_x_cl_data': [1, 6, '', 1, 6],
  'x_y_cl_data': [71.953, 71.953, '', 71.834, 71.834], 'x_x_viol_data': [], 'x_y_viol_data': [],
  'x_x_center_data': [1, 6], 'x_y_center_data': [71.894, 71.894], 'x_y_range': [71.79433333333334, 71.99266666666666],
  'r_name': '80_r', 'r_title': '5.Length(Bot)R-bar', 'r_x_data': [1, 2, 3, 4, 5, 6],
  'r_y_data': [0.07000000000000739, 0.07000000000000739, 0.04999999999999716, 0.04000000000000625, 0.05000000000001137,
               0.07000000000000739], 'r_x_cl_data': [1, 6, '', 1, 6], 'r_y_cl_data': [0.149, 0.149, '', 0.0, 0.0],
  'r_x_viol_data': [], 'r_y_viol_data': [], 'r_x_center_data': [1, 6], 'r_y_center_data': [0, 0],
  'r_y_range': [0, 0.1639], 'c_name': '80_c', 'c_title': '   5.Length(Bot)管制圖',
  'c_x_data': ['1 - 1', '1 - 2', '1 - 3', '2 - 1', '2 - 2', '2 - 3', '3 - 1', '3 - 2', '3 - 3', '4 - 1', '4 - 2',
               '4 - 3', '5 - 1', '5 - 2', '5 - 3', '6 - 1', '6 - 2', '6 - 3'],
  'c_y_data': [71.93, 71.86, 71.9, 71.9, 71.86, 71.93, 71.92, 71.9, 71.87, 71.86, 71.9, 71.86, 71.93, 71.88, 71.89,
               71.9, 71.86, 71.93], 'c_x_viol_data': ['1 - 2', '2 - 2', '4 - 1', '4 - 3', '6 - 2'],
  'c_y_viol_data': [71.86, 71.86, 71.86, 71.86, 71.86], 'c_x_center_data': ['1 - 1', '6 - 3'],
  'c_y_center_data': [71.9, 71.9], 'c_x_cl_data': ['1 - 1', '6 - 3', '', '1 - 1', '6 - 3'],
  'c_y_cl_data': [71.94, 71.94, '', 71.863, 71.863], 'c_x_range': [71.85016666666667, 71.95283333333333],
  'data': '量測數值', 'cl': '規格上限/規格下限', 'center': '規格中心', 'vol': '超出',
  'h_t_x_data': ['71.86', '71.87', '71.88', '71.88', '71.89', '71.9', '71.9', '71.91', '71.91', '71.92', '71.93'],
  'h_t_y_data': [5, 1, 0, 1, 1, 0, 5, 0, 0, 1, 4], 'h_chart_name': '5.Length(Bot)_直方圖', 'h_y_range': [0, 7.5],
  'h_name': '80_h'}, {'x_name': '81_x', 'x_title': '3.Width(Bot)X-bar', 'x_x_data': [1, 2, 3, 4, 5, 6],
                      'x_y_data': [55.026, 54.983, 55.007, 55.035, 55.003, 55.0], 'x_x_cl_data': [1, 6, '', 1, 6],
                      'x_y_cl_data': [55.039, 55.039, '', 54.979, 54.979], 'x_x_viol_data': [], 'x_y_viol_data': [],
                      'x_x_center_data': [1, 6], 'x_y_center_data': [55.009, 55.009],
                      'x_y_range': [54.958999999999996, 55.059000000000005], 'r_name': '81_r',
                      'r_title': '3.Width(Bot)R-bar', 'r_x_data': [1, 2, 3, 4, 5, 6],
                      'r_y_data': [0.03900000000000148, 0.010000000000005116, 0.030000000000001137,
                                   0.009000000000000341, 0.05799999999999983, 0.030000000000001137],
                      'r_x_cl_data': [1, 6, '', 1, 6], 'r_y_cl_data': [0.075, 0.075, '', 0.0, 0.0], 'r_x_viol_data': [],
                      'r_y_viol_data': [], 'r_x_center_data': [1, 6], 'r_y_center_data': [0, 0],
                      'r_y_range': [0, 0.08249999999999999], 'c_name': '81_c', 'c_title': '   3.Width(Bot)管制圖',
                      'c_x_data': ['1 - 1', '1 - 2', '1 - 3', '2 - 1', '2 - 2', '2 - 3', '3 - 1', '3 - 2', '3 - 3',
                                   '4 - 1', '4 - 2', '4 - 3', '5 - 1', '5 - 2', '5 - 3', '6 - 1', '6 - 2', '6 - 3'],
                      'c_y_data': [55.039, 55.038, 55.0, 54.98, 54.99, 54.98, 54.99, 55.02, 55.01, 55.03, 55.039,
                                   55.037, 55.038, 54.99, 54.98, 55.02, 54.99, 54.99],
                      'c_x_viol_data': ['1 - 1', '4 - 2'], 'c_y_viol_data': [55.039, 55.039],
                      'c_x_center_data': ['1 - 1', '6 - 3'], 'c_y_center_data': [55.0, 55.0],
                      'c_x_cl_data': ['1 - 1', '6 - 3', '', '1 - 1', '6 - 3'],
                      'c_y_cl_data': [55.038, 55.038, '', 54.963, 54.963], 'c_x_range': [54.950500000000005, 55.0505],
                      'data': '量測數值', 'cl': '規格上限/規格下限', 'center': '規格中心', 'vol': '超出',
                      'h_t_x_data': ['54.98', '54.99', '54.99', '55.0', '55.0', '55.01', '55.02', '55.02', '55.03',
                                     '55.03', '55.04'], 'h_t_y_data': [3, 5, 0, 1, 0, 1, 0, 2, 0, 1, 5],
                      'h_chart_name': '3.Width(Bot)_直方圖', 'h_y_range': [0, 7.5], 'h_name': '81_h'}]
