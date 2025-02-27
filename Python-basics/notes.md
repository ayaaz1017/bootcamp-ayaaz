# My Approach to the Problem

## Where I Struggled
One of the first things that tripped me up was publishing to Dev PyPI. I kept running into authentication issues and package naming conflicts.  
Also, figuring out how to make `typer` work properly with argument parsing wasn't as smooth as I expected. Debugging environment variable loading for YAML files was another headache.

## Breaking the Problem Down
Since the project had multiple components (CLI, YAML-based config, logging, and class-based structures), I split it into smaller sections:

- Setting up the `helloworld` module and making it callable via CLI.
- Integrating configuration management so that settings are loaded dynamically.
- Expanding it to support multiple names with `many-hellos`.
- Logging—turning it on/off at different levels for debugging.

## What Went Surprisingly Well
Using decorators for logging and memoization was easier than expected. I was able to add debugging features without modifying the core logic too much.  
Also, packaging everything properly with `setuptools` turned out to be more straightforward than I initially feared.

## Key Learnings
- Always test CLI tools in a fresh environment to avoid hidden dependencies.
- YAML files can be tricky when loading from different locations. Default fallback options are crucial.
- PyPI package names are unique—better check if a name is taken before publishing!
- Logging selectively (turning it on for just the config loader) helps when debugging.

## What AI Helped Me
I used ChatGPT to clarify certain implementation details, especially with packaging and environment variable handling.  
I also referred to official documentation for `typer`, `setuptools`, and `yaml`.

---

*Note: This document was created based on my experience solving the problem.*
