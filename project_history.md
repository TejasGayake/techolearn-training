# Internship Practice Portfolio Overview

This document reconstructs a realistic learning timeline for a data science internship trainee based on practice work completed between January and May 2026. The repository contains 89+ files across 23 directories covering Python, NumPy, Pandas, SQL, Matplotlib, Statistics, Feature Engineering, Power BI, Tableau, and Machine Learning.

The work reflects **authentic trainee behavior** — gradual skill building, debugging, experimentation, revision, and occasional incomplete or messy code.

---

# Technical Skills Learned

| Skill Area | Topics Covered | Proficiency Level |
|---|---|---|
| **Python Basics** | Pattern printing, list comprehensions, functions, generators, lambda, file I/O | Beginner → Intermediate |
| **NumPy** | Array creation, broadcasting, aggregation, sorting, random module, vectorization | Intermediate |
| **Pandas** | Series/DataFrame, CRUD, missing data handling, groupby, merge, concat, file export/import | Intermediate |
| **SQL (SQLite)** | CREATE, INSERT, SELECT, WHERE, JOINs, subqueries, keys, aggregate functions | Intermediate |
| **SQL (MySQL)** | Database connection from Python, CRUD application | Beginner |
| **Matplotlib** | Line, bar, pie, histogram, scatter, subplots, customization | Intermediate |
| **Seaborn** | Barplot, countplot, boxplot, heatmap, pairplot, violinplot, regplot | Intermediate |
| **Statistics** | Descriptive stats, variance, SD, binomial/poisson/normal distribution, hypothesis testing | Intermediate |
| **Outlier Detection** | Z-score, IQR, capping, imputation, log/sqrt transformation | Intermediate |
| **Sampling** | Random, stratified, cluster, convenience, snowball, systematic | Beginner-Intermediate |
| **Feature Engineering** | Numerical features, binning, encoding (label, one-hot, ordinal, frequency), scaling (normalization, standardization) | Intermediate |
| **Data Cleaning** | Missing value imputation, date parsing, duplicate handling, string normalization | Intermediate |
| **Power BI** | Dashboards, DAX measures, calculated columns, slicers, themes, visualizations | Beginner-Intermediate |
| **Tableau** | Workbooks, sheets, visualizations, dashboards | Beginner |
| **Machine Learning** | Linear Regression, Logistic Regression, KNN (Euclidean/Manhattan/Minkowski), Decision Tree theory | Beginner |

---

# Folder Structure

```
TecholearnLearnTraining/
├── 01_numpy_library/            (7 files)  - NumPy basics to advanced
├── 02_pandas_library/           (12 files) - Pandas series, dataframe, I/O
├── 03_sqllite/                  (1 file)   - SQLite setup
├── 0_assigments/                (7 files)  - Statistics, outlier, CI, feature eng, lambda, generators
├── 10_Data_cleaning_preparion/  (1 file)   - Data cleaning pipeline
├── 11_project/                  (1 file)   - Consolidated stats project (mixStats)
├── 12_feature_engineering/      (4 files)  - Features, encoding, scaling
├── 13_sql/                      (8 files)  - SQL clauses, joins, keys, assignments
├── 14===================================== (empty dir - placeholder)
├── 15_seaborn/                  (2 files)  - Seaborn visualization practice
├── 16_excel/                    (4 files)  - Excel file practice
├── 17_mini_project/             (1 file)   - Inventory management project
├── 18_power_BI/                 (9+ files) - Power BI dashboards and themes
├── 19_tableu/                   (3 files)  - Tableau workbooks
├── 20_ml/                       (6 files)  - ML algorithms
├── 4_operations/                (6 files)  - Pandas CRUD, missing data
├── 5_SQL_type_operation_on_df/  (1 file)   - Sort, groupby, merge on dataframes
├── 6_matplotlib/                (7 files)  - Matplotlib plotting
├── 7_staticstics/               (6 files)  - Statistics & distributions
├── 8_Outlier detection_&_treatment.py/ (2 files) - Outlier methods & hypothesis testing
├── 9_sampling_techniques.py/    (3 files)  - Sampling, covariance, correlation
├── logs/                        (1 file)   - Trading API error logs
├── a.py                         - Pattern printing exercise
├── t.py                         - Pattern printing draft
├── dashboard.py                 - Streamlit trading dashboard
├── machine test.py              - Machine test questions
├── prompt.md                    - This analysis prompt
└── Student_Data_raw.xlsx        - Generated student dataset
```

---

# File-by-File Timeline Analysis

## Phase 1: Python Basics & Introductory NumPy (Late Jan – Early Feb 2026)

### Root Python Files

| File | Created | Modified | Purpose | Complexity |
|---|---|---|---|---|
| `t.py` | Feb 23 | Feb 23 | Pattern printing draft — commented out attempt at star patterns | Beginner |
| `a.py` | Feb 23 | Feb 23 | Star pattern printing — diamond shape with hollow center | Beginner |

**Learning Purpose**: Basic Python loops, string multiplication, conditional logic in pattern printing.
**Probable Period**: Late January 2026 (timestamps may reflect file recreation, not original creation).

### `01_numpy_library/`

