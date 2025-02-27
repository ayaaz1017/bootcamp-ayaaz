# Working with APIs

## Where I Struggled
Dealing with authentication, especially OAuth tokens for GitHub and OpenWeatherMap API, was tricky at first. Handling rate limits and understanding response structures took some time.  
GraphQL queries were another challenge—compared to REST, crafting the right queries and handling nested responses required more effort.

## Breaking the Problem Down
Since APIs varied in complexity, I categorized them into three levels:

- **Basic API Calls:** Fetching public data like GitHub repos, public events, and Pokémon info using simple `requests.get()`.
- **Authenticated APIs:** Working with APIs requiring authentication, such as GitHub user contributions and OpenWeatherMap.
- **GraphQL Queries:** Querying GitHub and SpaceX data, focusing on structured queries and response handling.

For FastAPI and Streamlit, I followed a step-by-step approach:

- Started with a simple FastAPI app and expanded it to handle authentication, CRUD operations, and file uploads.
- For Streamlit, I built basic apps first, then added reactivity, authentication, and advanced data visualization.

## What Went Surprisingly Well
Despite initial struggles, handling REST APIs became easier with consistent patterns in requests and response parsing.  
Using Pydantic in FastAPI helped structure API requests and responses neatly.  
Streamlit’s session state for managing user interactions was intuitive and simplified stateful operations.

## Key Learnings
- REST APIs are straightforward once authentication and rate limits are handled.
- GraphQL is powerful but requires a deeper understanding of schemas and queries.
- FastAPI is well-suited for scalable API development with built-in validation and async support.
- Streamlit simplifies web UI development, making data visualization and interaction easy.

## What AI Helped Me
I used AI for debugging API authentication issues, understanding GraphQL query structuring, and refining FastAPI models.  
Official API documentation for GitHub, OpenWeatherMap, and SpaceX was essential for understanding request formats.

---

*Note: This document was created based on my experience working with APIs.*
