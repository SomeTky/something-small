import sqlite3

class dbmanager:
    def __init__(self, addr):
        self.db_addr = addr
        self.connect = sqlite3.connect(addr)
        if not self.connect:
            raise Exception('DB init fail')
        self.cur = self.connect.cursor()
    
    '''
    创建一张表
    '''
    def create_table(self, table_name: str, table_info: list):
        '''
        Item of table_info, (column_name, type, others)
        '''

        cmd = f'''
                CREATE TABLE {table_name}(
                    id INT AUTO_INCREMENT,
                '''
        for i in range(len(table_info)):
            item = table_info[i]
            cmd += item[0] + ' ' + item[1] + ' '
            if len(item) > 2:
                cmd += item[2]
            if i != len(table_info) - 1:
                cmd += ','
        cmd += ')'
        self.cur.execute(cmd)

    
    def add_one(self,table_name, item_info):
        '''
        向table_name中添加一条,temp_info是添加信息的键值对
        '''

        cmd_keys = str()
        cmd_values = str()

        for i, (k, v) in enumerate(item_info.items()):
            cmd_keys += k
            if type(v) == str:
                cmd_values += f"'{v}'"
            else:
                cmd_values += str(v)
            if i != len(item_info) - 1:
                cmd_keys += ','
                cmd_values += ','

        cmd = f'''
                INSERT INTO {table_name}({cmd_keys})
                VALUES({cmd_values})
                '''
        self.cur.execute(cmd)
        self.connect.commit()

    def get_one_cond(self, table_name, cond) -> list:
        '''
        单条件查询
        cond 是一个长度为2的列表
        where cond[0] = cond[1]
        '''
        cmd = f'''
                SELECT * FROM {table_name}
                where {cond[0]} = '{cond[1]}'
                '''
        self.cur.execute(cmd)

        info = []
        for item in self.cur:
            info.append(item)
        
        return info
    
    def del_one_cond(self, table_name, cond):
        '''
        table_name: 表名
        cond: where cond[0] = cond[1]
        '''
        
        cmd = f'''
                DELETE FROM {table_name} 
                WHERE {cond[0]} = '{cond[1]}'
                '''
        self.cur.execute(cmd)
        self.connect.commit()


db = dbmanager('test.db')

db.del_one_cond('user_info', ('name', 'tky2'))


        
