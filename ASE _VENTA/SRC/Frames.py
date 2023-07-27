'''SWITCH DE FRAME'''


class Frame:
    def __init__(self, mydriver):

        self.driver = mydriver


    def swith_to_frame (self, frame):

        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("fremain")
        self.driver.switch_to.frame(frame)

