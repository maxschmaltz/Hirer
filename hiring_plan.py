from employee import employee


def process_desc(llm, desc):
    template = f'''
        Retrieve all the job positions from the following desc: {desc}.
        Return the positions as semicolon-separated values: the title, the salary in cash equivalent and the bonus in cash equivalent.
        Use no delimiters for the numbers.
    '''
    response = llm(template)
    return response.split(';') # is supposed to be semicolon-separated


def hiring_plan(llm, desc):

    emplyee_descs = process_desc(llm, desc)
    positions = [
        employee(llm, desc)
        for desc in emplyee_descs
    ]

    total_salary, total_bonus = 0, 0
    for position in positions:
        try: # in case of incorrect response format
            total_salary += int(position['salary'])
            total_bonus += int(position['bonus'])
        except: continue


    return {
        'positions': positions,
        'total_annual_salary': total_salary,
        'total_annual_bonus': total_bonus,
        'total_annual_cost': total_salary + total_bonus
    }