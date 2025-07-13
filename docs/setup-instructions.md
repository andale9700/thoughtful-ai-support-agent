# Setup Instructions

## Environment Configuration

Since .env files are blocked, you'll need to set up your environment variables manually:

### Option 1: Create .env file manually
Create a `.env` file in the project root with:
```
OPENAI_API_KEY=your-openai-api-key-here
```

### Option 2: Set environment variable in Replit
1. Go to your Replit project
2. Click on "Secrets" in the left sidebar
3. Add a new secret:
   - Key: `OPENAI_API_KEY`
   - Value: Your OpenAI API key

### Option 3: Set environment variable in terminal
```bash
export OPENAI_API_KEY=your-openai-api-key-here
```

## Getting an OpenAI API Key

1. Go to [OpenAI API](https://platform.openai.com/api-keys)
2. Sign up or log in
3. Create a new API key
4. Copy the key and use it in your environment setup

## Running the Application

```bash
streamlit run main.py
```

The app will be available at `http://localhost:8501` 