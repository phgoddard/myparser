import abc

class Repository(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def save_study(self, studyobj):
        raise NotImplementedError

    @abc.abstractmethod
    def save_file(self, fileobj):
        raise NotImplementedError

    @abc.abstractmethod
    def save_dialog(self, dialogobj):
        raise NotImplementedError