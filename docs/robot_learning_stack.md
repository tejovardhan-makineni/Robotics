# Robot Learning Stack

Robot learning is not just "train a model." It is a pipeline.

## The Pipeline

1. Define the task.
2. Define observations.
3. Define actions.
4. Choose a robot embodiment.
5. Collect demonstrations or simulation rollouts.
6. Normalize and validate data.
7. Train a policy.
8. Evaluate closed-loop behavior.
9. Add safety filters.
10. Deploy gradually.
11. Log failures.
12. Add data for failures.
13. Retrain.

## Observation Design

Common observations:
- Joint positions
- Joint velocities
- End-effector pose
- Gripper state
- RGB images
- Depth images
- Point clouds
- Force/torque
- Tactile readings
- Language instruction

Bad observation design creates hidden state. If the policy needs information that is not observed, it must guess.

## Action Design

Common actions:
- Joint position targets
- Joint velocity targets
- Joint torque
- End-effector delta pose
- Gripper open/close
- Action chunks
- Discrete action tokens

Good action spaces are:
- Controllable
- Smooth
- Safe to limit
- Consistent across data
- Matched to robot hardware

## Data Quality

Check:
- Are timestamps consistent?
- Are actions delayed relative to observations?
- Are cameras calibrated?
- Are frames named and documented?
- Are failed demonstrations included or excluded intentionally?
- Are train and validation splits separated by scene/object/task when testing generalization?

## Policy Families

### Behavior cloning

Best first method. Fast, simple, data hungry, sensitive to distribution shift.

### Action chunking

Predicts multiple future actions. Useful when single-step control is jittery or temporally inconsistent.

### Diffusion policy

Models a distribution over action sequences. Useful for multimodal manipulation where averaging actions fails.

### Flow policy

Related distributional action generation with continuous transformation from noise to action.

### Reinforcement learning

Useful in simulation or when rewards are clear and exploration is safe. Expensive on real robots.

### Vision-language-action models

Map images and language instructions to actions. Useful for generalization, but still require careful embodiment, action representation, data, and safety.

## Evaluation

Track:
- Success rate
- Episode length
- Collision rate
- Recovery success
- Latency
- Intervention rate
- Generalization to new objects
- Generalization to new scenes
- Generalization to new language instructions

Offline loss is not enough. A policy with low validation loss can still fail when closed-loop errors accumulate.
