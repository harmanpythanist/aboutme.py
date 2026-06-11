import streamlit as st

# --- Page Config ---
st.set_page_config(page_title="My Portfolio", page_icon="💼", layout="centered")

# --- Header ---
st.title("💼 My Personal Portfolio")
st.write("Welcome to my portfolio app built with Streamlit!")

# --- Personal Information ---
st.header("👤 About Me")
st.write("""
Hello! My name is [Your Name].  
I live in **Lahore, Pakistan**.  
I completed my **Matriculation** from *Faiz Foundation School*.  
My goal is to **earn money** by using my skills and exploring opportunities online.
""")

# --- Skills Section ---
st.header("🛠️ My Skills")
skills = ["Basic Computer Knowledge", "Communication", "Tutoring (Matric subjects)", "Freelancing Interest"]
for skill in skills:
    st.write(f"- {skill}")

# --- Opportunities Section ---
st.header("💡 Earning Opportunities")
st.write("Here are some ways I can start earning:")

opportunities = {
    "Freelancing": "Offer services on platforms like Fiverr or Upwork (writing, tutoring, data entry).",
    "Tutoring": "Teach matric-level subjects to younger students in Lahore or online.",
    "Content Creation": "Start a YouTube channel or blog about student life, education, or local culture.",
    "Digital Skills": "Learn coding, graphic design, or digital marketing to expand opportunities."
}

for key, value in opportunities.items():
    st.subheader(key)
    st.write(value)

# --- Contact Section ---
st.header("📬 Contact Me")
st.write("If you'd like to collaborate or offer guidance, you can reach me at:")
st.write("📧 your_email@example.com")
st.write("📱 +92-300-0000000")

# --- Footer ---
st.markdown("---")
st.write("Made with ❤️ in Streamlit")

