# LLM Conversation Tool

This project demonstrates a tool that enables two Large Language Models (LLMs) to engage in a conversation with each other, refining ideas and exploring concepts. It uses LMStudio to run a local LLM model and interfaces with it using Python.

## Overview

The tool allows two AI assistants, powered by the same or different LLM models, to have a back-and-forth conversation on a given topic. This can be used for various purposes, such as idea generation, problem-solving, or exploring complex topics from multiple perspectives.

## Prerequisites

- Python
- LMStudio (for running the local LLM model)
- `requests` library (`pip install requests`)

## Setup

1. Install and set up LMStudio on your local machine.
2. Launch your chosen LLM model in LMStudio.
3. Note the server address provided by LMStudio (usually `http://localhost:1234` or similar).
4. Update the `server_url` in the `main.py` file with the correct address.

## Usage

1. Modify the `initial_prompt`, `precontext1`, and `precontext2` variables in `main.py` to set up the conversation topic and roles for each AI assistant.
2. Run the script:

   ```
   python main.py
   ```

3. The conversation will be saved in `llm_conversation.md`.

## How It Works

1. The script sends requests to the local LLM model running in LMStudio.
2. Two AI assistants take turns responding to each other's messages.
3. Each assistant is given a specific role and context to guide their responses.
4. The conversation continues for a set number of turns (default is 10).

## Customization

- Adjust the `message_limit` parameter in the `llm_conversation` function call to change the length of the conversation.
- Modify the `precontext1` and `precontext2` variables to assign different roles or personalities to the AI assistants.
- Change the `initial_prompt` to explore different topics or scenarios.

## Potential Applications

- Brainstorming and idea refinement
- Analyzing complex problems from multiple angles
- Generating creative content
- Simulating expert discussions on specific topics

## Limitations

- The quality of the conversation depends on the capabilities of the underlying LLM model.
- The tool does not have long-term memory beyond the current conversation context.
- Responses may sometimes be inconsistent or contradictory.

## Future Improvements

- Implement a shared memory system to maintain context across multiple conversations.
- Add support for more than two AI assistants in a single conversation.
- Integrate with external data sources to provide up-to-date information.

## License

This project is open-source and available under the MIT License.
