import cv2

cap = cv2.VideoCapture(r"C:\Users\sasi1\Desktop\Programovani\Python Projects\Analyse video and pictures\videos\video.avi")

car_cascade = cv2.CascadeClassifier(r"C:\Users\sasi1\Desktop\Programovani\Python Projects\XML FILES\haarcascade_smile.xml")

while True: 
    # reads frames from a video 
    ret, frames = cap.read() 
      
    # convert to gray scale of each frames 
    gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY) 
      
  
    # Detects cars of different sizes in the input image 
    cars = car_cascade.detectMultiScale(gray, 1.1, 1) 
      
    # To draw a rectangle in each cars 
    for (x,y,w,h) in cars: 
        cv2.rectangle(frames,(x,y),(x+w,y+h),(0,0,255),2) 
  
   # Display frames in a window  
    cv2.imshow('video2', frames) 
      
    # Wait for Esc key to stop 
    if cv2.waitKey(33) == 27: 
        break
  
# De-allocate any associated memory usage 
cv2.destroyAllWindows() 
