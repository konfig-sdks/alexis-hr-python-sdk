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
from alexis_hr_python_sdk.model.employment_type_response_mapped import EmploymentTypeResponseMapped as EmploymentTypeResponseMappedSchema
from alexis_hr_python_sdk.model.unauthorized_response import UnauthorizedResponse as UnauthorizedResponseSchema
from alexis_hr_python_sdk.model.not_found_response import NotFoundResponse as NotFoundResponseSchema
from alexis_hr_python_sdk.model.internal_server_error_response import InternalServerErrorResponse as InternalServerErrorResponseSchema
from alexis_hr_python_sdk.model.update_employment_type_request import UpdateEmploymentTypeRequest as UpdateEmploymentTypeRequestSchema
from alexis_hr_python_sdk.model.bad_request_response import BadRequestResponse as BadRequestResponseSchema

from alexis_hr_python_sdk.type.forbidden_response import ForbiddenResponse
from alexis_hr_python_sdk.type.update_employment_type_request import UpdateEmploymentTypeRequest
from alexis_hr_python_sdk.type.bad_request_response import BadRequestResponse
from alexis_hr_python_sdk.type.internal_server_error_response import InternalServerErrorResponse
from alexis_hr_python_sdk.type.employment_type_response_mapped import EmploymentTypeResponseMapped
from alexis_hr_python_sdk.type.not_found_response import NotFoundResponse
from alexis_hr_python_sdk.type.unauthorized_response import UnauthorizedResponse

from ...api_client import Dictionary
from alexis_hr_python_sdk.pydantic.internal_server_error_response import InternalServerErrorResponse as InternalServerErrorResponsePydantic
from alexis_hr_python_sdk.pydantic.update_employment_type_request import UpdateEmploymentTypeRequest as UpdateEmploymentTypeRequestPydantic
from alexis_hr_python_sdk.pydantic.employment_type_response_mapped import EmploymentTypeResponseMapped as EmploymentTypeResponseMappedPydantic
from alexis_hr_python_sdk.pydantic.not_found_response import NotFoundResponse as NotFoundResponsePydantic
from alexis_hr_python_sdk.pydantic.unauthorized_response import UnauthorizedResponse as UnauthorizedResponsePydantic
from alexis_hr_python_sdk.pydantic.bad_request_response import BadRequestResponse as BadRequestResponsePydantic
from alexis_hr_python_sdk.pydantic.forbidden_response import ForbiddenResponse as ForbiddenResponsePydantic

from . import path

# Path params
IdSchema = schemas.StrSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'id': typing.Union[IdSchema, str, ],
    }
)
RequestOptionalPathParams = typing_extensions.TypedDict(
    'RequestOptionalPathParams',
    {
    },
    total=False
)


class RequestPathParams(RequestRequiredPathParams, RequestOptionalPathParams):
    pass


request_path_id = api_client.PathParameter(
    name="id",
    style=api_client.ParameterStyle.SIMPLE,
    schema=IdSchema,
    required=True,
)
# body param
SchemaForRequestBodyApplicationJson = UpdateEmploymentTypeRequestSchema


request_body_update_employment_type_request = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
    required=True,
)
_auth = [
    'bearer',
]
SchemaFor200ResponseBodyApplicationJson = EmploymentTypeResponseMappedSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: EmploymentTypeResponseMapped


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: EmploymentTypeResponseMapped


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
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
SchemaFor404ResponseBodyApplicationJson = NotFoundResponseSchema


@dataclass
class ApiResponseFor404(api_client.ApiResponse):
    body: NotFoundResponse


@dataclass
class ApiResponseFor404Async(api_client.AsyncApiResponse):
    body: NotFoundResponse


