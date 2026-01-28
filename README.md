# Scalable Data Analysis using PySpark

This project demonstrates how large-scale datasets can be analyzed efficiently using **Apache Spark (PySpark)** on a local machine.

The goal of the project is to showcase **scalability concepts**, not just data analysis.

---

## Dataset
- **NYC Yellow Taxi Trip Records**
- Stored in **Parquet format**
- Millions of rows (≈3.4M+)
- Columnar storage enables fast reads and compression

⚠️ The dataset is not included in this repository due to size constraints.

---

## Tech Stack
- Python 3.11
- Apache Spark (PySpark 4.x)
- Java 17
- Windows OS

---

## Project Structure

---

## What This Project Demonstrates

- Loading large Parquet datasets using Spark
- Schema inspection and lazy evaluation
- Distributed computation on millions of rows
- Repartitioning to analyze performance behavior
- Spark execution without loading entire data into memory

---

## Key Concepts Shown

- **Scalability over size**: Spark processes data in partitions
- **Lazy execution**: actions trigger computation
- **Columnar storage** advantages with Parquet
- **Fault-tolerant execution model**

---

## How to Run

1. Install **Java 17** and **PySpark**
2. Place the Parquet dataset inside the `data/` folder
3. Run the analysis script:

```bash
python taxi_analysis.py
---

Notes
The dataset is excluded from the repository due to size constraints

This project focuses on scalable data processing concepts, not visualization


Make sure:
- The triple backticks before and after `python taxi_analysis.py` are present

Save the file.

---

## Commit the cleanup

```bat
git add README.md
git commit -m "Clean up README formatting and run instructions"
git push





