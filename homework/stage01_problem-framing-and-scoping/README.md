 # Project Title 
**Stage:** Problem Framing & Scoping (Stage 01) 

## Problem Statement 
Regulators require banks to report counterparty credit risk exposures (e.g., Basel III/IV). Create a lightweight framework to calculate Exposure at Default (EAD) and Probability of Default (PD) for counterparties, and generate simple compliance-ready reports on a monthly basis. 

## Stakeholder & User 
- **Stakeholder (Decision Owner):** Cheif Risk Officer  
- **Users:** Risk Reporting Analysts
- **Decision Window:** Monthly / Quarterly
  
## Useful Answer & Decision 
- **Type:** Descriptive + Predictive  
- **Artifact:** Monthly counterparty exposure table (EAD × PD → Capital Requirement)  
- **Decision Trigger:** Monthly / Quarterly regulatory submissions 

## Assumptions & Constraints 
- Historical counterparty exposure data is available  
- PD values can be approximated from credit ratings or CDS spreads  
- Reports must run within a few minutes
- Compliance with Basel III/IV formulas for CCR capital  

## Known Unknowns / Risks 
- Missing PD data for some counterparties  
- Data entry errors in raw exposure files  
- Regulatory updates requiring recalculation methods   

## Lifecycle Mapping 
Goal → Stage → Deliverable  
- Automate monthly CCR compliance reporting → Problem Framing & Scoping (Stage 01) → Scoping paragraph + repo skeleton  
- Implement exposure + PD calculations → Modeling & Validation (Stage 02) → Scripts + validation checks  
- Generate compliance reports → Deployment (Stage 03) → Automated monthly reports (Excel/CSV/PDF)  

## Repo Plan 
/data/, /src/, /notebooks/, /docs/ ; cadence for updates
