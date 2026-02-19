# ds-rag-pipeline_sia

A local, offline RAG (Retrieval-Augmented Generation) system built with Ollama, LangChain, FAISS and ChromaDB.  
Chat with your PDF – no internet required.

---

## 🗺️ Quick Overview

| | 🚀 Version 1 | 🎓 Version 2 | 🛠️ Version 3 |
|---|---|---|---|
| **File** | `RAG_Chat_Version_01.py` | `RAG_Exercise_Version_02_FAISS.ipynb` | `RAG_Exercise_Version_03_Chroma.ipynb` |
| **Environment** | Terminal | Jupyter | Jupyter |
| **Storage** | ChromaDB (Disk) | FAISS (RAM) | ChromaDB (Disk) |
| **Embeddings** | Ollama | HuggingFace ⚠️ | Ollama |
| **Stability** | ✅ Stable | ⚠️ M1 Fix applied | ✅ Stable |
| **Best For** | Daily use | Classroom exercise | Experimentation |

---

# 🇬🇧 English

## ⚙️ One-Time Setup (Copy & Paste)

> **Note:** Run these blocks only once. After that, only `source .venv/bin/activate` is needed each session.

---

### 🚀 Version 1 Setup (Terminal + ChromaDB)

**macOS**
```bash
pyenv local 3.11.3 && \
python -m venv .venv && \
source .venv/bin/activate && \
pip install --upgrade pip && \
pip install -r requirements.txt && \
pip install chromadb && \
ollama pull llama3.2:3b && \
ollama pull nomic-embed-text
```

**Windows – PowerShell**
```powershell
pyenv local 3.11.3; `
python -m venv .venv; `
.venv\Scripts\Activate.ps1; `
python -m pip install --upgrade pip; `
pip install -r requirements.txt; `
pip install chromadb; `
ollama pull llama3.2:3b; `
ollama pull nomic-embed-text
```

**Windows – Git-Bash**
```bash
pyenv local 3.11.3 && \
python -m venv .venv && \
source .venv/Scripts/activate && \
pip install --upgrade pip && \
pip install -r requirements.txt && \
pip install chromadb && \
ollama pull llama3.2:3b && \
ollama pull nomic-embed-text
```

---

### 🎓 Version 2 Setup (Jupyter + FAISS)

**macOS**
```bash
pyenv local 3.11.3 && \
python -m venv .venv && \
source .venv/bin/activate && \
pip install --upgrade pip && \
pip install -r requirements.txt && \
pip install faiss-cpu sentence-transformers && \
ollama pull llama3.2:3b
```

**Windows – PowerShell**
```powershell
pyenv local 3.11.3; `
python -m venv .venv; `
.venv\Scripts\Activate.ps1; `
python -m pip install --upgrade pip; `
pip install -r requirements.txt; `
pip install faiss-cpu sentence-transformers; `
ollama pull llama3.2:3b
```

**Windows – Git-Bash**
```bash
pyenv local 3.11.3 && \
python -m venv .venv && \
source .venv/Scripts/activate && \
pip install --upgrade pip && \
pip install -r requirements.txt && \
pip install faiss-cpu sentence-transformers && \
ollama pull llama3.2:3b
```

---

### 🛠️ Version 3 Setup (Jupyter + ChromaDB)

**macOS**
```bash
pyenv local 3.11.3 && \
python -m venv .venv && \
source .venv/bin/activate && \
pip install --upgrade pip && \
pip install -r requirements.txt && \
pip install chromadb && \
ollama pull llama3.2:3b && \
ollama pull nomic-embed-text
```

**Windows – PowerShell**
```powershell
pyenv local 3.11.3; `
python -m venv .venv; `
.venv\Scripts\Activate.ps1; `
python -m pip install --upgrade pip; `
pip install -r requirements.txt; `
pip install chromadb; `
ollama pull llama3.2:3b; `
ollama pull nomic-embed-text
```

**Windows – Git-Bash**
```bash
pyenv local 3.11.3 && \
python -m venv .venv && \
source .venv/Scripts/activate && \
pip install --upgrade pip && \
pip install -r requirements.txt && \
pip install chromadb && \
ollama pull llama3.2:3b && \
ollama pull nomic-embed-text
```

---

