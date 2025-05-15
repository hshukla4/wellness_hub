
# 🔐 Creating a GCP Service Account JSON Key

Follow these steps to create a service account and generate a JSON key for accessing Google Cloud APIs:

---

## ✅ Prerequisites

- A Google Cloud Project
- Owner or Editor permissions on the project
- Billing enabled for the project

---

## 🛠️ Step-by-Step Instructions

### 1. Go to the Google Cloud Console

🔗 [Google Cloud Console](https://console.cloud.google.com/)

---

### 2. Navigate to **IAM & Admin → Service Accounts**

- In the left sidebar, click **IAM & Admin**
- Then click **Service Accounts**

---

### 3. Click **Create Service Account**

- **Name:** `wellness-hub-service`
- **ID:** (auto-generated or custom)
- **Description:** `Access for Speech-to-Text and Text-to-Speech APIs`

---

### 4. Assign Roles

Choose the following roles:

- `Cloud Speech-to-Text API User`
- `Cloud Text-to-Speech API User`

Click **Continue**

---

### 5. Create and Download JSON Key

- In the next step, choose **"Create Key"**
- Select **JSON** format
- Click **Create** – this will download the key file

---

### 6. Save Your Key Securely

Save the downloaded `.json` file securely in your project:

```bash
mkdir -p ~/.gcp_keys
mv ~/Downloads/your-key-file.json ~/.gcp_keys/wellness-hub-service-account.json
```

---

### 7. Set the Environment Variable

```bash
export GOOGLE_APPLICATION_CREDENTIALS="$HOME/.gcp_keys/wellness-hub-service-account.json"
```

You can also add this to your shell profile (`~/.zshrc` or `~/.bash_profile`) to persist it.

---

## 🧪 Test It

Run a quick test to confirm authentication:

```bash
gcloud auth activate-service-account --key-file=$GOOGLE_APPLICATION_CREDENTIALS
```

---

## ✅ Done!

Your service account is now ready to be used with the Google APIs in your code!