_response_for_404 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor404,
    response_cls_async=ApiResponseFor404Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor404ResponseBodyApplicationJson),
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
    '200': _response_for_200,
    '400': _response_for_400,
    '401': _response_for_401,
    '403': _response_for_403,
    '404': _response_for_404,
    '500': _response_for_500,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _update_one_employment_type_mapped_args(
        self,
        country: str,
        id: str,
        name: typing.Optional[str] = None,
        vacation: typing.Optional[bool] = None,
        max_months: typing.Optional[typing.Union[int, float]] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _path_params = {}
        _body = {}
        if name is not None:
            _body["name"] = name
        if vacation is not None:
            _body["vacation"] = vacation
        if country is not None:
            _body["country"] = country
        if max_months is not None:
            _body["maxMonths"] = max_months
        args.body = _body
        if id is not None:
            _path_params["id"] = id
        args.path = _path_params
        return args

    async def _aupdate_one_employment_type_oapg(
        self,
        body: typing.Any = None,
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Replace One Employment Type
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'put'.upper()
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
            path_template='/employment-type/{id}',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_update_employment_type_request.serialize(body, content_type)
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


    def _update_one_employment_type_oapg(
        self,
        body: typing.Any = None,
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Replace One Employment Type
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'put'.upper()
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
            path_template='/employment-type/{id}',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_update_employment_type_request.serialize(body, content_type)
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


class UpdateOneEmploymentTypeRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aupdate_one_employment_type(
        self,
        country: str,
        id: str,
        name: typing.Optional[str] = None,
        vacation: typing.Optional[bool] = None,
        max_months: typing.Optional[typing.Union[int, float]] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._update_one_employment_type_mapped_args(
            country=country,
            id=id,
            name=name,
            vacation=vacation,
            max_months=max_months,
        )
        return await self._aupdate_one_employment_type_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def update_one_employment_type(
        self,
        country: str,
        id: str,
        name: typing.Optional[str] = None,
        vacation: typing.Optional[bool] = None,
        max_months: typing.Optional[typing.Union[int, float]] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._update_one_employment_type_mapped_args(
            country=country,
            id=id,
            name=name,
            vacation=vacation,
            max_months=max_months,
        )
        return self._update_one_employment_type_oapg(
            body=args.body,
            path_params=args.path,
        )

class UpdateOneEmploymentType(BaseApi):

    async def aupdate_one_employment_type(
        self,
        country: str,
        id: str,
        name: typing.Optional[str] = None,
        vacation: typing.Optional[bool] = None,
        max_months: typing.Optional[typing.Union[int, float]] = None,
        validate: bool = False,
        **kwargs,
    ) -> EmploymentTypeResponseMappedPydantic:
        raw_response = await self.raw.aupdate_one_employment_type(
            country=country,
            id=id,
            name=name,
            vacation=vacation,
            max_months=max_months,
            **kwargs,
        )
        if validate:
            return EmploymentTypeResponseMappedPydantic(**raw_response.body)
        return api_client.construct_model_instance(EmploymentTypeResponseMappedPydantic, raw_response.body)
    
    
    def update_one_employment_type(
        self,
        country: str,
        id: str,
        name: typing.Optional[str] = None,
        vacation: typing.Optional[bool] = None,
        max_months: typing.Optional[typing.Union[int, float]] = None,
        validate: bool = False,
    ) -> EmploymentTypeResponseMappedPydantic:
        raw_response = self.raw.update_one_employment_type(
            country=country,
            id=id,
            name=name,
            vacation=vacation,
            max_months=max_months,
        )
        if validate:
            return EmploymentTypeResponseMappedPydantic(**raw_response.body)
        return api_client.construct_model_instance(EmploymentTypeResponseMappedPydantic, raw_response.body)


class ApiForput(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aput(
        self,
        country: str,
        id: str,
        name: typing.Optional[str] = None,
        vacation: typing.Optional[bool] = None,
        max_months: typing.Optional[typing.Union[int, float]] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._update_one_employment_type_mapped_args(
            country=country,
            id=id,
            name=name,
            vacation=vacation,
            max_months=max_months,
        )
        return await self._aupdate_one_employment_type_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def put(
        self,
        country: str,
        id: str,
        name: typing.Optional[str] = None,
        vacation: typing.Optional[bool] = None,
        max_months: typing.Optional[typing.Union[int, float]] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._update_one_employment_type_mapped_args(
            country=country,
            id=id,
            name=name,
            vacation=vacation,
            max_months=max_months,
        )
        return self._update_one_employment_type_oapg(
            body=args.body,
            path_params=args.path,
        )

