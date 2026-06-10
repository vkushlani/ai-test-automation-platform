# AI-Powered QA Agent Platform

This is a Streamlit-based AI QA assistant that uses LLMs, RAG, memory, and specialized QA agents to support software testing activities.

## Key Capabilities

AI Testing Agents

AI-Powered Test Case Generation
Defect & Root Cause Analysis
Requirement Traceability
Regression Risk Assessment
Test Coverage Analysis
QA Planning & Strategy Support

Automation Engineering

Selenium + Cucumber + TestNG Framework Generation
Page Object Model (POM) Design
Feature File Generation
Step Definition Generation
Downloadable Automation Framework ZIP

Document Intelligence

Summarize Uploaded Documents
Compare Multiple Documents
Analyze Release Notes
Generate Tests from Requirements
Generate Automation from Manual Test Cases
Multi-Document Analysis

Advanced AI Features

Retrieval-Augmented Generation (RAG)
Persistent Memory
Vector-Based Memory Search
Live Web Search
Multi-Agent Architecture
Conversational QA Assistant

## Tech Stack

- Python
- Streamlit
- LangChain
- OpenAI
- ChromaDB
- PyPDF
- PDF / Word / Excel parsing

## Architecture

User Prompt  
→ Router  
→ Coordinator Agent  
→ Specialized QA & Automation Agents
→ RAG + Memory + Document Intelligence 
→ AI Response

## Supported Agents

Supported AI Agents
Test Case Agent

Generates:

→ Positive Test Cases
→ Negative Test Cases
→ Edge Cases
→ Regression Scenarios

Defect Analysis Agent

Provides:

→ Root Cause Analysis
→ Severity Assessment
→ Priority Assessment
→ Testing Recommendations

Requirement Traceability Agent

Creates:

→ Requirement Mapping
→ Coverage Matrix
→ Gap Analysis

Regression Risk Agent

Identifies:

→ High-Risk Areas
→ Impacted Modules
→ Regression Scope

Automation Framework Agent

Generates:

→ Selenium Framework Structure
→ Cucumber Feature Files
→ Page Objects
→ Step Definitions
→ TestNG Runners
→ Maven Configuration

Planning Agent

Creates:

→ QA Strategy
→ Test Plans
→ Recommended Testing Activities

## Example Prompts

Generate test cases for login page

Generate Selenium framework for uploaded manual test cases

Analyze defect: Users cannot login after password reset

Create traceability matrix for checkout feature

Perform regression risk analysis for payment module

Run test for login page

Summarize uploaded documents

Compare uploaded documents

## Local Setup

```bash
pip install -r requirements.txt
streamlit run app.py