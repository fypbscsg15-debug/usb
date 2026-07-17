@echo off
title SPSS Backend Server
echo =============================================================
echo          Smart Pharmacist Support System (SPSS)
echo                  Backend Server Setup
echo =============================================================
echo.
echo Starting FastAPI Backend on port 8000...
echo (Includes ML Similarity Models and OCR API Processors)
echo.
cd /d "%~dp0backend"
venv\Scripts\python.exe -m uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
pause
