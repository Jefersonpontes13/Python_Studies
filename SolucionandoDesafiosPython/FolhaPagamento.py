"""coding: utf-8"""


def main():
    emp_no = int(input())
    worked_hours = int(input())
    receives_per_worked_hour = float(input())
    salary = receives_per_worked_hour * worked_hours

    print(f"NUMBER = {emp_no}")
    print(f"SALARY = U$ {salary:.2f}")


if __name__ == '__main__':
    main()