| File | Modified | Purpose | Complexity |
|---|---|---|---|
| `numpyy.py` | Feb 5 | Notes file listing NumPy topics (broadcasting, aggregation, boolean indexing, etc.) | Beginner |
| `timer.py` | Feb 3 | Performance comparison: Python list comprehension vs NumPy vectorization (1M elements) | Beginner-Intermediate |
| `1_NumpyLecture.py` | Apr 8 | NumPy array creation (zeros, ones, full, eye, arange, linspace), random module, array attributes, indexing | Intermediate |
| `2_NumpyLecture2.py` | Apr 8 | Math operations (sqrt, exp, log, sin/cos), aggregation (min, max, mean, median), reshape, transpose, flatten, stacking, splitting | Intermediate |
| `3_numpy array__.py` | Feb 8 | Broadcasting, axis aggregation, boolean filtering, sorting, argsort, where, searchsorted | Intermediate |
| `test1.py` | Apr 8 | Random module practice — reworked version of commented-out sections from Lecture 1 | Beginner-Intermediate |

**Learning Purpose**: Systematic NumPy coverage — from basic array creation through advanced operations like broadcasting, boolean indexing, and searchsorted.
**Probable Period**: Late January – Early February 2026, with later revisions in April.

---

## Phase 2: Pandas & Data Manipulation (Early – Mid Feb 2026)

### `02_pandas_library/`

| File | Modified | Purpose | Complexity |
|---|---|---|---|
| `1_broadcasting.py` | Feb 12 | Documentation/notes explaining broadcasting concept for NumPy arrays | Beginner |
| `2_creating_series.py` | Feb 17 | Pandas Series creation (default index, custom index, from dict, scalar, from NumPy array) | Beginner |
| `3_operation_on_series.py` | Feb 12 | Series indexing (loc/iloc), slicing, aggregation (sum, mean) | Beginner |
| `4_dataframe.py` | Feb 12 | DataFrame creation (dict, list, NumPy array, Series → dict → DataFrame) | Beginner |
| `5_DataFrame_arributes.py` | Feb 4 | DataFrame attributes (shape, size, ndim, columns, values, head, tail, info, describe) | Beginner |
| `unknown.py` | Feb 6 | DataFrame export (CSV, Excel, JSON), SQLite integration (to_sql, read_excel, read_sql) | Intermediate |
| `Student_data.csv` | Feb 6 | Generated CSV from DataFrame export | - |
| `Student_data_excel.xlsx` | Feb 6 | Generated Excel file from DataFrame export | - |
| `Student_data_json.json` | Feb 6 | Generated JSON from DataFrame export | - |
| `Students_Data.db` | Feb 6 | SQLite database created from DataFrame | - |
| `student_data.txt` | Jan 29 | Raw text data file (earliest file in repo) | - |

### `4_operations/` (Duplicate practice folder)

| File | Modified | Purpose | Complexity |
|---|---|---|---|
| `2_curd_operations.py` | Feb 6 | DataFrame CRUD: add column, modify values, conditional updates, drop columns | Beginner-Intermediate |
| `3_Missing_data_handling.py` | Feb 6 | Missing value detection, dropna, fillna (const, ffill, bfill, mean imputation) | Intermediate |
| `a.py` | Feb 6 | DataFrame export + SQLite (same content as unknown.py in pandas_library) | Intermediate |

### `03_sqllite/`

| File | Modified | Purpose | Complexity |
|---|---|---|---|
| `1_sqlite_operation.py` | Feb 8 | SQLite connection setup, cursor creation, CREATE TABLE execution, commit understanding | Beginner |

### `5_SQL_type_operation_on_df/`

| File | Modified | Purpose | Complexity |
|---|---|---|---|
| `1_.py` | Feb 9 | DataFrame sort_values, sort_index, groupby (groups, agg, transform), merge (inner/right), join, concat, loc/iloc | Intermediate |

**Learning Purpose**: Comprehensive Pandas practice — from basic Series/DataFrame creation through advanced operations like groupby transforms, merges, and SQLite integration.
**Probable Period**: Early – Mid February 2026.

---

## Phase 3: Data Visualization — Matplotlib (Mid Feb 2026)

### `6_matplotlib/`

| File | Modified | Purpose | Complexity |
|---|---|---|---|
| `1_ploting_methods.py` | Feb 14 | Line plot with markers, line styles, colors, figure sizing, grid customization | Beginner-Intermediate |
| `2_bar_plot.py` | Feb 10 | Vertical bar, horizontal bar, sales comparison with multiple lines + legend | Intermediate |
| `3_pie_chart.py` | Feb 10 | Pie chart with autopct, custom colors, startangle | Beginner |
| `4_subplot.py` | Feb 10 | Subplots (1x2): line chart + bar chart in one figure | Intermediate |
| `5_histogram.py` | Feb 10 | Histogram with density, bins, edgecolor; overlay line plot with bin centers | Intermediate |
| `6_scatter_plot.py` | Feb 10 | Scatter plot with text annotations | Beginner |

**Learning Purpose**: Systematic Matplotlib coverage — all major plot types with customization. 
**Probable Period**: February 10–14, 2026.

---

## Phase 4: Statistics & Probability (Mid – Late Feb 2026)

### `7_staticstics/`

| File | Modified | Purpose | Complexity |
|---|---|---|---|
| `1_DiscriptiveStats.py` | Feb 13 | Mean, median, mode (including multi-mode detection), skewness, kurtosis, histogram | Intermediate |
| `2_variance_&_SD.py` | Feb 12 | Sample/population variance, standard deviation, range, coefficient of variation | Intermediate |
| `3_Binomial_D.py` | Feb 13 | Binomial probability (manual + scipy), PMF bar plot | Intermediate |
| `4_Possion_D.py` | Mar 6 | Poisson distribution (manual + scipy), PMF bar plot | Intermediate |
| `5_normal_D_important.py` | Feb 18 | Z-score calculation, manual normal PDF, scipy norm.pdf, bell curve plot | Intermediate |

### `8_Outlier detection_&_treatment.py/`

