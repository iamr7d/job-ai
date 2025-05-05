import time
import threading
from main import ROLES, scrape_linkedin, KEYWORDS

def run_scraper_loop():
    while True:
        for role in ROLES:
            scrape_linkedin(role, KEYWORDS)
        print("[INFO] Sleeping for 15 minutes before next run...")
        time.sleep(15 * 60)  # Sleep for 15 minutes

if __name__ == "__main__":
    # Run in a background thread to allow Railway/other hosts to keep process alive
    t = threading.Thread(target=run_scraper_loop)
    t.start()
    t.join()
