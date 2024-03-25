from alexis_hr_python_sdk.paths.employment_id.get import ApiForget
from alexis_hr_python_sdk.paths.employment_id.put import ApiForput
from alexis_hr_python_sdk.paths.employment_id.delete import ApiFordelete
from alexis_hr_python_sdk.paths.employment_id.patch import ApiForpatch


class EmploymentId(
    ApiForget,
    ApiForput,
    ApiFordelete,
    ApiForpatch,
):
    pass
