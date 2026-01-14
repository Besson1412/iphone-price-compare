import functions_framework
import json

@functions_framework.http
def run_iphone_agent(request):
    # 模拟返回的数据，先不接真实AI，确保流水线能通
    data = {
        "status": "success",
        "message": "Hello from Google Cloud DevOps Pipeline!",
        "prices": []
    }
    return json.dumps(data), 200