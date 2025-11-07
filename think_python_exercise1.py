# Calculate seconds in 42 minutes 42 seconds
seconds = 42 * 60 + 42
print("1) Total seconds:", seconds)

# Convert 10 kilometers to miles (1 mile = 1.61 km)
miles = 10 / 1.61
print("2) Miles in 10 kilometers:", miles)

# Average pace per mile
pace_seconds_per_mile = seconds / miles
pace_minutes = int(pace_seconds_per_mile // 60)
pace_seconds = pace_seconds_per_mile % 60

print(f"3a) Average pace: {pace_minutes} minutes {pace_seconds:.2f} seconds per mile")

# Average speed in miles per hour
hours = seconds / 3600
speed_mph = miles / hours

print(f"3b) Average speed: {speed_mph:.2f} miles per hour")