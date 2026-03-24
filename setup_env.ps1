$ErrorActionPreference = "Stop"

if (-not (Test-Path ".venv")) {
    python -m venv .venv
}

$python = Join-Path $PSScriptRoot ".venv\Scripts\python.exe"

& $python -m pip install --upgrade pip
& $python -m pip uninstall -y opencv-python
& $python -m pip install -r (Join-Path $PSScriptRoot "requirements.txt")
& $python (Join-Path $PSScriptRoot "check_env.py")
