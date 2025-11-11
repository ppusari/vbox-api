#!/bin/bash

# 가상환경 활성화
source venv/bin/activate

# 1️⃣ 기존 FastAPI 프로세스 종료
PID=$(ps -ef | grep "uvicorn app.main:app" | grep -v grep | awk '{print $2}')
if [ ! -z "$PID" ]; then
    echo "기존 FastAPI 서버 PID=$PID 종료"
    kill $PID
    sleep 1
fi

# 2️⃣ FastAPI 서버 실행
nohup uvicorn app.main:app --host 0.0.0.0 --port 20001 > vbox-api.log 2>&1 &
echo "FastAPI 서버 시작됨"


