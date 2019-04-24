param (
    [string]$WorkingDir = "$PWD"
)

$EnvDir = "env"
$EnvName = "dev"
$FullEnvPath = "$WorkingDir/$EnvDir/$EnvName"

# Check to see if we have this environment set up already
if (!(Test-Path $FullEnvPath)) {
    Write-Host "Environment not found, doing first-time setup..."

    # Create the virtual environment
    python -m venv $FullEnvPath
}

# Activate the environment
& "$FullEnvPath/Scripts/Activate.ps1"

# Update pip
python -m pip install --upgrade pip

# Install non-package dependencies
pip install pip-autoremove

# Install dependency packages
pip install -e .["$EnvName"]