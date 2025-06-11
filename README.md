# AnimalApp: Azure Functions Python PoC

This project demonstrates a simple Azure Functions Python app for managing animals, integrated with GitHub Copilot and a CI/CD pipeline using GitHub Actions.

## Features
- List all animals (GET)
- Add a new animal (POST)

## Endpoints
- **GET /api/AnimalFunction**: List all animals
- **POST /api/AnimalFunction**: Add a new animal (JSON body: `{ "animal": "Lion" }`)

## Local Development
1. Install requirements:
   ```powershell
   pip install -r requirements.txt
   ```
2. Run locally:
   ```powershell
   func start
   ```

## CI/CD Pipeline
- On push to `main`, GitHub Actions will build and deploy to Azure Function App: `func-copilot-pavan-1`.

## Setup
1. Fork or clone this repo.
2. Set up your Azure Function App and get deployment credentials.
3. Add the following secrets to your GitHub repo:
   - `AZURE_FUNCTIONAPP_PUBLISH_PROFILE` (from Azure Portal > Function App > Get Publish Profile)

## References
- [Azure Functions Python](https://docs.microsoft.com/azure/azure-functions/functions-reference-python)
- [GitHub Actions for Azure](https://github.com/Azure/actions)
