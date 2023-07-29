"""
this is database module in which we are fetching data from

various location and storing into databasse...

"""

import logging
import csv
import mysql.connector
logging.basicConfig(filename="Server.log",level=10,filemode='w',
                          format='%(asctime)s : %(levelname)s : %(name)s : %(message)s')
log = logging.getLogger(str(__file__).split('/')[-1])

log.info("Got file list from source file location")
try:
    # createing database on sql server
    log.info("connecting to database...")
    conn = mysql.connector.connect(host="localhost", user="root", password="12345", port="3307")
    log.info("connection sucessfully done.... ")
    con = conn.cursor()
    con.execute("Create database python_41")
    log.info("Database created")

except mysql.connector.errors.DatabaseError:
    # database already available on server
    log.info("database already created")
    conn = mysql.connector.connect(host="localhost", user="root", password="12345", port="3307", database="python_41")
    log.info("connected to the database.... ")
    con = conn.cursor()

def db_connection(file):

    files = [lst for lst in file if str(lst).endswith('.csv')]
    #checking csv file name and creating table in database
    for i in files:
        if i == 'Customer.csv':
            with open(i) as fp:
                read = csv.reader(fp)
                a = [j[0:] for j in read]
                id = a[0][0]
                name = a[0][1]
                ac_number = a[0][2]
                ph_number = a[0][3]
                balance = a[0][4]
            try:
                con.execute(f"create table customer({id} int primary key,"
                            f"{name} varchar(20),"
                            f"{ac_number} varchar(10),"
                            f"{ph_number} varchar(10),"
                            f"{balance} varchar(10))")
                log.info(f"creating {i} table")

            #Inserting data into created tables
            except mysql.connector.errors.ProgrammingError:
                log.info(f"table {i} already created")
                with open(i) as csv_file:
                    write = csv.reader(csv_file)
                    for row in write:
                        if row[0].isalpha():
                            continue
                        else:
                            try:
                                log.info(f"data insertinng into {i} tables")
                                con.execute(f"""insert into customer values({row[0]},'{row[1]}',{row[2]},{row[3]},{row[4]})""")
                                conn.commit()
                            except mysql.connector.errors.IntegrityError:
                                continue

            # Inserting data into created tables
            else:
                with open(i) as csv_file:
                    write = csv.reader(csv_file)
                    for row in write:
                        if row[0].isalpha():
                            continue
                        else:
                            try:
                                log.info(f"data inserting into {i} tables")
                                con.execute(f"""insert into customer values({row[0]},'{row[1]}',{row[2]},{row[3]},{row[4]})""")
                                conn.commit()
                            except mysql.connector.errors.IntegrityError:
                                continue

        elif i == 'Business_loan.csv':
            # checking csv file name and creating table in database
            with open(i) as fp:
                read = csv.reader(fp)
                a = [j[0:] for j in read]
                business_loan_customer_id = a[0][0]
                business_loan_id = a[0][1]
                business_loan_amt = a[0][2]

            try:
                con.execute(f"create table business_loan_data({business_loan_customer_id} int primary key,"
                            f"{business_loan_id} int,"
                            f"{business_loan_amt} int)")
                log.info(f"table {i} creating in database")

            # Inserting data into created tables
            except mysql.connector.errors.ProgrammingError:
                log.info(f"table {i} already in database")
                with open(i) as csv_file:
                    write = csv.reader(csv_file)
                    for row in write:
                        if row[0].isalpha():
                            continue
                        else:
                            try:
                                log.info(f"inserting data into {i} database")
                                con.execute(f"insert into business_loan_data values({row[0]},'{row[1]}',{row[2]})")
                                conn.commit()
                            except mysql.connector.errors.IntegrityError:
                                continue

            # Inserting data into created tables
            else:
                with open(i) as csv_file:
                    write = csv.reader(csv_file)
                    for row in write:
                        if row[0].isalpha():
                            continue
                        else:
                            try:
                                log.info(f"data inserting in {i} database")
                                con.execute(f"insert into business_loan_data values({row[0]},'{row[1]}',{row[2]})")
                                conn.commit()
                            except mysql.connector.errors.IntegrityError:
                                continue

        elif i == 'Home_loan.csv':
            # checking csv file name and creating table in database
            with open(i) as fp:
                read = csv.reader(fp)
                a = [j[0:] for j in read]
                home_loan_customer_id = a[0][0]
                home_loan_id = a[0][1]
                home_loan_amt = a[0][2]

            try:
                con.execute(f"create table home_loan_data({home_loan_customer_id} int primary key,"
                            f"{home_loan_id} int,"
                            f"{home_loan_amt} int)")
                log.info(f"table {i} creating in database")

            # Inserting data into created tables
            except mysql.connector.errors.ProgrammingError:
                log.info("table {i} already available in database")
                with open(i) as csv_file:
                    write = csv.reader(csv_file)
                    for row in write:
                        if row[0].isalpha():
                            continue
                        else:
                            try:
                                log.info(f"data inserting in {i} table")
                                con.execute(f"insert into home_loan_data values({row[0]},'{row[1]}',{row[2]})")
                                conn.commit()
                            except mysql.connector.errors.IntegrityError:
                                continue

            # Inserting data into created tables
            else:
                with open(i) as csv_file:
                    write = csv.reader(csv_file)
                    for row in write:
                        if row[0].isalpha():
                            continue
                        else:
                            try:
                                log.info(f"data inserting in {i} table")
                                con.execute(f"insert into home_loan_data values({row[0]},'{row[1]}',{row[2]})")
                                conn.commit()
                            except mysql.connector.errors.IntegrityError:
                                continue



def user_input():
    ch = int(input("Enter customer id to be search in database = "))
    log.info("taking user id from requester")
    con.execute(f"""select * from ((customer inner join business_loan_data on customer.id = business_loan_data.id) inner join home_loan_data on customer.id = home_loan_data.id) where customer.id = {ch}""")
    row = con.fetchall()
    for data in row:
        print(data)