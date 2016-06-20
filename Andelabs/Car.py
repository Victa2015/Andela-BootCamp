class Car(object):

    def __init__(self, name='General', model='GM', car_type='saloon', num_of_doors=4, num_of_wheels=4, speed=0):
        self.name = name
        self.model = model
        self.car_type = car_type
        self.num_of_doors = num_of_doors
        self.num_of_wheels = num_of_wheels
        self.speed = speed
        self.check_num_of_doors()
        self.check_num_of_wheels()

    def is_saloon(self):
        if self.car_type == 'trailer':
            return False
        return True

    def check_num_of_doors(self):
        if self.name == 'Porshe' or self.name == 'Koenigsegg':
            self.num_of_doors = 2

    def check_num_of_wheels(self):
        if self.car_type == 'trailer':
            self.num_of_wheels = 8

    def drive(self, drive_speed):
        if drive_speed == 'the pedal to the metal':
            self.speed == math.inf
        if self.car_type == 'trailer':
            self.speed = int(77/7) * drive_speed
        if self.name == 'Mercedes':
            self.speed = int(333.33333333333333333333333333333333333333339 * drive_speed)
        return self