class InternetUnreachableError(Exception):
    pass

def internet_reachable():
    import socket
    import requests
    try:
        requests.get("http://google.com", timeout=1)
    except (requests.exceptions.Timeout, requests.exceptions.ConnectionError, socket.timeout):
        return False
    return True

def assert_internet_reachable():
    from bodylabs.util.environ import location_is_ec2

    # ec2 is the internet.
    if location_is_ec2():
        return

    if not internet_reachable():
        raise InternetUnreachableError("Internet Unreachable")
