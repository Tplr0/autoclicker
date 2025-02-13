from pynput.mouse import Controller, Button
import time

mouse = Controller()
one = time.time_ns()
print("Python Auto Clicker")
print("-------------------")
x = int(input("Enter how many seconds the auto clicker will work for:"))
print("Auto Clicker will start in 3 seconds. Move your mouse to the desired click location.")
time.sleep(3)

for z in range(x):
    for i in range(1000):
        mouse.click(Button.left)

# print(two-one) - for debugging uncomment this if it's not running properly
#
