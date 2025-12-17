import streamlit as st

from product.problem_mapper import ProblemMapper
from product.feature_generator import FeatureGenerator
from product.framework_selector import FrameworkSelector
from product.framework_explainer import FrameworkExplainer
from product.framework_comparison import FrameworkComparison
from product.strategy_resolver import StrategyResolver
from product.decision_narrator import DecisionNarrator

from roadmap.roadmap_generator import RoadmapGenerator
from roadmap.roadmap_exporter import RoadmapExporter

# --------------------------------------------------
# PAGE CONFIG
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
# SIDEBAR CONTROLS
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
    "Product Problem",
    placeholder="Example: Users abandon onboarding due to too many steps and unclear value early on...",
    label_visibility="collapsed"
)

# --------------------------------------------------
# SESSION STATE INIT
# --------------------------------------------------
for key in [
    "problem_summary",
    "features",
    "framework",
    "explanation",
    "scored_features",
    "roadmap"
]:
    if key not in st.session_state:
        st.session_state[key] = None

# --------------------------------------------------
# RUN PIPELINE
# --------------------------------------------------
if run_clicked and user_problem.strip():

    # 1️⃣ Problem Mapping
    mapper = ProblemMapper()
    st.session_state.problem_summary = mapper.map_problem([user_problem])

    # 2️⃣ Feature Generation
    generator = FeatureGenerator()
    st.session_state.features = generator.generate(
        st.session_state.problem_summary
    )

    # 3️⃣ Framework Selection
    if decision_mode.startswith("Auto"):
        selector = FrameworkSelector()
        st.session_state.framework = selector.select(
            st.session_state.problem_summary
        )
    else:
        st.session_state.framework = manual_framework

    # 4️⃣ Framework Explanation
    explainer = FrameworkExplainer()
    st.session_state.explanation = explainer.explain(
        st.session_state.framework, {}
    )

    # 5️⃣ Strategy Resolution
    resolver = StrategyResolver()
    st.session_state.scored_features = resolver.resolve(
        st.session_state.framework,
        st.session_state.features
    )

    # 6️⃣ Roadmap Generation
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
        "📐 Framework",
        "📊 Prioritization",
        "🗺 Roadmap"
    ])

    # -----------------------------
    with tabs[0]:
        st.subheader("Problem Summary")
        st.write(st.session_state.problem_summary)

    # -----------------------------
    with tabs[1]:
        st.subheader("Generated Feature Ideas")
        for feature in st.session_state.features:
            st.markdown(f"- {feature}")

    # -----------------------------
    with tabs[2]:
        st.success(f"Selected Framework: **{st.session_state.framework}**")

        with st.expander("📘 Why this framework?"):
            st.info(st.session_state.explanation)

        with st.expander("⚖️ Framework Comparison"):
            comparison = FrameworkComparison()
            st.table(comparison.compare())

    # -----------------------------
    with tabs[3]:
        st.subheader("Feature Prioritization")
        st.dataframe(
            st.session_state.scored_features,
            width="stretch"
        )

    # -----------------------------
    with tabs[4]:
        st.subheader("Product Roadmap")
        for phase, items in st.session_state.roadmap.items():
            st.markdown(f"### {phase}")
            for item in items:
                st.markdown(f"- {item}")

    # --------------------------------------------------
    # PM REASONING (PHASE 2.1)
    # --------------------------------------------------
    st.divider()
    st.markdown("## 🧠 PM Reasoning")

    narrator = DecisionNarrator()

    st.markdown("### Framework Rationale")
    st.info(
        narrator.explain_framework_choice(
            st.session_state.framework
        )
    )

    st.markdown("### Prioritization Rationale")
    st.info(
        narrator.explain_prioritization(
            st.session_state.scored_features
        )
    )

    st.markdown("### Roadmap Rationale")
    st.info(
        narrator.explain_roadmap()
    )

    # --------------------------------------------------
    # EXPORT FULL ANALYSIS PDF
    # --------------------------------------------------
    st.divider()
    st.markdown("## 📤 Export Full Analysis")

    exporter = RoadmapExporter()

    analysis_data = {
        "problem": st.session_state.problem_summary,
        "features": st.session_state.features,
        "framework": st.session_state.framework,
        "explanation": st.session_state.explanation,
        "prioritization": st.session_state.scored_features,
        "roadmap": st.session_state.roadmap
    }

    if st.button("📄 Generate Full Analysis PDF"):
        pdf_path = exporter.export_full_analysis(analysis_data)

        with open(pdf_path, "rb") as f:
            st.download_button(
                label="⬇️ Download PDF",
                data=f,
                file_name=pdf_path.split("/")[-1],
                mime="application/pdf"
            )

        st.success("Full analysis PDF generated successfully!")

# --------------------------------------------------
# EMPTY STATE
# --------------------------------------------------
elif run_clicked:
    st.warning("Please enter a product problem to continue.")
