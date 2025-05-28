# На първия ред - средната скорост на движение - реално число в интервала [1000.00... 30000.00]
# • На втория ред - литри гориво нужни за 100 км - реално число в интервала [1.00...20.00]
import math
average_speed = float(input())
liters_needed_for_100km = float(input())
distance_lune_earth = 384400

total_distance = distance_lune_earth * 2 # отиване и връщане
total_time_go_and_back = total_distance / average_speed

total_time = total_time_go_and_back + 3
gas = (liters_needed_for_100km * total_distance) / 100

print(f"(math.ceil{total_time})")
print(int(gas))

# da se otpecata:
# Броят на часовете, за които Георги е отишъл и се е върнал (резултатът да се закръгли до по-голямото цяло число).
# • Количеството литри гориво, което е нужно за пътуването.