import typing_extensions

from alexis_hr_python_sdk.paths import PathValues
from alexis_hr_python_sdk.apis.paths.company import Company
from alexis_hr_python_sdk.apis.paths.company_id import CompanyId
from alexis_hr_python_sdk.apis.paths.employee import Employee
from alexis_hr_python_sdk.apis.paths.employee_id import EmployeeId
from alexis_hr_python_sdk.apis.paths.department import Department
from alexis_hr_python_sdk.apis.paths.department_id import DepartmentId
from alexis_hr_python_sdk.apis.paths.office import Office
from alexis_hr_python_sdk.apis.paths.office_id import OfficeId
from alexis_hr_python_sdk.apis.paths.team import Team
from alexis_hr_python_sdk.apis.paths.team_id import TeamId
from alexis_hr_python_sdk.apis.paths.employee_team_reference import EmployeeTeamReference
from alexis_hr_python_sdk.apis.paths.employee_team_reference_id import EmployeeTeamReferenceId
from alexis_hr_python_sdk.apis.paths.compensation import Compensation
from alexis_hr_python_sdk.apis.paths.compensation_id import CompensationId
from alexis_hr_python_sdk.apis.paths.employment import Employment
from alexis_hr_python_sdk.apis.paths.employment_id import EmploymentId
from alexis_hr_python_sdk.apis.paths.employment_type import EmploymentType
from alexis_hr_python_sdk.apis.paths.employment_type_id import EmploymentTypeId
from alexis_hr_python_sdk.apis.paths.cost_center import CostCenter
from alexis_hr_python_sdk.apis.paths.cost_center_id import CostCenterId
from alexis_hr_python_sdk.apis.paths.leave import Leave
from alexis_hr_python_sdk.apis.paths.leave_id import LeaveId
from alexis_hr_python_sdk.apis.paths.leave_type import LeaveType
from alexis_hr_python_sdk.apis.paths.leave_type_id import LeaveTypeId
from alexis_hr_python_sdk.apis.paths.leave_transaction import LeaveTransaction
from alexis_hr_python_sdk.apis.paths.leave_transaction_id import LeaveTransactionId
from alexis_hr_python_sdk.apis.paths.child import Child
from alexis_hr_python_sdk.apis.paths.child_id import ChildId
from alexis_hr_python_sdk.apis.paths.timesheet import Timesheet
from alexis_hr_python_sdk.apis.paths.timesheet_id import TimesheetId
from alexis_hr_python_sdk.apis.paths.timesheet_entry import TimesheetEntry
from alexis_hr_python_sdk.apis.paths.timesheet_entry_id import TimesheetEntryId
from alexis_hr_python_sdk.apis.paths.timesheet_entry_type import TimesheetEntryType
from alexis_hr_python_sdk.apis.paths.timesheet_entry_type_id import TimesheetEntryTypeId
from alexis_hr_python_sdk.apis.paths.work_week import WorkWeek
from alexis_hr_python_sdk.apis.paths.work_week_id import WorkWeekId

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.COMPANY: Company,
        PathValues.COMPANY_ID: CompanyId,
        PathValues.EMPLOYEE: Employee,
        PathValues.EMPLOYEE_ID: EmployeeId,
        PathValues.DEPARTMENT: Department,
        PathValues.DEPARTMENT_ID: DepartmentId,
        PathValues.OFFICE: Office,
        PathValues.OFFICE_ID: OfficeId,
        PathValues.TEAM: Team,
        PathValues.TEAM_ID: TeamId,
        PathValues.EMPLOYEETEAMREFERENCE: EmployeeTeamReference,
        PathValues.EMPLOYEETEAMREFERENCE_ID: EmployeeTeamReferenceId,
        PathValues.COMPENSATION: Compensation,
        PathValues.COMPENSATION_ID: CompensationId,
        PathValues.EMPLOYMENT: Employment,
        PathValues.EMPLOYMENT_ID: EmploymentId,
        PathValues.EMPLOYMENTTYPE: EmploymentType,
        PathValues.EMPLOYMENTTYPE_ID: EmploymentTypeId,
        PathValues.COSTCENTER: CostCenter,
        PathValues.COSTCENTER_ID: CostCenterId,
        PathValues.LEAVE: Leave,
        PathValues.LEAVE_ID: LeaveId,
        PathValues.LEAVETYPE: LeaveType,
        PathValues.LEAVETYPE_ID: LeaveTypeId,
        PathValues.LEAVETRANSACTION: LeaveTransaction,
        PathValues.LEAVETRANSACTION_ID: LeaveTransactionId,
        PathValues.CHILD: Child,
        PathValues.CHILD_ID: ChildId,
        PathValues.TIMESHEET: Timesheet,
        PathValues.TIMESHEET_ID: TimesheetId,
        PathValues.TIMESHEETENTRY: TimesheetEntry,
        PathValues.TIMESHEETENTRY_ID: TimesheetEntryId,
        PathValues.TIMESHEETENTRYTYPE: TimesheetEntryType,
        PathValues.TIMESHEETENTRYTYPE_ID: TimesheetEntryTypeId,
        PathValues.WORKWEEK: WorkWeek,
        PathValues.WORKWEEK_ID: WorkWeekId,
    }
)

path_to_api = PathToApi(
    {
        PathValues.COMPANY: Company,
        PathValues.COMPANY_ID: CompanyId,
        PathValues.EMPLOYEE: Employee,
        PathValues.EMPLOYEE_ID: EmployeeId,
        PathValues.DEPARTMENT: Department,
        PathValues.DEPARTMENT_ID: DepartmentId,
        PathValues.OFFICE: Office,
        PathValues.OFFICE_ID: OfficeId,
        PathValues.TEAM: Team,
        PathValues.TEAM_ID: TeamId,
        PathValues.EMPLOYEETEAMREFERENCE: EmployeeTeamReference,
        PathValues.EMPLOYEETEAMREFERENCE_ID: EmployeeTeamReferenceId,
        PathValues.COMPENSATION: Compensation,
        PathValues.COMPENSATION_ID: CompensationId,
        PathValues.EMPLOYMENT: Employment,
        PathValues.EMPLOYMENT_ID: EmploymentId,
        PathValues.EMPLOYMENTTYPE: EmploymentType,
        PathValues.EMPLOYMENTTYPE_ID: EmploymentTypeId,
        PathValues.COSTCENTER: CostCenter,
        PathValues.COSTCENTER_ID: CostCenterId,
        PathValues.LEAVE: Leave,
        PathValues.LEAVE_ID: LeaveId,
        PathValues.LEAVETYPE: LeaveType,
        PathValues.LEAVETYPE_ID: LeaveTypeId,
        PathValues.LEAVETRANSACTION: LeaveTransaction,
        PathValues.LEAVETRANSACTION_ID: LeaveTransactionId,
        PathValues.CHILD: Child,
        PathValues.CHILD_ID: ChildId,
        PathValues.TIMESHEET: Timesheet,
        PathValues.TIMESHEET_ID: TimesheetId,
        PathValues.TIMESHEETENTRY: TimesheetEntry,
        PathValues.TIMESHEETENTRY_ID: TimesheetEntryId,
        PathValues.TIMESHEETENTRYTYPE: TimesheetEntryType,
        PathValues.TIMESHEETENTRYTYPE_ID: TimesheetEntryTypeId,
        PathValues.WORKWEEK: WorkWeek,
        PathValues.WORKWEEK_ID: WorkWeekId,
    }
)
