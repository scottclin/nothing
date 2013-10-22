class Object:

    __name
    __description

    def __init__(self, name="Nemo", description="Is this latin or a reference to a movie.."):
        self.__name = name
        self.__description = description

    def setName(self, newname):
        self.__name = newname

    def getName(self):
        return __name

    def setDescription(self, newdescription):
        self.__description = newdescription

    def getDescription(self):
        return __description
