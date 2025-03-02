from abc import ABC, abstractmethod

class NotificationAlertObesrver(ABC):

    @abstractmethod
    def update(self, obervable):
        pass
