import time
from datetime import date

print("Seconds since January 1, 1970: ", end="")
print(f"{time.time():,.4f} ", end="")
print("or ", end="")
print(f"{time.time():.2e} ", end="")
print("in scientific notation")
print(date.today().strftime("%b %d %Y"))
