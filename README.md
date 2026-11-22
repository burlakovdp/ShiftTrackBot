# ShiftTrackBot

> A simple Telegram bot for tracking work shifts and processed messages.

ShiftTrackBot helps employees log their work shifts along with the number of messages handled in AmoCRM and Telegram chat. All entries are saved to a database and can be exported anytime as a structured PDF summary report.

The bot is bilingual (🇷🇺 Russian / 🇬🇧 English) — users can switch languages in the settings, and their preference is saved automatically.

## ✨ Features

- **Shift logging** — step-by-step flow: shift selection → AmoCRM messages → Telegram messages → review → confirmation.
- **PDF summary** — a clean table containing all user entries (entry number, date, day of the week, shift, AmoCRM, and Telegram chat).
- **Bilingual interface** — full support for Russian and English, with language preferences stored in the database.
- **Intuitive navigation** — "⬅️ Back" and "🏠 Main Menu" buttons available at every step of the dialog.
- **Time zone handling** — timestamps are stored in UTC in the database and automatically converted to Paris time (`Europe/Paris`) in the PDF report.

## 🧭 How It Works

The conversation flow is implemented as a finite state machine: each step (`stage`) is defined in `StorageManager.stage`, specifying its available buttons, transitions, and response message. The user's navigation history is stored on a `Stack`, allowing the **"Back"** button to simply pop the top state and **"Main Menu"** to reset the stack to its initial state.

```text
/start
  └─ menu_stage
       ├─ 📝 Add Entry  → shift_stage → counter_stage_1 → counter_stage_2 → check_stage → approve_stage → menu_stage
       ├─ 📊 Summary    → resume_stage (sends PDF) → menu_stage
       └─ ⚙️ Settings   → settings_stage → language_choose_stage → language_change_stage → menu_stage
```

## 🛠 Tech Stack

| Library | Purpose |
| :--- | :--- |
| **pyTelegramBotAPI (`telebot`)** | Interacting with the Telegram Bot API |
| **python-dotenv** | Loading the bot token from the `.env` file |
| **pendulum** | Handling dates, time zones, and localization |
| **fpdf2** | Generating PDF reports |
| **sqlite3** | Storing data |
