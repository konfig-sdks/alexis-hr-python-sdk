# coding: utf-8

"""
    AlexisHR API

    <h1 id=\"introduction\">Introduction</h1>  <p>    AlexisHR API is currently in preview. This means that small, backward    incompatible changes might be introduced while in preview. The changes will be    documented and communicated.    <a      href=\"https://cdn.forms-content.sg-form.com/56c6a65c-90a2-11eb-a700-a6de1aea3a1a\"      target=\"_blank\"      ><button>Subscribe to updates</button></a    >  </p>    <h1 id=\"authentication\">Authentication</h1>  <pre class=\"click-to-expand-wrapper is-snippet-wrapper language-undefined\">  <code class=\"is-highlighted language-bash\">curl https://api.alexishr.com/v1/employee \\    -H \"Authorization: Bearer &lt;your_access_token&gt;\"</code>  </pre>  <p>    Authenticate your account when using the API by including your secret Access    Token in the request.    <a href=\"https://app.alexishr.com/access-tokens\">Manage your Access Tokens</a    >.  </p>  <p>    Authentication is performed by passing the Access Token in the Authorization    header.  </p>  <hr />    <h1 id=\"structure\">Structure</h1>  <p>    You will find the structure of the API to be highly uniform and consistent.    Typically every resource can be accessed via a top level endpoint, such as    <code>/v1/employee</code>. For every such resource, you can perform some of    the following operations:  </p>  <h2>Operations</h2>  <table>    <tr>      <td>GET /v1/:resource</td>      <td>List all objects of this type</td>    </tr>    <tr>      <td>GET /v1/:resource/:id</td>      <td>Retrieve a resource by id</td>    </tr>    <tr>      <td>POST /v1/:resource</td>      <td>Create a resource of this type</td>    </tr>    <tr>      <td>PATCH /v1/:resource/:id</td>      <td>Update the resource by id</td>    </tr>    <tr>      <td>DELETE /v1/:resource/:id</td>      <td>Delete the resource by id</td>    </tr>  </table>  <hr />    <h1 id=\"roles\">Roles</h1>  <p>The Access Tokens will have owner permission on the account</p>  <hr />    <h1 id=\"filters\">Filters</h1>  <p>    Some of the list endpoints allow to filter results by certain conditions.    Refer to specific resources to find out what criteria are allowed. Below is a    list of the different conditions.  </p>    <h4 id=\"eq\"><code>$eq</code></h4>  <p>Find all results matching the attribute value specified.</p>  <div>    <pre><code class=\"language-shell\" data-lang=\"shell\">GET /v1/example?filters[fieldName][$eq]=value</code></pre>  </div>  <p>Can also be simplified like this.</p>  <div>    <pre><code class=\"language-shell\" data-lang=\"shell\">GET /v1/example?filters[fieldName]=value</code></pre>  </div>    <h4 id=\"neq\"><code>$neq</code></h4>  <p>Find all results not matching the attribute value specified.</p>  <div>    <pre><code class=\"language-shell\" data-lang=\"shell\">GET /v1/example?filters[fieldName][$neq]=value</code></pre>  </div>    <h4 id=\"gt\"><code>$gt</code>, <code>$gte</code></h4>  <p>    Find all results where the value is more (<code>$gt</code>) or more and equal    (<code>$gte</code>) to a given value.  </p>  <div>    <pre><code class=\"language-shell\" data-lang=\"shell\">GET /v1/example?filters[startDate][$gte]=2020-01-01</code></pre>  </div>  <hr />    <h4 id=\"lt\"><code>$lt</code>, <code>$lte</code></h4>  <p>    Find all results where the value is less (<code>$lt</code>) or less and equal    (<code>$lte</code>) to a given value.  </p>  <div>    <pre><code class=\"language-shell\" data-lang=\"shell\">GET /v1/example?filters[startDate][$lte]=2020-01-01</code></pre>  </div>  <hr />    <h4 id=\"in\"><code>$in</code>, <code>$nin</code></h4>  <p>    Find all results matching (<code>$in</code>) or not matching    (<code>$nin</code>) any of the attribute values specified.  </p>  <div>    <pre><code class=\"language-shell\" data-lang=\"shell\">GET /v1/example?filters[fieldName][$in][]=value1&filters[fieldName][$in][]=value2</code></pre>  </div>  <hr />    <h4 id=\"between\"><code>$between</code></h4>  <p>Find all results between two values specified.</p>  <div>    <pre><code class=\"language-shell\" data-lang=\"shell\">GET /v1/example?filters[startDate][$between][]=2020-01-01&filters[startDate][$between][]=2020-12-31</code></pre>  </div>  <hr />    <h1 id=\"versioning\">Versioning</h1>  <p>    Each version of the API is guaranteed to be compatible with the resources of    the same version. When we make breaking changes to the API a new version will    be published  </p>  <hr />    <h1 id=\"changelog\">Changelog</h1>  <h3>2023-12-20</h3>  <p>Field [updated] added for filter & select for Get Many Employments and Get Many Employees.</p>  <h3>2021-03-15</h3>  <p>First draft was published</p>  <hr />   # Authentication  <!-- ReDoc-Inject: <security-definitions> -->

    The version of the OpenAPI document: v1-preview
    Contact: support@alexishr.com
    Generated by: https://konfigthis.com
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from pydantic import RootModel
from alexis_hr_python_sdk.request_before_hook import request_before_hook
import json
from urllib3._collections import HTTPHeaderDict

from alexis_hr_python_sdk.api_response import AsyncGeneratorResponse
from alexis_hr_python_sdk import api_client, exceptions
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

from alexis_hr_python_sdk.model.forbidden_response import ForbiddenResponse as ForbiddenResponseSchema
from alexis_hr_python_sdk.model.create_department_request import CreateDepartmentRequest as CreateDepartmentRequestSchema
from alexis_hr_python_sdk.model.unauthorized_response import UnauthorizedResponse as UnauthorizedResponseSchema
from alexis_hr_python_sdk.model.department_response_mapped import DepartmentResponseMapped as DepartmentResponseMappedSchema
from alexis_hr_python_sdk.model.internal_server_error_response import InternalServerErrorResponse as InternalServerErrorResponseSchema
from alexis_hr_python_sdk.model.bad_request_response import BadRequestResponse as BadRequestResponseSchema

from alexis_hr_python_sdk.type.department_response_mapped import DepartmentResponseMapped
from alexis_hr_python_sdk.type.forbidden_response import ForbiddenResponse
from alexis_hr_python_sdk.type.bad_request_response import BadRequestResponse
from alexis_hr_python_sdk.type.internal_server_error_response import InternalServerErrorResponse
from alexis_hr_python_sdk.type.create_department_request import CreateDepartmentRequest
from alexis_hr_python_sdk.type.unauthorized_response import UnauthorizedResponse

from ...api_client import Dictionary
from alexis_hr_python_sdk.pydantic.internal_server_error_response import InternalServerErrorResponse as InternalServerErrorResponsePydantic
from alexis_hr_python_sdk.pydantic.unauthorized_response import UnauthorizedResponse as UnauthorizedResponsePydantic
from alexis_hr_python_sdk.pydantic.bad_request_response import BadRequestResponse as BadRequestResponsePydantic
from alexis_hr_python_sdk.pydantic.forbidden_response import ForbiddenResponse as ForbiddenResponsePydantic
from alexis_hr_python_sdk.pydantic.department_response_mapped import DepartmentResponseMapped as DepartmentResponseMappedPydantic
from alexis_hr_python_sdk.pydantic.create_department_request import CreateDepartmentRequest as CreateDepartmentRequestPydantic

from . import path

# body param
SchemaForRequestBodyApplicationJson = CreateDepartmentRequestSchema


request_body_create_department_request = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
    required=True,
)
_auth = [
    'bearer',
]
SchemaFor201ResponseBodyApplicationJson = DepartmentResponseMappedSchema


@dataclass
class ApiResponseFor201(api_client.ApiResponse):
    body: DepartmentResponseMapped


@dataclass
class ApiResponseFor201Async(api_client.AsyncApiResponse):
    body: DepartmentResponseMapped


_response_for_201 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor201,
    response_cls_async=ApiResponseFor201Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor201ResponseBodyApplicationJson),
    },
)
SchemaFor400ResponseBodyApplicationJson = BadRequestResponseSchema


@dataclass
class ApiResponseFor400(api_client.ApiResponse):
    body: BadRequestResponse


@dataclass
class ApiResponseFor400Async(api_client.AsyncApiResponse):
    body: BadRequestResponse


_response_for_400 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor400,
    response_cls_async=ApiResponseFor400Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor400ResponseBodyApplicationJson),
    },
)
SchemaFor401ResponseBodyApplicationJson = UnauthorizedResponseSchema


@dataclass
class ApiResponseFor401(api_client.ApiResponse):
    body: UnauthorizedResponse


@dataclass
class ApiResponseFor401Async(api_client.AsyncApiResponse):
    body: UnauthorizedResponse


_response_for_401 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor401,
    response_cls_async=ApiResponseFor401Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor401ResponseBodyApplicationJson),
    },
)
SchemaFor403ResponseBodyApplicationJson = ForbiddenResponseSchema


@dataclass
class ApiResponseFor403(api_client.ApiResponse):
    body: ForbiddenResponse


@dataclass
class ApiResponseFor403Async(api_client.AsyncApiResponse):
    body: ForbiddenResponse


_response_for_403 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor403,
    response_cls_async=ApiResponseFor403Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor403ResponseBodyApplicationJson),
    },
)
SchemaFor500ResponseBodyApplicationJson = InternalServerErrorResponseSchema


@dataclass
class ApiResponseFor500(api_client.ApiResponse):
    body: InternalServerErrorResponse


@dataclass
class ApiResponseFor500Async(api_client.AsyncApiResponse):
    body: InternalServerErrorResponse


_response_for_500 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor500,
    response_cls_async=ApiResponseFor500Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor500ResponseBodyApplicationJson),
    },
)
_status_code_to_response = {
    '201': _response_for_201,
    '400': _response_for_400,
    '401': _response_for_401,
    '403': _response_for_403,
    '500': _response_for_500,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _create_one_mapped_args(
        self,
        name: str,
        description: typing.Optional[str] = None,
        cost_center_id: typing.Optional[str] = None,
        parent_id: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _body = {}
        if description is not None:
            _body["description"] = description
        if name is not None:
            _body["name"] = name
        if cost_center_id is not None:
            _body["costCenterId"] = cost_center_id
        if parent_id is not None:
            _body["parentId"] = parent_id
        args.body = _body
        return args

    async def _acreate_one_oapg(
        self,
        body: typing.Any = None,
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Create One Department
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        used_path = path.value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        if body is schemas.unset:
            raise exceptions.ApiValueError(
                'The required body parameter has an invalid value of: unset. Set a valid value instead')
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/department',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_create_department_request.serialize(body, content_type)
        if 'fields' in serialized_data:
            _fields = serialized_data['fields']
        elif 'body' in serialized_data:
            _body = serialized_data['body']
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            auth_settings=_auth,
            timeout=timeout,
            **kwargs
        )
    
        if stream:
            if not 200 <= response.http_response.status <= 299:
                body = (await response.http_response.content.read()).decode("utf-8")
                raise exceptions.ApiStreamingException(
                    status=response.http_response.status,
                    reason=response.http_response.reason,
                    body=body,
                )
    
            async def stream_iterator():
                """
                iterates over response.http_response.content and closes connection once iteration has finished
                """
                async for line in response.http_response.content:
                    if line == b'\r\n':
                        continue
                    yield line
                response.http_response.close()
                await response.session.close()
            return AsyncGeneratorResponse(
                content=stream_iterator(),
                headers=response.http_response.headers,
                status=response.http_response.status,
                response=response.http_response
            )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = await response_for_status.deserialize_async(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserializationAsync(
                body=await response.http_response.json() if is_json else await response.http_response.text(),
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        # cleanup session / response
        response.http_response.close()
        await response.session.close()
    
        return api_response


    def _create_one_oapg(
        self,
        body: typing.Any = None,
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Create One Department
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        used_path = path.value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        if body is schemas.unset:
            raise exceptions.ApiValueError(
                'The required body parameter has an invalid value of: unset. Set a valid value instead')
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/department',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_create_department_request.serialize(body, content_type)
        if 'fields' in serialized_data:
            _fields = serialized_data['fields']
        elif 'body' in serialized_data:
            _body = serialized_data['body']
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            auth_settings=_auth,
            timeout=timeout,
        )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = response_for_status.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserialization(
                body=json.loads(response.http_response.data) if is_json else response.http_response.data,
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        return api_response


class CreateOneRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def acreate_one(
        self,
        name: str,
        description: typing.Optional[str] = None,
        cost_center_id: typing.Optional[str] = None,
        parent_id: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_one_mapped_args(
            name=name,
            description=description,
            cost_center_id=cost_center_id,
            parent_id=parent_id,
        )
        return await self._acreate_one_oapg(
            body=args.body,
            **kwargs,
        )
    
    def create_one(
        self,
        name: str,
        description: typing.Optional[str] = None,
        cost_center_id: typing.Optional[str] = None,
        parent_id: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_one_mapped_args(
            name=name,
            description=description,
            cost_center_id=cost_center_id,
            parent_id=parent_id,
        )
        return self._create_one_oapg(
            body=args.body,
        )

class CreateOne(BaseApi):

    async def acreate_one(
        self,
        name: str,
        description: typing.Optional[str] = None,
        cost_center_id: typing.Optional[str] = None,
        parent_id: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> DepartmentResponseMappedPydantic:
        raw_response = await self.raw.acreate_one(
            name=name,
            description=description,
            cost_center_id=cost_center_id,
            parent_id=parent_id,
            **kwargs,
        )
        if validate:
            return DepartmentResponseMappedPydantic(**raw_response.body)
        return api_client.construct_model_instance(DepartmentResponseMappedPydantic, raw_response.body)
    
    
    def create_one(
        self,
        name: str,
        description: typing.Optional[str] = None,
        cost_center_id: typing.Optional[str] = None,
        parent_id: typing.Optional[str] = None,
        validate: bool = False,
    ) -> DepartmentResponseMappedPydantic:
        raw_response = self.raw.create_one(
            name=name,
            description=description,
            cost_center_id=cost_center_id,
            parent_id=parent_id,
        )
        if validate:
            return DepartmentResponseMappedPydantic(**raw_response.body)
        return api_client.construct_model_instance(DepartmentResponseMappedPydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        name: str,
        description: typing.Optional[str] = None,
        cost_center_id: typing.Optional[str] = None,
        parent_id: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_one_mapped_args(
            name=name,
            description=description,
            cost_center_id=cost_center_id,
            parent_id=parent_id,
        )
        return await self._acreate_one_oapg(
            body=args.body,
            **kwargs,
        )
    
    def post(
        self,
        name: str,
        description: typing.Optional[str] = None,
        cost_center_id: typing.Optional[str] = None,
        parent_id: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_one_mapped_args(
            name=name,
            description=description,
            cost_center_id=cost_center_id,
            parent_id=parent_id,
        )
        return self._create_one_oapg(
            body=args.body,
        )

