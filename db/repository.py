import abc

class Repository(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def save_cxdata(self):
        raise NotImplementedError