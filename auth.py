import streamlit as st
import time
import json
import random
import string
import re
import hashlib
import uuid

def initialize_auth_state():
    """Initialize authentication-related session state variables if they don't exist."""
    if 'authenticated' not in st.session_state:
        st.session_state.authenticated = False
    if 'user_info' not in st.session_state:
        st.session_state.user_info = {}
    if 'auth_error' not in st.session_state:
        st.session_state.auth_error = None
    if 'is_admin' not in st.session_state:
        st.session_state.is_admin = False
    if 'login_attempts' not in st.session_state:
        st.session_state.login_attempts = {}
    if 'blocked_ips' not in st.session_state:
        st.session_state.blocked_ips = set()

def check_authentication():
    """Check if the user is authenticated."""
    initialize_auth_state()
    return st.session_state.authenticated

def is_valid_team_name(team_name):
    """Validate team name format."""
    # Team name should be 3-30 characters and contain only letters, numbers, spaces and underscores
    pattern = r'^[A-Za-z0-9_ ]{3,30}$'
    return bool(re.match(pattern, team_name))

def is_valid_password(password):
    """Validate password strength."""
    # Password should be at least 8 characters
    if len(password) < 8:
        return False, "Password must be at least 8 characters long."
    
    # Check for complexity (optional for CTF)
    # has_upper = any(c.isupper() for c in password)
    # has_lower = any(c.islower() for c in password)
    # has_digit = any(c.isdigit() for c in password)
    # has_special = any(not c.isalnum() for c in password)
    
    # if not (has_upper and has_lower and has_digit):
    #     return False, "Password must include uppercase, lowercase, and numbers."
    
    return True, ""

def generate_secure_team_id():
    """Generate a cryptographically secure team ID."""
    return str(uuid.uuid4())

def format_team_email(team_name):
    """Convert team name to a secure email format."""
    # Replace spaces with underscores and convert to lowercase
    base_email = team_name.lower().replace(' ', '_')
    # Remove any non-alphanumeric characters
    base_email = re.sub(r'[^a-z0-9_]', '', base_email)
    # Add a unique suffix to prevent email collisions
    suffix = ''.join(random.choices(string.ascii_lowercase + string.digits, k=4))
    return f"{base_email}_{suffix}@ctfteam.secure"

