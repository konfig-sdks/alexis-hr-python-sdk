# coding: utf-8

"""
    AlexisHR API

    <h1 id=\"introduction\">Introduction</h1>  <p>    AlexisHR API is currently in preview. This means that small, backward    incompatible changes might be introduced while in preview. The changes will be    documented and communicated.    <a      href=\"https://cdn.forms-content.sg-form.com/56c6a65c-90a2-11eb-a700-a6de1aea3a1a\"      target=\"_blank\"      ><button>Subscribe to updates</button></a    >  </p>    <h1 id=\"authentication\">Authentication</h1>  <pre class=\"click-to-expand-wrapper is-snippet-wrapper language-undefined\">  <code class=\"is-highlighted language-bash\">curl https://api.alexishr.com/v1/employee \\    -H \"Authorization: Bearer &lt;your_access_token&gt;\"</code>  </pre>  <p>    Authenticate your account when using the API by including your secret Access    Token in the request.    <a href=\"https://app.alexishr.com/access-tokens\">Manage your Access Tokens</a    >.  </p>  <p>    Authentication is performed by passing the Access Token in the Authorization    header.  </p>  <hr />    <h1 id=\"structure\">Structure</h1>  <p>    You will find the structure of the API to be highly uniform and consistent.    Typically every resource can be accessed via a top level endpoint, such as    <code>/v1/employee</code>. For every such resource, you can perform some of    the following operations:  </p>  <h2>Operations</h2>  <table>    <tr>      <td>GET /v1/:resource</td>      <td>List all objects of this type</td>    </tr>    <tr>      <td>GET /v1/:resource/:id</td>      <td>Retrieve a resource by id</td>    </tr>    <tr>      <td>POST /v1/:resource</td>      <td>Create a resource of this type</td>    </tr>    <tr>      <td>PATCH /v1/:resource/:id</td>      <td>Update the resource by id</td>    </tr>    <tr>      <td>DELETE /v1/:resource/:id</td>      <td>Delete the resource by id</td>    </tr>  </table>  <hr />    <h1 id=\"roles\">Roles</h1>  <p>The Access Tokens will have owner permission on the account</p>  <hr />    <h1 id=\"filters\">Filters</h1>  <p>    Some of the list endpoints allow to filter results by certain conditions.    Refer to specific resources to find out what criteria are allowed. Below is a    list of the different conditions.  </p>    <h4 id=\"eq\"><code>$eq</code></h4>  <p>Find all results matching the attribute value specified.</p>  <div>    <pre><code class=\"language-shell\" data-lang=\"shell\">GET /v1/example?filters[fieldName][$eq]=value</code></pre>  </div>  <p>Can also be simplified like this.</p>  <div>    <pre><code class=\"language-shell\" data-lang=\"shell\">GET /v1/example?filters[fieldName]=value</code></pre>  </div>    <h4 id=\"neq\"><code>$neq</code></h4>  <p>Find all results not matching the attribute value specified.</p>  <div>    <pre><code class=\"language-shell\" data-lang=\"shell\">GET /v1/example?filters[fieldName][$neq]=value</code></pre>  </div>    <h4 id=\"gt\"><code>$gt</code>, <code>$gte</code></h4>  <p>    Find all results where the value is more (<code>$gt</code>) or more and equal    (<code>$gte</code>) to a given value.  </p>  <div>    <pre><code class=\"language-shell\" data-lang=\"shell\">GET /v1/example?filters[startDate][$gte]=2020-01-01</code></pre>  </div>  <hr />    <h4 id=\"lt\"><code>$lt</code>, <code>$lte</code></h4>  <p>    Find all results where the value is less (<code>$lt</code>) or less and equal    (<code>$lte</code>) to a given value.  </p>  <div>    <pre><code class=\"language-shell\" data-lang=\"shell\">GET /v1/example?filters[startDate][$lte]=2020-01-01</code></pre>  </div>  <hr />    <h4 id=\"in\"><code>$in</code>, <code>$nin</code></h4>  <p>    Find all results matching (<code>$in</code>) or not matching    (<code>$nin</code>) any of the attribute values specified.  </p>  <div>    <pre><code class=\"language-shell\" data-lang=\"shell\">GET /v1/example?filters[fieldName][$in][]=value1&filters[fieldName][$in][]=value2</code></pre>  </div>  <hr />    <h4 id=\"between\"><code>$between</code></h4>  <p>Find all results between two values specified.</p>  <div>    <pre><code class=\"language-shell\" data-lang=\"shell\">GET /v1/example?filters[startDate][$between][]=2020-01-01&filters[startDate][$between][]=2020-12-31</code></pre>  </div>  <hr />    <h1 id=\"versioning\">Versioning</h1>  <p>    Each version of the API is guaranteed to be compatible with the resources of    the same version. When we make breaking changes to the API a new version will    be published  </p>  <hr />    <h1 id=\"changelog\">Changelog</h1>  <h3>2023-12-20</h3>  <p>Field [updated] added for filter & select for Get Many Employments and Get Many Employees.</p>  <h3>2021-03-15</h3>  <p>First draft was published</p>  <hr />   # Authentication  <!-- ReDoc-Inject: <security-definitions> -->

    The version of the OpenAPI document: v1-preview
    Contact: support@alexishr.com
    Generated by: https://konfigthis.com
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from alexis_hr_python_sdk import schemas  # noqa: F401


class EmployeeGetOneRelationsResponse(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            
            
            class office(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['OfficeResponse']:
                        return OfficeResponse
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['OfficeResponse'], typing.List['OfficeResponse']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'office':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'OfficeResponse':
                    return super().__getitem__(i)
            
            
            class costCenter(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['CostCenterResponse']:
                        return CostCenterResponse
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['CostCenterResponse'], typing.List['CostCenterResponse']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'costCenter':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'CostCenterResponse':
                    return super().__getitem__(i)
            
            
            class effectiveCostCenter(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['CostCenterResponse']:
                        return CostCenterResponse
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['CostCenterResponse'], typing.List['CostCenterResponse']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'effectiveCostCenter':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'CostCenterResponse':
                    return super().__getitem__(i)
            
            
            class child(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['ChildResponse']:
                        return ChildResponse
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['ChildResponse'], typing.List['ChildResponse']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'child':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'ChildResponse':
                    return super().__getitem__(i)
            
            
            class department(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['DepartmentResponse']:
                        return DepartmentResponse
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['DepartmentResponse'], typing.List['DepartmentResponse']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'department':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'DepartmentResponse':
                    return super().__getitem__(i)
            
            
            class emergencyContact(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['EmergencyContactResponse']:
                        return EmergencyContactResponse
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['EmergencyContactResponse'], typing.List['EmergencyContactResponse']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'emergencyContact':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'EmergencyContactResponse':
                    return super().__getitem__(i)
            
            
            class employment(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['EmploymentResponse']:
                        return EmploymentResponse
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['EmploymentResponse'], typing.List['EmploymentResponse']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'employment':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'EmploymentResponse':
                    return super().__getitem__(i)
            
            
            class employmentType(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['EmploymentTypeResponse']:
                        return EmploymentTypeResponse
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['EmploymentTypeResponse'], typing.List['EmploymentTypeResponse']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'employmentType':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'EmploymentTypeResponse':
                    return super().__getitem__(i)
            
            
            class compensation(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['CompensationResponse']:
                        return CompensationResponse
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['CompensationResponse'], typing.List['CompensationResponse']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'compensation':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'CompensationResponse':
                    return super().__getitem__(i)
            
            
            class managerEmployee(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['EmployeeResponse']:
                        return EmployeeResponse
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['EmployeeResponse'], typing.List['EmployeeResponse']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'managerEmployee':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'EmployeeResponse':
                    return super().__getitem__(i)
            
            
            class teamReference(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['EmployeeTeamReferenceResponse']:
                        return EmployeeTeamReferenceResponse
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['EmployeeTeamReferenceResponse'], typing.List['EmployeeTeamReferenceResponse']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'teamReference':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'EmployeeTeamReferenceResponse':
                    return super().__getitem__(i)
            __annotations__ = {
                "office": office,
                "costCenter": costCenter,
                "effectiveCostCenter": effectiveCostCenter,
                "child": child,
                "department": department,
                "emergencyContact": emergencyContact,
                "employment": employment,
                "employmentType": employmentType,
                "compensation": compensation,
                "managerEmployee": managerEmployee,
                "teamReference": teamReference,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["office"]) -> MetaOapg.properties.office: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["costCenter"]) -> MetaOapg.properties.costCenter: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["effectiveCostCenter"]) -> MetaOapg.properties.effectiveCostCenter: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["child"]) -> MetaOapg.properties.child: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["department"]) -> MetaOapg.properties.department: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["emergencyContact"]) -> MetaOapg.properties.emergencyContact: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["employment"]) -> MetaOapg.properties.employment: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["employmentType"]) -> MetaOapg.properties.employmentType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["compensation"]) -> MetaOapg.properties.compensation: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["managerEmployee"]) -> MetaOapg.properties.managerEmployee: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["teamReference"]) -> MetaOapg.properties.teamReference: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["office", "costCenter", "effectiveCostCenter", "child", "department", "emergencyContact", "employment", "employmentType", "compensation", "managerEmployee", "teamReference", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["office"]) -> typing.Union[MetaOapg.properties.office, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["costCenter"]) -> typing.Union[MetaOapg.properties.costCenter, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["effectiveCostCenter"]) -> typing.Union[MetaOapg.properties.effectiveCostCenter, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["child"]) -> typing.Union[MetaOapg.properties.child, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["department"]) -> typing.Union[MetaOapg.properties.department, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["emergencyContact"]) -> typing.Union[MetaOapg.properties.emergencyContact, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["employment"]) -> typing.Union[MetaOapg.properties.employment, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["employmentType"]) -> typing.Union[MetaOapg.properties.employmentType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["compensation"]) -> typing.Union[MetaOapg.properties.compensation, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["managerEmployee"]) -> typing.Union[MetaOapg.properties.managerEmployee, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["teamReference"]) -> typing.Union[MetaOapg.properties.teamReference, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["office", "costCenter", "effectiveCostCenter", "child", "department", "emergencyContact", "employment", "employmentType", "compensation", "managerEmployee", "teamReference", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        office: typing.Union[MetaOapg.properties.office, list, tuple, schemas.Unset] = schemas.unset,
        costCenter: typing.Union[MetaOapg.properties.costCenter, list, tuple, schemas.Unset] = schemas.unset,
        effectiveCostCenter: typing.Union[MetaOapg.properties.effectiveCostCenter, list, tuple, schemas.Unset] = schemas.unset,
        child: typing.Union[MetaOapg.properties.child, list, tuple, schemas.Unset] = schemas.unset,
        department: typing.Union[MetaOapg.properties.department, list, tuple, schemas.Unset] = schemas.unset,
        emergencyContact: typing.Union[MetaOapg.properties.emergencyContact, list, tuple, schemas.Unset] = schemas.unset,
        employment: typing.Union[MetaOapg.properties.employment, list, tuple, schemas.Unset] = schemas.unset,
        employmentType: typing.Union[MetaOapg.properties.employmentType, list, tuple, schemas.Unset] = schemas.unset,
        compensation: typing.Union[MetaOapg.properties.compensation, list, tuple, schemas.Unset] = schemas.unset,
        managerEmployee: typing.Union[MetaOapg.properties.managerEmployee, list, tuple, schemas.Unset] = schemas.unset,
        teamReference: typing.Union[MetaOapg.properties.teamReference, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'EmployeeGetOneRelationsResponse':
        return super().__new__(
            cls,
            *args,
            office=office,
            costCenter=costCenter,
            effectiveCostCenter=effectiveCostCenter,
            child=child,
            department=department,
            emergencyContact=emergencyContact,
            employment=employment,
            employmentType=employmentType,
            compensation=compensation,
            managerEmployee=managerEmployee,
            teamReference=teamReference,
            _configuration=_configuration,
            **kwargs,
        )

from alexis_hr_python_sdk.model.child_response import ChildResponse
from alexis_hr_python_sdk.model.compensation_response import CompensationResponse
from alexis_hr_python_sdk.model.cost_center_response import CostCenterResponse
from alexis_hr_python_sdk.model.department_response import DepartmentResponse
from alexis_hr_python_sdk.model.emergency_contact_response import EmergencyContactResponse
from alexis_hr_python_sdk.model.employee_response import EmployeeResponse
from alexis_hr_python_sdk.model.employee_team_reference_response import EmployeeTeamReferenceResponse
from alexis_hr_python_sdk.model.employment_response import EmploymentResponse
from alexis_hr_python_sdk.model.employment_type_response import EmploymentTypeResponse
from alexis_hr_python_sdk.model.office_response import OfficeResponse
