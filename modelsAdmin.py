from flask_login import UserMixin

from sql import SQL

class Admin(UserMixin):
    '''
    id
    account
    password
    power
    '''
    def __init__(self):
        self.table_name = 'admins'
        self.sql = SQL()
        self.id = None

    def get_admin_object(self, admin_id):
        target_list = ['id', admin_id]
        sql_result = self.sql.search_line_targetly(self.table_name, target_list)
        try:
            sql_tuple = sql_result.pop(0)
            self.id = sql_tuple[0]
            self.account = sql_tuple[1]
            self.password = sql_tuple[2]
            self.power = sql_tuple[3]
        except:
            print('NO SUCH ADMIN.')

    def add_new_admin(self, admin_list):
        # 在数据库中新加权限为LOW的admin
        self.id = None # id为None则数据库会自增id
        self.account = admin_list[0]
        self.password = admin_list[1]
        self.power = 'LOW'

        value_list = [self.id]
        value_list.append(self.account)
        value_list.append(self.password)
        value_list.append(self.power)

        self.sql.add_line(self.table_name, value_list)

    def delect_low_admin(self, admin_id):
        pass

    def verify_login(self, login_list):
        # 验证登录
        target_list = ['account', login_list[0]]
        print(target_list)
        sql_result = self.sql.search_line_targetly(self.table_name, target_list)
        print(sql_result)
        if sql_result is None:
            result_flag = False
        elif sql_result[0][2] == login_list[1]:
            result_flag = True
        else:
            result_flag = False
        return result_flag
