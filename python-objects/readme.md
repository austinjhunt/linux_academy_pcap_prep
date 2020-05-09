# Inspecting Objects

(venv) Austins-iMac:python-objects huntaj$ python -i amphibious.py
>>> water_car = AmphibiousVehicle('4 cylinder')
>>> water_car.description()
'A AmphibiousVehicle that has traveled 0 miles. using a motor'
>>> AmphibiousVehicle.__mro__
(<class '__main__.AmphibiousVehicle'>, <class 'car.Car'>, <class 'boat.Boat'>, <class 'vehicle.Vehicle'>, <class 'object'>)
>>> quit()
(venv) Austins-iMac:python-objects huntaj$ python -i amphibious.py
>>> water_car = AmphibiousVehicle('4 cylinder')
>>> water_car.description()
'A AmphibiousVehicle that has traveled 0 miles. using a motor'
>>> quit()
(venv) Austins-iMac:python-objects huntaj$ python -i amphibious.py
>>> water_car = AmphibiousVehicle('4 cylinder')
>>> water_car.description()
'A AmphibiousVehicle that has traveled 0 miles. using a motor'
>>> quit()
(venv) Austins-iMac:python-objects huntaj$ python -i mapping.py
>>> Mapping.__update
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: type object 'Mapping' has no attribute '__update'
>>> dir(Mapping)
['_Mapping__update', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'update']
>>> quit()
(venv) Austins-iMac:python-objects huntaj$ python -i amphibious.py
>>> AmphibiousVehicle.__bases__
(<class 'car.Car'>, <class 'boat.Boat'>)
>>> from vehicle import Vehicle
>>> Vehicle.__subclasses__()
[<class 'boat.Boat'>, <class 'car.Car'>]
>>> from bicycle import Bicycle
>>> Vehicle.__subclasses__()
[<class 'boat.Boat'>, <class 'car.Car'>, <class 'bicycle.Bicycle'>]
>>> # Only shows modules that have been loaded.
>>> dir(AmphibiousVehicle)
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'default_tire', 'description', 'drive', 'travel', 'voyage']
>>> # Note that bases is not included. There are some special read-only attributes that arent included in dir output.
>>> hasattr(Boat,'boat_type')
False
>>> # Class does not have that attribute. Instances do.
>>> b = Boat()
>>> hasattr(b, 'boat_type')
True
>>> hasattr(Car,'default_tire')
True
>>> # Has a class level default tire var
>>> issubclass(Boat, Vehicle)
True
>>> issubclass(Boat, AmphibiousVehicle)
False
>>> issubclass(AmphibiousVehicle,Boat)
True
>>> Vehicle.__subclasses__()
[<class 'boat.Boat'>, <class 'car.Car'>, <class 'bicycle.Bicycle'>]
>>> issubclass(AmphibiousVehicle, Vehicle)
True
>>> # Not listed in direct subclass, but is a subclass of a subclass
>>> water_car = AmphibiousVehicle('4 cylinder')
>>> isinstance(water_car, Bicycle)
False
>>> isinstance(water_car, AmphibiousVehicle) and isinstance(water_car, Car) and isinstance(water_car, Boat)
True
>>> water_car is AmphibiousVehicle
False
>>> # instance not the same as parent class
>>> water_car.__dict__
{'distance_traveled': 0, 'unit': 'miles', 'boat_type': 'motor', 'tires': ['tire', 'tire', 'tire', 'tire'], 'engine': '4 cylinder'}
>>> type(water_car)
<class '__main__.AmphibiousVehicle'>
>>> # Because we read amphibious module in for this interpreter session.
>>> Boat.__module__
'boat'
>>> # Not read in
>>> AmphibiousVehicle.__module
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: type object 'AmphibiousVehicle' has no attribute '__module'
>>> AmphibiousVehicle.__module__
'__main__'
>>> str(water_car)
'<__main__.AmphibiousVehicle object at 0x10f53f6d0>'
>>> # Not helpful. We can change this.
>>>