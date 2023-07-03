import cv2
import datetime
import time

# Keeps track of how long program has been running
startTime = time.time()
def getUptime():
    uptime_seconds = int(time.time() - startTime)
    minutes, seconds = divmod(uptime_seconds, 60)
    return f"{minutes} minutes, {seconds:.1f} seconds."

# Initialize camera
cameraPort = 2  # The index of the camera
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
#cap.set(cv2.CAP_PROP_SETTINGS, 1)

# Create preview window
window_width = 1280  # Define window size
window_height = 720  # Define window size
cv2.namedWindow("Preview Window", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Preview Window", window_width, window_height)

folder_path = "./Screenshots/"
currentDateTimeString = datetime.datetime.today().strftime('%m-%d-%Y_%H-%M_')

# Define region of interest
x, y, w, h = 785, 450, 10, 10

# calculate the average color in the region
def calculateColorAverage():
    # Takes average of colors from time executed
    color0_average = total_color0/timesExecuted
    color1_average = total_color1/timesExecuted
    color2_average = total_color2/timesExecuted

    # Round to nearest hundredths
    color0_average = round(color0_average, 1)
    color1_average = round(color1_average, 1)
    color2_average = round(color2_average, 1)

    # Print Results
    print("The average colors are:")
    # (Blue, Green, Red, Alpha)
    print("(" + str(color0_average) + ", " + str(color1_average) + ", " + str(color2_average) + ", 0.0" +")")

# calculate the tolerance to use
def calculateColorTolerance():
    # Prints Results
    print("The highest color tolerance should be:")
    print(round(max_tolerance, 1)) # Rounds to first decimal

# Main
timesExecuted = 0.0;

# Tolerance variables
max_tolerance = 0.0

# Color variables
total_color0 = 0.0
total_color1 = 0.0
total_color2 = 0.0

while True:
    # While loop counter
    timesExecuted += 1

    # Start Camera
    success, frame = cap.read()  # Initialize Camera
    roi = frame[y:y + h, x:x + w]  # Region of Interest (The region we are analyzing0.
    avg_color = cv2.mean(roi)  # Get average color (Default BGRA).
    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)  # Draw ROI to visualize what it's observing
    cv2.imshow("Preview Window", frame)  # Pop-up Window to observe

    # Add the color to its respective variable
    total_color0 += avg_color[0]
    total_color1 += avg_color[1]
    total_color2 += avg_color[2]

    # Calculate the tolerance
    # Temporarily calculate the average color
    temp_color0_average = total_color0/timesExecuted
    temp_color1_average = total_color1/timesExecuted
    temp_color2_average = total_color2/timesExecuted

    # Subtract the recently collected color from the average to get the tolerance per color
    color0 = abs(avg_color[0] - temp_color0_average)
    color1 = abs(avg_color[1] - temp_color1_average)
    color2 = abs(avg_color[2] - temp_color2_average)
    # Find which color had the highest tolerance
    highest_tolerance = max(color0, color1, color2)
    # Replace max_tolerance if the recently found tolerance is higher than the max_tolerance
    max_tolerance = max(max_tolerance, highest_tolerance)

    # Press Q to Close the Preview Window
    if cv2.waitKey(1) == ord('q'):
        print("Closing Preview and Program (Pressed Q)")
        print("The program executed for " + str(timesExecuted) + " amount of times.")
        calculateColorAverage()
        calculateColorTolerance()
        print("The program has been running for: " + getUptime())
        break

# Releases camera when program finishes
cap.release()
cv2.destroyAllWindows()
