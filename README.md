# 🍳 AI Recipe Creator

An AI-powered recipe generation web application built with Python and Streamlit. It helps users discover recipe ideas using Generative AI.

## ✨ Features

- 🤖 AI-powered recipe generation
- 🍽️ Generate recipe ideas based on user input
- 🎨 Custom-designed interface with CSS styling
- 🐍 Built with Python and Streamlit
- 🔐 Uses environment variables to protect API credentials

## 🛠️ Technologies Used

- Python
- Streamlit
- Generative AI
- Google Gemini API
- HTML/CSS styling through Streamlit

## 📁 Project Structure

```text
ai_recipe_creator/
├── app.py
├── style.css
├── .gitignore
├── .env.example
└── README.md
```

## 🚀 Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/chethansree77/ai-recipe-creator.git
cd ai-recipe-creator
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

**Windows PowerShell:**

```powershell
.\venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
pip install streamlit google-genai python-dotenv
```

### 5. Configure your API key

Create a `.env` file in the project folder:

```env
GEMINI_API_KEY=your_api_key_here
```

Replace `your_api_key_here` with your own Gemini API key. Never upload your real API key to GitHub.

### 6. Run the application

```bash
streamlit run app.py
```

## 🎯 Project Goal

This project demonstrates practical skills in Python development, Generative AI integration, and interactive web application development.

## 👩‍💻 Author

**Chethana Sai Sree**

GitHub: [@chethansree77](https://github.com/chethansree77)
