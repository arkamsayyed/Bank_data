"""

this python code for take source file and
merge into list for further operation

"""


import logging
import os

logging.basicConfig(filename="Server.log",level=10,filemode='w',
                          format='%(asctime)s : %(levelname)s : %(name)s : %(message)s')
log = logging.getLogger(str(__file__).split('/')[-1])
def get_data():
        file_list = []
        #take input as a file location from user
        dir_location = str(input("Enter file location path = "))
        log.info("got file location from user")
        #Path set to source loaction
        os.chdir(dir_location)
        log.info(f"Directory path is set to {dir_location}")
        avail_file = os.listdir('.')
        #check wheather file folder empty or not
        log.info("File location check ")
        if len(avail_file)<=0:
            print(f"There is no file available at {dir_location} please enter backup directory location")
            def_dir_location = str(input("Enter default directory location path = "))
            log.info("got default directory location from user")
            os.chdir(def_dir_location)
            log.info(f"Directory path is set to {def_dir_location}")
        else:
            log.info("File location is not empty")
            for file in avail_file:
                if file.endswith('.csv'):
                    file_list.append(file)

        log.info("Retirning file list to database file")
        return file_list


