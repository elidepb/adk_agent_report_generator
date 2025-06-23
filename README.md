# 🤖 AI Research Report Agent

## 📄 Overview

The AI Research Report Agent is an advanced, multi-agent system designed to streamline the research process by generating comprehensive, well-structured, and fact-checked reports on any given topic. Instead of a simple search, this agent engages in a sophisticated, multi-step workflow that includes planning, iterative research, and user collaboration, ensuring the final output is both thorough and aligned with user expectations.

This agent goes beyond simple writing. It can **analyze and replicate your writing style**, allow you to **approve the tone and length**, automatically **manage and format citations**, generate a final report in a professional **PDF format**, and deliver the report in **multiple languages**.

> **Mission:** To transform a simple idea or topic into a polished, professional report, giving you full control over the tone, style, and structure of the content so the result feels truly their own.

---

## ✨ Key Features

| Feature | Description |
| :--- | :--- |
| 🗣️ **Conversational & Collaborative** | The agent engages in a dialogue to understand your needs, including tone, length, and style, before starting the work. |
| 🧬 **Style Analysis & Replication** | Upload a sample document, and the agent will analyze its writing style (formality, sentence structure, vocabulary) and replicate it. |
| ✅ **Approval-Based Workflow (HITL)** | You are in control. The agent will not proceed with writing until you have **explicitly approved** the proposed style and report outline. |
| 📚 **Automated Citation Management** | The agent automatically tracks all web sources used for research and compiles a complete bibliography in **APA, MLA, or Chicago** style. |
| ✍️ **Iterative, Section-Based Writing** | The report is built section by section. For each part, the agent performs focused, deep research, ensuring high-quality and relevant content throughout. |
| 🌐 **Multi-Language Translation** | Once the report is complete, you can request an instant translation into another language. |
| 📑 **Professional PDF Generation** | Receive your final report as a beautifully formatted PDF, complete with a cover page, ready for presentation or distribution. |

---

## 🏗️ Agent Architecture

The system's architecture is a collaborative network of specialized agents, orchestrated by a central `Coordinator`. This design allows for a clear separation of concerns, where each agent is an expert in its specific domain, leading to a more robust and capable system.

![Agent Architecture](resources/diagrams/architecture.png)

---

## 🌊 Agent Workflow

The agent operates in a clear, multi-phase process that prioritizes user alignment before autonomous execution. This ensures the final output is precisely what the user envisioned, moving from high-level planning to detailed creation and final delivery.

![Agent Workflow](resources/diagrams/workflow.png)

---

## 🧠 How the Agent Thinks

This diagram provides a conceptual look into the agent's "internal monologue," showing the decisions and delegations it makes at each step. It illustrates how the different specialized agents are called upon to contribute to the final goal.

![How the Agent Thinks](resources/diagrams/how_the_agent_think.png)

---

## 🔄 Sequence Diagram

For a more technical view, the sequence diagram below details the precise order of API calls and interactions between each component of the system, from the initial user request to the final delivery of all potential artifacts.

![Sequence Diagram](resources/diagrams/sequences.png)

---

## ☁️ Deployment Architecture

The agent is designed for scalable and efficient deployment on Google Cloud. Each agent can be deployed as an independent microservice on Cloud Run, invoking Vertex AI for its powerful generative capabilities and using the Google Search API as its primary tool for information gathering.

![Deployment Architecture](resources/diagrams/deploy.png)

---

## 📁 Project Structure

The project follows a modular structure where each specialized agent resides in its own sub-directory, promoting clear organization and scalability.

```
/report-agent-adk/
├── .env.example              # Example environment variables
├── README.md                   # This documentation file
├── requirements.txt            # Project dependencies for pip
│
├── report_agent/               # Main application directory
│   ├── __init__.py
│   ├── agent.py                # Main Coordinator Agent definition
│   └── prompt.py               # Main Coordinator Agent prompt
│
└── └── sub_agents/             # Directory for all specialized agents
        ├── outline/            # Generates the report outline
        ├── style_analysis/     # Analyzes writing style from a document
        ├── writing/            # Writes content for each section
        ├── report_builder/     # Assembles the final report
        ├── reference_formatting/ # Formats the bibliography
        ├── translation/        # Translates the final report
        ├── pdf_generator/      # Creates the final PDF document
        └── web_search/         # A tool-agent for web searches
```

---

## 🛠️ Technology Stack

-   **Core Framework:** Google Agent Development Kit (ADK)
-   **Language:** Python 3.11+
-   **Dependency Management:** pip
-   **AI Model:** Google Gemini 1.5 Pro (via Vertex AI)
-   **Core Tool:** Google Search
-   **Key Libraries:** FPDF2 (for PDF Generation), Markdown2

---

## 🚀 Setup and Installation

### 1. Prerequisites

-   Python 3.11+
-   `pip` for dependency management.
-   A Google Cloud Project with the Vertex AI API enabled.
-   Google Cloud SDK (`gcloud` CLI) installed and authenticated.

