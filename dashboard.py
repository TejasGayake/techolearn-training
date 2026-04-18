
# ===============================
# dashboard.py - Streamlit Trading Dashboard
# ===============================

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import time
from datetime import datetime

# Import your existing modules
from data.processor import TickProcessor
from indicators.calculator import IndicatorCalculator
from angel_api.client import AngelAPIClient

# Page configuration
st.set_page_config(
    page_title="Live Trading Dashboard",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .stAlert {
        font-size: 14px;
    }
    .positive {
        color: #00ff00;
    }
    .negative {
        color: #ff0000;
    }
</style>
""", unsafe_allow_html=True)

# ============================================
# INITIALIZE YOUR EXISTING SYSTEM
# ============================================
@st.cache_resource
def initialize_system():
    """Initialize your existing trading system"""
    from config.credentials import API_KEY, CLIENT_ID, PASSWORD, TOTP_SECRET
    
    api_client = AngelAPIClient(API_KEY, CLIENT_ID, PASSWORD, TOTP_SECRET)
    indicator_calc = IndicatorCalculator(api_client)
    processor = TickProcessor(indicator_calc, None, api_client)
    
    return processor, indicator_calc

# ============================================
# DASHBOARD HEADER
# ============================================
st.title("📈 Live Trading Dashboard")
st.caption(f"Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

# Sidebar
with st.sidebar:
    st.header("⚙️ Controls")
    
    # Token management
    st.subheader("📋 Watchlist")
    tokens_input = st.text_area(
        "Enter tokens (one per line)",
        placeholder="5097\n4503\n11351\n21690\n25049"
    )
    
    if st.button("➕ Update Watchlist"):
        tokens = [t.strip() for t in tokens_input.split("\n") if t.strip()]
        st.success(f"✅ Watching {len(tokens)} tokens")
        st.session_state['tokens'] = tokens
    
    # Refresh rate
    refresh_rate = st.slider("Refresh Rate (seconds)", 1, 10, 2)
    
    # Show/Hide options
    show_chart = st.checkbox("Show Chart", value=True)
    show_alerts = st.checkbox("Show Alerts", value=True)

# ============================================
# MAIN CONTENT LAYOUT
# ============================================

# Create placeholders for dynamic content
watchlist_placeholder = st.empty()
chart_placeholder = st.empty()
alerts_placeholder = st.empty()

# ============================================
# SIMULATED DATA (Replace with your actual data)
# ============================================
def get_sample_data():
    """Replace this with your actual live data"""
    data = {
        'SYMBOL': ['ETERNAL-EQ', 'MPHASIS-EQ', 'PETRONET-EQ', 'PREMIERENE-EQ', 'DIXON-EQ'],
        'LTP': [241.98, 2132.01, 249.52, 914.92, 10411.00],
        'CHANGE': [5.2, -12.3, 1.8, 3.5, -24.0],
        'CHANGE%': [2.19, -0.57, 0.73, 0.38, -0.23],
        'VOLUME': [552145, 12302, 164143, 50138, 7771],
        'RSI14': [57.2, 75.0, 63.4, 52.3, 45.9],
        'ALERT': ['', '🔴 OVERBOUGHT', '', '', '']
    }
    return pd.DataFrame(data)

# ============================================
# 1. WATCHLIST TABLE
# ============================================
def display_watchlist():
    df = get_sample_data()
    
    # Color formatting for CHANGE column
    def color_change(val):
        if isinstance(val, (int, float)):
            if val > 0:
                return 'color: #00ff00'
            elif val < 0:
                return 'color: #ff0000'
        return ''
    
    styled_df = df.style.applymap(color_change, subset=['CHANGE', 'CHANGE%'])
    
    watchlist_placeholder.dataframe(
        styled_df,
        use_container_width=True,
        height=300
    )

# ============================================
# 2. CANDLESTICK CHART
# ============================================
def display_chart(symbol="ETERNAL-EQ"):
    # Sample candlestick data (replace with your historical data)
    import numpy as np
    
    dates = pd.date_range(end=datetime.now(), periods=100, freq='5min')
    np.random.seed(42)
    
    # Generate sample OHLC data
    base_price = 240
    prices = base_price + np.cumsum(np.random.randn(100) * 2)
    
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, 
                        vertical_spacing=0.03, row_heights=[0.7, 0.3])
    
    # Candlestick chart
    fig.add_trace(go.Candlestick(
        x=dates,
        open=prices * 0.99,
        high=prices * 1.01,
        low=prices * 0.98,
        close=prices,
        name=symbol
    ), row=1, col=1)
    
    # Volume chart
    volumes = np.random.randint(100000, 1000000, 100)
    fig.add_trace(go.Bar(x=dates, y=volumes, name="Volume", marker_color='gray'), row=2, col=1)
    
    fig.update_layout(
        title=f"{symbol} - Live Chart",
        xaxis_title="Time",
        yaxis_title="Price",
        height=500,
        template="plotly_dark"
    )
    
    chart_placeholder.plotly_chart(fig, use_container_width=True)

# ============================================
# 3. ALERTS PANEL
# ============================================
def display_alerts():
    alerts = [
        {"time": "14:35:22", "symbol": "MPHASIS-EQ", "message": "RSI above 70 (Overbought)", "type": "warning"},
        {"time": "14:32:15", "symbol": "LTF-EQ", "message": "Price below L4 (Support broken)", "type": "error"},
        {"time": "14:30:01", "symbol": "WAAREEENER-EQ", "message": "Price above H4 (Breakout)", "type": "info"},
    ]
    
    for alert in alerts:
        if alert['type'] == 'warning':
            alerts_placeholder.warning(f"🔔 {alert['time']} - {alert['symbol']}: {alert['message']}")
        elif alert['type'] == 'error':
            alerts_placeholder.error(f"🔴 {alert['time']} - {alert['symbol']}: {alert['message']}")
        else:
            alerts_placeholder.info(f"ℹ️ {alert['time']} - {alert['symbol']}: {alert['message']}")

# ============================================
# MAIN LOOP (Auto-refresh)
# ============================================
def main_loop():
    while True:
        display_watchlist()
        
        if show_chart:
            # Get selected token from watchlist
            selected_token = "ETERNAL-EQ"  # You can add a selector
            display_chart(selected_token)
        
        if show_alerts:
            display_alerts()
        
        time.sleep(refresh_rate)

# ============================================
# RUN THE DASHBOARD
# ============================================
if __name__ == "__main__":
    st.info("🚀 Dashboard is running. Data refreshes every 2 seconds...")
    
    # For Streamlit, we use st.rerun() instead of a loop
    # This is a simplified version
    display_watchlist()
    if show_chart:
        display_chart()
    if show_alerts:
        display_alerts()
    
    # Auto-refresh using st.rerun
    import time
    time.sleep(refresh_rate)
    st.rerun()