from db.repository import *
import mysql.connector


class MysqlRepository(Repository):

    def __init__(self):
        super().__init__()
        config = {
            'user': 'root',
            'password': 'root',
            'host': 'localhost', # to run LOCALLY, this should be localhost
            'port': '32000', # to run LOCALLY, this should be 32000
            'database': 'cxdata'
        }
        self.connection = mysql.connector.connect(**config)
        self.cursor = self.connection.cursor()

    def __del__(self):
        #self.cursor.close()
        self.connection.close()

    def save_study(self, studyobj):
        sql = ("INSERT INTO study "
         "(studyname) "
         f"VALUES ("
         f"'{studyobj.studyname}') "
        )
        print(sql)
        self.cursor.execute(sql)
        self.connection.commit()

    def save_file(self, fileobj):
        sql = ("INSERT INTO file "
         "(file_name,all_text) "
         f"VALUES ("
         f"'{fileobj.file_name}', "
         f"'{fileobj.all_text}') "
         )
        print(sql)
        self.cursor.execute(sql)
        self.connection.commit()

    def save_dialog(self, dialogobj):
        sql = ("INSERT INTO dialog "
               "(line_number,clean_timestamp,speaker_name,file_id,output_filename) "
               f"VALUES ("
               f"{dialogobj.line_number}, "
               f"'{dialogobj.clean_timestamp}', "
               f"'{dialogobj.speaker_name}', "
               f"'{dialogobj.output_filename}', "
               f"{dialogobj.file_id}) "
               )
        print(sql)
        self.cursor.execute(sql)
        self.connection.commit()