# snoonu-thermal-bag-checker
# 🤖 Snoonu AI Thermal Bag Inspector

[cite_start]Yasir Pulikkal 
**Task:** AI Innovation Intern - Test Task 1: Thermal Bag Quality Checker

This repository contains my submission for the Snoonu AI Innovation Intern test task. It is a functional web application that uses a multimodal AI model (GPT-4o) to analyze photos of courier thermal bags and determine if they are in acceptable condition for a shift.

---

### 🚀 Live Demo

This application is deployed on Hugging Face Spaces and is publicly accessible.

**Live App URL:** **[Link to your Deployed Hugging Face Space]**

### 🎬 2-Minute Video Walkthrough

[**Link to your 2-minute Loom or YouTube demo video**]

---

### 1. Problem Statement

[cite_start]The task [cite: 4] [cite_start]is to create a tool (chatbot, app, or webhook) [cite: 4] [cite_start]that evaluates the quality of a courier's thermal bag from a single photo[cite: 5]. [cite_start]The tool must be able to distinguish between an acceptable and an unacceptable bag[cite: 7].

### 2. Solution Approach

Given the 2-day timeline and a small example set, training a custom computer vision model from scratch would be impractical and likely low-accuracy.

I chose a modern, "AI-driven" approach that aligns with the "experimental, AI-powered projects"  goal of the internship. My solution is a **Gradio web app** that uses the **GPT-4o multimodal model** to perform "few-shot" visual analysis.

**Why this stack?**
* [cite_start]**Gradio:** Rapidly builds a clean, professional "small app"  UI for image uploads, perfectly matching the task requirement. [cite_start]My experience with Gradio  allowed for fast development.
* **GPT-4o (Vision API):** Leverages a powerful SOTA model to understand nuanced, human-like concepts like "cleanliness," "integrity," and "functionality" from an image with zero training data.
* **Hugging Face Spaces:** The industry-standard platform for hosting and sharing AI/ML demos, demonstrating familiarity with the modern AI ecosystem.

This solution proves I can "prototype and test AI-driven solutions to real operational challenges"   quickly and effectively.

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