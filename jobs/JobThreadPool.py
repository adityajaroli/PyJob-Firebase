from concurrent.futures import ThreadPoolExecutor


class JobThreadPool:

    executor = ThreadPoolExecutor(5)

    @staticmethod
    def get_executor():
        return JobThreadPool.executor
