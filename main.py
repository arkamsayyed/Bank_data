#!/usr/bin/python3

"""
this python code for data who took different different

loan from same bank...

"""
import Source_file_location
import DB_file
import logging


logging.basicConfig(filename="Server.log",level=10,filemode='w',
                          format='%(asctime)s : %(levelname)s : %(name)s : %(message)s')
log = logging.getLogger(str(__file__).split('/')[-1])

log.info("Calling  sourcce data location file")
source = Source_file_location.get_data()
log.info("calling DB ffile with source file list")
DB_file.db_connection(source)

