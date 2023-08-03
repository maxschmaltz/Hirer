# Hirer: A simple hiring plan creator with GPT.


### Input params:

desc : `str` : the description of the hiring plan you want to get

## Returns:

hiring_plan : `dict` : hiring plan; consists of the following fields:
1. `positions`: `list[dict]` of positions; each position includes title (field `name`), yearly salary (`salary`) and bonus (`bonus`);
2. `total_annual_salary`: summed annual salary for all proposed positions;
3. `total_annual_bonus`: summed annual bonus for all proposed positions;
4. `total_annual_cost`" summed annual salary + bonus for all proposed positions.

## Example:

```python
from langchain import OpenAI
from hiring_plan import hiring_plan

llm = OpenAI({
    model='text-davinci-003',
    temperature=0.35,
    max_tokens=128
})

desc = '''
  Team 1:

      - CEO: Joe Smith
      - CFO: Sarah Johnson
      - Marketing Manager: Tom Brown
      - HR Manager: Lisa Jones
      - IT Manager: Mike Williams
      - Sales Manager: Jane Taylor
      - Operations Manager: David White
      - Accounting Manager: Karen Anderson
'''

plan = hiring_plan(llm, desc)
print(plan)
```

Output:

```json
{
    "positions": [
        {
            "name": "Chief Executive Officer",
            "salary": "200000",
            "bonus": "100000"
        },
        {
            "name": "Manager",
            "salary": "100000",
            "bonus": "10000"
        },
        {
            "name": "Manager",
            "salary": "100000",
            "bonus": "10000"
        },
        {
            "name": "Chief Financial Officer",
            "salary": "150000",
            "bonus": "30000"
        },
        {
            "name": "Senior Manager",
            "salary": "90000",
            "bonus": "18000"
        },
        {
            "name": "Employee",
            "salary": "720000",
            "bonus": "160000"
        },
        {
            "name": "Marketing Manager",
            "salary": "70000",
            "bonus": "10000"
        },
        {
            "name": "Manager",
            "salary": "80000",
            "bonus": "8000"
        },
        {
            "name": "Sales Representative",
            "salary": "84000",
            "bonus": "2100"
        },
        {
            "name": "HR Manager",
            "salary": "80000",
            "bonus": "10000"
        },
        {
            "name": "Senior Software Engineer",
            "salary": "70000",
            "bonus": "3500"
        },
        {
            "name": "Software Engineer",
            "salary": "72000",
            "bonus": "6000"
        },
        {
            "name": "IT Manager",
            "salary": "70000",
            "bonus": "5000"
        },
        {
            "name": "Employee",
            "salary": "60000",
            "bonus": "6000"
        },
        {
            "name": "Employee",
            "salary": "50000",
            "bonus": "2500"
        },
        {
            "name": "Sales Manager",
            "salary": "70000",
            "bonus": "5000"
        },
        {
            "name": "Employee",
            "salary": "5000000",
            "bonus": "250000"
        },
        {
            "name": "Software Engineer",
            "salary": "48000",
            "bonus": "4000"
        },
        {
            "name": "Operations Manager",
            "salary": "80000",
            "bonus": "10000"
        },
        {
            "name": "Employee",
            "salary": "40000",
            "bonus": "0"
        },
        {
            "name": "Sales Representative",
            "salary": "36000",
            "bonus": "3000"
        },
        {
            "name": "Accounting Manager",
            "salary": "70000",
            "bonus": "10000"
        },
        {
            "name": "Software Engineer",
            "salary": "30000",
            "bonus": "3000"
        },
        {
            "name": "Sales Representative",
            "salary": "20000",
            "bonus": "2000"
        }
    ],
    "total_annual_salary": 7390000,
    "total_annual_bonus": 668100,
    "total_annual_cost": 8058100
}
```
