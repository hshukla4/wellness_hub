
# 🛠️ GCP Service Account Setup Guide for Wellness Hub (macOS)

This guide helps you install and configure Google Cloud SDK and generate service account credentials for use with Google STT/TTS APIs.

---

## ✅ Step 1: Install Google Cloud SDK (macOS)

```bash
brew install --cask google-cloud-sdk
```

If needed:
```bash
source "$(brew --prefix)/Caskroom/google-cloud-sdk/latest/google-cloud-sdk/path.bash.inc"
```

---

## ✅ Step 2: Fix Permissions (If Needed)

If you encounter a permission error:
```bash
sudo mkdir -p ~/.config/gcloud
sudo chown -R $(whoami) ~/.config/gcloud
```

---

## ✅ Step 3: Initialize SDK

```bash
gcloud init
```

---

## ✅ Step 4: Enable Required APIs

```bash
gcloud services enable speech.googleapis.com
gcloud services enable texttospeech.googleapis.com
```

---

## ✅ Step 5: Create Service Account

```bash
gcloud iam service-accounts create wellness-hub-sa --display-name "Wellness Hub Service Account"
```

---

## ✅ Step 6: Assign Role

```bash
gcloud projects add-iam-policy-binding YOUR_PROJECT_ID \
  --member="serviceAccount:wellness-hub-sa@YOUR_PROJECT_ID.iam.gserviceaccount.com" \
  --role="roles/editor"
```

---

## ✅ Step 7: Generate and Download Key File

```bash
gcloud iam service-accounts keys create ~/Downloads/service-account.json \
  --iam-account=wellness-hub-sa@YOUR_PROJECT_ID.iam.gserviceaccount.com
```

---

## ✅ Step 8: Set Environment Variable

```bash
export GOOGLE_APPLICATION_CREDENTIALS="~/Downloads/service-account.json"
```

---

## ✅ Step 9: Verify

```bash
echo $GOOGLE_APPLICATION_CREDENTIALS
```

✅ Done! You're ready to use Google STT and TTS securely.

