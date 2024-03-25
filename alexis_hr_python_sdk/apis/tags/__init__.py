# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from alexis_hr_python_sdk.apis.tag_to_api import tag_to_api

import enum


class TagValues(str, enum.Enum):
    EMPLOYEE = "employee"
    DEPARTMENT = "department"
    OFFICE = "office"
    TEAM = "team"
    EMPLOYEETEAMREFERENCE = "employee-team-reference"
    COMPENSATION = "compensation"
    EMPLOYMENT = "employment"
    EMPLOYMENTTYPE = "employment-type"
    COSTCENTER = "cost-center"
    LEAVE = "leave"
    LEAVETYPE = "leave-type"
    CHILD = "child"
    TIMESHEETENTRY = "timesheet-entry"
    WORKWEEK = "work-week"
    COMPANY = "company"
    LEAVETRANSACTION = "leave-transaction"
    TIMESHEET = "timesheet"
    TIMESHEETENTRYTYPE = "timesheet-entry-type"
