from rest_framework.exceptions import (APIException,NotFound,PermissionDenied,
                                        NotAuthenticated)

class TokenExpired(NotAuthenticated):
    status_code = 403
    default_detail = "Access Token Expired"
    default_code = "forbidden"
    

class ClientNotFound(NotAuthenticated):
    status_code = 403
    default_detail = "Client Not Found"
    default_code = "forbidden"