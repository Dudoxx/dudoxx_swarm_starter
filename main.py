from dudoxx_swarm_starter.agents import get_agent
from dudoxx_swarm_starter.config import AGENT_ROLES
from dudoxx_swarm_starter.logger import setup_logger
from dudoxx_swarm_starter.config import LOG_FILE, LOG_LEVEL

logger = setup_logger(LOG_FILE, LOG_LEVEL)

def main():
    logger.info("Starting Dudoxx Swarm Starter")
    print("Welcome to the Dudoxx Swarm Starter!")
    print(f"Available agents: {', '.join(AGENT_ROLES.keys())}")
    print("Type 'switch' to change agents or 'exit' to quit.")

    try:
        current_agent = get_agent("customer_support")
        logger.info("Initialized with customer support agent")
    except Exception as e:
        logger.error(f"Failed to initialize customer support agent: {e}")
        print("An error occurred while initializing the agent. Please try again later.")
        return

    while True:
        try:
            user_input = input(f"\n[{current_agent.role}] User: ").strip()
            logger.info(f"User input: {user_input}")
            
            if user_input.lower() == 'exit':
                logger.info("User requested to exit")
                print("Thank you for using Dudoxx Swarm Starter. Goodbye!")
                break
            elif user_input.lower() == 'switch':
                new_role = input(f"Which agent would you like to switch to? ({', '.join(AGENT_ROLES.keys())}): ").strip()
                logger.info(f"User requested to switch to {new_role} agent")
                try:
                    current_agent = get_agent(new_role)
                    logger.info(f"Switched to {current_agent.role} agent")
                    print(f"Switched to {current_agent.role} agent.")
                except ValueError as e:
                    logger.warning(f"Failed to switch agent: {e}")
                    print(f"Error: {e}")
                continue

            response = current_agent.process_message(user_input)
            logger.info(f"Agent response: {response}")
            print(f"[{current_agent.role}] Agent: {response}")
        except Exception as e:
            logger.error(f"An error occurred during conversation: {e}")
            print("An error occurred. Please try again.")

if __name__ == "__main__":
    main()