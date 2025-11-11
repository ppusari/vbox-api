# 🖥️ VBox API Server (FastAPI)

VirtualBox VM을 원격에서 제어할 수 있는 간단한 REST API 서버입니다.  
React UI(`vbox-ui`)와 연동하여 웹에서 VM을 시작하거나 중지할 수 있습니다.

---

## 🚀 Features
- VirtualBox VM 목록 조회 (`/vms`)
- VM 시작 (`/vms/{name}/start`)
- VM 중지 (`/vms/{name}/stop`)
- 로그인 API (`/login`)
- `.env`로 관리자 계정 설정 가능
- server port: 20001

---

## ⚙️ Installation

```bash
# Clone repository
git clone https://github.com/ppusari/vbox-api.git
cd vbox-api

# 가상환경 생성 및 활성화
python3 -m venv venv
source venv/bin/activate

# 패키지 설치
pip install -r requirements.txt

# 환경변수 설정 (.env 파일 생성)
echo "ADMIN_USER=admin" >> .env
echo "ADMIN_PASS=admin123" >> .env
```

##  서버 구동
- 실행: bash start.sh
- 중지: bash stop.sh
- 상태확인: bash status.sh
