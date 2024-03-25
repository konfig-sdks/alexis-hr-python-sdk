from alexis_hr_python_sdk.paths.cost_center_id.get import ApiForget
from alexis_hr_python_sdk.paths.cost_center_id.put import ApiForput
from alexis_hr_python_sdk.paths.cost_center_id.delete import ApiFordelete
from alexis_hr_python_sdk.paths.cost_center_id.patch import ApiForpatch


class CostCenterId(
    ApiForget,
    ApiForput,
    ApiFordelete,
    ApiForpatch,
):
    pass
