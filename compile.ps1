# Set the path to PyInstaller
$pyInstallerPath = "C:\Users\total\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\localcache\local-packages\Python312\Scripts\pyinstaller.exe"

# Ask for the script name
$scriptName = ".\_qualityHunterLauncher"

# Run PyInstaller
& $pyInstallerPath --onefile "$scriptName.pyw"

# Check if the .exe file already exists in the root directory and delete it if it does
$exePath = ".\$scriptName.exe"
if (Test-Path $exePath) {
    Remove-Item $exePath
}

# Move the new .exe file to the root directory and delete the dist folder
Move-Item ".\dist\$scriptName.exe" -Destination $exePath
Remove-Item -Recurse -Force .\dist

# Remove the build directory and .spec file
Remove-Item -Recurse -Force .\build
Remove-Item -Force "$scriptName.spec"

Write-Host "compilation successful and cleanup complete!"