from persiantools.jdatetime import JalaliDate, JalaliDateTime
import time

# install persiantools: pip install persiantools

# formats
# %Y: Year as a decimal number (e.g., 1401)
# %m: Month as a zero-padded decimal number (e.g., 01 for Farvardin)
# %d: Day of the month as a zero-padded decimal number (e.g., 01)
# %b: Abbreviated month name (e.g., Far)
# %B: Full month name (e.g., Farvardin)
# %a: Abbreviated weekday name (e.g., Shan)
# %A: Full weekday name (e.g., Shani)

# solution 1
while True:
    now = JalaliDateTime.now()
    print(now.strftime("%H:%M:%S"))
    print(JalaliDate(now).strftime("%d %B %Y"))
    time.sleep(1)
