
class Mobile:
    def show(self):
        print("This is a Mobile Device")

class SmartPhone(Mobile):
    def smartphone(self):
        print("A Smartphone is an advanced Mobile Device")

class FeaturePhone:
    def featurephone(self):
        print("Feature phones have basic calling and texting functions")

class Android(SmartPhone, FeaturePhone):
    def __init__(self):
        print("Android comes with android os")

class iPhone(SmartPhone, FeaturePhone):
    def __init__(self):
        print("iPhone comes with iOS")

print("--------- Android Phone ---------")
android = Android()
android.show()
android.smartphone()
android.featurephone()

print("--------- iPhone ---------")
iphone = iPhone()
iphone.show()
iphone.smartphone()
iphone.featurephone()
