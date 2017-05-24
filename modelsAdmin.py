from flask_login import UserMixin

from sql import SQL

class Admin(UserMixin):

    
    def __init__(self):
        self.table_name = 'admins'
        self.sql = SQL()
        self.id = None
        self.account = None
        self.password = None
        self.power = None
        self.info = None

    def get_account(self):
        return self.account

    def get_info(self):
        return self.info

    def get_power(self):
        return self.power
        
    def is_HIGH(self):
        if self.power == 'HIGH':
            return True
        else:
            return False

    def get_admin_object(self, admin_id):
        target_list = ['id', admin_id]
        sql_result = self.sql.search_line_targetly(self.table_name, target_list)
        try:
            sql_tuple = sql_result.pop(0)
            self.id = sql_tuple[0]
            self.account = sql_tuple[1]
            self.password = sql_tuple[2]
            self.power = sql_tuple[3]
            self.info = sql_tuple[4]
        except:
            print('NO SUCH ADMIN.')

    def result_to_object(self, sql_result):
        # sql_result：一行数据是一个元组，整个数据是一个列表；[(-),...]
        # 从sql_result中获取数据，保存到对象中去
        if sql_result != []:
            result_tuple = sql_result[0]
            self.id = result_tuple[0]
            self.account = result_tuple[1]
            self.password = result_tuple[2]
            self.power = result_tuple[3]
            self.info = result_tuple[4]
        else:
            pass

    def result_to_object_list(self, sql_result):
        # 从sql_result中获取数据，保存为对象列表
        admin_list = []
        if sql_result != []:
            for i in range(len(sql_result)):
                admin = Admin()
                admin.result_to_object([sql_result.pop()])
                admin_list.append(admin)
            return admin_list

    def search_all(self):
        # 搜索全部管理员，返回一个object_list
        sql_result = self.sql.search_line_all(self.table_name)
        return self.result_to_object_list(sql_result)

    def add_new_admin(self, admin_list):
        # 在数据库中新加权限为LOW的admin
        self.id = None # id为None则数据库会自增id
        self.account = admin_list[0]
        self.password = admin_list[1]
        self.power = 'LOW'
        self.info = admin_list[2]

        value_list = [self.id]
        value_list.append(self.account)
        value_list.append(self.password)
        value_list.append(self.power)
        value_list.append(self.info)

        self.sql.add_line(self.table_name, value_list)

    def delect_low_admin(self, admin_id):
        pass

    def verify_login(self, login_list):
        # 验证登录
        target_list = ['account', login_list[0]]
        sql_result = self.sql.search_line_targetly(self.table_name, target_list)
        try:
            if sql_result[0][2] == login_list[1]:
                result_flag = True
            else:
                result_flag = False
        except:
            result_flag = False
        return result_flag
