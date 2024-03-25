operation_parameter_map = {
    '/child-POST': {
        'parameters': [
            {
                'name': 'employeeId'
            },
            {
                'name': 'name'
            },
            {
                'name': 'birthdate'
            },
        ]
    },
    '/child/{id}-DELETE': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/child-GET': {
        'parameters': [
            {
                'name': 'select'
            },
            {
                'name': 'filters'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'offset'
            },
            {
                'name': 'sort'
            },
        ]
    },
    '/child/{id}-GET': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'select'
            },
        ]
    },
    '/child/{id}-PUT': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'birthdate'
            },
            {
                'name': 'id'
            },
        ]
    },
    '/child/{id}-PATCH': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'birthdate'
            },
            {
                'name': 'id'
            },
        ]
    },
    '/company/{id}-GET': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'select'
            },
        ]
    },
    '/company-GET': {
        'parameters': [
            {
                'name': 'select'
            },
            {
                'name': 'filters'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'offset'
            },
            {
                'name': 'sort'
            },
        ]
    },
    '/compensation-POST': {
        'parameters': [
            {
                'name': 'employeeId'
            },
            {
                'name': 'userId'
            },
            {
                'name': 'amount'
            },
            {
                'name': 'effectiveDate'
            },
            {
                'name': 'currency'
            },
            {
                'name': 'payoutDay'
            },
            {
                'name': 'payoutPeriod'
            },
            {
                'name': 'payoutFrequency'
            },
            {
                'name': 'paidOvertime'
            },
            {
                'name': 'companyId'
            },
            {
                'name': 'salarySchedule'
            },
            {
                'name': 'note'
            },
        ]
    },
    '/compensation/{id}-DELETE': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/compensation-GET': {
        'parameters': [
            {
                'name': 'select'
            },
            {
                'name': 'filters'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'offset'
            },
            {
                'name': 'sort'
            },
        ]
    },
    '/compensation/{id}-GET': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'select'
            },
        ]
    },
    '/compensation/{id}-PUT': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'employeeId'
            },
            {
                'name': 'userId'
            },
            {
                'name': 'amount'
            },
            {
                'name': 'currency'
            },
            {
                'name': 'payoutDay'
            },
            {
                'name': 'payoutPeriod'
            },
            {
                'name': 'payoutFrequency'
            },
            {
                'name': 'salarySchedule'
            },
            {
                'name': 'paidOvertime'
            },
            {
                'name': 'note'
            },
        ]
    },
    '/compensation/{id}-PATCH': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'employeeId'
            },
            {
                'name': 'userId'
            },
            {
                'name': 'amount'
            },
            {
                'name': 'currency'
            },
            {
                'name': 'payoutDay'
            },
            {
                'name': 'payoutPeriod'
            },
            {
                'name': 'payoutFrequency'
            },
            {
                'name': 'salarySchedule'
            },
            {
                'name': 'paidOvertime'
            },
            {
                'name': 'note'
            },
        ]
    },
    '/cost-center-POST': {
        'parameters': [
            {
                'name': 'code'
            },
            {
                'name': 'name'
            },
        ]
    },
    '/cost-center/{id}-DELETE': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/cost-center-GET': {
        'parameters': [
            {
                'name': 'select'
            },
            {
                'name': 'filters'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'offset'
            },
            {
                'name': 'sort'
            },
        ]
    },
    '/cost-center/{id}-GET': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'select'
            },
        ]
    },
    '/cost-center/{id}-PUT': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'code'
            },
            {
                'name': 'name'
            },
        ]
    },
    '/cost-center/{id}-PATCH': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'code'
            },
            {
                'name': 'name'
            },
        ]
    },
    '/department-POST': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'description'
            },
            {
                'name': 'costCenterId'
            },
            {
                'name': 'parentId'
            },
        ]
    },
    '/department/{id}-DELETE': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/department/{id}-GET': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'select'
            },
            {
                'name': 'relations'
            },
        ]
    },
    '/department-GET': {
        'parameters': [
            {
                'name': 'select'
            },
            {
                'name': 'relations'
            },
            {
                'name': 'filters'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'offset'
            },
            {
                'name': 'sort'
            },
        ]
    },
    '/department/{id}-PUT': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'id'
            },
            {
                'name': 'description'
            },
            {
                'name': 'costCenterId'
            },
            {
                'name': 'parentId'
            },
        ]
    },
    '/department/{id}-PATCH': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'id'
            },
            {
                'name': 'description'
            },
            {
                'name': 'costCenterId'
            },
            {
                'name': 'parentId'
            },
        ]
    },
    '/employee-POST': {
        'parameters': [
            {
                'name': 'title'
            },
            {
                'name': 'officeId'
            },
            {
                'name': 'managerEmployeeId'
            },
            {
                'name': 'departmentId'
            },
            {
                'name': 'costCenterId'
            },
            {
                'name': 'userName'
            },
            {
                'name': 'division'
            },
            {
                'name': 'organization'
            },
            {
                'name': 'employeeNumber'
            },
            {
                'name': 'tax'
            },
            {
                'name': 'workEmail'
            },
            {
                'name': 'workPhone'
            },
            {
                'name': 'hasOccupationalPension'
            },
            {
                'name': 'privateEmail'
            },
            {
                'name': 'firstName'
            },
            {
                'name': 'lastName'
            },
            {
                'name': 'ssn'
            },
            {
                'name': 'privatePhone'
            },
            {
                'name': 'birthDate'
            },
            {
                'name': 'avatarUrl'
            },
            {
                'name': 'nationality'
            },
            {
                'name': 'gender'
            },
            {
                'name': 'pronoun'
            },
            {
                'name': 'bankAccount'
            },
            {
                'name': 'homeAddress'
            },
            {
                'name': 'custom'
            },
        ]
    },
    '/employee/{id}-GET': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'select'
            },
            {
                'name': 'relations'
            },
        ]
    },
    '/employee-GET': {
        'parameters': [
            {
                'name': 'select'
            },
            {
                'name': 'relations'
            },
            {
                'name': 'filters'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'offset'
            },
            {
                'name': 'sort'
            },
        ]
    },
    '/employee/{id}-DELETE': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/employee/{id}-PUT': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'title'
            },
            {
                'name': 'officeId'
            },
            {
                'name': 'managerEmployeeId'
            },
            {
                'name': 'departmentId'
            },
            {
                'name': 'costCenterId'
            },
            {
                'name': 'userName'
            },
            {
                'name': 'division'
            },
            {
                'name': 'organization'
            },
            {
                'name': 'employeeNumber'
            },
            {
                'name': 'tax'
            },
            {
                'name': 'workEmail'
            },
            {
                'name': 'workPhone'
            },
            {
                'name': 'hasOccupationalPension'
            },
            {
                'name': 'privateEmail'
            },
            {
                'name': 'firstName'
            },
            {
                'name': 'lastName'
            },
            {
                'name': 'ssn'
            },
            {
                'name': 'privatePhone'
            },
            {
                'name': 'birthDate'
            },
            {
                'name': 'avatarUrl'
            },
            {
                'name': 'nationality'
            },
            {
                'name': 'gender'
            },
            {
                'name': 'pronoun'
            },
            {
                'name': 'bankAccount'
            },
            {
                'name': 'homeAddress'
            },
            {
                'name': 'custom'
            },
            {
                'name': 'active'
            },
        ]
    },
    '/employee/{id}-PATCH': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'title'
            },
            {
                'name': 'officeId'
            },
            {
                'name': 'managerEmployeeId'
            },
            {
                'name': 'departmentId'
            },
            {
                'name': 'costCenterId'
            },
            {
                'name': 'userName'
            },
            {
                'name': 'division'
            },
            {
                'name': 'organization'
            },
            {
                'name': 'employeeNumber'
            },
            {
                'name': 'tax'
            },
            {
                'name': 'workEmail'
            },
            {
                'name': 'workPhone'
            },
            {
                'name': 'hasOccupationalPension'
            },
            {
                'name': 'privateEmail'
            },
            {
                'name': 'firstName'
            },
            {
                'name': 'lastName'
            },
            {
                'name': 'ssn'
            },
            {
                'name': 'privatePhone'
            },
            {
                'name': 'birthDate'
            },
            {
                'name': 'avatarUrl'
            },
            {
                'name': 'nationality'
            },
            {
                'name': 'gender'
            },
            {
                'name': 'pronoun'
            },
            {
                'name': 'bankAccount'
            },
            {
                'name': 'homeAddress'
            },
            {
                'name': 'custom'
            },
            {
                'name': 'active'
            },
        ]
    },
    '/employee-team-reference-POST': {
        'parameters': [
            {
                'name': 'teamId'
            },
            {
                'name': 'companyId'
            },
            {
                'name': 'employeeId'
            },
            {
                'name': 'userId'
            },
        ]
    },
    '/employee-team-reference/{id}-DELETE': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/employee-team-reference-GET': {
        'parameters': [
            {
                'name': 'select'
            },
            {
                'name': 'relations'
            },
            {
                'name': 'filters'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'offset'
            },
            {
                'name': 'sort'
            },
        ]
    },
    '/employee-team-reference/{id}-GET': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'select'
            },
            {
                'name': 'relations'
            },
        ]
    },
    '/employee-team-reference/{id}-PUT': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'teamId'
            },
        ]
    },
    '/employee-team-reference/{id}-PATCH': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'teamId'
            },
        ]
    },
    '/employment-POST': {
        'parameters': [
            {
                'name': 'employeeId'
            },
            {
                'name': 'userId'
            },
            {
                'name': 'typeId'
            },
            {
                'name': 'startDate'
            },
            {
                'name': 'terminated'
            },
            {
                'name': 'rate'
            },
            {
                'name': 'country'
            },
            {
                'name': 'endDate'
            },
            {
                'name': 'effectiveEndDate'
            },
            {
                'name': 'note'
            },
        ]
    },
    '/employment/{id}-GET': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'select'
            },
            {
                'name': 'relations'
            },
        ]
    },
    '/employment-GET': {
        'parameters': [
            {
                'name': 'select'
            },
            {
                'name': 'relations'
            },
            {
                'name': 'filters'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'offset'
            },
            {
                'name': 'sort'
            },
        ]
    },
    '/employment/{id}-DELETE': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/employment/{id}-PUT': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'employeeId'
            },
            {
                'name': 'userId'
            },
            {
                'name': 'typeId'
            },
            {
                'name': 'startDate'
            },
            {
                'name': 'endDate'
            },
            {
                'name': 'effectiveEndDate'
            },
            {
                'name': 'terminated'
            },
            {
                'name': 'rate'
            },
            {
                'name': 'note'
            },
            {
                'name': 'country'
            },
        ]
    },
    '/employment/{id}-PATCH': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'employeeId'
            },
            {
                'name': 'userId'
            },
            {
                'name': 'typeId'
            },
            {
                'name': 'startDate'
            },
            {
                'name': 'endDate'
            },
            {
                'name': 'effectiveEndDate'
            },
            {
                'name': 'terminated'
            },
            {
                'name': 'rate'
            },
            {
                'name': 'note'
            },
            {
                'name': 'country'
            },
        ]
    },
    '/employment-type-POST': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'vacation'
            },
            {
                'name': 'country'
            },
            {
                'name': 'maxMonths'
            },
        ]
    },
    '/employment-type/{id}-DELETE': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/employment-type-GET': {
        'parameters': [
            {
                'name': 'select'
            },
            {
                'name': 'filters'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'offset'
            },
            {
                'name': 'sort'
            },
        ]
    },
    '/employment-type/{id}-GET': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'select'
            },
        ]
    },
    '/employment-type/{id}-PUT': {
        'parameters': [
            {
                'name': 'country'
            },
            {
                'name': 'id'
            },
            {
                'name': 'name'
            },
            {
                'name': 'vacation'
            },
            {
                'name': 'maxMonths'
            },
        ]
    },
    '/employment-type/{id}-PATCH': {
        'parameters': [
            {
                'name': 'country'
            },
            {
                'name': 'id'
            },
            {
                'name': 'name'
            },
            {
                'name': 'vacation'
            },
            {
                'name': 'maxMonths'
            },
        ]
    },
    '/leave-POST': {
        'parameters': [
            {
                'name': 'employeeId'
            },
            {
                'name': 'typeId'
            },
            {
                'name': 'duration'
            },
            {
                'name': 'startDate'
            },
            {
                'name': 'endDate'
            },
            {
                'name': 'description'
            },
            {
                'name': 'childId'
            },
            {
                'name': 'extent'
            },
            {
                'name': 'morning'
            },
            {
                'name': 'afternoon'
            },
        ]
    },
    '/leave/{id}-DELETE': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/leave-GET': {
        'parameters': [
            {
                'name': 'select'
            },
            {
                'name': 'relations'
            },
            {
                'name': 'filters'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'offset'
            },
            {
                'name': 'sort'
            },
        ]
    },
    '/leave/{id}-GET': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'select'
            },
            {
                'name': 'relations'
            },
        ]
    },
    '/leave/{id}-PUT': {
        'parameters': [
            {
                'name': 'extent'
            },
            {
                'name': 'id'
            },
            {
                'name': 'description'
            },
            {
                'name': 'childId'
            },
            {
                'name': 'duration'
            },
            {
                'name': 'startDate'
            },
            {
                'name': 'endDate'
            },
            {
                'name': 'morning'
            },
            {
                'name': 'afternoon'
            },
            {
                'name': 'status'
            },
            {
                'name': 'approvalNote'
            },
        ]
    },
    '/leave/{id}-PATCH': {
        'parameters': [
            {
                'name': 'extent'
            },
            {
                'name': 'id'
            },
            {
                'name': 'description'
            },
            {
                'name': 'childId'
            },
            {
                'name': 'duration'
            },
            {
                'name': 'startDate'
            },
            {
                'name': 'endDate'
            },
            {
                'name': 'morning'
            },
            {
                'name': 'afternoon'
            },
            {
                'name': 'status'
            },
            {
                'name': 'approvalNote'
            },
        ]
    },
    '/leave-transaction/{id}-GET': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'select'
            },
            {
                'name': 'relations'
            },
        ]
    },
    '/leave-transaction-GET': {
        'parameters': [
            {
                'name': 'select'
            },
            {
                'name': 'relations'
            },
            {
                'name': 'filters'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'offset'
            },
            {
                'name': 'sort'
            },
        ]
    },
    '/leave-type-POST': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'kind'
            },
            {
                'name': 'minimumDuration'
            },
            {
                'name': 'deductible'
            },
            {
                'name': 'paid'
            },
            {
                'name': 'disabled'
            },
            {
                'name': 'archived'
            },
        ]
    },
    '/leave-type/{id}-DELETE': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/leave-type-GET': {
        'parameters': [
            {
                'name': 'select'
            },
            {
                'name': 'relations'
            },
            {
                'name': 'filters'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'offset'
            },
            {
                'name': 'sort'
            },
        ]
    },
    '/leave-type/{id}-GET': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'select'
            },
            {
                'name': 'relations'
            },
        ]
    },
    '/leave-type/{id}-PUT': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'name'
            },
            {
                'name': 'kind'
            },
            {
                'name': 'minimumDuration'
            },
            {
                'name': 'deductible'
            },
            {
                'name': 'paid'
            },
            {
                'name': 'disabled'
            },
            {
                'name': 'archived'
            },
        ]
    },
    '/leave-type/{id}-PATCH': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'name'
            },
            {
                'name': 'kind'
            },
            {
                'name': 'minimumDuration'
            },
            {
                'name': 'deductible'
            },
            {
                'name': 'paid'
            },
            {
                'name': 'disabled'
            },
            {
                'name': 'archived'
            },
        ]
    },
    '/office-POST': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'phone'
            },
            {
                'name': 'email'
            },
            {
                'name': 'timezone'
            },
            {
                'name': 'CFAR'
            },
            {
                'name': 'SCB'
            },
            {
                'name': 'SNI'
            },
        ]
    },
    '/office/{id}-DELETE': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/office/{id}-GET': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'select'
            },
        ]
    },
    '/office-GET': {
        'parameters': [
            {
                'name': 'select'
            },
            {
                'name': 'filters'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'offset'
            },
            {
                'name': 'sort'
            },
        ]
    },
    '/office/{id}-PUT': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'name'
            },
            {
                'name': 'phone'
            },
            {
                'name': 'email'
            },
            {
                'name': 'timezone'
            },
            {
                'name': 'CFAR'
            },
            {
                'name': 'SCB'
            },
            {
                'name': 'SNI'
            },
        ]
    },
    '/office/{id}-PATCH': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'name'
            },
            {
                'name': 'phone'
            },
            {
                'name': 'email'
            },
            {
                'name': 'timezone'
            },
            {
                'name': 'CFAR'
            },
            {
                'name': 'SCB'
            },
            {
                'name': 'SNI'
            },
        ]
    },
    '/team-POST': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'bgColor'
            },
            {
                'name': 'fgColor'
            },
            {
                'name': 'description'
            },
        ]
    },
    '/team/{id}-DELETE': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/team/{id}-GET': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'select'
            },
        ]
    },
    '/team-GET': {
        'parameters': [
            {
                'name': 'select'
            },
            {
                'name': 'filters'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'offset'
            },
            {
                'name': 'sort'
            },
        ]
    },
    '/team/{id}-PUT': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'description'
            },
            {
                'name': 'name'
            },
            {
                'name': 'bgColor'
            },
            {
                'name': 'fgColor'
            },
        ]
    },
    '/team/{id}-PATCH': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'description'
            },
            {
                'name': 'name'
            },
            {
                'name': 'bgColor'
            },
            {
                'name': 'fgColor'
            },
        ]
    },
    '/timesheet/{id}-GET': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'select'
            },
            {
                'name': 'relations'
            },
        ]
    },
    '/timesheet-GET': {
        'parameters': [
            {
                'name': 'select'
            },
            {
                'name': 'relations'
            },
            {
                'name': 'filters'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'offset'
            },
            {
                'name': 'sort'
            },
        ]
    },
    '/timesheet-entry-POST': {
        'parameters': [
            {
                'name': 'typeId'
            },
            {
                'name': 'employeeId'
            },
            {
                'name': 'date'
            },
            {
                'name': 'minutes'
            },
            {
                'name': 'note'
            },
        ]
    },
    '/timesheet-entry/{id}-DELETE': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/timesheet-entry/{id}-GET': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'select'
            },
            {
                'name': 'relations'
            },
        ]
    },
    '/timesheet-entry-GET': {
        'parameters': [
            {
                'name': 'select'
            },
            {
                'name': 'relations'
            },
            {
                'name': 'filters'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'offset'
            },
            {
                'name': 'sort'
            },
        ]
    },
    '/timesheet-entry/{id}-PUT': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'typeId'
            },
            {
                'name': 'employeeId'
            },
            {
                'name': 'date'
            },
            {
                'name': 'minutes'
            },
            {
                'name': 'note'
            },
        ]
    },
    '/timesheet-entry/{id}-PATCH': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'typeId'
            },
            {
                'name': 'employeeId'
            },
            {
                'name': 'date'
            },
            {
                'name': 'minutes'
            },
            {
                'name': 'note'
            },
        ]
    },
    '/timesheet-entry-type/{id}-GET': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'select'
            },
        ]
    },
    '/timesheet-entry-type-GET': {
        'parameters': [
            {
                'name': 'select'
            },
            {
                'name': 'filters'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'offset'
            },
            {
                'name': 'sort'
            },
        ]
    },
    '/work-week-POST': {
        'parameters': [
            {
                'name': 'effectiveFrom'
            },
            {
                'name': 'timezone'
            },
            {
                'name': 'duration'
            },
            {
                'name': 'monday'
            },
            {
                'name': 'tuesday'
            },
            {
                'name': 'wednesday'
            },
            {
                'name': 'thursday'
            },
            {
                'name': 'friday'
            },
            {
                'name': 'saturday'
            },
            {
                'name': 'sunday'
            },
            {
                'name': 'employeeId'
            },
            {
                'name': 'officeId'
            },
            {
                'name': 'effectiveTo'
            },
        ]
    },
    '/work-week/{id}-DELETE': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/work-week-GET': {
        'parameters': [
            {
                'name': 'select'
            },
            {
                'name': 'relations'
            },
            {
                'name': 'filters'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'offset'
            },
            {
                'name': 'sort'
            },
        ]
    },
    '/work-week/{id}-GET': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'select'
            },
            {
                'name': 'relations'
            },
        ]
    },
    '/work-week/{id}-PUT': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'effectiveTo'
            },
        ]
    },
    '/work-week/{id}-PATCH': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'effectiveTo'
            },
        ]
    },
};