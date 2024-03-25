from alexis_hr_python_sdk.paths.employment_type_id.get import ApiForget
from alexis_hr_python_sdk.paths.employment_type_id.put import ApiForput
from alexis_hr_python_sdk.paths.employment_type_id.delete import ApiFordelete
from alexis_hr_python_sdk.paths.employment_type_id.patch import ApiForpatch


class EmploymentTypeId(
    ApiForget,
    ApiForput,
    ApiFordelete,
    ApiForpatch,
):
    pass
