<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/hoangtrann05/Real-Time-Batch-Data-Pipeline-Vietnam-Gold-Price-Dashboard">
    <img src="docs/logo.png" alt="Logo" width="100" height="100">
  </a>

<h3 align="center">🇻🇳 Vietnam Gold Price Pipeline</h3>

  <p align="center">
    Real-time & Batch Data Engineering Project using Python, Kafka, Spark, Airflow, and PostgreSQL
    <br />
    <a href="https://github.com/hoangtrann05/Real-Time-Batch-Data-Pipeline-Vietnam-Gold-Price-Dashboard"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="#demo">View Demo</a>
    ·
    <a href="https://github.com/hoangtrann05/Real-Time-Batch-Data-Pipeline-Vietnam-Gold-Price-Dashboard/issues">Report Bug</a>
    ·
    <a href="https://github.com/hoangtrann05/Real-Time-Batch-Data-Pipeline-Vietnam-Gold-Price-Dashboard/issues">Request Feature</a>
  </p>
</div>

---

<!-- TABLE OF CONTENTS -->
## 🧭 Table of Contents
- [About The Project](#about-the-project)
  - [Pipeline Overview](#pipeline-overview)
  - [Architecture](#architecture)
  - [Tech Stack](#tech-stack)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Roadmap](#roadmap)
- [Demo](#demo)
- [Contact](#contact)
- [Acknowledgments](#acknowledgments)

---

<!-- ABOUT THE PROJECT -->
## 🪙 About The Project

This project demonstrates a **complete end-to-end data pipeline** for real-time and batch processing of **Vietnam gold price data**.  
It showcases key components of a modern Data Engineering ecosystem — including **Kafka**, **Spark**, **Airflow**, **PostgreSQL**, and **Streamlit Dashboard**.

### 🎯 Objectives
- Build a unified pipeline for gold price collection, cleaning, and analysis.
- Apply both batch and stream processing.
- Automate data orchestration and monitoring.
- Visualize real-time data insights.

---

### 🧱 Pipeline Overview
![Pipeline Diagram](docs/pipeline_diagram.png)
API → Kafka → Spark Streaming → PostgreSQL → Streamlit Dashboard
↑
Airflow DAG (batch ETL)

---

### 🧩 Architecture

| Layer | Tool | Description |
|-------|------|-------------|
| Ingestion | **Kafka, Python (requests)** | Collect real-time data from public gold APIs |
| Transformation | **Pandas, PySpark** | Clean, map schema, and compute KPIs |
| Storage | **PostgreSQL, HDFS** | Persist processed datasets |
| Orchestration | **Apache Airflow** | Manage & schedule ETL workflows |
| Monitoring | **Python logging, Great Expectations** | Ensure data quality |
| Visualization | **Streamlit** | Real-time dashboard |

---

### ⚙️ Tech Stack

[![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)]()
[![Apache Kafka](https://img.shields.io/badge/Kafka-Streaming-orange?logo=apachekafka)]()
[![Apache Spark](https://img.shields.io/badge/Spark-Data_Processing-yellow?logo=apachespark)]()
[![Airflow](https://img.shields.io/badge/Airflow-Orchestration-brightgreen?logo=apacheairflow)]()
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-336791?logo=postgresql)]()
[![Docker](https://img.shields.io/badge/Docker-Container-blue?logo=docker)]()
[![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-ff4b4b?logo=streamlit)]()

---

<!-- GETTING STARTED -->
## 🚀 Getting Started

Follow these steps to set up the project locally.

### 🔧 Prerequisites
- Python ≥ 3.10  
- Docker & Docker Compose  
- Git

### ⚙️ Installation
```bash
# Clone repository
git clone https://github.com/hoangtrann05/Real-Time-Batch-Data-Pipeline-Vietnam-Gold-Price-Dashboard.git
cd vietnam-gold-price-pipeline

# Install dependencies
pip install -r requirements.txt

# Start services
docker-compose up -d
```