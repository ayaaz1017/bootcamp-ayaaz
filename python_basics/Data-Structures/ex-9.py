all_stations = set()
for stations in train_lines.values():
    all_stations.update(stations)
all_stations.update(['Station1', 'Station2', 'Station3', 'Station4', 'Station5'])
total_unique_stations = len(all_stations)