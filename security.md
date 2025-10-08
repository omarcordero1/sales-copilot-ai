# Security Guide for Sales Copilot AI

## 🔒 API Key Security

### Never Do This:
- ❌ Commit API keys to GitHub
- ❌ Hardcode keys in source files
- ❌ Share keys in public repositories

### Safe Practices:
- ✅ Use environment variables
- ✅ Use Streamlit Secrets for deployment
- ✅ Use .env files for local development (add to .gitignore)
- ✅ Rotate keys regularly

## 🛡️ Local Development Setup

### Option 1: Environment Variables
```bash
# Set environment variable
export OPENAI_API_KEY="your_actual_api_key_here"

# Verify it's set
echo $OPENAI_API_KEY