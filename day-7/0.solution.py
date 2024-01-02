import datetime
import time

# formats
# %Y: Year with century as a decimal number.
# %m: Month as a decimal number [01,12].
# %d: Day of the month as a decimal number [01,31].
# %H: Hour (24-hour clock) as a decimal number [00,23].
# %M: Minute as a decimal number [00,59].
# %S: Second as a decimal number [00,59].
# %b: Abbreviated month name.
# %B: Full month name.


# solution 1
while True:
    now = datetime.datetime.now()
    print(now.strftime("%H:%M:%S"))
    print(now.strftime("%d %B %Y"))
    time.sleep(1)
