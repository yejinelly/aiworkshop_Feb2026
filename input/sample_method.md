## Methods

### Participants

A total of 420 adolescents (ages 13-18, M = 15.4, SD = 1.6) were recruited from 12 high schools across South Korea. Schools were stratified by region type: urban (n = 180), suburban (n = 140), and coastal (n = 100). Coastal regions were defined as areas within 10 km of the shoreline, selected to examine potential differences in climate anxiety based on direct exposure to sea-level rise and coastal weather events.

Inclusion criteria were: (a) enrolled in grades 7-12, (b) Korean language proficiency, and (c) parental consent and student assent. Exclusion criteria included current psychiatric treatment or inability to complete online surveys. The sample was 52% female, with a mean household income of KRW 5.2 million/month (SD = 2.1 million). Income levels were categorized as low (< 3 million, 24%), middle (3-7 million, 51%), and high (> 7 million, 25%).

### Measures

**Climate Anxiety Scale (CAS; Clayton & Karazsia, 2020)**
A 22-item measure assessing cognitive, emotional, and behavioral dimensions of climate anxiety. Subscales include: (a) cognitive-emotional impairment (8 items), (b) functional impairment (6 items), and (c) personal experience of climate change (8 items). Items are rated on a 5-point Likert scale (1 = never to 5 = almost always). Internal consistency in the current sample was excellent (α = .91).

**Patient Health Questionnaire-9 (PHQ-9; Kroenke et al., 2001)**
A 9-item screening tool for depressive symptoms over the past two weeks. Scores range from 0-27, with higher scores indicating greater severity. The Korean version demonstrated good reliability (α = .87).

**Perceived Stress Scale (PSS-10; Cohen et al., 1983)**
A 10-item measure of perceived stress in the past month. The Korean adaptation showed acceptable reliability (α = .84).

**Demographics Questionnaire**
Included age, gender, grade level, residential region (urban/suburban/coastal), distance from coastline (km), household monthly income, parental education level, and history of exposure to extreme weather events (flooding, typhoons, heatwaves).

### Procedure

This study employed a longitudinal design with four waves of data collection over 24 months (baseline, 8 months, 16 months, 24 months). At each wave, participants completed online surveys via Qualtrics, taking approximately 25-30 minutes. Surveys were administered during school hours in computer labs, with trained research assistants available for questions.

At baseline, participants also completed a brief interview about their personal experiences with climate-related events (e.g., property damage from flooding, evacuation due to typhoons). Follow-up surveys were sent via email with two reminders. Retention rates were 94% at Wave 2, 89% at Wave 3, and 85% at Wave 4.

The study was approved by the Institutional Review Board of Seoul National University (IRB-2024-0123). All participants provided informed consent (parental consent for minors under 14).

### Data Analysis

Data were analyzed using R version 4.3.1. Preliminary analyses included descriptive statistics, missing data patterns (< 5% missing, handled via multiple imputation), and assumption checks for normality and multicollinearity.

**Primary analyses:**
1. Multilevel growth models (MLM) were used to examine trajectories of climate anxiety over time, with time points (Level 1) nested within individuals (Level 2). Random intercepts and slopes were estimated to capture individual variability in initial levels and rates of change.

2. Regional differences in climate anxiety trajectories were examined by including region type (urban, suburban, coastal) as a Level 2 predictor, with planned contrasts comparing coastal vs. non-coastal regions.

3. Moderation analyses tested whether household income moderated the relationship between regional residence and climate anxiety trajectories, using cross-level interactions.

4. Mediation analyses examined whether perceived stress mediated the relationship between climate anxiety and depressive symptoms at each wave, using multilevel structural equation modeling (MSEM) in Mplus 8.6.

Effect sizes were reported as standardized coefficients (β) for fixed effects and intraclass correlation coefficients (ICC) for random effects. Statistical significance was set at α = .05, with Bonferroni correction applied for multiple comparisons.
