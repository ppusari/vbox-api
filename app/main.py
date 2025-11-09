import os
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException, Form
import subprocess
from fastapi.middleware.cors import CORSMiddleware

load_dotenv()  # .env 파일 읽기

app = FastAPI(title="VirtualBox REST API")

# CORS 허용
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


# 환경변수에서 관리자 계정 정보 가져오기
ADMIN_USER = os.getenv("ADMIN_USER", "admin")
ADMIN_PASS = os.getenv("ADMIN_PASS", "password")

@app.post("/login")
def login(username: str = Form(...), password: str = Form(...)):
    if username == ADMIN_USER and password == ADMIN_PASS:
        return {"success": True, "token": "fake-jwt-token"}
    raise HTTPException(status_code=401, detail="Invalid credentials")


# VM 이름 자동 조회
def list_all_vms():
    try:
        result = subprocess.run(
            "VBoxManage list vms",
            shell=True,
            capture_output=True,
            text=True,
        )
        vms = []
        for line in result.stdout.strip().splitlines():
            # "h1_winBase" {UUID} 형태
            if line:
                name = line.split('"')[1]
                vms.append(name)
        return vms
    except Exception as e:
        return []

# 특정 VM 상태 조회
def get_vm_status(vm_name):
    try:
        result = subprocess.run(
            f'VBoxManage showvminfo "{vm_name}" --machinereadable | grep -E "^VMState="',
            shell=True,
            capture_output=True,
            text=True,
        )
        state = result.stdout.strip().split('=')[1].replace('"','') if result.stdout else "unknown"
        return {"name": vm_name, "state": state}
    except Exception as e:
        return {"name": vm_name, "state": "error", "error": str(e)}

# VM 시작
def start_vm(vm_name):
    subprocess.run(f'VBoxManage startvm "{vm_name}" --type headless', shell=True)
    return {"name": vm_name, "action": "start"}

# VM 중지
def stop_vm(vm_name):
    subprocess.run(f'VBoxManage controlvm "{vm_name}" savestate', shell=True)
    return {"name": vm_name, "action": "stop"}

# 전체 VM 상태 조회
@app.get("/vms")
def list_vms():
    vms = list_all_vms()
    return [get_vm_status(vm) for vm in vms]

# 특정 VM 상태
@app.get("/vms/{vm_name}")
def vm_status(vm_name: str):
    if vm_name not in list_all_vms():
        raise HTTPException(status_code=404, detail="VM not found")
    return get_vm_status(vm_name)

# VM 시작
@app.post("/vms/{vm_name}/start")
def vm_start(vm_name: str):
    if vm_name not in list_all_vms():
        raise HTTPException(status_code=404, detail="VM not found")
    return start_vm(vm_name)

# VM 중지
@app.post("/vms/{vm_name}/stop")
def vm_stop(vm_name: str):
    if vm_name not in list_all_vms():
        raise HTTPException(status_code=404, detail="VM not found")
    return stop_vm(vm_name)

