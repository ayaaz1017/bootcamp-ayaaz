import abc

class PersistentQueue(abc.ABC):
    """Abstract base class for persistent queues."""
    
    @abc.abstractmethod
    def enqueue(self, job_data: dict):
        """Add a job to the queue."""
        pass

    @abc.abstractmethod
    def dequeue(self):
        """Retrieve and lock a job for processing."""
        pass

    @abc.abstractmethod
    def mark_complete(self, job_id: int):
        """Mark a job as completed."""
        pass

    @abc.abstractmethod
    def mark_failed(self, job_id: int):
        """Mark a job as failed after too many retries."""
        pass
