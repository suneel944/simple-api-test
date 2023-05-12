def check_for_status(response):
    """Checks whether or not the response was successful"""
    if 200 <= response.status_code < 300:
        return response