| File | Modified | Purpose | Complexity |
|---|---|---|---|
| `1_Statistical_mtds_for_outlier_dtctn.py` | Feb 19 | Z-score outlier detection, IQR method, capping (percentile clip), median imputation, log/sqrt transformation | Intermediate-Advanced |
| `2_hypothesis testing.py` | Feb 20 | One-sample t-test (manual + scipy), confidence interval calculation, null hypothesis rejection | Intermediate-Advanced |

### `9_sampling_techniques.py/`

| File | Modified | Purpose | Complexity |
|---|---|---|---|
| `1_Sampling_techniques.py` | Feb 26 | Non-probability (cluster, convenience, snowball), probability (simple random, systematic), stratified sampling | Intermediate |
| `2_covariance.py` | Feb 27 | Covariance (manual + NumPy), covariance matrix interpretation | Intermediate |
| `3_correlation.py` | Feb 27 | Pearson correlation (manual formula + np.corrcoef) | Intermediate |

### `10_Data_cleaning_preparion/`

| File | Modified | Purpose | Complexity |
|---|---|---|---|
| `1_handling_missing_data.py` | Feb 27 | End-to-end data cleaning: string normalization, mean imputation, mode imputation, duplicate removal, date parsing with coerce, salary capping via quantile | Intermediate |

**Learning Purpose**: Complete statistics pipeline — from descriptive stats through probability distributions, outlier detection, hypothesis testing, sampling, and correlation analysis.
**Probable Period**: February 12–27, 2026.

---

## Phase 5: Feature Engineering (Early March 2026)

### `12_feature_engineering/`

| File | Modified | Purpose | Complexity |
|---|---|---|---|
| `1_features.py` | Mar 5 | Numerical feature creation (price_per_sq_ft, age, area_per_bedroom), binning (pd.cut), text features (word count, keyword detection) | Intermediate |
| `2_encoding_techinques.py` | Mar 5 | Label encoding, one-hot encoding, ordinal encoding, frequency/count encoding | Intermediate |
| `3_feature_scaling.py` | Mar 6 | Min-Max Normalization, Standardization (Z-score), with practice dataset | Intermediate |

**Learning Purpose**: Core feature engineering techniques — creating features, encoding categories, scaling numerical data.
**Probable Period**: March 5–6, 2026.

---

## Phase 6: SQL (Mid – Late March 2026)

### `13_sql/`

| File | Modified | Purpose | Complexity |
|---|---|---|---|
| `1_clauses.sql` | Mar 17 | Database/table creation, INSERT, WHERE (AND, IN, LIKE), ORDER BY, DISTINCT, aggregate, GROUP BY, HAVING, complete query composition | Intermediate |
| `joints.md` | Mar 17 | Notes: Inner, Left, Right, Full, Self join definitions | Beginner |
| `2_joins.sql` | Mar 18 | Join practice queries | Intermediate |
| `3_keys.sql` | Mar 18 | Primary/foreign key creation, subqueries (single row, multi-row, correlated) | Intermediate |
| `keys.sql` | Mar 19 | Extended subquery practice (single row, multi-level, correlated) | Intermediate |
| `sql_assignment.sql` | Mar 29 | Full assignment: 4-table schema (Customers, Products, Orders, OrderItems), 15 queries including joins, aggregation, subqueries, advanced SQL | Intermediate-Advanced |
| `sql assignment1.sql` | Apr 1 | Similar assignment with different data and same query structure | Intermediate-Advanced |
| `sqlIntegration.py` | Mar 30 | Python-MySQL CRUD application: add/view/update/delete students with menu-driven interface | Intermediate |

**Learning Purpose**: Complete SQL journey — from basic clauses through complex multi-table queries, subqueries, and Python integration.
**Probable Period**: March 17 – April 1, 2026.

---

## Phase 7: Assignments & Python Advanced (Late March – Early April 2026)

### `0_assigments/`

| File | Modified | Purpose | Complexity |
|---|---|---|---|
| `1_discriptive_stats_assignmetn.py` | Mar 6 | Statistics assignment: mean, median, mode, variance, SD on sales data | Intermediate |
| `2_outlier_dection_assignment.py` | Mar 6 | Outlier detection assignment: Z-score and IQR methods across 6 datasets | Intermediate |
| `3_CI.py` | Mar 17 | Confidence interval calculation, covariance and correlation interpretation | Intermediate |
| `4_feature_engineering.py` | Mar 25 | Comprehensive feature engineering assignment: 2 datasets with cleaning, numeric features, binning, encoding, text features | Intermediate-Advanced |
| `5_generator.py` | Mar 28 | Python generators: number generator, even numbers, Fibonacci, generator expression, character generator | Intermediate |
| `7_lambda function.py` | Mar 28 | Lambda functions: map (cubes), filter (primes), reduce (product), conditional lambda, discount, salary, GST, string operations | Intermediate |

**Learning Purpose**: Applied practice through structured assignments combining statistics, outlier detection, feature engineering, and Python advanced concepts.
**Probable Period**: March 6–28, 2026.

---

## Phase 8: Seaborn, Excel, Mini Projects (Early – Mid April 2026)

### `15_seaborn/`

| File | Modified | Purpose | Complexity |
|---|---|---|---|
| `1_plots_using_sns.py` | Apr 2 | Seaborn: tips dataset exploration, barplot, countplot, scatter, histogram (with KDE), boxplot, heatmap, pairplot, lineplot, violinplot, regplot, subplot | Intermediate |

### `16_excel/`

| File | Modified | Purpose | Complexity |
|---|---|---|---|
| `1_sheet.xlsx` | Apr 3 | Empty Excel file (placeholder) | - |
| `Book1.xlsx` | Apr 7 | Excel practice file | - |
| `Book3.xlsx` | Apr 7 | Excel practice file | - |

