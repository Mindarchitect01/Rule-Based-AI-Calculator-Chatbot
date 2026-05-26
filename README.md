# Rule-Based AI Calculator

Chatbot kalkulator berbasis NLP (Natural Language Processing) menggunakan **Python**, **Flask**, dan custom **Rule-Based AI** tanpa menggunakan OpenAI API atau LLM.

Project ini dibuat untuk mempelajari bagaimana chatbot matematika bekerja secara internal menggunakan:
- NLP dasar
- parsing
- symbolic computation
- rule-based reasoning
- software engineering architecture

---

# Features

- Natural language math parsing
- NLP Bahasa Indonesia sederhana
- Rule-based AI engine
- Mathematical expression evaluation
- Flask backend architecture
- Modern chatbot interface
- Unit testing menggunakan Pytest
- Clean & scalable project structure

---

# Contoh Query

```text
5+2
```

```text
berapa 10 dikali 5
```


```text
100 dibagi 4
```

---

# Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Flask | Backend web framework |
| HTML/CSS/JavaScript | Frontend UI |
| SymPy | Safe mathematical evaluation |
| Pytest | Unit testing |

---

# Cara Kerja Sistem

Chatbot menggunakan pipeline NLP sederhana:

```text
User Input
↓
Text Cleaning
↓
Intent Detection
↓
Operator Mapping
↓
Expression Builder
↓
Math Evaluation
↓
Response
```

---

# Installation

## 1. Clone Repository

```bash
git clone https://github.com/Mindarchitect01/Rule-Based-AI-Calculator-Chatbot.git
```

---

## 2. Masuk ke Folder Project

```bash
cd Rule-Based-AI-Calculator-Chatbot
```

---

## 3. Buat Virtual Environment

### Windows

```bash
python -m venv venv
```

Activate:

```bash
venv\Scripts\activate
```

---

### Mac/Linux

```bash
python3 -m venv venv
```

Activate:

```bash
source venv/bin/activate
```

---

## 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Menjalankan Project

```bash
python run.py
```

Buka browser:

```text
http://127.0.0.1:5000
```

---

# Running Tests

Menjalankan semua unit testing:

```bash
python -m pytest
```

Expected output:

```text
9 passed
```

---

# Contoh Unit Test

```python
def test_addition():
    assert evaluate_expression("5+2") == 7.0
```

---

# Limitations

Karena project ini menggunakan rule-based NLP dan bukan LLM, sistem masih memiliki beberapa keterbatasan:

- Belum bisa memahami soal cerita kompleks
- Belum memiliki memory/context conversation
- Belum memahami reasoning manusia secara penuh
- Masih bergantung pada keyword dan rules
- Belum mendukung semantic understanding tingkat lanjut

Project ini dibuat untuk mempelajari fundamental NLP sebelum menggunakan modern AI models.

---

# Why This Project Matters

Kebanyakan chatbot modern hanya menggunakan LLM API.

Sedangkan project ini fokus pada:
- NLP fundamentals
- Rule-based reasoning
- Symbolic computation
- Software architecture
- Backend engineering
- Testing practices

Tujuan project ini adalah memahami bagaimana sistem AI sederhana bekerja secara internal tanpa bergantung pada external AI services.

---

# Learning Goals

Project ini dirancang untuk membantu developer mempelajari:

- Fundamental Natural Language Processing
- Rule-Based AI Systems
- Flask Backend Architecture
- Software Engineering Best Practices
- Debugging & Testing
- Clean Code Organization

---

# Final Notes

Project ini sengaja dibuat tanpa menggunakan OpenAI API atau LLM agar developer dapat memahami fundamental:
- NLP
- parsing
- symbolic reasoning
- backend architecture
- software engineering

sebelum menggunakan modern AI frameworks.