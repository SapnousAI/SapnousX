
# SapnousX

**A Self-Hosted, Modular AGI Agent Platform**

SapnousX is a general-purpose AI agent designed to “do anything” a human can on a computer: from shell commands and web browsing to code authoring, video editing, 3D modeling, document generation, and beyond. Built atop a suite of best-in-class LLMs and hosted entirely in isolated Docker sandboxes, SapnousX is your all-in-one programmable assistant and research partner.

---

## 🚀 Project Overview

- **Name:** SapnousX  
- **Goal:** Provide a single agent interface that can plan, execute, and reflect on tasks across any digital domain—CLI, browser, multimedia, 3D design, document processing, communication, and more.  
- **Core Philosophy:**  
  1. **Modular Tools**  
  2. **Privileged-but-isolated Containers**  
  3. **RAG-powered Memory & Summaries**  
  4. **Multi-Model Workflows (Claude, GPT-4.1, Gemini 2.5, Flash)**  
  5. **Self-Improving & Extensible**

---

## 🎯 Key Features & Capabilities

| Category                | Tools & APIs                                      |
|-------------------------|----------------------------------------------------|
| **1. CLI Execution**    | `subprocess`, `pexpect`, `paramiko`                |
| **2. Browser Control**  | Playwright-based “browser-use” Python library       |
| **3. File I/O**         | Create/Edit/Delete/Search via stdlib + TinyDB      |
| **4. Web Search**       | WebScout Toolkit (Google/Bing/Azure abstractions)  |
| **5. Audio I/O**        | Whisper, pyttsx3, gTTS (TTS/STT via WebScout)      |
| **6. Video I/O**        | Qwen models & FFmpeg pipelines                     |
| **7. Image I/O**        | PIL, OpenCV + custom pipelines                     |
| **8. UI Automation**    | `xdotool`, `pyautogui` (keyboard/mouse)            |
| **9. Self-Access Code** | Git integration, AST transforms, self-patching     |
| **10. Tool Creation**   | Scaffold new tools via templates & manifest system |
| **11. Email**           | SMTP/IMAP (via WebScout temp email service)        |
| **12. Telephony**       | SMS/voice via Twilio API (through WebScout)        |
| **13. 3D Design**       | Blender Python API, FreeCAD, OpenSCAD              |
| **14. PDF/Docx**        | LaTeX, python-docx, PyMuPDF                        |
| **15. Spreadsheets**    | CSV/Excel via `pandas`, `openpyxl`                 |
| **16. Slides & HTML**   | `python-pptx`, `reveal.js` templates               |
| **17. MCP Servers**     | Model Context Protocol clients                     |
| **18+. Advanced**       | Memory DB (Qdrant), Planner (AutoGen/ReAct), …     |

---

## 🏗️ Architecture

```

┌───────────────────────┐
│    Client Interface   │  ←─ Chat / REST / CLI
└───────────────────────┘
│
▼
┌───────────────────────┐
│    Sapnous Kernel    │  ←─ Task queue, planner, tool router
└───────────────────────┘
▲       ▲        ▲
│       │        │
│       │        │
┌───┴───┐ ┌─┴────┐ ┌─┴────────┐
│ Tools │ │Memory │ │ Model    │
│ Dir   │ │Store  │ │Registry  │
└───┬───┘ └───┬───┘ └───┬──────┘
│         │         │
▼         ▼         ▼
\[Dockerized Sandboxes running each tool & model]

````

- **Kernel**: Central Python process managing tasks, tool loading, model calls, RAG memory lookups.  
- **Models & Roles**:  
  - **Claude** — primary reasoning & planning  
  - **GPT-4.1** — librarian for chat summarization & context compression  
  - **Gemini 2.5 Pro** — heavy-context, complex tasks  
  - **Flash** — background jobs & housekeeping  
- **WebScout Toolkit**: Provides unified APIs for TTS/STT, email, phone, web search, temp hosting.

---

## ⚙️ Getting Started

### Prerequisites

- Docker & Docker Compose  
- Python 3.10+  
- (Optional) NVIDIA GPU + `nvidia-docker2` for local LLMs  
- Clone this repo:

  ```bash
  git clone https://github.com/your-org/SapnousX.git
  cd SapnousX
````

### Installation

1. **Build Docker images & spin up services**

   ```bash
   docker-compose build
   docker-compose up -d
   ```
2. **Install Python dependencies**

   ```bash
   pip install -r requirements.txt
   ```
3. **Configure credentials**
   Copy `config/.env.sample → config/.env` and fill in:

   * OpenAI / Claude API keys
   * Twilio/SMTP credentials (or leave blank to use WebScout temp services)
   * MCP server endpoints & tokens

### Configuration

* **Tool Registry**: `config/tools.yml` lists all available tools, entrypoint scripts, cost estimates.
* **Models**: `config/models.json` maps tasks → LLM endpoint + prompt templates.
* **Memory**: `config/memory.yml` configures vector DB (Qdrant/Weaviate), embedding model.

---

## ▶️ Usage

Run the main agent process:

```bash
python sapnous_kernel.py
```

Open the Web UI at `http://localhost:8000` (built with FastAPI + React) or interact via CLI:

```bash
sapnous-cli --ask "Fetch latest sales report, summarize key metrics, and email me."
```

---

## 🛠️ Development

1. **Add a new tool**

   * Create `tools/my_tool/manifest.yml` describing name, category, entrypoint.
   * Write the Python wrapper in `tools/my_tool/tool.py`.
   * Add to `config/tools.yml`.

2. **Extend the planner**

   * Edit `sapnous_kernel/planner.py` to add new planning primitives or policies.

3. **Improve memory**

   * Tweak `sapnous_kernel/memory.py` to adjust RAG retrieval strategies.

---

## 📅 Roadmap

* [ ] Vision-to-Action: UI element detection & image-driven automation
* [ ] Multi-Agent Collaboration: Orchestrate sub-agents for complex tasks
* [ ] Real-Time Feedback UI: Live terminal and video stream dashboard
* [ ] Ethical Guardrails & Explainability Module
* [ ] Mobile Agent Extension (iOS/Android)

---

## 🙌 Contributing

1. Fork the repo
2. Create a feature branch (`git checkout -b feature/awesome`)
3. Commit your changes (`git commit -m 'Add awesome feature'`)
4. Push to origin (`git push origin feature/awesome`)
5. Open a PR — we love thoughtful tests & docs!

---

## 📄 License

This project is licensed under the **MIT License**. See [LICENSE](LICENSE) for details.

---

> “SapnousX is not just a tool—it’s the beginning of a self-evolving digital partner.”
> — Atah Alam, Founder & Lead Architect

```
```
