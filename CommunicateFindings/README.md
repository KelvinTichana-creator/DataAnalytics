ProsperLoanData Exploratory Analysis

#Introduction

In this project, we will be exploring the ProsperLoanData dataset, which contains information about loans facilitated by Prosper, a peer-to-peer lending platform. The dataset includes information about the borrowers, such as their employment status, credit score, and debt-to-income ratio, as well as information about the loans themselves, such as the loan amount, interest rate, and term.

Our goal is to perform an exploratory analysis on this dataset, using univariate, bivariate, and multivariate visualizations to better understand the relationships between the different variables in the dataset and to uncover any interesting patterns or trends.

#Dataset

The ProsperLoanData dataset contains 113,937 observations and 81 variables.

#Methodology

I will be using Python and its data science libraries, such as Pandas, Matplotlib, and Seaborn, to perform the exploratory analysis. The analysis will be broken down into three parts:

#Summary of Findings
Univariate Exploration: In this part, we will explore individual variables in the dataset, looking at their distribution, central tendency, and variability.
Bivariate Exploration: In this part, we will explore the relationship between pairs of variables in the dataset, looking for any correlations or patterns.
Multivariate Exploration: In this part, we will explore the relationships between multiple variables in the dataset, using advanced visualization techniques such as heatmaps and clustering.
RESULTS:
The majority of the loanees are employed
Histogram:
The distribution of BorrowerAPR is approximately normal, with a peak around 0.2.
The majority of loans have an APR between 0.1 and 0.3.
There are a few loans with APRs as high as 0.5.
Kernel density plot:
Confirms the findings from the histogram, showing a normal-like distribution with a peak around 0.2.
Box plot:
The median APR is around 0.2, with the majority of loans falling between 0.1 and 0.3.
There are a few loans with APRs above 0.4, which are considered outliers.
The correlation coefficient for loan original amount to stated income is 0.183
We can see that as the Prosper Rating improves (i.e., goes from HR to AA), the mean BorrowerRate decreases. This is consistent with the idea that borrowers with better creditworthiness are able to secure loans at lower interest rates

employed borrowers have the highest count of loans, followed by full-time employed borrowers. 
From the scatter plot, we can see that there is a weak positive relationship between loan amount and borrower's APR. As loan amount increases, borrower's APR tends to increase as well, but the relationship is not very strong. However, we can also see that there are some outliers where larger loans have lower APRs than expected.
From the scatterplot matrix, we can see that there is a strong positive correlation between loan amount and borrower rate, meaning that as loan amount increases, borrower rate tends to increase as well. We can also see that there is a weak negative correlation between credit score range and borrower rate, meaning that as credit score range increases, borrower rate tends to decrease slightly.

We can also see that the distribution of loan amount is right-skewed, . The distribution of borrower rate is  with peaks around 680 and 760.

LoanOriginalAmount is strongly positively correlated with MonthlyLoanPayment and moderately positively correlated with Term and Investors.
MonthlyLoanPayment is strongly positively correlated with LoanOriginalAmount and moderately positively correlated with StatedMonthlyIncome.
Term is moderately positively correlated with LoanOriginalAmount and MonthlyLoanPayment.
BorrowerAPR is strongly negatively correlated with CreditScoreRangeLower and CreditScoreRangeUpper.
StatedMonthlyIncome is weakly positively correlated with AvailableBankcardCredit, BankcardUtilization, and CreditScoreRangeUpper, and weakly negatively correlated with DebtToIncomeRatio.
AvailableBankcardCredit is weakly positively correlated with StatedMonthlyIncome, BankcardUtilization, and CreditScoreRangeUpper.
BankcardUtilization is weakly positively correlated with StatedMonthlyIncome and AvailableBankcardCredit, and weakly negatively correlated with CreditScoreRangeUpper.
CreditScoreRangeLower and CreditScoreRangeUpper are strongly positively correlated.
Borrowers with higher monthly incomes tend to take out larger loans and make higher monthly loan payments.
There is a positive relationship between LoanOriginalAmount and MonthlyLoanPayment, which is consistent with our previous findings.
The data points show a wide range of StatedMonthlyIncome
From the heatmap, we can see that most loans are current, followed by completed loans. We can also see that most loans have a term of 36 months, with fewer loans having a term of 60 months. In terms of credit grade, most loans have a credit grade of C or D, with fewer loans having a credit grade of A or AA. The heatmap also shows that loans with a term of 60 months and a credit grade of A or AA are relatively rare.

From the scatter plot, we can see that there is a positive relationship between loan original amount and stated monthly income. As loan original amount increases, stated monthly income tends to increase as well. We can also see that the size and color of each data point represent Prosper rating, with higher Prosper ratings represented by larger and darker data points
#Key insights for presentation

By the end of this project, we hope to have a better understanding of the ProsperLoanData dataset and the relationships between its variables. We will summarize our findings in a Jupyter Notebook, including visualizations, key insights, and recommendations for future analysis.
The presentation focuses on the visualizations that show the rekationship between borrower APR and amount loaned, the distribution of the APR, the distribution of income, the distribution of professions, the employment status vs term, the year vs the loans, months vs loans, and days vs loans.
