import firebase_admin
from firebase_admin import credentials, auth

# Initialize Firebase Admin SDK
cred = credentials.Certificate(r"C:\Users\91934\Desktop\smarthealth\healthapp-6cfc4-firebase-adminsdk-cu8rp-661fcaa1b0.json")
firebase_admin.initialize_app(cred)
