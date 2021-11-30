import MySQLdb, base64, time


class sql_connect:
    def __init__(self):
        self.sql_host = '163.18.69.14'
        self.sqldb = 'pdal-measurement-2021'
        self.sql_user = 'root'
        self.sql_charset = 'utf8'
        self.sql_password = "rsa+0414018"

        # self.sql_host = gvar.sql_host
        # self.sqldb = gvar.sql_db
        # self.sql_user = gvar.sql_user
        # self.sql_charset = gvar.sql_charset
        # self.sql_password = gvar.sql_password

        self.all_name = ["mysite_project", "mysite_measure_items", "mysite_measurement_work_order_create",
                         "mysite_measuring_tool"]
        self.project_item = ["project_name", "project_create_time", "founder_name", "remake"]
        self.project_work_order = ["project_name", "sor_no", "part_no", "number_of_part", "materials",
                                   "manufacturing_machine",
                                   "batch_number", "class", "inspector", "remake"]
        self.measur_tool = ['tool_name', "tool_type", "tool_precision", "tool_test_date"]
        self.measure_item = ["project_name", "tool_name", "measure_items", "upper", "lower", "center", "decimal_piaces"]

        self.conn = MySQLdb.connect(host=self.sql_host, user=self.sql_user, passwd=self.sql_password, db=self.sqldb,
                                    charset=self.sql_charset)  # 新增 charset="utf8"才會顯示中文
        self.cursor = self.conn.cursor()

    def sql_find_work_order(self, project_name):
        SQL = (
                    "SELECT mysite_measure_items.image_base64_data FROM mysite_measure_items WHERE mysite_measure_items.id='%s'" % project_name)
        self.cursor.execute(SQL)
        data = self.cursor.fetchall()
        # list_data = []
        # for item in data:
        #     all_data = list(item)
        #     all_data.pop(0)
        #     all_data.pop(-1)
        #     all_data.insert(0, project_name)
        #     list_data.append(all_data)
        return data


def save(file_name, base64_data, pict_type):
    with open('%s.%s' % (file_name, pict_type), 'wb') as file:  # wd 寫入覆蓋文件
        jiema = base64.b64decode(base64_data)  # 解碼
        file.write(jiema)  # 將解碼資料寫入到片圖中


sql = sql_connect()
base64_data = sql.sql_find_work_order(62)[0][0]
print(base64_data)
with open('000.jpg', 'wb') as file: #儲存位置在運行py檔下 ^^
    jiema = base64.b64decode(base64_data)  # 解碼
    file.write(jiema)  # 將解碼資料寫入到片圖中

# with open('000.jpg', 'wd') as f:
#     f.write(image_data)
# print("successful")
