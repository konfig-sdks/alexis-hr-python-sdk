from alexis_hr_python_sdk.paths.employee_id.get import ApiForget
from alexis_hr_python_sdk.paths.employee_id.put import ApiForput
from alexis_hr_python_sdk.paths.employee_id.delete import ApiFordelete
from alexis_hr_python_sdk.paths.employee_id.patch import ApiForpatch


class EmployeeId(
    ApiForget,
    ApiForput,
    ApiFordelete,
    ApiForpatch,
):
    pass
