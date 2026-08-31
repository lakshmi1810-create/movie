import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

from analysis import (
    load_data,
    total_content,
    type_analysis,
    genre_analysis,
    language_analysis,
    platform_analysis,
    release_year_analysis,
    rating_analysis
)

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Netflix Analytics Dashboard",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

/* =========================================================
   GLOBAL / PAGE
   ========================================================= */

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background: #0b0b0f;
    color: #ffffff;
}

/* Fix the unnecessary top gap in the main dashboard */
.block-container {
    padding-top: 0.75rem !important;
    padding-bottom: 2rem !important;
    max-width: 100% !important;
}

/* Remove extra header space */
header[data-testid="stHeader"] {
    background: transparent !important;
}


/* =========================================================
   SIDEBAR
   ========================================================= */

section[data-testid="stSidebar"] {
    background: linear-gradient(
        180deg,
        #0d0d12 0%,
        #09090d 100%
    ) !important;

    border-right: 1px solid #25252d;
    min-width: 275px !important;
    max-width: 275px !important;
}

section[data-testid="stSidebar"] > div {
    padding: 1.15rem 1rem 1rem 1rem !important;
}

section[data-testid="stSidebar"] * {
    color: #eeeeee;
}


/* Sidebar brand */

.sidebar-title {
    font-size: 25px;
    font-weight: 800;
    color: #E50914 !important;
    letter-spacing: 0.5px;
    margin-bottom: 4px;
}

.sidebar-subtitle {
    color: #85858f !important;
    font-size: 12px;
    line-height: 1.5;
    margin-bottom: 20px;
}


/* Sidebar divider */

section[data-testid="stSidebar"] hr {
    border: none !important;
    border-top: 1px solid #222229 !important;
    margin: 16px 0 !important;
}


/* Navigation heading */

section[data-testid="stSidebar"] .stRadio > label {
    color: #777783 !important;
    font-size: 11px !important;
    font-weight: 700 !important;
    letter-spacing: 1.2px;
    text-transform: uppercase;
    margin-bottom: 8px !important;
}


/* Professional navigation buttons */

section[data-testid="stSidebar"] div[role="radiogroup"] {
    gap: 5px !important;
}

section[data-testid="stSidebar"] div[role="radiogroup"] label {
    position: relative;
    display: flex !important;
    align-items: center !important;
    width: 100% !important;
    min-height: 44px !important;

    background: #111117 !important;
    border: 1px solid #202027 !important;
    border-radius: 10px !important;

    padding: 0 14px !important;
    margin: 0 !important;

    color: #a7a7b2 !important;
    font-size: 13px !important;
    font-weight: 600 !important;

    cursor: pointer !important;
    transition: all 0.18s ease !important;
    box-sizing: border-box !important;
}


/* Hide radio circles */

section[data-testid="stSidebar"] div[role="radiogroup"] label > div:first-child {
    display: none !important;
}


/* Navigation text */

section[data-testid="stSidebar"] div[role="radiogroup"] label p {
    color: inherit !important;
    margin: 0 !important;
    padding: 0 !important;
}


/* Hover */

section[data-testid="stSidebar"] div[role="radiogroup"] label:hover {
    background: #19191f !important;
    border-color: #383842 !important;
    color: #ffffff !important;
    transform: translateX(2px);
}


/* Selected navigation button */

section[data-testid="stSidebar"] div[role="radiogroup"] label:has(input:checked) {
    background: linear-gradient(
        90deg,
        #E50914 0%,
        #b20710 100%
    ) !important;

    border-color: #E50914 !important;
    color: #ffffff !important;

    box-shadow: 0 7px 20px rgba(229, 9, 20, 0.20) !important;
}


/* Small active indicator */

section[data-testid="stSidebar"] div[role="radiogroup"] label:has(input:checked)::after {
    content: "";
    position: absolute;
    right: 12px;
    width: 6px;
    height: 6px;
    border-radius: 50%;
    background: #ffffff;
}


/* Database area */

section[data-testid="stSidebar"] .stCaption {
    color: #777783 !important;
    font-size: 11px !important;
    font-weight: 700 !important;
    letter-spacing: 0.8px;
}

