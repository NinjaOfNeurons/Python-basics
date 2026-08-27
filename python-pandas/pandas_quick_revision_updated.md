# Pandas — Quick Revision Notes

## 1. Import
```python
import pandas as pd
```

## 2. Series vs DataFrame
```python
s = pd.Series([10, 20, 30])

df = pd.DataFrame({
    "name": ["Karan", "Sam"],
    "age": [28, 25]
})
```
- Series → one column
- DataFrame → complete table

## 3. Read / Inspect
```python
df = pd.read_csv("file.csv")
df.head()
df.tail()
df.shape
df.columns
df.info()
df.describe()
```

## 4. Select Columns
```python
df["name"]                 # Series
df[["name", "age"]]        # DataFrame
```

## 5. Select Rows
```python
df.loc[0]                  # label
df.loc[df["age"] > 25]     # condition

df.iloc[0]                 # position
df.iloc[0:3]
```
**Remember:** `loc` → labels/conditions, `iloc` → positions.

## 6. Filtering
```python
df[df["age"] > 25]

df[(df["age"] > 25) & (df["city"] == "Delhi")]

df[(df["city"] == "Delhi") | (df["city"] == "Mumbai")]

df[df["city"] != "Delhi"]
```
Use `&` for AND, `|` for OR, `~` for NOT. Put each condition in parentheses.

## 7. isin()
```python
df[df["city"].isin(["Delhi", "Mumbai"])]
```

## 8. Sorting
```python
df.sort_values("age")
df.sort_values("age", ascending=False)

df.sort_values(
    ["city", "age"],
    ascending=[True, False]
)
```

## 9. Add / Transform Columns
```python
df["double_age"] = df["age"] * 2
df["adult"] = df["age"] >= 18
```

Conditional:
```python
import numpy as np

df["status"] = np.where(
    df["age"] >= 18,
    "Adult",
    "Minor"
)
```

## 10. Rename / Drop
```python
df.rename(columns={"age": "patient_age"})

df.drop(columns=["age", "city"])
```

## 11. Missing Values
```python
df.isna()
df.isna().sum()

df.dropna()

df["age"].fillna(0)
df["age"].fillna(df["age"].mean())
```

Mental model:
```text
isna()  → find missing
dropna() → remove missing
fillna() → replace missing
```

## 12. Duplicates
```python
df.duplicated()
df.duplicated().sum()
df.drop_duplicates()
df.drop_duplicates(subset=["first_name", "last_name"])
```

## 13. Unique / Counts
```python
df["city"].unique()
df["city"].nunique()
df["gender"].value_counts()
```

## 14. GroupBy
```python
df.groupby("city")["salary"].mean()

df.groupby("city")["salary"].agg(
    ["count", "mean", "min", "max"]
)

df.groupby("city").agg(
    average_salary=("salary", "mean"),
    employee_count=("salary", "count")
)
```

Think:
```text
groupby column
      ↓
groups
      ↓
aggregate each group
```

## 15. Aggregation
```python
df["salary"].sum()
df["salary"].mean()
df["salary"].median()
df["salary"].min()
df["salary"].max()
df["salary"].count()
```

## 16. apply()
```python
def classify(age):
    if age >= 18:
        return "Adult"
    return "Minor"

df["status"] = df["age"].apply(classify)

df["double_age"] = df["age"].apply(lambda x: x * 2)
```

Prefer vectorized operations when possible.

## 17. String Operations
```python
df["name"].str.lower()
df["name"].str.upper()
df["name"].str.strip()
df["name"].str.len()

df[df["name"].str.contains("kar", case=False, na=False)]
df[df["name"].str.startswith("K", na=False)]
```

## 18. Dates
```python
df["date"] = pd.to_datetime(df["date"])

df["date"].dt.year
df["date"].dt.month
df["date"].dt.day
df["date"].dt.day_name()
```

## 19. Merge / Join
SQL JOIN:
```sql
SELECT *
FROM patients p
JOIN admissions a
ON p.patient_id = a.patient_id;
```

Pandas:
```python
df = patients.merge(
    admissions,
    on="patient_id",
    how="inner"
)
```

Common:
```python
how="inner"
how="left"
how="right"
how="outer"
```

Different column names:
```python
df1.merge(
    df2,
    left_on="patient_id",
    right_on="id",
    how="left"
)
```

## 20. concat()
Rows:
```python
pd.concat([df1, df2])
```

Columns:
```python
pd.concat([df1, df2], axis=1)
```

- `axis=0` → rows
- `axis=1` → columns

## 21. Index
```python
df.reset_index(drop=True)
```

Useful after filtering/sorting.

## 22. SQL → Pandas
| SQL | Pandas |
|---|---|
| SELECT | `df[...]` |
| WHERE | `df[condition]` |
| GROUP BY | `groupby()` |
| HAVING | filter after aggregation / `groupby().filter()` |
| ORDER BY | `sort_values()` |
| JOIN | `merge()` |
| UNION | `pd.concat()` |
| DISTINCT | `unique()` / `drop_duplicates()` |
| COUNT | `count()` / `size()` |
| SUM | `sum()` |
| AVG | `mean()` |
| MAX | `max()` |
| MIN | `min()` |

