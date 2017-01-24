# Imports
from sys import platform, argv
from os.path import join, expanduser
from xml.etree import ElementTree as ET

# xpath black magic
status_path = ".//*[@name='" + argv[1] + "']/message"

# Always get the correct file path.
if (platform == 'win32'):
    filepath = join( expanduser('~'), 'AppData', 'Roaming', '.purple', 'status.xml' )
else:
    filepath = join( expanduser('~'), '.purple', 'status.xml' )

# Parse the XML tree, get our node, update it's text, write the file.
tree = ET.parse(filepath)
tree.getroot().find(status_path).text = str(argv[2])
tree.write(filepath)