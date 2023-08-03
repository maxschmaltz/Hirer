import unittest
import json

from prepare import get_model
from employee import employee
from hiring_plan import process_desc, hiring_plan


class EployeeTest(unittest.TestCase):

    params_path = './params.json'
    llm = get_model(params_path)

    n_iters = 5

    def generate_test_employee(self):
        desc = self.llm('Generate random job position description.') # to make testing faster we'll generate cases
        print(f'{desc}\n')
        response = employee(self.llm, desc)
        print(f'{response}\n\n')
        self.assertIsInstance(response, dict)
        self.assertListEqual(
            list(response.keys()),
            ['name', 'salary', 'bonus']
        )
        with self.assertRaises(ValueError): int(response['name']) # a textual string
        self.assertIsInstance(int(response['salary']), int) # a numeric string
        self.assertIsInstance(int(response['bonus']), int) # a numeric string

    def test_employee(self):
        for _ in range(self.n_iters): self.generate_test_employee() # no time for a better iteration way


class HiringPlanTest(unittest.TestCase):

    params_path = './params.json'
    llm = get_model(params_path)

    example_path = 'example.json'

    n_iters = 3

    def generate_test_hiring_plan(self):
        desc = self.llm('Generate random team at in a small for-profit organization.') # to make testing faster we'll generate cases
        print(f'{desc}\n')
        employee_descs = process_desc(self.llm, desc)
        print(f'{employee_descs}\n\n')
        self.assertIsInstance(employee_descs, list)


    def generate_test_hiring_plan(self):
        desc = self.llm('Generate random team for a small for-profit organization.') # to make testing faster we'll generate cases
        print(f'{desc}\n')
        response = hiring_plan(self.llm, desc)
        print(f'{response}\n\n')
        self.assertIsInstance(response, dict)
        self.assertListEqual(
            list(response.keys()),
            ['positions', 'total_annual_salary', 'total_annual_bonus', 'total_annual_cost']
        )
        self.assertIsInstance(response['positions'], list)
        self.assertIsInstance(int(response['total_annual_salary']), int) # a numeric string
        self.assertIsInstance(int(response['total_annual_bonus']), int) # a numeric string
        with open(self.example_path, 'w') as f: json.dump(response, f, indent=4)


    def test_hiring_plan(self):
        for _ in range(self.n_iters): self.generate_test_hiring_plan() # no time for a better iteration way



if __name__ == '__main__':
    unittest.main()