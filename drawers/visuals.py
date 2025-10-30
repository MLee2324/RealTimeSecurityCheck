import cv2


# Global variables for tracking
draw = False
ix, iy = -1, -1
# Vertical line for counting people entering and exiting
line_x = 400
hist = {}
# Draw bounding box, label, and tracking ID for person
def draw_person_box(frame, bbox, class_id, track_id):
    person_entered = False
    person_exited = False
    x1, y1, x2, y2 = bbox.astype(int)

    # Centroid Tracking
    cx = int((x1 + x2) / 2)
    cy = int((y1 + y2) / 2)

    if track_id in hist:
        prev_cx, prev_cy = hist[track_id]
        if prev_cx < line_x <= cx:
            person_entered = True
            cv2.circle(frame, (cx, cy), 3, (0, 0, 255), -1)
            cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 1)
            cv2.putText(frame, f"ID: {track_id}", (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 255, 0), 1)
        elif prev_cx > line_x >= cx:
            person_exited = True
            cv2.circle(frame, (cx, cy), 3, (0, 0, 255), -1)
            cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 1)
            cv2.putText(frame, f"ID: {track_id}", (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 255, 0), 1)

    hist[track_id] = (cx, cy)
    return person_entered, person_exited

#Counter
def draw_counter(frame, text, pos, color):
    font = cv2.FONT_HERSHEY_SIMPLEX 
    scale = 0.8
    thickness = 2
    cv2.putText(frame, text, pos, font, scale, color, thickness)

#Draw with mouse cursor custom rectangle to select area identify entry and exit
def draw_rectangle(event, x, y, flags, param):
    global ix, iy, draw
    if event == cv2.EVENT_LBUTTONDOWN:
        draw = True
        ix, iy = x, y
    elif event == cv2.EVENT_MOUSEMOVE:
        if draw:
            cv2.rectangle(param, (ix, iy), (x, y), (0, 255, 0), 1)
    elif event == cv2.EVENT_LBUTTONUP:
        draw = False
        cv2.rectangle(param, (ix, iy), (x, y), (0, 255, 0), 1)
