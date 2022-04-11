import logging
from main import main

logging.basicConfig(filename='file.log', format='%(asctime)s %(levelname)-8s %(message)s', level=logging.INFO,datefmt='%Y-%m-%d %H:%M:%S',force=True)
logging.info("starting the programme...")

if __name__ == "__main__":
    main()
