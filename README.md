# CrewAI Series

In this repository, I document my learning journey with CrewAI from basic to advanced concepts. The repository includes Jupyter notebooks demonstrating foundational concepts and complete CrewAI projects showcasing multi-agent systems.

## Contents

### Jupyter Notebooks
- **`basic_setup.ipynb`**: Initial setup and configuration for working with CrewAI, covering basic agent and crew creation.
- **`custom_tool.ipynb`**: Demonstrates how to create and integrate custom tools into CrewAI workflows.

### CrewAI Projects

#### 1. Research and Blog (`research_and_blog/`)
A multi-agent system that researches a topic and generates blog content.
- **Agents**: Report Generator, Blog Writer
- **Tasks**: Research report generation, blog post writing
- **Output**: Comprehensive research reports and engaging blog posts
- **Features**: Sequential workflow, custom output files

#### 2. Market Research Crew (`market_research_crew/`)
A multi-agent system designed for market research and analysis.
- **Agents**: Market research specialists
- **Tasks**: Market analysis and research tasks
- **Features**: Collaborative agent workflows

## Getting Started

### Prerequisites
- Python >=3.10 <=3.13
- [UV](https://docs.astral.sh/uv/) for dependency management

### Running Jupyter Notebooks
```bash
jupyter notebook basic_setup.ipynb
```

### Running CrewAI Projects
Navigate to the specific project directory and run:
```bash
cd research_and_blog  # or market_research_crew
crewai install
crewai run
```

### Configuration
Each CrewAI project requires API keys in a `.env` file:
- `GEMINI_API_KEY`: For Google AI Studio Gemini models
- Or `OPENAI_API_KEY`: For OpenAI models

## Project Structure
```
crewai-series/
├── basic_setup.ipynb          # Basic concepts notebook
├── custom_tool.ipynb          # Custom tools tutorial
├── research_and_blog/         # Research & blog generation crew
│   ├── src/
│   ├── config/
│   └── .env
└── market_research_crew/      # Market research crew
    ├── src/
    ├── config/
    └── .env
```

Stay tuned for updates as I expand this repository with more advanced concepts and real-world applications!


