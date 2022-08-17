import cv2
import numpy as np

# Create an object to read camera video 
filename = 'cvideo1.mp4'
#id = 0
id = 'rtsp://admin:L2E03F0A@192.168.1.7:80/cam/realmonitor?channel=1&subtype=0&unicast=false&proto=Onvif'
cap = cv2.VideoCapture(id)

# Check if camera opened successfully
if (cap.isOpened() == False): 
  print("Camera is unable to open.")

# Set resolutions of frame.
# convert from float to integer.
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

# Create VideoWriter object.
# and store the output in 'captured_video.avi' file.

video_cod = cv2.VideoWriter_fourcc(*'XVID')
video_output= cv2.VideoWriter(filename,
                      video_cod,
                      10,
                      (frame_width,frame_height))

while(True):
  ret, frame = cap.read()

  if ret == True: 
    
    # Write the frame into the file 'captured_video.avi'
    video_output.write(frame)

    # Display the frame, saved in the file   
    cv2.imshow('frame',frame)

    # Press x on keyboard to stop recording
    if cv2.waitKey(1) & 0xFF == ord('q'):
      break

  # Break the loop
  else:
    break  

# release video capture
# and video write objects
cap.release()
video_output.release()

# Closes all the frames
cv2.destroyAllWindows() 

print("The video was successfully saved") 