# 🤖 AI Coding Assistant

## 🚀 Overview

This project is an **AI-powered coding assistant** that leverages **Langchain** and the **Google API** (e.g., **Gemini**) to help developers in two key areas:

1. 🛠️ **Error Resolution & Development Ideas** – Analyzes code screenshots and user queries to identify errors, suggest fixes, and propose new features.
2. 💡 **Programming Q&A Agent** – Provides answers to development-related questions.

---

## ✨ Features

- 🖼️ **Screenshot Analysis** – Upload a screenshot of your code.
- 🧠 **Error Identification** – AI highlights possible errors in the code.
- 🧰 **Solution Suggestions** – Offers fixes and relevant code snippets.
- 💡 **Development Ideas** – Proposes optimizations and new features.
- ❓ **Programming Q&A** – Ask coding questions and get intelligent responses.
- 🔗 **Langchain Integration** – Manages LLM interaction and tool orchestration.
- 🌐 **Google LLM Powered** – Uses Gemini (via Google API) for smart code analysis.
- 🗣️ **Natural Language Query Processing** – Understands developer intent clearly.

---
## 🧰 Technologies Used

- 🐍 Python  
- 🪜 Langchain  
- 🌐 Google API (e.g., Gemini)  
- 🖼️ PIL (for image handling, optional)  
- 🖥️ Streamlit (for UI)  

---
## ⚙️ Setup and Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Anonymous7722/Coding_Assistant_AI_Agent
    cd Coding_Assistant_AI_Agent
    ```
2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    store your GOOGLE API IN .env file
    GOOGLE_API_KEY=your_api_key_here
    python3 -m streamlit run app.py
    ```
3.  **Configure Google API credentials:**
    *   Obtain API credentials from the Google.
    *   Set the environment variable `GOOGLE_API_KEY` (or use your preferred method of authentication).  Provide specific instructions.
4.  **[Any other setup steps specific to your project, e.g., database configuration]**

## 🧑‍💻 Usage

1.  **Error Resolution & Development Ideas:**
    *   📸 Upload a screenshot of the code.
    *   💬 Ask what’s wrong or how to improve it.
    *   🤖 Review AI-generated insights.
2.  **Programming Q&A:**
    *   🧠 Ask development questions.
    *  📜 Get quick and relevant answers from the AI.

## 📌 Examples

*   **Error Resolution:**
    *   Input: Screenshot of a Python code snippet with a syntax error, query: "What's wrong with this code?"
    *   Output: "The code has a syntax error on line 5.  Missing a colon after the `if` statement.  Suggested fix: `if x > 5:`"

*   **Development Idea:**
    *   Input: Screenshot of a function, query: "How can I improve this function's performance?"
    *   Output: "You can improve the function's performance by using memoization to cache the results of expensive calculations."

*   **Programming Q&A:**
    *   Input: Query: "What is the difference between `==` and `is` in Python?"
    *   Output: "The `==` operator compares the *values* of two objects, while the `is` operator checks if two variables refer to the *same object* in memory."

 ## Screenshot

 ![image](https://github.com/user-attachments/assets/91caa589-c5e1-40c2-b3da-d609d288a673)
 
 ![image](https://github.com/user-attachments/assets/d30e143f-d4aa-4d9a-aaa1-4767329de632)
 
 ![image](https://github.com/user-attachments/assets/a249f441-5758-45c3-885c-681287c04fff)

 ![image](https://github.com/user-attachments/assets/b0bb48a7-76a8-484a-b751-b05e94191ad8)

 ![image](https://github.com/user-attachments/assets/4c1bb9a8-bc2d-4ebc-8d92-a9a81c26356f)

 ![image](https://github.com/user-attachments/assets/4033102e-b28f-43f4-a48c-efab182517ca)





## License

