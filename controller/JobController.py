from flask import request, make_response
from jobs.JobThreadPool import JobThreadPool
from service.JobService import JobService

jobService = JobService()


def post_job():
    config_request = request.get_json()

    if config_request is None or len(config_request) != 4:
        return make_response("Incomplete parameters", 403)

    if "file_stream" not in config_request or "file_name" not in config_request or \
            "column_name" not in config_request or "file_id" not in config_request:
            return make_response("No file stream to process", 405)

    JobThreadPool.get_executor().submit(jobService.handle_job, config_request)

    return make_response("Received a request to process a file", 200)
