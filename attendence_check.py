import sqlite3

#display a_batch and b_batch students list

def connect_DB(db_file):
    conn=sqlite3.connect(db_file)
    cur=conn.cursor()
 
    #display participants list 
    
    
#creating table of participants
def table_creation(db_file,list_1):
    conn=sqlite3.connect(db_file)         
    cur=conn.cursor()
    #given txt file to list
    file_data = [i.strip('\n').split(',') for i in open(list_1)]
    new_data = [[str(a), *b] for a, *b in file_data] 
    new_att=[]
    for i in new_data:
        for j in i:
                 new_att.append(j)
                 

    #print(new_att)
    cur.execute("DROP TABLE Meet_list")
    cur.execute("CREATE TABLE Meet_list (stu_name text)")
    query= "INSERT INTO Meet_list(stu_name) VALUES(?);"
    for row in new_att:
        cur.execute(query, [row])
    conn.commit()
    
    cur.execute("SELECT stu_name FROM Meet_list")
   
   
def main():
    db_file=input("enter the name of DB\n")
    list_1=input("enter the participants list\n")
    conn=sqlite3.connect(db_file)         
    cur=conn.cursor()
    connect_DB(db_file)
    participants_list(list_1)
    table_creation(db_file,list_1) 
    print("a_batch absent")
    cur.execute("SELECT name FROM a_batch EXCEPT SELECT stu_name FROM Meet_list ")
    rows=cur.fetchall()
    for row in rows:
        print(row)
    print("\n")
    
    print("b_batch absent")
    cur.execute("SELECT name FROM b_batch EXCEPT SELECT stu_name FROM Meet_list ")
    rows=cur.fetchall()
    for row in rows:
        print(row)
    print("\n")
    
    print("external participants")
    cur.execute(" SELECT stu_name FROM Meet_list EXCEPT SELECT name FROM (SELECT name FROM a_batch UNION SELECT name FROM b_batch)")
    rows=cur.fetchall()
    for row in rows:
        print(row)
        
        
if __name__ == '__main__':
    
    main()
