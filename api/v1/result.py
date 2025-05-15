from flask import Request, Response
import requests

def handler(request: Request) -> Response:
    url = request.args.get("url")
    if not url:
        return Response("Missing 'url' parameter", status=400)

    try:
        res = requests.get(url)
        headers = {
            "Access-Control-Allow-Origin": "*",
            "Content-Type": res.headers.get("Content-Type", "text/html")
        }
        return Response(res.content, status=res.status_code, headers=headers)
    except Exception as e:
        return Response(f"Error: {str(e)}", status=500)
