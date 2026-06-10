import os
from tavily import TavilyClient
import zipfile
import json


def web_search(query):

    api_key = os.getenv("TAVILY_API_KEY")

    if not api_key:
        return "TAVILY_API_KEY is not configured."

    client = TavilyClient(api_key=api_key)

    results = client.search(
        query=query,
        max_results=5
    )

    return results

def analyze_risk(module_name):
    
    risks = {
        "payment": "High regression risk due to transaction handling.",
        "checkout": "Medium risk due to session changes.",
        "login": "High security testing required.",
        "cart": "Performance regression risk exists."
    }
    
    return risks.get(module_name.lower(),
        "No specific risk identified."
        )
    
def generate_test_cases(module_name):

    test_cases = {
        "payment": [
            "Validate retry handling",
            "Verify failed transaction recovery",
            "Test timeout behavior"
        ],

        "login": [
            "Verify MFA flow",
            "Test invalid password handling",
            "Validate password reset"
        ]
    }

    return test_cases.get(
        module_name.lower(),
        ["No test cases available."]
    )

def generate_testing_strategy(module_name):

    strategies = {

        "payment": """
        - Validate retries
        - Verify transaction rollback
        - Test timeout handling
        - Validate fraud detection
        """,

        "login": """
        - Test MFA
        - Validate password reset
        - Verify session handling
        - Test invalid login attempts
        """,

        "checkout": """
        - Verify discounts
        - Validate cart totals
        - Test session expiration
        """
    }

    return strategies.get(
        module_name.lower(),
        "No strategy available."
    )
    
def save_automation_framework(framework_content):

    folder = "exports/automation_framework"
    os.makedirs(folder, exist_ok=True)

    file_path = os.path.join(folder, "automation_framework_design.txt")

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(framework_content)

    return file_path

#Generate Separate Selenium+Cucumber files
# def save_framework_files(files_dict):

#     folder = "exports/generated_framework"
#     os.makedirs(folder, exist_ok=True)

#     for file_path, content in files_dict.items():

#         full_path = os.path.join(folder, file_path)
#         os.makedirs(os.path.dirname(full_path), exist_ok=True)

#         with open(full_path, "w", encoding="utf-8") as f:
#             f.write(content)

#     zip_path = "exports/generated_framework.zip"

#     with zipfile.ZipFile(zip_path, "w") as zipf:
#         for root, dirs, files in os.walk(folder):
#             for file in files:
#                 full_file = os.path.join(root, file)
#                 arcname = os.path.relpath(full_file, folder)
#                 zipf.write(full_file, arcname)

#     return zip_path

def save_framework_files_from_json(ai_response):

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    folder = os.path.join(
        BASE_DIR,
        "exports",
        "generated_framework"
    )

    os.makedirs(folder, exist_ok=True)

    # Clean old files
    for root, dirs, files in os.walk(folder):
        for file in files:
            os.remove(os.path.join(root, file))

    data = json.loads(ai_response)

    for file_item in data["files"]:

        file_path = file_item["path"]
        content = file_item["content"]

        full_path = os.path.join(folder, file_path)

        os.makedirs(
            os.path.dirname(full_path),
            exist_ok=True
        )

        with open(full_path, "w", encoding="utf-8") as f:
            f.write(content)

    zip_path = os.path.join(
        BASE_DIR,
        "exports",
        "generated_selenium_cucumber_framework.zip"
    )

    with zipfile.ZipFile(zip_path, "w") as zipf:

        for root, dirs, files in os.walk(folder):

            for file in files:

                full_file = os.path.join(root, file)

                arcname = os.path.relpath(
                    full_file,
                    folder
                )

                zipf.write(full_file, arcname)

    return zip_path

# tools.py

EXPORT_FOLDER = "exports"

os.makedirs(
    EXPORT_FOLDER,
    exist_ok=True
)

# =====================================
# SAVE TEST CASES
# =====================================

def save_test_cases(test_cases):

    file_path = os.path.join(
        EXPORT_FOLDER,
        "generated_test_cases.txt"
    )

    with open(
        file_path,
        "w",
        encoding="utf-8"
    ) as f:

        f.write(test_cases)

    return file_path


# =====================================
# SAVE TRACEABILITY REPORT
# =====================================

def save_traceability_report(report):

    file_path = os.path.join(
        EXPORT_FOLDER,
        "traceability_report.txt"
    )

    with open(
        file_path,
        "w",
        encoding="utf-8"
    ) as f:

        f.write(report)

    return file_path


# =====================================
# SAVE DEFECT REPORT
# =====================================

def save_defect_report(report):

    file_path = os.path.join(
        EXPORT_FOLDER,
        "defect_analysis_report.txt"
    )

    with open(
        file_path,
        "w",
        encoding="utf-8"
    ) as f:

        f.write(report)

    return file_path


# =====================================
# SAVE REGRESSION REPORT
# =====================================

def save_regression_report(report):

    file_path = os.path.join(
        EXPORT_FOLDER,
        "regression_risk_report.txt"
    )

    with open(
        file_path,
        "w",
        encoding="utf-8"
    ) as f:

        f.write(report)

    return file_path


# =====================================
# MOCK AUTOMATION TOOL
# =====================================

def run_mock_login_test():

    return """
LOGIN TEST RESULTS

Open Login Page ........ PASS
Enter Username ......... PASS
Enter Password ......... PASS
Click Login ............ PASS

OVERALL RESULT: PASS
"""