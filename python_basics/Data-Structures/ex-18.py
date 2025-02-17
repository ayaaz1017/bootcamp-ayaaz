from collections import Counter
station_visits = ['Station1', 'Station2', 'Station1', 'Station3', 'Station2', 'Station1']
station_counter = Counter(station_visits)
most_frequented_station = station_counter.most_common(1)[0]