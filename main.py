from fastapi import FastAPI
import logging
from logstash_async.handler import AsynchronousLogstashHandler
from logstash_async.handler import LogstashFormatter

# Create the logger and set it's logging level
logger = logging.getLogger("logstash")
logger.setLevel(logging.INFO)        

# Create the handler
handler = AsynchronousLogstashHandler(
    host='fbfa8f76-19ca-46bc-97c8-9df2d9d30276-ls.logit.io', 
    port=19404, 
    database_path='')
# Here you can specify additional formatting on your log record/message
formatter = LogstashFormatter()
handler.setFormatter(formatter)

# Assign handler to the logger
logger.addHandler(handler)

app = FastAPI()

@app.get("/")
def root(message: str):
    logger.info(message)
    return {"message": message}