bus_routes = ['Route1', 'Route2', 'Route3']
routes_with_stops = {'Route1': 5, 'Route2': 3, 'Route3': 7}
sorted_routes = sorted(bus_routes, key=lambda x: routes_with_stops[x])