## 23. Common Mistakes

### Don't use Python `and` / `or`
Wrong:
```python
df[(df["age"] > 20) and (df["age"] < 30)]
```

Correct:
```python
df[(df["age"] > 20) & (df["age"] < 30)]
```

### Multiple columns need double brackets
```python
df[["name", "age"]]
```

### loc vs iloc
```text
loc  → labels / conditions
iloc → integer positions
```

## 24. LeetCode Pandas Mental Checklist
Before solving:
```text
1. What columns do I need?
2. Which rows should stay?
3. Do I need a new column?
4. Do I need grouping?
5. Do I need a join?
6. Do I need sorting?
7. What exact columns should I return?
```

Typical pipeline:
```text
SELECT → FILTER → TRANSFORM → GROUP → SORT → RETURN
```

## 25. Mini Cheat Sheet
```python
# Filter
df[df["age"] > 25]

# Select
df[["name", "age"]]

# Sort
df.sort_values("age", ascending=False)

# Group
df.groupby("city")["salary"].mean()

# Aggregate
df.groupby("city")["salary"].agg(["count", "mean", "max"])

# Join
df1.merge(df2, on="id", how="left")

# Missing
df.isna().sum()
df.dropna()
df.fillna(0)

# Duplicates
df.drop_duplicates()

# Unique / counts
df["city"].unique()
df["city"].nunique()
df["city"].value_counts()

# Apply
df["x"] = df["age"].apply(lambda x: x * 2)

# Dates
df["date"] = pd.to_datetime(df["date"])
df["date"].dt.year

# Strings
df["name"].str.lower()
df["name"].str.contains("abc")
```

## 26. What to Prioritize for 30 Days of Pandas
### Must know
- DataFrame creation
- Selecting columns
- Filtering
- `loc` / `iloc`
- Sorting
- `isin`
- `value_counts`
- `unique`

### Very important
- `groupby`
- `agg`
- `apply`
- `merge`
- `concat`
- Missing values
- Duplicates

### Next
- Datetime
- String operations
- Conditional columns
- Index manipulation

## 27. Patterns We Learned — LeetCode Practice

### Boolean mask → filtered DataFrame

A condition by itself returns a Boolean Series:

```python
df["age"] > 25
```

Use it inside `df[...]` to filter rows:

```python
df[df["age"] > 25]
```

Mental model:

```text
condition
   ↓
True / False for every row
   ↓
df[condition]
   ↓
filtered DataFrame
```

Multiple conditions:

```python
df[
    (df["age"] > 25) &
    (df["city"].isin(["Delhi", "Mumbai"]))
]
```

Use `&`, `|`, `~` instead of Python `and`, `or`, `not`.

---

### Series vs DataFrame — one vs two brackets

```python
df["salary"]             # Series
df[["salary"]]           # DataFrame
df[["name", "salary"]]  # DataFrame
```

Mental rule:

```text
["column"]          → one Series
[["column"]]        → one-column DataFrame
[["a", "b"]]       → multi-column DataFrame
```

---

### `unique()` vs `drop_duplicates()`

```python
df["city"].unique()
```

Returns unique **values** from a Series.

```python
df.drop_duplicates(subset=["email"])
```

Returns unique **rows** of a DataFrame based on selected columns.

Mental model:

```text
unique()           → "What different values exist?"
drop_duplicates()  → "Which rows should I keep?"
```

---

### `value_counts()`

Use when you want the frequency of each unique value:

```python
df["city"].value_counts()
```

---

### String filtering

```python
df["name"].str.lower()
df["name"].str.upper()
df["name"].str.strip()
df["name"].str.len()
df["name"].str.contains("DIAB1")
df["name"].str.startswith("A")
df["name"].str.endswith(".com")
```

A string condition can be used as a Boolean mask:

```python
df[df["mail"].str.match(pattern)]
```

`str.match()` returns a Boolean Series; `df[...]` uses it to filter rows.

---

### `str.contains()` vs complete condition codes

Simple:

```python
df["conditions"].str.contains("DIAB1")
```

checks whether those characters occur anywhere, so it can incorrectly match:

```text
SADIAB100
```

If `DIAB1` must be a separate condition, regex can express boundaries:

```python
r"(^| )DIAB1[0-9]*( |$)"
```

A non-regex approach is:

```python
df["conditions"].str.split()
```

then check individual conditions with `startswith()` and `any()`.

Mental model:

```text
"ACNE DIAB100"
       ↓
["ACNE", "DIAB100"]
       ↓
check each condition
       ↓
does any start with "DIAB1"?
```

---

### `merge()` + rename

```python
merged = employee.merge(
    department,
    left_on="departmentId",
    right_on="id",
    how="left"
)
```

