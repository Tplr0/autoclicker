import pyautogui
import time
import random
# this program only does one click per .1 sec because of how the system optimises the
# program with pyautogui use pynput instead


# Function to perform auto clicks
def auto_clicker(num_clicks, click_delay):
    try:
        print("Auto Clicker will start in 3 seconds. Move your mouse to the desired click location.")
        time.sleep(3)

        for _ in range(num_clicks):
            x, y = pyautogui.position()  # Get current mouse position
            pyautogui.click(x, y)       # Perform a mouse click
            print(f"Click at ({x}, {y})")
            time.sleep(random.uniform(click_delay - 0.1, click_delay + 0.1))  # To add some randomness to the delay
            # If you do not want to have a click delay you can comment the time.sleep function

        print("Auto Clicker has finished.")
    except KeyboardInterrupt:
        print("Auto Clicker stopped.")


# Main function
def main():
    print("Python Auto Clicker")
    print("-------------------")
    num_clicks = int(input("Enter the number of clicks: "))
    click_delay = float(input("Enter the click delay (in seconds, and more than 0.1): "))
    click_delay2 = click_delay
    auto_clicker(num_clicks, click_delay)


if __name__ == "__main__":
    main()
