from typing import Callable, Iterator
from processing_functions import *

def string_to_stream_function(in_function: Callable[[str], str]) -> Callable[[Iterator[str]], Iterator[str]]:
    def stream_func(lines: Iterator[str]) -> Iterator[str]:
        for line in lines:
            yield in_function(line)
    return stream_func

# Adapting string functions to stream functions
stream_upper_case = string_to_stream_function(upper_case)
stream_remove_stop_words = string_to_stream_function(remove_stop_words)
stream_capitalize = string_to_stream_function(capitalize)
stream_lower_case = string_to_stream_function(lower_case)
