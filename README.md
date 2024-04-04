# R2-D2 Chat

Ask R2-D2 about anything related to Star Wars or how he was created. Powered by Python, Flask, and ChatGPT.

![image](https://github.com/rcorvus/R2D2ChatGpt/assets/5025458/1e75ba1b-f30a-48fe-91cd-d504724173d6)

## Use your api key
Create a .env file (the .gitignore file keeps those out of source control)
in the .env file add this line:

```
OPENAI_API_KEY="your_openai_api_key"
```


## Installation

```
az webapp up --runtime PYTHON:3.12 --sku F1 --logs --name r2d2chatgpt --location westus
```

Then go to:
``` http://r2d2chatgpt.azurewebsites.net ```


Locally or in a virtual env, use the package manager [pip](https://pip.pypa.io/en/stable/) to install the libraries listed in requirements.txt:

For example:
```
pip install -r requirements.txt
```



## License

[MIT](https://choosealicense.com/licenses/mit/)
