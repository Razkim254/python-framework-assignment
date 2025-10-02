DEPLOY LINK

https://razkim254-python-framework-assignment-streamlit-app-6d0lfu.streamlit.app/




markdown
# 🧠 CORD-19 Data Exploration & Visualization

This project explores the [CORD-19 dataset](https://www.semanticscholar.org/cord19) to uncover insights from COVID-19-related scientific literature. It includes data preprocessing, metadata analysis, and interactive visualizations via Streamlit.

## 📁 Project Structure

FRAMEWORK/ ├── app.py # Main script (optional entry point) ├── cord19_exploration.ipynb # Jupyter notebook for data exploration ├── generate_visuals.py # Script to generate plots and figures ├── metadata.csv # Metadata from the CORD-19 dataset ├── requirements.txt # Python dependencies └── streamlit_app.py # Streamlit dashboard for interactive exploration

Code

## 🚀 Features

- Cleaned and structured metadata from CORD-19
- Visualizations of publication trends, authorship, and topics
- Interactive dashboard built with Streamlit
- Modular codebase for reproducibility and extension

## 🛠️ Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/cord19-visualization.git
   cd cord19-visualization
Create and activate a virtual environment

bash
python -m venv venv
source venv/bin/activate  # or use PowerShell/Git Bash on Windows
Install dependencies

bash
pip install -r requirements.txt
Run the Streamlit app

bash
streamlit run streamlit_app.py
📊 Visualizations
📅 Publication timeline

🌍 Country-wise research distribution

🧬 Keyword frequency and trends

👥 Author and affiliation networks

📓 Notebook Highlights
The cord19_exploration.ipynb notebook includes:

Data cleaning and preprocessing

Exploratory data analysis (EDA)

Plot generation using matplotlib and seaborn

📦 Dependencies
Key packages:

pandas, numpy

matplotlib, seaborn

streamlit

openpyxl (if working with Excel files)

See requirements.txt for full list.

📌 Notes
Line endings may vary across platforms (LF vs CRLF); see .gitattributes for consistency.

Designed for reproducibility and cross-platform compatibility.

🙌 Acknowledgments
CORD-19 Dataset by Semantic Scholar

Visual inspiration from COVID-19 dashboards and academic tools
