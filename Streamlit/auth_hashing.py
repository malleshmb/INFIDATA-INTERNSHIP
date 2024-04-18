import streamlit_authenticator as stauth

hashed_passwords = stauth.Hasher(['hello']).generate()
print(hashed_passwords)
