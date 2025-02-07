
# sort these months according to the calendar

months = ['dec', 'aug','oct', 'nov', 'jun', 'jan', 'sep', 'feb', 'apr', 'may', 'jul', 'mar']

print(f"unsorted months :{months}")

print("-" * 60)
from calendar import month_abbr

print(list(month_abbr))

sort_months = sorted(months, key=list(map(lambda x: x.lower(), list(month_abbr))).index)

print("-" * 60)
print(f"sorted months :{sort_months}")








