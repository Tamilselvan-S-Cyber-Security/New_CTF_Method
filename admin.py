import streamlit as st
import json
import os
import time
from data.easy_challenges import easy_challenges
from data.medium_challenges import medium_challenges

def is_admin():
    """Check if the current user has admin privileges."""
    if 'user_info' in st.session_state and 'is_admin' in st.session_state.user_info:
        return st.session_state.user_info.get('is_admin', False)
    return False

def admin_login():
    """Display admin login form."""
    st.markdown("## Admin Login")
    st.info("Enter admin credentials to access the admin panel.")
    
    with st.form("admin_login_form"):
        admin_username = st.text_input("Admin Username")
        admin_password = st.text_input("Admin Password", type="password")
        submit_button = st.form_submit_button("Login")
        
        if submit_button:
            # Simple admin credentials check (you should use more secure methods in production)
            # For demo purposes, the admin credentials are hardcoded
            if admin_username == "admin" and admin_password == "ctfadmin123":
                st.session_state.user_info['is_admin'] = True
                st.success("Admin login successful!")
                time.sleep(1)
                st.rerun()
            else:
                st.error("Invalid admin credentials.")

def save_challenges_to_file(challenges, file_path):
    """Save updated challenges to the specified file."""
    # Format the challenges in Python code format
    code = "# This file contains challenge data for the CTF platform\n\n"
    code += f"{os.path.basename(file_path).split('.')[0]} = [\n"
    
    for challenge in challenges:
        code += "    {\n"
        for key, value in challenge.items():
            if isinstance(value, str):
                # Handle multi-line strings
                if '\n' in value:
                    code += f'        "{key}": """\n{value}\n""",\n'
                else:
                    code += f'        "{key}": "{value}",\n'
            else:
                code += f'        "{key}": {value},\n'
        code += "    },\n"
    
    code += "]\n"
    
    # Write to file
    with open(file_path, "w") as f:
        f.write(code)

def admin_panel():
    """Display the admin panel for challenge management."""
    if not is_admin():
        admin_login()
        return
    
    st.markdown("# Admin Panel")
    st.info("Manage your CTF challenges from this admin panel.")
    
    # Tab selection for different admin functions
    tab1, tab2 = st.tabs(["Manage Challenges", "User Management"])
    
    with tab1:
        st.markdown("## Challenge Management")
        category = st.selectbox("Select Category", ["Easy", "Medium"])
        
        if category == "Easy":
            manage_category_challenges(easy_challenges, "data/easy_challenges.py")
        else:
            manage_category_challenges(medium_challenges, "data/medium_challenges.py")
    
    with tab2:
        st.markdown("## User Management")
        st.info("User management features coming soon.")
        # Placeholder for user management features

def manage_category_challenges(challenges, file_path):
    """Manage challenges for a specific category."""
    # Make a copy of the challenges to avoid modifying the original list
    challenges_copy = challenges.copy()
    
    # Display existing challenges
    st.subheader("Existing Challenges")
    for idx, challenge in enumerate(challenges_copy):
        with st.expander(f"{idx+1}. {challenge['name']}"):
            st.write(f"**Description:** {challenge['description']}")
            st.write(f"**Points:** {challenge['points']}")
            st.write(f"**Flag:** {challenge['flag']}")
            st.write(f"**Difficulty:** {challenge['difficulty']}")
            
            # Edit challenge button
            if st.button(f"Edit Challenge #{idx+1}", key=f"edit_{idx}"):
                st.session_state.editing_challenge = idx
                st.session_state.editing_category = file_path
    
    # Add new challenge button
    if st.button("Add New Challenge"):
        st.session_state.editing_challenge = -1  # -1 indicates a new challenge
        st.session_state.editing_category = file_path
    
    # Check if we're editing a challenge
    if 'editing_challenge' in st.session_state and 'editing_category' in st.session_state:
        if st.session_state.editing_category == file_path:
            edit_idx = st.session_state.editing_challenge
            
            st.markdown("---")
            st.subheader("Challenge Editor")
            
            # Initialize form with existing data or empty values for new challenge
            if edit_idx >= 0:
                # Editing existing challenge
                challenge = challenges_copy[edit_idx]
                new_name = st.text_input("Challenge Name", value=challenge['name'])
                new_description = st.text_area("Description", value=challenge['description'])
                new_points = st.number_input("Points", value=challenge['points'], min_value=10, step=10)
                new_flag = st.text_input("Flag", value=challenge['flag'])
                new_difficulty = st.selectbox("Difficulty", options=["Easy", "Medium"], index=0 if challenge['difficulty'] == "Easy" else 1)
                
                # Hints are optional
                if 'hints' in challenge:
                    hint_count = len(challenge['hints'])
                    hint_inputs = []
                    for i in range(hint_count):
                        hint = st.text_area(f"Hint {i+1}", value=challenge['hints'][i])
                        hint_inputs.append(hint)
                    
                    # Option to add more hints
                    if st.button("Add Another Hint"):
                        hint_inputs.append("")
                else:
                    hint_count = 1
                    hint_inputs = [st.text_area("Hint 1", value="")]
                    
                    # Option to add more hints
                    if st.button("Add Another Hint"):
                        hint_inputs.append("")
            else:
                # Adding new challenge
                new_name = st.text_input("Challenge Name")
                new_description = st.text_area("Description")
                new_points = st.number_input("Points", value=100, min_value=10, step=10)
                new_flag = st.text_input("Flag")
                new_difficulty = st.selectbox("Difficulty", options=["Easy", "Medium"])
                
                # Hints
                hint_inputs = [st.text_area("Hint 1")]
                
                # Option to add more hints
                if st.button("Add Another Hint"):
                    hint_inputs.append(st.text_area("Hint 2"))
            
            # Save or cancel buttons
            col1, col2 = st.columns(2)
            with col1:
                if st.button("Save Challenge"):
                    # Filter out empty hints
                    hints = [hint for hint in hint_inputs if hint.strip()]
                    
                    # Create updated challenge dictionary
                    updated_challenge = {
                        "name": new_name,
                        "description": new_description,
                        "points": new_points,
                        "flag": new_flag,
                        "difficulty": new_difficulty
                    }
                    
                    # Add hints if any exist
                    if hints:
                        updated_challenge["hints"] = hints
                    
                    # Update challenge list
                    if edit_idx >= 0:
                        challenges_copy[edit_idx] = updated_challenge
                    else:
                        challenges_copy.append(updated_challenge)
                    
                    # Save to file
                    save_challenges_to_file(challenges_copy, file_path)
                    
                    # Clear editing state
                    del st.session_state.editing_challenge
                    del st.session_state.editing_category
                    
                    st.success("Challenge saved successfully!")
                    time.sleep(1)
                    st.rerun()
            
            with col2:
                if st.button("Cancel"):
                    # Clear editing state
                    del st.session_state.editing_challenge
                    del st.session_state.editing_category
                    st.rerun()
    
    # Delete challenge section
    st.markdown("---")
    st.subheader("Delete Challenge")
    delete_idx = st.number_input("Challenge Number to Delete", min_value=1, max_value=len(challenges_copy) if len(challenges_copy) > 0 else 1, step=1) - 1
    
    if st.button("Delete Selected Challenge", type="primary", use_container_width=True):
        if 0 <= delete_idx < len(challenges_copy):
            deleted_name = challenges_copy[delete_idx]['name']
            challenges_copy.pop(delete_idx)
            save_challenges_to_file(challenges_copy, file_path)
            st.success(f"Challenge '{deleted_name}' deleted successfully!")
            time.sleep(1)
            st.rerun()
        else:
            st.error("Invalid challenge number.")