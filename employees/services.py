
from .models import EmployeeDetails,EmployeeWork

def build_prompt(employee,work):
  prompt={
    "name":f"{employee.employee_first_name} {employee.employee_last_name}",
    "email":employee.email,
    "phone":employee.phone,
    "role":work.role,
    "department":work.department,
    "office_location":work.office_location,
    "projects":work.projects,
    "no_of_projects_completed":work.no_of_projects_completed,
    "rating":work.rating,
    "performance_summary":work.performance_summary
    
  }
  return prompt
def generate_summary(data):
  name=data["name"]
  email=data["email"]
  phone=data["phone"]
  role=data["role"]
  department=data["department"]
  office_location=data["office_location"]
  projects=data["projects"]
  no_of_projects_completed=data["no_of_projects_completed"]
  rating=data["rating"]
  performance_summary=data["performance_summary"]
  summary=f"""{name} works as a {role} in the {department} department located in {office_location}.
The employee has successfully completed {no_of_projects_completed} projects including {projects}.
Their performance rating is {rating}/5.

Performance Overview:
{performance_summary}"""
  return summary   
  