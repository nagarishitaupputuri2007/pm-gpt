import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st

from nlp.text_cleaner import TextCleaner
from nlp.sentiment import SentimentAnalyzer
from nlp.clustering import ProblemClusterer
from product.problem_mapper import ProblemMapper
from product.feature_generator import FeatureGenerator
from product.strategy_resolver import StrategyResolver
from roadmap.roadmap_generator import RoadmapGenerator


# ---------- UI CONFIG ----------
st.set_page_config(page_title="PM-GPT", layout="wide")
st.title("🧠 PM-GPT")
st.caption("AI Co-Pilot for Product Managers")

st.markdown("""
PM-GPT analyzes feedback and applies **Product Management frameworks**
to help you make better decisions.
""")

st.divider()

# ---------- INIT ----------
cleaner = TextCleaner()
sentiment = SentimentAnalyzer()
clusterer = ProblemClusterer(num_clusters=2)
mapper = ProblemMapper()
generator = FeatureGenerator()
resolver = StrategyResolver()
roadmap_generator = RoadmapGenerator()

# ---------- FRAMEWORK ----------
st.header("⚙️ Prioritization Framework")
framework = st.selectbox(
    "Select framework",
    ["RICE", "ICE", "MoSCoW", "Kano"]
)

strategy = resolver.resolve(framework)

st.divider()

# ---------- INPUT ----------
feedback = st.text_area(
    "Enter user feedback (one per line)",
    height=200,
    placeholder="Payment failed again\nSearch results are inaccurate"
)

if st.button("🚀 Generate PM Insights"):
    if not feedback.strip():
        st.warning("Please enter feedback")
        st.stop()

    feedbacks = feedback.split("\n")
    cleaned = [cleaner.clean(f) for f in feedbacks if cleaner.clean(f)]

    clusters = clusterer.cluster(cleaned)

    st.header("🔍 Product Problems")
    scored_features = []

    for items in clusters.values():
        problem = mapper.map_problem(items)
        st.subheader(problem)

        for i in items:
            s = sentiment.analyze(i)
            st.write(f"- {i} _(urgency: {s['compound']})_")

        features = generator.generate_features(problem)

        for feature in features:
            metrics = {
                "reach": 1000,
                "impact": 3,
                "confidence": 0.8,
                "effort": 2
            }

            score = (
                metrics["reach"]
                * metrics["impact"]
                * metrics["confidence"]
            ) / metrics["effort"]

            scored_features.append({
                "feature": feature,
                "score": score
            })

    st.divider()
    st.header("📊 Prioritization Output")

    result = strategy.prioritize(scored_features)

    # ---------- OUTPUT ----------
    if framework in ["MoSCoW", "Kano"]:
        for bucket, items in result.items():
            st.subheader(bucket)
            for f in items:
                st.write("-", f)
    else:
        roadmap = roadmap_generator.generate(result)
        for phase, items in roadmap.items():
            st.subheader(phase)
            for f in items:
                st.write("-", f)
