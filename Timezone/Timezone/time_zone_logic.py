# The basic logic functions involved in returning Time Zone data for the Time Zone problem.

import arrow
from tzwhere import tzwhere
from datetime import datetime, date, time

class TimezoneFuncs(object):
    def __init__(self):
        self.server_lat = 45.589
        self.server_lng = -122.59
        # Example format: 2016-08-25T17:27:45.556703+00:00
        self.tz = tzwhere.tzwhere()
        self.timeformat = 'YYYY-MM-DDTHH:mm:ss.SSSSSSZZ'
        self.server_tz = self.tz.tzNameAt(self.server_lat, self.server_lng)

    def get_time_at_server(self):
        """
        takes a lat / lng.  Returns a time.
        #>>> TimezoneFuncs().get_time_at_server()
        #'2017-04-12T14:09:48.594734-07:00'
        
        
        """
        loc_time = arrow.get(datetime.now(), self.server_tz).format(self.timeformat)
        return loc_time

    def get_time_at_lat_lng(self, lat, lng):
        """
        There are not good doctest options for 
        :param lat: 
        :param lng: 
        :return: 
        """
        loc_tz = self.get_tz_lat_lng(lat, lng)
        server_time = arrow.get(datetime.now(), self.server_tz)
        loc_time = server_time.to(loc_tz)
        return loc_time

    def get_tz_lat_lng(self, latitude, longitude):
    # takes a latitude and longitude.  Returns the timezone at that location.
        return self.tz.tzNameAt(latitude, longitude)

    def get_time_at_time_lat_lng(self, time_in, lat, lng):
    # takes a time, latitude, and longitude.  Changes the timezone to the target latitude
    # and longitude's timezone.
        target_tz = self.get_tz_lat_lng(lat, lng)
        targ_time = arrow.get(time_in).to(target_tz).format(self.timeformat)
        return targ_time

def main():
    tz_instance = TimezoneFuncs();
    servertime = tz_instance.get_time_at_server();
    print(servertime)
    # '2017-04-12T14:09:48.594734-07:00'
    othertime = tz_instance.get_time_at_lat_lng(25, 0);
    print(othertime)
    movedothertime = tz_instance.get_time_at_time_lat_lng(othertime, 45.58, -122.59)
    print(movedothertime)
    return

if __name__ == '__main__':
    main()

