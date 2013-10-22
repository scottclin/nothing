from xmlparse import Parser
import os.path as outside

class Actions:

    __parse

    def __init__(self):
      __parse = Parser()  

    def communication(self, arg):
        text = ""
        for part in arg:
            text += part + " "
        text = str.strip(text)
        print  text
	return


    def action(self, arg):
        print "You did: " + arg
        return

    def load(self, arg):
        if outside.isFile(arg):
            parse.loadxml(arg)

