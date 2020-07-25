#list in dict
car = {'Honda': ['civic','accord'],'Toyata':{1:'vios',2:'yaris'}}
print(car['Honda'][1])
print(car['Toyata'][2])

car.keys() #use in dict only
list(car.keys()) # key display
list(car.values()) #values display
list(car.items())# display all