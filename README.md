# Event Whisperer

Event Whisperer is a command-line application that finds upcoming events in a city,
caches them locally, and uses Google's Gemini AI to rank and recommend those events
based on your personal interests.

You tell it where you are and what you like; it tells you which events are worth your time and why.

---

## ✨ Features

- **Event search** : pulls up to 20 upcoming events for any city from [ticketmaster.com], optionally filtered by a keyword.
- **Local caching** : stores fetched events in a local SQLite database (`eventcache.db`) via SQLAlchemy.
- **AI recommendations** : sends the cached events to Google Gemini, which ranks them from most to least relevant to your stated interests and explains *why* each one was recommended.
- **Interactive loop** : search again and again in a single session until you choose to quit.

---

## 🧱 How It Works

```
                ┌─────────────┐     ┌──────────────┐     ┌────────────────┐
   user input → │ eventfinder │ →   │   database   │ →   │   genai_API    │ → recommendation
   (city +      │ (Ticketmaster)    │  (SQLite via │     │   (Gemini AI)  │
    interests)  └─────────────┘     │  SQLAlchemy) │     └────────────────┘
                                    └──────────────┘
```

1. **`eventfinder.py`** queries the Ticketmaster API for events in the given city/keyword and returns a list of event dictionaries.
2. **`database.py`** clears any previous results and stores the new events in the `event` table of `eventcache.db`.
3. **`genai_API.py`** reads the cached events, builds a prompt with the user's interests, and asks Gemini to rank and explain the recommendations.
4. **`main.py`** ties it all together with an interactive command-line interface.

---

## 📂 Project Structure

| File | Description |
|------|-------------|
| `main.py` | Entry point : interactive CLI that orchestrates the search → store → recommend flow. |
| `eventfinder.py` | Fetches events from the Ticketmaster Discovery API. |
| `database.py` | Stores events in a local SQLite database using SQLAlchemy. |
| `genai_API.py` | Builds the prompt and calls the Google Gemini API for recommendations. |
| `test_functions.py` | Unit tests for `store_events`, `find_events`, and `build_prompt`. |
| `requirements.txt` | Python dependencies. |
| `eventcache.db` | SQLite database file (created/populated at runtime). |

---

## 🛠️ Prerequisites

- **Python 3.10+**
- A **Ticketmaster API key** : get one from the [Ticketmaster Developer Portal](https://developer.ticketmaster.com/).
- A **Google Gemini API key** : get one from [Google AI Studio](https://aistudio.google.com/apikey).

---

## 🚀 Setup & Installation

1. **Clone the repository**

   ```bash
   git clone <repository-url>
   cd week2project-pairedprogramming
   ```

2. **(Optional) Create and activate a virtual environment (to avoid installing packages on global Python environment)**

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set your API keys as environment variables**

   ```bash
   export TICKETMASTER_API_KEY="your_ticketmaster_key_here"
   export GENAI_KEY="your_gemini_key_here"
   ```

   > Tip: To avoid re-exporting these every session, add them to your shell profile
   > (`~/.zshrc` / `~/.bashrc`), and `source` your shell file or use a `.env` file (already git-ignored).

---

## ▶️ Usage

Run the application from the project root:

```bash
python main.py
```

You'll be prompted for:

- **City** : e.g. `New York`
- **Keyword** : e.g. `concert` (press Enter to skip)
- **Interests & preferences** : what you're into and what you look for in an event, e.g. `jazz at small venues, family-friendly festivals, weekend sports`

Event Whisperer will list the upcoming events it found and then print an AI-ranked
set of recommendations explaining why each event matches your interests. After each
search you can choose to look for another set of events or quit.

### Example session

```
Enter city: New York
Enter a keyword (or press Enter to skip): jazz
What are you interested in and what do you look for in an event? (e.g. jazz at small venues, family-friendly festivals, weekend sports): live music at small venues

20 Upcoming Events in New York:
------------------------------------------------------------
Event: Jazz Night at the Blue Note
Date: 2026-07-12
Venue: Blue Note
Tickets: https://www.ticketmaster.com/...
----------------------------------------
...

Here are the events ranked from most to least relevant based on your interest in
intimate live music venues:
1. Jazz Night at the Blue Note — an intimate jazz performance in a small, iconic venue.
...
```

---

## 🌐 Environment Variables

| Variable | Required | Description |
|----------|----------|-------------|
| `TICKETMASTER_API_KEY` | ✅ | API key for the Ticketmaster Discovery API. |
| `GENAI_KEY` | ✅ | API key for the Google Gemini API. |

---

## 🧪 Running Tests

The project includes unit tests that use an in-memory SQLite database and a mocked
Ticketmaster request, so **no API keys or network access are required** to run them.

```bash
python -m unittest test_functions.py
```

This covers:

- `store_events` : verifies events are correctly written to the database.
- `find_events` : verifies the Ticketmaster response is parsed into the expected structure (using a mocked HTTP request).
- `build_prompt` : verifies the AI prompt is built correctly from event data.

---

## 🧰 Tech Stack

**Language & runtime**

- **Python 3.10+** : core language

**External APIs / Services**

- **[Ticketmaster API]** : source of upcoming event data (search by city and keyword)
- **[Google Gemini API]** (`gemini-2.5-flash`) : ranks events and generates personalized recommendations

**Libraries**

- **[requests]** : HTTP calls to the Ticketmaster API
- **[SQLAlchemy]** : database toolkit
- **[SQLite]** : lightweight local database for caching events (`eventcache.db`)
- **[google-genai]** : official Python client for the Google Gemini API

**Tooling**

- **[unittest]** + **[unittest.mock]** : testing
- **[venv]** : virtual environment / dependency isolation

---

## 👥 Authors

Built by **Will Zhu**, **Elham Fayzi**, and **Nicole Jallim**.
