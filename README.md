# statistical_analysis_program

## Background

Every academical research has 2 competing hypothesis:
1. null hypothesis (H0) - the effect being studies does not exist and any experimentally observed effect is due to chance alone.  
2. Alternative hypothesis (H1) - the effect being studied exhibit a true phenomenon.
   
Therefore, there is a need in tools to prove that the research findings have statistical significance, meaning the probability to get a certain result or more extreme one (a.k.a the p-value) would be very low, under the assumption the null hypothesis is true.

In order to prove it, the most common method nowdays is to choose an α value, the study's significance level (defined as the probability to reject H0, given H0 is true), which usually chosen to be 5% or lower, depends on the study. The researcher also need to choose the type of tail-test:
1. One-tail test: Specifying direction of the difference between the means,so that H1 states if the popluation's mean is smaller or bigger than the hypothesized mean. Therefore, the rejection region will be placed entirely in one tail of the sampling distribution, either the upper tail (right-sided test) or the lower tail (left-sided test).
2. Two-tail test: Not specifying the direction of difference, so that H1 only states that the population's mean is different than the hypothesized mean. Therefore, the rejection region is divided equally between both tails of the sampling distribution.

Afterwards, the p-value will be calculated from the data using different tests, intended for different sets of data. The p-value will be compared to α, and the result will be declared as statistically significant, by the standards of the study, if p-value ≤ α.

## Goal of the project

The project is intended to provide a tool that simplifies the statistical analysis stage that comes after an experiment. Insted of writing a program that will analyse the results for each experiment specifically, this program is meant to provide a general tool to different experiments. 

Another goal is to add more tests as time passes in order to enrich the program with as many tools as possible.

Note that the program still requires basic statistical knowledge, in order to to match the right statistical test to the experiment.

This project was originally implemented as part of the [Python programming course](https://github.com/szabgab/wis-python-course-2024-04) at the [Weizmann Institute of Science](https://www.weizmann.ac.il/) taught by [Gabor Szabo](https://szabgab.com/).

## Test types

### 1. Z-test:

* Background: According to the CLT, the sampling distribution of the mean of sample group of n size, will be distributed normally with a mean that equals to the true mean of the population with a std of 𝜎/sqrt(𝑛) (𝜎 is the std of the population).
Under the null hypothesis, we will assume that the mean recived in our experiment is part of the sampling distribution of the population. 
Therefore, if we standardize the mean that was recieved we will get a Z-score, which can be used to calculate the probability to recieve this mean or a more extreme value. This is the p-value, which we will compare to α  that easdeterminted in the beggining of the experiment.If the p-value if smaller than the alpha we could reject the null hypothesis and say that mean recieved is signicantlly different from the mean of the population. 

* Use when: Comparing our experiment's mean to the population's one, when the mean and the variance of the population is known.

* Assumptions:
1. Population's mean (μ) and std (σ) are known.
2. The population from which the sample is drawn follow a normal distribution. Alterntively, the sample size is large enough for the sampling distribution of the sample mean to be approximately normal (n ≥ ~30)

### 2. One sample t-test:

* Background: Test which is simillar to the Z-test, however it is used when the variance in the population is not known. Instead, we will evaluate the variance in the population using the variance recieved from the results. Since it adds uncertainty, the sampling distribution of the mean will follow a t-distribution with n-1 degrees of freedom.
  𝑡 =ത𝑋𝑛− 𝜇𝑆𝑛~ 𝑡𝑛−1

* Use when: Comparing our experiment's mean to the population's one, when it is known.

* Assumptions: 
1. Population's mean (μ) is known.
2. The population from which the sample is drawn follow a normal distribution. Alterntively, the sample size is large enough for the sampling distribution of the sample mean to be approximately normal (n ≥ ~30)

### 3. Two-sample paired sample t-test:

* Background: Test used for comparing 2 samples groups, in which we can match between each sample in group 1 to sample in group 2. In this case, we can calculate the differences between each pair of samples, and preform a one-sample t-test on the differences' mean, which will be zero most of the times (since the null hypothesis is that there is no effect), using also the variance of the differences.

* Use when: comparing between the means of 2 groups, when it is possible to match between each sample in the first group to a sample in the second group, for example - comparing the effect of a drug before and after consumption.

* Assumptions:

### 4. Two-sample independent t-test:

* Background: test used for comparing the means of 2 different samples groups, that cannot be matched. note! In most cases it will be preferable to preform a paired t-test over independent t-test, since this test will have more power (the probability to reject H0 given that H1 is true). in this test we will calculate the difference between the means and will use the weighted average of their variances.

* Use when: comparing the means of 2 different groups.

* Assumptions:

### 5. Pearson correlation:

* Backgorund: measures the strength and direction of the linear relationship between two variables
test to measure the covariance of the 2 contious variables relative to their variances, in order to see if those variables change together in some manner (positive or negative). r is calculated by: 
if rho is not zero then:

* Use when: test to see if 2 variables change together significatelly.

* assumptions:

### 6. Linear regression:
* Background: Builds on correlation to predict values.
Uses known relationships to predict the value of one variable based on another.

* meant for:
  
* assumptions:

## The code

the program takes as an input a file that summerizes the results of the experiment and the test that the user would like to preform, with an given alpha and two vs. one tail test, and will print as an output the p-value of the test, and weather it is able to reject the null hypothesis. 
for tests 1-2 the program will expect to recieve one column of the samples results, and the mean of the population. in test 1 it will also require the variance in population.
for the remaining tests the program will expect 2 columns of results.
