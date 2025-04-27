#!/bin/bash

# filepath: ./set_env_from_file.sh

# Check if .env file exists
ENV_FILE=".env"
if [[ ! -f "$ENV_FILE" ]]; then
  echo "Error: .env file not found in the current directory."
  exit 1
fi

# Export each variable from the .env file
while IFS='=' read -r key value; do
  # Skip empty lines and comments
  if [[ -z "$key" || "$key" == \#* ]]; then
    continue
  fi

  # Remove any surrounding quotes from the value
  value=$(echo "$value" | sed -e 's/^"//' -e 's/"$//' -e "s/^'//" -e "s/'$//")

  # Export the variable
  export "$key=$value"
  echo "Exported: $key=$value"
done < "$ENV_FILE"

echo "Environment variables set successfully."