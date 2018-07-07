from dal.JobDal import JobDal
from util.AppUtil import AppUtil
from .HttpService import HttpService
import time


class JobService:

    def __init__(self):
        self.jobDal = JobDal()

    def handle_job(self, file_params):
        file_path = AppUtil.create_file(file_params["file_stream"], file_params["file_name"])

        payload = {
            "file_path" : file_path
        }

        # This sleep is just to simulate a call
        time.sleep(60)

        # Post result to firebase
        # HttpService.send_request("<end_point_path", http_method='PUT', params="params", payload=payload)
