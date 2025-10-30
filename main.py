import cv2
from ultralytics import YOLO

from drawers import (
     draw_person_box,
     draw_counter
     )

#instance variables
entered = 0
exited = 0
line_x = 340

def detect_people(frame,model):
    global entered, exited
    ##Given Code Reuse from website##
    #To track people in the frame
    results = model.track(frame, persist=True, conf=0.6)

    #Loop to figure out if class_id = 0 then person
    for box in results[0].boxes:
        if int(box.cls) == 0 and box.conf > 0.6:
            #print("Person detected.")
            ##Given Code Reuse from website##
            bbox = box.xyxy[0].cpu().numpy()
            if box.id is not None: 
                track_id = int(box.id.item())
                #Usage of draw method
                person_entered, person_exited = draw_person_box(frame, bbox, int(box.cls), track_id)
                if person_entered:
                    entered += 1
                if person_exited:
                    exited += 1
        return entered, exited

#Debugging code to track mouse position
#def mouse_callback(event, x, y, flags, param):
    #if event == cv2.EVENT_MOUSEMOVE:
       #print(f"Mouse Position moved to: ({x}, {y})")

def main():
    #Load Pretrained Model
    model = YOLO("yolov8m.pt")
    
    #Initialize Webcam
    cap = cv2.VideoCapture (0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 700)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    if cap.isOpened() == False:
            print("Webcam Invalid.")
            return

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        detect_people(frame, model)
        draw_counter(frame, f"Entered: {entered}", (10, 40), (0, 255, 0))
        draw_counter(frame, f"Exited: {exited}", (520, 40), (0, 0, 255))
        
        #Draw vertical line in the middle of the frame
        cv2.line(frame,(line_x,0),(line_x,frame.shape[0]),(255,255,255),2)
        #Debugging code to track frame shape
        #print(frame.shape)
        #cv2.setMouseCallback("Security System Checker", mouse_callback)
        cv2.imshow("Security System Checker",frame)

        if cv2.waitKey(1) == ord('q'):
             break
    cap.release()
    cv2.destroyAllWindows()
        
#To protect outsiders to execute code
if __name__ == "__main__":
     main()