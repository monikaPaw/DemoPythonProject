@echo off
pytest -s -v -m "smoke" --html=./Reports/SmokeTestReport.html testCases/ --browser chrome

pause
