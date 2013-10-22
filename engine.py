from action import Actions

class Engine:

    __commands = {}
    __act = Actions()


    def __init__(self):
       self.__commands = {'say': self.__act.communication,'do': self.__act.action}
        

    def promit(self):
        uinput = raw_input("Testing: ")
        print uinput

        #some sanatising required
        uinput = str.strip(uinput)
        elements = uinput.split(' ')

        print self.__commands[elements[0]](elements[1:])
        
        return


        
