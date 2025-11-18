class Mahindra:
    def vehicles(self):
        print("Mahindra produces reliable and powerful vehicles.")
    
    def technology(self):
        print("Mahindra focuses on advanced automotive technology.")

class MahindraAuto(Mahindra):
    def __init__(self):
        print("For Travel")

class MahindraTractor(Mahindra):
    def __init__(self):
        print("For Farming")

print("====Mahindra Auto====")
auto = MahindraAuto()
auto.vehicles()
auto.technology()

print("====Mahindra Tractor====")
tractor = MahindraTractor()
tractor.vehicles()
tractor.technology()
