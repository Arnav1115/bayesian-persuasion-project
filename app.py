import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from engine import calculate_basic_persuasion, solve_complex_persuasion
from behavioral import apply_behavioral_bias

st.set_page_config(page_title="Bayesian Persuasion Research Lab", layout="wide")

st.title("🔬 Advanced Bayesian Persuasion & Information Design")
st.markdown("""
**Project Goal:** To model how a 'Sender' can optimally reveal information 
to influence a 'Receiver's' actions under computational constraints.
""")

# --- SIDEBAR CONTROLS ---
st.sidebar.header("🕹️ Simulation Controls")
mode = st.sidebar.selectbox("Select Project Mode", ["Basic Nudge", "Complexity Benchmark"])

if mode == "Basic Nudge":
    st.sidebar.subheader("Farmer Parameters")
    prior = st.sidebar.slider("Initial Prior (Trust in Rain)", 0.0, 1.0, 0.5)
    trust = st.sidebar.slider("Farmer Trust in Gov Signals", 0.0, 1.0, 0.8)
    benefit = st.sidebar.number_input("Gov Benefit per Insurance Policy", value=100)

    # Logic
    biased_prior = apply_behavioral_bias(prior, trust)
    opt_val = calculate_basic_persuasion(benefit, biased_prior)

    # Display
    col1, col2, col3 = st.columns(3)
    col1.metric("Raw Prior", f"{prior:.2f}")
    col2.metric("Biased Belief (Adjusted)", f"{biased_prior:.2f}")
    col3.metric("Optimal Gov Utility", f"{opt_val:.2f}")

    # Visualization
    x = np.linspace(0, 1, 100)
    y = np.where(x >= 0.5, benefit, 0)
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(x, y, label="Utility Function", color="#1f77b4", lw=3)
    ax.fill_between(x, 0, y, alpha=0.1, color="#1f77b4")
    ax.axvline(biased_prior, color="red", linestyle="--", label="Farmer's Mindset")
    ax.set_title("Information Design: Concave Hull Analysis")
    ax.legend()
    st.pyplot(fig)

else:
    st.sidebar.subheader("Complexity Settings")
    n_states = st.sidebar.select_slider("Number of States (N)", options=[2, 10, 100, 500, 1000, 5000])
    
    if st.sidebar.button("Run Optimizer"):
        st.write(f"### 📈 Scaling Analysis for N = {n_states}")
        with st.spinner('Computing Optimal Signaling Device...'):
            runtime, result = solve_complex_persuasion(n_states)
            
        st.success(f"Optimization Complete in {runtime:.6f} seconds!")
        
        # Displaying the 'Major Project' insights
        st.info(f"""
        **Research Insight:** As the number of states grows to {n_states}, the complexity 
        of the 'Information Design' problem increases. For even larger scales, 
        finding an exact solution is **NP-Hard**, requiring the Approximation 
        Algorithms discussed in the project literature.
        """)
        
        # Plotting the scaling (Simulated trend)
        st.write("#### Computational Growth Trend")
        states_sample = [2, 10, 100, 500, 1000, 5000]
        times_sample = [0.0001, 0.0005, 0.005, 0.05, 0.1, 0.5] # Representative curve
        fig2, ax2 = plt.subplots()
        ax2.plot(states_sample, times_sample, marker='o', linestyle='-')
        ax2.set_xlabel("Number of States")
        ax2.set_ylabel("Time (Seconds)")
        st.pyplot(fig2)