If both tables contain `name`, Pandas may create:

```text
name_x
name_y
```

Rename after merging:

```python
merged = merged.rename(columns={
    "name_x": "Employee",
    "name_y": "Department"
})
```

`merge()` itself does not have a general rename argument.

---

### Group maximum while preserving rows — `transform()`

If you need the highest salary for each department while keeping employee rows:

```python
df["max_salary"] = (
    df.groupby("Department")["Salary"]
      .transform("max")
)
```

Then:

```python
df[df["Salary"] == df["max_salary"]]
```

Mental distinction:

```text
groupby().max()
    → one result per group

groupby().transform("max")
    → maximum repeated onto every original row
```

---

### Nth highest salary

Pattern:

```python
salaries = (
    employee["salary"]
    .drop_duplicates()
    .sort_values(ascending=False)
)
```

Then:

```python
nth_salary = salaries.iloc[N - 1]
```

Because:

```text
N = 1 → iloc[0]
N = 2 → iloc[1]
N = 3 → iloc[2]
```

Edge case:

```python
if N <= 0 or len(salaries) < N:
    ...
```

Negative `.iloc` indexing is valid Python:

```text
iloc[-1] → last element
iloc[-2] → second-last element
```

So validate `N` before using `iloc[N - 1]`.

---

### Second highest salary

```python
salaries = (
    employee["salary"]
    .drop_duplicates()
    .sort_values(ascending=False)
)

if len(salaries) < 2:
    second_highest = None
else:
    second_highest = salaries.iloc[1]
```

`drop_duplicates()` comes first because the second highest means the second **distinct** salary.

---

### Ranking — `dense`

When ties get the same rank and there are no gaps:

```python
df["rank"] = (
    df["score"]
    .rank(method="dense", ascending=False)
    .astype(int)
)
```

Example:

```text
Score   Rank
100     1
90      2
90      2
80      3
```

Use `method="dense"` when the problem says there should be no holes between ranks.

---

### `round()` vs `astype(int)`

```python
series.round(0)
```

rounds values but normally keeps them as floats:

```text
1.0 → 1.0
```

Whereas:

```python
series.astype(int)
```

converts:

```text
1.0 → 1
```

Use `round()` for numeric precision; use `astype(int)` when the output must be integer-valued.

---

### Delete duplicates while keeping the smallest ID

Requirement:

> Delete duplicate emails and keep the row with the smallest `id`.

Pattern:

```python
person.sort_values("id", inplace=True)

person.drop_duplicates(
    subset=["email"],
    keep="first",
    inplace=True
)
```

Mental model:

```text
sort by id ascending
        ↓
smallest id comes first
        ↓
drop duplicate emails
        ↓
keep first
```

For this type of LeetCode problem, the function may require:

```python
-> None
```

because the DataFrame must be modified **in-place**.

---

### `inplace=True`

Without `inplace`:

```python
new_df = df.drop_duplicates()
```

the original `df` remains unchanged.

With:

```python
df.drop_duplicates(inplace=True)
```

the original DataFrame is modified.

---

## 28. Problem-Solving Patterns

### Filter rows

```python
df[condition]
```

### Select columns after filtering

```python
df[condition][["name", "salary"]]
```

### Sort then take top N

```python
df.sort_values("salary", ascending=False).head(N)
```

### Unique values then rank

```python
df["salary"].drop_duplicates().sort_values(ascending=False)
```

### Group → aggregate

```python
df.groupby("department")["salary"].mean()
```

### Group → calculate per-row group statistic

```python
df["group_max"] = (
    df.groupby("department")["salary"].transform("max")
)
```

### Merge → filter

```python
merged = left.merge(right, ...)
merged[condition]
```

### Sort → drop duplicates

Useful when a specific row should survive:

```python
df.sort_values("id").drop_duplicates(
    subset=["email"],
    keep="first"
)
```

---

## 29. How to Decide Which Pandas Method to Use

```text
"Which different values?"
        ↓
unique()

"How many times does each value occur?"
        ↓
value_counts()

"Which duplicate rows should I remove?"
        ↓
drop_duplicates()

"Sort the rows"
        ↓
sort_values()

"Find one scalar statistic"
        ↓
mean(), max(), min(), sum(), count()

"Calculate separately for each group"
        ↓
groupby()

"Keep original rows but attach a group statistic"
        ↓
groupby().transform()

"Apply custom Python logic"
        ↓
apply()

"Join information from another table"
        ↓
merge()
```

---

## 30. LeetCode Output Checklist

Before submitting:

```text
1. Correct rows?
2. Correct columns?
3. Series or DataFrame as required?
4. Exact column names?
5. Correct row order?
6. Duplicates handled?
7. Missing/edge cases handled?
8. In-place modification required?
9. Any accidental negative iloc indexing?
10. Exact expected output schema?
```

Golden rule:

> Don't just ask "Did I get the right value?"
>
> Also ask "Did I get the right shape, column names, rows, and order?"
