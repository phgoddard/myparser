from db.repository import *
import mysql.connector

class MysqlRepository(Repository):

    def __init__(self):
        super().__init__()
        config = {
            'user': 'root',
            'password': 'root',
            'host': 'db', # to run LOCALLY, this should be localhost
            'port': '3306', # to run LOCALLY, this should be 32000
            'database': 'cxdata'
        }
        self.connection = mysql.connector.connect(**config)
        self.cursor = self.connection.cursor()

    def __del__(self):
        self.cursor.close()
        self.connection.close()

    def checkifstudyexists(self, studyname):
        sql = ("SELECT study_id "
            "FROM study "
            f"WHERE studyname = '{studyname}'")
        self.cursor.execute(sql)
        entries = [study_id[0] for study_id in self.cursor]
        return entries

    def create_study(self, studyname):
        sql = ("INSERT INTO study "
        "(studyname) "
        "VALUES ("
        f"'{studyname}')"
        )
        self.cursor.execute(sql)
        last_id = self.cursor.getlastrowid()
        self.connection.commit()
        return [last_id]

    def save_study(self, studyobj):
        sql = ("INSERT INTO study "
         "(studyname,study_id) "
         f"VALUES ("
         f"'{studyobj.studyname}', "
         f"{studyobj.study_id}) "
        )
        #print(sql)
        self.cursor.execute(sql)
        self.connection.commit()

    def save_file(self, fileobj):
        sql = ("INSERT INTO file "
         "(file_name,all_text,study_id) "
         f"VALUES ("
         f"'{fileobj.file_name}', "
         f"'{fileobj.all_text}', "
         f"{fileobj.study_id}) "
         )
        #print(sql)
        self.cursor.execute(sql)
        last_id = self.cursor.getlastrowid()
        self.connection.commit()
        fileobj.file_id = last_id

    def save_dialog(self, dialogobj):
        sql = ("INSERT INTO dialog "
               "(file_id,line_number,speaker_name,clean_timestamp) "
               f"VALUES ")
        print(dialogobj.dialogdata_for_sql)
        for row in range(1,len(dialogobj.dialogdata_for_sql)):
            row_str = ( f"({dialogobj.file_id}, "
                        f"{dialogobj.dialogdata_for_sql[row][0]}, "
                        f"'{dialogobj.dialogdata_for_sql[row][1]}', "
                        f"'{dialogobj.dialogdata_for_sql[row][2]}'), "
                )
            sql += row_str
        sql = sql[:-2]
        #print(sql)
        self.cursor.execute(sql)
        self.connection.commit()