
from Modules.Scheduler import *
class SliceAdministrator:
    def __init__(self):
        pass

    def create_topology(self, grafo):
        FACTOR = 0.5
        nuevo_grafo = scheduler_main(grafo, FACTOR)
        return nuevo_grafo