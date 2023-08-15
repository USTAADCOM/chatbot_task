# Internship-Tasks (Real Time ChatBot)
ChatBot project is desigend where user can communicate with the Chatbot in real time.

## Setup
  
  clone project from repo
  [chatbot UI](https://github.com/USTAADCOM/chatbot_task.git)
  ```code
  git clone https://github.com/USTAADCOM/chatbot_task.git
  cd chatbot_task
  pip install -r requirements.txt
  ```
  Download Model From
  [Model](https://drive.google.com/file/d/157cGLz6s94la0G8bdzxxTOo3D7ckHB1w/view?usp=sharing) 

  Copy Model in chatbot_app repo
## Project Structure

```bash
│   model_GPT2.pkl
│   README.md
│   requirements.txt
│   server.py
│   tokenizer_GPT2.pkl
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
    │
    └───__pycache__
            events.cpython-310.pyc
            extensions.cpython-310.pyc
            routes.cpython-310.pyc
            __init__.cpython-310.pyc
```

## run ChatBot 
```code
python server.py
```
______________________________________
## ## run ChatBot using on Google Colab
ChatBot_task.ipynb file on colab 