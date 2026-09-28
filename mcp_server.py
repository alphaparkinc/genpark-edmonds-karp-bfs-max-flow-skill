import sys
import json
from client import EdmondsKarpMaxFlow

def handle_request(req):
    method = req.get("method")
    params = req.get("params", {})
    req_id = req.get("id")

    if method == "tools/list":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "tools": [
                    {
                        "name": "edmonds_karp_flow",
                        "description": "Calculate maximum flow using BFS-based Edmonds-Karp algorithm",
                        "inputSchema": {
                            "type": "object",
                            "properties": {
                                "num_nodes": {"type": "integer"},
                                "edges": {
                                    "type": "array",
                                    "items": {"type": "array", "items": {"type": "number"}}
                                },
                                "source": {"type": "integer"},
                                "sink": {"type": "integer"}
                            },
                            "required": ["num_nodes", "edges", "source", "sink"]
                        }
                    }
                ]
            }
        }
    elif method == "tools/call":
        name = params.get("name")
        args = params.get("arguments", {})
        if name == "edmonds_karp_flow":
            ek = EdmondsKarpMaxFlow(args["num_nodes"])
            for u, v, c in args["edges"]:
                ek.add_edge(int(u), int(v), float(c))
            flow = ek.compute_max_flow(int(args["source"]), int(args["sink"]))
            return {"jsonrpc": "2.0", "id": req_id, "result": {"content": [{"type": "text", "text": json.dumps({"max_flow": flow})}]}}
    return {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32601, "message": "Method not found"}}

def main():
    for line in sys.stdin:
        if line.strip():
            req = json.loads(line)
            res = handle_request(req)
            sys.stdout.write(json.dumps(res) + "\n")
            sys.stdout.flush()

if __name__ == "__main__":
    main()
