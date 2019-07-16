import logging
import datetime
import sys

# python generate_log_script.py univrse-Windows .\Univrse-Core\Windows\

def setup():
    date = datetime.date.today()
    log_file_name = build_directory + str(date) + '_' + build_name + '.log'
    logging.basicConfig(filename=log_file_name,
                        level=logging.DEBUG,
                        format='%(asctime)s:%(levelname)s:%(message)s')

if __name__ == "__main__":
    if len(sys.argv) < 3:
        raise UserWarning("Error: Not enough arguments")

    # Log file name
    build_name = sys.argv[1]

    # Log file directory
    build_directory = sys.argv[2]

    # Log file settings
    setup()

    #Write the log file
    logging.debug(build_name)
    
    #Return success
    print("Build logged!")
