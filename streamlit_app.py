import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 📦 Load data safely
@st.cache_data
def load_data():
    try:
        df = pd.read_csv("metadata.csv")
        return df
    except FileNotFoundError:
        st.error("metadata.csv not found. Please ensure the file is in the project directory.")
        return pd.DataFrame()
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return pd.DataFrame()

# 📊 Overview tab
def show_overview(df):
    st.subheader("Dataset Overview")
    st.write(f"Total records: {len(df)}")
    st.write("Available columns:", df.columns.tolist())
    st.dataframe(df.head(10))

# 📈 Visuals tab
def show_visuals(df):
    st.subheader("Publication Timeline")

    if 'date' in df.columns:
        df['date'] = pd.to_datetime(df['date'], errors='coerce')
        df = df.dropna(subset=['date'])

        fig, ax = plt.subplots()
        sns.histplot(df['date'], bins=30, ax=ax)
        ax.set_title("Distribution of Publication Dates")
        ax.set_xlabel("Date")
        ax.set_ylabel("Count")
        st.pyplot(fig)
    else:
        st.warning("Column 'date' not found. Showing fallback visualization.")

        # Try fallback using any available categorical column
        fallback_cols = ['location', 'continent', 'iso_code']
        available_fallback = [col for col in fallback_cols if col in df.columns]

        if available_fallback:
            fallback_col = available_fallback[0]
            st.write(f"Fallback: Top values in '{fallback_col}'")
            st.bar_chart(df[fallback_col].value_counts().head(10))
        else:
            st.info("No suitable fallback column available for visualization.")

# 🚀 Main app logic
def main():
    st.set_page_config(page_title="CORD-19 Dashboard", layout="wide")
    st.title("CORD-19 Metadata Explorer")

    df = load_data()
    if df.empty:
        st.stop()

    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Overview", "Visuals"])

    if page == "Overview":
        show_overview(df)
    elif page == "Visuals":
        show_visuals(df)

# 🧠 Entry point
if __name__ == "__main__":
    main()
