class cake():
    def __init__(self, layers, event, flavour):
        self.layers=layers
        self.event=event
        self.flavour=flavour

inputLayers = input("How many layers would you like for your cake \n")
inputEvent = input("What event will this cake be made for \n")
inputCake = input("What flavour of cake? \n")

freshCake = cake(inputLayers,inputEvent,inputCake)

print("The cake will have "+ freshCake.layers+ " layers")
print("The cake will be made for a "+freshCake.event)
print("The cake will be "+freshCake.flavour + " flavour")
