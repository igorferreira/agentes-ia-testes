#!/bin/bash

# Set timestamp
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
BACKUP_DIR="bkp/$TIMESTAMP"

# Create backup directory
mkdir -p "$BACKUP_DIR"
echo "Created backup directory: $BACKUP_DIR"

# Folders to backup and clean
FOLDERS="conversations execucoes logs recordings results"

# Backup and clean each folder
for folder in $FOLDERS; do
    if [ -d "$folder" ]; then
        # Create backup folder
        mkdir -p "$BACKUP_DIR/$folder"
        
        # Copy files to backup
        cp -r "$folder"/* "$BACKUP_DIR/$folder"/ 2>/dev/null || true
        echo "Backed up $folder to $BACKUP_DIR/$folder"
        
        # Clean original folder
        rm -rf "$folder"/*
        echo "Cleaned $folder"
    else
        echo "Warning: Source directory not found: $folder"
    fi
done

echo "Backup completed: $BACKUP_DIR"