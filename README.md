# A Travel Weather API

A Python weather API.

## Run in a Codespace
Click the button below to create a codespace with the repository

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://github.com/codespaces/new?hide_repo_select=true&ref=main&repo=775546635)

## Run locally
Clone the repository and navigate to the project root directory

Run the command below to set up the virtual environment
```bash
python3 -m venv .venv
```

Set the source of the virtual environment
```bash
source .venv/bin/activate
```

Install the dependencies
```bash
pip install -r requirements.txt
```

Run the application with uvicorn
```bash
uvicorn --host 0.0.0.0 webapp.main:app
```

## Deploy to Azure with the Azure Developer CLI (azd)
### Pre-requisites:
- AZD CLI
- Azure Subscription
- Docker Desktop

Install the Azure Developer CLI - follow the instructions [here](https://learn.microsoft.com/azure/developer/azure-developer-cli/install-azd?tabs=winget-windows%2Cbrew-mac%2Cscript-linux&pivots=os-mac#pre-requisites). It is only a few commands.

Once you have all the pre-requisites, navigate to the root project directory and begin the process of deployment with azd.

The first command to run is logging into your Azure account
```bash
azd auth login
```

Next, run the command below to deploy the application to Azure
```bash
azd up
```

## Trademarks

This project may contain trademarks or logos for projects, products, or services. Authorized use of Microsoft
trademarks or logos is subject to and must follow
[Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general).
Use of Microsoft trademarks or logos in modified versions of this project must not cause confusion or imply Microsoft sponsorship.
Any use of third-party trademarks or logos are subject to those third-party's policies.
