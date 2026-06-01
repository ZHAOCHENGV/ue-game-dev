# Character Movement Prediction Matrix

| Scenario | Authority Owner | Client Prediction | Server Correction | Evidence |
|---|---|---|---|---|
| Sprint | Server validates intent | Client predicts speed change | Correct movement mode and max speed | Two-client PIE with packet lag |
| Dash | Server validates cooldown and direction | Client predicts launch | Reconcile location and montage | Listen server and dedicated server |
| Root motion ability | Server owns ability activation | Client predicts montage when allowed | Correct montage section and root motion source | GAS prediction key log |
| Custom movement mode | Server owns mode transition | Client predicts mode if deterministic | Correct movement mode byte and velocity | `p.NetShowCorrections 1` |

## Evidence Checklist

- Record whether the issue appears on listen server, dedicated server, autonomous proxy, or simulated proxy.
- Capture `p.NetShowCorrections 1` output when the symptom is snapping, rubber-banding, or jitter.
- Compare client intent inputs with server-authoritative movement mode, acceleration, velocity, and timestamp.
- Validate packet lag and packet loss scenarios before claiming prediction is stable.