## 🚀 Version 1: The "Production" Version (Terminal + Chroma)

- **Goal:** High speed and no crashes.
- **How it works:** External Python script (`RAG_Chat_Version_01.py`) in the Terminal.
- **Storage:** ChromaDB – saves data to your hard drive.
- **Why use it:** Minimal RAM usage, no browser overhead from Jupyter. Best for daily use.

### ✅ Check-List Version 1
- [ ] Is Ollama running?
- [ ] Is the `.venv` activated?
- [ ] Are Ollama models downloaded? (`llama3.2:3b` + `nomic-embed-text`)
- [ ] Is `requirements.txt` installed?
- [ ] Is the `paracetamol.pdf` in the `/documents` folder?

### 📖 How to Use Version 1

**Step 1: Open your Terminal**
```bash
cd ds-rag-pipeline_sia
```
**Step 2: Activate your Environment**
```bash
source .venv/bin/activate
```
**Step 3: Start the Program**
```bash
python RAG_Chat_Version_01.py
```
**Step 4: Chat with your PDF**
- Wait for the message: `--- Medical AI Chat (Type 'exit' to stop) ---`
- Type your question (e.g., *"What is the dosage for children?"*) and press **Enter**
- Type `exit` to close the program

> **Note:** Make sure **Ollama** is running in the background before you start!

---

## 🎓 Version 2: The "School" Version (Jupyter + FAISS)

- **Goal:** Follow the original classroom exercise.
- **How it works:** Everything runs inside the Jupyter Notebook.
- **Storage:** FAISS – keeps data in RAM (memory).

> ### ⚠️ Apple Silicon M1 Fix
> ~~**Original setup:** `OllamaEmbeddings` with `nomic-embed-text`~~  
> ~~`from langchain_community.embeddings import OllamaEmbeddings`~~  
> ~~`embeddings = OllamaEmbeddings(model="nomic-embed-text")`~~
>
> **Problem:** `OllamaEmbeddings` causes a kernel crash on Apple Silicon M1 when FAISS runs a search, because the external Ollama process responds too slowly.
>
> **Fix applied:** Switched to `HuggingFaceEmbeddings` which runs directly in Python – no external process, no crash.
> ```python
> from langchain_huggingface import HuggingFaceEmbeddings
> embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
> ```

### ✅ Check-List Version 2
- [ ] Is Ollama running?
- [ ] Is the `.venv` activated?
- [ ] Is `requirements.txt` installed? (includes `sentence-transformers`)
- [ ] Is the `paracetamol.pdf` in the `/documents` folder?

### 📖 How to Use Version 2

**Step 1: Open your Terminal**
```bash
cd ds-rag-pipeline_sia
```
**Step 2: Activate your Environment**
```bash
source .venv/bin/activate
```
**Step 3: Open VS Code / Jupyter Lab**
```bash
jupyter lab
```
**Step 4: Open and run the Notebook**
- Open `RAG_Exercise_Version_02_FAISS.ipynb`
- Run all cells from top to bottom
- Use the chat cell at the end to ask questions

> **Note:** FAISS stores data in RAM. If your Mac slows down, use Version 3 instead.

---

## 🛠️ Version 3: The "Hybrid" Version (Jupyter + Chroma)

- **Goal:** Safe experimentation in the Notebook.
- **How it works:** ChromaDB integrated directly in the Notebook.
- **Storage:** Data is saved to the hard drive, not just RAM.
- **Why use it:** Safer than Version 2 – less likely to crash on M1 Mac.

### ✅ Check-List Version 3
- [ ] Is Ollama running?
- [ ] Is the `.venv` activated?
- [ ] Is `requirements.txt` installed?
- [ ] Is the `paracetamol.pdf` in the `/documents` folder?

### 📖 How to Use Version 3

**Step 1: Open your Terminal**
```bash
cd ds-rag-pipeline_sia
```
**Step 2: Activate your Environment**
```bash
source .venv/bin/activate
```
**Step 3: Open VS Code / Jupyter Lab**
```bash
jupyter lab
```
**Step 4: Open and run the Notebook**
- Open `RAG_Exercise_Version_03_Chroma.ipynb`
- Run all cells from top to bottom
- Use the chat cell at the end to ask questions

