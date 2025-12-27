# --------------------------------------------------
# STREAMLIT CLOUD PATH FIX (DO NOT REMOVE)
# --------------------------------------------------
import sys
import os

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

# --------------------------------------------------
# IMPORTS
# --------------------------------------------------
import streamlit as st

from product.problem_mapper import ProblemMapper
from product.feature_generator import FeatureGenerator
from product.framework_selector import FrameworkSelector
from product.framework_explainer import FrameworkExplainer
from product.framework_comparison import FrameworkComparison
from product.strategy_resolver import StrategyResolver
from product.decision_narrator import DecisionNarrator
from product.pm_judgment_engine import PMJudgmentEngine

from roadmap.roadmap_generator import RoadmapGenerator
from roadmap.roadmap_exporter import RoadmapExporter


# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------
st.set_page_config(
    page_title="PM-GPT | Product Management Copilot",
    layout="wide"
)

st.title("🚀 PM-GPT — Product Management Copilot")
st.caption("Problems → Features → Strategy → Roadmap → Decision Review")
st.divider()


# --------------------------------------------------
# SESSION STATE
# --------------------------------------------------
if "analysis_ready" not in st.session_state:
    st.session_state.analysis_ready = False

if "analysis_payload" not in st.session_state:
    st.session_state.analysis_payload = None

if "pdf_path" not in st.session_state:
    st.session_state.pdf_path = None


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
        "Example:\n"
        "Users abandon onboarding due to unclear verification steps, "
        "causing low activation and higher support costs."
    ),
    height=160,
    label_visibility="collapsed"
)


