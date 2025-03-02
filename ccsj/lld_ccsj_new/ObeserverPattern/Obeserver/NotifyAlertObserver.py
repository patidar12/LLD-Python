from abc import ABC, abstractmethod
class NotifyAlertObeserver(ABC):

    @abstractmethod
    def update(self):
        pass