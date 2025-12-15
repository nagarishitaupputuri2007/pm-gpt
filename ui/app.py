import sys
import os

# Allow imports from project root
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st

from nlp.text_cleaner import TextCleaner
from nlp.sentiment import SentimentAnalyzer
from nlp.clustering import ProblemClusterer
from product.problem_mapper import ProblemMapper
from product.feature_generator import FeatureGenerator
from product.rice_scoring import RiceScorer
from roadmap.roadmap_generator import RoadmapGenerator


# -------------------- PAGE CONFIG --------------------
st.set_page_config(
    page_title="PM-GPT",
    layout="wide"
)

# -------------------- HEADER --------------------
st.title("🧠 PM-GPT")
st.caption("AI Co-Pilot for Product Managers")

st.markdown(
    """
PM-GPT helps Product Managers:
- Understand user feedback  
- Identify core product problems  
- Generate feature ideas  
- Prioritize using PM frameworks (RICE)  
- Build data-driven roadmaps  
"""
)

st.divider()

# -------------------- INITIALIZE COMPONENTS --------------------
cleaner = TextCleaner()
sentiment_analyzer = SentimentAnalyzer()
clusterer = ProblemClusterer(num_clusters=2)
problem_mapper = ProblemMapper()
feature_generator = FeatureGenerator()
rice_scorer = RiceScorer()
roadmap_generator = RoadmapGenerator()

# -------------------- INPUT --------------------
st.header("📥 Input: User Feedback")

feedback = st.text_area(
    "Enter one feedback per line",
    height=200,
    placeholder="Payment failed again...\nSearch results are inaccurate..."
)

# -------------------- ACTION --------------------
if st.button("🚀 Generate PM Insights"):

    if not feedback.strip():
        st.warning("Please enter user feedback.")
        st.stop()

    feedbacks = feedback.split("\n")

    # -------- TEXT CLEANING --------
    cleaned_feedbacks = [cleaner.clean(f) for f in feedbacks]

    st.divider()
    st.header("🧹 Cleaned Feedback")
    for text in cleaned_feedbacks:
        st.write("-", text)

    # -------- CLUSTERING (PROBLEMS) --------
    clusters = clusterer.cluster(cleaned_feedbacks)

    st.divider()
    st.header("🔍 Detected Product Problems")

    scored_features = []

    for cluster_items in clusters.values():
        problem = problem_mapper.map_problem(cluster_items)
        st.subheader(problem)

        for item in cluster_items:
            sentiment = sentiment_analyzer.analyze(item)
            st.write(f"- {item} _(urgency: {sentiment['compound']})_")

        # -------- FEATURE GENERATION --------
        features = feature_generator.generate_features(problem)

        for feature in features:
            metrics = {
                "reach": 1000,
                "impact": 3,
                "confidence": 0.8,
                "effort": 2
            }

            score = rice_scorer.score(feature, metrics)
            scored_features.append({
                "feature": feature,
                "score": score
            })

    # -------- ROADMAP --------
    st.divider()
    st.header("📊 Prioritized Roadmap")

    roadmap = roadmap_generator.generate(scored_features)

    for phase, features in roadmap.items():
        st.subheader(phase)
        for feature in features:
            st.write("-", feature)