### `17_mini_project/`

| File | Modified | Purpose | Complexity |
|---|---|---|---|
| `project9.py` | Apr 18 | Inventory management: stock tracking, total value, category profit, expiry risk detection, purchase planning with conditional rules | Intermediate |

### Root Files

| File | Modified | Purpose | Complexity |
|---|---|---|---|
| `machine test.py` | Apr 8 | Machine test: cubes list, random sampling, category encoding, Z-scores, array reshape, SQL query, chatbot | Intermediate |
| `dashboard.py` | Apr 18 | Streamlit dashboard (trading): watchlist, candlestick charts, alerts panel, auto-refresh — imports from external modules (data.processor, indicators.calculator, angel_api.client) | Advanced |

### `11_project/`

| File | Modified | Purpose | Complexity |
|---|---|---|---|
| `1_mixStats.py` | Apr 8 | Consolidated statistics project: synthetic data generation, descriptive stats, probability, distributions (normal, binomial, poisson), outlier detection, sampling (random + stratified), confidence interval, correlation, covariance | Intermediate-Advanced |

**Learning Purpose**: Applied projects consolidating multiple skills — Seaborn visualization, Streamlit dashboard, inventory management, and a comprehensive statistics project.
**Probable Period**: April 2–18, 2026.

---

## Phase 9: Power BI (Late April 2026)

### `18_power_BI/`

| File | Modified | Purpose |
|---|---|---|
| `Calculated Colums.pbix` | Apr 28 | Power BI calculated columns practice |
| `Dashboard Demo.pbix` | Apr 29 | Dashboard demonstration |
| `Dashboard_Demo.zip` | Apr 29 | Zipped backup of dashboard |
| `DATA FOR VISUAL1.pbix` | Apr 29 | Data preparation for visualizations |
| `DAX Measures.pbix` | Apr 29 | DAX measure creation practice |
| `Liquid_Glass_Dashboard.pbix` | Apr 29 | Styled dashboard with liquid glass theme |
| `liquid_glass_pro.json` | Apr 29 | Custom theme JSON (professional) |
| `liquid_glass_theme.json` | Apr 29 | Custom theme JSON (liquid glass style) |
| `madhav_Ecommerce_project.pbix` | Apr 29 | E-commerce sales dashboard |
| `Sales Dashboard.pbix` | Apr 29 | General sales dashboard |
| `Slicer tlt.pbix` | Apr 29 | Slicer/filter practice |
| `Tlt Charts.pbix` | Apr 29 | Chart type exploration |
| `tlt_powerbi.pbix` | Apr 29 | Power BI integrated practice |

**Learning Purpose**: Power BI exploration — creating dashboards, DAX measures, calculated columns, custom themes, slicers.
**Probable Period**: April 28–29, 2026 (intensive 2-day session).

---

## Phase 10: Tableau (Early May 2026)

### `19_tableu/`

| File | Modified | Size | Purpose |
|---|---|---|---|
| `Book1.twb` | May 6 | 67 KB | Initial Tableau workbook |
| `Book2.twb` | May 7 | 155 KB | More complex Tableau workbook |
| `Book3.twb` | May 8 | 138 KB | Advanced Tableau workbook |

**Learning Purpose**: Tableau introduction — creating workbooks with increasing complexity.
**Probable Period**: May 6–8, 2026.

---

## Phase 11: Machine Learning (Mid – Late May 2026)

### `20_ml/`

| File | Modified | Purpose | Complexity |
|---|---|---|---|
| `1_linear_regression.py` | May 15 | Linear Regression: study hours vs marks prediction, model fitting, prediction for new input | Intermediate |
| `2_Logistic_Regression.py` | May 19 | Logistic Regression: study hours → pass/fail classification, train/test split, prediction | Intermediate |
| `2_Logistic_Regression.ipynb` | May 19 | Jupyter notebook version (same code) | Intermediate |
| `3_ex.md` | May 21 | Decision Tree theory: Gini Index calculation walkthrough, tree visualization | Intermediate-Advanced |
| `3_KNN_algorithm.ipynb` | May 21 | KNN: Euclidean distance calculation (manual), Scikit-learn KNN with Euclidean/Manhattan/Minkowski metrics (has execution errors indicating learning-in-progress) | Intermediate |
| `4_Decision_Tree.ipynb` | May 23 | Empty notebook (newly created, work in progress) | - |

**Learning Purpose**: ML algorithm implementation — Linear Regression first, then classification (Logistic Regression, KNN), Decision Tree theory, with progression visible in notebook debugging attempts.
**Probable Period**: May 15–23, 2026.

---

### Logs

| File | Content |
|---|---|
| `logs/2026-02-20/app.log` | Angel One trading API error logs — "TooManyRequests" errors when fetching historical candle data (Feb 20, 2026) |

---

# Learning Progression Timeline

## Month-by-Month Summary

### January 2026 (Practicing Foundation)
- Python basics: pattern printing, simple scripts
- Raw data file creation (student_data.txt)

### February 2026 (Core Data Science Toolkit)
- **Week 1**: NumPy fundamentals — arrays, operations, vectorization
- **Week 2 (10–14)**: Pandas Series/DataFrame, Matplotlib plotting
- **Week 2–3 (12–18)**: Statistics — descriptive stats, probability distributions
- **Week 3 (18–20)**: Outlier detection, hypothesis testing, Z-scores
- **Week 4 (26–27)**: Sampling techniques, covariance, correlation, data cleaning

