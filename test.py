import edsdk

def pic_taken(filename):
    print(f"got picture: {filename}")
    global cam
    cam.disconnect()
    edsdk.terminate()

def got_camera(c):
    global cam
    cam = c
    if cam is None:
        print("no cam connected")
        edsdk.terminate()
    else:
        print("taking picture")
        cam.setPictureCompleteCallback(pic_taken)
        cam.takePicture("C:\\test.jpg")

def got_name(name):
    print(f"Camera name: {name}")

def err(level, msg):
    print(msg)

edsdk.setErrorLevel(edsdk.ErrorLevel.Warn)
edsdk.setErrorMessageCallback(err)

edsdk.getFirstCamera(got_camera)
