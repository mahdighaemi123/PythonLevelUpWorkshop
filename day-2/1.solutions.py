# solution 1
temp = int(input())

if temp >= 20:
    print ("turn off heater")
else:
    print("turn on heater")

# solution 2
print("turn off heater" if int(input()) >= 20 else "turn on heater")