def authenticate_user(auth):
    """Display login form and handle user authentication."""
    initialize_auth_state()
    
    st.markdown("## CTF Login")
    st.info("Enter your team name and password to start the CTF challenge.")
    
    with st.form("login_form"):
        team_name = st.text_input("Team Name", key="login_team")
        password = st.text_input("Password", type="password", key="login_password")
        # Add a registration checkbox
        is_registering = st.checkbox("New team? Register here", value=False)
        
        submit_text = "Register Team" if is_registering else "Login to CTF"
        submit_button = st.form_submit_button(submit_text)
        
        if submit_button:
            # Check for empty fields
            if not team_name or not password:
                st.error("Team name and password are required.")
                return
            
            # Validate team name
            if not is_valid_team_name(team_name):
                st.error("Team name must be 3-30 characters and can only contain letters, numbers, spaces, and underscores.")
                return
            
            # Validate password for new registrations
            if is_registering:
                is_password_valid, password_error = is_valid_password(password)
                if not is_password_valid:
                    st.error(password_error)
                    return
            
            # Special case for admin login
            if team_name.lower() == "admin" and password == "ctfadmin123":
                st.session_state.authenticated = True
                st.session_state.user_info = {
                    'uid': "admin",
                    'name': "Admin",
                    'team_id': "admin_" + generate_secure_team_id(),
                    'is_admin': True
                }
                
                # Initialize fresh challenge progress
                st.session_state.solved_challenges = {}
                
                st.success("Admin login successful!")
                time.sleep(1)
                st.rerun()
                return
            
            try:
                team_email = format_team_email(team_name)
                
                if is_registering:
                    # Try to create a new account
                    try:
                        user = auth.create_user_with_email_and_password(team_email, password)
                        
                        # Save additional team info to Firebase (in a real app)
                        # team_data = {
                        #     'name': team_name,
                        #     'created_at': time.time(),
                        #     'team_id': generate_secure_team_id()
                        # }
                        # db.child("teams").child(user['localId']).set(team_data)
                        
                        st.session_state.authenticated = True
                        st.session_state.user_info = {
                            'uid': user['localId'],
                            'name': team_name,
                            'team_id': generate_secure_team_id(),
                            'is_admin': False,
                            'email': team_email
                        }
                        
                        # Initialize fresh challenge progress
                        st.session_state.solved_challenges = {}
                        
                        st.success(f"Team {team_name} registered successfully!")
                        time.sleep(1)
                        st.rerun()
                    except Exception as create_error:
                        error_msg = str(create_error)
                        if "EMAIL_EXISTS" in error_msg:
                            st.error("A team with this name already exists. Please try a different name or login instead.")
                        elif "WEAK_PASSWORD" in error_msg:
                            st.error("Password is too weak. Please use a stronger password.")
                        else:
                            st.error(f"Registration error: {error_msg}")
                else:
                    # Try logging in with existing account
                    try:
                        # Since we don't know the exact email used during registration,
                        # we'll need to first look up the team by name (in a real app)
                        # For this demo, we'll try a direct login
                        
                        # In a real app with a database, you would:
                        # 1. Query the database for the team by name
                        # 2. Retrieve the associated email
                        # 3. Use that email to attempt login
                        
                        user = auth.sign_in_with_email_and_password(team_email, password)
                        
                        st.session_state.authenticated = True
                        st.session_state.user_info = {
                            'uid': user['localId'],
                            'name': team_name,
                            'team_id': generate_secure_team_id(),
                            'is_admin': False,
                            'email': team_email
                        }
                        
                        # Initialize fresh challenge progress
                        st.session_state.solved_challenges = {}
                        
                        st.success(f"Welcome back, Team {team_name}!")
                        time.sleep(1)
                        st.rerun()
                    except Exception as login_error:
                        # Try a few different email formats for login attempts
                        # This is a workaround for the demo; in a real app with a database
                        # you would query the database to find the correct email
                        alternative_emails = [
                            f"{team_name.lower().replace(' ', '_')}@ctf.com",
                            f"{team_name.lower().replace(' ', '_')}_team@ctfteam.secure",
                            f"team_{team_name.lower().replace(' ', '_')}@ctfteam.secure"
                        ]
                        
                        login_successful = False
                        for alt_email in alternative_emails:
                            try:
                                user = auth.sign_in_with_email_and_password(alt_email, password)
                                
                                st.session_state.authenticated = True
                                st.session_state.user_info = {
                                    'uid': user['localId'],
                                    'name': team_name,
                                    'team_id': generate_secure_team_id(),
                                    'is_admin': False,
                                    'email': alt_email
                                }
                                
                                # Initialize fresh challenge progress
                                st.session_state.solved_challenges = {}
                                
                                st.success(f"Welcome back, Team {team_name}!")
                                login_successful = True
                                time.sleep(1)
                                st.rerun()
                                break
                            except:
                                continue
                        
                        if not login_successful:
                            # As a last resort for demo purposes, try to create a new account
                            # (in a real app, you would not do this)
                            try:
                                user = auth.create_user_with_email_and_password(team_email, password)
                                
                                st.session_state.authenticated = True
                                st.session_state.user_info = {
                                    'uid': user['localId'],
                                    'name': team_name,
                                    'team_id': generate_secure_team_id(),
                                    'is_admin': False,
                                    'email': team_email
                                }
                                
                                # Initialize fresh challenge progress
                                st.session_state.solved_challenges = {}
                                
                                st.success(f"Welcome, Team {team_name}!")
                                time.sleep(1)
                                st.rerun()
                            except Exception as e:
                                st.error("Invalid team name or password. Please try again or register a new team.")
            except Exception as e:
                st.session_state.auth_error = f"Login failed: {str(e)}"
                st.error(st.session_state.auth_error)

def logout_user():
    """Log out the current user."""
    # Reset authentication state
    st.session_state.authenticated = False
    st.session_state.user_info = {}
    
    # Clear solved challenges - no history preservation
    st.session_state.solved_challenges = {}
    
    # Reset active category and timer
    st.session_state.active_category = None
    if 'timer_end' in st.session_state:
        del st.session_state.timer_end
        
    # Reset admin state
    if 'is_admin' in st.session_state:
        st.session_state.is_admin = False
    
    # Reset any editing state for admin panel
    if 'editing_challenge' in st.session_state:
        del st.session_state.editing_challenge
    if 'editing_category' in st.session_state:
        del st.session_state.editing_category
