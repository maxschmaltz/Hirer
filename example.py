import json

from prepare import get_model
from hiring_plan import hiring_plan


def main():

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

    example_path = './example.json'

    with open(example_path, 'w') as f: json.dump(plan, f, indent=4)


if __name__ == '__main__':
    main()