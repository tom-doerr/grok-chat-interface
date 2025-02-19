# Grok Chat Interface

A Streamlit-based chat interface for interacting with xAI's Grok model.

## Features

- Clean and intuitive chat interface
- Support for system messages to control assistant behavior
- Temperature control for response randomness
- Full API response viewing capability
- Model selection support

## Setup

1. Clone this repository
2. Install dependencies:
```bash
pip install -r requirements.txt
```
3. Set up your environment variables:
   - Create a `.env` file or set up environment variables
   - Add your xAI API key: `XAI_API_KEY=your-key-here`

## Usage

1. Run the Streamlit app:
```bash
streamlit run main.py
```
2. The interface will be available at `http://localhost:5000`

## Configuration

- Model: Choose between available Grok models (default: grok-2-latest)
- System Message: Set the behavior of the AI assistant
- Temperature: Control response randomness (0 = focused, 1 = creative)

## Security

- API keys are handled through environment variables
- No sensitive data is stored in the code
- API keys are only used in memory during requests

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request
