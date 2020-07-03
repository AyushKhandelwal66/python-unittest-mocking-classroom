import pandas as pd

import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="ayush",
    database="employee",
    )
mycursor=mydb.cursor()

sql='SELECT Salary FROM employee'
mycursor.execute(sql)
res=mycursor.fetchall()

df=pd.read_sql(sql,mydb)
class DbHelper:
    def get_maximum_salary(self):
        '''
        Implement the logic to find and return maximum salary from employee table
        '''
        a=df.nlargest(1,['Salary'])

        return a

    def get_minimum_salary(self):
        '''
        Implement the logic to find and return minimum salary from employee table
        '''
        b=df.nsmallest(1,['Salary'])
        return b

if __name__ == "__main__":
    db_helper = DbHelper()
    min_salary = db_helper.get_minimum_salary()
    max_salary = db_helper.get_maximum_salary()
    print(max_salary)
    print(min_salary)
