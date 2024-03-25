from alexis_hr_python_sdk.paths.work_week_id.get import ApiForget
from alexis_hr_python_sdk.paths.work_week_id.put import ApiForput
from alexis_hr_python_sdk.paths.work_week_id.delete import ApiFordelete
from alexis_hr_python_sdk.paths.work_week_id.patch import ApiForpatch


class WorkWeekId(
    ApiForget,
    ApiForput,
    ApiFordelete,
    ApiForpatch,
):
    pass
