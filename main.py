from fastapi import FastAPI
from api import api_router
import logging

logging.config.fileConfig('logging.conf', disable_existing_loggers=False,defaults={'logfilename': '/Users/mithunkarthickvenkatesan/Desktop/CS101/Mini_Project/Backend/logging.log'})
logger = logging.getLogger(__name__)

app=FastAPI()

app.include_router(api_router)
