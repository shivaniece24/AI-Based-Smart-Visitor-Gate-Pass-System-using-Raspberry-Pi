import cv2

def capture_face():

    camera = cv2.VideoCapture(0)

    while True:

        ret, frame = camera.read()

        cv2.imshow("Visitor Camera", frame)

        key = cv2.waitKey(1)

        if key == ord('s'):

            filename = "visitor_photos/visitor.jpg"

            cv2.imwrite(filename, frame)

            break

    camera.release()

    cv2.destroyAllWindows()

    return filename
