class Television:
    def __init__(self, brand, power_rating, resolution):
        self.brand = brand
        self.power_rating = power_rating
        self.resolution = resolution
        self.is_on = False  

    def turn_on(self):
        self.is_on = True
        print(f"Turning on {self.brand} TV")

    def turn_off(self):
        self.is_on = False
        print(f"Turning off {self.brand} TV")

    def change_channel(self, channel):
        if self.is_on:
            print(f"Changing channel to {channel} on {self.brand} TV")
        else:
            print("TV is off. Please turn it on first.")

    def adjust_volume(self, volume):
        if self.is_on:
            print(f"Adjusting volume to {volume} on {self.brand} TV")
        else:
            print("TV is off. Please turn it on first.")


class smartTV(Television):
    def __init__(self, brand, power_rating, resolution, voice_control):
        super().__init__(brand, power_rating, resolution)
        self.voice_control = voice_control

    def voice_command(self, command):
        if self.is_on and self.voice_control:
            print(f"Processing voice command: {command}")
        else:
            print("Voice control is not available or TV is off.")


 
    

samsung_tv = Television("Samsung", "A" , "4K")
samsung_tv.turn_on()
samsung_tv.change_channel(10)
samsung_tv.adjust_volume(20)
samsung_tv.turn_off()


tv_list = [Television("Samsung", "A", "4K"), smartTV("LG", 75, "8K", True)]

for tv in tv_list:
    tv.turn_on()  