

---

## 📄 `README.md`

```markdown
# 🧾 PDF Metadata Uploader (Flask Project)

A simple Flask web app that allows users to upload PDF files, extract metadata (like number of pages), and display results. This is perfect for showcasing file handling, form validation, and PDF automation in your portfolio.

---

## 🚀 Features

- Upload PDF files via a secure web form
- Extract:
  - File name
  - Page count
  - PDF metadata
- Validate:
  - File type (`.pdf` only)
  - File size (max 5MB)
- Save uploaded files with a unique name (timestamp + username)
- Log uploads in a JSON file (`upload_log.json`)
- Basic error handling (missing file, invalid type, etc.)

---

## 🗂️ Project Structure

```

pdf\_metadata\_tool/
├── app.py                # Main Flask app
├── upload\_log.json       # (Created automatically) Upload logs
├── uploads/              # Stores uploaded PDF files
├── templates/
│   ├── index.html        # Upload form
│   └── result.html       # Displays metadata
├── .venv/                # Virtual environment (optional)
├── requirements.txt      # Project dependencies

````

---

## 🛠️ How to Run the Project

### 1. Clone the Repo

```bash
git clone https://github.com/yourusername/pdf_metadata_tool.git
cd pdf_metadata_tool
````

### 2. Create & Activate a Virtual Environment

```bash
# Windows PowerShell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the App

```bash
python app.py
```

Open [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.

---

## 📦 Dependencies

* Flask
* PyPDF2
* Werkzeug (comes with Flask)

Install them all with:

```bash
pip install Flask PyPDF2
```

---

## 📥 Example Log Entry (`upload_log.json`)

```json
{
  "username": "john_doe",
  "filename": "1720748032_john_doe_sample.pdf",
  "pages": 5,
  "timestamp": "Wed Jun 11 15:00:32 2025"
}
```

---

## 📸 Screenshots

*Add screenshots of your form page and result page here if you push to GitHub.*

---

## 👨‍💻 Author

**CoderMundaAK** – [@yourgithub](https://github.com/CoderMundaAk/PDF_Metadata_Extractor/upload/main)

---

## 📌 License

This project is open-source and available under the [MIT License](LICENSE).

