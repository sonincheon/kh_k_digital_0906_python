# 생성자는 클래스가 객체로 만들어 질 때 자동으로 호출되며, 객체의 초기값을 지정 할 수 있습니다
# 생성자 키워드 : __init__
# self는 자신의 객체를 가르키는 변수
class TV :
    def __init__(self, name, is_on, channel, volume):
        self.name = name
        self.is_on = is_on
        self.chnnel = channel
        self.volume = volume

    def set_on(self, is_on):
        self.is_on=is_on

    def set_channel(self,cnl):
        self.chnnel = cnl

    def set_volume(self, vol):
        self.volume = vol

    def get_on(self):
        return self.is_on

    def get_channel(self):
        return self.chnnel

    def view_tv(self):
        power =
