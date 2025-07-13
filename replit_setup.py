#!/usr/bin/env python3
"""
Fixed setup script for Replit deployment with Python 3.12 compatibility
Run this after uploading files to install dependencies
"""

import subprocess
import sys
import os

def install_requirements():
    """Install required packages with Python 3.12 compatibility"""
    print("Installing requirements for Python 3.12...")
    
    # Install packages one by one to handle potential issues
    packages = [
        "streamlit>=1.28.0",
        "openai>=1.95.0", 
        "python-dotenv>=1.0.0",
        "thefuzz>=0.19.0",
        "pytest>=7.4.0",
    ]
    
    # Install basic packages first
    for package in packages:
        try:
            print(f"Installing {package}...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", package, "--quiet"])
            print(f"✅ {package} installed successfully!")
        except subprocess.CalledProcessError as e:
            print(f"⚠️  Warning: Could not install {package}: {e}")
    
    # Install ML packages separately (they might take longer)
    ml_packages = [
        "numpy>=1.26.0",
        "sentence-transformers>=2.3.0"
    ]
    
    for package in ml_packages:
        try:
            print(f"Installing {package} (this may take a moment)...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", package, "--quiet", "--no-build-isolation"])
            print(f"✅ {package} installed successfully!")
        except subprocess.CalledProcessError as e:
            print(f"⚠️  Warning: Could not install {package}: {e}")
            print("Trying alternative installation method...")
            try:
                subprocess.check_call([sys.executable, "-m", "pip", "install", package, "--no-deps", "--quiet"])
                print(f"✅ {package} installed with --no-deps!")
            except subprocess.CalledProcessError:
                print(f"❌ Failed to install {package}")
    
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
        from sentence_transformers import SentenceTransformer
        print("✅ Sentence Transformers import successful")
    except ImportError as e:
        print(f"⚠️  Sentence Transformers import failed: {e}")
        print("   The app may still work but RAG matching might have issues")
    
    return True

def test_app_modules():
    """Test if our app modules can be imported"""
    print("\nTesting app modules...")
    
    try:
        # Test if our main modules can be imported
        import data
        print("✅ data.py import successful")
        
        import config
        print("✅ config.py import successful")
        
        import llm_service
        print("✅ llm_service.py import successful")
        
        # Test question_matcher - this might fail if sentence-transformers isn't working
        try:
            import question_matcher
            print("✅ question_matcher.py import successful")
        except ImportError as e:
            print(f"⚠️  question_matcher.py import failed: {e}")
            print("   You may need to manually install sentence-transformers")
        
        return True
    except Exception as e:
        print(f"❌ App module test failed: {e}")
        return False

def main():
    """Main setup function"""
    print("🚀 Setting up Thoughtful AI Project on Replit (Python 3.12)...")
    print("=" * 60)
    
    # Check Python version
    print(f"Python version: {sys.version}")
    
    if install_requirements():
        create_env_template()
        
        if test_imports() and test_app_modules():
            print("\n🎉 Setup completed successfully!")
            print("\n📋 Next steps:")
            print("1. Add your OpenAI API key to the .env file")
            print("2. Run: streamlit run main.py")
            print("3. Your app should be running!")
            print("\n💡 If you encounter issues with sentence-transformers:")
            print("   Try: pip install sentence-transformers --no-build-isolation")
        else:
            print("\n⚠️  Setup completed with some issues")
            print("💡 Try running: pip install sentence-transformers --no-build-isolation")
            print("   Then test again with: python -c 'from sentence_transformers import SentenceTransformer'")
    else:
        print("\n❌ Setup failed during package installation")

if __name__ == "__main__":
    main() 