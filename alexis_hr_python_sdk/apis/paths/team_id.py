from alexis_hr_python_sdk.paths.team_id.get import ApiForget
from alexis_hr_python_sdk.paths.team_id.put import ApiForput
from alexis_hr_python_sdk.paths.team_id.delete import ApiFordelete
from alexis_hr_python_sdk.paths.team_id.patch import ApiForpatch


class TeamId(
    ApiForget,
    ApiForput,
    ApiFordelete,
    ApiForpatch,
):
    pass
