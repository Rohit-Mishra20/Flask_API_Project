import mysql.connector as my_con
import json

class matrics_model_class():
    
    def __init__(self):
        try:
            self.db_con=my_con.connect(host="localhost",user='root',password='',database='interview_project_db')
            self.db_con.autocommit=True
            self.cur=self.db_con.cursor(dictionary=True)
            print("DB Connection Successful")
        except Exception as e:
            print("Error while connecting to DB",e)
    def get_matrics_data_model(self,data):
        start=data.get('start')
        end=data.get('end')
        #print("start :",start,"end: ",end)
        if start != None and end != None:
            query=f"SELECT * FROM matrics_info_table where Time BETWEEN '{start}' and '{end}'"
            self.cur.execute(query)
            result=self.cur.fetchall()
        else:
            query=f"SELECT * FROM matrics_info_table"
            self.cur.execute(query)
            result=self.cur.fetchall()

        if len(result)>0:
            return json.dumps(result, default=str)
        else:
            return json.dumps([{"error": "Data is not present"}])

    def post_matrics_data_model(self,data):
        #self.cur.execute(f"insert into users(Time,ID_1,ID_2) values({},{},{})")
        pass

