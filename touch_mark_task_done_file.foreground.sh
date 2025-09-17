#!/bin/bash

# Sleep for 900 seconds (15 minutes)
sleep 900

# Get the directory of the current script
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

# File path for MARK_TASK_DONE
DONE_FILE="$SCRIPT_DIR/MARK_TASK_DONE"

# "touch" the file (create if not exists, update timestamp if exists)
touch "$DONE_FILE"

echo "Created or updated: $DONE_FILE"
