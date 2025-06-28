import os
from dotenv import load_dotenv
import streamlit as st
from ibm_watsonx_ai.foundation_models import Model

# Load environment variables
load_dotenv()
api_key = os.getenv("WATSONX_API_KEY")
project_id = os.getenv("WATSONX_PROJECT_ID")
watsonx_url = os.getenv("WATSONX_URL")

# Credentials
credentials = {
    "url": watsonx_url,
    "apikey": api_key
}

# Model options with descriptions in names
model_options = {
    "Granite 13B Instruct v2 (Instructions)": "ibm/granite-13b-instruct-v2",
    "FLAN T5 XXL (Summarization/Rephrasing)": "google/flan-t5-xxl",
    "Llama 2 13B Chat (Conversational)": "meta-llama/llama-2-13b-chat",
    "Mistral Large (Concise Instructions)": "mistralai/mistral-large"
}

# Model descriptions in sidebar
model_descriptions = """
**Model descriptions:**
- 🟢 **Granite 13B Instruct v2** – Best for precise instructions and factual advice.
- 🟢 **FLAN T5 XXL** – Great for summarization, rephrasing, and shorter outputs.
- 🟢 **Llama 2 13B Chat** – More conversational, friendly, and verbose.
- 🟢 **Mistral Large** – Strong instruction following with concise responses.
"""

# Suggest the best model based on input
def suggest_model(user_input):
    recommendations = [
        ("health", "Llama 2 13B Chat (Conversational)"),
        ("exercise", "Llama 2 13B Chat (Conversational)"),
        ("motivation", "Llama 2 13B Chat (Conversational)"),
        ("focus", "Granite 13B Instruct v2 (Instructions)"),
        ("productivity", "Granite 13B Instruct v2 (Instructions)"),
        ("study", "Granite 13B Instruct v2 (Instructions)"),
        ("learning", "FLAN T5 XXL (Summarization/Rephrasing)"),
        ("summarize", "FLAN T5 XXL (Summarization/Rephrasing)"),
        ("concise", "Mistral Large (Concise Instructions)")
    ]
    for keyword, model in recommendations:
        if keyword in user_input.lower():
            return model
    return "Granite 13B Instruct v2 (Instructions)"

# Generation parameters
params = {
    "decoding_method": "greedy",
    "max_new_tokens": 300,
    "temperature": 0.5
}

# Knowledge base
knowledge_base = {
    "health": "Staying healthy requires regular exercise, balanced nutrition, and enough sleep.",
    "productivity": "To be productive, set clear goals, break tasks into small steps, and remove distractions.",
    "learning": "Effective learning involves spaced repetition, active recall, and teaching others.",
    "motivation": "Motivation can be built by celebrating small wins and visualizing success."
}

keywords = {
    "health": ["health", "exercise", "fitness"],
    "productivity": ["productivity", "work", "focus"],
    "learning": ["study", "learning", "education"],
    "motivation": ["motivation", "inspiration", "goal"]
}

# Retrieve reference text based on keywords
def retrieve_reference(user_input):
    for topic, words in keywords.items():
        if any(word in user_input.lower() for word in words):
            return knowledge_base[topic]
    return ""

# Clean output if model returns extra text
def clean_output(text):
    markers = ["Answer:", "Advice:", "Response:", "Rewritten:", "Rephrase:"]
    for marker in markers:
        if marker in text:
            return text.split(marker, 1)[1].strip()
    return text.strip()

# Generate output with Watsonx
def generate_output(prompt):
    model = Model(
        model_id=model_id,
        params=params,
        credentials=credentials,
        project_id=project_id
    )
    result = model.generate_text(prompt=prompt)
    return result

# Streamlit UI
st.set_page_config(page_title="AI Personal Coach", layout="wide")

# Sidebar
st.sidebar.title("AI Personal Coach")
st.sidebar.markdown("""
This app uses IBM Watsonx foundation models with retrieval-augmented generation to create personalized coaching content.

**Developed by:** Sagnik Sen\n
**Powered by:** Watsonx.ai
""")
selected_model_label = st.sidebar.selectbox(
    "Choose a model:",
    list(model_options.keys()),
    index=0
)
model_id = model_options[selected_model_label]

st.sidebar.markdown(model_descriptions)

# Main Title
st.title("AI Personal Coach with Knowledge-Enhanced Generation")
st.markdown("""
Enter your goal or challenge below to receive personalized advice, plans, and motivational content.
""")

user_input = st.text_area("Enter your goal or challenge:")

# Auto-suggest model
if user_input.strip() != "":
    recommendation = suggest_model(user_input)
    st.info(f"💡 **Recommended Model:** {recommendation}")

# Generate content
if st.button("Generate Coaching Plan"):
    if user_input.strip() == "":
        st.warning("Please enter a goal or challenge.")
    else:
        reference = retrieve_reference(user_input)
        st.info(f"**Retrieved Reference Text:**\n{reference if reference else 'None'}")
        
        with st.spinner("Generating coaching content..."):
            advice_prompt = f"Reference text: {reference}\nUser goal: {user_input}\nProvide friendly and encouraging advice."
            plan_prompt = f"Reference text: {reference}\nUser goal: {user_input}\nCreate a clear, step-by-step action plan."
            quote_prompt = f"Reference text: {reference}\nUser goal: {user_input}\nSuggest a short motivational quote."
            rephrase_prompt = f"Reference text: {reference}\nUser goal: {user_input}\nRewrite the advice in simpler words."
            email_prompt = f"Reference text: {reference}\nUser goal: {user_input}\nDraft a motivational email to an accountability partner."

            try:
                advice = clean_output(generate_output(advice_prompt))
                plan = clean_output(generate_output(plan_prompt))
                quote = clean_output(generate_output(quote_prompt))
                rephrase = clean_output(generate_output(rephrase_prompt))
                email = clean_output(generate_output(email_prompt))
            except Exception as e:
                st.error(f"Error generating outputs: {e}")
                st.stop()

        st.success("✅ Coaching plan generated successfully!")

        # Expanders and download buttons
        with st.expander("Encouraging Advice"):
            st.write(advice)
            st.download_button(
                label="Download Advice",
                data=advice,
                file_name="advice.txt",
                mime="text/plain"
            )

        with st.expander("Step-by-Step Action Plan"):
            st.write(plan)
            st.download_button(
                label="Download Action Plan",
                data=plan,
                file_name="action_plan.txt",
                mime="text/plain"
            )

        with st.expander("Motivational Quote"):
            st.write(quote)
            st.download_button(
                label="Download Quote",
                data=quote,
                file_name="quote.txt",
                mime="text/plain"
            )

        with st.expander("Rephrased Advice"):
            st.write(rephrase)
            st.download_button(
                label="Download Rephrased Advice",
                data=rephrase,
                file_name="rephrased_advice.txt",
                mime="text/plain"
            )

        with st.expander("Email Draft"):
            st.write(email)
            st.download_button(
                label="Download Email Draft",
                data=email,
                file_name="email_draft.txt",
                mime="text/plain"
            )
