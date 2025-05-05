# Job Notifier Scraper

This project scrapes job postings for various tech roles and sends WhatsApp notifications for new jobs every 15 minutes. Duplicate notifications are avoided using a persistent sent job tracking file.

## Features
- Scrapes LinkedIn for a wide range of tech roles (customizable in `main.py`)
- Sends WhatsApp messages using Twilio
- Runs every 15 minutes automatically (suitable for Railway, Render, Heroku, etc.)
- Avoids duplicate job notifications

## Deployment Instructions

1. **Install dependencies**
   ```sh
   pip install -r requirements.txt
   ```

2. **Set up Twilio credentials**
   - Edit `main.py` and set your `SID`, `TOKEN`, `FROM`, and `TO` variables for WhatsApp API.

3. **Deploy to Railway/Render/Heroku**
   - Ensure your project contains:
     - `main.py`
     - `job_notifier.py`
     - `Procfile`
     - `requirements.txt`
   - Railway/Heroku will auto-detect the `Procfile` and run `python job_notifier.py` as a worker.

4. **Persistence**
   - The script uses `sent_urls.txt` to avoid duplicate notifications. Make sure your deployment supports persistent storage if you want this across restarts.

## Customization
- Edit `ROLES` and `KEYWORDS` in `main.py` to change what jobs are scraped.
- Adjust the interval in `job_notifier.py` if you want more/less frequent notifications.

## Notes
- Only LinkedIn scraping is enabled by default. You can add other sources (Indeed, Naukri, etc.) by extending `job_notifier.py`.
- Make sure your Twilio WhatsApp sender is approved for your recipient number.

## Troubleshooting
- If you get blocked by LinkedIn, increase the sleep interval or rotate proxies.
- For persistent errors, check your logs and Twilio account status.

---

**Happy job hunting!**
# job-kba
