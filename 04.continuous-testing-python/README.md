Converted Node.js lab to Python (FastAPI + pytest)

Structure:
lab/
  src/
    app.py
    dbclient.py
    controllers/user.py
    routes/user.py
  tests/
    test_user_controller.py
    test_user_api.py

Run tests:
1. Create a venv and install:
   python -m venv venv
   source venv/bin/activate  # or venv\Scripts\activate on Windows
   pip install -r requirements.txt
2. Run tests:
   pytest -q

Run the app:
   uvicorn lab.src.app:app --reload