import shutil
import subprocess
import sys
import os
import webbrowser
from common import all_file_path
from common.robothandler import sync_to_feishu

os.environ["PYTHONIOENCODING"] = "utf-8"


def run_pytest(allure_dir, test_paths):
    # 判断 allure 报告目录是否存在，不存在则创建
    if not os.path.exists(allure_dir):
        os.makedirs(allure_dir)

    # 构建 pytest 命令，包括 allure 报告目录和 --clean-alluredir 选项
    command = [sys.executable, "-m", "pytest"]
    command.extend(["--alluredir", allure_dir, "--clean-alluredir"])

    # 遍历测试路径列表，添加到命令中
    for path in test_paths:
        if os.path.isdir(path):
            # 如果是目录，则添加目录路径
            command.append(path)
        elif os.path.isfile(path):
            # 如果是文件，则添加文件路径
            command.append(path)
        else:
            print(
                f"Warning: {path} is neither a file nor a directory and will be skipped."
            )

    # 运行 pytest 命令
    try:
        subprocess.run(command, check=False)  # 不报错，生成报告
    except subprocess.CalledProcessError as e:
        print(f"Error running pytest: {e}")
        sys.exit(1)


def generate_allure_report(allure_dir):
    # 复制 environment.properties 文件到 allure 报告目录
    env_properties_path = os.path.join(
        os.path.dirname(__file__), "environment.properties"
    )
    print(env_properties_path)
    if os.path.exists(env_properties_path):
        shutil.copy(env_properties_path, allure_dir)
    # 构建 allure 报告命令
    generate_command = f"allure generate {allure_dir} -o {allure_dir}/report"

    # 运行 allure 报告命令
    try:
        subprocess.run(generate_command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error generating Allure report: {e}")
        sys.exit(1)

    # 打开 allure 报告
    print(f"Allure report generated at: {all_file_path.report_link_path}")
    webbrowser.open(all_file_path.report_link_path)


def main():
    # 指定 allure 报告目录
    allure_dir = all_file_path.allure_report_path
    # 指定测试路径列表，可以包含文件或目录
    test_paths = [
        r"D:\CODE\AUTOMATED_UI_QA\test_case_object\test_login",
        # r"D:\CODE\AUTOMATED_UI_QA\test_case_object\test_operation_and_maintenance_workbench",
        # r"D:\CODE\AUTOMATED_UI_QA\test_case_object\test_maintenance_tools",

    ]

    # 运行 pytest 测试用例并生成 allure 报告
    run_pytest(allure_dir=allure_dir, test_paths=test_paths)

    # 生成 allure 报告
    generate_allure_report(allure_dir)

    # 将测试结果同步至飞书
    sync_to_feishu()


if __name__ == "__main__":
    main()
