# The basic logic functions involved in returning Time Zone data for the Time Zone problem.

import arrow
from tzwhere import tzwhere
from datetime import datetime, date, time

class TimezoneFuncs(object):
    def __init__(self):
        self.server_lat = 45.589
        self.server_lng = -122.59
        # Example format: 2016-08-25T17:27:45.556703+00:00
        self.timeformat = 'YYYY-MM-DDTHH:mm:ss'
    def get_time_at_server(self):
        """
        takes a lat / lng.  Returns a time.
        >>> TimezoneFuncs().get_time_at_server()
        Blue
        
        
        """

        tz = tzwhere.tzwhere()
        mytz = tz.tzNameAt(self.server_lat, self.server_lng)
        loc_time = arrow.get(datetime.now(), mytz).st
        return loc_time

    def get_time_at_lat_lng(self, lat, lng):
        return 0

    def get_tz_lat_lng(self, latitude, longitude):
    # takes a latitude and longitude.  Returns the timezone at that location.
        return tzwhere.tzNameAt(latitude, longitude)

    def get_time_at_time_lat_lng(self, time_in, latitude, longitude):
    # takes a time, latitude, and longitude.  Changes the timezone to the target latitude
    # and longitude's timezone.

        return 0

def main():
    tz_instance = TimezoneFuncs();
    tz_instance.get_time_at_server();
    return

if __name__ == '__main__':
    main()

