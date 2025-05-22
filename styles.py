import streamlit as st

def apply_styles():
    """Apply custom styles to the Streamlit app."""
    # Custom CSS to enhance the UI
    st.markdown("""
        <style>
        /* Card styling for challenges */
        .stExpander {
            border-radius: 8px;
            border: 1px solid rgba(49, 51, 63, 0.2);
            margin-bottom: 1rem;
        }
        
        /* Improve button styling */
        .stButton button {
            width: 100%;
            border-radius: 5px;
            font-weight: 500;
        }
        
        /* Header styling */
        h1, h2, h3 {
            margin-top: 0;
        }
        
        /* Footer attribution */
        .footer {
            position: fixed;
            bottom: 0;
            right: 0;
            padding: 5px 10px;
            font-size: 0.8rem;
            color: #888;
        }
        
        /* Timer styling */
        .timer {
            font-family: monospace;
            font-size: 2rem;
            text-align: center;
            margin: 1rem 0;
        }
        
        /* Add bottom padding to main content to avoid overlap with footer */
        .main .block-container {
            padding-bottom: 60px;
        }
        </style>
    """, unsafe_allow_html=True)
    
    # Add footer attribution
    st.markdown(
        """
        <div class="footer">Created by S.Tamilselvan</div>
        """,
        unsafe_allow_html=True
    )