### March 2026 (Feature Engineering & SQL)
- **Week 1 (5–6)**: Feature engineering — creating features, encoding, scaling
- **Week 2–3 (6–17)**: Statistics assignments, confidence intervals
- **Week 3 (17–19)**: SQL basics → joins → keys → subqueries
- **Week 4–5 (25–30)**: SQL assignments, Python-MySQL integration, advanced Python (generators, lambda)

### April 2026 (Projects & Visualization Tools)
- **Early April (1–8)**: SQL assignments, Seaborn, consolidated stats project, machine test
- **Mid April (18)**: Mini project (inventory), Streamlit dashboard
- **Late April (28–29)**: **Power BI intensive** — 9+ dashboards in 2 days

### May 2026 (Advanced Visualization & ML)
- **Early May (6–8)**: Tableau workbooks
- **Mid May (15–19)**: ML — Linear Regression, Logistic Regression
- **Late May (20–23)**: KNN, Decision Tree theory (work in progress)

### Technology Transition Points
- **Python → NumPy**: Late Jan (natural progression)
- **NumPy → Pandas**: Early Feb (data manipulation focus)
- **Pandas → Matplotlib**: Mid Feb (visualization after data handling)
- **Matplotlib → Statistics**: Mid Feb (analytical foundation)
- **Statistics → Feature Engineering**: Early Mar (applied statistics)
- **Feature Engineering → SQL**: Mid Mar (database skills)
- **SQL → Projects**: Apr (consolidation)
- **Projects → Power BI → Tableau**: Late Apr – Early May (BI tools)
- **BI → ML**: Mid May (modeling)

---

# Suggested Realistic Git Commit History

Total: **79 commits** across 64 unique days over 5 months, including revision sessions, debugging, experimentation, and natural learning gaps.

## January 2026

### Jan 29 — Data file setup
```
Commit: creating sample data for practice
Files: student_data.txt
Notes: Raw data file — simple student records text file.
```

### Jan 31 — Pattern printing attempts
```
Commit: trying star pattern printing
Files: a.py, t.py
Notes: Diamond star pattern with hollow center. Multiple attempts visible.
```

## February 2026

### Feb 1 — NumPy notes and planning
```
Commit: reviewing numpy array basics
Files: 01_numpy_library/numpyy.py (initial draft)
Notes: Reading up on array creation, broadcasting, indexing.
```

### Feb 3 — NumPy vectorization experiment
```
Commit: testing numpy vs python list performance
Files: 01_numpy_library/timer.py
Notes: 1M element multiplication benchmark. NumPy ~30x faster.
```

### Feb 4 — Pandas DataFrame attributes
```
Commit: exploring dataframe attributes — shape, info, describe
Files: 02_pandas_library/5_DataFrame_arributes.py
Notes: Learning to inspect dataframes using built-in methods.
```

### Feb 5 — NumPy topic checklist
```
Commit: making numpy revision checklist
Files: 01_numpy_library/numpyy.py (final)
Notes: Notes file listing key NumPy concepts to cover systematically.
```

### Feb 6 — Pandas CRUD and file I/O
```
Commit: practicing dataframe crud operations
Files: 4_operations/2_curd_operations.py
Notes: Adding columns, updating values, conditional modifications, drop.
```
```
Commit: dataframe export to csv/excel/json/sqlite
Files: 02_pandas_library/unknown.py, 4_operations/a.py, 02_pandas_library/Student_data.csv, Student_data_excel.xlsx, Student_data_json.json, Students_Data.db
Notes: Converting dataframes to multiple formats. Reading them back successfully.
```

### Feb 7 — Missing data handling
```
Commit: filling and dropping missing values
Files: 4_operations/3_Missing_data_handling.py
Notes: ffill, bfill, constant fill, mean imputation. Noticed deprecation warning for method parameter.
```

### Feb 8 — NumPy advanced + SQLite
```
Commit: numpy broadcasting and boolean indexing
Files: 01_numpy_library/3_numpy array__.py
Notes: Aggregation with axis, boolean filtering, sorting, where clause, searchsorted.
```
```
Commit: setting up sqlite database
Files: 03_sqllite/1_sqlite_operation.py
Notes: Connection, cursor, CREATE TABLE. Learning about commit() importance.
```

### Feb 9 — DataFrame joins and grouping
```
Commit: learning groupby and merge on dataframes
Files: 5_SQL_type_operation_on_df/1_.py
Notes: Sort, groupby with agg/transform, merge (inner/right), join, concat. SQL-like operations on pandas.
```

### Feb 10 — Matplotlib multi-chart practice
```
Commit: trying different matplotlib plots
Files: 6_matplotlib/2_bar_plot.py, 3_pie_chart.py, 4_subplot.py, 5_histogram.py, 6_scatter_plot.py
Notes: Bar, pie, subplot, histogram, scatter in one session. Learning customization options.
```

### Feb 11 — Revisiting pandas indexing
```
Commit: reviewing loc and iloc indexing
Files: 02_pandas_library/3_operation_on_series.py (modified)
Notes: Reinforcement of label-based vs integer-based indexing concepts.
```

### Feb 12 — Descriptive statistics
```
Commit: variance, standard deviation, range
Files: 7_staticstics/2_variance_&_SD.py
Notes: Population vs sample variance. Coefficient of variation. Scipy dependency notes.
```

### Feb 13 — Probability distributions
```
Commit: exploring binomial distribution
Files: 7_staticstics/1_DiscriptiveStats.py, 3_Binomial_D.py
Notes: Descriptive stats with skewness/kurtosis. Binomial PMF using scipy. Manual comb formula too.
```

### Feb 14 — Line plot customization
```
Commit: line plot styling — markers, colors, grid
Files: 6_matplotlib/1_ploting_methods.py
Notes: Marker styles, line styles, figure sizing, grid customization.
```

