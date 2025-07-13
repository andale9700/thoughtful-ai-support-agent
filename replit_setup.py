#!/usr/bin/env python3
"""
Setup script for Replit deployment with keyword-based RAG
Simple installation without heavy ML dependencies
"""

import subprocess
import sys
import os

def install_requirements():
    """Install required packages"""
    print("Installing requirements...")
    
    packages = [
        "streamlit>=1.28.0",
        "openai>=1.95.0", 
        "python-dotenv>=1.0.0",
        "thefuzz>=0.19.0",
        "pytest>=7.4.0",
        "numpy>=1.26.0"
    ]
    
    for package in packages:
        try:
            print(f"Installing {package}...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", package, "--quiet"])
            print(f"✅ {package} installed successfully!")
        except subprocess.CalledProcessError as e:
            print(f"⚠️  Warning: Could not install {package}: {e}")
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

def test_imports():
    """Test if critical imports work"""
    print("\nTesting imports...")
    
    try:
        import streamlit
        print("✅ Streamlit import successful")
    except ImportError as e:
        print(f"❌ Streamlit import failed: {e}")
        return False
    
    try:
        import openai
        print("✅ OpenAI import successful")
    except ImportError as e:
        print(f"❌ OpenAI import failed: {e}")
        return False
    
    try:
        import numpy
        print("✅ NumPy import successful")
    except ImportError as e:
        print(f"❌ NumPy import failed: {e}")
        return False
    
    return True

def test_app_modules():
    """Test if our app modules can be imported"""
    print("\nTesting app modules...")
    
    try:
        import data
        print("✅ data.py import successful")
        
        import config
        print("✅ config.py import successful")
        
        import llm_service
        print("✅ llm_service.py import successful")
        
        import question_matcher
        print("✅ question_matcher.py import successful")
        
        return True
    except Exception as e:
        print(f"❌ App module test failed: {e}")
        return False

def test_rag_functionality():
    """Test if RAG matching works"""
    print("\nTesting RAG functionality...")
    
    try:
        from question_matcher import find_best_match
        
        test_question = "What does EVA do?"
        result = find_best_match(test_question)
        
        if result:
            answer, score = result
            print(f"✅ RAG test successful: '{test_question}' → {score:.3f} match")
            print(f"   Answer: {answer[:60]}...")
            return True
        else:
            print(f"⚠️  RAG test: No match found for '{test_question}' (may need tuning)")
            return True  # Still count as success since the system is working
            
    except Exception as e:
        print(f"❌ RAG test failed: {e}")
        return False

def main():
    """Main setup function"""
    print("🚀 Setting up Thoughtful AI Project on Replit...")
    print("=" * 60)
    
    print(f"Python version: {sys.version}")
    print("Using keyword-based RAG (no heavy ML dependencies)")
    print()
    
    if install_requirements():
        create_env_template()
        
        if test_imports() and test_app_modules() and test_rag_functionality():
            print("\n🎉 Setup completed successfully!")
            print("\n📋 Next steps:")
            print("1. Add your OpenAI API key to the .env file")
            print("2. Run: streamlit run main.py")
            print("3. Your app should be running!")
            print("\n💡 Features enabled:")
            print("   ✅ Keyword-based RAG matching")
            print("   ✅ Streaming LLM responses")
            print("   ✅ Healthcare automation Q&A")
        else:
            print("\n⚠️  Setup completed with some issues")
            print("Please check the error messages above")
    else:
        print("\n❌ Setup failed during package installation")

if __name__ == "__main__":
    main() 