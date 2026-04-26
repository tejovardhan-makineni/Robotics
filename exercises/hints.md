# Exercise Hints

Use this only after struggling for a bit.

## Kalman Filter Velocity State

Use state `[position, velocity]`.

The motion model can be:

```text
x_next = A x + B u
A = [[1, dt],
     [0, 1]]
B = [[0.5 dt^2],
     [dt]]
```

If your measurement is position only, use:

```text
H = [[1, 0]]
```

## Three-Link Arm

Forward kinematics is the cumulative sum of link vectors:

```text
x = l1 cos(q1) + l2 cos(q1 + q2) + l3 cos(q1 + q2 + q3)
y = l1 sin(q1) + l2 sin(q1 + q2) + l3 sin(q1 + q2 + q3)
```

The Jacobian columns are derivatives of endpoint position with respect to each joint.

## DAgger-Style Correction

Run the cloned policy. Save states where it drifts. Ask the expert what action should have been taken at those states. Add those new state-action pairs to the dataset and retrain.

## Safety Filter

A simple safety filter can:

1. Clip action norm.
2. Predict the next position.
3. Reject the action if the next position is inside an obstacle or outside workspace.
4. Replace rejected action with stop or retreat.

## Paper Reproduction

Do not reproduce the whole paper first. Reproduce the smallest meaningful claim:

- One environment
- One baseline
- One metric
- One ablation

Then expand.
