
# Вашата задача е да им помогнете като напишете програма, която да приема броя на локациите и очакван среден добив на злато за ден за една локация.
# За всеки ден ще получавате колко злато са добили на локацията. Проверете дали са постигнали очаквания добив за дадена локация или не.
#
# За всяка една локация се четат две числа, по едно на ред:
# 1. На първия ред – очакван среден добив на ден злато – реално число в интервала [0.00.. 10000.00]
# 2. На втория ред – брой дни, в който ще се копае на дадената локация – цяло число в интервала [1.. 30]
# За всеки ден се чете по едно число:
#  Добито злато за деня – реално число в интервала [0.00.. 1000.00]
location_count = int(input())
produced_gold = 0

for location in range (1, location_count +1):
    expected_average_production = float(input())
    days_count = int(input())
    current_days_count = days_count
    while True:
        if current_days_count == 0:
            break
        current_days_count -= 1
        gold_production_per_day = float(input())
        produced_gold += gold_production_per_day
    average_gold_production = produced_gold / days_count
    if average_gold_production >= expected_average_production:
        print(f"Good job! Average gold per day: {average_gold_production:.2f}.")
    elif average_gold_production < expected_average_production:
        gold_needed = expected_average_production - average_gold_production
        print(f"You need {gold_needed:.2f} gold.")
    produced_gold = 0



# След приключване на копаенето на дадена локация се печата един ред според случая:
#  Ако средният добив злато за ден достига или надвишава очаквания среден добив на ден злато: o "Good job! Average gold per day: {среден добив на ден за дадената локация}."
#  Ако средният добив злато за ден е под очаквания среден добив на ден злато:
# o "You need {злато, което не е достигнало за достигане на очакваният среден добив} gold."
# Резултатът да бъде форматиран до вторият знак след десетичният разделител.


