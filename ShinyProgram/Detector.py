# import packages
import cv2
import serial
import datetime
import time
import requests

# Keeps track of how long program has been running
startTime = time.time()
def getUptime():
    uptime_seconds = int(time.time() - startTime)
    minutes, seconds = divmod(uptime_seconds, 60)
    return f"{minutes} minutes, {seconds:.1f} seconds."

# Initialize Arduino connection
COM = 'COM4'
BAUD = 9600
ser = serial.Serial(COM, BAUD)

# Set the webhook URL and user ID to tag
webhook_url = ""
user_id = ""

# Initialize camera
# If there are camera errors debug in CollectColor
cameraPort = 0  # The index of the camera
cap = cv2.VideoCapture(cameraPort, cv2.CAP_DSHOW)
wCam = 1920  # Width of camera resolution
hCam = 1080  # Height of camera resolution
cap.set(cv2.CAP_PROP_FRAME_WIDTH, wCam)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, hCam)

# Adjust Camera Settings
# Comment out when finished adjusting/not in use.
# Recommended setting parameters that have an "Auto" feature
# Format is: cap.set(cv2.CAP_PROP_NAME-PROPERTY)
cap.set(cv2.CAP_PROP_FOCUS, 85)  # Focus
cap.set(cv2.CAP_PROP_EXPOSURE, -5)  # Exposure
# # WB 6100 b/c code doesnt work
cap.set(cv2.CAP_PROP_SETTINGS, 1)

# Create preview window dimensions
window_width = 1280  # Define window size
window_height = 720  # Define window size
cv2.namedWindow("Preview Window", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Preview Window", window_width, window_height)

# file system
folder_path = "./Screenshots/"
currentDateTimeString = datetime.datetime.today().strftime('%m-%d-%Y_%I-%M-%p_')

# Define region of interest
x, y, w, h = 915, 515, 10, 10

# Color gathered from CollectColor
pokemonColor = (213.3, 88.06, 105.72, 0.0)

# Define color tolerance
# Recommended to have low tolerance (will increase chance of false positives)
tolerance = 20

# Reset Counter
resetCounter = 21

# Check if Pokemon is Shiny
def isItShiny():
    # Check if color is different from usual color
    # If different this means its shiny
    # Compare the colors with a tolerance
    color0 = abs(avg_color[0] - pokemonColor[0])
    color1 = abs(avg_color[1] - pokemonColor[1])
    color2 = abs(avg_color[2] - pokemonColor[2])
    if color0 <= tolerance and color1 <= tolerance and color2 <= tolerance:
        # The colors match.
        # Pokemon is not Shiny.
        ser.write(b'n')  # Sends a message to the Arduino.
        print("The Pokemon is not shiny.")
        takeScreenshot(False, "")  # Take screenshot, and don't tag to Discord or send specialized message.
    else:
        # The colors don't match within the tolerance range.
        # Pokemon is Shiny.
        ser.write(b'y')  # Sends a message to the Arduino
        print("The Pokemon is Shiny! Found After " + str(resetCounter) + " resets.")
        # Take screenshot, tag to Discord, and send specialized message.
        specialMessage = "The Pokemon is Shiny! Found After " + str(resetCounter) + " resets." + "\nUptime is: " + getUptime()
        takeScreenshot(True, specialMessage)

    # Monitor what isItShiny() receives/outputs
    # Compare the highest value among the three colors
    # highest_color = max(color0, color1, color2)
    # print()  # Blank line
    # print("The average color was:")
    # print(avg_color)
    # print("The color to compare against:")
    # print(pokemonColor)
    # print("The highest color difference is", str(round(highest_color, 1)))
    print("The program has reset: " + str(resetCounter) + " times.")


# Takes screenshot when called and saves to folder path.
# Parameter determines whether to send message to Discord or not.
def takeScreenshot(sendMessage, message_str):
    # Take Screenshot of comparison
    cv2.imwrite(folder_path + currentDateTimeString + str(resetCounter) + '.png', frame)
    print(f"Saved screenshot to {folder_path}")

    # Set the file path and name
    file_name = currentDateTimeString + str(resetCounter) + '.png'
    file_path = folder_path + file_name

    # Open the file in binary mode
    with open(file_path, "rb") as f:
        # Read the contents of the file
        file_contents = f.read()

    # Set the file attachment for the POST request
    files = {
        "file": (file_name, file_contents)
    }

    # Message to send
    message = {
        "content": f"<@{user_id}> **Encounter Notification** \n {message_str}",
    }

    # Based on parameter determines whether to post image to Discord
    if sendMessage:
        # Sends message to Discord
        response = requests.post(webhook_url, data=message, files=files)  # Send Image To Discord
    else:
        pass  # Sends nothing


# Main
while True:
    success, frame = cap.read()  # Initialize Camera
    roi = frame[y:y + h, x:x + w]  # Region of Interest (The region we are analyzing.
    avg_color = cv2.mean(roi)  # Get average color (Default BGR).
    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)  # Draw ROI to visualize what it's observing
    cv2.imshow("Preview Window", frame)  # Pop-up Window to observe

    # Wait for "Command: CheckShiny" message from Arduino
    while ser.in_waiting:
        message = ser.readline()  # Reads message from Arduino
        print()  # Blank line
        print("Message from Arduino:")
        print(message)
        if message == b'Command: checkIfShiny\r\n':
            resetCounter += 1  # increase resetCounter
            isItShiny()
        else:
            pass  # do nothing

    # Press Q to Close the Preview Window
    if cv2.waitKey(1) == ord('q'):
        print("Closing Preview and Program (Pressed Q)")
        break

# Releases camera when program finishes
cap.release()
cv2.destroyAllWindows()
