# Python flask app

## Local run in Docker
1. docker build -t gptserver .
2. docker run -p 5000:5000 gptserver

## Run in Cloud
### 1. Push image into [Azure Container Registry](https://portal.azure.com/#@junnorgangmail.onmicrosoft.com/resource/subscriptions/765e1ed7-a890-4d1d-86a3-a7116c7c7250/resourcegroups/GPT/providers/Microsoft.ContainerRegistry/registries/gptbotacr/overview)
Run commands locally
```
docker build -t gptserver .
docker tag gptserver gptbotacr.azurecr.io/gptserver
az login # login with junnor.gan@gmail.com
az acr login --name gptbotacr
docker push gptbotacr.azurecr.io/gptserver
``` 

### Run it on Azure App Service
Here's the link of our [app service resource](https://portal.azure.com/#@junnorgangmail.onmicrosoft.com/resource/subscriptions/765e1ed7-a890-4d1d-86a3-a7116c7c7250/resourcegroups/GPT/providers/Microsoft.Web/sites/gpt-backend/appServices)

When you push the image into the acr, you should wait 2-3 minutes syncing this new image in our app service. 
You don't need to deploy app service manually.

### How to access your api
for example: http://gpt-backend.azurewebsites.net/testget
