# If "new_folder" exists, create "if_folder"
if (Test-Path "new_folder") {
    New-Item -ItemType Directory -Name "if_folder"
}

# Checking if "if_folder" exists
if (Test-Path "if_folder") {
    # If it exists, create "hyperionDev"
    New-Item -ItemType Directory -Name "hyperionDev"
} else {
    # If it does not exist, creating "new-projects"
    New-Item -ItemType Directory -Name "new-projects"
}

