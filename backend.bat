@echo off
cd /d E:\temp\AI-detector-for-admissions-essays-1\backend
call ..\.venv\Scripts\activate.bat
python -m uvicorn app.main:app --reload
pause