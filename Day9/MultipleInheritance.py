"""

child          parent
CLass A  ----> Class B


"""

class CarShowroom:

    def __init__(self):
        print("BMW Car Showroom")

    def doors(self):
            print("Doors")

    def wheels(self):
            print("wheels")


class ThreeM:
    def foilers(self):
        print("foilers")

class BMW(CarShowroom,ThreeM):

    def sunroof(self):
        print("sun roof")

c=BMW()
c.doors()
c.wheels()
c.sunroof()
c.foilers()
