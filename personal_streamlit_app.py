import streamlit as st

st.title("Wan Chengtao Personal Webpage")

# Sidebar navigation
sections = [
    "Personal Information",
    "EDUCATION",
    "PROFESSIONAL EXPERIENCE",
    "CO-CURRICULAR ACTIVITIES AND ACHIEVEMENTS",
    "SKILLS AND INTERESTS"
]
section = st.sidebar.radio("Navigation", sections)

if section == "Personal Information":
    st.header("Personal Information")
    st.write("""
M: (86) 18717688231 | E: willywan@126.com  
Address: Luohu District, Shenzhen
""")

elif section == "EDUCATION":
    st.header("EDUCATION")
    st.write("""
**The Chinese University of Hong Kong**  
MSc in Marketing  
Hong Kong SAR, China  2024.8-2025.6  
- Courses: Big Data Strategy, Digital Marketing, Marketing Analytics etc.

**Tongji University**  
Bachelor of German  
Shanghai, China  2020.9-2024.6  
- GPA: 89/100
- Thesis: Electrification of German Automotive Giants: A Case Study of Audi
- Achievements: Second Prize of Tongji University Outstanding Student Scholarship in the academic year 2020-2021

**Friedrich-Alexander University Erlangen-Nuremberg**  
German Studies (Public Exchange Programme)  
Erlangen, Germany  2022.9-2023.2
""")

elif section == "PROFESSIONAL EXPERIENCE":
    st.header("PROFESSIONAL EXPERIENCE")
    st.write("""
**PepsiCo China**  
Trade Marketing Intern  
Shanghai, China  2023.12-2024.4
- Assisted in budget allocation and cross-department coordination for the Lay's x KapibaraSan IP campaign, ensuring on-time product launch in retail channels.
- Streamlined billing reconciliation processes, enhancing efficiency in distributor transactions by optimizing workflow mechanisms.

**PwC China**  
Strategic Consulting Intern  
Shanghai, China  2023.9-2023.10
- Analyzed 30+ pet food industry reports, identifying market pain points and delivering 40+ actionable solutions via data visualization (PPT/charts).

**Heinz (China) Investment Co., Ltd**  
E-Commerce Intern  
Shanghai, China  2023.7-2023.8
- Tracked sales trends and competitor activities using SQL, supporting data-driven decisions for product iteration and marketing strategies.
- Optimized promotional strategies, achieving a 10% average monthly GMV growth through trend forecasting and user feedback integration.

**Venchi China**  
E-Commerce Intern  
Shanghai, China  2023.3-2023.6
- Designed annual sales strategies by monitoring key e-commerce KPIs (GMV, inventory turnover).
- Produced monthly reports tracking 5 competitors' sales activities and customer reviews on Tmall.

**Bosch (China)**  
Automotive Aftermarket Intern  
Shanghai, China  2022.7-2022.8
- Created pivot tables to streamline contract tracking, improving sales data transparency.
- Reduced contract approval time by 50% by redesigning workflow procedures.
""")

elif section == "CO-CURRICULAR ACTIVITIES AND ACHIEVEMENTS":
    st.header("CO-CURRICULAR ACTIVITIES AND ACHIEVEMENTS")
    st.write("""
**Individual Project**  
Shanghai, China  2023.6-2023.11
- Conducted Python-based sentiment analysis on customer complaints and regression analysis on product variables, delivering actionable recommendations for brand improvement.

**Innovation Programs of Tongji University**  
Project Leader  
Shanghai, China  2021.3-2022.6
- Analyzed survey data from 200+ students using clustering methods, visualized insights via scatter/line charts, and earned "Outstanding Project" recognition.

**German Department Youth League Branch**  
Class Secretary  
Shanghai, China  2021.9-2024.6
- Organized activities. Wrote the annual workbook. Recommended outstanding members of the Youth League Branch.
""")

elif section == "SKILLS AND INTERESTS":
    st.header("SKILLS AND INTERESTS")
    st.write("""
- Languages: English (CET-6: 612, IELTS 7); German (C1-C2, TEM-8)
- Computer Skills: Python, R, SQL, Excel, PowerPoint
""") 