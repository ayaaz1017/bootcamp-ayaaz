from abc import ABC, abstractmethod

class Streamable(ABC):
    @abstractmethod
    def stream(self):
        pass

class VideoStream(Streamable):
    def stream(self):
        return "Streaming video..."

class AudioStream(Streamable):
    def stream(self):
        return "Streaming audio..."

# Create instances
video = VideoStream()
audio = AudioStream()

print(video.stream())
print(audio.stream())