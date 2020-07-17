i=10
j=0

print("Starting")

try:
    print(i/j)
except:
    print("Exception handle")
    raise
finally:
    print("Closing Connection")

print("Ending...")