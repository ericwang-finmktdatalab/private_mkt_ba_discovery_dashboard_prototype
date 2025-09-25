# BA Private Markets Case Study

## Role: Business Analyst (Private Markets)

## Background:
You are a Business Analyst supporting the Private Markets business. Your role involves understanding business needs, analyzing data, writing user requirements, solution designing, and software test planning. You play a critical role in bridging the gap between business stakeholders and the technology team, ensuring that the solutions developed meet the business objectives and are technically feasible.

---

## Scenario:
The Private Markets division relies on a proprietary Investment Lifecycle Management Platform (ILMP) to support its end-to-end investment operations. The division is facing usability challenges, workflow inefficiencies and data accessibility issues that hinder investment decision-making.

---
 
## Paint Points:
A stakeholder interview was conducted, revealing the following pain points:

Module 1: Deal Sourcing & Due Diligence
User Pain Points: No integration with third-party data providers like PitchBook. No centralized document repository.

Module 2: Portfolio Management
User Pain Points: Investment teams lack dynamic performance computation, data quality, data coverage, data lineage and consistency in methodologies for portfolio performance. No clear data visualization on portfolio performance dashboard.

Module 3: Exit Planning
User Pain Points: Generating exit reports is inefficient. No automated valuation analysis.

In a strategic planning meeting, the CIO highlighted the need to focus on the following three prioritized enhancements:
	1. Automating Data Integration – Enhance overall data processes with a primary focus on reducing manual efforts for investment professionals. 
	2. Centralized Document Repository - Institutionalize knowledge and enable future AI-driven insights.
	3. Dynamic Portfolio Dashboard – Provide an interactive dashboard with financial KPIs and performance tracking.

---

## Tasks for Business Analyst:
	1. Compile a comprehensive list of questions to ask your stakeholders during the requirements gathering session to address the identified user pain points for the 3 modules.
	2. Create diagram(s) to describe the to-be state of the platform.
	3. Create the user stories and acceptance criteria for the 3 prioritized enhancement. 
	4. As part of product discovery, make use of the 2 datasets provided to create a dashboard prototype in any form (Excel, PowerPoint, Figma etc.) to address the CIO’s key questions. The dashboard should be dynamic to serve different analytics purposes.
	 
	CIO’s key questions to be addressed in a dashboard for portfolio management particularly for Funds:
		a. What is the Fund’s EBITDA growth?
		b. How did each sector perform in terms of EBITDA growth?

---

## Datasets:
Dataset 1: Fund_Metrics
Includes Fund Attributes and Metrics
CSV: fund_metrics_20250816_145827.csv
```plaintext
FUND_NAME,FUND_CCY,REPORTING_DATE,FUND_EBITDA_GROWTH
Alpha Fund XIV,USD,31-Dec-24,...
Bravo Fund II,EUR,31-Dec-24,...
...
```

Dataset 2: Company_Metrics
Includes Portfolio Company & UPC Attributes and Metrics
CSV: company_metrics_20250816_145827.csv
```plaintext
COMPANY_NAME,PARENT_FUND,EBITDA_GROWTH,MARKET_VALUE,SECTOR
ABC Inc,Alpha Fund XIV,0.085427548,4513500000,Healthcare
XYZ Limited,Bravo Fund II,0.232567384,1467900000,Business Services
DEF Holdings,Alpha Fund XIV,0.145385725,3345000000,TMT
GPP Corporations,Alpha Fund XIV,-0.181888182,1788800000,TMT
FYT LLC,Bravo Fund II,0.462567462,721882000,Business Services
GEN Z,-,0.220584289,997100000,Business Services
...
```

UPC: Underlying Portfolio Company

---

## Formula for calculation:
```plaintext
1. Fund’s EBITDA Growth =
(∑ni=1 EBITDA Growth of UPCi × Market Value of UPCi) ÷ ∑ Market Value of UPC
, where n represents the number of UPCs in the Fund
2. Provide the SQL query required to calculate each sector’s EBITDA growth.
3. Develop a high-level implementation plan of the proposed platform, including key milestones and timelines.
```

---

## Expected Output Format:
1. Report submission in MS Word format
2. Presentation slides for interview panel