section[data-testid="stSidebar"] .stAlert {
    background: #09251b !important;
    border: 1px solid #123d2d !important;
    border-radius: 10px !important;
    color: #d8f5e8 !important;
}

section[data-testid="stSidebar"] .stAlert p {
    color: #d8f5e8 !important;
    font-size: 12px !important;
}


/* =========================================================
   MAIN TITLES
   ========================================================= */

.main-title {
    font-size: 40px;
    font-weight: 800;
    color: #ffffff;
    margin: 0 0 4px 0;
    letter-spacing: -0.7px;
}

.main-subtitle {
    color: #92929d;
    font-size: 15px;
    margin: 0 0 26px 0;
}


/* =========================================================
   HERO
   ========================================================= */

.hero {
    position: relative;
    overflow: hidden;

    background:
        linear-gradient(
            100deg,
            rgba(229, 9, 20, 0.98) 0%,
            rgba(167, 5, 14, 0.90) 42%,
            rgba(62, 0, 4, 0.88) 100%
        );

    padding: 31px 36px;
    border-radius: 17px;

    margin: 0 0 22px 0;

    border: 1px solid rgba(255,255,255,0.08);
    box-shadow: 0 14px 38px rgba(0,0,0,0.30);
}

.hero::after {
    content: "NETFLIX";
    position: absolute;
    right: 28px;
    bottom: -16px;

    font-size: 80px;
    font-weight: 800;
    letter-spacing: -4px;

    color: rgba(255,255,255,0.055);
    pointer-events: none;
}

.hero h1 {
    position: relative;
    z-index: 1;

    font-size: 36px;
    font-weight: 800;
    margin: 0;
    color: white;
}

.hero p {
    position: relative;
    z-index: 1;

    color: #f8dddd;
    font-size: 14px;
    line-height: 1.6;
    max-width: 720px;
    margin: 8px 0 0 0;
}


/* =========================================================
   KPI CARDS
   ========================================================= */

.kpi {
    background: linear-gradient(
        145deg,
        #17171e 0%,
        #101015 100%
    );

    border: 1px solid #272731;
    border-radius: 14px;

    padding: 19px 20px;
    min-height: 105px;

    box-shadow: 0 7px 22px rgba(0,0,0,0.22);

    transition: all 0.2s ease;
}

.kpi:hover {
    border-color: #3b3b46;
    transform: translateY(-2px);
}

.kpi-label {
    color: #898995;
    font-size: 11px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.9px;
}

.kpi-value {
    color: #ffffff;
    font-size: 30px;
    font-weight: 800;
    margin-top: 8px;
}

.kpi-accent {
    color: #E50914;
}


/* =========================================================
   SECTION HEADINGS
   ========================================================= */

.section-title {
    font-size: 21px;
    font-weight: 750;
    color: #ffffff;
    margin-top: 26px;
    margin-bottom: 13px;
}


/* =========================================================
   MOVIE CARDS
   ========================================================= */

.movie-card {
    background: linear-gradient(
        145deg,
        #17171d,
        #111117
    );

    border: 1px solid #292932;
    border-radius: 13px;

    padding: 17px;
    margin-bottom: 13px;

    min-height: 125px;

    transition: all 0.2s ease;
}

.movie-card:hover {
    border-color: #E50914;
    transform: translateY(-2px);
    box-shadow: 0 8px 20px rgba(0,0,0,0.25);
}

.movie-title {
    font-size: 17px;
    font-weight: 700;
    color: #ffffff;
}

.movie-meta {
    color: #8f8f9a;
    font-size: 12px;
    line-height: 1.5;
    margin-top: 5px;
}

.badge {
    display: inline-block;
    background: #E50914;
    color: white;

    border-radius: 20px;
    padding: 4px 9px;

    font-size: 10px;
    font-weight: 700;

    margin-top: 9px;
}


/* =========================================================
   PLOTLY / DATAFRAME
   ========================================================= */

div[data-testid="stDataFrame"] {
    border-radius: 12px;
    overflow: hidden;
    border: 1px solid #292932;
}


/* =========================================================
   BUTTONS
   ========================================================= */

