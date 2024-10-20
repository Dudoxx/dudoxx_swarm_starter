# Dudoxx Swarm Starter

Dudoxx Swarm Starter is a project that orchestrates agents using routines and handoffs with large language models (LLMs). It provides a flexible framework for creating conversational agents with different roles and capabilities.

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/Dudoxx/dudoxx_swarm_starter.git
   cd dudoxx_swarm_starter
   ```

2. Create and activate a Conda environment:
   ```
   conda create --name dudoxx-swarm python=3.9
   conda activate dudoxx-swarm
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the project root directory with the following content:
   ```
   OPENAI_API_KEY=your-api-key-here
   OPENAI_BASE_URL=https://api.openai.com/v1
   OPENAI_MODEL=gpt-4
   ```
   Replace `your-api-key-here` with your actual OpenAI API key.

## Usage

To run the Dudoxx Swarm Starter:

```
python -m dudoxx_swarm_starter
```

Follow the on-screen prompts to interact with the agents. You can switch between different agent roles by typing 'switch' during the conversation.

## Running Tests

To run the unit tests:

```
pytest
```

This will run all the tests in the `tests` directory.

## Project Structure

```
dudoxx_swarm_starter/
├── agents.py
├── api_client.py
├── config.py
├── logger.py
├── main.py
├── __init__.py
├── __main__.py
├── .env
├── requirements.txt
└── tests/
    ├── test_agents.py
    ├── test_api_client.py
    └── test_main.py
```

- `agents.py`: Defines the Agent class and agent-related functions.
- `api_client.py`: Handles the OpenAI API client initialization.
- `config.py`: Contains configuration variables for the project.
- `logger.py`: Sets up logging for the application.
- `main.py`: The main entry point for the application.
- `__init__.py`: Makes the directory a Python package.
- `__main__.py`: Allows the package to be run as a script.
- `.env`: Contains environment variables (not tracked by git).
- `tests/`: Contains unit tests for the project.

## Contributing

Contributions to Dudoxx Swarm Starter are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Write your code and tests.
4. Ensure all tests pass by running `pytest`.
5. Submit a pull request with a clear description of your changes.

## License

[MIT License](https://opensource.org/licenses/MIT)

Copyright (c) 2024 Dudoxx UG

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.