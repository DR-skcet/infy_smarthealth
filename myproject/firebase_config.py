import firebase_admin
from firebase_admin import credentials, auth

# Initialize Firebase Admin SDK
cred = credentials.Certificate(r"C:\Users\91934\Desktop\smarthealth\healthapp-6cfc4-firebase-adminsdk-cu8rp-d23ef7c1ff.json")

if not firebase_admin._apps:
    firebase_admin.initialize_app(cred)