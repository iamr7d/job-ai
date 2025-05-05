import os
import time
import requests
from bs4 import BeautifulSoup
from twilio.rest import Client
from groq import Groq
from datetime import datetime

# --- Configuration ---
SID = os.getenv('TWILIO_ACCOUNT_SID')
TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
twilio = Client(SID, TOKEN)
FROM, TO = 'whatsapp:+14155238886', 'whatsapp:+919061360912'

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ = Groq(api_key=GROQ_API_KEY)
HEADERS = {'User-Agent': 'Mozilla/5.0'}
LOC = "India"
KEYWORDS = "full stack, react, node, blockchain, solidity"

# --- Track Sent Jobs ---
# (rest of your code here, please add the remaining content if needed)
