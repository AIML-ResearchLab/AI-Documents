# 21 - Advanced Time Series and State-Space Models

## 21.1 Classical Models
- AR, MA, ARMA
- ARIMA and seasonal SARIMA

Choose model family based on stationarity and seasonality diagnostics.

## 21.2 State-Space Models
Represent latent process and observation equations.

Core algorithms:
- Kalman filter (online estimation)
- Kalman smoother (retrospective refinement)

## 21.3 Volatility Modeling
- ARCH/GARCH for conditional variance dynamics
- Useful in risk-sensitive forecasting

## 21.4 Change-Point Detection
Detect regime changes in mean/variance/structure.
Critical for production monitoring.

## 21.5 Multivariate Time Series
- VAR models
- Dynamic factor models
- Granger-causality intuition (predictive, not causal proof)

## 21.6 Forecast Uncertainty
Always produce prediction intervals, not only point forecasts.

## 21.7 Backtesting and Validation
- Rolling-origin evaluation
- Time-respecting splits
- Forecast horizon-specific metrics

## 21.8 Real-Time Example
Forecast API traffic by minute:
- Use state-space model
- Trigger autoscaling from upper prediction interval
- Log interval coverage drift weekly

