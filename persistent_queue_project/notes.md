# Persistent Queue System

## Overview
The system consists of a persistent queue where producers submit jobs, and consumers process them. The queue should survive application restarts, ensuring that jobs are not lost even in case of crashes.

## System Architecture
There are three main applications interacting with the queue:

- **Producer:** Submits jobs to the queue.
- **Consumer:** Processes jobs from the queue.
- **Ops/Admin:** Monitors job status, resubmits jobs, and manages failures.

The system supports multiple producers and consumers working simultaneously, ensuring robustness and preventing job duplication.

## Key Considerations
- The queue must persist jobs beyond application restarts.
- Multiple producers and consumers must be able to interact with the queue.
- Each job must have a unique identifier.
- Isolation of implementation details to avoid abstraction leaks.
- Future extensibility for alternative implementations.

## Setup and Design
Project initialization should include a well-documented README explaining the problem, system design, and usage instructions. The queue interface should be structured as an abstract base class, ensuring flexibility in implementation.

## Process Management
Since the system involves multiple running applications, process management is crucial. The recommended approach is using **Supervisor** to manage producers and consumers, ensuring they restart upon failures. Logs must be maintained for debugging.

## Implementation Plan
- **Producer:** Generates and submits jobs at regular intervals.
- **Consumer:** Processes jobs from the queue, modifying data as required.
- **Persistent Queue:** Implemented using SQLite to ensure data is not lost.
- **Process Management:** Use Supervisor for monitoring and restarting processes.

## Challenges and Considerations
Several challenges must be addressed:

- Ensuring jobs are not processed by multiple consumers simultaneously.
- Handling consumer crashes by allowing other processes to pick up unprocessed jobs.
- Implementing a mechanism to flag problematic jobs as unprocessable.
- Using database locking strategies to prevent job duplication.
