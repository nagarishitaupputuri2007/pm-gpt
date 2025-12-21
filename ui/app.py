# ui/app.py
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

st.title("🚀 PM-GPT — Product Management Copilot")
st.caption("Problems → Features → Strategy → Roadmap")
st.divider()


# --------------------------------------------------
# SESSION STATE
# --------------------------------------------------
if "analysis_ready" not in st.session_state:
    st.session_state.analysis_ready = False

if "analysis_data" not in st.session_state:
    st.session_state.analysis_data = None


# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------
st.sidebar.header("⚙️ Configuration")

decision_mode = st.sidebar.radio(
    "Framework Selection Mode",
    ["Auto (PM-GPT decides)", "Manual (I choose framework)"]
)

manual_framework = None
if decision_mode == "Manual (I choose framework)":
    manual_framework = st.sidebar.selectbox(
        "Choose Framework",
        ["RICE", "ICE", "MoSCoW", "Kano"]
    )

run_clicked = st.sidebar.button("🚀 Run PM-GPT")


# --------------------------------------------------
# INPUT
# --------------------------------------------------
st.subheader("🧠 Describe the Product Problem")

problem_text = st.text_area(
    "Product Problem",
    placeholder=(
        "Example: Users drop off during onboarding due to KYC failures, "
        "increasing support costs and delaying first transaction completion."
    ),
    height=160,
    label_visibility="collapsed"
)


# --------------------------------------------------
# RUN PIPELINE
# --------------------------------------------------
if run_clicked:
    st.session_state.analysis_ready = False
    st.session_state.analysis_data = None

    if problem_text.strip():
        problem_mapper = ProblemMapper()
        problem_data = problem_mapper.map(problem_text)

        feature_generator = FeatureGenerator()
        features = feature_generator.generate(problem_data.get("summary", ""))

        if decision_mode == "Auto (PM-GPT decides)":
            framework_selector = FrameworkSelector()
            framework = framework_selector.select(problem_text)
        else:
            framework = manual_framework

        framework_explainer = FrameworkExplainer()
        framework_explanation = framework_explainer.explain(framework, {})

        strategy_resolver = StrategyResolver()
        scored_features = strategy_resolver.resolve(framework, features)

        roadmap_generator = RoadmapGenerator()
        roadmap = roadmap_generator.generate(scored_features)

        st.session_state.analysis_data = {
            "problem": problem_data,
            "features": features,
            "framework": framework,
            "framework_explanation": framework_explanation,
            "prioritization": scored_features,
            "roadmap": roadmap
        }

        st.session_state.analysis_ready = True
    else:
        st.warning("Please describe a product problem to continue.")


# --------------------------------------------------
# OUTPUT
# --------------------------------------------------
if st.session_state.analysis_ready:
    data = st.session_state.analysis_data
    problem = data.get("problem", {})

    tabs = st.tabs([
        "🧩 Problem Insight",
        "🛠 Features",
        "📐 Framework",
        "📊 Prioritization",
        "🗺 Roadmap"
    ])

    # -------------------------
    # PROBLEM INSIGHT (REFINED)
    # -------------------------
    with tabs[0]:
        st.subheader("🚨 Core Problem")
        st.error(problem.get("core_problem", "Not identified"))

        st.subheader("❌ Critical Failure Point")
        st.warning(problem.get("user_failure_point", "Not specified"))

        st.subheader("📉 Business Impact")
        for impact in problem.get("business_impact", []):
            st.markdown(f"- {impact}")

        st.subheader("⛓ Constraints")
        for c in problem.get("constraints", []):
            st.markdown(f"- {c}")

        st.subheader("🎯 Success Definition")
        st.success(problem.get("success_definition", "Not defined"))

        st.divider()
        st.subheader("🧠 PM Verdict")
        st.info(problem.get("summary", ""))

    # -------------------------
    # FEATURES
    # -------------------------
    with tabs[1]:
        st.subheader("Generated Feature Ideas")
        for f in data["features"]:
            st.markdown(f"- {f}")

    # -------------------------
    # FRAMEWORK
    # -------------------------
    with tabs[2]:
        st.subheader("Selected Framework")
        st.success(data["framework"])
        st.info(data["framework_explanation"])

        with st.expander("⚖️ Framework Comparison"):
            comparison = FrameworkComparison()
            st.table(comparison.compare())

    # -------------------------
    # PRIORITIZATION
    # -------------------------
    with tabs[3]:
        st.subheader("Feature Prioritization")
        for item in data["prioritization"]:
            st.markdown(f"- **{item['feature']}** (score: {item['score']})")

    # -------------------------
    # ROADMAP
    # -------------------------
    with tabs[4]:
        st.subheader("6-Month Product Roadmap")
        for phase, items in data["roadmap"].items():
            st.markdown(f"### {phase}")
            for item in items:
                st.markdown(f"- {item}")

    # -------------------------
    # EXPORT
    # -------------------------
    st.divider()
    exporter = RoadmapExporter()

    if st.button("📄 Generate Full Analysis PDF"):
        pdf_path = exporter.export_full_analysis(data)
        with open(pdf_path, "rb") as f:
            st.download_button(
                "⬇️ Download PDF",
                data=f,
                file_name=pdf_path.split("/")[-1],
                mime="application/pdf"
            )
