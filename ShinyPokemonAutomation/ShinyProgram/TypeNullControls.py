import win32gui
import keyboard
import time

# Get handle to the Citra emulator window
citra_window = win32gui.FindWindow(None, "Citra Nightly 1888 | Pokémon Ultra Moon")

# Set Citra emulator window as the foreground window
win32gui.SetForegroundWindow(citra_window)

# Wait for the window to become the foreground window
while True:
    if win32gui.GetForegroundWindow() == citra_window:
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
    time.sleep(3)

    # Move Character Left
    keyboard.press('right')
    time.sleep(1.5)
    keyboard.release('right')
    time.sleep(1)

    # Message 1
    keyboard.press('a')
    time.sleep(.15)
    keyboard.release('a')
    time.sleep(3)
    # Message 2
    keyboard.press('a')
    time.sleep(.15)
    keyboard.release('a')
    time.sleep(1)
    # Message 3
    keyboard.press('a')
    time.sleep(.15)
    keyboard.release('a')
    time.sleep(1)
    # Message 4
    keyboard.press('a')
    time.sleep(.15)
    keyboard.release('a')
    time.sleep(1)
    # Message 5
    keyboard.press('a')
    time.sleep(.15)
    keyboard.release('a')
    time.sleep(1)
    # Message 6
    keyboard.press('a')
    time.sleep(.15)
    keyboard.release('a')
    time.sleep(1)
    # Message 7
    keyboard.press('a')
    time.sleep(.15)
    keyboard.release('a')
    time.sleep(7)
    # Message 8
    keyboard.press('a')
    time.sleep(.15)
    keyboard.release('a')
    time.sleep(1.25)
    # Message 9
    keyboard.press('a')
    time.sleep(.15)
    keyboard.release('a')
    time.sleep(1)
    # Message 10
    keyboard.press('a')
    time.sleep(.15)
    keyboard.release('a')
    time.sleep(1)
    # Message 11
    keyboard.press('a')
    time.sleep(.15)
    keyboard.release('a')
    time.sleep(6.5)
    # Message 12
    keyboard.press('a')
    time.sleep(.15)
    keyboard.release('a')
    time.sleep(3)  # Delay to collect correct color
    print("Finished Dialog")
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