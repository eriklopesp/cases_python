import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:

    resultado = (
        employee
            .merge(department, how="left", left_on="departmentId", right_on="id")
            .rename(columns={"name_x": "Employee","name_y": "Department","salary": "Salary"})
    )

    resultado["MaxSalary"] = (resultado.groupby("Department")["Salary"].transform("max"))

    resultado = (
        resultado[resultado["Salary"] == resultado["MaxSalary"]]
            [["Department", "Employee", "Salary"]]
            .sort_values(["Department", "Employee"])
            .reset_index(drop=True)
    )
    return resultado

employee = pd.DataFrame({
    "id": [1, 2, 3, 4, 5],
    "name": ["Alice", "Bob", "Charlie", "David", "Eve"],
    "salary": [50000, 60000, 55000, 70000, 65000],
    "departmentId": [1, 2, 1, 3, 2]
})

department = pd.DataFrame({
    "id": [1, 2, 3],
    "name": ["HR", "Engineering", "Sales"]
})

print(department_highest_salary(employee, department))