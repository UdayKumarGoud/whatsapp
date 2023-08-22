import logging
from rest_framework.views import exception_handler
from rest_framework.exceptions import Throttled

# class CustomThrottleException(Throttled):
#     def __init__(self, wait=None):
#         self.wait = wait or 0

#         detail = f"Request was throttled. Try again in {self.wait} seconds."
#         super().__init__(detail, wait)

def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)
    
    if isinstance(exc, Throttled): # check that a Throttled exception is raised
        wait_time_seconds = exc.wait
        wait_time_minutes = wait_time_seconds // 60  # integer division to get the number of minutes
        wait_time_seconds_remainder = wait_time_seconds % 60  # get the remaining seconds
        wait_time_formatted = f"{wait_time_minutes}:{wait_time_seconds_remainder:02d}"  # format the wait time as a string with leading zero
        custom_response_data = { # prepare custom response data
            'status': False,
            'status_code': 429,
            'code': 0,
            'message': 'Maximum attempts reached. please try after %s seconds'%(wait_time_formatted)
            # 'availableIn': '%d seconds'%exc.wait
        }
        logging.info('Too many request attempt by user:  %s', custom_response_data)
        response.data = custom_response_data # set the custom response data on response object
        response.status_code = 200
    return response