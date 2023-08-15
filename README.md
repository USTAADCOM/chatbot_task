# Internship-Tasks (Real Time ChatBot)
ChatBot project is desigend where user can communicate with the Chatbot in real time.

## Setup
  
  clone project
  ```code
  git clone https://github.com/USTAADCOM/chatbot_task.git
  cd chatbot_task
  pip install -r requirements.txt
  ```
## Model
  Download Model Link below

  [Large Model](https://drive.google.com/file/d/157cGLz6s94la0G8bdzxxTOo3D7ckHB1w/view?usp=sharing) 

  [Small Model](https://drive.google.com/file/d/1ZGcM9Zz5O8BuYda87tTHSMtOPC5kzi5g/view?usp=sharing)

  Copy Model in chatbot_app repo
## Project Structure

```bash
 chatbot_task
 │  chatot model small.rar
 │   model_GPT2.pkl
 │   model_GPT2_small.pkl
 │   README.md
 │   requirements.txt
 │   server.py
 │   tokenizer_GPT2.pkl
 │   tokenizer_GPT2_small.pkl
 │
 └───chatapp
    │   events.py
    │   extensions.py
    │   module_chat.py
    │   routes.py
    │   __init__.py
    │
    ├───static
    │       style.css
    │
    ├───templates
    │       chat.html
    │       index.html
```

## run ChatBot 
```code
python server.py
```
______________________________________
## run ChatBot on Google Colab
ChatBot_task.ipynb file on colab 