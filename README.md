
# Forge Symbolic Monitor (Render Deployment)

This folder contains everything you need to deploy a self-healing symbolic monitor
that runs every 15 minutes on Render.com.

## 🔧 How It Works
This worker:

1. Runs `script_18_netlify_error_crawler.py` to crawl forgeforall.com
2. Maps live errors to source files using `script_19_match_live_errors_to_source.py`
3. Runs symbolic patch monitor `script_21_live_symbolic_patch_monitor.py`
4. Logs all activity to `patchlog/script_22_hourly_monitor_log.txt`

## 📦 Required Files

- `monitor.py` — master cycle script (derived from script_22)
- `requirements.txt` — Python packages
- `patchlog/` — where all logs are stored
- Your service account JSON (uploaded securely via Render Dashboard)

## 🚀 Deploy Steps

1. Go to https://render.com > Create a new **Background Worker**
2. Connect this folder’s GitHub repo or zip
3. Set the command to:
    python monitor.py

4. Add Environment Variable:
   ```
   GOOGLE_APPLICATION_CREDENTIALS=service-account.json
   ```

5. Upload your Firebase credentials in Render dashboard as `service-account.json`
6. Deploy — and Forge will now self-patch hourly.