# --------------------------------------------------
# MAIN PIPELINE
# --------------------------------------------------
if run_clicked and problem_text.strip():

    # 1️⃣ Problem Mapping
    problem_data = ProblemMapper().map(problem_text)
    problem_type = problem_data.get("problem_type", "general")
    problem_summary = problem_data.get("summary", problem_text)

    # SAFE defaults
    business_impact = problem_data.get(
        "business_impact",
        [
            "Negative impact on key product metrics",
            "Increased risk of user churn",
            "Long-term business impact if unresolved"
        ]
    )

    constraints = problem_data.get(
        "constraints",
        [
            "Limited engineering capacity",
            "Need to balance speed with quality",
            "Execution risk must be managed"
        ]
    )

    # 2️⃣ Feature Generation
    features = FeatureGenerator().generate(
        problem_type=problem_type,
        summary=problem_summary
    )

    # 3️⃣ Framework Selection
    if decision_mode == "Auto (PM-GPT decides)":
        framework = FrameworkSelector().select(
            problem_type=problem_type,
            summary=problem_summary
        )
    else:
        framework = manual_framework

    framework_explanation = FrameworkExplainer().explain(framework, {})

    # 4️⃣ Prioritization
    scored_features = StrategyResolver().resolve(framework, features)

    # 5️⃣ Roadmap
    roadmap = RoadmapGenerator().generate(scored_features)

    # 6️⃣ Judgment
    narrator = DecisionNarrator()
    judgment = PMJudgmentEngine().generate(
        problem=problem_data.get("core_problem", problem_summary),
        constraints=constraints,
        prioritized_features=scored_features,
        roadmap=roadmap
    )

    # --------------------------------------------------
    # SAVE ANALYSIS
    # --------------------------------------------------
    def safe_call(fn, *args):
        try:
            return fn(*args)
        except TypeError:
            return fn(args[0])

    st.session_state.analysis_payload = {
        "problem": problem_data,
        "features": features,
        "framework": framework,
        "framework_explanation": framework_explanation,
        "prioritization": scored_features,
        "roadmap": roadmap,
        "reasoning": {
            "framework": safe_call(narrator.explain_framework_choice, framework, problem_type),
            "prioritization": safe_call(narrator.explain_prioritization, scored_features, problem_type),
            "roadmap": safe_call(narrator.explain_roadmap, problem_type),
            "tradeoffs": safe_call(narrator.explain_tradeoffs, problem_type),
            "metrics": safe_call(narrator.explain_success_metrics, problem_type),
        },
        "judgment": judgment
    }

    st.session_state.analysis_ready = True
    st.session_state.pdf_path = None


    # --------------------------------------------------
    # TABS
    # --------------------------------------------------
    tabs = st.tabs([
        "🧩 Problem Insight",
        "🛠 Features",
        "📐 Framework",
        "📊 Prioritization",
        "🗺 Roadmap",
        "🧠 Decision Review"
    ])

    # -------------------------
    # TAB 1: PROBLEM INSIGHT
    # -------------------------
    with tabs[0]:
        st.subheader("🚨 Core Problem")
        st.error(problem_data.get("core_problem", problem_summary))

        st.subheader("❌ Where Users Fail")
        st.warning(problem_data.get("user_failure_point", "User friction detected"))

        st.subheader("📉 Business Impact (Why This Matters)")
        for impact in business_impact:
            st.markdown(f"- {impact}")

        st.subheader("⛓️ Execution Constraints")
        for c in constraints:
            st.markdown(f"- {c}")

        st.subheader("🎯 Success Definition")
        st.success(problem_data.get("success_definition", "Improve key product outcomes"))

        st.divider()
        st.subheader("🧠 PM Narrative Summary")
        st.info(problem_summary)

    # -------------------------
    # TAB 2: FEATURES
    # -------------------------
    with tabs[1]:
        st.subheader("🛠 Generated Feature Ideas")
        for f in features:
            st.markdown(f"- {f}")

    # -------------------------
    # TAB 3: FRAMEWORK
    # -------------------------
    with tabs[2]:
        st.subheader("📐 Selected Framework")
        st.success(framework)
        st.info(framework_explanation)

        with st.expander("⚖️ Framework Comparison"):
            st.table(FrameworkComparison().compare())

    # -------------------------
    # TAB 4: PRIORITIZATION
    # -------------------------
    with tabs[3]:
        st.subheader("📊 Feature Prioritization")
        for item in scored_features:
            st.markdown(f"- **{item['feature']}** (score: {item['score']})")

    # -------------------------
    # TAB 5: ROADMAP
    # -------------------------
    with tabs[4]:
        st.subheader("🗺 6-Month Product Roadmap")
        for phase, items in roadmap.items():
            st.markdown(f"### {phase}")
            for item in items:
                st.markdown(f"- {item}")

    # -------------------------
    # TAB 6: DECISION REVIEW
    # -------------------------
    with tabs[5]:
        reasoning_tab, exec_tab = st.tabs(["🧠 PM Reasoning", "🏛 Executive Review"])

        with reasoning_tab:
            st.markdown("### 📌 Framework Rationale")
            st.info(st.session_state.analysis_payload["reasoning"]["framework"])

            st.markdown("### 📌 Prioritization Rationale")
            st.info(st.session_state.analysis_payload["reasoning"]["prioritization"])

            st.markdown("### 📌 Roadmap Rationale")
            st.info(st.session_state.analysis_payload["reasoning"]["roadmap"])

            st.markdown("### 📌 Trade-offs Considered")
            st.info(st.session_state.analysis_payload["reasoning"]["tradeoffs"])

            st.markdown("### 📌 Success Metrics")
            st.info(st.session_state.analysis_payload["reasoning"]["metrics"])

        with exec_tab:
            st.markdown("### ❌ What We Explicitly Did NOT Do")
            st.info(judgment.get("did_not_do", "No explicit exclusions documented."))

            st.markdown("### 🎯 Primary Bet")
            st.success(judgment.get("primary_bet", "Primary bet identified."))

            st.markdown("### ⚠️ Biggest Execution Risk")
            st.warning(judgment.get("execution_risk", "Execution risk identified."))

            st.markdown("### ⚖️ Key Trade-off")
            st.info(judgment.get("tradeoff", "Trade-off evaluated."))

            st.markdown("### 🧑‍💼 Leadership Pushback & PM Response")
            st.markdown(judgment.get("leadership_exchange", "No leadership objections recorded."))


# --------------------------------------------------
# EXPORT
# --------------------------------------------------
if st.session_state.analysis_ready:
    st.divider()
    st.subheader("📤 Export Full Analysis")

    exporter = RoadmapExporter()

    if st.session_state.pdf_path is None:
        if st.button("📄 Generate Full Analysis PDF"):
            st.session_state.pdf_path = exporter.export_full_analysis(
                st.session_state.analysis_payload
            )
            st.toast("✅ PDF generated successfully", icon="📄")

    if st.session_state.pdf_path:
        with open(st.session_state.pdf_path, "rb") as f:
            st.download_button(
                "⬇️ Download PDF",
                data=f,
                file_name=st.session_state.pdf_path.split("/")[-1],
                mime="application/pdf"
            )
