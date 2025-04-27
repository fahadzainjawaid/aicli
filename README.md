#Generative AI Command-Line-Interface (AI CLI)
This little repository allows us to use Azure Open AI and AWS Bedrock and perform chat interactions using a commmand-line utility.

!!Keys and Model required in Azure or AWS.

##Interactive mode
`bedrockcli.py interactive`
This method will allow us to interactively provide prompt and get a response using AWS Bedrock

`aiocli.py interactive`
This method will allow us to interactively provide prompt and get a response using Azure Open AI GPT4 mode

##Inline Model
`bedrockcli.py inline <prompt>`
This method will allow us to programatically provide prompt and get a response in line. This is helpful because we can now include this in a Powershell or Bash script for volume interaction from another source.

`aiocli.py inline <prompt>`
This method will allow us to programatically provide prompt and get a response in line. This is helpful because we can now include this in a Powershell or Bash script for volume interaction from another source.





