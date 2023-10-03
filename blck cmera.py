import ctypes

class DisableCamera:
    def __init__(self):
        self.status = None

    def disable(self):
        try:
            ctypes.windll.user32.SendMessageW(1, 0x0112, 0xF170, 2)
            self.status = "Camera disabled successfully"
        except Exception as e:
            self.status = "Failed to disable camera: " + str(e)

camera = DisableCamera()
camera.disable()
print(camera.status)
