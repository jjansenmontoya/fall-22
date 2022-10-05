library(faraway)

# 6.2a
lmod <- lm(gamb ~ ..., data = teengamb)
plot(fitted(lmod), resid(lmod))
abline(h =0)

# 6.2b
qqnorm(resid(lmod))
qqline(resid(lmod))

# 6.2c
hatvalues(lmod) > 2*mean(hatvalues(lmod))

# 6.2d
rstandard(lmod)[abs(rstandard(lmod))>2]

#6.2e
cooks.distance(lmod)[39] > 4/length(cooks.distance(lmod))
cooks.distance(lmod)[47] > 4/length(cooks.distance(lmod))
cooks.distance(lmod)[69] > 4/length(cooks.distance(lmod))
cooks.distance(lmod)[95] > 4/length(cooks.distance(lmod))
cooks.distance(lmod)[97] > 4/length(cooks.distance(lmod))

# 6.2f 
