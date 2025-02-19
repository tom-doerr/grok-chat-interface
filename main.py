import streamlit as st
import requests
import json
import os
from typing import Dict, Any

st.set_page_config(
    page_title="Grok Chat Interface",
    page_icon="🤖",
    layout="wide"
)

# Custom CSS for better styling
st.markdown("""
    <style>
    .stTextInput > div > div > input {
        background-color: #f0f2f6;
    }
    .api-response {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
        margin: 10px 0;
    }
    </style>
""", unsafe_allow_html=True)

def make_api_call(messages: list, temperature: float = 0, model: str = "grok-2-latest") -> Dict[str, Any]:
    """
    Make an API call to xAI's Grok model
    """
    api_key = os.getenv("XAI_API_KEY")
    if not api_key:
        raise Exception("XAI API key not found in environment variables")

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    payload = {
        "messages": messages,
        "model": model,
        "stream": False,
        "temperature": temperature
    }

    try:
        response = requests.post(
            "https://api.x.ai/v1/chat/completions",
            headers=headers,
            json=payload
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        if hasattr(e.response, 'json'):
            try:
                error_detail = e.response.json()
                raise Exception(f"API Error: {json.dumps(error_detail, indent=2)}")
            except json.JSONDecodeError:
                raise Exception(f"API Error: {str(e)}\nResponse: {e.response.text}")
        raise Exception(f"Request Error: {str(e)}")

def main():
    st.title("🤖 Grok Chat Interface")

    # Model selection
    model = st.text_input(
        "Model",
        value="grok-2-latest",
        help="The xAI model to use for chat completions"
    )

    # System message input
    system_message = st.text_area(
        "System Message (optional)",
        value="You are a helpful assistant.",
        help="This sets the behavior of the AI assistant"
    )

    # User message input
    user_message = st.text_area(
        "Your Message",
        help="Enter your message to Grok"
    )

    # Temperature slider
    temperature = st.slider(
        "Temperature",
        min_value=0.0,
        max_value=1.0,
        value=0.0,
        step=0.1,
        help="Higher values make the output more random, lower values make it more focused"
    )

    if st.button("Send Message", disabled=not user_message):
        try:
            with st.spinner("Waiting for response..."):
                messages = []
                if system_message:
                    messages.append({
                        "role": "system",
                        "content": system_message
                    })
                messages.append({
                    "role": "user",
                    "content": user_message
                })

                response = make_api_call(messages, temperature, model)

                # Display the response in a nice format
                st.markdown("### Response")
                st.markdown('<div class="api-response">', unsafe_allow_html=True)

                # Display the assistant's message
                if response.get("choices") and len(response["choices"]) > 0:
                    assistant_message = response["choices"][0]["message"]["content"]
                    st.write(assistant_message)

                # Display full API response in an expander
                with st.expander("View Full API Response"):
                    st.json(response)

                st.markdown('</div>', unsafe_allow_html=True)

        except Exception as e:
            st.error(f"Error occurred: {str(e)}")

    # Add usage instructions in an expander
    with st.expander("Usage Instructions"):
        st.markdown("""
        1. Optionally modify the model name (default: grok-2-latest)
        2. Optionally modify the system message to change the AI's behavior
        3. Enter your message in the message field
        4. Adjust the temperature if desired (0 for focused responses, higher for more creative ones)
        5. Click 'Send Message' to get a response
        """)

if __name__ == "__main__":
    main()