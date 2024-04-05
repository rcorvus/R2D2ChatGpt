# R2-D2 Chat

Ask R2-D2 about anything related to Star Wars or how he was created. Powered by Python, Flask, and ChatGPT.

![image](https://github.com/rcorvus/R2D2ChatGpt/assets/5025458/1e75ba1b-f30a-48fe-91cd-d504724173d6)

## Add Environment Variable to your computer and reboot
``` OPENAI_API_KEY=my_openai_api_key ```

## Create a Dockerfile file (the .gitignore file keeps those out of source control)
Should look like this (be sure to include your own OPENAI_API_KEY)

```
# syntax=docker/dockerfile:1

FROM python:3.12

ENV OPENAI_API_KEY="my_openai_api_key"

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 50505

ENTRYPOINT ["gunicorn", "app:app"]
```


## Installation

### Test your docker build
Start your docker app on your computer.

Build the docker image:
``` docker build -t r2d2chatgpt . ```

Run it locally:
``` docker run --detach --publish 5000:50505 r2d2chatgpt ```

In docker app, click on app and test that it runs correctly.

Deploy your app to Azure:
```
az webapp up --runtime PYTHON:3.12 --sku F1 --logs --name r2d2chatgpt --location westus
```

###NOTE: If you get an error like "Insufficient permissions to create a zip in current directory. Please re-run the command with administrator privileges":
That means you need to close Visual Studio before running the above command again :-)

Then go to:
``` http://r2d2chatgpt.azurewebsites.net ```


Locally or in a virtual env, use the package manager [pip](https://pip.pypa.io/en/stable/) to install the libraries listed in requirements.txt:

For example:
```
pip install -r requirements.txt
```



## License

[MIT](https://choosealicense.com/licenses/mit/)
