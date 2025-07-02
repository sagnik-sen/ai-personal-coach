# AI Personal Coach

This project is a web-based personal coaching tool built with Streamlit and IBM Watsonx foundation models. It generates structured, motivational, and actionable content based on user goals. The application demonstrates the use of Generative AI in a practical context while maintaining simplicity for ease of understanding and reproducibility.

> 📝 This project was developed as part of a Generative AI capstone assignment to demonstrate proficiency with foundation models and retrieval-augmented generation.

## Features

**Dynamic Model Selection**

* Choose among several pre-trained foundation models:

  * Granite Instruct
  * FLAN T5
  * Meta Llama 2 Chat
  * Mistral Large

**Retrieval-Augmented Generation**

* Enriches user input with a small internal knowledge base.

**Personalized Outputs**

* Generates:

  * Encouraging Advice
  * Step-by-Step Action Plan
  * Motivational Quote
  * Rephrased Advice
  * Accountability Email Draft

**Auto-Suggested Model**

* Recommends a model suitable for the input text.

**Downloadable Results**

* Save generated content as text files.

## Tech Stack

* IBM Watsonx.ai Studio
* Python
* Streamlit
* dotenv for configuration

## How to Run Locally

1. Clone the repository

```bash
git clone https://github.com/sagnik-sen/ai-personal-coach.git
cd ai-personal-coach
```

2. Create and activate a virtual environment

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Set up environment variables

Create a `.env` file with your Watsonx credentials:

```
WATSONX_API_KEY=your_api_key_here
WATSONX_PROJECT_ID=your_project_id_here
WATSONX_URL=your_watsonx_url_here
```

*(Do not commit **`.env`** to version control.)*

5. Start the app

```bash
streamlit run app/streamlit_app.py
```

## Knowledge Base

The app includes a small internal knowledge base to enhance response relevance:

* Health & Fitness
* Productivity
* Learning
* Motivation

## License

This project is licensed under the [MIT License](LICENSE).
