# Working with Iterators and Streams

## Where I Struggled
Initially, understanding how iterators and generators work under the hood was tricky. Writing a custom iterator with `__iter__` and `__next__` seemed unnecessary at first, but it helped grasp how Python handles iteration internally.  
File streaming was another challenge—handling large files efficiently while maintaining readability required switching from simple file reads to generator-based processing.

## Breaking the Problem Down
The tasks varied in complexity, so I took a layered approach:

- Started with basic iterator creation and moved to file streaming.
- Converted a custom file-reading iterator into a generator for efficiency.
- Built processing pipelines that applied multiple transformations dynamically.
- Used `itertools.chain` to combine multiple iterators seamlessly.
- Integrated exception handling to deal with file access issues.

## What Went Surprisingly Well
Implementing stream functions like line numbering and filtering was smoother than expected, thanks to Python’s built-in iterators.  
Mapping existing string functions to stream functions helped reuse logic effectively.  
Also, using YAML configurations to define transformation pipelines made the system more flexible.

## Key Learnings
- Generators significantly improve memory efficiency for large datasets.
- Using iterators allows for a functional, pipeline-style approach to processing data.
- Exception handling in streams is crucial to prevent silent failures in file processing.
- Writing reusable stream functions ensures flexibility when modifying pipelines later.

## What AI Helped Me
I used AI to clarify how iterators and generators differ in behavior, especially regarding memory usage. It also helped in designing function lookups for dynamic pipeline execution.  
Official Python documentation on `itertools` and `fileinput` provided additional insights.

---

*Note: This document was created based on my experience solving the problem.*

[Chat with ChatGPT](https://chatgpt.com/c/67c0724f-2090-8010-a38c-6da98801b71b)