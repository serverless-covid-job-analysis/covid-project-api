import json

from flask import jsonify, make_response

from .decimal_encoder import DecimalEncoder


def create_response(message, status_code):
    """
    :param message:
    :param status_code:
    :return: """
    return_res = jsonify(status=str(status_code),
                          message=json.dumps(message, cls=DecimalEncoder)
                        )
    return add_required_headers(make_response(return_res)), int(status_code)
    # return {
    #     'statusCode': str(status_code),
    #     'body': json.dumps(message, cls=DecimalEncoder),
    #     'headers': {
    #         'Content-Type': 'application/json',
    #         'Access-Control-Allow-Origin': '*'
    #     },
    # }


def add_required_headers(response):
    response.headers['Content-Type'] = 'application/json'
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response
