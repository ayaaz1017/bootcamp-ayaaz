from abc import ABC, abstractmethod

class PersistentQInterface(ABC):
    @abstractmethod
    def enqueue(self, job_id, payload):
        pass

    @abstractmethod
    def dequeue(self):
        pass

    @abstractmethod
    def mark_done(self, job_id):
        pass

    @abstractmethod
    def mark_failed(self, job_id):
        pass
