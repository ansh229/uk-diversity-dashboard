import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Load and clean data
def load_data():
    df = pd.read_csv("./figure-6.csv")
    df = df.dropna(subset=[df.columns[0], df.columns[1]])
    df.columns = [
        "Title",
        "Group",
        "Region",
        "Contract Type",
        "Job Role",
        "Count"
    ]
    df = df.dropna()
    df = df[df['Count'].apply(lambda x: str(x).isdigit())]
    df['Count'] = df['Count'].astype(int)
    return df

# Visualizations
def bar_chart(df, title):
    fig = px.bar(df, x='Group', y='Count', color='Region', title=title)
    st.plotly_chart(fig, use_container_width=True)

def pie_chart(df, title):
    fig = px.pie(df, names='Group', values='Count', title=title, hole=0.4)
    st.plotly_chart(fig, use_container_width=True)

def grouped_chart(df, title):
    fig = px.bar(df, x='Group', y='Count', color='Contract Type', barmode='group', title=title)
    st.plotly_chart(fig, use_container_width=True)

def treemap_chart(df, title):
    fig = px.treemap(df, path=['Region', 'Contract Type', 'Group'], values='Count', title=title)
    st.plotly_chart(fig, use_container_width=True)

def sunburst_chart(df, title):
    fig = px.sunburst(df, path=['Region', 'Contract Type', 'Group'], values='Count', title=title)
    st.plotly_chart(fig, use_container_width=True)

def stats_cards(df):
    total = df['Count'].sum()
    unique_groups = df['Group'].nunique()
    regions = df['Region'].nunique()
    contracts = df['Contract Type'].nunique()
    
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("👥 Total Staff", f"{total:,}")
    col2.metric("📌 Unique Groups", unique_groups)
    col3.metric("🌍 Regions", regions)
    col4.metric("📝 Contract Types", contracts)

# Main app
def main():
    st.set_page_config(page_title="UK Staff Diversity Dashboard", layout="wide")
    st.title("📊 UK Staff Diversity Analysis Dashboard")
    df = load_data()

    # Sidebar filters
    with st.sidebar:
        st.header("🔍 Filter Data")
        categories = df['Title'].unique().tolist()
        selected_category = st.selectbox("Select Category", categories)

        filtered_df = df[df['Title'] == selected_category]

        regions = st.multiselect("Select Regions", filtered_df['Region'].unique(), default=filtered_df['Region'].unique())
        filtered_df = filtered_df[filtered_df['Region'].isin(regions)]

        contract_types = st.multiselect("Select Contract Types", filtered_df['Contract Type'].unique(), default=filtered_df['Contract Type'].unique())
        filtered_df = filtered_df[filtered_df['Contract Type'].isin(contract_types)]

    # Top stats
    st.markdown("### 🔢 Summary Statistics")
    stats_cards(filtered_df)

    # Main visualizations
    st.markdown(f"### 📈 {selected_category} by Region and Contract Type")
    tab1, tab2, tab3, tab4, tab5 = st.tabs(["Bar Chart", "Donut Chart", "Grouped Comparison", "Treemap", "Sunburst"])

    with tab1:
        bar_chart(filtered_df, f"{selected_category} - Count by Group and Region")

    with tab2:
        pie_chart(filtered_df.groupby('Group', as_index=False)['Count'].sum(), f"{selected_category} - Proportion by Group")

    with tab3:
        grouped_chart(filtered_df, f"{selected_category} - Grouped by Contract Type")

    with tab4:
        treemap_chart(filtered_df, f"{selected_category} - Region > Contract > Group")

    with tab5:
        sunburst_chart(filtered_df, f"{selected_category} - Sunburst View")

    # Optional data view and export
    with st.expander("🔎 View Raw Filtered Data"):
        st.dataframe(filtered_df.reset_index(drop=True))
        csv = filtered_df.to_csv(index=False).encode('utf-8')
        st.download_button("📥 Download CSV", csv, "filtered_data.csv", "text/csv")

    st.markdown("---")
    st.caption("Developed for 5DATA004W – Data Science Project Lifecycle")

if __name__ == "__main__":
    main()
