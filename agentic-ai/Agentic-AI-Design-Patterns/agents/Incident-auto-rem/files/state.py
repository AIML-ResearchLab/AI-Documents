"""
State definitions — shared across all LangGraph nodes.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from typing      import Any, Optional, TypedDict


# ── Domain objects ────────────────────────────────────────────────────────────

@dataclass
class IncidentEvent:
    incident_id  : str
    title        : str
    severity     : str          # P1 / P2 / P3 / P4
    source       : str          # prometheus / pagerduty / cloudwatch / datadog
    affected_svc : str
    namespace    : str
    raw_alert    : dict         # original alert payload


@dataclass
class DiagnosisReport:
    symptoms         : list[str]
    metric_snapshot  : dict[str, Any]
    log_excerpt      : str
    hypothesis_tree  : list[dict]   # ToT branches explored
    best_hypothesis  : str
    confidence       : float        # 0-1


@dataclass
class RCAResult:
    root_cause       : str
    causal_chain     : list[str]    # trigger → contributing factors → root cause
    confidence       : float
    similar_incidents: list[dict]   # from vector DB
    matched_runbooks : list[str]


@dataclass
class RemediationStep:
    step_id    : str
    description: str
    command    : str            # actual command / API call
    tool       : str            # kubectl / ansible / aws-cli / terraform
    rollback   : str            # inverse command
    timeout_s  : int = 120


@dataclass
class RemediationPlan:
    plan_id     : str
    title       : str
    steps       : list[RemediationStep]
    risk_score  : float         # 0-10
    impact      : str
    duration_est: str
    rollback_plan: list[str]


@dataclass
class ExecutionResult:
    plan_id      : str
    steps_done   : list[dict]   # {step_id, status, output, duration_s}
    success      : bool
    rolled_back  : bool
    error        : Optional[str] = None


@dataclass
class HealthStatus:
    resolved          : bool
    metrics_recovered : dict[str, Any]
    checks_passed     : list[str]
    checks_failed     : list[str]
    slo_restored      : bool
    mttr_seconds      : int


@dataclass
class LessonsLearned:
    incident_id       : str
    root_cause        : str
    resolution        : str
    what_worked       : list[str]
    what_failed       : list[str]
    runbook_updates   : list[str]
    vector_db_entry   : dict        # stored in Chroma


# ── LangGraph State (TypedDict) ───────────────────────────────────────────────

class IncidentState(TypedDict):
    incident_event    : IncidentEvent
    diagnosis_report  : Optional[DiagnosisReport]
    rca_result        : Optional[RCAResult]
    remediation_plan  : Optional[RemediationPlan]
    validation_status : Optional[dict]      # {safe: bool, issues: list, risk: float}
    execution_result  : Optional[ExecutionResult]
    health_status     : Optional[HealthStatus]
    lessons_learned   : Optional[LessonsLearned]
    feedback_sent     : bool
    retry_count       : int
    replan_count      : int
    error_log         : list[str]
    audit_trail       : list[dict]
    human_approved    : bool
