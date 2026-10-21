import streamlit as st
from google import genai
from dotenv import load_dotenv
from pathlib import Path
import os


# =========================================================
# 1. LOAD ENVIRONMENT VARIABLES
# =========================================================

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")


# =========================================================
# 2. CHECK API KEY
# =========================================================

if not api_key:
    st.error("❌ GEMINI_API_KEY is missing. Please check your .env file.")
    st.stop()


# =========================================================
# 3. CREATE GEMINI CLIENT
# =========================================================

client = genai.Client(api_key=api_key)


# =========================================================
# 4. PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="AI Recipe Creator",
    page_icon="🍳",
    layout="centered"
)


# =========================================================
# 5. LOAD CSS
# =========================================================

css_path = Path("style.css")

if css_path.exists():

    with open(css_path, "r", encoding="utf-8") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

else:

    st.warning("⚠️ style.css file was not found.")


# =========================================================
# 6. APPLICATION HEADER
# =========================================================

st.markdown(
    '<div class="main-title">🍳 AI Recipe Creator</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    '✨ Turn your everyday ingredients into delicious recipes with AI ✨'
    '</div>',
    unsafe_allow_html=True
)


# =========================================================
# 7. INGREDIENT INPUT
# =========================================================

st.markdown("### 🥕 What ingredients do you have?")

ingredients = st.text_area(
    "🥕 Enter your available ingredients",
    placeholder="💡 Example: vegetables, rice, pasta, eggs, chicken, spices...",
    height=160
)


# =========================================================
# 8. GENERATE RECIPE BUTTON
# =========================================================

if st.button("🍳 Generate My Recipe"):

    if not ingredients.strip():

        st.warning(
            "🥕 Please enter at least one ingredient first."
        )

    else:

        # Loading message
        with st.spinner("👨‍🍳 AI Chef is preparing your recipe..."):

            # =================================================
            # 9. GEMINI PROMPT
            # =================================================

            prompt = f"""
You are a professional AI chef and recipe assistant.

The user has these ingredients:

{ingredients}

Create a delicious and practical recipe using the available
ingredients.

Return the answer in exactly this style:

# 🍽️ Recipe Name

Write a short one-line description of the recipe.

**⏱️ Cooking Time:** XX minutes

**👥 Servings:** X

**🌶️ Difficulty:** Easy / Medium / Hard

---

## 🥕 Ingredients

- Ingredient 1
- Ingredient 2
- Ingredient 3

Include reasonable basic ingredients such as salt, oil,
pepper or spices when necessary.

---

## 👨‍🍳 Step-by-Step Instructions

1. 🔪 First cooking step.
2. 🔥 Second cooking step.
3. 🧅 Third cooking step.
4. 🍳 Fourth cooking step.
5. 🍽️ Final serving step.

---

## 💡 Chef's Tip

Give one useful cooking tip.

Use simple language.

Make the instructions practical for a beginner.
"""


            # =================================================
            # 10. SEND REQUEST TO GEMINI
            # =================================================

            try:

                interaction = client.interactions.create(
                    model="gemini-3.6-flash",
                    input=prompt
                )

                recipe = interaction.output_text


                # =================================================
                # 11. DISPLAY RECIPE
                # =================================================

                st.markdown(
                    '<div class="recipe-card">',
                    unsafe_allow_html=True
                )

                st.markdown(
                    "## 🍽️ Your AI Generated Recipe"
                )

                st.markdown(recipe)

                st.markdown(
                    "</div>",
                    unsafe_allow_html=True
                )


                # =================================================
                # 12. SUCCESS MESSAGE
                # =================================================

                st.success(
                    "🎉 Your recipe is ready! Happy cooking! 👨‍🍳"
                )


            except Exception as e:

                st.error("❌ Gemini Error")

                st.code(str(e))