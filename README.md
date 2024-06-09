# statistical_analysis_program

## background
In any academical research there is a need in proving that the research findings are statistical significant and show a true phenomenon. 
In order to prove it, it is common nowdays to calculate p-values from the test data compared to the null hypothesis, representing the probability to recieve a value such as the one recieved or more extreme, under the assumption the null hypothesis is true.

the point of the project is to create a tool that simplifies the statistical analysis after the experiment, insted of writing a program that will anlyse the results for each experiment. the goal is to add more kinds of tests as time passes in order for the program to be generic as possible?

there are different tests to different sets of data:
1. Z-test:
background: according to the CLT, the sampling distribution of the mean of samples in the size of n,  will be distributed normally with a mean equal to the true mean of the population and std of sigma/sqrt(n). 
under the null hypothesis (H0), we will assume that the mean recived in our experiment is part of the sampling distribution of the population. 
therefore, if we standerize the mean that was calculted in the experiment we can get a Z-score and to calculate the probability to recieve this mean or a more extreme value. this is the p-value, which we will compare to an alpha determinted in the beggining of the experiment, and if the p-value if smaller than the alpha we could reject the null hypothesis and say that mean recieved is signicantlly different from the mean of the population. 
meant for: comparing our experiment to the population, when the mean and the variance of the population is known.
assumptions:
2. one sample t-test: test which is simillar to the Z-test, however it is used when the variance in the population is not known. therefore, we will evaluate the variance in the population using the variance recived from the samples. since it adds uncertianty, the sampling distribution of the mean will be a t-distribution with n-1 degrees of freedom.
meant for: comparing our experiment to the population, when the mean is known and the variance of the population is  not known.
assumptions:
3. two-sample paired sample t-test: test used for comparing 2 samples groups, in which we can match between each sample in group 1 to sample in group 2. in this case, we can calculate the differences between each pair of samples, and preform a one-sample t-test on the difference, which will be zero most of the times (since the null hypothesis is that there is no effect). we will also use the variance of the differences.
meant for: comparing between the means of 2 groups, when it is possible to match between each sample in the first group to a sample in the second group, for example- comparing the effect of a drug before and after consumption.
assumptions:
4. two-sample independent t-test: test used for comparing the means of 2 different samples groups, that cannot be matched. note! In most cases it will be preferable to preform a paired t-test over independent t-test, since this test will have more power (the probability to reject H0 given that H1 is true). in this test we will calculate the difference between the means and will use the weighted average of their variances.
meant for: comparing the means of 2 different groups.
assumptions:
5. Pearson correlation: measures the strength and direction of the linear relationship between two variables
test to measure the covariance of the 2 contious variables relative to their variances, in order to see if those variables change together in some manner (positive or negative). r is calculated by: 
if rho is not zero then:
meant for: test to see if 2 variables change together significatelly.
assumptions:
6. linear regression: Builds on correlation to predict values.
Uses known relationships to predict the value of one variable based on another.
assumptions:

the code
the program takes as an input a file that summerizes the results of the experiment and the test that the user would like to preform, with an given alpha and two vs. one tail test, and will print as an output the p-value of the test, and weather it is able to reject the null hypothesis. 
for tests 1-2 the program will expect to recieve one column of the samples results, and the mean of the population. in test 1 it will also require the variance in population.
for the remaining tests the program will expect 2 columns of results.
