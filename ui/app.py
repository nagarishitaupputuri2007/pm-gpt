# ui/app.py
import streamlit as st

from product.problem_mapper import ProblemMapper
from product.feature_generator import FeatureGenerator
from product.framework_selector import FrameworkSelector
from product.framework_explainer import FrameworkExplainer
from product.framework_comparison import FrameworkComparison
from product.strategy_resolver import StrategyResolver

from roadmap.roadmap_generator import RoadmapGenerator
from roadmap.roadmap_exporter import RoadmapExporter

# --------------------------------------------------
# Page config
# --------------------------------------------------
st.set_page_config(
    page_title="PM-GPT | Product Copilot",
    layout="wide"
)

st.title("🚀 PM-GPT – Product Management Copilot")
st.caption("AI-assisted product thinking: problems → features → strategy → roadmap")

# --------------------------------------------------
# Sidebar controls
# --------------------------------------------------
st.sidebar.header("⚙️ Controls")

decision_mode = st.sidebar.radio(
    "Decision Mode",
    ["Auto (PM-GPT decides)", "Manual (I choose framework)"]
)

manual_framework = None
if decision_mode == "Manual (I choose framework)":
    manual_framework = st.sidebar.selectbox(
        "Choose Framework",
        ["RICE", "ICE", "MoSCoW", "Kano"]
    )

user_problem = st.sidebar.text_area(
    "Describe the product problem",
    placeholder="Example: Users drop off during onboarding because it is too long..."
)

run_clicked = st.sidebar.button("Run PM-GPT")

# --------------------------------------------------
# INIT SESSION STATE
# --------------------------------------------------
for key in [
    "problem_summary",
    "features",
    "framework",
    "scored_features",
    "roadmap"
]:
    if key not in st.session_state:
        st.session_state[key] = None

# --------------------------------------------------
# RUN MAIN PIPELINE (ONLY ON RUN CLICK)
# --------------------------------------------------
if run_clicked and user_problem.strip():

    # 1. Problem Mapping
    st.subheader("1️⃣ Problem Mapping")
    mapper = ProblemMapper()
    problem_summary = mapper.map_problem([user_problem])
    st.session_state.problem_summary = problem_summary
    st.write(problem_summary)

    # 2. Feature Generation
    st.subheader("2️⃣ Feature Generation")
    generator = FeatureGenerator()
    features = generator.generate(problem_summary)
    st.session_state.features = features
    st.write(features)

    # 3. Framework Selection
    st.subheader("3️⃣ Framework Selection")
    if decision_mode.startswith("Auto"):
        selector = FrameworkSelector()
        framework = selector.select(problem_summary)
    else:
        framework = manual_framework

    st.session_state.framework = framework
    st.success(f"Selected Framework: **{framework}**")

    # 4. Framework Explanation
    st.subheader("4️⃣ Framework Explanation")
    explainer = FrameworkExplainer()
    explanation = explainer.explain(framework, {})
    st.info(explanation)

    # 5. Framework Comparison
    st.subheader("5️⃣ Framework Comparison")
    comparison = FrameworkComparison()
    st.table(comparison.compare())

    # 6. Strategy Resolution
    st.subheader("6️⃣ Strategy Resolution")
    resolver = StrategyResolver()
    scored_features = resolver.resolve(framework, features)
    st.session_state.scored_features = scored_features
    st.json(scored_features)

    # 7. Roadmap Generation
    st.subheader("7️⃣ Roadmap Generation")
    roadmap_gen = RoadmapGenerator()
    roadmap = roadmap_gen.generate(scored_features)
    st.session_state.roadmap = roadmap
    st.json(roadmap)

# --------------------------------------------------
# EXPORT SECTION (ALWAYS VISIBLE IF ROADMAP EXISTS)
# --------------------------------------------------
if st.session_state.roadmap:
    st.subheader("8️⃣ Export Roadmap")
    exporter = RoadmapExporter()

    if st.button("📄 Export Roadmap"):
        path = exporter.export(st.session_state.roadmap)
        st.success("Roadmap exported successfully!")
        st.code(path)
