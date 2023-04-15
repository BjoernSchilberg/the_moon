import datetime
import ephem
import pytz

def get_astronomical_twilight(observer):
    sun = ephem.Sun()
    observer.date = datetime.datetime.utcnow()
    observer.horizon = '-18'  # Set horizon to -18 degrees for astronomical twilight
    
    astronomical_twilight_evening = observer.next_setting(sun, use_center=True).datetime()
    astronomical_twilight_morning = observer.next_rising(sun, use_center=True).datetime()
    
    return astronomical_twilight_evening, astronomical_twilight_morning

def convert_to_berlin_time(utc_time):
    berlin_tz = pytz.timezone('Europe/Berlin')
    return utc_time.replace(tzinfo=pytz.utc).astimezone(berlin_tz)

if __name__ == "__main__":
    # Set the location to Osnabrueck (latitude, longitude, and elevation)
    observer = ephem.Observer()
    observer.lat, observer.lon, observer.elevation = '52.2799', '8.0472', 62.0

    # Get astronomical twilight start and end times
    astronomical_twilight_evening_utc, astronomical_twilight_morning_utc = get_astronomical_twilight(observer)

    # Convert UTC times to Berlin timezone
    astronomical_twilight_evening = convert_to_berlin_time(astronomical_twilight_evening_utc)
    astronomical_twilight_morning = convert_to_berlin_time(astronomical_twilight_morning_utc)

    print("Astronomical twilight starts in the evening at (Berlin Time):", astronomical_twilight_evening)
    print("Astronomical twilight ends in the morning at (Berlin Time):", astronomical_twilight_morning)
