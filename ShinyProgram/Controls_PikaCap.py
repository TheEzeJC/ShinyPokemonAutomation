import win32gui
import keyboard
import time

# Get handle to the Citra emulator window
emu_window = win32gui.FindWindow(None, "Azahar 2126.0 | Pokémon Ultra Sun")

# Set Citra emulator window as the foreground window
win32gui.SetForegroundWindow(emu_window)

# Wait for the window to become the foreground window
while True:
    if win32gui.GetForegroundWindow() == emu_window:
        break

# Skips over text
def skipFluff():
    print()
    print("Skipping Fluff")

    # Skip Menu Cutscene
    keyboard.press('a')
    time.sleep(.15)
    keyboard.release('a')
    time.sleep(3)

    # Skip Menu
    keyboard.press('a')
    time.sleep(.15)
    keyboard.release('a')
    time.sleep(4.5)

    # Message 1
    # print("M1")
    keyboard.press('a')
    time.sleep(.15)
    keyboard.release('a')
    time.sleep(1.5)
    # Message 2
    #print("M2")
    keyboard.press('a')
    time.sleep(.15)
    keyboard.release('a')
    time.sleep(1)
    # Accept Gift
    # print("M3")
    keyboard.press('a')
    time.sleep(.15)
    keyboard.release('a')
    time.sleep(5)
    # Finsish Accept Gift
    # print("M4")
    keyboard.press('a')
    time.sleep(.15)
    keyboard.release('a')
    time.sleep(2)
    # Message 5
    # print("M5")
    keyboard.press('a')
    time.sleep(.15)
    keyboard.release('a')
    time.sleep(3.5)

    print("Finished Dialog")


    # Open the viewable menu to check if the Pokemon is shiny or not.
    # Open menu
    print("Opening Menu")
    #print("B1")
    keyboard.press('z')
    time.sleep(.15)
    keyboard.release('z')
    time.sleep(1)
    # Select Pokemon Menu
    # Assumes first in list
    # print("B2")
    keyboard.press('a')
    time.sleep(.15)
    keyboard.release('a')
    time.sleep(3)
    # Select first Pokemon in list to open menu
    print("B3")
    keyboard.press('a')
    time.sleep(.15)
    keyboard.release('a')
    time.sleep(1)
    # open Summary menu/load 3D model of Pokemon
    # print("B4")
    keyboard.press('a')
    time.sleep(.15)
    keyboard.release('a')
    time.sleep(3)
    # Scroll to latest pokemon in the list by going up
    # print("B5")
    keyboard.press('up')
    time.sleep(.15)
    keyboard.release('up')
    time.sleep(1)
    print("Finished Opening Menu")

    # Delay to collect correct color
    print("Waiting to collect color")
    time.sleep(3)

    return True

def reset():
    # Press Buttons
    print("Resetting Game")
    keyboard.press('q')  # Left Trigger
    keyboard.press('w')  # Right Trigger
    keyboard.press('m')  # Start Button
    time.sleep(.5)
    # Release Buttons
    keyboard.release('q')  # Left Trigger
    keyboard.release('w')  # Right Trigger
    keyboard.release('m')  # Start Button
    time.sleep(7)  # let the game load
    return True