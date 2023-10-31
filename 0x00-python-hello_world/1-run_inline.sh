#!/bin/bash

# Check if the $PYCODE environment variable is set
if [ -z "$PYCODE" ]; then
  echo "Error: The PYFILE environment variable is not set."
  exit 1
fi

# Run the Python code
python3 -c "$PYCODE"