.stButton > button {
    background: #17171e !important;
    color: #ffffff !important;

    border: 1px solid #30303a !important;
    border-radius: 9px !important;

    font-weight: 600 !important;
    transition: all 0.2s ease !important;
}

.stButton > button:hover {
    background: #E50914 !important;
    border-color: #E50914 !important;
    color: white !important;
}


/* =========================================================
   SELECT BOXES
   ========================================================= */

div[data-baseweb="select"] > div {
    background-color: #17171e !important;
    border-color: #30303a !important;
    color: white !important;
    border-radius: 9px !important;
}

div[data-baseweb="select"] * {
    color: white !important;
}


/* =========================================================
   TEXT INPUTS
   ========================================================= */

.stTextInput input {
    background: #17171e !important;
    color: white !important;

    border: 1px solid #30303a !important;
    border-radius: 9px !important;
}

.stTextInput input:focus {
    border-color: #E50914 !important;
    box-shadow: 0 0 0 1px #E50914 !important;
}


/* =========================================================
   TABS
   ========================================================= */

button[data-baseweb="tab"] {
    color: #8f8f9a !important;
    font-weight: 600 !important;
}

button[data-baseweb="tab"][aria-selected="true"] {
    color: #ffffff !important;
}

div[data-baseweb="tab-highlight"] {
    background-color: #E50914 !important;
}


/* =========================================================
   ALERTS
   ========================================================= */

div[data-testid="stAlert"] {
    border-radius: 10px !important;
}


/* =========================================================
   DIVIDERS
   ========================================================= */

hr {
    border-color: #292932 !important;
}


/* =========================================================
   SCROLLBAR
   ========================================================= */

::-webkit-scrollbar {
    width: 7px;
}

::-webkit-scrollbar-track {
    background: #0b0b0f;
}

::-webkit-scrollbar-thumb {
    background: #34343d;
    border-radius: 10px;
}

