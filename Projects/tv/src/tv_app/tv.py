class Television:

    def __init__(self):
        self.is_on = False
        self.volume_level = 0
        self.channel = 1
        self.is_mute = False

    def get_volume(self):
        return self.volume_level

    def get_mute(self):
        return self.is_mute

    def get_channel(self):
        return self.channel
    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False
        self.volume_level = 0
        self.channel = 1

    def volume_up(self):
        if self.is_on and self.volume_level < 100:
            self.volume_level += 1
            self.is_mute = False

    def get_volume(self):
        return self.volume_level
    def get_mute(self):
        return self.is_mute

    def volume_down(self):
        if self.is_on and self.volume_level > 0:
            self.volume_level -= 1

    def channel_up(self):
        if self.is_on and self.channel <=100:
            self.channel += 1
    def channel_down(self):
        if self.is_on and self.channel > 1:
            self.channel -= 1

    def set_channel(self, channel):
        if self.is_on and channel <= 100 or self.channel > 1:
            self.channel = channel
    def mute(self):
        if self.is_on:
            self.is_mute = True
    def unmute(self):
        if self.is_on:
            self.is_mute = False












