git clone https://github.com/tom-doerr/grok-chat-interface.git
cd grok-chat-interface
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up your environment variables:
   - Create a `.env` file in the project root
   - Add your xAI API key: `XAI_API_KEY=your-key-here`
   - You can obtain an API key from xAI's developer portal

4. Run the Streamlit app:
```bash
streamlit run main.py