### Feb 16 — Debugging mode function
```
Commit: fixing mode calculation for multi-modal data
Files: 7_staticstics/1_DiscriptiveStats.py (modified)
Notes: statistics.mode() only returns first mode. Implemented manual multi-mode detection.
```

### Feb 17 — Pandas series creation
```
Commit: creating pandas series — different methods
Files: 02_pandas_library/2_creating_series.py
Notes: Series from list, dict, scalar, numpy array. Custom indexing with loc/iloc.
```

### Feb 18 — Normal distribution and z-scores
```
Commit: z-scores and normal distribution curve
Files: 7_staticstics/5_normal_D_important.py
Notes: Z-score calculation, manual PDF formula, scipy norm.pdf, bell curve with axvline.
```

### Feb 19 — Outlier detection
```
Commit: outlier detection with z-score and iqr
Files: 8_Outlier detection_&_treatment.py/1_Statistical_mtds_for_outlier_dtctn.py
Notes: Z-score >3, IQR method, percentile capping, median imputation, log/sqrt transformation.
```

### Feb 20 — Hypothesis testing + API logs
```
Commit: t-test and confidence interval manually
Files: 8_Outlier detection_&_treatment.py/2_hypothesis testing.py
Notes: Manual t-statistics calculation, compared with scipy. CI via scipy.stats.t.interval().
```
```
Commit: debugging angel one api — toomanyrequests errors
Files: logs/2026-02-20/app.log
Notes: Rate limiting on historical data endpoint. Token 2885, FIVE_MINUTE interval.
```

### Feb 22 — Revision — outlier review
```
Commit: revision — reviewing outlier detection methods
Files: 8_Outlier detection_&_treatment.py/1_Statistical_mtds_for_outlier_dtctn.py (modified)
Notes: Reread code, added transformation section comments.
```

### Feb 23 — Pattern printing refresh
```
Commit: revising star patterns
Files: a.py, t.py (modified)
Notes: Diamond pattern with loop logic. Practiced after gap.
```

### Feb 26 — Sampling techniques
```
Commit: learning sampling methods
Files: 9_sampling_techniques.py/1_Sampling_techniques.py
Notes: Cluster, convenience, snowball, random, systematic, stratified sampling implementations.
```

### Feb 27 — Correlation and data cleaning
```
Commit: manual covariance and correlation formulas
Files: 9_sampling_techniques.py/2_covariance.py, 3_correlation.py
Notes: Implemented formulas from scratch, verified against numpy functions.
```
```
Commit: end-to-end data cleaning pipeline
Files: 10_Data_cleaning_preparion/1_handling_missing_data.py
Notes: Title casing, mean/mode imputation, drop_duplicates, date parsing with coerce, salary capping.
```

### Feb 28 — Experimenting with imputation
```
Commit: trying different imputation strategies
Files: 10_Data_cleaning_preparion/1_handling_missing_data.py (modified)
Notes: Experimenting with median vs mean for salary column.
```

## March 2026

### Mar 2 — Researching encoding techniques
```
Commit: reading about categorical encoding methods
Files: 12_feature_engineering/2_encoding_techinques.py (initial draft)
Notes: Label, one-hot, ordinal encoding notes. Planning feature engineering practice.
```

### Mar 5 — Numerical features and encoding
```
Commit: feature engineering — numerical features
Files: 12_feature_engineering/1_features.py
Notes: Price per sq ft, age of flat, area per bedroom. Binning with pd.cut, text features.
```
```
Commit: implementing encoding techniques
Files: 12_feature_engineering/2_encoding_techinques.py
Notes: Label, one-hot, ordinal, frequency encoding on sample dataset.
```

### Mar 6 — Feature scaling + stats assignments
```
Commit: min-max normalization and standardization
Files: 12_feature_engineering/3_feature_scaling.py
Notes: Manual implementation. Practice dataset with marks, study hours, attendance.
```
```
Commit: statistics and outlier detection assignments
Files: 0_assigments/1_discriptive_stats_assignmetn.py, 2_outlier_dection_assignment.py, 7_staticstics/4_Possion_D.py
Notes: Sales data stats. 6 outlier detection problems. Poisson distribution practice.
```

### Mar 8 — Weekend revision — stats recap
```
Commit: revising statistics and probability concepts
Files: 7_staticstics/3_Binomial_D.py (modified), 4_Possion_D.py (modified)
Notes: Revisited binomial and poisson distributions. Added plot labels.
```

### Mar 12 — SQL join preparation
```
Commit: reading about sql joins — notes
Files: 13_sql/joints.md
Notes: Inner, left, right, full, self join definitions. Set theory analogy.
```

### Mar 17 — SQL clauses + CI assignment
```
Commit: sql where, group by, having, order by
Files: 13_sql/1_clauses.sql
Notes: Full clause composition. Foreign key constraint, describe, aggregate functions.
```
```
Commit: confidence interval calculation
Files: 0_assigments/3_CI.py
Notes: 95% CI using scipy. Covariance and correlation interpretation.
```

### Mar 18 — SQL joins practice
```
Commit: sql joins — inner, left, right
Files: 13_sql/2_joins.sql, 13_sql/3_keys.sql
Notes: Join queries with foreign key relationships.
```

### Mar 19 — SQL subqueries
```
Commit: practicing subqueries — single, multi-level, correlated
Files: 13_sql/keys.sql
Notes: Three subquery types with employee/department schema.
```

### Mar 22 — Fixing foreign key constraint
```
Commit: fixing sql foreign key reference
Files: 13_sql/1_clauses.sql (modified)
Notes: Corrected fk_department constraint to reference dept_id properly.
```

