from collections import defaultdict

passengers_per_station = defaultdict(int)

# Example: Adding passengers to stations
passengers_per_station['Station1'] += 10 
passengers_per_station['Station2'] += 5   
passengers_per_station['Station1'] += 3  

# Output the number of passengers at each station
for station, count in passengers_per_station.items():
    print(f"{station}: {count} passengers")