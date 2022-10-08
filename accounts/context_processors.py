import datetime

def get_time(request):
    time_now = datetime.datetime.now()
    return {'time': time_now}

