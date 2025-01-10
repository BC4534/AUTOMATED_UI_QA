import requests
from common import all_file_path

# 配置项
webhook_url = all_file_path.feishu_webhook_url
report_link = all_file_path.report_link_path


def sync_to_feishu():
    # @所有人
    message = {
        "msg_type": "text",
        "content": {
            "text": "<at user_id='all'></at>"
            + "自动化测试报告已生成，点击查看："
            + report_link
        },
        "receive_id": "all",
    }

    headers = {"Content-Type": "application/json"}
    res = requests.post(webhook_url, headers=headers, json=message)
    print(res.text)


if __name__ == "__main__":
    # sync_to_feishu()
    pass
