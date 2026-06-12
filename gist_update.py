#!/usr/bin/env python3
import json, sys

tunnel = sys.argv[1]
user = sys.argv[2]
passwd = sys.argv[3]
apikey = sys.argv[4]

content = "===========================================\n"
content += "HERMES AGENT OFFICIAL - DEPLOYMENT INFO\n"
content += "===========================================\n\n"
content += "PUBLIC DASHBOARD URL:\n"
content += tunnel + "\n\n"
content += "IMAGE: nousresearch/hermes-agent:latest\n\n"
content += "LOGIN CREDENTIALS:\n"
content += "Username: " + user + "\n"
content += "Password: " + passwd + "\n\n"
content += "PORTS: Dashboard=9119 | Gateway=8642\n\n"
content += "API KEY: " + apikey + "\n\n"
content += "RUNTIME: Up to 6 hours\n"
content += "===========================================\n"

data = {"files": {"hermes-access.txt": {"content": content}}}
with open('/tmp/gist_payload.json', 'w') as f:
    json.dump(data, f)

print("[OK] JSON prepared")