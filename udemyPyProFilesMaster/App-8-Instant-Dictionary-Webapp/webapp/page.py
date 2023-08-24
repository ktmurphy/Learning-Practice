from abc import ABC, abstractmethod

class Page:

    @abstractmethod
    def serve(self):
        pass