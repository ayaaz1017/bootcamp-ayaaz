class TransportNetwork:
    def __init__(self):
        self.routes = []
        self.schedules = {} 
        self.passengers = defaultdict(list) 

    def add_route(self, route):
        self.routes.append(route)

    def update_schedule(self, route, schedule):
        self.schedules[route] = schedule

    def add_passenger(self, station, passenger):
        self.passengers[station].append(passenger)

    def total_unique_stations(self):
        stations = set()
        for schedule in self.schedules.values():
            for stop in schedule:
                stations.add(stop.station)
        return len(stations)

    def most_frequented_station(self):
        station_counts = Counter()
        for passengers in self.passengers.values():
            station_counts.update(passengers)
        return station_counts.most_common(1)[0]

    def sort_routes_by_stops(self):
        return sorted(self.routes, key=lambda x: len(self.schedules.get(x, [])))

    def merge_network(self, other_network):
        self.routes.extend(other_network.routes)
        for route, schedule in other_network.schedules.items():
            self.schedules[route] = schedule
        for station, passengers in other_network.passengers.items():
            self.passengers[station].extend(passengers)
            
            