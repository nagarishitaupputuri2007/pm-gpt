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
# Page Config
# --------------------------------------------------
st.set_page_config(
    page_title="PM-GPT | Product Copilot",
    layout="wide"
)

# --------------------------------------------------
# HERO SECTION
# --------------------------------------------------
st.markdown("""
# 🚀 PM-GPT
### AI Copilot for Structured Product Decision-Making

Turn **unclear product problems** into  
**prioritized features, strategic clarity, and actionable roadmaps**.
""")
st.divider()

# --------------------------------------------------
# SIDEBAR CONTROLS (ONLY CONTROLS)
# --------------------------------------------------
st.sidebar.header("⚙️ Configuration")

decision_mode = st.sidebar.radio(
    "Framework Selection Mode",
    ["Auto (PM-GPT decides)", "Manual (I choose framework)"]
)

manual_framework = None
if decision_mode.startswith("Manual"):
    manual_framework = st.sidebar.selectbox(
        "Choose Framework",
        ["RICE", "ICE", "MoSCoW", "Kano"]
    )

run_clicked = st.sidebar.button("🚀 Run PM-GPT")

# --------------------------------------------------
# MAIN INPUT
# --------------------------------------------------
st.markdown("## 🧠 Describe the Product Problem")
user_problem = st.text_area(
    "",
    placeholder="Example: Users abandon onboarding due to too many steps and unclear value early on..."
)

# --------------------------------------------------
# INIT SESSION STATE
# --------------------------------------------------
for key in [
    "problem_summary",
    "features",
    "framework",
    "scored_features",
    "roadmap",
    "explanation"
]:
    if key not in st.session_state:
        st.session_state[key] = None

# --------------------------------------------------
# RUN PIPELINE
# --------------------------------------------------
if run_clicked and user_problem.strip():

    # 1. Problem Mapping
    mapper = ProblemMapper()
    st.session_state.problem_summary = mapper.map_problem([user_problem])

    # 2. Feature Generation
    generator = FeatureGenerator()
    st.session_state.features = generator.generate(st.session_state.problem_summary)

    # 3. Framework Selection
    if decision_mode.startswith("Auto"):
        selector = FrameworkSelector()
        st.session_state.framework = selector.select(st.session_state.problem_summary)
    else:
        st.session_state.framework = manual_framework

    # 4. Framework Explanation
    explainer = FrameworkExplainer()
    st.session_state.explanation = explainer.explain(
        st.session_state.framework, {}
    )

    # 5. Strategy Resolution
    resolver = StrategyResolver()
    st.session_state.scored_features = resolver.resolve(
        st.session_state.framework,
        st.session_state.features
    )

    # 6. Roadmap Generation
    roadmap_gen = RoadmapGenerator()
    st.session_state.roadmap = roadmap_gen.generate(
        st.session_state.scored_features
    )

# --------------------------------------------------
# RESULTS SECTION
# --------------------------------------------------
if st.session_state.roadmap:

    tabs = st.tabs([
        "🧩 Problem Insight",
        "🛠 Features",
        "📐 Framework Decision",
        "📊 Prioritization",
        "🗺 Roadmap"
    ])

    with tabs[0]:
        st.subheader("Problem Summary")
        st.write(st.session_state.problem_summary)

    with tabs[1]:
        st.subheader("Generated Feature Ideas")
        for feature in st.session_state.features:
            st.markdown(f"- {feature}")

    with tabs[2]:
        st.success(f"Selected Framework: **{st.session_state.framework}**")

        with st.expander("📘 Why this framework was chosen"):
            st.info(st.session_state.explanation)

        with st.expander("⚖️ Framework comparison"):
            comparison = FrameworkComparison()
            st.table(comparison.compare())

    with tabs[3]:
        st.subheader("Feature Prioritization")
        st.dataframe(
            st.session_state.scored_features,
            use_container_width=True
        )

    with tabs[4]:
        st.subheader("Product Roadmap")
        for phase, items in st.session_state.roadmap.items():
            st.markdown(f"### {phase}")
            for item in items:
                st.markdown(f"- {item}")

    # --------------------------------------------------
    # PM DECISION SUMMARY (THE WOW)
    # --------------------------------------------------
    st.divider()
    st.markdown("## ✅ PM Decision Summary")

    st.success(
        f"""
**Framework Used:** {st.session_state.framework}

**Rationale:**  
The selected framework aligns with the problem context and helps maximize impact while balancing effort and feasibility.

**Outcome:**  
A focused roadmap prioritizing the highest-value features first, enabling faster validation and reduced execution risk.
"""
    )

    # --------------------------------------------------
    # EXPORT
    # --------------------------------------------------
    st.markdown("## 📤 Export")
    exporter = RoadmapExporter()

    if st.button("📄 Export Roadmap"):
        path = exporter.export(st.session_state.roadmap)
        st.success("Roadmap exported successfully!")
        st.code(path)
