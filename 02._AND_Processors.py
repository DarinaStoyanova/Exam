# Първи ред – броят процесори, които трябва да се изработят – цяло число в интервала [1...500 000]
# • Втори ред – броят служители – цяло число в интервала [1...1000]
# • Трети ред – работните дни – цяло число в интервала [1...1000]
import math
processor_count = int(input())
employee_count = int(input())
working_days = int(input())

time_for_one_processor = 3
working_time_per_employee_per_day = 8

total_time = employee_count * working_days * working_time_per_employee_per_day
total_processors_made = math.floor(total_time / 3)

if total_processors_made >= processor_count:
    difference = total_processors_made - processor_count
    gain = difference * 110.10
    print(f"Profit: -> {gain:.2f} BGN")

if total_processors_made < processor_count:
    difference = processor_count - total_processors_made
    lose = difference * 110.10
    print(f"Losses: -> {lose:.2f} BGN")
