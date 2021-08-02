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
        self.cursor.close()
        self.connection.close()

    def save_cxdata(self):
        sql = 'SELECT * FROM dialog'
        self.cursor.execute(sql)
        entries = [{'file_id': file_id,
                    'line_number': line_number,
                    'line_txt': line_text,
                    'clean_nlnum': clean_nlnum,
                    'clean_timestamp': clean_timestamp,
                    'speaker_name': speaker_name
                    } for (file_id, line_number, line_text, clean_nlnum, clean_timestamp, speaker_name) in self.cursor]
