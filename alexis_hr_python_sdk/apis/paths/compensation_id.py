from alexis_hr_python_sdk.paths.compensation_id.get import ApiForget
from alexis_hr_python_sdk.paths.compensation_id.put import ApiForput
from alexis_hr_python_sdk.paths.compensation_id.delete import ApiFordelete
from alexis_hr_python_sdk.paths.compensation_id.patch import ApiForpatch


class CompensationId(
    ApiForget,
    ApiForput,
    ApiFordelete,
    ApiForpatch,
):
    pass
