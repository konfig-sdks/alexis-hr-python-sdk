from alexis_hr_python_sdk.paths.leave_id.get import ApiForget
from alexis_hr_python_sdk.paths.leave_id.put import ApiForput
from alexis_hr_python_sdk.paths.leave_id.delete import ApiFordelete
from alexis_hr_python_sdk.paths.leave_id.patch import ApiForpatch


class LeaveId(
    ApiForget,
    ApiForput,
    ApiFordelete,
    ApiForpatch,
):
    pass
