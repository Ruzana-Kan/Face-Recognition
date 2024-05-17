import cv2
face_Capture = cv2.CascadeClassifier("... ... ...")
video_Capture = cv2.videoCapture

while True:
    ret,video = video_Capture.read()
    faces = face_Capture.detectMultiscale(
        col = cv2.cvtColor(video_data,cv2.color_BGR2GRAY)
        col,scale_Factor = 1.1,
        min_Neighbors = 5,
        min_Size = (30,30),
        flags = cv2.CASCADE_SCALE_IMAGE
    )
    for(X,Y,W,H) in faces:
        cv2.rectangle(video_data,(X,Y),(X+H),(W+H),(0,255,0),2)

        if cv2.waitkey(10) ord("a"):

    break
video_Capture.release()