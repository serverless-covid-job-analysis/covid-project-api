import os, sys; sys.path.append(os.path.dirname(os.path.realpath(__file__)))
import sys, importlib
from pathlib import Path


def import_parents(level=1):
    global __package__
    file = Path(__file__).resolve()
    parent, top = file.parent, file.parents[level]

    sys.path.append(str(top))
    try:
        sys.path.remove(str(parent))
    except ValueError:  # already removed
        pass

    __package__ = '.'.join(parent.parts[len(top.parts):])
    importlib.import_module(__package__)  # won't be needed after that


print(f"Name is '{__name__}' Package is - '{__package__}'")
if __name__ == '__main__' and __package__ is None:
    import_parents(level=3)

import awsgi
from flask import Flask, jsonify, request
import logging

logger = logging.getLogger()
logger.setLevel(int(os.getenv("LOGLEVEL", 10)))

try:
#     from api.route import api_v1, api_v2, api_v3, api_v4, api_v5
#     from api.sessions import AwsSession
#     from api.sys_manager import ParameterStore
#     from api.sns_manager import SnsPublisher
#     from api.tenant import TenantData, TenantInfo, TenantInfoService, TenantDataService, TenantAccountInfo, \
#         TenantAccountInfoService
    from api.util import DecimalEncoder, create_response
#     from api.enums import BillTypeEnum, CloudProvidersEnum, ResponseTypeEnum, ErrorCodes, get_error_message
#     from api.cognito_auth import CognitoIdentityProvider, CognitoAuthService
#     from api.user import UserInfo
#     from api.admin import AdminUserInfo, AdminUserInfoService
#     from api.s3_manager import S3Service
except:
#     from .api.route import api_v1, api_v2, api_v3, api_v4, api_v5
#     from .api.sessions import AwsSession
#     from .api.sys_manager import ParameterStore
#     from .api.sns_manager import SnsPublisher
#     from .api.tenant import TenantData, TenantInfo, TenantInfoService, TenantDataService, TenantAccountInfo, \
#         TenantAccountInfoService
    from .api.util import DecimalEncoder, create_response
#     from .api.enums import BillTypeEnum, CloudProvidersEnum, ResponseTypeEnum, ErrorCodes, get_error_message
#     from .api.cognito_auth import CognitoIdentityProvider, CognitoAuthService
#     from .api.user import UserInfo
#     from .api.admin import AdminUserInfo, AdminUserInfoService
#     from .api.s3_manager import S3Service

app = Flask(__name__)
app.config.from_object(__name__)
app.config["DEBUG"] = True
# app.register_blueprint(api_v1)
# app.register_blueprint(api_v2)
# app.register_blueprint(api_v3)
# app.register_blueprint(api_v4)
# app.register_blueprint(api_v5)

def lambda_handler(event, context):
    logger.info("HELLO LAMBDA...WAKE UP NOW")
    return awsgi.response(app, event, context)


@app.route('/ping', methods=['GET'])
def ping():
    """
    just the ping test
    :param head:
    :return: json
    """
    os.listdir("/tmp/")
    print("Request Args", request.args)
    print("Request", request)
    res = {"statusCode": 200, "body": "ping"}
    return create_response("Ping", 200)


# @app.route('/*', methods=['GET', 'POST'])
# def endpoint():
#     composite_log = {}
#     response = {}
#     status_code = 200
#     try:
#         request_data = request.get_json(silent=True)
#         composite_log = request_data["data"]
#         # print(f"Request data : {request_data} composite_log")

#     except Exception as e:
#         print(e)
#         raise
#         status_code = 500
#     return jsonify(status=status_code, message=response)
#     # responder.return_json(response, head, status_code)


if __name__ == '__main__':
    # try:
    #     from api.route import api_v1, api_v2, api_v3, api_v4, api_v5
    # except:
    #     from .api.route import api_v1, api_v2, api_v3, api_v4, api_v5
    # app.register_blueprint(api_v1)
    # app.register_blueprint(api_v2)
    # app.register_blueprint(api_v3)
    # app.register_blueprint(api_v4)
    # app.register_blueprint(api_v5)
    app.run(debug=bool(os.getenv('DEBUG', True)))

