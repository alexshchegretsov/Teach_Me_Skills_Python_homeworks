from abc import ABC, abstractmethod


class FelineInterface(ABC):
    pass

    @abstractmethod
    def scratchy(self):
        raise NotImplemented

    @abstractmethod
    def climb_on_tree(self):
        raise NotImplemented


class CanineInterface(ABC):
    pass

    @abstractmethod
    def swim(self):
        raise NotImplemented

    @abstractmethod
    def sled(self):
        raise NotImplemented
