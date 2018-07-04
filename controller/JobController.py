from flask import request, make_response
from jobs.JobThreadPool import JobThreadPool
from dal.JobDal import JobDal

jobDal = JobDal()


def handle_job(file_stream, constant_x, constant_y):
    # Do the required work here and receive the result
    # Post result to firebase
    object_to_insert = {"job_name": "dummy_job", "job_status": "Success"}
    JobDal.insert(object_to_insert)


# The request should come with three arguments
# { file_stream: fileStream, constant_x: x, constant_y: y
def post_job():
    config_request = request.get_json()

    if config_request is None or len(config_request) != 3:
        return make_response("Incomplete parameters", 403)

    if "file_stream" not in config_request:
        return make_response("No file stream to process", 403)

    if "constant_x" not in config_request:
        return make_response("Need constant_x", 403)

    if "constant_y" not in config_request:
        return make_response("Need constant_y", 403)

    JobThreadPool.get_executor().submit(handle_job,
                                 config_request["file_stream"],
                                 config_request["constant_x"],
                                 config_request["constant_y"])

    return make_response("Received a request to process a file", 200)
