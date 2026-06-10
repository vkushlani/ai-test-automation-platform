import os
from pathlib import Path

import streamlit as st
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

from tools import (
    web_search,
    save_test_cases,
    save_traceability_report,
    save_defect_report,
    save_regression_report,
    run_mock_login_test,
    save_framework_files_from_json
)

# =====================================================
# LOAD ENVIRONMENT VARIABLES
# =====================================================

env_path = Path(__file__).with_name(".env")
load_dotenv(dotenv_path=env_path)

try:
    if "OPENAI_API_KEY" in st.secrets:
        os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]
except Exception:
    pass

# =====================================================
# LLM
# =====================================================

llm = ChatOpenAI(
    model="gpt-4.1-mini",
    temperature=0.2
)

# =====================================================
# TEST CASE AGENT
# =====================================================

def test_case_agent(context, question):

    prompt = f"""
You are a Senior QA Test Design Agent.

Generate detailed manual test cases.

Include:
1. Test Case ID
2. Test Scenario
3. Preconditions
4. Test Steps
5. Test Data
6. Expected Result
7. Priority
8. Type: Positive, Negative, Edge, Regression

Context:
{context}

Question:
{question}
"""

    response = llm.invoke(prompt)

    save_test_cases(response.content)

    return response.content


# =====================================================
# DEFECT ANALYSIS AGENT
# =====================================================

def defect_analysis_agent(context, question):

    prompt = f"""
You are a Senior Defect Analysis Agent.

Analyze:
- Root Cause
- Impact
- Severity
- Priority
- Affected Modules
- Recommended Tests
- Prevention Suggestions

Context:
{context}

Question:
{question}
"""

    response = llm.invoke(prompt)

    save_defect_report(response.content)

    return response.content


# =====================================================
# REQUIREMENT TRACEABILITY AGENT
# =====================================================

def requirement_traceability_agent(context, question):

    prompt = f"""
You are a Requirement Traceability Agent.

Create:
- Requirement Mapping
- Coverage Matrix
- Test Case Mapping
- Missing Coverage
- Recommendations

Context:
{context}

Question:
{question}
"""

    response = llm.invoke(prompt)

    save_traceability_report(response.content)

    return response.content


# =====================================================
# REGRESSION RISK AGENT
# =====================================================

def regression_risk_agent(context, question):

    prompt = f"""
You are a Regression Risk Agent.

Analyze:
- High Risk Areas
- Impacted Modules
- Regression Scope
- Integration Risks
- Testing Priorities
- Recommended Regression Suite

Context:
{context}

Question:
{question}
"""

    response = llm.invoke(prompt)

    save_regression_report(response.content)

    return response.content


# =====================================================
# QA REPORT AGENT
# =====================================================

def qa_report_agent(context):

    prompt = f"""
You are a QA Reporting Agent.

Create:
- Executive Summary
- Key Findings
- Risks
- Recommendations
- Next Steps

Context:
{context}
"""

    response = llm.invoke(prompt)

    return response.content


# =====================================================
# COVERAGE PIPELINE
# =====================================================

def coverage_analysis_pipeline(context, question):

    traceability_output = requirement_traceability_agent(
        context,
        question
    )

    test_output = test_case_agent(
        traceability_output,
        question
    )

    risk_output = regression_risk_agent(
        test_output,
        question
    )

    combined_context = f"""
TRACEABILITY OUTPUT:
{traceability_output}

TEST CASE OUTPUT:
{test_output}

REGRESSION RISK OUTPUT:
{risk_output}
"""

    final_report = qa_report_agent(combined_context)

    return final_report


# =====================================================
# WEBSITE TESTING AGENT
# =====================================================

def website_testing_agent(context, question):

    prompt = f"""
You are a Senior Website Testing Agent.

Generate:
1. Functional Tests
2. UI Tests
3. Negative Tests
4. Security Tests
5. Performance Risks
6. Accessibility Checks

Context:
{context}

Question:
{question}
"""

    response = llm.invoke(prompt)

    return response.content


# =====================================================
# PLANNING AGENT
# =====================================================

def planning_agent(question):

    prompt = f"""
You are an AI Planning Agent.

Break the user's request into logical QA tasks.

Question:
{question}

Return:
1. Step-by-step plan
2. Recommended QA activities
3. Suggested agents/workflows
"""

    response = llm.invoke(prompt)

    return response.content


# =====================================================
# MOCK AUTOMATION AGENT
# =====================================================

def automation_agent(question):

    return run_mock_login_test()


# =====================================================
# WEB SEARCH AGENT
# =====================================================

def web_search_agent(context, question):

    search_results = web_search(question)

    prompt = f"""
You are a live web research assistant.

Use the live web search results below to answer the user's question.

If the results include titles, URLs, or snippets, summarize them clearly.

Web Search Results:
{search_results}

Context:
{context}

Question:
{question}
"""

    response = llm.invoke(prompt)

    return response.content


# =====================================================
# AUTOMATION FRAMEWORK AGENT
# =====================================================

def automation_framework_agent(context, question):

    prompt = f"""
You are a Senior SDET Automation Architect.

Create a Selenium + Cucumber + TestNG framework from the provided manual test cases.

Return ONLY valid JSON.
Do not include markdown.
Do not include ```json.
Do not include explanation outside JSON.

JSON format:

{{
  "files": [
    {{
      "path": "pom.xml",
      "content": "file content here"
    }},
    {{
      "path": "src/test/resources/features/Login.feature",
      "content": "file content here"
    }},
    {{
      "path": "src/test/java/pages/LoginPage.java",
      "content": "file content here"
    }}
  ]
}}

Rules:
- Identify all modules from the uploaded/manual test cases or previous chat context.
- If test cases include Login, Search, Checkout, create separate feature/page/step files.
- Do not hardcode only Login.
- Use Selenium Java, Cucumber, TestNG, Maven.
- Use Page Object Model.
- Include pom.xml.
- Include feature files.
- Include page classes.
- Include step definition classes.
- Include DriverFactory.java.
- Include Hooks.java.
- Include TestRunner.java.
- Include config.properties.
- Escape all newlines correctly in JSON.

Context:
{context}

Question:
{question}
"""

    response = llm.invoke(prompt)

    save_framework_files_from_json(
        response.content
    )

    return """
✅ Selenium Cucumber TestNG framework generated successfully.

The framework ZIP is ready. Use the download button below.
"""


# =====================================================
# COORDINATOR AGENT
# =====================================================

def coordinator_agent(query_type, context, question):

    if query_type == "test_case":

        return test_case_agent(
            context,
            question
        )

    elif query_type == "defect_analysis":

        return defect_analysis_agent(
            context,
            question
        )

    elif query_type == "traceability":

        return requirement_traceability_agent(
            context,
            question
        )

    elif query_type == "regression_risk":

        return regression_risk_agent(
            context,
            question
        )

    elif query_type == "coverage_pipeline":

        return coverage_analysis_pipeline(
            context,
            question
        )

    elif query_type == "website_testing":

        return website_testing_agent(
            context,
            question
        )

    elif query_type == "automation_framework":

        return automation_framework_agent(
            context,
            question
        )

    elif query_type == "planning":

        return planning_agent(
            question
        )

    elif query_type == "automation":

        return automation_agent(
            question
        )

    elif query_type == "web_search":

        return web_search_agent(
            context,
            question
        )

    else:

        prompt = f"""
You are a helpful AI QA assistant.

The router could not identify a specialized workflow,
so answer the user's question as best as possible.

Use context if available.

Context:
{context}

Question:
{question}
"""

        response = llm.invoke(prompt)

        return response.content