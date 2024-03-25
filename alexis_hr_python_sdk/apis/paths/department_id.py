from alexis_hr_python_sdk.paths.department_id.get import ApiForget
from alexis_hr_python_sdk.paths.department_id.put import ApiForput
from alexis_hr_python_sdk.paths.department_id.delete import ApiFordelete
from alexis_hr_python_sdk.paths.department_id.patch import ApiForpatch


class DepartmentId(
    ApiForget,
    ApiForput,
    ApiFordelete,
    ApiForpatch,
):
    pass
