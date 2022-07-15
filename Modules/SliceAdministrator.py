
from Modules.Scheduler import *
from Modules.LinuxClusterDriver import *
class SliceAdministrator:
    def __init__(self):
        pass

    def create_topology(self, grafo):
        FACTOR = 2
        slice, result = scheduler_main(grafo, FACTOR)
        if result:
            result = linux_driver_main(slice)
        else:
            return False