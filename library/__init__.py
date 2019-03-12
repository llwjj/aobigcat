import sys
import os

path = os.path.abspath('..')

if path not in sys.path:
    sys.path.insert(0,path)

import setting

resource = setting.resource.library
