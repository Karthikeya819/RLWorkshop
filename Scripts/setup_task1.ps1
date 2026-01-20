
$WorkspaceName = "RL_Workshop"
$PythonInstallerUrl = "https://www.python.org/ftp/python/3.11.5/python-3.11.5-amd64.exe"
$PythonInstaller = "python_installer.exe"


function Check-Admin {
    $currentPrincipal = New-Object Security.Principal.WindowsPrincipal([Security.Principal.WindowsIdentity]::GetCurrent())
    if (-not $currentPrincipal.IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)) {
        Write-Warning "This script requires Administrator privileges to install software."
        Write-Host "Please right-click the script and select 'Run with PowerShell' -> 'Run as Administrator', or run from an Admin PowerShell."
        Start-Sleep -Seconds 5
        Exit
    }
}

function Install-Python {
    Write-Host "Checking Python installation..." -ForegroundColor Cyan
    try {
        $pyVersion = python --version 2>&1
        if ($pyVersion -match "Python 3") {
            Write-Host "Python is already installed: $pyVersion" -ForegroundColor Green
            return
        }
    } catch {
        # Python not found
    }

    Write-Host "Python not found. Downloading Python 3.11..." -ForegroundColor Yellow
    try {
        Invoke-WebRequest -Uri $PythonInstallerUrl -OutFile $PythonInstaller
    } catch {
        Write-Error "Failed to download Python. Please install manually."
        return
    }
    Write-Host "Installing Python..." -ForegroundColor Yellow
    Start-Process -FilePath $PythonInstaller -ArgumentList "/quiet InstallAllUsers=1 PrependPath=1" -Wait
    Remove-Item $PythonInstaller
    
    $env:Path = [System.Environment]::GetEnvironmentVariable("Path","Machine") + ";" + [System.Environment]::GetEnvironmentVariable("Path","User")
    Write-Host "Python installed." -ForegroundColor Green
}

# --- Main Execution ---

Clear-Host
Write-Host "==========================================" -ForegroundColor Magenta
Write-Host "   Project MANAS RL Workshop - Task 1     " -ForegroundColor Magenta
Write-Host "==========================================" -ForegroundColor Magenta

Check-Admin

Install-Python

Write-Host "Installing Python Dependencies..." -ForegroundColor Cyan
python -m pip install --upgrade pip

$Dependencies = @("numpy", "pygame", "cbor2", "pyzmq", "coppeliasim-zmqremoteapi-client")
foreach ($dep in $Dependencies) {
    Write-Host "Installing $dep..."
    python -m pip install $dep
}

Write-Host "==========================================" -ForegroundColor Green
Write-Host "           Task 1 Setup Complete!         " -ForegroundColor Green
Write-Host "==========================================" -ForegroundColor Green
