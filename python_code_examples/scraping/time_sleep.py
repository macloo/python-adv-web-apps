import time

print("I will write the same line 3 times, slowly.\n")

time.sleep(2)

for n in range(3):
    print("Sleep ... zzz ...")
    time.sleep(5)

print("\nThe End")
