from employee import employee


def process_desc(llm, desc):
    template = f'''
        Retrieve all the job positions from the following desc: {desc}.
        Return the positions as semicolon-separated titles with no additional tokens.
        Use no delimiters for the numbers.
    '''
    response = llm(template)
    return response.split(';') # is supposed to be semicolon-separated


def hiring_plan(llm, desc):

    employee_descs = process_desc(llm, desc)
    positions = [
        employee(llm, desc)
        for desc in employee_descs
    ]

    total_salary, total_bonus = 0, 0
    for position in positions:
        try: # in case of incorrect response format
            total_salary += position['salary']
            total_bonus += position['bonus']
        except: continue


    return {
        'positions': positions,
        'total_annual_salary': total_salary,
        'total_annual_bonus': total_bonus,
        'total_annual_cost': total_salary + total_bonus
    }