> **Note:** ChromaDB saves the index to disk. You can restart the Notebook without rebuilding the index.

---
---

# 🇩🇪 Deutsch

## ⚙️ Einmaliges Setup (Copy & Paste)

> **Hinweis:** Diese Blöcke nur einmal ausführen. Danach reicht jede Session nur `source .venv/bin/activate`.

---

### 🚀 Version 1 Setup (Terminal + ChromaDB)

**macOS**
```bash
pyenv local 3.11.3 && \
python -m venv .venv && \
source .venv/bin/activate && \
pip install --upgrade pip && \
pip install -r requirements.txt && \
pip install chromadb && \
ollama pull llama3.2:3b && \
ollama pull nomic-embed-text
```

**Windows – PowerShell**
```powershell
pyenv local 3.11.3; `
python -m venv .venv; `
.venv\Scripts\Activate.ps1; `
python -m pip install --upgrade pip; `
pip install -r requirements.txt; `
pip install chromadb; `
ollama pull llama3.2:3b; `
ollama pull nomic-embed-text
```

**Windows – Git-Bash**
```bash
pyenv local 3.11.3 && \
python -m venv .venv && \
source .venv/Scripts/activate && \
pip install --upgrade pip && \
pip install -r requirements.txt && \
pip install chromadb && \
ollama pull llama3.2:3b && \
ollama pull nomic-embed-text
```

---

### 🎓 Version 2 Setup (Jupyter + FAISS)

**macOS**
```bash
pyenv local 3.11.3 && \
python -m venv .venv && \
source .venv/bin/activate && \
pip install --upgrade pip && \
pip install -r requirements.txt && \
pip install faiss-cpu sentence-transformers && \
ollama pull llama3.2:3b
```

**Windows – PowerShell**
```powershell
pyenv local 3.11.3; `
python -m venv .venv; `
.venv\Scripts\Activate.ps1; `
python -m pip install --upgrade pip; `
pip install -r requirements.txt; `
pip install faiss-cpu sentence-transformers; `
ollama pull llama3.2:3b
```

**Windows – Git-Bash**
```bash
pyenv local 3.11.3 && \
python -m venv .venv && \
source .venv/Scripts/activate && \
pip install --upgrade pip && \
pip install -r requirements.txt && \
pip install faiss-cpu sentence-transformers && \
ollama pull llama3.2:3b
```

---

### 🛠️ Version 3 Setup (Jupyter + ChromaDB)

**macOS**
```bash
pyenv local 3.11.3 && \
python -m venv .venv && \
source .venv/bin/activate && \
pip install --upgrade pip && \
pip install -r requirements.txt && \
pip install chromadb && \
ollama pull llama3.2:3b && \
ollama pull nomic-embed-text
```

**Windows – PowerShell**
```powershell
pyenv local 3.11.3; `
python -m venv .venv; `
.venv\Scripts\Activate.ps1; `
python -m pip install --upgrade pip; `
pip install -r requirements.txt; `
pip install chromadb; `
ollama pull llama3.2:3b; `
ollama pull nomic-embed-text
```

**Windows – Git-Bash**
```bash
pyenv local 3.11.3 && \
python -m venv .venv && \
source .venv/Scripts/activate && \
pip install --upgrade pip && \
pip install -r requirements.txt && \
pip install chromadb && \
ollama pull llama3.2:3b && \
ollama pull nomic-embed-text
```

---

## 🚀 Version 1: Die "Production" Version (Terminal + Chroma)

- **Fokus:** Maximale Performance & Stabilität.
- **Technik:** Externes Python-Skript (`RAG_Chat_Version_01.py`), ChromaDB (on-disk), Ollama.
- **Vorteil:** Minimaler RAM-Verbrauch, kein Browser-Overhead durch Jupyter. Ideal für den täglichen Einsatz.

### ✅ Checkliste Version 1
- [ ] Läuft Ollama im Hintergrund?
- [ ] Ist die `.venv` aktiviert?
- [ ] Sind die Ollama Modelle geladen? (`llama3.2:3b` + `nomic-embed-text`)
- [ ] Ist `requirements.txt` installiert?
- [ ] Liegt `paracetamol.pdf` im Ordner `/documents`?

### 📖 Bedienungsanleitung Version 1

