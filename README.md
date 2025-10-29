# snoonu-thermal-bag-checker
# 🤖 Snoonu AI Thermal Bag Inspector

Yasir Pulikkal 
**Task:** AI Innovation Intern - Test Task 1: Thermal Bag Quality Checker

This repository contains my submission for the Snoonu AI Innovation Intern test task. It is a functional web application that uses a multimodal AI model (GPT-4o) to analyze photos of courier thermal bags and determine if they are in acceptable condition for a shift.

---

### 🚀 Live Demo

This application is deployed on Hugging Face Spaces and is publicly accessible.

**Live App URL:** **https://huggingface.co/spaces/yasirp11/snoonu-thermal-bag-checker**

### 🎬 2-Minute Video Walkthrough

* **[yasirpfaisal/snoonu-thermal-bag-checker]([https://github.com/yasirpfaisal/snoonu-thermal-bag-checker](https://www.loom.com/share/3abcc1708d064bec8f383955a2cfac83))** 
---

### 1. Problem Statement

The task is to create a tool (chatbot, app, or webhook) that evaluates the quality of a courier's thermal bag from a single photo.The tool must be able to distinguish between an acceptable and an unacceptable bag.

### 2. Solution Approach

Given the 2-day timeline and a small example set, training a custom computer vision model from scratch would be impractical and likely low-accuracy.

I chose a modern, "AI-driven" approach that aligns with the "experimental, AI-powered projects"  goal of the internship. My solution is a **Gradio web app** that uses the **GPT-4o multimodal model** to perform "few-shot" visual analysis.

**Why this stack?**
* **Gradio:** Rapidly builds a clean, professional "small app"  UI for image uploads, perfectly matching the task requirement. My experience with Gradio  allowed for fast development.
* **GPT-4o (Vision API):** Leverages a powerful SOTA model to understand nuanced, human-like concepts like "cleanliness," "integrity," and "functionality" from an image with zero training data.
* **Hugging Face Spaces:** The industry-standard platform for hosting and sharing AI/ML demos, demonstrating familiarity with the modern AI ecosystem.

This solution proves I can "prototype and test AI-driven solutions to real operational challenges" quickly and effectively.

---

### 3. Features

* **AI-Powered Analysis:** Uses GPT-4o to analyze bag quality against three core criteria: **Cleanliness, Integrity, and Functionality**.
* **Structured JSON Output:** The prompt is engineered to force the AI to return a JSON object, which is then parsed to provide a clean, reliable UI.
* **Clear Results:** Provides a clear "✅ ACCEPTABLE" or "❌ NOT ACCEPTABLE" status.
* **Detailed Rationale:** The AI provides a plain-English reason for its decision and a Pass/Fail status for each criterion.
* **Multiple Inputs:** Supports file uploads and direct webcam access for "live" testing.
* **Example-Driven:** Includes the two sample bags as one-click examples for easy testing.

---

### 4. How to Run Locally

You can run this project on your local machine for testing.

**Prerequisites:**
* Python 3.9+
* An OpenAI API Key

**Step 1: Clone the Repository**
```bash
git clone https://github.com/yasirpfaisal/snoonu-thermal-bag-checker.git
cd snoonu-thermal-bag-checker
```

**Step 2: Set Up a Virtual Environment**
It's highly recommended to use a virtual environment to manage dependencies.

*On Windows (PowerShell):*
```bash
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**Step 3: Install Dependencies Install all the required packages from the requirements.txt file.**
```bash
pip install -r requirements.txt
```

**Step 4: Configure Environment Variables The application requires an OpenAI API key to function.**
*On Windows (PowerShell):*
```Bash
copy .env.example .env
```
Open the newly created .env file in your text editor.
Paste your secret OpenAI API key into the file:
```Bash
OPENAI_API_KEY="sk-YourSecretOpenAI_API_KeyGoesHere"
```

**Step 5: Run the Application**
```Bash
python app.py
```

The application will launch and print a local URL (e.g., http://127.0.0.1:7860) in your terminal. Open this link in your web browser to use the app
