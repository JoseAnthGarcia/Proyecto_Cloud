
from Modules.Scheduler import *
class SliceAdministrator:
    def __init__(self):
        pass

    def create_topology(self, grafo):
        scheduler = Scheduler()
        scheduler.decisor(grafo)
        pass