# AgenticWorkflow - Tree of Thought Analysis with Reflection 

## Project Overview 📚

AgenticWorkflow implements an advanced analytical framework using Tree of Thought methodology enhanced with reflection techniques. This project leverages ChatGPT models from OpenAI to perform deep, multi-perspective analysis of complex questions through structured branching and reflection.

## Core Concept: Tree of Thought with Reflection 🧠

### Tree of Thought (ToT) Approach 🌳
The Tree of Thought methodology starts with a root question that branches into multiple perspectives. Each perspective is then further analyzed through sub-branches that focus on specific aspects of the initial branch. This creates a comprehensive analytical structure where:

1. The "First question ( Root )"  defines the overall analysis scope
2. Primary branches represent major analytical perspectives
3. Sub-branches explore specialized dimensions within each perspective
4. Each branch receives tailored prompt instructions specific to its analytical focus

### Reflection Enhancement ✔️
The reflection technique enriches the Tree of Thought approach by:

1. Reviewing initial perspective outputs for accuracy and completeness
2. Identifying potential gaps or weaknesses in the reasoning
3. Refining arguments to increase clarity and professionalism
4. Adding nuance before the perspective informs sub-branches
5. Ensuring each analytical thread maintains high quality throughout the tree

This combined approach ensures that each branch not only addresses its designated perspective but does so with refined reasoning and enhanced analytical depth.

## Architecture 🛠️

### Primary Branches 🌿
- **Domestic Market Competition**: Analyzes competitive dynamics between Chinese and Thai businesses
- **Consumer Behavior**: Examines shifts in Thai consumer preferences and spending patterns

### Sub-Branches 🍃

**Domestic Market Competition:**
- Price Undercutting: Effects on Thai producers and vulnerable sectors
- Market Share Losses: Displacement of local products and survival strategies
- Innovation and Quality Improvement: Need for innovation and R&D investments

**Consumer Behavior:**
- Demand for Cheaper Goods: Shifting preferences and impact on local brands
- Disposable Income and Spending Patterns: Changes in consumer purchasing power
- Brand Loyalty and Perception: Erosion of loyalty and perception of Chinese products

### Workflow Process ⚙️ 

1. Initial perspectives are generated for primary branches
2. Reflection is applied to these perspectives for refinement
3. Sub-branch analyses are created using the refined perspectives
4. Selected sub-branch outputs are combined
5. A final conclusion synthesizes all insights

## Case Study: Analysis of Chinese Price War Impact on Thailand's Economy

This project analyzes the question: **"What is the potential impact of Chinese price war on Thailand economy?"**

The analysis is structured as follows:

1. **Root Question**: The potential impact of Chinese price war on Thailand's economy
   
2. **Primary Branch #1: Domestic Market Competition**
   - Initial analysis of competitive dynamics
   - *Reflection applied*
   - Sub-branches analyze:
     - Price undercutting effects on Thai producers
     - Market share losses across different sectors
     - Innovation requirements to maintain competitiveness

3. **Primary Branch #2: Consumer Behavior**
   - Initial analysis of shifting consumer dynamics
   - *Reflection applied*
   - Sub-branches analyze:
     - Changes in demand for cheaper goods
     - Effects on disposable income and spending patterns
     - Impacts on brand loyalty and perception
  
4. **Conclusion Generation**: 
   - Selected sub-branch insights are aggregated
   - Comprehensive conclusion synthesizes all perspectives
   - Balanced assessment of positive and negative impacts

This structured approach allows for comprehensive analysis of complex economic dynamics from multiple angles while maintaining analytical rigor through reflection processes.

## ✅ Benefits 

- **Comprehensive Analysis**: Examines issues from multiple specialized perspectives
- **Enhanced Reasoning**: Reflection stages improve quality of analysis
- **Structured Approach**: Tree of Thought methodology provides clear organization
- **Customizable Depth**: Branches can be added or removed based on analytical needs
- **Developer Control**: Manual curation of which sub-branches to include in final analysis
- **Perspective Isolation**: Each perspective receives specialized prompt instructions
- **Improved Output Quality**: Reflection processes refine and enhance initial analyses

## 🚀 Applications

While the example implementation analyzes Chinese price war impacts on Thailand's economy, this framework can analyze any complex question requiring multi-perspective thinking, including:

- Economic policy analysis
- Market entry strategy development
- Competitive landscape assessment
- Social impact studies
- Risk analysis for investment decisions
- Policy consequence evaluation
  

## Project Structure 📁

```bash
AgenticWorkflow/
├── agentic_workflow/
│   ├── __init__.py
│   ├── config.py                         # API keys and model configuration
│   ├── core/
│   │   ├── __init__.py
│   │   ├── reflection.py                 # Reflection implementation
│   │   └── tot.py                        # Tree of Thought core logic
│   ├── perspectives/
│   │   ├── __init__.py
│   │   ├── domestic_market/
│   │   │   ├── __init__.py
│   │   │   ├── price_undercutting.py     # Sub-branch implementation
│   │   │   ├── market_share_losses.py    # Sub-branch implementation
│   │   │   └── innovation_quality.py     # Sub-branch implementation
│   │   └── consumer_behavior/
│   │       ├── __init__.py
│   │       ├── demand_cheaper_goods.py   # Sub-branch implementation
│   │       ├── disposable_income.py      # Sub-branch implementation
│   │       └── brand_loyalty.py          # Sub-branch implementation
│   └── utils/
│       ├── __init__.py
│       └── llm_handler.py                # LLM API interaction handler
├── examples/
│   ├── economic_analysis.py              # Example script for economic analysis
│   └── custom_analysis.py                # Template for custom analysis
├── main.py                               # Main script to run the analysis
├── requirements.txt                      # Project dependencies
└── README.md                             # Project documentation
```

## Installation & Usage 🚀

Clone the repository and set up the environment:

```bash
# Clone the repository
git clone https://github.com/username/AgenticWorkflow.git
cd AgenticWorkflow
```

### Create Virtual Environment (optional but recommended)

```bash
python -m venv venv
```

###  Activate Virtual Environment (venv)
```bash
source venv/bin/activate  # On MacOS use this
venv\Scripts\activate     # On Windows use this 
```
### Install dependencies
```bash
pip install -r requirements.txt
```


## Configure API key
#### Edit agentic_workflow/config.py with your API key

## Run the analysis

```bash
python main.py
```

## Example Analysis & Output 📊

### Input Query:

**What is the potential impact of Chinese price war on Thailand economy?**


### Output Summary:

Based on the user's input, the best conclusion is that Thai businesses and policymakers should focus on strategies such as diversifying export markets, enhancing product differentiation, strengthening domestic market presence, innovating and improving efficiency, and enhancing export competitiveness in order to mitigate the potential negative impact of a Chinese price war. Additionally, Thai industries should invest in technology and research and development, implement quality management systems, and explore diversification strategies to compete on quality rather than price. Furthermore, Thai brands should address potential erosion of brand loyalty through strategic marketing communications that emphasize unique attributes and differentiate themselves from Chinese competitors
