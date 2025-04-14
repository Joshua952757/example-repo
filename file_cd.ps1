# Creating three new folders
New-Item -ItemType Directory -Name "FolderA"
New-Item -ItemType Directory -Name "FolderB"
New-Item -ItemType Directory -Name "FolderC"

# Navigate into FolderA
Set-Location -Path "FolderA"

# Creating three subfolders inside FolderA
New-Item -ItemType Directory -Name "Sub1"
New-Item -ItemType Directory -Name "Sub2"
New-Item -ItemType Directory -Name "Sub3"

# Going back to the parent directory
Set-Location ..

# Removing two folders (FolderB and FolderC)
Remove-Item -Recurse -Force "FolderB"
Remove-Item -Recurse -Force "FolderC"
