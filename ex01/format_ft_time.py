import time
from datetime import date

print(f"Seconds since January 1, 1970: ", end="")
print(f"{time.time():,.4f} ", end="")
print(f"or ", end="")
print(f"{time.time():.2e} ", end="")
print(f"in scientific notation")
print(date.today().strftime("%b %d %Y"))


