# Python Code Setup and OpenAI API Implementation Log

## Task ID: IMPL_SWARM_STARTER_20241019_T1
## Status: Completed

### Actions Taken:
1. Created main.py file in the dudoxx_swarm_starter directory.
2. Implemented basic OpenAI API call functionality.
3. Created agents.py file with agent classes for customer support and sales roles.
4. Updated main.py to include agent implementation and handoff logic.

### Current Implementation:

#### agents.py
```python
from openai import OpenAI
import os

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

class Agent:
    def __init__(self, role, instructions):
        self.role = role
        self.instructions = instructions

    def process_message(self, user_input):
        try:
            completion = client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": self.instructions},
                    {"role": "user", "content": user_input}
                ]
            )
            return completion.choices[0].message.content
        except Exception as e:
            return f"An error occurred: {e}"

class CustomerSupportAgent(Agent):
    def __init__(self):
        super().__init__("Customer Support", "You are a helpful customer support agent. Assist users with their inquiries and problems.")

class SalesAgent(Agent):
    def __init__(self):
        super().__init__("Sales", "You are a knowledgeable sales agent. Help users with product information and purchasing decisions.")

def get_agent(role):
    if role.lower() == "customer support":
        return CustomerSupportAgent()
    elif role.lower() == "sales":
        return SalesAgent()
    else:
        raise ValueError(f"Unknown agent role: {role}")
```

#### main.py
```python
import os
from agents import get_agent

def main():
    print("Welcome to the Dudoxx Swarm Starter!")
    print("Available agents: Customer Support, Sales")
    print("Type 'switch' to change agents or 'exit' to quit.")

    current_agent = get_agent("customer support")
    
    while True:
        user_input = input(f"\n[{current_agent.role}] User: ").strip()
        
        if user_input.lower() == 'exit':
            print("Thank you for using Dudoxx Swarm Starter. Goodbye!")
            break
        elif user_input.lower() == 'switch':
            new_role = input("Which agent would you like to switch to? (Customer Support/Sales): ").strip()
            try:
                current_agent = get_agent(new_role)
                print(f"Switched to {current_agent.role} agent.")
            except ValueError as e:
                print(f"Error: {e}")
            continue

        response = current_agent.process_message(user_input)
        print(f"[{current_agent.role}] Agent: {response}")

if __name__ == "__main__":
    main()
```

### Next Steps:
1. Refactor the code into reusable modules (Task ID: IMPL_SWARM_STARTER_20241019_T3)
2. Add logging and error handling (Task ID: IMPL_SWARM_STARTER_20241019_T4)
3. Write unit tests for core functions (Task ID: IMPL_SWARM_STARTER_20241019_T5)
4. Update the README.md file with usage instructions

### Notes:
- The current implementation uses the environment variable OPENAI_API_KEY. Ensure this is set before running the script.
- The agent switching functionality has been implemented, allowing users to switch between customer support and sales agents.
- Consider implementing a more robust error handling and logging system in future iterations.
- The next phase of development should focus on improving code structure, testing, and documentation.