**Schritt 1: Terminal öffnen**
```bash
cd ds-rag-pipeline_sia
```
**Schritt 2: Umgebung aktivieren**
```bash
source .venv/bin/activate
```
**Schritt 3: Programm starten**
```bash
python RAG_Chat_Version_01.py
```
**Schritt 4: Mit der PDF chatten**
- Warte auf die Meldung: `--- Medical AI Chat (Type 'exit' to stop) ---`
- Tippe deine Frage ein (z.B. *"Wie hoch ist die Dosis für Kinder?"*) und drücke **Enter**
- Tippe `exit` um das Programm zu beenden

> **Wichtig:** Stelle sicher, dass **Ollama** im Hintergrund läuft, bevor du das Skript startest!

---

## 🎓 Version 2: Die "Classic Exercise" (Jupyter + FAISS)

- **Fokus:** Standard-Lernpfad der ursprünglichen Kursübung.
- **Speicher:** FAISS – hält Daten im RAM.

> ### ⚠️ Apple Silicon M1 Fix
> ~~**Ursprüngliches Setup:** `OllamaEmbeddings` mit `nomic-embed-text`~~  
> ~~`from langchain_community.embeddings import OllamaEmbeddings`~~  
> ~~`embeddings = OllamaEmbeddings(model="nomic-embed-text")`~~
>
> **Problem:** `OllamaEmbeddings` verursacht einen Kernel-Crash auf Apple Silicon M1 wenn FAISS eine Suchanfrage macht, weil der externe Ollama-Prozess zu langsam antwortet.
>
> **Fix:** Wechsel zu `HuggingFaceEmbeddings` – läuft direkt in Python, kein externer Prozess, kein Crash.
> ```python
> from langchain_huggingface import HuggingFaceEmbeddings
> embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
> ```

### ✅ Checkliste Version 2
- [ ] Läuft Ollama im Hintergrund?
- [ ] Ist die `.venv` aktiviert?
- [ ] Ist `requirements.txt` installiert? (enthält `sentence-transformers`)
- [ ] Liegt `paracetamol.pdf` im Ordner `/documents`?

### 📖 Bedienungsanleitung Version 2

**Schritt 1: Terminal öffnen**
```bash
cd ds-rag-pipeline_sia
```
**Schritt 2: Umgebung aktivieren**
```bash
source .venv/bin/activate
```
**Schritt 3: VS Code / Jupyter Lab öffnen**
```bash
jupyter lab
```
**Schritt 4: Notebook öffnen und ausführen**
- Öffne `RAG_Exercise_Version_02_FAISS.ipynb`
- Führe alle Zellen von oben nach unten aus
- Nutze die Chat-Zelle am Ende für Fragen

> **Hinweis:** FAISS speichert Daten im RAM. Falls der Mac langsam wird, nutze lieber Version 3.

---

## 🛠️ Version 3: Die "Hybrid" Lösung (Jupyter + Chroma)

- **Fokus:** Flexibilität und sicheres Experimentieren im Notebook.
- **Technik:** ChromaDB direkt im Notebook integriert.
- **Vorteil:** Vermeidet RAM-Abstürze, da Vektoren auf die SSD ausgelagert werden.

### ✅ Checkliste Version 3
- [ ] Läuft Ollama im Hintergrund?
- [ ] Ist die `.venv` aktiviert?
- [ ] Ist `requirements.txt` installiert?
- [ ] Liegt `paracetamol.pdf` im Ordner `/documents`?

### 📖 Bedienungsanleitung Version 3

**Schritt 1: Terminal öffnen**
```bash
cd ds-rag-pipeline_sia
```
**Schritt 2: Umgebung aktivieren**
```bash
source .venv/bin/activate
```
**Schritt 3: VS Code / Jupyter Lab öffnen**
```bash
jupyter lab
```
**Schritt 4: Notebook öffnen und ausführen**
- Öffne `RAG_Exercise_Version_03_Chroma.ipynb`
- Führe alle Zellen von oben nach unten aus
- Nutze die Chat-Zelle am Ende für Fragen

> **Hinweis:** ChromaDB speichert den Index auf der Festplatte. Du kannst das Notebook neu starten ohne den Index neu aufzubauen.
