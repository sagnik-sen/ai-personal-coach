# AI Personal Coach with Knowledge-Enhanced Generation

This project uses IBM Watsonx.ai to provide personalized coaching, including:
- Encouraging advice
- Step-by-step action plan
- Motivational quote
- Rephrased advice
- Email draft for accountability

It also retrieves relevant reference text to enrich the generation.

## How to Run Locally

1. Clone this repo.
2. Install dependencies:
pip install -r requirements.txt
3. Create `.env` with your IBM Watsonx credentials.
4. Run the app:
streamlit run app/streamlit_app.py


## Deployment
You can deploy to Streamlit Cloud and set environment variables in the Secrets Manager.

