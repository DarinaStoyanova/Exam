pastry = input()
pastry_count = int(input())
day = int(input())

if pastry == "Cake":
    if day <= 15:
        pastry_price_per_count = 24
    elif day > 15:
        pastry_price_per_count = 28.70
elif pastry == "Souffle":
    if day <= 15:
        pastry_price_per_count = 6.66
    elif day > 15:
        pastry_price_per_count = 9.80
elif pastry == "Baklava":
    if day <= 15:
        pastry_price_per_count = 12.60
    elif day > 15:
        pastry_price_per_count = 16.98

total_price_before_disc = pastry_count * pastry_price_per_count
if day <= 22:
    if 100 <= total_price_before_disc <= 200:
        total_price = total_price_before_disc * (1 - 0.15)
        if day <= 15:
            total_price = total_price * (1 - 0.10)
    elif total_price_before_disc > 200:
        total_price = total_price_before_disc * (1 - 0.25)
        if day <= 15:
            total_price = total_price * (1 - 0.10)
else:
    total_price = pastry_count * pastry_price_per_count

print(f"{total_price:.2f}")



