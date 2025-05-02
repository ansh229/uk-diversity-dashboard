# UK Higher Education Staff Diversity Dashboard

This project presents an interactive dashboard that visualises demographic data of staff across UK higher education institutions. Built with Streamlit, it provides insights into diversity characteristics such as ethnicity, gender, nationality, and job classification.

---

## 📁 Project Contents

* `dashboard_figure6.py` – Main Streamlit application
* `figure-6.csv` – Dataset sourced from [data.gov.uk](https://data.gov.uk)
* `requirements.txt` – Required Python packages
* `test_cases_runner.py` – Script to run automated test cases

---

## 🚀 Getting Started

### Using a Virtual Environment 

To avoid package conflicts, it’s best to use a virtual environment.

### 🔧 Setup Instructions

#### 1. **Create a virtual environment**

```bash
python3 -m venv venv
```

#### 2. **Activate the virtual environment**

```bash
source venv/bin/activate  # macOS/Linux
# OR
venv\Scripts\activate     # Windows
```

#### 3. **Install required packages**

```bash
pip install -r requirements.txt
```

#### 4. **Run your Streamlit app**

```bash
streamlit run dashboard_figure6.py
```

#### 5. **Run test cases (optional)**

```bash
python test_cases_runner.py
```

> This will log results into `test_log.txt`

---

##  Features

* Clean and structured data processing from a real government dataset
* Interactive charts: bar, donut, grouped bar, treemap, and sunburst
* Sidebar filters: region, contract type, and demographic category
* Summary cards and live data preview table
* CSV export functionality for filtered views
* Test script with automated logging of results

---


