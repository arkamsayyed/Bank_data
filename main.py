#!/usr/bin/python3

"""
this python code for data who took different different

loan from same bank...

"""
import Source_file_location
import logging
import DB_file

flag = True

logging.basicConfig(filename="Server.log",level=10,filemode='w',
                          format='%(asctime)s : %(levelname)s : %(name)s : %(message)s')
log = logging.getLogger(str(__file__).split('/')[-1])

#calling Source file location module
log.info("Calling  sourcce data location file")
source = Source_file_location.get_data()

# Calling DB_file module and passing list
log.info("calling DB ffile with source file list")
DB_file.db_connection(source)

while flag:
    #calling user input method
    log.info("Calling user input method")
    DB_file.user_input()
    while flag:
        choice = input(str("Do you want to continue Y/N = "))
        if choice == 'Y' or choice == 'y':
            break

        elif choice == 'N' or choice == 'n':
            flag = False




