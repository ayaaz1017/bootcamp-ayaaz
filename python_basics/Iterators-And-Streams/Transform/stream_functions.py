from typing import Iterator

def number_the_lines(lines: Iterator[str]) -> Iterator[str]:
    for index, line in enumerate(lines, start=1):
        yield f"{index}. {line}"

def coalesce_empty_lines(lines: Iterator[str]) -> Iterator[str]:
    prev_line = None
    for line in lines:
        if line.strip():
            yield line
        elif prev_line and prev_line.strip():
            yield ''
        prev_line = line

def remove_empty_lines(lines: Iterator[str]) -> Iterator[str]:
    for line in lines:
        if line.strip():
            yield line

def remove_even_lines(lines: Iterator[str]) -> Iterator[str]:
    for index, line in enumerate(lines, start=1):
        if index % 2 != 0:
            yield line

def break_lines(lines: Iterator[str], max_length=20) -> Iterator[str]:
    for line in lines:
        while len(line) > max_length:
            yield line[:max_length]
            line = line[max_length:]
        if line:
            yield line
