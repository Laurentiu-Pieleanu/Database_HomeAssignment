# Database_HomeAssignment

# Setup Instructions

1. Clone the Github repository using URL link in the Github Desktop
2. Open the cloned folder inside VS Code
3. Creating and running the virtual environment
    python -m venv env
    env\Scripts\activate
4. Changed Get-ExecutionPolicy to RemoteSigned in order to run the virtual environment
5. Installing the dependencies
    pip install fastapi
    pip install uvicorn
    pip install motor
    pip install pydantic
    pip install python-dotenv
    pip install requests
6. Creating txt file with the dependencies verisons
    pip freeze > requirements.txt
7. Installed pip install python-multipart in order to run the FastAPI
8. Command used to run the FastAPI : uvicorn main:app --reload