### Mar 25 — Feature engineering assignment
```
Commit: feature engineering assignment — 2 datasets
Files: 0_assigments/4_feature_engineering.py
Notes: Missing value imputation, price_per_sqft, binning, city encoding, luxury keyword detection. Employee dataset with salary, experience, department features.
```

### Mar 26 — Reviewing assignment
```
Commit: checking feature engineering output
Files: 0_assigments/4_feature_engineering.py (modified)
Notes: Verified binning boundaries and encoding mappings. Small fixes.
```

### Mar 28 — Generators and lambda
```
Commit: practicing python generators
Files: 0_assigments/5_generator.py
Notes: Number gen, even gen, fibonacci, generator expression, char gen.
```
```
Commit: lambda functions — map, filter, reduce
Files: 0_assigments/7_lambda function.py
Notes: Map cubes, filter primes, reduce product. Discount, GST, username cleaning lambdas.
```

### Mar 29 — SQL assignment
```
Commit: sql assignment — online store database
Files: 13_sql/sql_assignment.sql
Notes: 4-table schema (customers, products, orders, orderitems). 15 queries from basic to advanced.
```

### Mar 30 — Python-MySQL CRUD
```
Commit: python mysql crud application
Files: 13_sql/sqlIntegration.py
Notes: Menu-driven add/view/update/delete using mysql.connector. Parameterized queries.

## April 2026

### Apr 1 — SQL assignment 2
```
Commit: second sql assignment — similar query patterns
Files: 13_sql/sql assignment1.sql
Notes: Same schema structure, different data values. Reinforcing join and subquery syntax.
```

### Apr 2 — Seaborn visualization
```
Commit: exploring seaborn with tips dataset
Files: 15_seaborn/1_plots_using_sns.py
Notes: Barplot, countplot, scatter, histogram+kde, boxplot, heatmap, pairplot, violinplot, regplot. Flights dataset lineplot+heatmap too.
```

### Apr 3 — Starting Excel practice
```
Commit: starting excel practice
Files: 16_excel/1_.md, 1_sheet.xlsx
Notes: Placeholder files for Excel data work.
```

### Apr 5 — Experimenting with seaborn styles
```
Commit: trying seaborn theme and style options
Files: 15_seaborn/1_plots_using_sns.py (modified)
Notes: Testing different seaborn styles and color palettes.
```

### Apr 7 — Excel data files
```
Commit: excel data practice workbooks
Files: 16_excel/Book1.xlsx, Book3.xlsx
Notes: Excel workbooks for data manipulation practice.
```

### Apr 8 — NumPy revision + consolidated project
```
Commit: revising numpy lectures
Files: 01_numpy_library/1_NumpyLecture.py, 2_NumpyLecture2.py, test1.py
Notes: Major revision — reorganized random module examples. Array attributes, reshaping, stacking, splitting.
```
```
Commit: building consolidated statistics project
Files: 11_project/1_mixStats.py
Notes: Synthetic data generation, descriptive stats, probability, distributions, outlier detection, stratified sampling, CI, correlation. All topics combined.
```
```
Commit: machine test — mixed topics
Files: machine test.py
Notes: Cubes list, random sampling, category encoding, z-scores, array reshape, sql query, chatbot.
```

### Apr 10 — Debugging mixstats project
```
Commit: fixing mixstats output formatting
Files: 11_project/1_mixStats.py (modified)
Notes: Cleaned up print statements. Fixed shapiro test output alignment.
```

### Apr 15 — Researching streamlit
```
Commit: looking into streamlit dashboard components
Files: dashboard.py (initial draft)
Notes: Researching layout options, placeholders, caching for live data.
```

### Apr 18 — Mini project + Streamlit dashboard
```
Commit: inventory management mini project
Files: 17_mini_project/project9.py
Notes: Stock tracking, category profit, expiry risk detection, purchase planning.
```
```
Commit: streamlit trading dashboard
Files: dashboard.py
Notes: Watchlist table with conditional formatting, candlestick chart, alerts panel, auto-refresh.
```

### Apr 22 — Power BI research
```
Commit: exploring power bi templates and themes
Files: 18_power_BI/temp_pbix/
Notes: Investigating pbix structure and theme customization options.
```

### Apr 25 — DAX formula practice
```
Commit: practicing dax measures
Files: 18_power_BI/DAX Measures.pbix (initial)
Notes: Basic DAX measures — sum, average, calculate, filter context.
```

### Apr 28 — Power BI calculated columns
```
Commit: power bi calculated columns practice
Files: 18_power_BI/Calculated Colums.pbix, temp_pbix/
Notes: Creating calculated columns using DAX expressions.
```

### Apr 29 — Power BI dashboards (intensive session)
```
Commit: data preparation for visualizations
Files: 18_power_BI/DATA FOR VISUAL1.pbix
Notes: Structuring data for Power BI charts.
```
```
Commit: dashboard demo and sales dashboard
Files: 18_power_BI/Dashboard Demo.pbix, Sales Dashboard.pbix
Notes: Building main dashboards with multiple visual elements.
```
```
Commit: liquid glass theme customization
Files: 18_power_BI/liquid_glass_pro.json, liquid_glass_theme.json
Notes: Custom JSON themes for professional styling.
```
```
Commit: ecommerce project in power bi
Files: 18_power_BI/madhav_Ecommerce_project.pbix
Notes: E-commerce sales analysis dashboard.
```
```
Commit: slicer and chart type exploration
Files: 18_power_BI/Slicer tlt.pbix, Tlt Charts.pbix, tlt_powerbi.pbix
Notes: Testing slicer functionality and different chart visualizations.

## May 2026

