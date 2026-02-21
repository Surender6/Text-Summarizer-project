# 📝 Text Summarization using Transformers (NLP)

An end-to-end Natural Language Processing (NLP) project that leverages Transformer-based models to generate concise summaries from long text.  
This repository demonstrates how to build, run, and deploy an abstractive text summarizer using state-of-the-art transformer models.

---

## 📌 Problem Statement

With the explosion of digital content — news articles, research papers, long documents — reading and understanding long text has become time-consuming.

Text summarization automates this task by generating a short, meaningful representation of long text while **preserving key information** and context. This is widely used in:

- Automatic report summarization  
- News aggregators  
- Research summarization  
- Document understanding systems

This project builds a **transformer-based abstractive summarizer** that produces fluent summaries from input text.

---

## 🚀 Project Overview

This project uses Transformer models (e.g., BART, T5, PEGASUS — depending on implementation) to perform **abstractive summarization** — meaning it generates summaries in its own words rather than extracting sentences verbatim. :contentReference[oaicite:0]{index=0}

Unlike extractive methods, abstractive approaches **better capture the essence of the text** and produce more natural summaries. :contentReference[oaicite:1]{index=1}

This repository includes:

✔ Data preprocessing  
✔ Transformer model integration using the `transformers` library  
✔ Summarization pipeline  
✔ Inference and evaluation  
✔ Optional deployment setup  

---

## 🛠️ Tech Stack

| Component | Technology |
|-----------|------------|
| Programming Language | Python |
| Machine Learning | Transformers (Hugging Face) |
| Models | BART / T5 / Pegasus (Transformer Seq2Seq) |
| Inference | Python Script / API |
| Deployment | Docker / Cloud Deployment |
| Environment | Virtualenv / Conda |

---

## 📂 Repository Structure
Text-Summarizer-project/
├── src/textsummarizer/ # Core summarization modules
├── texts/ # Sample text files for summarization
├── app.py # Application entry point
├── main.py # Main script for training / inference
├── params.yaml # Config and hyperparameters
├── requirements.txt # Dependency list
├── Dockerfile # (optional) Container config
├── README.md # (This file)
└── setup.py # Project installer


---

## 🔄 Workflow

### 1️⃣ Preprocessing

- Load text data
- Clean and normalize text
- Tokenize using the transformer tokenizer

---

### 2️⃣ Model Setup

A transformer model (e.g., BART / T5) is loaded using the Hugging Face library.  
The model generates summaries by learning to map long text → concise text.

---

### 3️⃣ Summarization

During inference:

- Input text is passed to the model
- The model generates a summary
- Output is decoded and returned as a readable summary

---

### 4️⃣ Evaluation (Optional)

Evaluation metrics for summarization often include:

- **ROUGE-1**  
- **ROUGE-2**  
- **ROUGE-L**

These measure overlap between generated summaries and reference summaries — higher values mean better quality.

---

🔹 Step 2: Setup Environment

You can use either virtualenv or conda.

Using virtualenv:
python3 -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
Using conda:
conda create -n textsum python=3.9 -y
conda activate textsum
pip install -r requirements.txt

🔹 Step 3: Run the App
python app.py

## ⚙️ How to Run Locally

### 🔹 Step 1: Clone the Repo

```bash
git clone https://github.com/Surender6/Text-Summarizer-project.git
cd Text-Summarizer-project


## How to run?
STEPS:
Clone the repository

https://github.com/Surender6/Text-Summarizer-project.git
STEP 01- Create a conda environment after opening the repository
conda create -n summary python=3.8 -y
conda activate summary
STEP 02- install the requirements
pip install -r requirements.txt
# Finally run the following command
python app.py
Now,

open up you local host and port
Author: Surender
Data Scientist
Email: gudasurendar6@gmail.com
AWS-CICD-Deployment-with-Github-Actions
1. Login to AWS console.
2. Create IAM user for deployment
#with specific access 

1. EC2 access : It is virtual machine

2. ECR: Elastic Container registry to save your docker image in aws


#Description: About the deployment

1. Build docker image of the source code

2. Push your docker image to ECR

3. Launch Your EC2 

4. Pull Your image from ECR in EC2

5. Lauch your docker image in EC2

#Policy:

1. AmazonEC2ContainerRegistryFullAccess

2. AmazonEC2FullAccess
3. Create ECR repo to store/save docker image
- Save the URI: 774305601026.dkr.ecr.eu-north-1.amazonaws.com/textsum
4. Create EC2 machine (Ubuntu)
5. Open EC2 and Install docker in EC2 Machine:
#optinal

sudo apt-get update -y

sudo apt-get upgrade

#required

curl -fsSL https://get.docker.com -o get-docker.sh

sudo sh get-docker.sh

sudo usermod -aG docker ubuntu

newgrp docker
6. Configure EC2 as self-hosted runner:
setting>actions>runner>new self hosted runner> choose os> then run command one by one
7. Setup github secrets:
AWS_ACCESS_KEY_ID=

AWS_SECRET_ACCESS_KEY=

AWS_REGION = ap-south-1

AWS_ECR_LOGIN_URI = demo>>  566373416292.dkr.ecr.ap-south-1.amazonaws.com

ECR_REPOSITORY_NAME = textsum


### 🧠 Real-World Use Cases

Automatic news article summarization

Research and academic paper condensed summary

Customer support ticket summarization

Document digest for knowledge workers

### 🔮 Future Enhancements

Fine-tune on domain-specific dataset

Add REST API backend using FastAPI

Add web UI for user interaction

Real-time summarization for streaming inputs