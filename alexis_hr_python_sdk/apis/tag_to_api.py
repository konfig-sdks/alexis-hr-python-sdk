import typing_extensions

from alexis_hr_python_sdk.apis.tags import TagValues
from alexis_hr_python_sdk.apis.tags.employee_api import EmployeeApi
from alexis_hr_python_sdk.apis.tags.department_api import DepartmentApi
from alexis_hr_python_sdk.apis.tags.office_api import OfficeApi
from alexis_hr_python_sdk.apis.tags.team_api import TeamApi
from alexis_hr_python_sdk.apis.tags.employee_team_reference_api import EmployeeTeamReferenceApi
from alexis_hr_python_sdk.apis.tags.compensation_api import CompensationApi
from alexis_hr_python_sdk.apis.tags.employment_api import EmploymentApi
from alexis_hr_python_sdk.apis.tags.employment_type_api import EmploymentTypeApi
from alexis_hr_python_sdk.apis.tags.cost_center_api import CostCenterApi
from alexis_hr_python_sdk.apis.tags.leave_api import LeaveApi
from alexis_hr_python_sdk.apis.tags.leave_type_api import LeaveTypeApi
from alexis_hr_python_sdk.apis.tags.child_api import ChildApi
from alexis_hr_python_sdk.apis.tags.timesheet_entry_api import TimesheetEntryApi
from alexis_hr_python_sdk.apis.tags.work_week_api import WorkWeekApi
from alexis_hr_python_sdk.apis.tags.company_api import CompanyApi
from alexis_hr_python_sdk.apis.tags.leave_transaction_api import LeaveTransactionApi
from alexis_hr_python_sdk.apis.tags.timesheet_api import TimesheetApi
from alexis_hr_python_sdk.apis.tags.timesheet_entry_type_api import TimesheetEntryTypeApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.EMPLOYEE: EmployeeApi,
        TagValues.DEPARTMENT: DepartmentApi,
        TagValues.OFFICE: OfficeApi,
        TagValues.TEAM: TeamApi,
        TagValues.EMPLOYEETEAMREFERENCE: EmployeeTeamReferenceApi,
        TagValues.COMPENSATION: CompensationApi,
        TagValues.EMPLOYMENT: EmploymentApi,
        TagValues.EMPLOYMENTTYPE: EmploymentTypeApi,
        TagValues.COSTCENTER: CostCenterApi,
        TagValues.LEAVE: LeaveApi,
        TagValues.LEAVETYPE: LeaveTypeApi,
        TagValues.CHILD: ChildApi,
        TagValues.TIMESHEETENTRY: TimesheetEntryApi,
        TagValues.WORKWEEK: WorkWeekApi,
        TagValues.COMPANY: CompanyApi,
        TagValues.LEAVETRANSACTION: LeaveTransactionApi,
        TagValues.TIMESHEET: TimesheetApi,
        TagValues.TIMESHEETENTRYTYPE: TimesheetEntryTypeApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.EMPLOYEE: EmployeeApi,
        TagValues.DEPARTMENT: DepartmentApi,
        TagValues.OFFICE: OfficeApi,
        TagValues.TEAM: TeamApi,
        TagValues.EMPLOYEETEAMREFERENCE: EmployeeTeamReferenceApi,
        TagValues.COMPENSATION: CompensationApi,
        TagValues.EMPLOYMENT: EmploymentApi,
        TagValues.EMPLOYMENTTYPE: EmploymentTypeApi,
        TagValues.COSTCENTER: CostCenterApi,
        TagValues.LEAVE: LeaveApi,
        TagValues.LEAVETYPE: LeaveTypeApi,
        TagValues.CHILD: ChildApi,
        TagValues.TIMESHEETENTRY: TimesheetEntryApi,
        TagValues.WORKWEEK: WorkWeekApi,
        TagValues.COMPANY: CompanyApi,
        TagValues.LEAVETRANSACTION: LeaveTransactionApi,
        TagValues.TIMESHEET: TimesheetApi,
        TagValues.TIMESHEETENTRYTYPE: TimesheetEntryTypeApi,
    }
)
