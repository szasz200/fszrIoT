import requests
from flask import Flask, Response, request
from http import HTTPStatus

server = Flask(__name__)

handler_instance = AAPSHandler()


@server.route('/')
def index():
    return Response("The server refuses the attempt to brew coffee with a teapot.", 418)

@server.route('/', methods=["POST"])
def checkServerStatus():
    return Response("", HTTPStatus.OK)

@server.route('/basal', methods=["POST"])
def setBasal():
    return Response("", HTTPStatus.OK)

@server.route('/initialize', methods=["POST"])
def initializeSimulation():
    if status:
        return Response(" ", HTTPStatus.OK)
    else:
        return Response(" ", HTTPStatus.BAD_REQUEST)


server.run()
