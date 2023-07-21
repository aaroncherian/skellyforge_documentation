# Interpolation

Motion capture data often contains gaps or missing data points due to various reasons such as occlusions, markers falling off, or data corruption. Interpolation is the process of estimating the missing data points based on the known ones.

In SkellyForge, we use Pandas interpolation methods to estimate these missing values. There are three primary methods we allow users to choose from: 'linear', 'cubic', and 'spline'. 

## Interpolation Options

SkellyForge allows users to utilize several powerful interpolation methods using the pandas library to estimate missing values in their datasets.

### Linear Interpolation
Linear interpolation is the simplest form of interpolation. When a data point is missing, this method simply draws a straight line between the two nearest known points and uses that line to estimate the missing value. It's best used when your data points are roughly in a straight line or the data changes slowly and smoothly.

### Cubic Interpolation
The 'cubic' method in SkellyForge corresponds to what is often known as 'cubic spline interpolation'. This is a more sophisticated method than linear interpolation. Instead of just drawing a straight line between known points, cubic interpolation fits a smooth curve through these points. The curve is made up of small cubic (or third-degree polynomial) segments, and each segment between two known points is determined only by the data on that segment. This allows it to capture more complex patterns in the data.

### Spline Interpolation
The term 'spline' in general refers to a piecewise-defined polynomial function that can be used for interpolation. The cubic interpolation methd above would be considered a '3rd order spline interpolation'. For example, a 4th order spline would fit segments of 4th degree (or quartic) polynomials to the data. Higher order spline interpolation could potentially capture even more complex patterns in the data, but they can also overfit the data and lead to wild swings in the interpolated values. 

Using spline interpolation will take *much* longer than the other methods however. 
## Which method should you choose?
There's no one-size-fits-all solution here. The best method will largely depend on the characteristics of your specific data. For data that changes slowly or has small gaps, linear interpolation mgiht be a good choice. If you have more complex patterns or movements, higher order spline interpolations might be more suitable. 

Ultimately, choosing the right interpolation method might require some trial and error. The Interpolation tab in SkellyForge allows you to visualize the impact of different interpolation methods on your data. You can try different methods, look at how they affect the trajectories, and decide which one best preserves the true motion.