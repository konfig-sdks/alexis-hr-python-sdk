from alexis_hr_python_sdk.paths.child_id.get import ApiForget
from alexis_hr_python_sdk.paths.child_id.put import ApiForput
from alexis_hr_python_sdk.paths.child_id.delete import ApiFordelete
from alexis_hr_python_sdk.paths.child_id.patch import ApiForpatch


class ChildId(
    ApiForget,
    ApiForput,
    ApiFordelete,
    ApiForpatch,
):
    pass
