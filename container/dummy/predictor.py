import os
import io
import logging
import flask
import time
from datetime import datetime
from s3_logs.put_content_to_s3 import put_content_to_s3
from s3_logs.string_io_logger import get_string_io_logger

# Cria um objeto string i/o como string buffer
log_stringio_obj = io.StringIO()
log_handler = logging.StreamHandler(log_stringio_obj)
logger = get_string_io_logger(log_stringio_obj, logger_name="my_s3_logger")

prefix = "/opt/ml/"
model_path = os.path.join(prefix, "model")


def store_logs_s3():
    # Persiste os logs no s3
    timestamp = datetime.fromtimestamp(time.time()).strftime("%Y%m%d%H%M%S")
    s3_log_path = "s3://BUCKET/python_s3_loggger_demo/{0}/".format(timestamp)

    s3_store_response = put_content_to_s3(
        s3_path=s3_log_path + "logs.txt",
        content=log_stringio_obj.getvalue(),
    )
    assert s3_store_response[
        "success"
    ], "Error Putting logs to S3:\n{0}".format(s3_store_response["data"])


app = flask.Flask(__name__)


@app.route("/ping", methods=["GET"])
def ping():
    # Implementar um healthcheck
    logger.info("ping")
    store_logs_s3()
    return flask.Response(
        response="\n", status=200, mimetype="application/json"
    )


@app.route("/invocations", methods=["POST"])
def transformation():
    # Implementar predição
    logger.info("test")
    store_logs_s3()
    return flask.Response(
        response="teste dummy", status=200, mimetype="text/csv"
    )
