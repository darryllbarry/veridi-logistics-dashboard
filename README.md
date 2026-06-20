# 🚚 Veridi Logistics — Delivery Performance Audit

## A. Executive Summary
Analysis of 96,478 delivered orders from Olist's Brazilian e-commerce dataset reveals 
that 8.1% of deliveries are late, directly impacting customer satisfaction. 
Northeastern states (AL, MA, PI) show the highest late delivery rates, suggesting 
a geographic distribution problem far from São Paulo's distribution centers. 
Late deliveries average 3.46/5 stars vs 4.29/5 for on-time orders, confirming 
logistics is the root cause of negative reviews. Orders placed on Mondays have 
the highest late rate at 9.1%, likely due to weekend order backlog.

## B. Project Links
- 📓 **Notebook:** [Google Colab](https://colab.research.google.com/drive/1bMbCP58dHzdhDDQS-PgdTMgSsZZJdBHl?usp=sharing)
- 📊 **Dashboard:** [Streamlit App](https://veridi-logistics-dashboard-nznybrv2ucemdpg2fa6rhv.streamlit.app/)
- 📎 **Presentation:** [Slide Deck](https://docs.google.com/presentation/d/1eMZfzeo4TCL-vxlHj-mAOBEH1C1cbYi0NGEcsEh1tRk/edit?usp=sharing)

## C. Technical Explanation

### Data Cleaning
- Deduplicated reviews — kept only the most recent review per order
- Excluded canceled/unavailable orders, keeping 96,478 delivered orders
- Parsed all date columns and computed delay as estimated minus actual delivery date
- Classified orders as On Time, Late (1-5 days), or Super Late (>5 days)

### Candidate's Choice — Late Delivery Rate by Day of Purchase
Monday orders have the highest late rate at 9.1% vs Sunday at 7.5%.
Weekend order volume creates a processing backlog that strains Monday dispatch capacity.
**Business value:** Operations teams can proactively increase Monday staffing or adjust 
estimated delivery dates for Monday orders to set realistic customer expectations.
