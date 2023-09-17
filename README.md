Commands
Virtual Environment Creation
python  -m venv venv

Activate Virtual Env in gitbash
source venv/Scripts/activate

Running the fastAPI server

python -m uvicorn main:app --reload --host 0.0.0.0 --port 8000 --workers 2
