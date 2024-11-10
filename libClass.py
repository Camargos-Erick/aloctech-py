from tkcalendar import*
import sqlite3
class CRUD:
    t= "gotcha"
    a = None
    matriz= []
    con = sqlite3.connect("data_base.db")
    curl= con.cursor()

    def create(scriptSQL):  
        CRUD.curl.execute(scriptSQL)
        CRUD.con.commit()
    
    def read(scriptSQL):
        CRUD.curl.execute(scriptSQL)
    
    def update(scripSQL):
        CRUD.curl.execute(scripSQL)
        CRUD.con.commit()
   
    def delete(scriptSQL):       
        CRUD.curl.execute(scriptSQL)
        CRUD.con.commit()
