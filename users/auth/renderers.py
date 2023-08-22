from rest_framework import renderers,status
import json


class Renderer(renderers.JSONRenderer):
    charset = 'utf-8'

    def render(self, data, accepted_media_type=None, renderer_context=None):
        response = ''
        if 'ErrorDetail' in str(data):
            response = json.dumps({
                'code': 1,
                'errors': data,
                'message': "please retry again...",
                'success': "fail",
                'status': status.HTTP_400_BAD_REQUEST
            })
        else:
            response = json.dumps({
                'code': 0,
                'data': data,
                'message': "Successfully fetched the data",
                'success': "success",
                'status': status.HTTP_200_OK
            })
        return response