### 2. Installation

First, clone the repository and navigate into the project directory:
```bash
# Clone this repository
git clone <your-repository-url>
cd report-agent-adk

# Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

# Install dependencies using pip
pip install -r requirements.txt
```

### 3. Configuration

Create a `.env` file in the root of the project directory by copying the `.env.example` file.

```bash
cp .env.example .env
```

Now, edit the `.env` file with your credentials. Using Vertex AI is highly recommended for full functionality.

```bash
# .env file
GOOGLE_GENAI_USE_VERTEXAI=true
GOOGLE_CLOUD_PROJECT="your-gcp-project-id"
GOOGLE_CLOUD_LOCATION="your-gcp-region" # e.g., us-central1
```

---

## ▶️ Running the Agent

You can interact with your agent using a command-line interface (CLI) or a web UI.

-   **To run via CLI:**
    ```bash
    adk run report_agent
    ```
-   **To run via Web Interface:**
    ```bash
    adk web .
    ```
    This will start a local web server. Open the URL, select `report_agent`, and begin your conversation.

---

## 💬 Example Interaction

Here is a sample workflow featuring the agent's core functionalities.

**👤 User:**
> I need a report on the history of quantum computing. I want an academic tone.

**🤖 Agent (Coordinator):**
> Of course! For the "academic" tone, I will use formal language, complex sentence structures, and a focus on objective analysis. Do you have a sample document you'd like me to analyze to further refine the style, or shall I proceed with this general academic pattern? Also, please let me know your preferred citation style (e.g., APA, MLA, Chicago).

**👤 User:**
> Let's stick with the general academic pattern for now. Please use APA 7th edition.

**🤖 Agent (Coordinator):**
> Perfect. I will now generate a proposed outline for the report on the history of quantum computing.

*(A few moments later...)*

**🤖 Agent (Coordinator):**
> Here is the proposed structure for the report. Do you approve it so we can begin writing?
>
> 1.  **The Theoretical Origins (1900-1980):** This section will cover the foundational ideas from quantum mechanics that predicted quantum computational phenomena...
> 2.  **Early Models and Algorithms (1981-1993):** This part will discuss the pioneering work of Feynman, Deutsch, and the development of key algorithms like Shor's and Grover's...
> 3.  *(...and so on)*

**👤 User:**
> Looks great, please proceed.

*(The agent begins its work, providing updates as it completes each section.)*

**🤖 Agent (Report Builder):**
> (internal)SECTION COMPLETED: 1. The Theoretical Origins (1900-1980)
> (internal)SECTION COMPLETED: 2. Early Models and Algorithms (1981-1993)
> *(...)*

*(After completion...)*

**🤖 Agent (Coordinator):**
> The full report on the history of quantum computing is complete and ready for you below. Would you like me to translate it to another language or generate a PDF version?

---

## 🎨 Customization

This agent is designed to be a canvas for your ideas.

* **Adjust Style Analysis:** Modify the `StyleAnalysisAgent`'s prompt to look for different features in texts (e.g., use of metaphors, data density, rhetorical devices).
* **Expand Citation Styles:** Add new prompts and logic to the `ReferenceFormattingAgent` to support other citation styles like Harvard or Vancouver.
* **Integrate Internal Sources:** Equip the `WebSearchAgent` (or create a new agent) with tools to search your internal databases, Confluence, or Google Drive, so reports can include proprietary knowledge.
* **Add New Output Formats:** Create new tools to convert the final Markdown into other formats like `.docx` or `.html` with custom CSS.

---

## 🛠️ Troubleshooting and Common Issues

* **Issue: The agent stops responding after I approve the outline.**
    * **Cause:** The report generation process is long and intensive. A 7-section report can take **15-35 minutes**. It is most likely still working in the background.
* **Issue: The replicated writing style doesn't perfectly match the source document.**
    * **Cause:** The style analysis captures the essence (tone, structure, complexity) but is not an exact imitation. The quality and length of the source document are also key.
    * **Solution:** Provide a longer, more representative text document for the style you want. You can also refine the `StyleAnalysisAgent`'s prompt to focus on the aspects that matter most to you.

---

## ✨ Optimization and Adjustment Tips

* **Quick Style Tests:** To test the style replication feature, ask for a very short report (a single paragraph) on a simple topic. This will allow you to validate the style analysis without waiting for a full report.
* **Define a Glossary:** If the report is on a highly technical topic, you can customize the `WritingAgent`'s prompt to use a specific glossary of terms, ensuring consistency.
* **Optimize for Speed vs. Quality:** In the code, you can configure which Gemini model to use for each agent. Use a faster, more economical model (like Gemini 2.5 Flash) for simple tasks (like the `Coordinator`) and a more powerful model (like Gemini 2.5 Pro) for complex tasks like writing (`WritingAgent`) and style analysis.