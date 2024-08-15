years_to_count = 3
secondS_in_year = 31536000
total_seconds = years_to_count * secondS_in_year
current_population = 380123456
number_of_people_being_born = total_seconds / 6
print(int(number_of_people_being_born))
number_of_people_die = total_seconds / 12
print(int(number_of_people_die))
number_of_people_immgrate = total_seconds / 40
print(int(number_of_people_immgrate))
total_population = current_population + number_of_people_being_born - number_of_people_die + number_of_people_immgrate
print (int(total_population))