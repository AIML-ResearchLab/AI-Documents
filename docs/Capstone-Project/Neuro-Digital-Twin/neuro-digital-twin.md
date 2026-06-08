---
title: Clinical Brain Twin
hide:
  - toc
---

<div class="cbt-page">
  <section class="cbt-hero">
    <div class="cbt-hero__rail">
      <div>
        <div class="cbt-hero__eyebrow">Clinical Brain Twin</div>
        <h1>Neurocritical operations console</h1>
      </div>
      <div class="cbt-live-pill">
        <span class="cbt-live-pill__dot"></span>
        Realtime twin connected
      </div>
    </div>
    <p class="cbt-hero__lead">
      An enterprise command surface for live neurologic monitoring, forecast validation, policy-aware
      interventions, and clinician sign-off from one realtime workspace.
    </p>
    <div class="cbt-chip-row">
      <span class="cbt-chip cbt-chip--soft">Bedside telemetry streaming</span>
      <span class="cbt-chip cbt-chip--soft">Counterfactual therapy simulator</span>
      <span class="cbt-chip cbt-chip--soft">Human approval with audit trail</span>
    </div>
  </section>

  <section class="cbt-command-grid">
    <article class="cbt-command-card">
      <span class="cbt-command-card__label">Active patient</span>
      <strong>CBT-1042</strong>
      <p>Post-op neuro ICU, multimodal feeds healthy across ICP, EEG, MAP, and ventilator channels.</p>
    </article>
    <article class="cbt-command-card">
      <span class="cbt-command-card__label">Twin sync</span>
      <strong>24s behind live bedside</strong>
      <p>Inference cadence 2.1s with last state merge at 08:14:26 and no missing packets.</p>
    </article>
    <article class="cbt-command-card">
      <span class="cbt-command-card__label">Risk posture</span>
      <strong>Moderate, improving</strong>
      <p>Pressure stability improved after vasopressor tuning, though seizure likelihood remains elevated.</p>
    </article>
    <article class="cbt-command-card">
      <span class="cbt-command-card__label">Governance</span>
      <strong>12 of 12 safety gates green</strong>
      <p>Medication, perfusion, ventilation, and escalation rules passed before recommendation release.</p>
    </article>
  </section>

  <section class="cbt-live-grid">
    <article class="cbt-panel cbt-panel--spotlight">
      <div class="cbt-panel__header">
        <div>
          <span class="cbt-section-kicker">Decision Workspace</span>
          <h2>Live intervention window</h2>
        </div>
        <span class="cbt-status-pill cbt-status-pill--success">Awaiting clinician action</span>
      </div>
      <p class="cbt-panel__intro">
        Recommendation stays open until the care team approves, requests changes, or escalates the case.
        No forced timeout, no auto-dismiss, and a persistent longitudinal audit trail.
      </p>

      <div class="cbt-recommendation-card">
        <div class="cbt-recommendation-card__header">
          <div>
            <span class="cbt-recommendation-card__label">Primary recommendation</span>
            <h3>Increase propofol infusion from 18 to 22 mcg/kg/min</h3>
          </div>
          <span class="cbt-chip cbt-chip--accent">Simulation confidence 88%</span>
        </div>
        <p class="cbt-note">
          Maintain CPP between 65-70 mmHg, keep continuous EEG active, and trigger a nurse-facing reassessment
          workflow 15 minutes after titration.
        </p>

        <div class="cbt-detail-grid">
          <div class="cbt-detail-card">
            <span>Predicted ICP delta</span>
            <strong>-3.8 mmHg</strong>
          </div>
          <div class="cbt-detail-card">
            <span>Hemodynamic downside</span>
            <strong>Low</strong>
          </div>
          <div class="cbt-detail-card">
            <span>Response horizon</span>
            <strong>120 min</strong>
          </div>
          <div class="cbt-detail-card">
            <span>Escalation risk</span>
            <strong>9%</strong>
          </div>
        </div>
      </div>

      <div class="cbt-signal-strip">
        <div class="cbt-signal-card">
          <span>ICP waveform</span>
          <div class="cbt-bars cbt-bars--blue">
            <i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i>
          </div>
          <strong>19 mmHg</strong>
        </div>
        <div class="cbt-signal-card">
          <span>CPP reserve</span>
          <div class="cbt-bars cbt-bars--teal">
            <i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i>
          </div>
          <strong>67 mmHg</strong>
        </div>
        <div class="cbt-signal-card">
          <span>EEG burden</span>
          <div class="cbt-bars cbt-bars--amber">
            <i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i>
          </div>
          <strong>Low</strong>
        </div>
      </div>

      <div class="cbt-insight-grid">
        <div class="cbt-insight-card">
          <h3>Why the model is confident</h3>
          <ul class="cbt-list">
            <li>Recent ICP spikes cluster around stimulation events despite steady oxygenation and temperature.</li>
            <li>Counterfactual runs project fewer rebound excursions above the neuro intervention threshold.</li>
            <li>No projected interaction conflicts with the current vasopressor and anti-epileptic regimen.</li>
          </ul>
        </div>
        <div class="cbt-insight-card">
          <h3>Realtime evidence stack</h3>
          <div class="cbt-evidence-list">
            <div class="cbt-evidence-item">
              <strong>Signal fusion</strong>
              <p>Arterial line, ICP, EEG, and ventilator streams align to a stress-response pattern with stable oxygen reserve.</p>
            </div>
            <div class="cbt-evidence-item">
              <strong>Forecast engine</strong>
              <p>Projected next 120 minutes show fewer pressure excursions after titration than the current protocol path.</p>
            </div>
            <div class="cbt-evidence-item">
              <strong>Policy engine</strong>
              <p>All sedation, MAP floor, and respiratory reserve constraints passed in the last release cycle.</p>
            </div>
          </div>
        </div>
      </div>

      <div class="cbt-action-row">
        <a class="md-button md-button--primary" href="javascript:void(0)">Approve intervention</a>
        <a class="md-button" href="javascript:void(0)">Request revision</a>
        <a class="md-button" href="javascript:void(0)">Escalate to attending</a>
      </div>
    </article>

    <aside class="cbt-side-stack">
      <section class="cbt-panel cbt-panel--dense">
        <div class="cbt-panel__header">
          <div>
            <span class="cbt-section-kicker">Live Feed</span>
            <h2>Event stream</h2>
          </div>
          <span class="cbt-chip cbt-chip--neutral">Auto-refreshing context</span>
        </div>
        <div class="cbt-timeline">
          <div class="cbt-timeline__item">
            <span class="cbt-timeline__time">08:14:26</span>
            <div>
              <strong>Twin state merged</strong>
              <p>ICP, MAP, sedation pump, EEG summary, and ventilator telemetry all reconciled.</p>
            </div>
          </div>
          <div class="cbt-timeline__item">
            <span class="cbt-timeline__time">08:14:09</span>
            <div>
              <strong>Counterfactual run completed</strong>
              <p>Five intervention variants scored; propofol titration ranked highest on stability-to-risk ratio.</p>
            </div>
          </div>
          <div class="cbt-timeline__item">
            <span class="cbt-timeline__time">08:13:41</span>
            <div>
              <strong>EEG spike cluster softened</strong>
              <p>Burden moved from moderate to low after bedside stimulation ceased.</p>
            </div>
          </div>
          <div class="cbt-timeline__item">
            <span class="cbt-timeline__time">08:12:58</span>
            <div>
              <strong>Nurse workflow notified</strong>
              <p>Prepared q15 minute neuro assessment checklist if intervention is approved.</p>
            </div>
          </div>
        </div>
      </section>

      <section class="cbt-panel cbt-panel--dense">
        <div class="cbt-panel__header">
          <div>
            <span class="cbt-section-kicker">Supervisory Layer</span>
            <h2>Clinician sign-off</h2>
          </div>
          <span class="cbt-chip cbt-chip--soft">Responsible AI in loop</span>
        </div>

        <div class="cbt-checklist">
          <div class="cbt-checklist__item">
            <strong>Recommendation validated</strong>
            <p>Matches bedside intent for ICP control while preserving perfusion reserve.</p>
          </div>
          <div class="cbt-checklist__item">
            <strong>Safety review cleared</strong>
            <p>MAP buffer, ventilation tolerance, and seizure monitoring coverage remain acceptable.</p>
          </div>
          <div class="cbt-checklist__item">
            <strong>Escalation path armed</strong>
            <p>Attending review and intervention rollback are available if post-change trends drift.</p>
          </div>
        </div>

        <div class="cbt-comment-box">
          <span class="cbt-comment-box__label">Clinician note</span>
          <p>
            Acceptable if MAP remains above 72. Continue q15 minute neuro review after the first dose change
            and reopen simulation if EEG burden rises again.
          </p>
        </div>
      </section>
    </aside>
  </section>

  <section class="cbt-lower-grid">
    <article class="cbt-panel">
      <span class="cbt-section-kicker">Forecast Horizons</span>
      <h2>Projected system behavior</h2>
      <div class="cbt-forecast-grid">
        <div class="cbt-forecast-card">
          <span>15 min</span>
          <strong>Pressure spikes flatten</strong>
          <p>Immediate stabilization with low vasopressor sensitivity.</p>
        </div>
        <div class="cbt-forecast-card">
          <span>1 hour</span>
          <strong>CPP remains in target</strong>
          <p>Median forecast stays within goal with mild variability.</p>
        </div>
        <div class="cbt-forecast-card">
          <span>6 hours</span>
          <strong>Repeat review recommended</strong>
          <p>Model confidence tapers as medication response uncertainty widens.</p>
        </div>
      </div>
    </article>

    <article class="cbt-panel">
      <span class="cbt-section-kicker">Operational Continuity</span>
      <h2>After approval</h2>
      <div class="cbt-handoff-list">
        <div class="cbt-handoff-item">
          <strong>Write-back to audit ledger</strong>
          <p>Decision, clinician identity, rationale, and policy snapshot are stored as a durable record.</p>
        </div>
        <div class="cbt-handoff-item">
          <strong>Refresh the twin</strong>
          <p>Live forecast reruns as soon as the bedside order is confirmed by the care team.</p>
        </div>
        <div class="cbt-handoff-item">
          <strong>Persist the workspace</strong>
          <p>The same console remains active as a shift-to-shift source of truth for neuro ICU coordination.</p>
        </div>
      </div>
    </article>
  </section>
</div>
