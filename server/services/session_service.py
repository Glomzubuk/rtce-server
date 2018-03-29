import server.rpc
import time
import uuid
import re
import hashlib

@server.rpc.HandleRpc('Login')
def Login(request, response, handler):
    handler.set_cookie("user_info", "{0}|{1}".format(re.sub("[^\w\d_]", "", request.login), hashlib.sha256(request.login + request.password + server.config.tripcode_salt).hexdigest() if request.password else ""))
    # Uncomment later when we have actual auth.
    #handler.set_cookie("password", re.sub("[^\w\d_]", "", request.password))

@server.rpc.HandleRpc('Logout')
def Logout(request, response, handler):
    server.users.DestroySession(handler)

@server.rpc.HandleRpc('GetGameSessionTicket')
def GetGameSessionTicket(request, response, handler):
    response.game = request.game
    response.nonce = str(uuid.uuid4())

@server.rpc.HandleRpc('RedeemGameSessionTicket')
def RedeemGameSessionTicket(request, response, handler):
    # TODO:  Remove this sleep statement and instead implement an asynchronous event handler in the same style as GetEvent
    time.sleep(server.config.game_session_ticket_wait_interval_ms)
    session_key = request.nonce
    server.users.CreateSession(handler, session_key)
