import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

# Ensure visuals directory exists
os.makedirs('visuals', exist_ok=True)

# Load data
df = pd.read_csv('metadata.csv', low_memory=False)
df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')
df['year'] = df['publish_time'].dt.year
df['abstract_word_count'] = df['abstract'].fillna('').apply(lambda x: len(x.split()))

# Analysis
year_counts = df['year'].value_counts().sort_index()
top_journals = df['journal'].value_counts().head(10)
source_counts = df['source_x'].value_counts().head(10)

# Word cloud
title_text = ' '.join(df['title'].dropna().astype(str))
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(title_text)

# Save visualizations
plt.figure(figsize=(8, 5))
plt.bar(year_counts.index.astype(int), year_counts.values)
plt.title('Publications by Year')
plt.xlabel('Year')
plt.ylabel('Count')
plt.tight_layout()
plt.savefig('visuals/publications_by_year.png')
plt.close()

plt.figure(figsize=(10, 6))
sns.barplot(x=top_journals.values, y=top_journals.index)
plt.title('Top Journals Publishing COVID-19 Research')
plt.xlabel('Number of Papers')
plt.tight_layout()
plt.savefig('visuals/top_journals.png')
plt.close()

plt.figure(figsize=(8, 5))
sns.barplot(x=source_counts.values, y=source_counts.index)
plt.title('Top Sources')
plt.xlabel('Count')
plt.tight_layout()
plt.savefig('visuals/source_distribution.png')
plt.close()

plt.figure(figsize=(10, 6))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.tight_layout()
plt.savefig('visuals/wordcloud_titles.png')
plt.close()
