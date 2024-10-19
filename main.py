import requests
import time

# Define your server address
server_url = "http://172.19.176.1:1234"

# Function to get chat completion with max_tokens
def get_completion(model, prompt, max_tokens=150):
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": max_tokens
    }
    response = requests.post(f"{server_url}/v1/chat/completions", json=data, headers=headers)
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        print(f"Failed to retrieve completion. Status code: {response.status_code}")
        return None

# Function to let two LLMs chat with a message limit per LLM
def llm_conversation(model1, model2, initial_prompt, precontext1, precontext2, message_limit=10):
    conversation = []
    current_prompt = initial_prompt

    for i in range(message_limit):
        # LLM 1 responds
        prompt = f"{precontext1}\n\nCurrent conversation:\n{current_prompt}\n\nYour response:"
        print(f"LLM 1 (Turn {i + 1}): {prompt}")
        response1 = get_completion(model1, prompt)
        conversation.append({'speaker': 'LLM 1', 'message': response1})
        print(f"LLM 1 Response: {response1}\n")
        
        # Update current_prompt for LLM 2
        current_prompt = response1
        
        # Delay to simulate real-time conversation
        time.sleep(1)

        # LLM 2 responds
        prompt = f"{precontext2}\n\nCurrent conversation:\n{current_prompt}\n\nYour response:"
        print(f"LLM 2 (Turn {i + 1}): {prompt}")
        response2 = get_completion(model2, prompt)
        conversation.append({'speaker': 'LLM 2', 'message': response2})
        print(f"LLM 2 Response: {response2}\n")
        
        # Update current_prompt for next iteration
        current_prompt = response2
        
        # Delay before next turn
        time.sleep(1)

    # Save the conversation to a Markdown file
    save_to_md("llm_conversation.md", conversation)

# Function to save the conversation to a Markdown file
def save_to_md(filename, conversation):
    with open(filename, 'w') as f:
        f.write("# LLM Conversation\n\n")
        for i, turn in enumerate(conversation):
            f.write(f"### Turn {i+1}\n\n")
            f.write(f"{turn['speaker']}: {turn['message']}\n\n")

# Initial conversation setup
initial_prompt = """Let's discuss the tool that allows two LLMs to talk to each other and refine ideas. 
What are the potential business cases where this tool could provide value? 
How can it be used effectively in various industries or scenarios?"""

precontext1 = """You are an AI assistant named Innovator, discussing the potential applications and business cases for a tool 
that enables two LLMs to converse and refine ideas. Your role is to propose innovative use cases, identify potential benefits, 
and consider how this tool could be applied in various industries. Be creative, but also practical in your suggestions. 
Consider both the advantages and potential challenges of using such a tool.

Keep your responses brief and conversational, around 2-3 sentences. Avoid repeating information and focus on adding new ideas or insights to the discussion."""

precontext2 = """You are an AI assistant named Analyst, evaluating the business potential and practical applications of a tool 
that allows two LLMs to communicate and develop ideas. Your task is to critically assess the proposed use cases, discuss potential 
ROI, and consider implementation challenges. Provide insights on how businesses could leverage this tool to solve real-world 
problems or improve existing processes. Be analytical and consider both opportunities and limitations.

Keep your responses brief and conversational, around 2-3 sentences. Avoid repeating information and focus on adding new ideas or insights to the discussion."""

llm_conversation("model-id-1", "model-id-2", initial_prompt, precontext1, precontext2, message_limit=10)
