states_needed = {'mt', 'wa', 'or', 'id', 'nv', 'ut', 'ca', 'az'}

stations = dict()
stations['kone'] = {'id', 'nv', 'ut'}
stations['ktwo'] = {'wa', 'id', 'mt'}
stations['kthree'] = {'or', 'nv', 'ca'}
stations['kfour'] = {'nv', 'ut'}
stations['kfive'] = {'ca', 'az'}

final_stations = set()


def my_greedy_algo(states_set, stations_dict):
    while states_set:
        n_top = 0
        for station, states in stations_dict.items():
            if len(states & states_set) > n_top:
                top = station
                n_top = len(states & states_set)
        states_set -= stations_dict[top]
        final_stations.add(top)
    return final_stations


def book_greedy_algo(states_set, stations_dict):
    while states_set:
        states_set, stations_dict = states_needed, stations
        best_station = None
        states_covered = set()
        for station, states in stations_dict.items():
            covered = states_set & states
            if len(covered) > len(states_covered):
                best_station = station
                states_covered = covered
        states_set -= states_covered
        final_stations.add(best_station)
    return final_stations


#print(my_greedy_algo(states_needed, stations))
print(book_greedy_algo(states_needed, stations))
