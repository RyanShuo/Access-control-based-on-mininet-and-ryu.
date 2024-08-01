#coding:utf-8

import sys
import urllib.request as urllib2
import json

class RyuApi:
    
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

    def get_flow_entries(self, dpid):
        url = "http://{0}:{1}/stats/flow/".format(self.ip, self.port) + str(dpid)
        req = urllib2.Request(url)
        res_data = urllib2.urlopen(req)
        res = res_data.read()
        res = json.loads(res)
        return res

    def add_flow_entry(self, dpid, match, priority, actions):
        url = "http://{0}:{1}/stats/flowentry/add".format(self.ip, self.port)
        post_data = json.dumps({
            'dpid': dpid,
            'match': match,
            'priority': priority,
            'actions': actions
        }).encode('utf-8')
        req = urllib2.Request(url, post_data, {'Content-Type': 'application/json'})
        res = urllib2.urlopen(req)
        return res.getcode()

    def upate_flow_entry(self, dpid, match, priority, actions):
        url = "http://{0}:{1}/stats/flowentry/modify_strict".format(self.ip, self.port)
        post_data = json.dumps({
            'dpid': dpid,
            'match': match,
            'priority': priority,
            'actions': actions
        }).encode('utf-8')
        req = urllib2.Request(url, post_data, {'Content-Type': 'application/json'})
        res = urllib2.urlopen(req)
        return res.getcode()

    def delete_flow_entry(self, dpid, match=None, priority=None, actions=None):
        url = "http://{0}:{1}/stats/flowentry/delete".format(self.ip, self.port)
        post_data = {'dpid': dpid}
        if match is not None:
            post_data['match'] = match
        if priority is not None:
            post_data['priority'] = priority
        if actions is not None:
            post_data['actions'] = actions
        post_data = json.dumps(post_data).encode('utf-8')
        req = urllib2.Request(url, post_data, {'Content-Type': 'application/json'})
        res = urllib2.urlopen(req)
        return res.getcode()

class FlowUtil:
    @staticmethod
    def get_flow(dpid):
        print("put flow:")
        ryu_api = RyuApi("127.0.0.1", "8080")
        return ryu_api.get_flow_entries(dpid)

    @staticmethod
    def delete_flow(dpid, match=None, priority=None, actions=None):
        print("delete flow:")
        ryu_api = RyuApi("127.0.0.1", "8080")
        return ryu_api.delete_flow_entry(dpid, match=match, priority=priority, actions=actions)

    @staticmethod
    def update_flow(dpid, match, priority, actions):
        print("update flow:")
        ryu_api = RyuApi("127.0.0.1", "8080")
        return ryu_api.upate_flow_entry(dpid, match, priority, actions)

    @staticmethod
    def add_flow(dpid, match, priority, actions):
        print("add flow:")
        ryu_api = RyuApi("127.0.0.1", "8080")
        return ryu_api.add_flow_entry(dpid, match, priority, actions)


FlowUtil.add_flow("3", {"nw_src": "10.0.0.1", "nw_proto": 6, "tp_dst": 8080, "nw_dst": "10.0.0.4", "dl_type": 2048}, "100", [])
FlowUtil.add_flow("3", {"nw_src": "10.0.0.2", "nw_dst": "10.0.0.4", "dl_type": 2048}, "100", [])
