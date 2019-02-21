def selectquery(table_name):
    cursor, conn = getConn()

    query="select * from "+table_name
    cursor.execute(query)
    all_records=[]
    for row in cursor:
        all_records.append(row)

    closeConn(cursor, conn)

    return all_records


def select_where_query(table_name,name):

    cursor,conn = getConn()

    query="select * from "+table_name +" where masjid_name = '"+name+"'"
    cursor.execute(query)
    all_records=[]
    for row in cursor:
        all_records.append(row)

    closeConn(cursor, conn)

    print(all_records)
    return all_records

def insertQuery(table_name,columns,values):

    cursor, conn = getConn()
    # query = INSERT INTO masjid.customer (name,email,password,reg_id,latitute,langitute) VALUES("Masjid1","name1@name1.com","name1","name1reg","21",'-21');
    query = "INSERT INTO " + table_name + " "+columns+" VALUES" + values + ";"
    # print(query)
    try:
        cursor.execute(query)
        conn.commit()
        print(cursor.rowcount, "record inserted.")
        return cursor.rowcount
    except Exception as e:
        print('in expect')
        print(e)
        return e
    finally:
        closeConn(cursor, conn)


def getConn():
    import mysql.connector
    conn = mysql.connector.connect(user='root', password='root',
                                   host='127.0.0.1',
                                   database='datad_demo')

    return conn.cursor(),conn

def closeConn(cursor,conn):
    cursor.close()
    conn.close()

# if __name__ == "__main__":
#     values = "'Masjid3', 'name1@name1.com', 'name1','name1reg','21','-21'"
#     insertQuery("customer", "(name,email,password,reg_id,latitute,langitute)", values )