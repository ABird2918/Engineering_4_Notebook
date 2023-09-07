import time
import board #type: ignore
import digitalio #type: ignore

# for every integer between 10 and 0
# print the countdown
#go down by one every time
for i in range(10,0,-1):
    print(i)
    time.sleep(1)

# when the countdown reaches 0, print liftoff
print("Liftoff!")
