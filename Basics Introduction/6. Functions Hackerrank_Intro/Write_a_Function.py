# A Python Function to Print whether a 
# Year is Leap Year or Not. 
def is_leap(year):
    leap = False
    # Leap Year Logic
    if year%4 == 0:
        leap = True
        if year%100 == 0:
            if year%400 == 0:
                leap = True
            else:
                leap = False
    else:
        leap = False
    return leap

year = int(input())
print(is_leap(year))