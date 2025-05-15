# Wellness Hub Platform – Technical Stack Overview

---

## 🔹 Foundational Components

### 🔍 User Interface (UX Layer)
- **Flutter / Firebase Hosting / Web App**
- **Firebase Auth** – login, personalized journeys
- **Firebase Analytics** – usage, session behavior

### 🌐 API Gateway Layer
- **Apigee API Gateway** – secure, scalable APIs for all pillars
- **Cloud Endpoints** – microservice interface points

### 🧰 AI Orchestration Engine
- **Vertex AI Pipelines** – orchestrate data → AI model → response
- **Cloud Workflows** – manage multi-step workflows between services
- **Cloud Functions** – event-based triggers (e.g., journaling reminder)

### 📱 Wearable Device Integration
- **MQTT / Cloud PubSub** – replace deprecated Cloud IoT Core
- **Pub/Sub** – stream vitals (HRV, sleep, steps) to backend
- **BigQuery** – log + analyze wearable data

### 🎤 Voice Interface (Speech AI)
- **Speech-to-Text API** – convert reflection/commands to text
- **Text-to-Speech API** – read affirmations/mantras aloud
- **Dialogflow CX** – Bhakti Voice Assistant

---

## 🌿 12 Pillars and Mapped GCP AI Tools

### 🧠 1. Mind – Mood, Affirmations, Reframing
- **Vertex AI custom models**
- **Natural Language API** (sentiment)
- **Dialogflow CX + Text-to-Speech**

### 🧘 2. Body – Yoga, Breathwork
- **Media AI** (pose analysis)
- **TensorFlow + Vertex AI** (custom model)
- **Cloud Run** (on-demand session stream)

### 🌌 3. Spirituality – Gita Wisdom, Bhakti
- **Document AI** (extract shlokas)
- **Vertex AI Search** (semantic lookup)
- **Firestore** (user-deity preferences)

### 🌿 4. Ayurveda – Dosha, Herbs, Healing
- **BigQuery** (seasonal mapping)
- **Recommendations AI** (dosha/herb link)
- **Vertex Matching Engine**

### 🥚 5. Satvik Food – Lunar/Seasonal Diet
- **Cloud Scheduler** (daily alerts)
- **BigQuery + Data Studio** (dashboards)
- **Firestore** (meal logs)

### 🎶 6. Music & Raga – Emotional Therapy
- **Cloud Storage** (music archive)
- **Cloud Transcoder + Media Translation**
- **Vertex AI** (emotion-tag prediction)

### ⛪️ 7. Pooja – Rituals, Devotion
- **Firestore** (sankalpa logs)
- **Cloud Functions** (ritual generator)
- **Scheduler + Text-to-Speech**

### 🔮 8. Astrology – Transit & Karma
- **Vertex AI Forecast**
- **Firestore** (birth data)
- **Cloud Tasks** (reminders by grah hours)

### 🏡 9. Vastu – Energy, Panchang Sync
- **Maps API** (location context)
- **BigQuery** (vastu rule logic)
- **Vertex AI** (room placement model)

### 📓 10. Journal & Reflection
- **Speech-to-Text**
- **Natural Language API** (emotion tagging)
- **Firestore** (secure journaling)

### 📜 11. Dharma Feed – Gita & Upanishads
- **Document AI** (text extraction)
- **Vertex AI Search** (wisdom snippets)
- **Scheduler** (push wisdom feed)

### ⏰ 12. Notification & Nudges
- **Cloud Tasks**
- **Firebase Cloud Messaging**
- **Vertex AI** (behavior nudges)

---

## ✅ Optional AI Enhancements
- **Looker Studio + BigQuery** – BI & trends
- **Vertex AI Agent Builder** – custom voice agents
- **Cloud Run Gen2** – stateless API-based microservices