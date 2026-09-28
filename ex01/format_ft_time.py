import time

print(f"Seconds since January 1, 1970: ", end="")
print(f"{time.time():,.4f} ", end="")
print(f"or ", end="")
print(f"{time.time():.2e} ", end="")