::-webkit-scrollbar-thumb:hover {
    background: #E50914;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# LOAD DATA
# =========================================================

@st.cache_data(ttl=600)
def get_data():
    return load_data()


try:
    df = get_data()

except Exception as e:
    st.error("Unable to load data from MySQL database.")
    st.exception(e)
    st.stop()


# =========================================================
# DATA CLEANING
# =========================================================

df = df.copy()

# Standardize common columns

if "type" in df.columns:
    df["type"] = df["type"].astype(str).str.strip()

if "title" in df.columns:
    df["title"] = df["title"].astype(str).str.strip()

if "release_year" in df.columns:
    df["release_year"] = pd.to_numeric(
        df["release_year"],
        errors="coerce"
    )

if "rating" in df.columns:
    df["rating"] = pd.to_numeric(
        df["rating"],
        errors="coerce"
    )


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.markdown(
        '<div class="sidebar-title">NETFLIX</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="sidebar-subtitle">'
        'Analytics & Recommendation Platform'
        '</div>',
        unsafe_allow_html=True
    )

    st.divider()

    menu = st.radio(
        "NAVIGATION",
        [
            "Dashboard",
            "Content Explorer",
            "Search",
            "Recommendations",
            "Analytics",
            "Visualizations"
        ],
        label_visibility="visible"
    )

    st.divider()

    st.caption("DATABASE")

    st.success(
        f"● Connected  •  {len(df):,} records"
    )

    st.caption("Netflix Analytics Dashboard")


# =========================================================
# HELPER FUNCTIONS
# =========================================================

def kpi_card(label, value, accent=False):

    accent_class = "kpi-accent" if accent else ""

    st.markdown(
        f"""
        <div class="kpi">
            <div class="kpi-label">{label}</div>
            <div class="kpi-value {accent_class}">
                {value}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


def movie_card(row):

    title = row.get("title", "Unknown")
    content_type = row.get("type", "Unknown")
    year = row.get("release_year", "N/A")
    rating = row.get("rating", "N/A")
    genre = row.get("genre", "Unknown")

    st.markdown(
        f"""
        <div class="movie-card">
            <div class="movie-title">
                {title}
            </div>

            <div class="movie-meta">
                {content_type} &nbsp; • &nbsp;
                {year} &nbsp; • &nbsp;
                ⭐ {rating}
            </div>

            <div class="movie-meta">
                {genre}
            </div>

            <span class="badge">
                {content_type.upper()}
            </span>
        </div>
        """,
        unsafe_allow_html=True
    )


def dark_chart(fig):

    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor="#111116",
        plot_bgcolor="#111116",
        font_color="#ffffff",
        margin=dict(l=20, r=20, t=50, b=20),
        legend=dict(
            bgcolor="rgba(0,0,0,0)"
        )
    )

    return fig


# =========================================================
# DASHBOARD
# =========================================================

if menu == "Dashboard":

    st.markdown(
        """
        <div class="hero">
            <h1>🎬 Netflix Analytics</h1>
            <p>
                Explore your Netflix catalog, discover content,
                analyze trends and generate personalized recommendations.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    # -----------------------------------------------------
    # KPI SECTION
    # -----------------------------------------------------

    total = len(df)

    movie_count = len(
        df[
            df["type"]
            .astype(str)
            .str.lower()
            .eq("movie")
        ]
    )

    series_count = len(
        df[
            df["type"]
            .astype(str)
            .str.lower()
            .isin(["series", "tv show", "tv"])
        ]
    )

    genres_count = (
        df["genre"].nunique()
        if "genre" in df.columns
        else 0
    )

    languages_count = (
        df["language"].nunique()
        if "language" in df.columns
        else 0
    )

    c1, c2, c3, c4, c5 = st.columns(5)

    with c1:
        kpi_card("Total Content", f"{total:,}", True)

    with c2:
        kpi_card("Movies", f"{movie_count:,}")

    with c3:
        kpi_card("Series", f"{series_count:,}")

    with c4:
        kpi_card("Genres", f"{genres_count:,}")

    with c5:
        kpi_card("Languages", f"{languages_count:,}")

    # -----------------------------------------------------
    # CHARTS
    # -----------------------------------------------------

    st.markdown(
        '<div class="section-title">Content Overview</div>',
        unsafe_allow_html=True
    )

    col1, col2 = st.columns([1, 1])

    # Type chart

    with col1:

        type_result = type_analysis(df)

        fig = px.pie(
            values=type_result.values,
            names=type_result.index,
            hole=0.65,
            color_discrete_sequence=[
                "#E50914",
                "#8B0000",
                "#555555"
            ]
        )

        fig.update_traces(
            textinfo="percent+label"
        )

        fig.update_layout(
            title="Content Type",
            showlegend=False
        )

        st.plotly_chart(
            dark_chart(fig),
            use_container_width=True
        )

    # Genre chart

    with col2:

        genre_result = genre_analysis(df).head(8)

        fig = px.bar(
            x=genre_result.values,
            y=genre_result.index,
            orientation="h",
            color=genre_result.values,
            color_continuous_scale=[
                "#330000",
                "#E50914"
            ]
        )

        fig.update_layout(
            title="Top Genres",
            xaxis_title="Content",
            yaxis_title="",
            coloraxis_showscale=False
        )

        st.plotly_chart(
            dark_chart(fig),
            use_container_width=True
        )

    # -----------------------------------------------------
    # RELEASE TREND
    # -----------------------------------------------------

    if "release_year" in df.columns:

        year_data = (
            df["release_year"]
            .dropna()
            .astype(int)
            .value_counts()
            .sort_index()
        )

        fig = px.area(
            x=year_data.index,
            y=year_data.values,
            labels={
                "x": "Release Year",
                "y": "Content"
            }
        )

        fig.update_traces(
            line_color="#E50914",
            fillcolor="rgba(229,9,20,0.18)"
        )

        fig.update_layout(
            title="Content Release Trend"
        )

        st.plotly_chart(
            dark_chart(fig),
            use_container_width=True
        )

    # -----------------------------------------------------
    # LATEST CONTENT
    # -----------------------------------------------------

    st.markdown(
        '<div class="section-title">Latest Content</div>',
        unsafe_allow_html=True
    )

    latest = (
        df.dropna(subset=["release_year"])
        .sort_values(
            "release_year",
            ascending=False
        )
        .head(6)
    )

    cards = st.columns(3)

    for i, (_, row) in enumerate(latest.iterrows()):

        with cards[i % 3]:
            movie_card(row)


# =========================================================
# CONTENT EXPLORER
# =========================================================

elif menu == "Content Explorer":

    st.markdown(
        '<div class="main-title">Content Explorer</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="main-subtitle">'
        'Browse and filter the complete Netflix catalog.'
        '</div>',
        unsafe_allow_html=True
    )

    c1, c2, c3 = st.columns(3)

    with c1:

        types = ["All"] + sorted(
            df["type"]
            .dropna()
            .astype(str)
            .unique()
            .tolist()
        )

        selected_type = st.selectbox(
            "Content Type",
            types
        )

    with c2:

        if "platform" in df.columns:

            platforms = ["All"] + sorted(
                df["platform"]
                .dropna()
                .astype(str)
                .unique()
                .tolist()
            )

            selected_platform = st.selectbox(
                "Platform",
                platforms
            )

        else:
            selected_platform = "All"

    with c3:

        search = st.text_input(
            "Search title",
            placeholder="Search movies or series..."
        )

    filtered = df.copy()

    if selected_type != "All":

        filtered = filtered[
            filtered["type"]
            .astype(str)
            .eq(selected_type)
        ]

    if selected_platform != "All":

        filtered = filtered[
            filtered["platform"]
            .astype(str)
            .str.contains(
                selected_platform,
                case=False,
                na=False
            )
        ]

    if search:

        filtered = filtered[
            filtered["title"]
            .astype(str)
            .str.contains(
                search,
                case=False,
                na=False
            )
        ]

    st.info(
        f"Showing **{len(filtered):,}** of **{len(df):,}** records"
    )

    st.dataframe(
        filtered,
        use_container_width=True,
        hide_index=True,
        height=600
    )


# =========================================================
# SEARCH
# =========================================================

elif menu == "Search":

    st.markdown(
        '<div class="main-title">Search Netflix</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="main-subtitle">'
        'Find movies and series instantly.'
        '</div>',
        unsafe_allow_html=True
    )

    search = st.text_input(
        "Search",
        placeholder="Try: Stranger Things, Tom Cruise, Drama..."
    )

    if search:

        result = df[
            df.astype(str)
            .apply(
                lambda row: row.str.contains(
                    search,
                    case=False,
                    na=False
                ).any(),
                axis=1
            )
        ]

        st.success(
            f"{len(result):,} result(s) found"
        )

        if len(result) > 0:

            for _, row in result.head(12).iterrows():
                movie_card(row)

            if len(result) > 12:

                st.dataframe(
                    result,
                    use_container_width=True,
                    hide_index=True
                )

        else:

            st.warning(
                "No matching content found."
            )


# =========================================================
# RECOMMENDATIONS
# =========================================================

elif menu == "Recommendations":

    st.markdown(
        '<div class="main-title">Recommendations</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="main-subtitle">'
        'Discover content based on your preferences.'
        '</div>',
        unsafe_allow_html=True
    )

    recommendation_type = st.selectbox(
        "Recommendation method",
        [
            "By Type",
            "By Genre",
            "By Language",
            "By Platform",
            "By Actor"
        ]
    )

    result = pd.DataFrame()

    # -----------------------------------------------------
    # TYPE
    # -----------------------------------------------------

    if recommendation_type == "By Type":

        selected = st.selectbox(
            "Select content type",
            sorted(
                df["type"]
                .dropna()
                .astype(str)
                .unique()
            )
        )

        result = df[
            df["type"]
            .astype(str)
            .str.lower()
            .eq(selected.lower())
        ]

    # -----------------------------------------------------
    # GENRE
    # -----------------------------------------------------

    elif recommendation_type == "By Genre":

        genres = genre_analysis(df)

        selected = st.selectbox(
            "Select genre",
            genres.index.tolist()
        )

        result = df[
            df["genre"]
            .astype(str)
            .str.contains(
                selected,
                case=False,
                na=False
            )
        ]

    # -----------------------------------------------------
    # LANGUAGE
    # -----------------------------------------------------

    elif recommendation_type == "By Language":

        languages = language_analysis(df)

        selected = st.selectbox(
            "Select language",
            languages.index.tolist()
        )

        result = df[
            df["language"]
            .astype(str)
            .str.contains(
                selected,
                case=False,
                na=False
            )
        ]

    # -----------------------------------------------------
    # PLATFORM
    # -----------------------------------------------------

    elif recommendation_type == "By Platform":

        platforms = sorted(
            df["platform"]
            .dropna()
            .astype(str)
            .unique()
        )

        selected = st.selectbox(
            "Select platform",
            platforms
        )

        result = df[
            df["platform"]
            .astype(str)
            .str.contains(
                selected,
                case=False,
                na=False
            )
        ]

    # -----------------------------------------------------
    # ACTOR
    # -----------------------------------------------------

    elif recommendation_type == "By Actor":

        actor = st.text_input(
            "Enter actor or actress name",
            placeholder="e.g. Leonardo DiCaprio"
        )

        if actor:

            result = df[
                df["actors"]
                .astype(str)
                .str.contains(
                    actor,
                    case=False,
                    na=False
                )
            ]

    # -----------------------------------------------------
    # DISPLAY
    # -----------------------------------------------------

    if len(result) > 0:

        st.success(
            f"{len(result):,} recommendation(s) found"
        )

        display_result = result.head(12)

        cards = st.columns(3)

        for i, (_, row) in enumerate(
            display_result.iterrows()
        ):

            with cards[i % 3]:
                movie_card(row)

        if len(result) > 12:

            with st.expander(
                f"View all {len(result):,} results"
            ):

                st.dataframe(
                    result,
                    use_container_width=True,
                    hide_index=True
                )

    elif recommendation_type == "By Actor":

        st.info(
            "Enter an actor or actress name to get recommendations."
        )

    else:

        st.warning(
            "No content found for this selection."
        )


# =========================================================
# ANALYTICS
# =========================================================

elif menu == "Analytics":

    st.markdown(
        '<div class="main-title">Analytics</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="main-subtitle">'
        'Explore statistical insights from your catalog.'
        '</div>',
        unsafe_allow_html=True
    )

    tab1, tab2, tab3, tab4 = st.tabs(
        [
            "📦 Content",
            "🎭 Genres",
            "🌎 Languages",
            "⭐ Ratings"
        ]
    )

    # -----------------------------------------------------
    # CONTENT
    # -----------------------------------------------------

    with tab1:

        type_result = type_analysis(df)

        c1, c2 = st.columns(2)

        with c1:

            st.metric(
                "Total Content",
                f"{len(df):,}"
            )

        with c2:

            st.metric(
                "Content Types",
                len(type_result)
            )

        st.dataframe(
            type_result.rename("Count"),
            use_container_width=True
        )

    # -----------------------------------------------------
    # GENRES
    # -----------------------------------------------------

    with tab2:

        genre_result = genre_analysis(df)

        st.dataframe(
            genre_result.rename("Count"),
            use_container_width=True
        )

    # -----------------------------------------------------
    # LANGUAGES
    # -----------------------------------------------------

    with tab3:

        language_result = language_analysis(df)

        st.dataframe(
            language_result.rename("Count"),
            use_container_width=True
        )

    # -----------------------------------------------------
    # RATINGS
    # -----------------------------------------------------

    with tab4:

        highest, lowest, average = rating_analysis(df)

        c1, c2, c3 = st.columns(3)

        with c1:
            kpi_card(
                "Highest Rating",
                highest,
                True
            )

        with c2:
            kpi_card(
                "Lowest Rating",
                lowest
            )

        with c3:
            kpi_card(
                "Average Rating",
                round(average, 2)
            )


# =========================================================
# VISUALIZATIONS
# =========================================================

elif menu == "Visualizations":

    st.markdown(
        '<div class="main-title">Visualizations</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="main-subtitle">'
        'Interactive charts for deeper exploration.'
        '</div>',
        unsafe_allow_html=True
    )

    visualization = st.selectbox(
        "Choose visualization",
        [
            "Movies vs Series",
            "Top Genres",
            "Languages",
            "Platforms",
            "Release Trend",
            "Rating Distribution"
        ]
    )

    # -----------------------------------------------------
    # MOVIES VS SERIES
    # -----------------------------------------------------

    if visualization == "Movies vs Series":

        result = type_analysis(df)

        fig = px.bar(
            x=result.index,
            y=result.values,
            color=result.index,
            color_discrete_sequence=[
                "#E50914",
                "#6c0000"
            ]
        )

        fig.update_layout(
            title="Movies vs Series",
            xaxis_title="Content Type",
            yaxis_title="Number of Titles",
            showlegend=False
        )

        st.plotly_chart(
            dark_chart(fig),
            use_container_width=True
        )

    # -----------------------------------------------------
    # GENRES
    # -----------------------------------------------------

    elif visualization == "Top Genres":

        result = genre_analysis(df).head(15)

        fig = px.bar(
            x=result.values,
            y=result.index,
            orientation="h",
            color=result.values,
            color_continuous_scale=[
                "#300000",
                "#E50914"
            ]
        )

        fig.update_layout(
            title="Top 15 Genres",
            xaxis_title="Number of Titles",
            yaxis_title="Genre",
            coloraxis_showscale=False
        )

        st.plotly_chart(
            dark_chart(fig),
            use_container_width=True
        )

    # -----------------------------------------------------
    # LANGUAGES
    # -----------------------------------------------------

    elif visualization == "Languages":

        result = language_analysis(df).head(15)

        fig = px.bar(
            x=result.values,
            y=result.index,
            orientation="h",
            color=result.values,
            color_continuous_scale="Reds"
        )

        fig.update_layout(
            title="Top Languages",
            xaxis_title="Content",
            yaxis_title="Language",
            coloraxis_showscale=False
        )

        st.plotly_chart(
            dark_chart(fig),
            use_container_width=True
        )

    # -----------------------------------------------------
    # PLATFORMS
    # -----------------------------------------------------

    elif visualization == "Platforms":

        result = platform_analysis(df)

        fig = px.bar(
            x=result.index,
            y=result.values,
            color=result.index,
            color_discrete_sequence=[
                "#E50914",
                "#990000",
                "#555555",
                "#777777"
            ]
        )

        fig.update_layout(
            title="Platform Distribution",
            xaxis_title="Platform",
            yaxis_title="Number of Titles",
            showlegend=False
        )

        st.plotly_chart(
            dark_chart(fig),
            use_container_width=True
        )

    # -----------------------------------------------------
    # RELEASE TREND
    # -----------------------------------------------------

    elif visualization == "Release Trend":

        year_count = (
            df["release_year"]
            .dropna()
            .astype(int)
            .value_counts()
            .sort_index()
        )

        fig = px.line(
            x=year_count.index,
            y=year_count.values,
            markers=True
        )

        fig.update_traces(
            line_color="#E50914",
            marker_color="#ffffff"
        )

        fig.update_layout(
            title="Content Release Trend",
            xaxis_title="Release Year",
            yaxis_title="Number of Releases"
        )

        st.plotly_chart(
            dark_chart(fig),
            use_container_width=True
        )

    # -----------------------------------------------------
    # RATINGS
    # -----------------------------------------------------

    elif visualization == "Rating Distribution":

        rating_data = df["rating"].dropna()

        fig = px.histogram(
            rating_data,
            nbins=15,
            color_discrete_sequence=[
                "#E50914"
            ]
        )

        fig.update_layout(
            title="Rating Distribution",
            xaxis_title="Rating",
            yaxis_title="Number of Titles"
        )

        st.plotly_chart(
            dark_chart(fig),
            use_container_width=True
        )


# =========================================================
# FOOTER
# =========================================================

st.markdown(
    """
    <br><br>
    <div style="
        text-align:center;
        color:#666670;
        padding:20px;
        border-top:1px solid #24242c;
    ">
        🎬 Netflix Analytics Dashboard
        <br>
        <small>Built with Streamlit • Pandas • Plotly • MySQL</small>
    </div>
    """,
    unsafe_allow_html=True
)
