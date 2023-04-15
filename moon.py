# https://www.der-mond.de/
import ephem
import math
import datetime

# Get the current date
current_date = datetime.datetime.utcnow()

# Create observer at Osnabrück, Germany
observer = ephem.Observer()
observer.lat = '52.2799'
observer.lon = '8.0472'
observer.date = current_date

# Get the Moon and Sun objects
moon = ephem.Moon(observer)
sun = ephem.Sun(observer)

# Calculate the angle between the moon and the sun
moon_angle = math.degrees(ephem.separation(moon, sun))

# Calculate the moon's age and phase

next_new_moon = ephem.next_new_moon(current_date)
previous_new_moon = ephem.previous_new_moon(current_date)
moon_age = (current_date - previous_new_moon.datetime()).days + (current_date - previous_new_moon.datetime()).seconds / 86400
moon_phase = moon_age / 29.53058867  # Normalize the age to a value between 0 and 1

# Calculate the phase angle and the illumination percentage
phase_angle = math.degrees(ephem.separation(moon, sun))
illumination_percentage = 100-(1+ math.cos(math.radians(phase_angle))) / 2 * 100

# Determine the phase name
if moon_phase < 0.125:
    phase_name = "New Moon"
elif moon_phase < 0.25:
    phase_name = "Waxing Crescent"
elif moon_phase < 0.375:
    phase_name = "First Quarter"
elif moon_phase < 0.5:
    phase_name = "Waxing Gibbous"
elif moon_phase < 0.625:
    phase_name = "Full Moon"
elif moon_phase < 0.75:
    phase_name = "Waning Gibbous"
elif moon_phase < 0.875:
    phase_name = "Last Quarter"
else:
    phase_name = "Waning Crescent"

print(f"Moon's age: {moon_age:.2f} days")
print("Moon's phase:", moon_phase)
print("Phase name:", phase_name)
print(f"Illuminance: {illumination_percentage:.2f}% of the lunar surface illuminated")
