from dudoxx_swarm_starter.api_client import client
from dudoxx_swarm_starter.config import AGENT_ROLES, DEFAULT_MODEL
from dudoxx_swarm_starter.logger import setup_logger
from dudoxx_swarm_starter.config import LOG_FILE, LOG_LEVEL

logger = setup_logger(LOG_FILE, LOG_LEVEL)

class Agent:
    def __init__(self, role):
        self.role = role
        self.instructions = AGENT_ROLES.get(role.lower(), "You are a helpful assistant.")
        logger.info(f"Agent created with role: {role}")

    def process_message(self, user_input):
        try:
            logger.info(f"Processing message for {self.role} agent")
            completion = client.chat.completions.create(
                model=DEFAULT_MODEL,
                messages=[
                    {"role": "system", "content": self.instructions},
                    {"role": "user", "content": user_input}
                ]
            )
            response = completion.choices[0].message.content
            logger.info(f"Message processed successfully for {self.role} agent")
            return response
        except Exception as e:
            logger.error(f"Error processing message for {self.role} agent: {e}")
            return f"An error occurred while processing your message: {e}"

def get_agent(role):
    try:
        role = role.lower()
        if role in AGENT_ROLES:
            logger.info(f"Creating agent with role: {role}")
            return Agent(role)
        else:
            logger.warning(f"Attempted to create agent with unknown role: {role}")
            raise ValueError(f"Unknown agent role: {role}")
    except Exception as e:
        logger.error(f"Error creating agent: {e}")
        raise