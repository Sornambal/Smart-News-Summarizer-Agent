# 📰 Smart News Summarizer Agent

**Build an agent that automatically finds recent news on a topic and creates a brief summary.**

## 🎯 Goal

The agent makes **2 autonomous decisions**:
1. What search query to use
2. Which articles are most relevant to summarize

## ✅ Evaluation Checklist

- ✅ Agent successfully searches for news
- ✅ Agent autonomously selects relevant articles (not hardcoded)
- ✅ Agent fetches and summarizes each article  
- ✅ Output is well-formatted and readable
- ✅ Handles errors gracefully (no crashes)
- ✅ Code is clean and commented

## 🏗️ 4-Module Architecture

```
User Topic
    ↓
[Module 1: Query Generation] ← Friend
    ↓
[Module 2: Web Search & Article Selection] ← Friend
    ↓
[Module 3: Article Extraction & Summarization] ← You
    ↓
[Module 4: Report Generation & Error Handling] ← You
    ↓
Professional Report (Localhost Web UI)
```

### Modules Overview

| Module | Owner | File | What It Does |
|--------|-------|------|--------------|
| **1** | Friend | `modules/query_generator.py` | Generates optimized search queries |
| **2** | Friend | `modules/web_search.py` | Searches API & filters relevant articles |
| **3** | You | `modules/summarizer.py` | Fetches & summarizes articles |
| **4** | You | `modules/report_generator.py` | Creates professional reports |

## 🚀 Quick Start

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Add API Keys
Create `.env` file:
```
GROQ_API_KEY=your_key_here
TAVILY_API_KEY=your_key_here
```

### 3. Run on Localhost
```bash
python flask_api.py
```

Open: **http://localhost:5000**

## 📂 Project Structure

```
Smart-News-Summarizer-Agent/
├── modules/
│   ├── query_generator.py      # Module 1
│   ├── web_search.py           # Module 2
│   ├── summarizer.py           # Module 3
│   └── report_generator.py     # Module 4
├── app/
│   └── app.py                  # Orchestration
├── flask_api.py                # Web UI ← Run this!
├── .env                        # API Keys
└── requirements.txt
```

## 📚 Documentation

- **COMPLETION_REPORT.md** - Full project completion report
- **IMPLEMENTATION_GUIDE.md** - Technical implementation details
- **PROJECT_INDEX.md** - Complete project overview
- **MODULE_3_4_SUMMARY.md** - Modules 3 & 4 specific details

## ✅ Testing

```powershell
python test_modules_3_4.py       # Test Modules 3 & 4
python test_end_to_end.py        # Full integration test
python QUICKSTART.py             # Verify setup
```

## 📊 Sample Output

```
================================================================================
📰 NEWS SUMMARY REPORT: YOUR TOPIC
================================================================================

📋 EXECUTIVE SUMMARY
[LLM-synthesized overview of all articles]

📄 ARTICLE SUMMARIES
[Individual 3-4 sentence summaries with URLs]

⚠️ FAILED TO PROCESS
[Transparent error reporting]

📊 STATISTICS
Total URLs Found: 5
Successfully Processed: 3
Success Rate: 60.0%
```

## 🔧 Technologies

- **Groq API** - LLM for query generation and summarization
- **Tavily API** - News search and article discovery
- **newspaper3k** - Article content extraction
- **LangChain** - LLM framework and prompts
- **Python 3.11** - Runtime environment

## 👥 Team

- **Modules 1 & 2** - Your Friend (Query Generation, Web Search)
- **Modules 3 & 4** - You (Article Extraction, Report Generation)

## ✅ Status

**COMPLETE ✅** - All modules implemented, tested, and ready for production!

---

**Start summarizing news now:** `python interactive_mode.py`