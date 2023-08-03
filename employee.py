def employee(llm, desc):
    template = f'''
        I need to hire an employee for the following position: {desc}.
        Please name their position title and calculate the yearly salary and the yearly bonus for them.
        Return exactly 3 semicolon-separated values: the title, the salary in cash equivalent and the bonus in cash equivalent.
        Use no delimiters for the numbers.
    '''
    response = llm(template)
    try:
        # here we diverge from the task descriptions for the following reasons:
        # 1. Calling `set()` to match the suggested response type sorts values 
        # so that the order "title-salary-bonus" might change, which we don't want;
        # 2. Such a structure will make the hiring plan creation easier. 
        title, salary, bonus = response.split(';') # is supposed to be semicolon-separated
        return {
            'name': title.strip(),
            'salary': salary,
            'bonus': bonus
        }
    except: return {'desc': response} # in case the model refuses to give us the needed structure