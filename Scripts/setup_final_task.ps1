$CoppeliaSimUrl = "https://downloads.coppeliarobotics.com/V4_10_0_rev0/CoppeliaSim_Edu_V4_10_0_rev0_Setup.exe"
$CoppeliaSimInstaller = "CoppeliaSim_Setup.exe"


function Check-Admin {
    $currentPrincipal = New-Object Security.Principal.WindowsPrincipal([Security.Principal.WindowsIdentity]::GetCurrent())
    if (-not $currentPrincipal.IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)) {
        Write-Warning "This script requires Administrator privileges to install software."
        Write-Host "Please right-click the script and select 'Run with PowerShell' -> 'Run as Administrator', or run from an Admin PowerShell."
        Start-Sleep -Seconds 5
        Exit
    }
}

function Install-CoppeliaSim {
    Write-Host "Checking CoppeliaSim installation..." -ForegroundColor Cyan
    if (Test-Path "$env:ProgramFiles\CoppeliaRobotics") {
        Write-Host "CoppeliaSim folder found in Program Files. Skipping installation." -ForegroundColor Green
        return
    }

    Write-Host "CoppeliaSim not found. Downloading Installer (approx 200MB+)..." -ForegroundColor Yellow
    try {
        Invoke-WebRequest -Uri $CoppeliaSimUrl -OutFile $CoppeliaSimInstaller
    } catch {
        Write-Error "Failed to download CoppeliaSim. The link may be outdated. Please download manually from https://www.coppeliarobotics.com/downloads"
        return
    }

    Write-Host "Installing CoppeliaSim..." -ForegroundColor Yellow
    Start-Process -FilePath $CoppeliaSimInstaller -ArgumentList "/S" -Wait
    Remove-Item $CoppeliaSimInstaller
    Write-Host "CoppeliaSim installed." -ForegroundColor Green
}

# --- Main Execution ---

Clear-Host
Write-Host "==========================================" -ForegroundColor Magenta
Write-Host "   Project MANAS RL Workshop - Final Task " -ForegroundColor Magenta
Write-Host "==========================================" -ForegroundColor Magenta

Check-Admin

Install-CoppeliaSim

Write-Host "==========================================" -ForegroundColor Green
Write-Host "           Final Task Setup Complete!     " -ForegroundColor Green
Write-Host "==========================================" -ForegroundColor Green