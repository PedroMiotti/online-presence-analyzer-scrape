def response(status, message, object_name=False, body=False):
    res = {}
    res["status"] = status
    res["message"] = message

    if object_name and body:
        res[object_name] = body

    return res
