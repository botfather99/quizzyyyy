<div align="center">

# 🎯 Quizzyyyy
## ✨ The Cutest Quiz Platform Ever

[![Python](https://img.shields.io/badge/Python-87.8%25-3776ab?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![HTML](https://img.shields.io/badge/HTML-12.1%25-E34C26?style=for-the-badge&logo=html5&logoColor=white)](https://html.spec.whatwg.org/)
[![Love](https://img.shields.io/badge/Made%20with-Love%20%F0%9F%92%9C-ff69b4?style=for-the-badge)](https://github.com/botfather99)

---

### 👋 Created by [Berlin](https://github.com/botfather99) with ❤️

</div>

---

## 🌟 Welcome to Quizzyyyy!

Quizzyyyy is a **delightful, feature-rich quiz platform** that makes learning interactive and fun! Whether you're creating quizzes, taking exams, or building a quiz community, Quizzyyyy has you covered with cute UX and powerful features.

---

## ✨ Amazing Features

<table>
  <tr>
    <td width="50%">
      
### 🎨 Quiz Creation
- 📝 Text input support
- 📤 Telegram poll imports
- 📄 PDF file imports
- 🤖 AI-generated quizzes
- ✏️ Easy editing & customization

    </td>
    <td width="50%">
      
### 📊 Smart Analytics
- 👤 Per-user performance tracking
- 🏆 Leaderboards & rankings
- 📈 Sectional score breakdowns
- 📋 Detailed progress reports
- 🎓 Performance insights

    </td>
  </tr>
  <tr>
    <td width="50%">
      
### 🎮 Interactive Modes
- 📚 Practice mode with instant feedback
- 🎯 Exam mode for serious testing
- ⏱️ Sectional timers
- 🎪 Standard & advanced formats
- 🔗 Inline sharing features

    </td>
    <td width="50%">
      
### 🔐 Smart Control
- 💰 Free & premium tiers
- 🔑 Batch access management
- 🛡️ Auth-chat lists
- 👑 Admin controls
- 🚀 Payment integration

    </td>
  </tr>
</table>

---

## 🏗️ Platform Architecture

```
Quizzyyyy Architecture
├── 🤖 Creator Bot (Pyrogram)
│   ├── Quiz creation & editing
│   ├── PDF/poll imports
│   ├── Batch management
│   └── Payment processing
│
├── 🎮 Runner Bot (python-telegram-bot)
│   ├── Quiz sessions
│   ├── Real-time scoring
│   ├── Leaderboard management
│   └── AI generation
│
├── 🎨 Mini App (FastAPI)
│   ├── Visual quiz player
│   ├── Practice & exam modes
│   ├── Interactive UI
│   └── Secure authentication
│
└── 🗄️ MongoDB Database
    ├── User profiles
    ├── Quiz content
    ├── Performance data
    └── Payment records
```

---

## 🚀 Quick Start

### Prerequisites
- **Python** 3.11+
- **MongoDB** (free Atlas cluster works great!)
- **Telegram Bot Tokens** (get from [@BotFather](https://t.me/botfather))
- **Telegram API Credentials** (from [my.telegram.org](https://my.telegram.org))

### Setup in 3 Steps

```bash
# 1️⃣ Clone & Setup Environment
git clone https://github.com/botfather99/quizzyyyy
cd quizzyyyy
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# 2️⃣ Install Dependencies
pip install -r requirements.txt

# 3️⃣ Configure & Run
cp .env.example .env
nano .env  # Fill in your credentials (see Configuration Reference)
python run.py
```

That's it! 🎉 Your platform is now running!

---

## ⚙️ Configuration Reference

Create a `.env` file with these essential variables:

| Variable | Required | Description |
|----------|----------|-------------|
| `API_ID` | ✅ | Your Telegram API ID from [my.telegram.org](https://my.telegram.org) |
| `API_HASH` | ✅ | Your Telegram API Hash |
| `CREATOR_BOT_TOKEN` | ✅ | Token for creation/editing bot |
| `RUNNER_BOT_TOKEN` | ✅ | Token for quiz playing bot |
| `MONGODB_URI` | ✅ | MongoDB connection string |
| `MONGODB_DB_NAME` | ✅ | Database name (default: `quizbot`) |
| `OWNER_ID` | ✅ | Your Telegram user ID |
| `ADMIN_IDS` | ➖ | Space-separated admin IDs |
| `MINI_APP_DOMAIN` | ➖ | Public HTTPS URL for the Mini App |
| `RAZORPAY_KEY_ID` | ➖ | Razorpay API key (for payments) |
| `RAZORPAY_KEY_SECRET` | ➖ | Razorpay API secret |

**💡 Tip:** Copy `.env.example` and fill in your values. Keep this file private!

---

## 🎮 Running the Platform

### Start Everything
```bash
python run.py
```

### Start Specific Components
```bash
python run.py --only creator    # Creator Bot only
python run.py --only runner     # Runner Bot only
python run.py --only miniapp    # Mini App only
```

### Docker Deployment
```bash
docker compose up -d --build
```

### VPS / Always-On Setup
```bash
sudo nano /etc/systemd/system/quizbot.service
# [See systemd configuration]
sudo systemctl enable --now quizbot
```

---

## 📱 Mini App Experience

The cute **Mini App** is your visual quiz player!

### 🎯 Practice Mode
- ✅ Instant feedback after each answer
- 📖 Explanation shown immediately
- ⏭️ Auto-advance to next question
- 🎨 Beautiful interactive UI

### 🏆 Exam Mode
- 🤐 Answers hidden until completion
- 📊 Full detailed review at the end
- 📈 Score breakdown by sections
- 💯 Performance analytics

**Access:** Open the "Play" button after creating a quiz!

---

## 🗄️ Database

- **Platform:** MongoDB Atlas
- **Free Tier:** M0 cluster (perfect for starting!)
- **Auto Setup:** All indexes created automatically
- **Backup:** Atlas built-in backup & restore

---

## 📊 Tech Stack

| Component | Technology |
|-----------|-----------|
| **Language** | Python 3.11+ |
| **Telegram API** | Pyrogram & python-telegram-bot |
| **Web Framework** | FastAPI |
| **Database** | MongoDB with Motor async driver |
| **Authentication** | HMAC-SHA256 verification |
| **Encryption** | AES-256-GCM for secure sessions |
| **Payments** | Razorpay integration |
| **Frontend** | HTML5 + CSS3 + JavaScript |

---

## 🤝 Contributing

We ❤️ contributions! Feel free to:
- 🐛 Report bugs
- ✨ Suggest features
- 🔧 Submit pull requests
- 📚 Improve documentation

---

## 📄 License

This project is open source and available under the MIT License.

---

## 🙏 Credits & Acknowledgments

<div align="center">

| Role | Contributor |
|------|-------------|
| **👨‍💻 Created & Maintained by** | [Berlin](https://github.com/botfather99) |
| **🎯 Repository** | [github.com/botfather99/quizzyyyy](https://github.com/botfather99/quizzyyyy) |
| **🎓 Originally Created by** | [devgagan](https://github.com/devgaganin) |
| **🚀 Powered by** | Telegram API |
| **📦 Dependencies** | [Pyrogram](https://pyrogram.org), [python-telegram-bot](https://python-telegram-bot.org), [MongoDB](https://mongodb.com), [FastAPI](https://fastapi.tiangolo.com) |

---

### 💖 Made with love for quiz enthusiasts everywhere!

**Questions?** Reach out to Berlin or check out the [repository](https://github.com/botfather99/quizzyyyy).

</div>

---

<div align="center">

⭐ **If you love Quizzyyyy, please give it a star!** ⭐

</div>