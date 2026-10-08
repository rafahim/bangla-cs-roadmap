$ErrorActionPreference = "Stop"
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$Launcher = Get-Command py -ErrorAction SilentlyContinue
if ($Launcher) {
    & py -3 (Join-Path $ScriptDir "generate_repo.py")
} else {
    $Launcher = Get-Command python -ErrorAction SilentlyContinue
    if (-not $Launcher) { throw "Python 3 was not found. Install Python 3 and rerun setup.ps1." }
    & python (Join-Path $ScriptDir "generate_repo.py")
}
if ($LASTEXITCODE -ne 0) { throw "Repository generation failed with exit code $LASTEXITCODE" }
Write-Host "Regenerated all repository files and bangla-cs-roadmap.zip."
