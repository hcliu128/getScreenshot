import cv2
import time
import os

snap_url = "rtsp://admin:sp77343488@192.168.1.108:554/cam/realmonitor?channel=1&subtype=0&unicast=true&proto=Onvif"

#path setting

def makedir():
    folder_path = os.getcwd() +"\\pics"
    if not os.path.isdir(folder_path):
        os.mkdir(folder_path)

    folder_path += f"\\{(lambda : (time.ctime().split()[1]) )()}"
    if not os.path.isdir(folder_path):
        os.mkdir(folder_path)
    
    folder_path += f"\\{(lambda : (time.ctime().split()[2]) )()}"
    if not os.path.isdir(folder_path):
        os.mkdir(folder_path)

    folder_path +=  f"\\{(lambda : (time.ctime().split()[3]) )()}"
    if not os.path.isdir(folder_path):
        os.mkdir(folder_path)

    return folder_path

def save_screenshot():
    cap = cv2.VideoCapture(snap_url)
    
    while True:
        retval, frame = cap.read()
        if not retval:
            raise IOError("Camera is not open")
        cv2.imshow("capture", frame)
        folder_path = makedir()
        file_name = f'{folder_path}+{time.time()}.png'
        if cv2.waitKey(1) :   #一秒儲存一張
            cv2.imwrite(f'{file_name}', frame)   #儲存路徑
        break

    cap.release()
    cv2.destroyAllWindows()
        

if __name__ == "__main__":
    try:
        while True:
            save_screenshot()
    except KeyboardInterrupt:
        pass
    
