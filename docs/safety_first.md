# Robotics Safety First

Robotics is software that can move mass through the world. Treat safety as a design requirement from the first simulation, not a final review.

## Core Rule

No learned policy should be the only safety layer.

Use independent safety mechanisms:
- Speed limits
- Joint limits
- Workspace limits
- Collision checks
- Current and torque limits
- Emergency stop
- Watchdog timeouts
- Human exclusion zones
- Logging and replay

## Simulation Safety

Even in simulation, practice safe habits:
- Track collisions.
- Track action saturation.
- Track near misses.
- Track policy uncertainty.
- Track whether the robot reached a state that was absent from training data.

## Real Hardware Checklist

Before moving:
- The robot is mechanically assembled and inspected.
- The workspace is clear.
- Emergency stop is tested.
- Motors start disabled.
- First motion is slow and small.
- Joint limits are configured.
- Controller outputs are clipped.
- Logs are enabled.
- A human can disable power without entering the workspace.

Before learning-based control:
- Run the classical controller first.
- Run the policy in shadow mode.
- Compare policy commands to safe controller commands.
- Enable only one axis or low-power mode first.
- Add fallback behavior.
- Collect failure logs.

## Watchdog Pattern

A watchdog disables motion when commands stop arriving or arrive too late.

Use watchdogs for:
- Motor commands
- Sensor streams
- Network links
- Teleoperation
- Learned policy inference

## Safety Metrics

Track:
- Collision rate
- Near-miss count
- Emergency-stop count
- Watchdog trip count
- Max speed
- Max torque/current
- Time outside planned workspace
- Human intervention rate

## Safety In Modern Robot Learning

VLA and diffusion policies can produce plausible actions that are physically unsafe. Add:
- Action clipping
- Workspace guards
- Collision-checking filters
- Language-command allowlists for risky tasks
- Human confirmation for irreversible actions
- Policy confidence and fallback controllers

Safety is not an obstacle to mastery. It is part of mastery.
