from datetime import datetime

job = {
    "start": "",
    "stop": "",
    "diff": ""
}

def print_anything(anything):
    print(anything)

def get_time_now():
    # Tageszeit, dass auch die Uhrzeit enthält
    now = datetime.now()
    return now

def clear_job():
    for e in job:
        job[e] = ""

def print_time():
    timestamp = get_time_now()
    print(f"Zeit: {timestamp}")

def set_job_time(start_or_stop, time):
    job[start_or_stop] = time

def set_start_time():
    clear_job()
    timestamp = get_time_now()
    set_job_time("start", timestamp)

def set_time_diff():
    diff = job["stop"] - job["start"]
    job["diff"] = diff
    # seconds_in_day = 60 * 60 * 24
    print_anything(job)
    print(diff.total_seconds())
    # print(60*60*24)
    # print(divmod(diff.days * seconds_in_day + diff.seconds, 60))

def set_stop_time():
    timestamp = get_time_now()
    set_job_time("stop", timestamp)
    


