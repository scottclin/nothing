import xAhml.etree.ElementTree as xmltree

class Parser:

    def readxml(self, filepath):
        try:
            tree = xmltree.parse('filepath')
            root = tree.getroot()
            
        except IOError:
            print 'Failed to load xml file'
        

    def writexml(self, filepath, element, pelement):
        SubElement(pelement, element)
