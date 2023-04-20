from abc import ABC, abstractmethod

class Serviceable(ABC):

    def __init__(self):


    @abstractmethod
    def needs_service(self):
        pass