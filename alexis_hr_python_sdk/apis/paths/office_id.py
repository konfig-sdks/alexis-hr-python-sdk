from alexis_hr_python_sdk.paths.office_id.get import ApiForget
from alexis_hr_python_sdk.paths.office_id.put import ApiForput
from alexis_hr_python_sdk.paths.office_id.delete import ApiFordelete
from alexis_hr_python_sdk.paths.office_id.patch import ApiForpatch


class OfficeId(
    ApiForget,
    ApiForput,
    ApiFordelete,
    ApiForpatch,
):
    pass
