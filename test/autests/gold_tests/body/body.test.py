'''
Verify basic body reading functionality.
'''
# @file
#
# Copyright 2020, Verizon Media
# SPDX-License-Identifier: Apache-2.0
#

Test.Summary = '''
Verify basic HTTPS functionality.
'''

r = Test.AddTestRun("Verify bodies can be read correctly.")
client = r.AddClientProcess("client1", "body.yaml", https_ports=[4443], other_args="--verbose diag")
server = r.AddServerProcess("server1", "body.yaml", https_ports=[4444], other_args="--verbose diag")
proxy = r.AddProxyProcess("proxy1", listen_port=4443, server_port=4444, use_ssl=True)

proxy.Streams.stdout = "gold/body_proxy.gold"
client.Streams.stdout = "gold/body_client.gold"
server.Streams.stdout = "gold/body_server.gold"

client.Streams.stdout += Testers.ExcludesExpression(
        "Violation:",
        "There should be no verification errors because there are none added.")

server.Streams.stdout += Testers.ExcludesExpression(
        "Violation:",
        "There should be no verification errors because there are none added.")
