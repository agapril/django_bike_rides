import gpxpy.gpx
import pandas as pd
def handle_uploaded_file(f):
    with open('static/upload/'+f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def read_gpx(f):

    with open('static/upload/'+f.name, 'r') as gpx_input:
        gpx_data = gpxpy.parse(gpx_input)
        start_time = gpx_data.time
        total_time = gpx_data.get_duration()
        # max_speed = gpx_data.get_moving_data(raw=True).max_speed * 1.35
        max_speed = gpx_data.get_moving_data(raw=True).max_speed * 3.6
        distance = gpx_data.length_3d()/1000
        moving_time = gpx_data.get_moving_data(raw=True).moving_time
    return start_time, total_time, max_speed, distance, moving_time

