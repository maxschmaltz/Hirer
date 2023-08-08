# Hirer: A simple hiring plan creator with GPT-3.

This repo contains a solution to a test task for an NLP Engineer position. The coding took about 1 h 15 min including testing, setting up the repo and writing the README. An update took about 20 min more afterwards.

---

### Table of Contents
* [Quick Start](#quick-start)
* [Input Parameters](#input-parameters)
* [Returns](#returns)
* [Example](#example)

---

## Quick Start

```python
from prepare import get_model
from hiring_plan import hiring_plan

params_path = '<path_to_your_params>'
llm = get_model(params_path)

desc = '<Your description>'
response = hiring_plan(llm, desc)
print(response)
```


## Input Parameters:

llm : `langchain.llms.base.BaseLLM`
<ul>
the LLM to generate the hiring plan with
</ul>

<br>

desc : `str`
<ul>
the description of the hiring plan you want to get
</ul>


## Returns:

hiring_plan : `dict`
<ul>
hiring plan; consists of the following fields:

<br>

`"positions"` : `list[dict]`
    <ul>
    list of positions encoded in `dict` each; each position includes title (field `"name"`), yearly salary (`"salary"`) and bonus (`"bonus"`)
    </ul>

<br>

`"total_annual_salary"` : `int`
    <ul>
    summed annual salary for all proposed positions
    </ul>

<br>

`"total_annual_bonus"` : `int`
    <ul>
    summed annual bonus for all proposed positions
    </ul>

<br>

`"total_annual_cost"` : `int`
    <ul>
    summed annual salary + bonus for all proposed positions
    </ul>
</ul>


## Example:

This example is available in [example.py](./example.py)

```python
from prepare import get_model
from hiring_plan import hiring_plan

params_path = './params.json'
llm = get_model(params_path)

# The description is generated with ChatGPT
desc = '''
    I need a hiring plan for a following team:
    
    1. Innovation Catalyst: Sparks creative ideas and guides exploration of new opportunities.
    2. Execution Maestro: Plans, coordinates, and ensures smooth project implementation.
    3. Analytics Guru: Analyzes data to provide actionable insights for decision-making.
    4. Relationship Orchestrator: Builds and maintains strong relationships with stakeholders.
'''
plan = hiring_plan(llm, desc)
print(plan)
```

Output (manually prettied):

```json
{
    "positions": [
        {
            "name": "Innovation Catalyst",
            "salary": 70000,
            "bonus": 5000
        },
        {
            "name": "Execution Maestro",
            "salary": 720000,
            "bonus": 180000
        },
        {
            "name": "Analytics Guru",
            "salary": 80000,
            "bonus": 10000
        },
        {
            "name": "Relationship Orchestrator",
            "salary": 80000,
            "bonus": 10000
        }
    ],
    "total_annual_salary": 950000,
    "total_annual_bonus": 205000,
    "total_annual_cost": 1155000
}
```
