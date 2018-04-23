"""
config.py
"""

import ConfigParser
import os
import socket
import ipgetter
import tbmatch.match_pb2
import tbportal.portal_pb2

# UTILITY FUNCS

def get_external_ip():
    try:
        return ipgetter.myip()
    except:
        return None

def load_config():
    config = ConfigParser.SafeConfigParser()
    if len(config.read("rt.cfg")) == 0:
        build_default_config(config)

    return config

def build_default_config(config):
    cfgfile = open("rt.cfg", 'w')
    # Disable lower()
    config.optionxform = str
    # Network settings
    config.add_section('Network')

    ip = get_external_ip()
    if ip is None:
        ip = "127.0.0.1"

    config.set('Network', 'Hostname', ip)
    config.set('Network','RPCPort', "1337") # It's 2003 again
    config.set('Network', 'PortalUDPPortBase', "40000")
    config.set('Network', 'MaxPortalUDPPorts', "8192")
    config.set('Network', 'SSLCertFile', "")
    config.set('Network', 'SSLKeyFile', "")

    config.add_section('Portal')
    config.set('Portal', 'PortalPingCount', "5")
    config.set('Portal', 'GuestUsername', 'Anonymous')
    config.set('Portal', 'UseTripCodes', "False")
    config.set('Portal', 'TripcodeSecureSalt', "CHANGETHIS")

    config.add_section('GameSession')
    config.set('GameSession','RankedMatchRounds', "2")
    config.set('GameSession', 'HandshakeReplyIntervalMs',"1000")

    config.write(cfgfile)
    cfgfile.flush()
    cfgfile.close()

###### CONFIG PARSER SETUP #####

config = load_config()



# The external hostname of the Rising Thunder server.
# If environment variable RT_SERVER_HOSTNAME is defined, it will be used, otherwise
# default to 127.0.0.1 for localhost.
hostname = config.get('Network','Hostname')

# Web port to listen on for RPCs
port = config.getint('Network', 'RPCPort')

# The UDP port on this server that clients can use for ping testing.
portal_port_base = config.getint('Network', 'PortalUDPPortBase')
portal_port_range = config.getint('Network', 'MaxPortalUDPPorts')

# Certificates for HTTPS
ssl_cert_file = config.get('Network', 'SSLCertFile')
ssl_key_file  = config.get('Network', 'SSLKeyFile')

# Tripcodes so we use 4chan style !whrdasfd based on password.
tripcode_enabled = config.get('Portal', 'UseTripCodes')
tripcode_salt = config.get('Portal', 'TripcodeSecureSalt')

# number of times to ping for the ping test
portal_ping_count = config.getint('Portal','PortalPingCount')

guest_username = config.get('Portal', 'GuestUsername').split(',') # allow for multiple

# amount of time to wait on the client to allow for UI setup before redeeming the game session ticket
# TODO: Move to config file but this seems like a hacky setting to make up for something else.
game_session_ticket_wait_interval_ms = 0.25

game_session_config = tbportal.portal_pb2.GameSessionConfig()
game_session_config.games_to_win = config.getint('GameSession','RankedMatchRounds')
game_session_config.handshake_reply_interval_ms = config.getint('GameSession', 'HandshakeReplyIntervalMs')

# Enabled features.
featureSet = tbmatch.match_pb2.ClientFeatureSet()

# Webhook Features
webhook_match_over = config.get('Webhook','MatchOver')
webhook_user_logged_in = config.get('Webhook','UserLoggedIn')
webhook_user_in_matchmaking = config.get('Webhook','InMatchmaking')
