from alexis_hr_python_sdk.paths.leave_type_id.get import ApiForget
from alexis_hr_python_sdk.paths.leave_type_id.put import ApiForput
from alexis_hr_python_sdk.paths.leave_type_id.delete import ApiFordelete
from alexis_hr_python_sdk.paths.leave_type_id.patch import ApiForpatch


class LeaveTypeId(
    ApiForget,
    ApiForput,
    ApiFordelete,
    ApiForpatch,
):
    pass
