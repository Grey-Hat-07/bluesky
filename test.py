import bluesky as bs

# Create an aircraft object
aircraft = bs.Aircraft(
    name="A123",
    callsign="ABC123",
    type="Boeing 737",
    latitude=37.7749,
    longitude=-122.4194,
    altitude=30000,
    heading=270,
    speed=250,
)

# Define a simple flight path
flight_path = [
    bs.Waypoint(latitude=37.8042, longitude=-122.4786, altitude=30000),
    bs.Waypoint(latitude=37.7122, longitude=-122.2711, altitude=30000),
    bs.Waypoint(latitude=37.6325, longitude=-122.1919, altitude=30000),
]

# Assign the flight path to the aircraft
aircraft.set_flight_path(flight_path)

# Simulate the aircraft's movement
for _ in range(10):
    aircraft.update_position()
    print(aircraft.get_state())
