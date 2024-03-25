from alexis_hr_python_sdk.paths.timesheet_entry_id.get import ApiForget
from alexis_hr_python_sdk.paths.timesheet_entry_id.put import ApiForput
from alexis_hr_python_sdk.paths.timesheet_entry_id.delete import ApiFordelete
from alexis_hr_python_sdk.paths.timesheet_entry_id.patch import ApiForpatch


class TimesheetEntryId(
    ApiForget,
    ApiForput,
    ApiFordelete,
    ApiForpatch,
):
    pass
