#!/usr/bin/env python3
"""
Quick setup script for Replit deployment
Run this after uploading files to install dependencies
"""

import subprocess
import sys

def install_requirements():
    """Install required packages"""
    print("Installing requirements...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Requirements installed successfully!")
    except subprocess.CalledProcessError:
        print("❌ Error installing requirements")
        return False
    return True

def create_env_template():
    """Create .env template file"""
    env_content = """# Add your OpenAI API key here
OPENAI_API_KEY=your-openai-api-key-here
"""
    
    try:
        with open(".env", "w") as f:
            f.write(env_content)
        print("✅ .env template created - add your OpenAI API key!")
    except Exception as e:
        print(f"❌ Error creating .env file: {e}")

def test_setup():
    """Test if everything is working"""
    print("\nTesting setup...")
    try:
        from question_matcher import find_best_match
        result = find_best_match("What does EVA do?")
        if result:
            print("✅ RAG matching works!")
        else:
            print("⚠️  RAG matching returns no results (this is normal)")
        
        print("✅ All imports successful!")
        return True
    except Exception as e:
        print(f"❌ Setup test failed: {e}")
        return False

def main():
    """Main setup function"""
    print("🚀 Setting up Thoughtful AI Project on Replit...")
    print("=" * 50)
    
    if install_requirements():
        create_env_template()
        if test_setup():
            print("\n🎉 Setup complete!")
            print("\n📋 Next steps:")
            print("1. Add your OpenAI API key to the .env file")
            print("2. Run: streamlit run main.py")
            print("3. Your app should be running!")
        else:
            print("\n⚠️  Setup completed with warnings")
    else:
        print("\n❌ Setup failed")

if __name__ == "__main__":
    main() 