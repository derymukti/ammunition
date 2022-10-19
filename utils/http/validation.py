from functools import wraps
from utils.http import response
from utils.constants import HTTP_RESPONSE

def validation_response(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        res = fn(*args, **kwargs)
        err_json = res.get_json()

        # check if pydantic throws an error (if not continue normally)
        if (err_json is None) or ("validation_error" not in err_json):
            return res
        val_err = err_json["validation_error"]
        
        # here you implement the logic to change the msg format
        if "body_params" in val_err:
            final_msg = []
            for sing_err in val_err["body_params"]:
                final_msg.append(" ".join([sing_err["loc"][0], sing_err["msg"]]))

            final_msg = ". ".join(final_msg)

        # this is the final response format
        return response.error_response(data=val_err['path_params'],http_status=HTTP_RESPONSE.FAILED)
 
    return wrapper