### May 3 — Excel data review
```
Commit: reviewing excel data structure
Files: 16_excel/Book1.xlsx, Book3.xlsx (modified)
Notes: Checking data layout before moving to tableau.
```

### May 6 — Tableau start
```
Commit: first tableau workbook
Files: 19_tableu/Book1.twb
Notes: Introduction to Tableau interface and basic visualizations.
```

### May 7 — Tableau workbook 2
```
Commit: more tableau practice
Files: 19_tableu/Book2.twb
Notes: Increasing complexity — multiple sheets and dashboard elements.
```

### May 8 — Tableau workbook 3
```
Commit: advanced tableau workbook
Files: 19_tableu/Book3.twb
Notes: Continued Tableau practice with larger workbook.
```

### May 12 — Reading about linear regression
```
Commit: researching linear regression assumptions
Files: 20_ml/1_ex.md (deleted)
Notes: Reading about OLS assumptions, gradient descent basics.
```

### May 15 — Linear Regression implementation
```
Commit: linear regression — study hours vs marks
Files: 20_ml/1_linear_regression.py
Notes: First ML model. Sklearn LinearRegression. Prediction for custom input.
```

### May 18 — Debugging logistic regression
```
Commit: debugging logistic regression model
Files: 20_ml/2_Logistic_Regression.py (initial draft)
Notes: Fixed train_test_split random_state. Verified binary classification output.
```

### May 19 — Logistic Regression final
```
Commit: logistic regression — pass/fail classification
Files: 20_ml/2_Logistic_Regression.py, 2_Logistic_Regression.ipynb
Notes: Working binary classification with train/test split. Notebook version created.
```

### May 20 — ML algorithms comparison notes
```
Commit: reviewing differences between regression and classification
Files: 20_ml/3_ex.md (initial draft)
Notes: Understanding when to use linear vs logistic regression. Decision tree intro.
```

### May 21 — KNN algorithm implementation
```
Commit: knn with manual distance calculation
Files: 20_ml/3_KNN_algorithm.ipynb
Notes: Euclidean distance manual calculation. Tried sklearn KNN with euclidean/manhattan/minkowski metrics — hit NameError, learning in progress.
```
```
Commit: decision tree gini index notes
Files: 20_ml/3_ex.md
Notes: Step-by-step Gini calculation walkthrough. Tree visualization for credit/employed split.
```

### May 22 — Researching decision tree parameters
```
Commit: researching decision tree hyperparameters
Files: 20_ml/4_Decision_Tree.ipynb (initial)
Notes: Reading about max_depth, min_samples_split, pruning.
```

### May 23 — Decision Tree start
```
Commit: starting decision tree notebook
Files: 20_ml/4_Decision_Tree.ipynb, prompt.md
Notes: Empty notebook — work just beginning. Created project analysis prompt for portfolio review.
```

---

# Important Practice Modules

## 1. NumPy Mastery (`01_numpy_library/`)
Systematic coverage from array creation to advanced operations (broadcasting, boolean indexing, vectorization). Includes performance comparison with Python lists.

## 2. Pandas Data Manipulation (`02_pandas_library/`, `4_operations/`, `5_SQL_type_operation_on_df/`)
Complete pandas workflow: Series/DataFrame creation → CRUD → missing data → groupby/merge → file I/O (CSV, Excel, JSON, SQLite).

## 3. Statistics Pipeline (`7_staticstics/`, `8_Outlier detection_&_treatment.py/`, `9_sampling_techniques.py/`)
Full statistics journey: descriptive stats → probability distributions → outlier detection → hypothesis testing → sampling → correlation.

## 4. Feature Engineering (`12_feature_engineering/`, `10_Data_cleaning_preparion/`)
Numerical features, binning, encoding techniques, feature scaling, and data cleaning pipeline.

## 5. SQL Proficiency (`13_sql/`)
From basic clauses to complex multi-table queries, subqueries, and Python-MySQL CRUD integration.

## 6. Consolidated Project (`11_project/1_mixStats.py`)
Capstone project combining data generation, descriptive statistics, probability distributions, outlier detection, sampling, confidence intervals, and correlation analysis.

## 7. Power BI Dashboards (`18_power_BI/`)
Intensive dashboard creation covering calculated columns, DAX measures, custom themes, and various visualization types.

## 8. ML Algorithms (`20_ml/`)
Linear Regression, Logistic Regression, K-Nearest Neighbors, and Decision Tree theory — demonstrating the transition from statistics to machine learning.

---

# Resume-Friendly Internship Summary

> **Data Science Intern** | Jan 2026 – Present
>
> Completed intensive hands-on training in the data science toolkit, building proficiency across the full data pipeline:
>
> - **Data Manipulation**: NumPy, Pandas — data cleaning, transformation, aggregation, and file I/O across multiple formats
> - **Statistical Analysis**: Descriptive/inferential statistics, probability distributions, hypothesis testing, correlation analysis
> - **Data Visualization**: Matplotlib, Seaborn, Power BI (dashboards, DAX, custom themes), Tableau
> - **Feature Engineering**: Numerical feature creation, categorical encoding (label, one-hot, ordinal, frequency), feature scaling (normalization, standardization)
> - **Databases**: SQL (joins, subqueries, aggregation, keys), SQLite integration, Python-MySQL CRUD application development
> - **Machine Learning**: Linear Regression, Logistic Regression, KNN classification, Decision Tree fundamentals
> - **Tools & Projects**: Built a consolidated statistics analysis project, inventory management system, Streamlit trading dashboard, and multiple Power BI/Tableau dashboards
>
> Demonstrated consistent learning progression from foundational Python through advanced ML algorithms, with natural emphasis on practice, revision, and experimentation.
