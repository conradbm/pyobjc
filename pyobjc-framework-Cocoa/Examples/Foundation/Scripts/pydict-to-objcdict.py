import pprint

from PyObjCTools.Conversion import propertyListFromPythonCollection

input_value = {
    "a": [1, 2, 3, 4],
    "b": "c",
    "d": 3,
    "e": None,
    "f": [1, {"2": 3, "a": "b"}, [3, 4]],
    "g": {"h": "i"},
    "j": (1, 2, 3, "k", "l"),
}

print("Converting (Python Collection):")
pprint.pprint(input_value)

convertedCollection = propertyListFromPythonCollection(input_value)

print()
print()
print("Converted (ObjC collection):")
print("%s" % convertedCollection.description())
