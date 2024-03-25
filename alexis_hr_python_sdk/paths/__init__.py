# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from alexis_hr_python_sdk.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    COMPANY = "/company"
    COMPANY_ID = "/company/{id}"
    EMPLOYEE = "/employee"
    EMPLOYEE_ID = "/employee/{id}"
    DEPARTMENT = "/department"
    DEPARTMENT_ID = "/department/{id}"
    OFFICE = "/office"
    OFFICE_ID = "/office/{id}"
    TEAM = "/team"
    TEAM_ID = "/team/{id}"
    EMPLOYEETEAMREFERENCE = "/employee-team-reference"
    EMPLOYEETEAMREFERENCE_ID = "/employee-team-reference/{id}"
    COMPENSATION = "/compensation"
    COMPENSATION_ID = "/compensation/{id}"
    EMPLOYMENT = "/employment"
    EMPLOYMENT_ID = "/employment/{id}"
    EMPLOYMENTTYPE = "/employment-type"
    EMPLOYMENTTYPE_ID = "/employment-type/{id}"
    COSTCENTER = "/cost-center"
    COSTCENTER_ID = "/cost-center/{id}"
    LEAVE = "/leave"
    LEAVE_ID = "/leave/{id}"
    LEAVETYPE = "/leave-type"
    LEAVETYPE_ID = "/leave-type/{id}"
    LEAVETRANSACTION = "/leave-transaction"
    LEAVETRANSACTION_ID = "/leave-transaction/{id}"
    CHILD = "/child"
    CHILD_ID = "/child/{id}"
    TIMESHEET = "/timesheet"
    TIMESHEET_ID = "/timesheet/{id}"
    TIMESHEETENTRY = "/timesheet-entry"
    TIMESHEETENTRY_ID = "/timesheet-entry/{id}"
    TIMESHEETENTRYTYPE = "/timesheet-entry-type"
    TIMESHEETENTRYTYPE_ID = "/timesheet-entry-type/{id}"
    WORKWEEK = "/work-week"
    WORKWEEK_ID = "/work-week/{id}"
