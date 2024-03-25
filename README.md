<div align="left">

[![Visit Alexishr](./header.png)](https://alexishr.com)

# Alexishr<a id="alexishr"></a>

<h1 id=\"introduction\">Introduction</h1>
<p>
  AlexisHR API is currently in preview. This means that small, backward
  incompatible changes might be introduced while in preview. The changes will be
  documented and communicated.
  <a
    href=\"https://cdn.forms-content.sg-form.com/56c6a65c-90a2-11eb-a700-a6de1aea3a1a\"
    target=\"_blank\"
    ><button>Subscribe to updates</button></a
  >
</p>

<h1 id=\"authentication\">Authentication</h1>
<pre class=\"click-to-expand-wrapper is-snippet-wrapper language-undefined\">
<code class=\"is-highlighted language-bash\">curl https://api.alexishr.com/v1/employee \\
  -H \"Authorization: Bearer &lt;your_access_token&gt;\"</code>
</pre>
<p>
  Authenticate your account when using the API by including your secret Access
  Token in the request.
  <a href=\"https://app.alexishr.com/access-tokens\">Manage your Access Tokens</a
  >.
</p>
<p>
  Authentication is performed by passing the Access Token in the Authorization
  header.
</p>
<hr />

<h1 id=\"structure\">Structure</h1>
<p>
  You will find the structure of the API to be highly uniform and consistent.
  Typically every resource can be accessed via a top level endpoint, such as
  <code>/v1/employee</code>. For every such resource, you can perform some of
  the following operations:
</p>
<h2>Operations</h2>
<table>
  <tr>
    <td>GET /v1/:resource</td>
    <td>List all objects of this type</td>
  </tr>
  <tr>
    <td>GET /v1/:resource/:id</td>
    <td>Retrieve a resource by id</td>
  </tr>
  <tr>
    <td>POST /v1/:resource</td>
    <td>Create a resource of this type</td>
  </tr>
  <tr>
    <td>PATCH /v1/:resource/:id</td>
    <td>Update the resource by id</td>
  </tr>
  <tr>
    <td>DELETE /v1/:resource/:id</td>
    <td>Delete the resource by id</td>
  </tr>
</table>
<hr />

<h1 id=\"roles\">Roles</h1>
<p>The Access Tokens will have owner permission on the account</p>
<hr />

<h1 id=\"filters\">Filters</h1>
<p>
  Some of the list endpoints allow to filter results by certain conditions.
  Refer to specific resources to find out what criteria are allowed. Below is a
  list of the different conditions.
</p>

<h4 id=\"eq\"><code>$eq</code></h4>
<p>Find all results matching the attribute value specified.</p>
<div>
  <pre><code class=\"language-shell\" data-lang=\"shell\">GET /v1/example?filters[fieldName][$eq]=value</code></pre>
</div>
<p>Can also be simplified like this.</p>
<div>
  <pre><code class=\"language-shell\" data-lang=\"shell\">GET /v1/example?filters[fieldName]=value</code></pre>
</div>

<h4 id=\"neq\"><code>$neq</code></h4>
<p>Find all results not matching the attribute value specified.</p>
<div>
  <pre><code class=\"language-shell\" data-lang=\"shell\">GET /v1/example?filters[fieldName][$neq]=value</code></pre>
</div>

<h4 id=\"gt\"><code>$gt</code>, <code>$gte</code></h4>
<p>
  Find all results where the value is more (<code>$gt</code>) or more and equal
  (<code>$gte</code>) to a given value.
</p>
<div>
  <pre><code class=\"language-shell\" data-lang=\"shell\">GET /v1/example?filters[startDate][$gte]=2020-01-01</code></pre>
</div>
<hr />

<h4 id=\"lt\"><code>$lt</code>, <code>$lte</code></h4>
<p>
  Find all results where the value is less (<code>$lt</code>) or less and equal
  (<code>$lte</code>) to a given value.
</p>
<div>
  <pre><code class=\"language-shell\" data-lang=\"shell\">GET /v1/example?filters[startDate][$lte]=2020-01-01</code></pre>
</div>
<hr />

<h4 id=\"in\"><code>$in</code>, <code>$nin</code></h4>
<p>
  Find all results matching (<code>$in</code>) or not matching
  (<code>$nin</code>) any of the attribute values specified.
</p>
<div>
  <pre><code class=\"language-shell\" data-lang=\"shell\">GET /v1/example?filters[fieldName][$in][]=value1&filters[fieldName][$in][]=value2</code></pre>
</div>
<hr />

<h4 id=\"between\"><code>$between</code></h4>
<p>Find all results between two values specified.</p>
<div>
  <pre><code class=\"language-shell\" data-lang=\"shell\">GET /v1/example?filters[startDate][$between][]=2020-01-01&filters[startDate][$between][]=2020-12-31</code></pre>
</div>
<hr />

<h1 id=\"versioning\">Versioning</h1>
<p>
  Each version of the API is guaranteed to be compatible with the resources of
  the same version. When we make breaking changes to the API a new version will
  be published
</p>
<hr />

<h1 id=\"changelog\">Changelog</h1>
<h3>2023-12-20</h3>
<p>Field [updated] added for filter & select for Get Many Employments and Get Many Employees.</p>
<h3>2021-03-15</h3>
<p>First draft was published</p>
<hr />

# Authentication<a id="authentication"></a>

<!-- ReDoc-Inject: <security-definitions> -->


</div>

## Table of Contents<a id="table-of-contents"></a>

<!-- toc -->

- [Requirements](#requirements)
- [Installation](#installation)
- [Getting Started](#getting-started)
- [Async](#async)
- [Raw HTTP Response](#raw-http-response)
- [Reference](#reference)
  * [`alexishr.child.create_one`](#alexishrchildcreate_one)
  * [`alexishr.child.delete_child`](#alexishrchilddelete_child)
  * [`alexishr.child.get_many`](#alexishrchildget_many)
  * [`alexishr.child.get_one_child`](#alexishrchildget_one_child)
  * [`alexishr.child.replace_child_data`](#alexishrchildreplace_child_data)
  * [`alexishr.child.update_child_data`](#alexishrchildupdate_child_data)
  * [`alexishr.company.get_one`](#alexishrcompanyget_one)
  * [`alexishr.company.list_many_companies`](#alexishrcompanylist_many_companies)
  * [`alexishr.compensation.create_one_compensation`](#alexishrcompensationcreate_one_compensation)
  * [`alexishr.compensation.delete_one`](#alexishrcompensationdelete_one)
  * [`alexishr.compensation.get_many_compensations`](#alexishrcompensationget_many_compensations)
  * [`alexishr.compensation.get_one`](#alexishrcompensationget_one)
  * [`alexishr.compensation.replace_one_compensation`](#alexishrcompensationreplace_one_compensation)
  * [`alexishr.compensation.update_one`](#alexishrcompensationupdate_one)
  * [`alexishr.cost_center.create_one_cost_center`](#alexishrcost_centercreate_one_cost_center)
  * [`alexishr.cost_center.delete_one_cost_center`](#alexishrcost_centerdelete_one_cost_center)
  * [`alexishr.cost_center.get_many`](#alexishrcost_centerget_many)
  * [`alexishr.cost_center.get_one_cost_center`](#alexishrcost_centerget_one_cost_center)
  * [`alexishr.cost_center.replace_one_cost_center`](#alexishrcost_centerreplace_one_cost_center)
  * [`alexishr.cost_center.update_one_cost_center`](#alexishrcost_centerupdate_one_cost_center)
  * [`alexishr.department.create_one`](#alexishrdepartmentcreate_one)
  * [`alexishr.department.delete_one_department`](#alexishrdepartmentdelete_one_department)
  * [`alexishr.department.get_one`](#alexishrdepartmentget_one)
  * [`alexishr.department.list_many_departments`](#alexishrdepartmentlist_many_departments)
  * [`alexishr.department.replace_one`](#alexishrdepartmentreplace_one)
  * [`alexishr.department.update_one_department`](#alexishrdepartmentupdate_one_department)
  * [`alexishr.employee.create_one_employee`](#alexishremployeecreate_one_employee)
  * [`alexishr.employee.get_one`](#alexishremployeeget_one)
  * [`alexishr.employee.list_many_employees`](#alexishremployeelist_many_employees)
  * [`alexishr.employee.remove_employee`](#alexishremployeeremove_employee)
  * [`alexishr.employee.replace_one_employee`](#alexishremployeereplace_one_employee)
  * [`alexishr.employee.update_one`](#alexishremployeeupdate_one)
  * [`alexishr.employee_team_reference.create_one_employee_team_reference`](#alexishremployee_team_referencecreate_one_employee_team_reference)
  * [`alexishr.employee_team_reference.delete_one`](#alexishremployee_team_referencedelete_one)
  * [`alexishr.employee_team_reference.get_many`](#alexishremployee_team_referenceget_many)
  * [`alexishr.employee_team_reference.get_one_employee_team_reference`](#alexishremployee_team_referenceget_one_employee_team_reference)
  * [`alexishr.employee_team_reference.replace_one`](#alexishremployee_team_referencereplace_one)
  * [`alexishr.employee_team_reference.update_one_employee_team_reference`](#alexishremployee_team_referenceupdate_one_employee_team_reference)
  * [`alexishr.employment.create_one_employment`](#alexishremploymentcreate_one_employment)
  * [`alexishr.employment.get_one`](#alexishremploymentget_one)
  * [`alexishr.employment.list_many_employments`](#alexishremploymentlist_many_employments)
  * [`alexishr.employment.remove_one`](#alexishremploymentremove_one)
  * [`alexishr.employment.replace_one`](#alexishremploymentreplace_one)
  * [`alexishr.employment.update_employment_data`](#alexishremploymentupdate_employment_data)
  * [`alexishr.employment_type.create_one_employment_type`](#alexishremployment_typecreate_one_employment_type)
  * [`alexishr.employment_type.delete_one_type`](#alexishremployment_typedelete_one_type)
  * [`alexishr.employment_type.get_many_employment_types`](#alexishremployment_typeget_many_employment_types)
  * [`alexishr.employment_type.get_one`](#alexishremployment_typeget_one)
  * [`alexishr.employment_type.update_one_employment_type`](#alexishremployment_typeupdate_one_employment_type)
  * [`alexishr.employment_type.update_one_employment_type_0`](#alexishremployment_typeupdate_one_employment_type_0)
  * [`alexishr.leave.create_one`](#alexishrleavecreate_one)
  * [`alexishr.leave.delete_one_leave`](#alexishrleavedelete_one_leave)
  * [`alexishr.leave.get_many_leaves`](#alexishrleaveget_many_leaves)
  * [`alexishr.leave.get_one_leave`](#alexishrleaveget_one_leave)
  * [`alexishr.leave.replace_one`](#alexishrleavereplace_one)
  * [`alexishr.leave.update_one_leave`](#alexishrleaveupdate_one_leave)
  * [`alexishr.leave_transaction.get_one_leave_transaction`](#alexishrleave_transactionget_one_leave_transaction)
  * [`alexishr.leave_transaction.list_many_transactions`](#alexishrleave_transactionlist_many_transactions)
  * [`alexishr.leave_type.create_one_leave_type`](#alexishrleave_typecreate_one_leave_type)
  * [`alexishr.leave_type.delete_one_leave_type`](#alexishrleave_typedelete_one_leave_type)
  * [`alexishr.leave_type.get_many_leave_types`](#alexishrleave_typeget_many_leave_types)
  * [`alexishr.leave_type.get_one_leave_type`](#alexishrleave_typeget_one_leave_type)
  * [`alexishr.leave_type.replace_leave_type`](#alexishrleave_typereplace_leave_type)
  * [`alexishr.leave_type.update_one_leave_type`](#alexishrleave_typeupdate_one_leave_type)
  * [`alexishr.office.create_one_office`](#alexishrofficecreate_one_office)
  * [`alexishr.office.delete_one`](#alexishrofficedelete_one)
  * [`alexishr.office.get_one_office`](#alexishrofficeget_one_office)
  * [`alexishr.office.list_many_offices`](#alexishrofficelist_many_offices)
  * [`alexishr.office.replace_one`](#alexishrofficereplace_one)
  * [`alexishr.office.update_one`](#alexishrofficeupdate_one)
  * [`alexishr.team.create_one_team`](#alexishrteamcreate_one_team)
  * [`alexishr.team.delete_one`](#alexishrteamdelete_one)
  * [`alexishr.team.get_one_team`](#alexishrteamget_one_team)
  * [`alexishr.team.list_teams`](#alexishrteamlist_teams)
  * [`alexishr.team.replace_team`](#alexishrteamreplace_team)
  * [`alexishr.team.update_team`](#alexishrteamupdate_team)
  * [`alexishr.timesheet.get`](#alexishrtimesheetget)
  * [`alexishr.timesheet.get_many`](#alexishrtimesheetget_many)
  * [`alexishr.timesheet_entry.create_one_entry`](#alexishrtimesheet_entrycreate_one_entry)
  * [`alexishr.timesheet_entry.delete_one_entry`](#alexishrtimesheet_entrydelete_one_entry)
  * [`alexishr.timesheet_entry.get_one_entry`](#alexishrtimesheet_entryget_one_entry)
  * [`alexishr.timesheet_entry.list_many_entries`](#alexishrtimesheet_entrylist_many_entries)
  * [`alexishr.timesheet_entry.update_one_entry`](#alexishrtimesheet_entryupdate_one_entry)
  * [`alexishr.timesheet_entry.update_one_entry_0`](#alexishrtimesheet_entryupdate_one_entry_0)
  * [`alexishr.timesheet_entry_type.get_one_timesheet_entry_type`](#alexishrtimesheet_entry_typeget_one_timesheet_entry_type)
  * [`alexishr.timesheet_entry_type.list_many_timesheet_entry_types`](#alexishrtimesheet_entry_typelist_many_timesheet_entry_types)
  * [`alexishr.work_week.create_one_workweek`](#alexishrwork_weekcreate_one_workweek)
  * [`alexishr.work_week.delete_one`](#alexishrwork_weekdelete_one)
  * [`alexishr.work_week.get_many`](#alexishrwork_weekget_many)
  * [`alexishr.work_week.get_one`](#alexishrwork_weekget_one)
  * [`alexishr.work_week.replace_one`](#alexishrwork_weekreplace_one)
  * [`alexishr.work_week.update_one`](#alexishrwork_weekupdate_one)

<!-- tocstop -->

## Requirements<a id="requirements"></a>

Python >=3.7

## Installation<a id="installation"></a>
<div align="center">
  <a href="https://konfigthis.com/sdk-sign-up?company=AlexisHR&language=Python">
    <img src="https://raw.githubusercontent.com/konfig-dev/brand-assets/HEAD/cta-images/python-cta.png" width="70%">
  </a>
</div>

## Getting Started<a id="getting-started"></a>

```python
from pprint import pprint
from alexis_hr_python_sdk import AlexisHr, ApiException

alexishr = AlexisHr(access_token="YOUR_BEARER_TOKEN")

try:
    # Create One Child
    create_one_response = alexishr.child.create_one(
        employee_id="507f1f77bcf86cd799439011",
        name="string_example",
        birthdate="1970-01-01T00:00:00.00Z",
    )
    print(create_one_response)
except ApiException as e:
    print("Exception when calling ChildApi.create_one: %s\n" % e)
    pprint(e.body)
    if e.status == 400:
        pprint(e.body["status_code"])
        pprint(e.body["message"])
        pprint(e.body["error"])
    if e.status == 401:
        pprint(e.body["status_code"])
        pprint(e.body["message"])
        pprint(e.body["error"])
    if e.status == 500:
        pprint(e.body["status_code"])
        pprint(e.body["message"])
        pprint(e.body["error"])
    if e.status == 403:
        pprint(e.body["status_code"])
        pprint(e.body["message"])
        pprint(e.body["error"])
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```

## Async<a id="async"></a>

`async` support is available by prepending `a` to any method.

```python
import asyncio
from pprint import pprint
from alexis_hr_python_sdk import AlexisHr, ApiException

alexishr = AlexisHr(access_token="YOUR_BEARER_TOKEN")


async def main():
    try:
        # Create One Child
        create_one_response = await alexishr.child.acreate_one(
            employee_id="507f1f77bcf86cd799439011",
            name="string_example",
            birthdate="1970-01-01T00:00:00.00Z",
        )
        print(create_one_response)
    except ApiException as e:
        print("Exception when calling ChildApi.create_one: %s\n" % e)
        pprint(e.body)
        if e.status == 400:
            pprint(e.body["status_code"])
            pprint(e.body["message"])
            pprint(e.body["error"])
        if e.status == 401:
            pprint(e.body["status_code"])
            pprint(e.body["message"])
            pprint(e.body["error"])
        if e.status == 500:
            pprint(e.body["status_code"])
            pprint(e.body["message"])
            pprint(e.body["error"])
        if e.status == 403:
            pprint(e.body["status_code"])
            pprint(e.body["message"])
            pprint(e.body["error"])
        pprint(e.headers)
        pprint(e.status)
        pprint(e.reason)
        pprint(e.round_trip_time)


asyncio.run(main())
```

## Raw HTTP Response<a id="raw-http-response"></a>

To access raw HTTP response values, use the `.raw` namespace.

```python
from pprint import pprint
from alexis_hr_python_sdk import AlexisHr, ApiException

alexishr = AlexisHr(access_token="YOUR_BEARER_TOKEN")

try:
    # Create One Child
    create_one_response = alexishr.child.raw.create_one(
        employee_id="507f1f77bcf86cd799439011",
        name="string_example",
        birthdate="1970-01-01T00:00:00.00Z",
    )
    pprint(create_one_response.body)
    pprint(create_one_response.body["status"])
    pprint(create_one_response.body["data"])
    pprint(create_one_response.headers)
    pprint(create_one_response.status)
    pprint(create_one_response.round_trip_time)
except ApiException as e:
    print("Exception when calling ChildApi.create_one: %s\n" % e)
    pprint(e.body)
    if e.status == 400:
        pprint(e.body["status_code"])
        pprint(e.body["message"])
        pprint(e.body["error"])
    if e.status == 401:
        pprint(e.body["status_code"])
        pprint(e.body["message"])
        pprint(e.body["error"])
    if e.status == 500:
        pprint(e.body["status_code"])
        pprint(e.body["message"])
        pprint(e.body["error"])
    if e.status == 403:
        pprint(e.body["status_code"])
        pprint(e.body["message"])
        pprint(e.body["error"])
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```


## Reference<a id="reference"></a>
### `alexishr.child.create_one`<a id="alexishrchildcreate_one"></a>

Create One Child

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_one_response = alexishr.child.create_one(
    employee_id="507f1f77bcf86cd799439011",
    name="string_example",
    birthdate="1970-01-01T00:00:00.00Z",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### employee_id: `str`<a id="employee_id-str"></a>

##### name: `str`<a id="name-str"></a>

##### birthdate: `datetime`<a id="birthdate-datetime"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CreateChildRequest`](./alexis_hr_python_sdk/type/create_child_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ChildResponseMapped`](./alexis_hr_python_sdk/pydantic/child_response_mapped.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/child` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `alexishr.child.delete_child`<a id="alexishrchilddelete_child"></a>

Delete One Child

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
delete_child_response = alexishr.child.delete_child(
    id="507f1f77bcf86cd799439011",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Resource Id

#### 🔄 Return<a id="🔄-return"></a>

[`EmptyResponseMapped`](./alexis_hr_python_sdk/pydantic/empty_response_mapped.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/child/{id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `alexishr.child.get_many`<a id="alexishrchildget_many"></a>

Get Many Children

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_many_response = alexishr.child.get_many(
    select=["string_example"],
    filters={},
    limit=1,
    offset=1,
    sort={
        "id": "asc",
        "employee_id": "asc",
        "name": "asc",
        "birthdate": "asc",
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### select: List[`str`]<a id="select-liststr"></a>

Select Child fields, comma-separated. (e.g. `select=id,firstName,lastName,workEmail`)

##### filters: [`Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`](./alexis_hr_python_sdk/type/typing_dict_str_typing_union_bool_date_datetime_dict_float_int_list_str_none.py)<a id="filters-dictstr-unionbool-date-datetime-dict-float-int-list-str-nonealexis_hr_python_sdktypetyping_dict_str_typing_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>

Filters conditions per field. (e.g. `filters[id][$eq]=507f1f77bcf86cd799439011`)

##### limit: `int`<a id="limit-int"></a>

Limit amount of received Children. (e.g. `limit=20`)

##### offset: `int`<a id="offset-int"></a>

Offset amount of received Children. (e.g. `offset=20`)

##### sort: [`Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`](./alexis_hr_python_sdk/type/typing_dict_str_typing_union_bool_date_datetime_dict_float_int_list_str_none.py)<a id="sort-dictstr-unionbool-date-datetime-dict-float-int-list-str-nonealexis_hr_python_sdktypetyping_dict_str_typing_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>

Sort received Children by field. (e.g. `sort[id]=asc`)

#### 🔄 Return<a id="🔄-return"></a>

[`ChildrenGetManyResponseMapped`](./alexis_hr_python_sdk/pydantic/children_get_many_response_mapped.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/child` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `alexishr.child.get_one_child`<a id="alexishrchildget_one_child"></a>

Get One Child

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_one_child_response = alexishr.child.get_one_child(
    id="507f1f77bcf86cd799439011",
    select=["string_example"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Resource Id

##### select: List[`str`]<a id="select-liststr"></a>

Select Child fields, comma-separated. (e.g. `select=id,firstName,lastName,workEmail`)

#### 🔄 Return<a id="🔄-return"></a>

[`ChildGetOneResponseMapped`](./alexis_hr_python_sdk/pydantic/child_get_one_response_mapped.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/child/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `alexishr.child.replace_child_data`<a id="alexishrchildreplace_child_data"></a>

Replace One Child

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
replace_child_data_response = alexishr.child.replace_child_data(
    name="string_example",
    birthdate="1970-01-01T00:00:00.00Z",
    id="507f1f77bcf86cd799439011",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

##### birthdate: `datetime`<a id="birthdate-datetime"></a>

##### id: `str`<a id="id-str"></a>

Resource Id

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UpdateChildRequest`](./alexis_hr_python_sdk/type/update_child_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ChildResponseMapped`](./alexis_hr_python_sdk/pydantic/child_response_mapped.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/child/{id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `alexishr.child.update_child_data`<a id="alexishrchildupdate_child_data"></a>

Update One Child

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_child_data_response = alexishr.child.update_child_data(
    name="string_example",
    birthdate="1970-01-01T00:00:00.00Z",
    id="507f1f77bcf86cd799439011",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

##### birthdate: `datetime`<a id="birthdate-datetime"></a>

##### id: `str`<a id="id-str"></a>

Resource Id

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UpdateChildRequest`](./alexis_hr_python_sdk/type/update_child_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ChildResponseMapped`](./alexis_hr_python_sdk/pydantic/child_response_mapped.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/child/{id}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `alexishr.company.get_one`<a id="alexishrcompanyget_one"></a>

Get One Company

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_one_response = alexishr.company.get_one(
    id="507f1f77bcf86cd799439011",
    select=["string_example"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Resource Id

##### select: List[`str`]<a id="select-liststr"></a>

Select Company fields, comma-separated. (e.g. `select=id,firstName,lastName,workEmail`)

#### 🔄 Return<a id="🔄-return"></a>

[`CompanyGetOneResponseMapped`](./alexis_hr_python_sdk/pydantic/company_get_one_response_mapped.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/company/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `alexishr.company.list_many_companies`<a id="alexishrcompanylist_many_companies"></a>

Get Many Companies

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_many_companies_response = alexishr.company.list_many_companies(
    select=["string_example"],
    filters={},
    limit=1,
    offset=1,
    sort={
        "id": "asc",
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### select: List[`str`]<a id="select-liststr"></a>

Select Company fields, comma-separated. (e.g. `select=id,firstName,lastName,workEmail`)

##### filters: [`Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`](./alexis_hr_python_sdk/type/typing_dict_str_typing_union_bool_date_datetime_dict_float_int_list_str_none.py)<a id="filters-dictstr-unionbool-date-datetime-dict-float-int-list-str-nonealexis_hr_python_sdktypetyping_dict_str_typing_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>

Filters conditions per field. (e.g. `filters[id][$eq]=507f1f77bcf86cd799439011`)

##### limit: `int`<a id="limit-int"></a>

Limit amount of received Companies. (e.g. `limit=20`)

##### offset: `int`<a id="offset-int"></a>

Offset amount of received Companies. (e.g. `offset=20`)

##### sort: [`Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`](./alexis_hr_python_sdk/type/typing_dict_str_typing_union_bool_date_datetime_dict_float_int_list_str_none.py)<a id="sort-dictstr-unionbool-date-datetime-dict-float-int-list-str-nonealexis_hr_python_sdktypetyping_dict_str_typing_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>

Sort received Companies by field. (e.g. `sort[id]=asc`)

#### 🔄 Return<a id="🔄-return"></a>

[`CompaniesGetManyResponseMapped`](./alexis_hr_python_sdk/pydantic/companies_get_many_response_mapped.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/company` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `alexishr.compensation.create_one_compensation`<a id="alexishrcompensationcreate_one_compensation"></a>

Create One Compensation

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_one_compensation_response = alexishr.compensation.create_one_compensation(
    employee_id="507f1f77bcf86cd799439011",
    user_id="507f1f77bcf86cd799439011",
    amount=3.14,
    effective_date="string_example",
    currency="SEK",
    payout_day=25,
    payout_period="MONTHLY",
    payout_frequency="MONTH",
    paid_overtime=False,
    company_id="string_example",
    salary_schedule="ADVANCE",
    note="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### employee_id: `str`<a id="employee_id-str"></a>

##### user_id: `str`<a id="user_id-str"></a>

##### amount: `Union[int, float]`<a id="amount-unionint-float"></a>

##### effective_date: `str`<a id="effective_date-str"></a>

##### currency: `str`<a id="currency-str"></a>

##### payout_day: `Union[int, float]`<a id="payout_day-unionint-float"></a>

##### payout_period: `str`<a id="payout_period-str"></a>

##### payout_frequency: `str`<a id="payout_frequency-str"></a>

##### paid_overtime: `bool`<a id="paid_overtime-bool"></a>

##### company_id: `str`<a id="company_id-str"></a>

##### salary_schedule: `str`<a id="salary_schedule-str"></a>

##### note: `str`<a id="note-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CreateCompensationRequest`](./alexis_hr_python_sdk/type/create_compensation_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`CompensationResponseMapped`](./alexis_hr_python_sdk/pydantic/compensation_response_mapped.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/compensation` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `alexishr.compensation.delete_one`<a id="alexishrcompensationdelete_one"></a>

Delete One Compensation

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
delete_one_response = alexishr.compensation.delete_one(
    id="507f1f77bcf86cd799439011",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Resource Id

#### 🔄 Return<a id="🔄-return"></a>

[`EmptyResponseMapped`](./alexis_hr_python_sdk/pydantic/empty_response_mapped.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/compensation/{id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `alexishr.compensation.get_many_compensations`<a id="alexishrcompensationget_many_compensations"></a>

Get Many Compensations

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_many_compensations_response = alexishr.compensation.get_many_compensations(
    select=["string_example"],
    filters={},
    limit=1,
    offset=1,
    sort={
        "id": "asc",
        "employee_id": "asc",
        "company_id": "asc",
        "amount": "asc",
        "effective_date": "asc",
        "base_amount": "asc",
        "exchange_rate": "asc",
        "currency": "asc",
        "payout_day": "asc",
        "payout_period": "asc",
        "payout_frequency": "asc",
        "salary_schedule": "asc",
        "paid_overtime": "asc",
        "note": "asc",
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### select: List[`str`]<a id="select-liststr"></a>

Select Compensation fields, comma-separated. (e.g. `select=id,firstName,lastName,workEmail`)

##### filters: [`Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`](./alexis_hr_python_sdk/type/typing_dict_str_typing_union_bool_date_datetime_dict_float_int_list_str_none.py)<a id="filters-dictstr-unionbool-date-datetime-dict-float-int-list-str-nonealexis_hr_python_sdktypetyping_dict_str_typing_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>

Filters conditions per field. (e.g. `filters[id][$eq]=507f1f77bcf86cd799439011`)

##### limit: `int`<a id="limit-int"></a>

Limit amount of received Compensations. (e.g. `limit=20`)

##### offset: `int`<a id="offset-int"></a>

Offset amount of received Compensations. (e.g. `offset=20`)

##### sort: [`Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`](./alexis_hr_python_sdk/type/typing_dict_str_typing_union_bool_date_datetime_dict_float_int_list_str_none.py)<a id="sort-dictstr-unionbool-date-datetime-dict-float-int-list-str-nonealexis_hr_python_sdktypetyping_dict_str_typing_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>

Sort received Compensations by field. (e.g. `sort[id]=asc`)

#### 🔄 Return<a id="🔄-return"></a>

[`CompensationsGetManyResponseMapped`](./alexis_hr_python_sdk/pydantic/compensations_get_many_response_mapped.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/compensation` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `alexishr.compensation.get_one`<a id="alexishrcompensationget_one"></a>

Get One Compensation

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_one_response = alexishr.compensation.get_one(
    id="507f1f77bcf86cd799439011",
    select=["string_example"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Resource Id

##### select: List[`str`]<a id="select-liststr"></a>

Select Compensation fields, comma-separated. (e.g. `select=id,firstName,lastName,workEmail`)

#### 🔄 Return<a id="🔄-return"></a>

[`CompensationGetOneResponseMapped`](./alexis_hr_python_sdk/pydantic/compensation_get_one_response_mapped.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/compensation/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `alexishr.compensation.replace_one_compensation`<a id="alexishrcompensationreplace_one_compensation"></a>

Replace One Compensation

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
replace_one_compensation_response = alexishr.compensation.replace_one_compensation(
    id="507f1f77bcf86cd799439011",
    employee_id="507f1f77bcf86cd799439011",
    user_id="507f1f77bcf86cd799439011",
    amount=3.14,
    currency="SEK",
    payout_day=25,
    payout_period="MONTHLY",
    payout_frequency="MONTH",
    salary_schedule="ADVANCE",
    paid_overtime=False,
    note="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Resource Id

##### employee_id: `str`<a id="employee_id-str"></a>

##### user_id: `str`<a id="user_id-str"></a>

##### amount: `Union[int, float]`<a id="amount-unionint-float"></a>

##### currency: `str`<a id="currency-str"></a>

##### payout_day: `Union[int, float]`<a id="payout_day-unionint-float"></a>

##### payout_period: `str`<a id="payout_period-str"></a>

##### payout_frequency: `str`<a id="payout_frequency-str"></a>

##### salary_schedule: `str`<a id="salary_schedule-str"></a>

##### paid_overtime: `bool`<a id="paid_overtime-bool"></a>

##### note: `str`<a id="note-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UpdateCompensationRequest`](./alexis_hr_python_sdk/type/update_compensation_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`CompensationResponseMapped`](./alexis_hr_python_sdk/pydantic/compensation_response_mapped.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/compensation/{id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `alexishr.compensation.update_one`<a id="alexishrcompensationupdate_one"></a>

Update One Compensation

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_one_response = alexishr.compensation.update_one(
    id="507f1f77bcf86cd799439011",
    employee_id="507f1f77bcf86cd799439011",
    user_id="507f1f77bcf86cd799439011",
    amount=3.14,
    currency="SEK",
    payout_day=25,
    payout_period="MONTHLY",
    payout_frequency="MONTH",
    salary_schedule="ADVANCE",
    paid_overtime=False,
    note="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Resource Id

##### employee_id: `str`<a id="employee_id-str"></a>

##### user_id: `str`<a id="user_id-str"></a>

##### amount: `Union[int, float]`<a id="amount-unionint-float"></a>

##### currency: `str`<a id="currency-str"></a>

##### payout_day: `Union[int, float]`<a id="payout_day-unionint-float"></a>

##### payout_period: `str`<a id="payout_period-str"></a>

##### payout_frequency: `str`<a id="payout_frequency-str"></a>

##### salary_schedule: `str`<a id="salary_schedule-str"></a>

##### paid_overtime: `bool`<a id="paid_overtime-bool"></a>

##### note: `str`<a id="note-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UpdateCompensationRequest`](./alexis_hr_python_sdk/type/update_compensation_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`CompensationResponseMapped`](./alexis_hr_python_sdk/pydantic/compensation_response_mapped.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/compensation/{id}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `alexishr.cost_center.create_one_cost_center`<a id="alexishrcost_centercreate_one_cost_center"></a>

Create One Cost Center

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_one_cost_center_response = alexishr.cost_center.create_one_cost_center(
    code="string_example",
    name="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### code: `str`<a id="code-str"></a>

##### name: `str`<a id="name-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CreateCostCenterRequest`](./alexis_hr_python_sdk/type/create_cost_center_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`CostCenterResponseMapped`](./alexis_hr_python_sdk/pydantic/cost_center_response_mapped.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/cost-center` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `alexishr.cost_center.delete_one_cost_center`<a id="alexishrcost_centerdelete_one_cost_center"></a>

Delete One Cost Center

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
delete_one_cost_center_response = alexishr.cost_center.delete_one_cost_center(
    id="507f1f77bcf86cd799439011",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Resource Id

#### 🔄 Return<a id="🔄-return"></a>

[`EmptyResponseMapped`](./alexis_hr_python_sdk/pydantic/empty_response_mapped.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/cost-center/{id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `alexishr.cost_center.get_many`<a id="alexishrcost_centerget_many"></a>

Get Many Cost Centers

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_many_response = alexishr.cost_center.get_many(
    select=["string_example"],
    filters={},
    limit=1,
    offset=1,
    sort={
        "id": "asc",
        "company_id": "asc",
        "code": "asc",
        "name": "asc",
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### select: List[`str`]<a id="select-liststr"></a>

Select Cost Center fields, comma-separated. (e.g. `select=id,firstName,lastName,workEmail`)

##### filters: [`Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`](./alexis_hr_python_sdk/type/typing_dict_str_typing_union_bool_date_datetime_dict_float_int_list_str_none.py)<a id="filters-dictstr-unionbool-date-datetime-dict-float-int-list-str-nonealexis_hr_python_sdktypetyping_dict_str_typing_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>

Filters conditions per field. (e.g. `filters[id][$eq]=507f1f77bcf86cd799439011`)

##### limit: `int`<a id="limit-int"></a>

Limit amount of received Cost Centers. (e.g. `limit=20`)

##### offset: `int`<a id="offset-int"></a>

Offset amount of received Cost Centers. (e.g. `offset=20`)

##### sort: [`Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`](./alexis_hr_python_sdk/type/typing_dict_str_typing_union_bool_date_datetime_dict_float_int_list_str_none.py)<a id="sort-dictstr-unionbool-date-datetime-dict-float-int-list-str-nonealexis_hr_python_sdktypetyping_dict_str_typing_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>

Sort received Cost Centers by field. (e.g. `sort[id]=asc`)

#### 🔄 Return<a id="🔄-return"></a>

[`CostCentersGetManyResponseMapped`](./alexis_hr_python_sdk/pydantic/cost_centers_get_many_response_mapped.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/cost-center` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `alexishr.cost_center.get_one_cost_center`<a id="alexishrcost_centerget_one_cost_center"></a>

Get One Cost Center

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_one_cost_center_response = alexishr.cost_center.get_one_cost_center(
    id="507f1f77bcf86cd799439011",
    select=["string_example"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Resource Id

##### select: List[`str`]<a id="select-liststr"></a>

Select Cost Center fields, comma-separated. (e.g. `select=id,firstName,lastName,workEmail`)

#### 🔄 Return<a id="🔄-return"></a>

[`CostCenterGetOneResponseMapped`](./alexis_hr_python_sdk/pydantic/cost_center_get_one_response_mapped.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/cost-center/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `alexishr.cost_center.replace_one_cost_center`<a id="alexishrcost_centerreplace_one_cost_center"></a>

Replace One Cost Center

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
replace_one_cost_center_response = alexishr.cost_center.replace_one_cost_center(
    id="507f1f77bcf86cd799439011",
    code="string_example",
    name="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Resource Id

##### code: `str`<a id="code-str"></a>

##### name: `str`<a id="name-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UpdateCostCenterRequest`](./alexis_hr_python_sdk/type/update_cost_center_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`CostCenterResponseMapped`](./alexis_hr_python_sdk/pydantic/cost_center_response_mapped.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/cost-center/{id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `alexishr.cost_center.update_one_cost_center`<a id="alexishrcost_centerupdate_one_cost_center"></a>

Update One Cost Center

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_one_cost_center_response = alexishr.cost_center.update_one_cost_center(
    id="507f1f77bcf86cd799439011",
    code="string_example",
    name="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Resource Id

##### code: `str`<a id="code-str"></a>

##### name: `str`<a id="name-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UpdateCostCenterRequest`](./alexis_hr_python_sdk/type/update_cost_center_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`CostCenterResponseMapped`](./alexis_hr_python_sdk/pydantic/cost_center_response_mapped.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/cost-center/{id}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `alexishr.department.create_one`<a id="alexishrdepartmentcreate_one"></a>

Create One Department

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_one_response = alexishr.department.create_one(
    name="string_example",
    description="string_example",
    cost_center_id="string_example",
    parent_id="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

##### description: `str`<a id="description-str"></a>

##### cost_center_id: `str`<a id="cost_center_id-str"></a>

##### parent_id: `str`<a id="parent_id-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CreateDepartmentRequest`](./alexis_hr_python_sdk/type/create_department_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`DepartmentResponseMapped`](./alexis_hr_python_sdk/pydantic/department_response_mapped.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/department` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `alexishr.department.delete_one_department`<a id="alexishrdepartmentdelete_one_department"></a>

Delete One Department

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
delete_one_department_response = alexishr.department.delete_one_department(
    id="507f1f77bcf86cd799439011",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Resource Id

#### 🔄 Return<a id="🔄-return"></a>

[`EmptyResponseMapped`](./alexis_hr_python_sdk/pydantic/empty_response_mapped.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/department/{id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `alexishr.department.get_one`<a id="alexishrdepartmentget_one"></a>

Get One Department

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_one_response = alexishr.department.get_one(
    id="507f1f77bcf86cd799439011",
    select=["string_example"],
    relations=["string_example"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Resource Id

##### select: List[`str`]<a id="select-liststr"></a>

Select Department fields, comma-separated. (e.g. `select=id,firstName,lastName,workEmail`)

##### relations: List[`str`]<a id="relations-liststr"></a>

Select related Department resources, comma-separated. (e.g. `relations=office,department`)

#### 🔄 Return<a id="🔄-return"></a>

[`DepartmentGetOneResponseMapped`](./alexis_hr_python_sdk/pydantic/department_get_one_response_mapped.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/department/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `alexishr.department.list_many_departments`<a id="alexishrdepartmentlist_many_departments"></a>

Get Many Departments

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_many_departments_response = alexishr.department.list_many_departments(
    select=["string_example"],
    relations=["string_example"],
    filters={},
    limit=1,
    offset=1,
    sort={
        "id": "asc",
        "company_id": "asc",
        "name": "asc",
        "cost_center_id": "asc",
        "effective_cost_center_id": "asc",
        "parent_id": "asc",
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### select: List[`str`]<a id="select-liststr"></a>

Select Department fields, comma-separated. (e.g. `select=id,firstName,lastName,workEmail`)

##### relations: List[`str`]<a id="relations-liststr"></a>

Select related Department resources, comma-separated. (e.g. `relations=office,department`)

##### filters: [`Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`](./alexis_hr_python_sdk/type/typing_dict_str_typing_union_bool_date_datetime_dict_float_int_list_str_none.py)<a id="filters-dictstr-unionbool-date-datetime-dict-float-int-list-str-nonealexis_hr_python_sdktypetyping_dict_str_typing_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>

Filters conditions per field. (e.g. `filters[id][$eq]=507f1f77bcf86cd799439011`)

##### limit: `int`<a id="limit-int"></a>

Limit amount of received Departments. (e.g. `limit=20`)

##### offset: `int`<a id="offset-int"></a>

Offset amount of received Departments. (e.g. `offset=20`)

##### sort: [`Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`](./alexis_hr_python_sdk/type/typing_dict_str_typing_union_bool_date_datetime_dict_float_int_list_str_none.py)<a id="sort-dictstr-unionbool-date-datetime-dict-float-int-list-str-nonealexis_hr_python_sdktypetyping_dict_str_typing_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>

Sort received Departments by field. (e.g. `sort[id]=asc`)

#### 🔄 Return<a id="🔄-return"></a>

[`DepartmentsGetManyResponseMapped`](./alexis_hr_python_sdk/pydantic/departments_get_many_response_mapped.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/department` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `alexishr.department.replace_one`<a id="alexishrdepartmentreplace_one"></a>

Replace One Department

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
replace_one_response = alexishr.department.replace_one(
    name="string_example",
    id="507f1f77bcf86cd799439011",
    description="string_example",
    cost_center_id="string_example",
    parent_id="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

##### id: `str`<a id="id-str"></a>

Resource Id

##### description: `str`<a id="description-str"></a>

##### cost_center_id: `str`<a id="cost_center_id-str"></a>

##### parent_id: `str`<a id="parent_id-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UpdateDepartmentRequest`](./alexis_hr_python_sdk/type/update_department_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`DepartmentResponseMapped`](./alexis_hr_python_sdk/pydantic/department_response_mapped.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/department/{id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `alexishr.department.update_one_department`<a id="alexishrdepartmentupdate_one_department"></a>

Update One Department

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_one_department_response = alexishr.department.update_one_department(
    name="string_example",
    id="507f1f77bcf86cd799439011",
    description="string_example",
    cost_center_id="string_example",
    parent_id="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

##### id: `str`<a id="id-str"></a>

Resource Id

##### description: `str`<a id="description-str"></a>

##### cost_center_id: `str`<a id="cost_center_id-str"></a>

##### parent_id: `str`<a id="parent_id-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UpdateDepartmentRequest`](./alexis_hr_python_sdk/type/update_department_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`DepartmentResponseMapped`](./alexis_hr_python_sdk/pydantic/department_response_mapped.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/department/{id}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `alexishr.employee.create_one_employee`<a id="alexishremployeecreate_one_employee"></a>

Create One Employee

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_one_employee_response = alexishr.employee.create_one_employee(
    title="string_example",
    office_id="507f1f77bcf86cd799439011",
    manager_employee_id="507f1f77bcf86cd799439011",
    department_id="507f1f77bcf86cd799439011",
    cost_center_id="507f1f77bcf86cd799439011",
    user_name="john.doe@example.com",
    division="Division 1",
    organization="Organization 1",
    employee_number="1",
    tax={},
    work_email="string_example",
    work_phone="string_example",
    has_occupational_pension=True,
    private_email="string_example",
    first_name="string_example",
    last_name="string_example",
    ssn="string_example",
    private_phone="string_example",
    birth_date="string_example",
    avatar_url="string_example",
    nationality="string_example",
    gender="string_example",
    pronoun="string_example",
    bank_account={},
    home_address={},
    custom={},
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### title: `str`<a id="title-str"></a>

##### office_id: `str`<a id="office_id-str"></a>

##### manager_employee_id: `str`<a id="manager_employee_id-str"></a>

##### department_id: `str`<a id="department_id-str"></a>

##### cost_center_id: `str`<a id="cost_center_id-str"></a>

##### user_name: `str`<a id="user_name-str"></a>

##### division: `str`<a id="division-str"></a>

##### organization: `str`<a id="organization-str"></a>

##### employee_number: `str`<a id="employee_number-str"></a>

##### tax: [`EmployeeTaxRequest`](./alexis_hr_python_sdk/type/employee_tax_request.py)<a id="tax-employeetaxrequestalexis_hr_python_sdktypeemployee_tax_requestpy"></a>


##### work_email: `str`<a id="work_email-str"></a>

##### work_phone: `str`<a id="work_phone-str"></a>

##### has_occupational_pension: `bool`<a id="has_occupational_pension-bool"></a>

##### private_email: `str`<a id="private_email-str"></a>

##### first_name: `str`<a id="first_name-str"></a>

##### last_name: `str`<a id="last_name-str"></a>

##### ssn: `str`<a id="ssn-str"></a>

##### private_phone: `str`<a id="private_phone-str"></a>

##### birth_date: `str`<a id="birth_date-str"></a>

##### avatar_url: `str`<a id="avatar_url-str"></a>

##### nationality: `str`<a id="nationality-str"></a>

##### gender: `str`<a id="gender-str"></a>

##### pronoun: `str`<a id="pronoun-str"></a>

##### bank_account: [`BankAccountRequest`](./alexis_hr_python_sdk/type/bank_account_request.py)<a id="bank_account-bankaccountrequestalexis_hr_python_sdktypebank_account_requestpy"></a>


##### home_address: [`HomeAddressRequest`](./alexis_hr_python_sdk/type/home_address_request.py)<a id="home_address-homeaddressrequestalexis_hr_python_sdktypehome_address_requestpy"></a>


##### custom: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="custom-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CreateEmployeeRequest`](./alexis_hr_python_sdk/type/create_employee_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`EmployeeResponseMapped`](./alexis_hr_python_sdk/pydantic/employee_response_mapped.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/employee` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `alexishr.employee.get_one`<a id="alexishremployeeget_one"></a>

Get One Employee

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_one_response = alexishr.employee.get_one(
    id="507f1f77bcf86cd799439011",
    select=["string_example"],
    relations=["string_example"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Resource Id

##### select: List[`str`]<a id="select-liststr"></a>

Select Employee fields, comma-separated. (e.g. `select=id,firstName,lastName,workEmail`)

##### relations: List[`str`]<a id="relations-liststr"></a>

Select related Employee resources, comma-separated. (e.g. `relations=office,department`)

#### 🔄 Return<a id="🔄-return"></a>

[`EmployeeGetOneResponseMapped`](./alexis_hr_python_sdk/pydantic/employee_get_one_response_mapped.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/employee/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `alexishr.employee.list_many_employees`<a id="alexishremployeelist_many_employees"></a>

Get Many Employees

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_many_employees_response = alexishr.employee.list_many_employees(
    select=["string_example"],
    relations=["string_example"],
    filters={},
    limit=1,
    offset=1,
    sort={
        "title": "asc",
        "id": "asc",
        "active": "asc",
        "company_id": "asc",
        "office_id": "asc",
        "manager_employee_id": "asc",
        "department_id": "asc",
        "cost_center_id": "asc",
        "employment_id": "asc",
        "employment_type_id": "asc",
        "employment_country": "asc",
        "compensation_id": "asc",
        "user_id": "asc",
        "user_name": "asc",
        "division": "asc",
        "organization": "asc",
        "employee_number": "asc",
        "work_email": "asc",
        "work_phone": "asc",
        "work_phone_sanitized": "asc",
        "hire_date": "asc",
        "end_date": "asc",
        "has_occupational_pension": "asc",
        "private_email": "asc",
        "first_name": "asc",
        "last_name": "asc",
        "ssn": "asc",
        "private_phone": "asc",
        "private_phone_sanitized": "asc",
        "birth_date": "asc",
        "age": "asc",
        "nationality": "asc",
        "gender": "asc",
        "pronoun": "asc",
        "created": "asc",
        "updated": "asc",
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### select: List[`str`]<a id="select-liststr"></a>

Select Employee fields, comma-separated. (e.g. `select=id,firstName,lastName,workEmail`)

##### relations: List[`str`]<a id="relations-liststr"></a>

Select related Employee resources, comma-separated. (e.g. `relations=office,department`)

##### filters: [`Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`](./alexis_hr_python_sdk/type/typing_dict_str_typing_union_bool_date_datetime_dict_float_int_list_str_none.py)<a id="filters-dictstr-unionbool-date-datetime-dict-float-int-list-str-nonealexis_hr_python_sdktypetyping_dict_str_typing_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>

Filters conditions per field. (e.g. `filters[id][$eq]=507f1f77bcf86cd799439011`)

##### limit: `int`<a id="limit-int"></a>

Limit amount of received Employees. (e.g. `limit=20`)

##### offset: `int`<a id="offset-int"></a>

Offset amount of received Employees. (e.g. `offset=20`)

##### sort: [`Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`](./alexis_hr_python_sdk/type/typing_dict_str_typing_union_bool_date_datetime_dict_float_int_list_str_none.py)<a id="sort-dictstr-unionbool-date-datetime-dict-float-int-list-str-nonealexis_hr_python_sdktypetyping_dict_str_typing_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>

Sort received Employees by field. (e.g. `sort[id]=asc`)

#### 🔄 Return<a id="🔄-return"></a>

[`EmployeesGetManyResponseMapped`](./alexis_hr_python_sdk/pydantic/employees_get_many_response_mapped.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/employee` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `alexishr.employee.remove_employee`<a id="alexishremployeeremove_employee"></a>

Delete One Employee

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
remove_employee_response = alexishr.employee.remove_employee(
    id="507f1f77bcf86cd799439011",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Resource Id

#### 🔄 Return<a id="🔄-return"></a>

[`EmptyResponseMapped`](./alexis_hr_python_sdk/pydantic/empty_response_mapped.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/employee/{id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `alexishr.employee.replace_one_employee`<a id="alexishremployeereplace_one_employee"></a>

Replace One Employee

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
replace_one_employee_response = alexishr.employee.replace_one_employee(
    id="507f1f77bcf86cd799439011",
    title="string_example",
    office_id="507f1f77bcf86cd799439011",
    manager_employee_id="507f1f77bcf86cd799439011",
    department_id="507f1f77bcf86cd799439011",
    cost_center_id="507f1f77bcf86cd799439011",
    user_name="john.doe@example.com",
    division="Division 1",
    organization="Organization 1",
    employee_number="1",
    tax={},
    work_email="string_example",
    work_phone="string_example",
    has_occupational_pension=True,
    private_email="string_example",
    first_name="string_example",
    last_name="string_example",
    ssn="string_example",
    private_phone="string_example",
    birth_date="string_example",
    avatar_url="string_example",
    nationality="string_example",
    gender="string_example",
    pronoun="string_example",
    bank_account={},
    home_address={},
    custom={},
    active=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Resource Id

##### title: `str`<a id="title-str"></a>

##### office_id: `str`<a id="office_id-str"></a>

##### manager_employee_id: `str`<a id="manager_employee_id-str"></a>

##### department_id: `str`<a id="department_id-str"></a>

##### cost_center_id: `str`<a id="cost_center_id-str"></a>

##### user_name: `str`<a id="user_name-str"></a>

##### division: `str`<a id="division-str"></a>

##### organization: `str`<a id="organization-str"></a>

##### employee_number: `str`<a id="employee_number-str"></a>

##### tax: [`EmployeeTaxRequest`](./alexis_hr_python_sdk/type/employee_tax_request.py)<a id="tax-employeetaxrequestalexis_hr_python_sdktypeemployee_tax_requestpy"></a>


##### work_email: `str`<a id="work_email-str"></a>

##### work_phone: `str`<a id="work_phone-str"></a>

##### has_occupational_pension: `bool`<a id="has_occupational_pension-bool"></a>

##### private_email: `str`<a id="private_email-str"></a>

##### first_name: `str`<a id="first_name-str"></a>

##### last_name: `str`<a id="last_name-str"></a>

##### ssn: `str`<a id="ssn-str"></a>

##### private_phone: `str`<a id="private_phone-str"></a>

##### birth_date: `str`<a id="birth_date-str"></a>

##### avatar_url: `str`<a id="avatar_url-str"></a>

##### nationality: `str`<a id="nationality-str"></a>

##### gender: `str`<a id="gender-str"></a>

##### pronoun: `str`<a id="pronoun-str"></a>

##### bank_account: [`BankAccountRequest`](./alexis_hr_python_sdk/type/bank_account_request.py)<a id="bank_account-bankaccountrequestalexis_hr_python_sdktypebank_account_requestpy"></a>


##### home_address: [`HomeAddressRequest`](./alexis_hr_python_sdk/type/home_address_request.py)<a id="home_address-homeaddressrequestalexis_hr_python_sdktypehome_address_requestpy"></a>


##### custom: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="custom-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

##### active: `bool`<a id="active-bool"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UpdateEmployeeRequest`](./alexis_hr_python_sdk/type/update_employee_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`EmployeeResponseMapped`](./alexis_hr_python_sdk/pydantic/employee_response_mapped.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/employee/{id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `alexishr.employee.update_one`<a id="alexishremployeeupdate_one"></a>

Update One Employee

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_one_response = alexishr.employee.update_one(
    id="507f1f77bcf86cd799439011",
    title="string_example",
    office_id="507f1f77bcf86cd799439011",
    manager_employee_id="507f1f77bcf86cd799439011",
    department_id="507f1f77bcf86cd799439011",
    cost_center_id="507f1f77bcf86cd799439011",
    user_name="john.doe@example.com",
    division="Division 1",
    organization="Organization 1",
    employee_number="1",
    tax={},
    work_email="string_example",
    work_phone="string_example",
    has_occupational_pension=True,
    private_email="string_example",
    first_name="string_example",
    last_name="string_example",
    ssn="string_example",
    private_phone="string_example",
    birth_date="string_example",
    avatar_url="string_example",
    nationality="string_example",
    gender="string_example",
    pronoun="string_example",
    bank_account={},
    home_address={},
    custom={},
    active=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Resource Id

##### title: `str`<a id="title-str"></a>

##### office_id: `str`<a id="office_id-str"></a>

##### manager_employee_id: `str`<a id="manager_employee_id-str"></a>

##### department_id: `str`<a id="department_id-str"></a>

##### cost_center_id: `str`<a id="cost_center_id-str"></a>

##### user_name: `str`<a id="user_name-str"></a>

##### division: `str`<a id="division-str"></a>

##### organization: `str`<a id="organization-str"></a>

##### employee_number: `str`<a id="employee_number-str"></a>

##### tax: [`EmployeeTaxRequest`](./alexis_hr_python_sdk/type/employee_tax_request.py)<a id="tax-employeetaxrequestalexis_hr_python_sdktypeemployee_tax_requestpy"></a>


##### work_email: `str`<a id="work_email-str"></a>

##### work_phone: `str`<a id="work_phone-str"></a>

##### has_occupational_pension: `bool`<a id="has_occupational_pension-bool"></a>

##### private_email: `str`<a id="private_email-str"></a>

##### first_name: `str`<a id="first_name-str"></a>

##### last_name: `str`<a id="last_name-str"></a>

##### ssn: `str`<a id="ssn-str"></a>

##### private_phone: `str`<a id="private_phone-str"></a>

##### birth_date: `str`<a id="birth_date-str"></a>

##### avatar_url: `str`<a id="avatar_url-str"></a>

##### nationality: `str`<a id="nationality-str"></a>

##### gender: `str`<a id="gender-str"></a>

##### pronoun: `str`<a id="pronoun-str"></a>

##### bank_account: [`BankAccountRequest`](./alexis_hr_python_sdk/type/bank_account_request.py)<a id="bank_account-bankaccountrequestalexis_hr_python_sdktypebank_account_requestpy"></a>


##### home_address: [`HomeAddressRequest`](./alexis_hr_python_sdk/type/home_address_request.py)<a id="home_address-homeaddressrequestalexis_hr_python_sdktypehome_address_requestpy"></a>


##### custom: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="custom-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

##### active: `bool`<a id="active-bool"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UpdateEmployeeRequest`](./alexis_hr_python_sdk/type/update_employee_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`EmployeeResponseMapped`](./alexis_hr_python_sdk/pydantic/employee_response_mapped.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/employee/{id}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `alexishr.employee_team_reference.create_one_employee_team_reference`<a id="alexishremployee_team_referencecreate_one_employee_team_reference"></a>

Create One EmployeeTeamReference

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_one_employee_team_reference_response = (
    alexishr.employee_team_reference.create_one_employee_team_reference(
        team_id="507f1f77bcf86cd799439011",
        company_id="507f1f77bcf86cd799439011",
        employee_id="507f1f77bcf86cd799439011",
        user_id="507f1f77bcf86cd799439011",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### team_id: `str`<a id="team_id-str"></a>

##### company_id: `str`<a id="company_id-str"></a>

##### employee_id: `str`<a id="employee_id-str"></a>

##### user_id: `str`<a id="user_id-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CreateEmployeeTeamReferenceRequest`](./alexis_hr_python_sdk/type/create_employee_team_reference_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`EmployeeTeamReferenceResponseMapped`](./alexis_hr_python_sdk/pydantic/employee_team_reference_response_mapped.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/employee-team-reference` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `alexishr.employee_team_reference.delete_one`<a id="alexishremployee_team_referencedelete_one"></a>

Delete One EmployeeTeamReference

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
delete_one_response = alexishr.employee_team_reference.delete_one(
    id="507f1f77bcf86cd799439011",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Resource Id

#### 🔄 Return<a id="🔄-return"></a>

[`EmptyResponseMapped`](./alexis_hr_python_sdk/pydantic/empty_response_mapped.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/employee-team-reference/{id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `alexishr.employee_team_reference.get_many`<a id="alexishremployee_team_referenceget_many"></a>

Get Many EmployeeTeamReferences

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_many_response = alexishr.employee_team_reference.get_many(
    select=["string_example"],
    relations=["string_example"],
    filters={},
    limit=1,
    offset=1,
    sort={
        "id": "asc",
        "company_id": "asc",
        "team_id": "asc",
        "user_id": "asc",
        "employee_id": "asc",
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### select: List[`str`]<a id="select-liststr"></a>

Select EmployeeTeamReference fields, comma-separated. (e.g. `select=id,firstName,lastName,workEmail`)

##### relations: List[`str`]<a id="relations-liststr"></a>

Select related EmployeeTeamReference resources, comma-separated. (e.g. `relations=office,department`)

##### filters: [`Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`](./alexis_hr_python_sdk/type/typing_dict_str_typing_union_bool_date_datetime_dict_float_int_list_str_none.py)<a id="filters-dictstr-unionbool-date-datetime-dict-float-int-list-str-nonealexis_hr_python_sdktypetyping_dict_str_typing_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>

Filters conditions per field. (e.g. `filters[id][$eq]=507f1f77bcf86cd799439011`)

##### limit: `int`<a id="limit-int"></a>

Limit amount of received EmployeeTeamReferences. (e.g. `limit=20`)

##### offset: `int`<a id="offset-int"></a>

Offset amount of received EmployeeTeamReferences. (e.g. `offset=20`)

##### sort: [`Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`](./alexis_hr_python_sdk/type/typing_dict_str_typing_union_bool_date_datetime_dict_float_int_list_str_none.py)<a id="sort-dictstr-unionbool-date-datetime-dict-float-int-list-str-nonealexis_hr_python_sdktypetyping_dict_str_typing_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>

Sort received EmployeeTeamReferences by field. (e.g. `sort[id]=asc`)

#### 🔄 Return<a id="🔄-return"></a>

[`EmployeeTeamReferencesGetManyResponseMapped`](./alexis_hr_python_sdk/pydantic/employee_team_references_get_many_response_mapped.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/employee-team-reference` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `alexishr.employee_team_reference.get_one_employee_team_reference`<a id="alexishremployee_team_referenceget_one_employee_team_reference"></a>

Get One EmployeeTeamReference

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_one_employee_team_reference_response = (
    alexishr.employee_team_reference.get_one_employee_team_reference(
        id="507f1f77bcf86cd799439011",
        select=["string_example"],
        relations=["string_example"],
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Resource Id

##### select: List[`str`]<a id="select-liststr"></a>

Select EmployeeTeamReference fields, comma-separated. (e.g. `select=id,firstName,lastName,workEmail`)

##### relations: List[`str`]<a id="relations-liststr"></a>

Select related EmployeeTeamReference resources, comma-separated. (e.g. `relations=office,department`)

#### 🔄 Return<a id="🔄-return"></a>

[`EmployeeTeamReferenceGetOneResponseMapped`](./alexis_hr_python_sdk/pydantic/employee_team_reference_get_one_response_mapped.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/employee-team-reference/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `alexishr.employee_team_reference.replace_one`<a id="alexishremployee_team_referencereplace_one"></a>

Replace One EmployeeTeamReference

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
replace_one_response = alexishr.employee_team_reference.replace_one(
    id="507f1f77bcf86cd799439011",
    team_id="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Resource Id

##### team_id: `str`<a id="team_id-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UpdateEmployeeTeamReferenceRequest`](./alexis_hr_python_sdk/type/update_employee_team_reference_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`EmployeeTeamReferenceResponseMapped`](./alexis_hr_python_sdk/pydantic/employee_team_reference_response_mapped.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/employee-team-reference/{id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `alexishr.employee_team_reference.update_one_employee_team_reference`<a id="alexishremployee_team_referenceupdate_one_employee_team_reference"></a>

Update One EmployeeTeamReference

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_one_employee_team_reference_response = (
    alexishr.employee_team_reference.update_one_employee_team_reference(
        id="507f1f77bcf86cd799439011",
        team_id="string_example",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Resource Id

##### team_id: `str`<a id="team_id-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UpdateEmployeeTeamReferenceRequest`](./alexis_hr_python_sdk/type/update_employee_team_reference_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`EmployeeTeamReferenceResponseMapped`](./alexis_hr_python_sdk/pydantic/employee_team_reference_response_mapped.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/employee-team-reference/{id}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `alexishr.employment.create_one_employment`<a id="alexishremploymentcreate_one_employment"></a>

Create One Employment

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_one_employment_response = alexishr.employment.create_one_employment(
    employee_id="507f1f77bcf86cd799439011",
    user_id="507f1f77bcf86cd799439011",
    type_id="507f1f77bcf86cd799439011",
    start_date="1970-01-01T00:00:00.00Z",
    terminated=True,
    rate=3.14,
    country="SE",
    end_date="1970-01-01T00:00:00.00Z",
    effective_end_date="1970-01-01T00:00:00.00Z",
    note="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### employee_id: `str`<a id="employee_id-str"></a>

##### user_id: `str`<a id="user_id-str"></a>

##### type_id: `str`<a id="type_id-str"></a>

##### start_date: `datetime`<a id="start_date-datetime"></a>

##### terminated: `bool`<a id="terminated-bool"></a>

##### rate: `Union[int, float]`<a id="rate-unionint-float"></a>

##### country: `str`<a id="country-str"></a>

##### end_date: `datetime`<a id="end_date-datetime"></a>

##### effective_end_date: `datetime`<a id="effective_end_date-datetime"></a>

##### note: `str`<a id="note-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CreateEmploymentRequest`](./alexis_hr_python_sdk/type/create_employment_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`EmploymentResponseMapped`](./alexis_hr_python_sdk/pydantic/employment_response_mapped.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/employment` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `alexishr.employment.get_one`<a id="alexishremploymentget_one"></a>

Get One Employment

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_one_response = alexishr.employment.get_one(
    id="507f1f77bcf86cd799439011",
    select=["string_example"],
    relations=["string_example"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Resource Id

##### select: List[`str`]<a id="select-liststr"></a>

Select Employment fields, comma-separated. (e.g. `select=id,firstName,lastName,workEmail`)

##### relations: List[`str`]<a id="relations-liststr"></a>

Select related Employment resources, comma-separated. (e.g. `relations=office,department`)

#### 🔄 Return<a id="🔄-return"></a>

[`EmploymentGetOneResponseMapped`](./alexis_hr_python_sdk/pydantic/employment_get_one_response_mapped.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/employment/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `alexishr.employment.list_many_employments`<a id="alexishremploymentlist_many_employments"></a>

Get Many Employments

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_many_employments_response = alexishr.employment.list_many_employments(
    select=["string_example"],
    relations=["string_example"],
    filters={},
    limit=1,
    offset=1,
    sort={
        "id": "asc",
        "company_id": "asc",
        "employee_id": "asc",
        "type_id": "asc",
        "start_date": "asc",
        "end_date": "asc",
        "updated": "asc",
        "effective_end_date": "asc",
        "terminated": "asc",
        "rate": "asc",
        "note": "asc",
        "country": "asc",
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### select: List[`str`]<a id="select-liststr"></a>

Select Employment fields, comma-separated. (e.g. `select=id,firstName,lastName,workEmail`)

##### relations: List[`str`]<a id="relations-liststr"></a>

Select related Employment resources, comma-separated. (e.g. `relations=office,department`)

##### filters: [`Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`](./alexis_hr_python_sdk/type/typing_dict_str_typing_union_bool_date_datetime_dict_float_int_list_str_none.py)<a id="filters-dictstr-unionbool-date-datetime-dict-float-int-list-str-nonealexis_hr_python_sdktypetyping_dict_str_typing_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>

Filters conditions per field. (e.g. `filters[id][$eq]=507f1f77bcf86cd799439011`)

##### limit: `int`<a id="limit-int"></a>

Limit amount of received Employments. (e.g. `limit=20`)

##### offset: `int`<a id="offset-int"></a>

Offset amount of received Employments. (e.g. `offset=20`)

##### sort: [`Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`](./alexis_hr_python_sdk/type/typing_dict_str_typing_union_bool_date_datetime_dict_float_int_list_str_none.py)<a id="sort-dictstr-unionbool-date-datetime-dict-float-int-list-str-nonealexis_hr_python_sdktypetyping_dict_str_typing_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>

Sort received Employments by field. (e.g. `sort[id]=asc`)

#### 🔄 Return<a id="🔄-return"></a>

[`EmploymentsGetManyResponseMapped`](./alexis_hr_python_sdk/pydantic/employments_get_many_response_mapped.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/employment` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `alexishr.employment.remove_one`<a id="alexishremploymentremove_one"></a>

Delete One Employment

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
remove_one_response = alexishr.employment.remove_one(
    id="507f1f77bcf86cd799439011",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Resource Id

#### 🔄 Return<a id="🔄-return"></a>

[`EmptyResponseMapped`](./alexis_hr_python_sdk/pydantic/empty_response_mapped.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/employment/{id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `alexishr.employment.replace_one`<a id="alexishremploymentreplace_one"></a>

Replace One Employment

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
replace_one_response = alexishr.employment.replace_one(
    id="507f1f77bcf86cd799439011",
    employee_id="507f1f77bcf86cd799439011",
    user_id="507f1f77bcf86cd799439011",
    type_id="507f1f77bcf86cd799439011",
    start_date="1970-01-01T00:00:00.00Z",
    end_date="1970-01-01T00:00:00.00Z",
    effective_end_date="1970-01-01T00:00:00.00Z",
    terminated=True,
    rate=3.14,
    note="string_example",
    country="SE",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Resource Id

##### employee_id: `str`<a id="employee_id-str"></a>

##### user_id: `str`<a id="user_id-str"></a>

##### type_id: `str`<a id="type_id-str"></a>

##### start_date: `datetime`<a id="start_date-datetime"></a>

##### end_date: `datetime`<a id="end_date-datetime"></a>

##### effective_end_date: `datetime`<a id="effective_end_date-datetime"></a>

##### terminated: `bool`<a id="terminated-bool"></a>

##### rate: `Union[int, float]`<a id="rate-unionint-float"></a>

##### note: `str`<a id="note-str"></a>

##### country: `str`<a id="country-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UpdateEmploymentRequest`](./alexis_hr_python_sdk/type/update_employment_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`EmploymentResponseMapped`](./alexis_hr_python_sdk/pydantic/employment_response_mapped.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/employment/{id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `alexishr.employment.update_employment_data`<a id="alexishremploymentupdate_employment_data"></a>

Update One Employment

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_employment_data_response = alexishr.employment.update_employment_data(
    id="507f1f77bcf86cd799439011",
    employee_id="507f1f77bcf86cd799439011",
    user_id="507f1f77bcf86cd799439011",
    type_id="507f1f77bcf86cd799439011",
    start_date="1970-01-01T00:00:00.00Z",
    end_date="1970-01-01T00:00:00.00Z",
    effective_end_date="1970-01-01T00:00:00.00Z",
    terminated=True,
    rate=3.14,
    note="string_example",
    country="SE",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Resource Id

##### employee_id: `str`<a id="employee_id-str"></a>

##### user_id: `str`<a id="user_id-str"></a>

##### type_id: `str`<a id="type_id-str"></a>

##### start_date: `datetime`<a id="start_date-datetime"></a>

##### end_date: `datetime`<a id="end_date-datetime"></a>

##### effective_end_date: `datetime`<a id="effective_end_date-datetime"></a>

##### terminated: `bool`<a id="terminated-bool"></a>

##### rate: `Union[int, float]`<a id="rate-unionint-float"></a>

##### note: `str`<a id="note-str"></a>

##### country: `str`<a id="country-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UpdateEmploymentRequest`](./alexis_hr_python_sdk/type/update_employment_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`EmploymentResponseMapped`](./alexis_hr_python_sdk/pydantic/employment_response_mapped.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/employment/{id}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `alexishr.employment_type.create_one_employment_type`<a id="alexishremployment_typecreate_one_employment_type"></a>

Create One Employment Type

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_one_employment_type_response = (
    alexishr.employment_type.create_one_employment_type(
        name="string_example",
        vacation=False,
        country="SE",
        max_months=12,
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

##### vacation: `bool`<a id="vacation-bool"></a>

##### country: `str`<a id="country-str"></a>

##### max_months: `Union[int, float]`<a id="max_months-unionint-float"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CreateEmploymentTypeRequest`](./alexis_hr_python_sdk/type/create_employment_type_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`EmploymentTypeResponseMapped`](./alexis_hr_python_sdk/pydantic/employment_type_response_mapped.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/employment-type` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `alexishr.employment_type.delete_one_type`<a id="alexishremployment_typedelete_one_type"></a>

Delete One Employment Type

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
delete_one_type_response = alexishr.employment_type.delete_one_type(
    id="507f1f77bcf86cd799439011",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Resource Id

#### 🔄 Return<a id="🔄-return"></a>

[`EmptyResponseMapped`](./alexis_hr_python_sdk/pydantic/empty_response_mapped.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/employment-type/{id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `alexishr.employment_type.get_many_employment_types`<a id="alexishremployment_typeget_many_employment_types"></a>

Get Many Employment Types

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_many_employment_types_response = alexishr.employment_type.get_many_employment_types(
    select=["string_example"],
    filters={},
    limit=1,
    offset=1,
    sort={
        "id": "asc",
        "company_id": "asc",
        "name": "asc",
        "vacation": "asc",
        "country": "asc",
        "max_months": "asc",
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### select: List[`str`]<a id="select-liststr"></a>

Select Employment Type fields, comma-separated. (e.g. `select=id,firstName,lastName,workEmail`)

##### filters: [`Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`](./alexis_hr_python_sdk/type/typing_dict_str_typing_union_bool_date_datetime_dict_float_int_list_str_none.py)<a id="filters-dictstr-unionbool-date-datetime-dict-float-int-list-str-nonealexis_hr_python_sdktypetyping_dict_str_typing_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>

Filters conditions per field. (e.g. `filters[id][$eq]=507f1f77bcf86cd799439011`)

##### limit: `int`<a id="limit-int"></a>

Limit amount of received Employment Types. (e.g. `limit=20`)

##### offset: `int`<a id="offset-int"></a>

Offset amount of received Employment Types. (e.g. `offset=20`)

##### sort: [`Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`](./alexis_hr_python_sdk/type/typing_dict_str_typing_union_bool_date_datetime_dict_float_int_list_str_none.py)<a id="sort-dictstr-unionbool-date-datetime-dict-float-int-list-str-nonealexis_hr_python_sdktypetyping_dict_str_typing_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>

Sort received Employment Types by field. (e.g. `sort[id]=asc`)

#### 🔄 Return<a id="🔄-return"></a>

[`EmploymentTypesGetManyResponseMapped`](./alexis_hr_python_sdk/pydantic/employment_types_get_many_response_mapped.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/employment-type` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `alexishr.employment_type.get_one`<a id="alexishremployment_typeget_one"></a>

Get One Employment Type

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_one_response = alexishr.employment_type.get_one(
    id="507f1f77bcf86cd799439011",
    select=["string_example"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Resource Id

##### select: List[`str`]<a id="select-liststr"></a>

Select Employment Type fields, comma-separated. (e.g. `select=id,firstName,lastName,workEmail`)

#### 🔄 Return<a id="🔄-return"></a>

[`EmploymentTypeGetOneResponseMapped`](./alexis_hr_python_sdk/pydantic/employment_type_get_one_response_mapped.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/employment-type/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `alexishr.employment_type.update_one_employment_type`<a id="alexishremployment_typeupdate_one_employment_type"></a>

Replace One Employment Type

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_one_employment_type_response = (
    alexishr.employment_type.update_one_employment_type(
        country="SE",
        id="507f1f77bcf86cd799439011",
        name="string_example",
        vacation=False,
        max_months=12,
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### country: `str`<a id="country-str"></a>

##### id: `str`<a id="id-str"></a>

Resource Id

##### name: `str`<a id="name-str"></a>

##### vacation: `bool`<a id="vacation-bool"></a>

##### max_months: `Union[int, float]`<a id="max_months-unionint-float"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UpdateEmploymentTypeRequest`](./alexis_hr_python_sdk/type/update_employment_type_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`EmploymentTypeResponseMapped`](./alexis_hr_python_sdk/pydantic/employment_type_response_mapped.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/employment-type/{id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `alexishr.employment_type.update_one_employment_type_0`<a id="alexishremployment_typeupdate_one_employment_type_0"></a>

Update One Employment Type

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_one_employment_type_0_response = (
    alexishr.employment_type.update_one_employment_type_0(
        country="SE",
        id="507f1f77bcf86cd799439011",
        name="string_example",
        vacation=False,
        max_months=12,
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### country: `str`<a id="country-str"></a>

##### id: `str`<a id="id-str"></a>

Resource Id

##### name: `str`<a id="name-str"></a>

##### vacation: `bool`<a id="vacation-bool"></a>

##### max_months: `Union[int, float]`<a id="max_months-unionint-float"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UpdateEmploymentTypeRequest`](./alexis_hr_python_sdk/type/update_employment_type_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`EmploymentTypeResponseMapped`](./alexis_hr_python_sdk/pydantic/employment_type_response_mapped.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/employment-type/{id}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `alexishr.leave.create_one`<a id="alexishrleavecreate_one"></a>

Create One Leave

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_one_response = alexishr.leave.create_one(
    employee_id="507f1f77bcf86cd799439011",
    type_id="507f1f77bcf86cd799439011",
    duration="minutes",
    start_date="1970-01-01T00:00:00.00Z",
    end_date="1970-01-01T00:00:00.00Z",
    description="string_example",
    child_id="507f1f77bcf86cd799439011",
    extent=50,
    morning={},
    afternoon={},
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### employee_id: `str`<a id="employee_id-str"></a>

##### type_id: `str`<a id="type_id-str"></a>

##### duration: `str`<a id="duration-str"></a>

##### start_date: `datetime`<a id="start_date-datetime"></a>

##### end_date: `datetime`<a id="end_date-datetime"></a>

##### description: `str`<a id="description-str"></a>

##### child_id: `str`<a id="child_id-str"></a>

##### extent: `Union[int, float]`<a id="extent-unionint-float"></a>

##### morning: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="morning-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

##### afternoon: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="afternoon-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CreateLeaveRequest`](./alexis_hr_python_sdk/type/create_leave_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`LeaveResponseMapped`](./alexis_hr_python_sdk/pydantic/leave_response_mapped.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/leave` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `alexishr.leave.delete_one_leave`<a id="alexishrleavedelete_one_leave"></a>

Delete One Leave

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
delete_one_leave_response = alexishr.leave.delete_one_leave(
    id="507f1f77bcf86cd799439011",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Resource Id

#### 🔄 Return<a id="🔄-return"></a>

[`EmptyResponseMapped`](./alexis_hr_python_sdk/pydantic/empty_response_mapped.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/leave/{id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `alexishr.leave.get_many_leaves`<a id="alexishrleaveget_many_leaves"></a>

Get Many Leaves

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_many_leaves_response = alexishr.leave.get_many_leaves(
    select=["string_example"],
    relations=["string_example"],
    filters={},
    limit=1,
    offset=1,
    sort={
        "id": "asc",
        "employee_id": "asc",
        "type_id": "asc",
        "status": "asc",
        "duration": "asc",
        "start_date": "asc",
        "end_date": "asc",
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### select: List[`str`]<a id="select-liststr"></a>

Select Leave fields, comma-separated. (e.g. `select=id,firstName,lastName,workEmail`)

##### relations: List[`str`]<a id="relations-liststr"></a>

Select related Leave resources, comma-separated. (e.g. `relations=office,department`)

##### filters: [`Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`](./alexis_hr_python_sdk/type/typing_dict_str_typing_union_bool_date_datetime_dict_float_int_list_str_none.py)<a id="filters-dictstr-unionbool-date-datetime-dict-float-int-list-str-nonealexis_hr_python_sdktypetyping_dict_str_typing_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>

Filters conditions per field. (e.g. `filters[id][$eq]=507f1f77bcf86cd799439011`)

##### limit: `int`<a id="limit-int"></a>

Limit amount of received Leaves. (e.g. `limit=20`)

##### offset: `int`<a id="offset-int"></a>

Offset amount of received Leaves. (e.g. `offset=20`)

##### sort: [`Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`](./alexis_hr_python_sdk/type/typing_dict_str_typing_union_bool_date_datetime_dict_float_int_list_str_none.py)<a id="sort-dictstr-unionbool-date-datetime-dict-float-int-list-str-nonealexis_hr_python_sdktypetyping_dict_str_typing_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>

Sort received Leaves by field. (e.g. `sort[id]=asc`)

#### 🔄 Return<a id="🔄-return"></a>

[`LeavesGetManyResponseMapped`](./alexis_hr_python_sdk/pydantic/leaves_get_many_response_mapped.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/leave` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `alexishr.leave.get_one_leave`<a id="alexishrleaveget_one_leave"></a>

Get One Leave

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_one_leave_response = alexishr.leave.get_one_leave(
    id="507f1f77bcf86cd799439011",
    select=["string_example"],
    relations=["string_example"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Resource Id

##### select: List[`str`]<a id="select-liststr"></a>

Select Leave fields, comma-separated. (e.g. `select=id,firstName,lastName,workEmail`)

##### relations: List[`str`]<a id="relations-liststr"></a>

Select related Leave resources, comma-separated. (e.g. `relations=office,department`)

#### 🔄 Return<a id="🔄-return"></a>

[`LeaveGetOneResponseMapped`](./alexis_hr_python_sdk/pydantic/leave_get_one_response_mapped.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/leave/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `alexishr.leave.replace_one`<a id="alexishrleavereplace_one"></a>

Replace One Leave

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
replace_one_response = alexishr.leave.replace_one(
    extent=50,
    id="507f1f77bcf86cd799439011",
    description="Description",
    child_id="507f1f77bcf86cd799439011",
    duration="minutes",
    start_date="1970-01-01T00:00:00.00Z",
    end_date="1970-01-01T00:00:00.00Z",
    morning=True,
    afternoon=True,
    status="string_example",
    approval_note="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### extent: `Union[int, float]`<a id="extent-unionint-float"></a>

##### id: `str`<a id="id-str"></a>

Resource Id

##### description: `str`<a id="description-str"></a>

##### child_id: `str`<a id="child_id-str"></a>

##### duration: `str`<a id="duration-str"></a>

##### start_date: `datetime`<a id="start_date-datetime"></a>

##### end_date: `datetime`<a id="end_date-datetime"></a>

##### morning: `bool`<a id="morning-bool"></a>

##### afternoon: `bool`<a id="afternoon-bool"></a>

##### status: `str`<a id="status-str"></a>

##### approval_note: `str`<a id="approval_note-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UpdateLeaveRequest`](./alexis_hr_python_sdk/type/update_leave_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`LeaveResponseMapped`](./alexis_hr_python_sdk/pydantic/leave_response_mapped.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/leave/{id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `alexishr.leave.update_one_leave`<a id="alexishrleaveupdate_one_leave"></a>

Update One Leave

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_one_leave_response = alexishr.leave.update_one_leave(
    extent=50,
    id="507f1f77bcf86cd799439011",
    description="Description",
    child_id="507f1f77bcf86cd799439011",
    duration="minutes",
    start_date="1970-01-01T00:00:00.00Z",
    end_date="1970-01-01T00:00:00.00Z",
    morning=True,
    afternoon=True,
    status="string_example",
    approval_note="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### extent: `Union[int, float]`<a id="extent-unionint-float"></a>

##### id: `str`<a id="id-str"></a>

Resource Id

##### description: `str`<a id="description-str"></a>

##### child_id: `str`<a id="child_id-str"></a>

##### duration: `str`<a id="duration-str"></a>

##### start_date: `datetime`<a id="start_date-datetime"></a>

##### end_date: `datetime`<a id="end_date-datetime"></a>

##### morning: `bool`<a id="morning-bool"></a>

##### afternoon: `bool`<a id="afternoon-bool"></a>

##### status: `str`<a id="status-str"></a>

##### approval_note: `str`<a id="approval_note-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UpdateLeaveRequest`](./alexis_hr_python_sdk/type/update_leave_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`LeaveResponseMapped`](./alexis_hr_python_sdk/pydantic/leave_response_mapped.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/leave/{id}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `alexishr.leave_transaction.get_one_leave_transaction`<a id="alexishrleave_transactionget_one_leave_transaction"></a>

Get One LeaveTransaction

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_one_leave_transaction_response = (
    alexishr.leave_transaction.get_one_leave_transaction(
        id="507f1f77bcf86cd799439011",
        select=["string_example"],
        relations=["string_example"],
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Resource Id

##### select: List[`str`]<a id="select-liststr"></a>

Select LeaveTransaction fields, comma-separated. (e.g. `select=id,firstName,lastName,workEmail`)

##### relations: List[`str`]<a id="relations-liststr"></a>

Select related LeaveTransaction resources, comma-separated. (e.g. `relations=office,department`)

#### 🔄 Return<a id="🔄-return"></a>

[`LeaveTransactionGetOneResponseMapped`](./alexis_hr_python_sdk/pydantic/leave_transaction_get_one_response_mapped.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/leave-transaction/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `alexishr.leave_transaction.list_many_transactions`<a id="alexishrleave_transactionlist_many_transactions"></a>

Get Many LeaveTransactions

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_many_transactions_response = alexishr.leave_transaction.list_many_transactions(
    select=["string_example"],
    relations=["string_example"],
    filters={},
    limit=1,
    offset=1,
    sort={
        "description": "asc",
        "id": "asc",
        "leave_type_id": "asc",
        "employee_id": "asc",
        "child_id": "asc",
        "date": "asc",
        "hours": "asc",
        "extent": "asc",
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### select: List[`str`]<a id="select-liststr"></a>

Select LeaveTransaction fields, comma-separated. (e.g. `select=id,firstName,lastName,workEmail`)

##### relations: List[`str`]<a id="relations-liststr"></a>

Select related LeaveTransaction resources, comma-separated. (e.g. `relations=office,department`)

##### filters: [`Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`](./alexis_hr_python_sdk/type/typing_dict_str_typing_union_bool_date_datetime_dict_float_int_list_str_none.py)<a id="filters-dictstr-unionbool-date-datetime-dict-float-int-list-str-nonealexis_hr_python_sdktypetyping_dict_str_typing_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>

Filters conditions per field. (e.g. `filters[id][$eq]=507f1f77bcf86cd799439011`)

##### limit: `int`<a id="limit-int"></a>

Limit amount of received LeaveTransactions. (e.g. `limit=20`)

##### offset: `int`<a id="offset-int"></a>

Offset amount of received LeaveTransactions. (e.g. `offset=20`)

##### sort: [`Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`](./alexis_hr_python_sdk/type/typing_dict_str_typing_union_bool_date_datetime_dict_float_int_list_str_none.py)<a id="sort-dictstr-unionbool-date-datetime-dict-float-int-list-str-nonealexis_hr_python_sdktypetyping_dict_str_typing_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>

Sort received LeaveTransactions by field. (e.g. `sort[id]=asc`)

#### 🔄 Return<a id="🔄-return"></a>

[`LeaveTransactionsGetManyResponseMapped`](./alexis_hr_python_sdk/pydantic/leave_transactions_get_many_response_mapped.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/leave-transaction` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `alexishr.leave_type.create_one_leave_type`<a id="alexishrleave_typecreate_one_leave_type"></a>

Create One LeaveType

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_one_leave_type_response = alexishr.leave_type.create_one_leave_type(
    name="string_example",
    kind="SICK_LEAVE",
    minimum_duration="DAY",
    deductible=True,
    paid=True,
    disabled=True,
    archived=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

##### kind: `str`<a id="kind-str"></a>

##### minimum_duration: `str`<a id="minimum_duration-str"></a>

##### deductible: `bool`<a id="deductible-bool"></a>

##### paid: `bool`<a id="paid-bool"></a>

##### disabled: `bool`<a id="disabled-bool"></a>

##### archived: `bool`<a id="archived-bool"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CreateLeaveTypeRequest`](./alexis_hr_python_sdk/type/create_leave_type_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`LeaveTypeResponseMapped`](./alexis_hr_python_sdk/pydantic/leave_type_response_mapped.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/leave-type` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `alexishr.leave_type.delete_one_leave_type`<a id="alexishrleave_typedelete_one_leave_type"></a>

Delete One LeaveType

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
delete_one_leave_type_response = alexishr.leave_type.delete_one_leave_type(
    id="507f1f77bcf86cd799439011",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Resource Id

#### 🔄 Return<a id="🔄-return"></a>

[`EmptyResponseMapped`](./alexis_hr_python_sdk/pydantic/empty_response_mapped.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/leave-type/{id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `alexishr.leave_type.get_many_leave_types`<a id="alexishrleave_typeget_many_leave_types"></a>

Get Many LeaveTypes

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_many_leave_types_response = alexishr.leave_type.get_many_leave_types(
    select=["string_example"],
    relations=["string_example"],
    filters={},
    limit=1,
    offset=1,
    sort={
        "id": "asc",
        "name": "asc",
        "kind": "asc",
        "minimum_duration": "asc",
        "deductible": "asc",
        "paid": "asc",
        "disabled": "asc",
        "archived": "asc",
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### select: List[`str`]<a id="select-liststr"></a>

Select LeaveType fields, comma-separated. (e.g. `select=id,firstName,lastName,workEmail`)

##### relations: List[`str`]<a id="relations-liststr"></a>

Select related LeaveType resources, comma-separated. (e.g. `relations=office,department`)

##### filters: [`Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`](./alexis_hr_python_sdk/type/typing_dict_str_typing_union_bool_date_datetime_dict_float_int_list_str_none.py)<a id="filters-dictstr-unionbool-date-datetime-dict-float-int-list-str-nonealexis_hr_python_sdktypetyping_dict_str_typing_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>

Filters conditions per field. (e.g. `filters[id][$eq]=507f1f77bcf86cd799439011`)

##### limit: `int`<a id="limit-int"></a>

Limit amount of received LeaveTypes. (e.g. `limit=20`)

##### offset: `int`<a id="offset-int"></a>

Offset amount of received LeaveTypes. (e.g. `offset=20`)

##### sort: [`Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`](./alexis_hr_python_sdk/type/typing_dict_str_typing_union_bool_date_datetime_dict_float_int_list_str_none.py)<a id="sort-dictstr-unionbool-date-datetime-dict-float-int-list-str-nonealexis_hr_python_sdktypetyping_dict_str_typing_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>

Sort received LeaveTypes by field. (e.g. `sort[id]=asc`)

#### 🔄 Return<a id="🔄-return"></a>

[`LeaveTypesGetManyResponseMapped`](./alexis_hr_python_sdk/pydantic/leave_types_get_many_response_mapped.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/leave-type` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `alexishr.leave_type.get_one_leave_type`<a id="alexishrleave_typeget_one_leave_type"></a>

Get One LeaveType

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_one_leave_type_response = alexishr.leave_type.get_one_leave_type(
    id="507f1f77bcf86cd799439011",
    select=["string_example"],
    relations=["string_example"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Resource Id

##### select: List[`str`]<a id="select-liststr"></a>

Select LeaveType fields, comma-separated. (e.g. `select=id,firstName,lastName,workEmail`)

##### relations: List[`str`]<a id="relations-liststr"></a>

Select related LeaveType resources, comma-separated. (e.g. `relations=office,department`)

#### 🔄 Return<a id="🔄-return"></a>

[`LeaveTypeGetOneResponseMapped`](./alexis_hr_python_sdk/pydantic/leave_type_get_one_response_mapped.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/leave-type/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `alexishr.leave_type.replace_leave_type`<a id="alexishrleave_typereplace_leave_type"></a>

Replace One LeaveType

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
replace_leave_type_response = alexishr.leave_type.replace_leave_type(
    id="507f1f77bcf86cd799439011",
    name="string_example",
    kind="SICK_LEAVE",
    minimum_duration="DAY",
    deductible=True,
    paid=True,
    disabled=True,
    archived=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Resource Id

##### name: `str`<a id="name-str"></a>

##### kind: `str`<a id="kind-str"></a>

##### minimum_duration: `str`<a id="minimum_duration-str"></a>

##### deductible: `bool`<a id="deductible-bool"></a>

##### paid: `bool`<a id="paid-bool"></a>

##### disabled: `bool`<a id="disabled-bool"></a>

##### archived: `bool`<a id="archived-bool"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UpdateLeaveTypeRequest`](./alexis_hr_python_sdk/type/update_leave_type_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`LeaveTypeResponseMapped`](./alexis_hr_python_sdk/pydantic/leave_type_response_mapped.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/leave-type/{id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `alexishr.leave_type.update_one_leave_type`<a id="alexishrleave_typeupdate_one_leave_type"></a>

Update One LeaveType

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_one_leave_type_response = alexishr.leave_type.update_one_leave_type(
    id="507f1f77bcf86cd799439011",
    name="string_example",
    kind="SICK_LEAVE",
    minimum_duration="DAY",
    deductible=True,
    paid=True,
    disabled=True,
    archived=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Resource Id

##### name: `str`<a id="name-str"></a>

##### kind: `str`<a id="kind-str"></a>

##### minimum_duration: `str`<a id="minimum_duration-str"></a>

##### deductible: `bool`<a id="deductible-bool"></a>

##### paid: `bool`<a id="paid-bool"></a>

##### disabled: `bool`<a id="disabled-bool"></a>

##### archived: `bool`<a id="archived-bool"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UpdateLeaveTypeRequest`](./alexis_hr_python_sdk/type/update_leave_type_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`LeaveTypeResponseMapped`](./alexis_hr_python_sdk/pydantic/leave_type_response_mapped.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/leave-type/{id}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `alexishr.office.create_one_office`<a id="alexishrofficecreate_one_office"></a>

Create One Office

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_one_office_response = alexishr.office.create_one_office(
    name="string_example",
    phone="string_example",
    email="string_example",
    timezone="Africa/Abidjan",
    cfar="string_example",
    scb="string_example",
    sni="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

##### phone: `str`<a id="phone-str"></a>

##### email: `str`<a id="email-str"></a>

##### timezone: `str`<a id="timezone-str"></a>

##### cfar: `str`<a id="cfar-str"></a>

##### scb: `str`<a id="scb-str"></a>

##### sni: `str`<a id="sni-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CreateOfficeRequest`](./alexis_hr_python_sdk/type/create_office_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`OfficeResponseMapped`](./alexis_hr_python_sdk/pydantic/office_response_mapped.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/office` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `alexishr.office.delete_one`<a id="alexishrofficedelete_one"></a>

Delete One Office

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
delete_one_response = alexishr.office.delete_one(
    id="507f1f77bcf86cd799439011",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Resource Id

#### 🔄 Return<a id="🔄-return"></a>

[`EmptyResponseMapped`](./alexis_hr_python_sdk/pydantic/empty_response_mapped.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/office/{id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `alexishr.office.get_one_office`<a id="alexishrofficeget_one_office"></a>

Get One Office

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_one_office_response = alexishr.office.get_one_office(
    id="507f1f77bcf86cd799439011",
    select=["string_example"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Resource Id

##### select: List[`str`]<a id="select-liststr"></a>

Select Office fields, comma-separated. (e.g. `select=id,firstName,lastName,workEmail`)

#### 🔄 Return<a id="🔄-return"></a>

[`OfficeGetOneResponseMapped`](./alexis_hr_python_sdk/pydantic/office_get_one_response_mapped.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/office/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `alexishr.office.list_many_offices`<a id="alexishrofficelist_many_offices"></a>

Get Many Offices

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_many_offices_response = alexishr.office.list_many_offices(
    select=["string_example"],
    filters={},
    limit=1,
    offset=1,
    sort={
        "id": "asc",
        "company_id": "asc",
        "name": "asc",
        "phone": "asc",
        "email": "asc",
        "timezone": "asc",
        "cfar": "asc",
        "scb": "asc",
        "sni": "asc",
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### select: List[`str`]<a id="select-liststr"></a>

Select Office fields, comma-separated. (e.g. `select=id,firstName,lastName,workEmail`)

##### filters: [`Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`](./alexis_hr_python_sdk/type/typing_dict_str_typing_union_bool_date_datetime_dict_float_int_list_str_none.py)<a id="filters-dictstr-unionbool-date-datetime-dict-float-int-list-str-nonealexis_hr_python_sdktypetyping_dict_str_typing_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>

Filters conditions per field. (e.g. `filters[id][$eq]=507f1f77bcf86cd799439011`)

##### limit: `int`<a id="limit-int"></a>

Limit amount of received Offices. (e.g. `limit=20`)

##### offset: `int`<a id="offset-int"></a>

Offset amount of received Offices. (e.g. `offset=20`)

##### sort: [`Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`](./alexis_hr_python_sdk/type/typing_dict_str_typing_union_bool_date_datetime_dict_float_int_list_str_none.py)<a id="sort-dictstr-unionbool-date-datetime-dict-float-int-list-str-nonealexis_hr_python_sdktypetyping_dict_str_typing_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>

Sort received Offices by field. (e.g. `sort[id]=asc`)

#### 🔄 Return<a id="🔄-return"></a>

[`OfficesGetManyResponseMapped`](./alexis_hr_python_sdk/pydantic/offices_get_many_response_mapped.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/office` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `alexishr.office.replace_one`<a id="alexishrofficereplace_one"></a>

Replace One Office

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
replace_one_response = alexishr.office.replace_one(
    id="507f1f77bcf86cd799439011",
    name="string_example",
    phone="string_example",
    email="string_example",
    timezone="Africa/Abidjan",
    cfar="string_example",
    scb="string_example",
    sni="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Resource Id

##### name: `str`<a id="name-str"></a>

##### phone: `str`<a id="phone-str"></a>

##### email: `str`<a id="email-str"></a>

##### timezone: `str`<a id="timezone-str"></a>

##### cfar: `str`<a id="cfar-str"></a>

##### scb: `str`<a id="scb-str"></a>

##### sni: `str`<a id="sni-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UpdateOfficeRequest`](./alexis_hr_python_sdk/type/update_office_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`OfficeResponseMapped`](./alexis_hr_python_sdk/pydantic/office_response_mapped.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/office/{id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `alexishr.office.update_one`<a id="alexishrofficeupdate_one"></a>

Update One Office

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_one_response = alexishr.office.update_one(
    id="507f1f77bcf86cd799439011",
    name="string_example",
    phone="string_example",
    email="string_example",
    timezone="Africa/Abidjan",
    cfar="string_example",
    scb="string_example",
    sni="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Resource Id

##### name: `str`<a id="name-str"></a>

##### phone: `str`<a id="phone-str"></a>

##### email: `str`<a id="email-str"></a>

##### timezone: `str`<a id="timezone-str"></a>

##### cfar: `str`<a id="cfar-str"></a>

##### scb: `str`<a id="scb-str"></a>

##### sni: `str`<a id="sni-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UpdateOfficeRequest`](./alexis_hr_python_sdk/type/update_office_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`OfficeResponseMapped`](./alexis_hr_python_sdk/pydantic/office_response_mapped.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/office/{id}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `alexishr.team.create_one_team`<a id="alexishrteamcreate_one_team"></a>

Create One Team

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_one_team_response = alexishr.team.create_one_team(
    name="Team 1",
    bg_color="#dee9fe",
    fg_color="#032f83",
    description="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

##### bg_color: `str`<a id="bg_color-str"></a>

##### fg_color: `str`<a id="fg_color-str"></a>

##### description: `str`<a id="description-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CreateTeamRequest`](./alexis_hr_python_sdk/type/create_team_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`TeamResponseMapped`](./alexis_hr_python_sdk/pydantic/team_response_mapped.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/team` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `alexishr.team.delete_one`<a id="alexishrteamdelete_one"></a>

Delete One Team

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
delete_one_response = alexishr.team.delete_one(
    id="507f1f77bcf86cd799439011",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Resource Id

#### 🔄 Return<a id="🔄-return"></a>

[`EmptyResponseMapped`](./alexis_hr_python_sdk/pydantic/empty_response_mapped.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/team/{id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `alexishr.team.get_one_team`<a id="alexishrteamget_one_team"></a>

Get One Team

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_one_team_response = alexishr.team.get_one_team(
    id="507f1f77bcf86cd799439011",
    select=["string_example"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Resource Id

##### select: List[`str`]<a id="select-liststr"></a>

Select Team fields, comma-separated. (e.g. `select=id,firstName,lastName,workEmail`)

#### 🔄 Return<a id="🔄-return"></a>

[`TeamGetOneResponseMapped`](./alexis_hr_python_sdk/pydantic/team_get_one_response_mapped.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/team/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `alexishr.team.list_teams`<a id="alexishrteamlist_teams"></a>

Get Many Teams

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_teams_response = alexishr.team.list_teams(
    select=["string_example"],
    filters={},
    limit=1,
    offset=1,
    sort={
        "description": "asc",
        "id": "asc",
        "company_id": "asc",
        "name": "asc",
        "bg_color": "asc",
        "fg_color": "asc",
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### select: List[`str`]<a id="select-liststr"></a>

Select Team fields, comma-separated. (e.g. `select=id,firstName,lastName,workEmail`)

##### filters: [`Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`](./alexis_hr_python_sdk/type/typing_dict_str_typing_union_bool_date_datetime_dict_float_int_list_str_none.py)<a id="filters-dictstr-unionbool-date-datetime-dict-float-int-list-str-nonealexis_hr_python_sdktypetyping_dict_str_typing_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>

Filters conditions per field. (e.g. `filters[id][$eq]=507f1f77bcf86cd799439011`)

##### limit: `int`<a id="limit-int"></a>

Limit amount of received Teams. (e.g. `limit=20`)

##### offset: `int`<a id="offset-int"></a>

Offset amount of received Teams. (e.g. `offset=20`)

##### sort: [`Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`](./alexis_hr_python_sdk/type/typing_dict_str_typing_union_bool_date_datetime_dict_float_int_list_str_none.py)<a id="sort-dictstr-unionbool-date-datetime-dict-float-int-list-str-nonealexis_hr_python_sdktypetyping_dict_str_typing_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>

Sort received Teams by field. (e.g. `sort[id]=asc`)

#### 🔄 Return<a id="🔄-return"></a>

[`TeamsGetManyResponseMapped`](./alexis_hr_python_sdk/pydantic/teams_get_many_response_mapped.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/team` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `alexishr.team.replace_team`<a id="alexishrteamreplace_team"></a>

Replace One Team

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
replace_team_response = alexishr.team.replace_team(
    id="507f1f77bcf86cd799439011",
    description="string_example",
    name="Team 1",
    bg_color="#dee9fe",
    fg_color="#032f83",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Resource Id

##### description: `str`<a id="description-str"></a>

##### name: `str`<a id="name-str"></a>

##### bg_color: `str`<a id="bg_color-str"></a>

##### fg_color: `str`<a id="fg_color-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UpdateTeamRequest`](./alexis_hr_python_sdk/type/update_team_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`TeamResponseMapped`](./alexis_hr_python_sdk/pydantic/team_response_mapped.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/team/{id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `alexishr.team.update_team`<a id="alexishrteamupdate_team"></a>

Update One Team

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_team_response = alexishr.team.update_team(
    id="507f1f77bcf86cd799439011",
    description="string_example",
    name="Team 1",
    bg_color="#dee9fe",
    fg_color="#032f83",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Resource Id

##### description: `str`<a id="description-str"></a>

##### name: `str`<a id="name-str"></a>

##### bg_color: `str`<a id="bg_color-str"></a>

##### fg_color: `str`<a id="fg_color-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UpdateTeamRequest`](./alexis_hr_python_sdk/type/update_team_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`TeamResponseMapped`](./alexis_hr_python_sdk/pydantic/team_response_mapped.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/team/{id}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `alexishr.timesheet.get`<a id="alexishrtimesheetget"></a>

Get One Timesheet

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_response = alexishr.timesheet.get(
    id="507f1f77bcf86cd799439011",
    select=["string_example"],
    relations=["string_example"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Resource Id

##### select: List[`str`]<a id="select-liststr"></a>

Select Timesheet fields, comma-separated. (e.g. `select=id,firstName,lastName,workEmail`)

##### relations: List[`str`]<a id="relations-liststr"></a>

Select related Timesheet resources, comma-separated. (e.g. `relations=office,department`)

#### 🔄 Return<a id="🔄-return"></a>

[`TimesheetGetOneResponseMapped`](./alexis_hr_python_sdk/pydantic/timesheet_get_one_response_mapped.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/timesheet/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `alexishr.timesheet.get_many`<a id="alexishrtimesheetget_many"></a>

Get Many Timesheets

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_many_response = alexishr.timesheet.get_many(
    select=["string_example"],
    relations=["string_example"],
    filters={},
    limit=1,
    offset=1,
    sort={
        "id": "asc",
        "status": "asc",
        "start_date": "asc",
        "end_date": "asc",
        "local_cut_off_date": "asc",
        "utc_cut_off_date": "asc",
        "approval_deadline_date": "asc",
        "interval": "asc",
        "note": "asc",
        "approver_employee_id": "asc",
        "employee_id": "asc",
        "submit_date": "asc",
        "approval_date": "asc",
        "rejected_date": "asc",
        "updated": "asc",
        "timezone": "asc",
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### select: List[`str`]<a id="select-liststr"></a>

Select Timesheet fields, comma-separated. (e.g. `select=id,firstName,lastName,workEmail`)

##### relations: List[`str`]<a id="relations-liststr"></a>

Select related Timesheet resources, comma-separated. (e.g. `relations=office,department`)

##### filters: [`Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`](./alexis_hr_python_sdk/type/typing_dict_str_typing_union_bool_date_datetime_dict_float_int_list_str_none.py)<a id="filters-dictstr-unionbool-date-datetime-dict-float-int-list-str-nonealexis_hr_python_sdktypetyping_dict_str_typing_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>

Filters conditions per field. (e.g. `filters[id][$eq]=507f1f77bcf86cd799439011`)

##### limit: `int`<a id="limit-int"></a>

Limit amount of received Timesheets. (e.g. `limit=20`)

##### offset: `int`<a id="offset-int"></a>

Offset amount of received Timesheets. (e.g. `offset=20`)

##### sort: [`Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`](./alexis_hr_python_sdk/type/typing_dict_str_typing_union_bool_date_datetime_dict_float_int_list_str_none.py)<a id="sort-dictstr-unionbool-date-datetime-dict-float-int-list-str-nonealexis_hr_python_sdktypetyping_dict_str_typing_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>

Sort received Timesheets by field. (e.g. `sort[id]=asc`)

#### 🔄 Return<a id="🔄-return"></a>

[`TimesheetsGetManyResponseMapped`](./alexis_hr_python_sdk/pydantic/timesheets_get_many_response_mapped.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/timesheet` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `alexishr.timesheet_entry.create_one_entry`<a id="alexishrtimesheet_entrycreate_one_entry"></a>

Create One TimesheetEntry

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_one_entry_response = alexishr.timesheet_entry.create_one_entry(
    type_id="507f1f77bcf86cd799439011",
    employee_id="507f1f77bcf86cd799439011",
    date="1970-01-01T00:00:00.00Z",
    minutes=3.14,
    note="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### type_id: `str`<a id="type_id-str"></a>

##### employee_id: `str`<a id="employee_id-str"></a>

##### date: `datetime`<a id="date-datetime"></a>

##### minutes: `Union[int, float]`<a id="minutes-unionint-float"></a>

##### note: `str`<a id="note-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CreateTimesheetEntryRequest`](./alexis_hr_python_sdk/type/create_timesheet_entry_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`TimesheetEntryResponseMapped`](./alexis_hr_python_sdk/pydantic/timesheet_entry_response_mapped.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/timesheet-entry` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `alexishr.timesheet_entry.delete_one_entry`<a id="alexishrtimesheet_entrydelete_one_entry"></a>

Delete One TimesheetEntry

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
delete_one_entry_response = alexishr.timesheet_entry.delete_one_entry(
    id="507f1f77bcf86cd799439011",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Resource Id

#### 🔄 Return<a id="🔄-return"></a>

[`EmptyResponseMapped`](./alexis_hr_python_sdk/pydantic/empty_response_mapped.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/timesheet-entry/{id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `alexishr.timesheet_entry.get_one_entry`<a id="alexishrtimesheet_entryget_one_entry"></a>

Get One TimesheetEntry

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_one_entry_response = alexishr.timesheet_entry.get_one_entry(
    id="507f1f77bcf86cd799439011",
    select=["string_example"],
    relations=["string_example"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Resource Id

##### select: List[`str`]<a id="select-liststr"></a>

Select TimesheetEntry fields, comma-separated. (e.g. `select=id,firstName,lastName,workEmail`)

##### relations: List[`str`]<a id="relations-liststr"></a>

Select related TimesheetEntry resources, comma-separated. (e.g. `relations=office,department`)

#### 🔄 Return<a id="🔄-return"></a>

[`TimesheetEntryGetOneResponseMapped`](./alexis_hr_python_sdk/pydantic/timesheet_entry_get_one_response_mapped.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/timesheet-entry/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `alexishr.timesheet_entry.list_many_entries`<a id="alexishrtimesheet_entrylist_many_entries"></a>

Get Many TimesheetEntries

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_many_entries_response = alexishr.timesheet_entry.list_many_entries(
    select=["string_example"],
    relations=["string_example"],
    filters={},
    limit=1,
    offset=1,
    sort={
        "id": "asc",
        "timesheet_id": "asc",
        "type_id": "asc",
        "employee_id": "asc",
        "date": "asc",
        "updated": "asc",
        "status": "asc",
        "minutes": "asc",
        "note": "asc",
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### select: List[`str`]<a id="select-liststr"></a>

Select TimesheetEntry fields, comma-separated. (e.g. `select=id,firstName,lastName,workEmail`)

##### relations: List[`str`]<a id="relations-liststr"></a>

Select related TimesheetEntry resources, comma-separated. (e.g. `relations=office,department`)

##### filters: [`Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`](./alexis_hr_python_sdk/type/typing_dict_str_typing_union_bool_date_datetime_dict_float_int_list_str_none.py)<a id="filters-dictstr-unionbool-date-datetime-dict-float-int-list-str-nonealexis_hr_python_sdktypetyping_dict_str_typing_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>

Filters conditions per field. (e.g. `filters[id][$eq]=507f1f77bcf86cd799439011`)

##### limit: `int`<a id="limit-int"></a>

Limit amount of received TimesheetEntries. (e.g. `limit=20`)

##### offset: `int`<a id="offset-int"></a>

Offset amount of received TimesheetEntries. (e.g. `offset=20`)

##### sort: [`Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`](./alexis_hr_python_sdk/type/typing_dict_str_typing_union_bool_date_datetime_dict_float_int_list_str_none.py)<a id="sort-dictstr-unionbool-date-datetime-dict-float-int-list-str-nonealexis_hr_python_sdktypetyping_dict_str_typing_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>

Sort received TimesheetEntries by field. (e.g. `sort[id]=asc`)

#### 🔄 Return<a id="🔄-return"></a>

[`TimesheetEntriesGetManyResponseMapped`](./alexis_hr_python_sdk/pydantic/timesheet_entries_get_many_response_mapped.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/timesheet-entry` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `alexishr.timesheet_entry.update_one_entry`<a id="alexishrtimesheet_entryupdate_one_entry"></a>

Replace One TimesheetEntry

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_one_entry_response = alexishr.timesheet_entry.update_one_entry(
    id="507f1f77bcf86cd799439011",
    type_id="507f1f77bcf86cd799439011",
    employee_id="507f1f77bcf86cd799439011",
    date="1970-01-01T00:00:00.00Z",
    minutes=3.14,
    note="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Resource Id

##### type_id: `str`<a id="type_id-str"></a>

##### employee_id: `str`<a id="employee_id-str"></a>

##### date: `datetime`<a id="date-datetime"></a>

##### minutes: `Union[int, float]`<a id="minutes-unionint-float"></a>

##### note: `str`<a id="note-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UpdateTimesheetEntryRequest`](./alexis_hr_python_sdk/type/update_timesheet_entry_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`TimesheetEntryResponseMapped`](./alexis_hr_python_sdk/pydantic/timesheet_entry_response_mapped.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/timesheet-entry/{id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `alexishr.timesheet_entry.update_one_entry_0`<a id="alexishrtimesheet_entryupdate_one_entry_0"></a>

Update One TimesheetEntry

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_one_entry_0_response = alexishr.timesheet_entry.update_one_entry_0(
    id="507f1f77bcf86cd799439011",
    type_id="507f1f77bcf86cd799439011",
    employee_id="507f1f77bcf86cd799439011",
    date="1970-01-01T00:00:00.00Z",
    minutes=3.14,
    note="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Resource Id

##### type_id: `str`<a id="type_id-str"></a>

##### employee_id: `str`<a id="employee_id-str"></a>

##### date: `datetime`<a id="date-datetime"></a>

##### minutes: `Union[int, float]`<a id="minutes-unionint-float"></a>

##### note: `str`<a id="note-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UpdateTimesheetEntryRequest`](./alexis_hr_python_sdk/type/update_timesheet_entry_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`TimesheetEntryResponseMapped`](./alexis_hr_python_sdk/pydantic/timesheet_entry_response_mapped.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/timesheet-entry/{id}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `alexishr.timesheet_entry_type.get_one_timesheet_entry_type`<a id="alexishrtimesheet_entry_typeget_one_timesheet_entry_type"></a>

Get One TimesheetEntryType

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_one_timesheet_entry_type_response = (
    alexishr.timesheet_entry_type.get_one_timesheet_entry_type(
        id="507f1f77bcf86cd799439011",
        select=["string_example"],
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Resource Id

##### select: List[`str`]<a id="select-liststr"></a>

Select TimesheetEntryType fields, comma-separated. (e.g. `select=id,firstName,lastName,workEmail`)

#### 🔄 Return<a id="🔄-return"></a>

[`TimesheetEntryTypeGetOneResponseMapped`](./alexis_hr_python_sdk/pydantic/timesheet_entry_type_get_one_response_mapped.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/timesheet-entry-type/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `alexishr.timesheet_entry_type.list_many_timesheet_entry_types`<a id="alexishrtimesheet_entry_typelist_many_timesheet_entry_types"></a>

Get Many TimesheetEntryTypes

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_many_timesheet_entry_types_response = (
    alexishr.timesheet_entry_type.list_many_timesheet_entry_types(
        select=["string_example"],
        filters={},
        limit=1,
        offset=1,
        sort={
            "id": "asc",
            "name": "asc",
            "kind": "asc",
        },
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### select: List[`str`]<a id="select-liststr"></a>

Select TimesheetEntryType fields, comma-separated. (e.g. `select=id,firstName,lastName,workEmail`)

##### filters: [`Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`](./alexis_hr_python_sdk/type/typing_dict_str_typing_union_bool_date_datetime_dict_float_int_list_str_none.py)<a id="filters-dictstr-unionbool-date-datetime-dict-float-int-list-str-nonealexis_hr_python_sdktypetyping_dict_str_typing_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>

Filters conditions per field. (e.g. `filters[id][$eq]=507f1f77bcf86cd799439011`)

##### limit: `int`<a id="limit-int"></a>

Limit amount of received TimesheetEntryTypes. (e.g. `limit=20`)

##### offset: `int`<a id="offset-int"></a>

Offset amount of received TimesheetEntryTypes. (e.g. `offset=20`)

##### sort: [`Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`](./alexis_hr_python_sdk/type/typing_dict_str_typing_union_bool_date_datetime_dict_float_int_list_str_none.py)<a id="sort-dictstr-unionbool-date-datetime-dict-float-int-list-str-nonealexis_hr_python_sdktypetyping_dict_str_typing_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>

Sort received TimesheetEntryTypes by field. (e.g. `sort[id]=asc`)

#### 🔄 Return<a id="🔄-return"></a>

[`TimesheetEntryTypesGetManyResponseMapped`](./alexis_hr_python_sdk/pydantic/timesheet_entry_types_get_many_response_mapped.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/timesheet-entry-type` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `alexishr.work_week.create_one_workweek`<a id="alexishrwork_weekcreate_one_workweek"></a>

Create One WorkWeek

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_one_workweek_response = alexishr.work_week.create_one_workweek(
    effective_from="1970-01-01T00:00:00.00Z",
    timezone="string_example",
    duration=3.14,
    monday={
        "working": True,
        "duration": 3.14,
        "shifts": [
            {
                "start_hour": 3.14,
                "start_minute": 3.14,
                "end_hour": 3.14,
                "end_minute": 3.14,
                "duration": 3.14,
            }
        ],
    },
    tuesday={
        "working": True,
        "duration": 3.14,
        "shifts": [
            {
                "start_hour": 3.14,
                "start_minute": 3.14,
                "end_hour": 3.14,
                "end_minute": 3.14,
                "duration": 3.14,
            }
        ],
    },
    wednesday={
        "working": True,
        "duration": 3.14,
        "shifts": [
            {
                "start_hour": 3.14,
                "start_minute": 3.14,
                "end_hour": 3.14,
                "end_minute": 3.14,
                "duration": 3.14,
            }
        ],
    },
    thursday={
        "working": True,
        "duration": 3.14,
        "shifts": [
            {
                "start_hour": 3.14,
                "start_minute": 3.14,
                "end_hour": 3.14,
                "end_minute": 3.14,
                "duration": 3.14,
            }
        ],
    },
    friday={
        "working": True,
        "duration": 3.14,
        "shifts": [
            {
                "start_hour": 3.14,
                "start_minute": 3.14,
                "end_hour": 3.14,
                "end_minute": 3.14,
                "duration": 3.14,
            }
        ],
    },
    saturday={
        "working": True,
        "duration": 3.14,
        "shifts": [
            {
                "start_hour": 3.14,
                "start_minute": 3.14,
                "end_hour": 3.14,
                "end_minute": 3.14,
                "duration": 3.14,
            }
        ],
    },
    sunday={
        "working": True,
        "duration": 3.14,
        "shifts": [
            {
                "start_hour": 3.14,
                "start_minute": 3.14,
                "end_hour": 3.14,
                "end_minute": 3.14,
                "duration": 3.14,
            }
        ],
    },
    employee_id="507f1f77bcf86cd799439011",
    office_id="507f1f77bcf86cd799439011",
    effective_to="1970-01-01T00:00:00.00Z",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### effective_from: `datetime`<a id="effective_from-datetime"></a>

##### timezone: `str`<a id="timezone-str"></a>

##### duration: `Union[int, float]`<a id="duration-unionint-float"></a>

##### monday: [`WorkWeekDayRequest`](./alexis_hr_python_sdk/type/work_week_day_request.py)<a id="monday-workweekdayrequestalexis_hr_python_sdktypework_week_day_requestpy"></a>


##### tuesday: [`WorkWeekDayRequest`](./alexis_hr_python_sdk/type/work_week_day_request.py)<a id="tuesday-workweekdayrequestalexis_hr_python_sdktypework_week_day_requestpy"></a>


##### wednesday: [`WorkWeekDayRequest`](./alexis_hr_python_sdk/type/work_week_day_request.py)<a id="wednesday-workweekdayrequestalexis_hr_python_sdktypework_week_day_requestpy"></a>


##### thursday: [`WorkWeekDayRequest`](./alexis_hr_python_sdk/type/work_week_day_request.py)<a id="thursday-workweekdayrequestalexis_hr_python_sdktypework_week_day_requestpy"></a>


##### friday: [`WorkWeekDayRequest`](./alexis_hr_python_sdk/type/work_week_day_request.py)<a id="friday-workweekdayrequestalexis_hr_python_sdktypework_week_day_requestpy"></a>


##### saturday: [`WorkWeekDayRequest`](./alexis_hr_python_sdk/type/work_week_day_request.py)<a id="saturday-workweekdayrequestalexis_hr_python_sdktypework_week_day_requestpy"></a>


##### sunday: [`WorkWeekDayRequest`](./alexis_hr_python_sdk/type/work_week_day_request.py)<a id="sunday-workweekdayrequestalexis_hr_python_sdktypework_week_day_requestpy"></a>


##### employee_id: `str`<a id="employee_id-str"></a>

##### office_id: `str`<a id="office_id-str"></a>

##### effective_to: `datetime`<a id="effective_to-datetime"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CreateWorkWeekRequest`](./alexis_hr_python_sdk/type/create_work_week_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`WorkWeekResponseMapped`](./alexis_hr_python_sdk/pydantic/work_week_response_mapped.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/work-week` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `alexishr.work_week.delete_one`<a id="alexishrwork_weekdelete_one"></a>

Delete One WorkWeek

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
delete_one_response = alexishr.work_week.delete_one(
    id="507f1f77bcf86cd799439011",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Resource Id

#### 🔄 Return<a id="🔄-return"></a>

[`EmptyResponseMapped`](./alexis_hr_python_sdk/pydantic/empty_response_mapped.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/work-week/{id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `alexishr.work_week.get_many`<a id="alexishrwork_weekget_many"></a>

Get Many WorkWeeks

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_many_response = alexishr.work_week.get_many(
    select=["string_example"],
    relations=["string_example"],
    filters={},
    limit=1,
    offset=1,
    sort={
        "id": "asc",
        "company_id": "asc",
        "office_id": "asc",
        "employee_id": "asc",
        "effective_from": "asc",
        "timezone": "asc",
        "duration": "asc",
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### select: List[`str`]<a id="select-liststr"></a>

Select WorkWeek fields, comma-separated. (e.g. `select=id,firstName,lastName,workEmail`)

##### relations: List[`str`]<a id="relations-liststr"></a>

Select related WorkWeek resources, comma-separated. (e.g. `relations=office,department`)

##### filters: [`Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`](./alexis_hr_python_sdk/type/typing_dict_str_typing_union_bool_date_datetime_dict_float_int_list_str_none.py)<a id="filters-dictstr-unionbool-date-datetime-dict-float-int-list-str-nonealexis_hr_python_sdktypetyping_dict_str_typing_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>

Filters conditions per field. (e.g. `filters[id][$eq]=507f1f77bcf86cd799439011`)

##### limit: `int`<a id="limit-int"></a>

Limit amount of received WorkWeeks. (e.g. `limit=20`)

##### offset: `int`<a id="offset-int"></a>

Offset amount of received WorkWeeks. (e.g. `offset=20`)

##### sort: [`Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`](./alexis_hr_python_sdk/type/typing_dict_str_typing_union_bool_date_datetime_dict_float_int_list_str_none.py)<a id="sort-dictstr-unionbool-date-datetime-dict-float-int-list-str-nonealexis_hr_python_sdktypetyping_dict_str_typing_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>

Sort received WorkWeeks by field. (e.g. `sort[id]=asc`)

#### 🔄 Return<a id="🔄-return"></a>

[`WorkWeeksGetManyResponseMapped`](./alexis_hr_python_sdk/pydantic/work_weeks_get_many_response_mapped.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/work-week` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `alexishr.work_week.get_one`<a id="alexishrwork_weekget_one"></a>

Get One WorkWeek

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_one_response = alexishr.work_week.get_one(
    id="507f1f77bcf86cd799439011",
    select=["string_example"],
    relations=["string_example"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Resource Id

##### select: List[`str`]<a id="select-liststr"></a>

Select WorkWeek fields, comma-separated. (e.g. `select=id,firstName,lastName,workEmail`)

##### relations: List[`str`]<a id="relations-liststr"></a>

Select related WorkWeek resources, comma-separated. (e.g. `relations=office,department`)

#### 🔄 Return<a id="🔄-return"></a>

[`WorkWeekGetOneResponseMapped`](./alexis_hr_python_sdk/pydantic/work_week_get_one_response_mapped.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/work-week/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `alexishr.work_week.replace_one`<a id="alexishrwork_weekreplace_one"></a>

Replace One WorkWeek

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
replace_one_response = alexishr.work_week.replace_one(
    id="507f1f77bcf86cd799439011",
    effective_to="1970-01-01T00:00:00.00Z",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Resource Id

##### effective_to: `datetime`<a id="effective_to-datetime"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UpdateWorkWeekRequest`](./alexis_hr_python_sdk/type/update_work_week_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`WorkWeekResponseMapped`](./alexis_hr_python_sdk/pydantic/work_week_response_mapped.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/work-week/{id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `alexishr.work_week.update_one`<a id="alexishrwork_weekupdate_one"></a>

Update One WorkWeek

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_one_response = alexishr.work_week.update_one(
    id="507f1f77bcf86cd799439011",
    effective_to="1970-01-01T00:00:00.00Z",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Resource Id

##### effective_to: `datetime`<a id="effective_to-datetime"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UpdateWorkWeekRequest`](./alexis_hr_python_sdk/type/update_work_week_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`WorkWeekResponseMapped`](./alexis_hr_python_sdk/pydantic/work_week_response_mapped.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/work-week/{id}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


## Author<a id="author"></a>
This Python package is automatically generated by [Konfig](https://konfigthis.com)
