#!/bin/bash
# FastAPI 서버 상태 확인 (uvicorn)

# uvicorn 프로세스 PID 찾기
PID=$(ps -ef | grep "[u]vicorn app.main:app" | awk '{print $2}')

if [ -z "$PID" ]; then
    echo "❌ FastAPI 서버가 실행 중이 아닙니다."
else
    echo "✅ FastAPI 서버가 실행 중입니다. PID=$PID"
    # 실행 포트와 로그 최근 내용도 간단히 표시
    PORT=$(netstat -tuln 2>/dev/null | grep ":2000 " | awk '{print $4}' | awk -F: '{print $NF}')
    if [ ! -z "$PORT" ]; then
        echo "📡 포트: $PORT"
    fi
    echo "📄 최근 로그 (vbox-api.log tail 5)"
    tail -n 5 vbox-api.log
fi

