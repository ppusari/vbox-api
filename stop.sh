#!/bin/bash
# FastAPI 서버 종료 (uvicorn)

# uvicorn 프로세스 PID 찾기
PID=$(ps -ef | grep "[u]vicorn app.main:app" | awk '{print $2}')

if [ -z "$PID" ]; then
    echo "FastAPI 서버가 실행 중이 아닙니다."
else
    echo "FastAPI 서버 PID=$PID 종료"
    kill $PID
fi

