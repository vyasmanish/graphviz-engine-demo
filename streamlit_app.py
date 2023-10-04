import graphviz as graphviz
import streamlit as st

engine = st.sidebar.radio(
    "Select engine", ["dot", "neato", "twopi", "circo", "fdp", "osage", "patchwork"]
)
finite = graphviz.Digraph("finite_state_machine", engine=engine)
finite.attr(rankdir="LR", size="8,5")

finite.attr("node", shape="doublecircle")
finite.node("LR_0")
finite.node("LR_3")
finite.node("LR_4")
finite.node("LR_8")

finite.attr("node", shape="circle")
finite.edge("LR_0", "LR_2", label="SS(B)")
finite.edge("LR_0", "LR_1", label="SS(S)")
finite.edge("LR_1", "LR_3", label="S($end)")
finite.edge("LR_2", "LR_6", label="SS(b)")
finite.edge("LR_2", "LR_5", label="SS(a)")
finite.edge("LR_2", "LR_4", label="S(A)")
finite.edge("LR_5", "LR_7", label="S(b)")
finite.edge("LR_5", "LR_5", label="S(a)")
finite.edge("LR_6", "LR_6", label="S(b)")
finite.edge("LR_6", "LR_5", label="S(a)")
finite.edge("LR_7", "LR_8", label="S(b)")
finite.edge("LR_7", "LR_5", label="S(a)")
finite.edge("LR_8", "LR_6", label="S(b)")
finite.edge("LR_8", "LR_5", label="S(a)")

st.graphviz_chart(finite)
