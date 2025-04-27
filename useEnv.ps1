$envFilePath = ".env"

# Check if the file exists
if (Test-Path $envFilePath) {
    Get-Content $envFilePath | ForEach-Object {
        # Split each line into key and value
        $line = $_ -split '='
        if ($line.Length -eq 2) {
            $key = $line[0].Trim()
            $value = $line[1].Trim()
            
            # Set the environment variable
            [System.Environment]::SetEnvironmentVariable($key, $value, [System.EnvironmentVariableTarget]::Process)
        }
    }
    Write-Host "Environment variables loaded successfully."
} else {
    Write-Host "The .env file was not found at $envFilePath."
}