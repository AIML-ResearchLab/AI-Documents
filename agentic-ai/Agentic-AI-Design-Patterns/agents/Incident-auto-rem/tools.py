"""
Shared tools for all agents.
In production these call real APIs; here they simulate with realistic outputs.
"""

import json
import random
import subprocess
from datetime import datetime
from langchain.tools import tool


# ── Monitoring / Observability tools ─────────────────────────────────────────

@tool
def fetch_pod_metrics(namespace: str, service: str) -> str:
    """Fetch CPU, memory, restart counts for pods in a namespace/service."""
    # Simulate Prometheus query result
    data = {
        "service"        : service,
        "namespace"      : namespace,
        "timestamp"      : datetime.utcnow().isoformat(),
        "cpu_usage_pct"  : 94.7,
        "memory_usage_mi": 510,
        "memory_limit_mi": 512,
        "restart_count"  : 7,
        "pod_status"     : "CrashLoopBackOff",
        "ready_replicas" : 0,
        "desired_replicas": 3,
    }
    return json.dumps(data, indent=2)


@tool
def fetch_application_logs(namespace: str, service: str, lines: int = 100) -> str:
    """Fetch recent application logs for a service."""
    logs = [
        "2024-03-15T10:23:41Z ERROR OutOfMemoryError: Java heap space",
        "2024-03-15T10:23:40Z WARN  Memory usage at 98%, GC overhead exceeded",
        "2024-03-15T10:23:38Z ERROR Connection pool exhausted: max=100 active=100",
        "2024-03-15T10:23:35Z INFO  Processing payment batch size=5000",
        "2024-03-15T10:23:30Z INFO  Received 2847 concurrent requests",
        "2024-03-15T10:20:00Z INFO  Deployment rollout started v2.4.1",
        "2024-03-15T10:19:50Z INFO  Config updated: payment.batch.size=5000 (was 500)",
    ]
    return "\n".join(logs[:lines])


@tool
def fetch_recent_deployments(namespace: str, service: str) -> str:
    """List recent deployments and config changes for a service."""
    data = {
        "recent_deployments": [
            {
                "version"   : "v2.4.1",
                "deployed_at": "2024-03-15T10:20:00Z",
                "deployed_by": "ci-pipeline",
                "changes"   : ["payment.batch.size: 500 → 5000", "heap.size: unchanged at 512Mi"],
            },
            {
                "version"   : "v2.4.0",
                "deployed_at": "2024-03-14T14:30:00Z",
                "deployed_by": "john.doe",
                "changes"   : ["Added async payment processor"],
            },
        ]
    }
    return json.dumps(data, indent=2)


@tool
def fetch_service_dependencies(service: str, namespace: str) -> str:
    """Get upstream and downstream service dependencies."""
    deps = {
        "upstream"  : ["api-gateway", "auth-service"],
        "downstream": ["postgres-primary", "redis-cache", "kafka-payments"],
        "external"  : ["stripe-api", "fraud-detection-svc"],
    }
    return json.dumps(deps, indent=2)


# ── Kubernetes tools ──────────────────────────────────────────────────────────

@tool
def kubectl_get_pods(namespace: str, service: str) -> str:
    """Get pod status for a service."""
    data = {
        "pods": [
            {"name": f"{service}-7d9f8b-xk2p9", "status": "OOMKilled",  "restarts": 7,  "age": "2m"},
            {"name": f"{service}-7d9f8b-mn3r1", "status": "OOMKilled",  "restarts": 5,  "age": "2m"},
            {"name": f"{service}-7d9f8b-pq7s4", "status": "Running",    "restarts": 3,  "age": "10m"},
        ]
    }
    return json.dumps(data, indent=2)


@tool
def kubectl_describe_pod(namespace: str, pod_name: str) -> str:
    """Describe a specific pod including events and resource usage."""
    return json.dumps({
        "pod"        : pod_name,
        "namespace"  : namespace,
        "last_state" : {"terminated": {"reason": "OOMKilled", "exit_code": 137}},
        "limits"     : {"memory": "512Mi", "cpu": "500m"},
        "requests"   : {"memory": "256Mi", "cpu": "250m"},
        "events"     : [
            "BackOff: Back-off restarting failed container",
            "OOMKilling: Memory cgroup out of memory: Kill process",
        ],
    }, indent=2)


@tool
def kubectl_scale_deployment(namespace: str, deployment: str, replicas: int) -> str:
    """Scale a Kubernetes deployment to specified replica count."""
    # In prod: subprocess.run(["kubectl", "scale", ...])
    return json.dumps({
        "action"    : "scale",
        "deployment": deployment,
        "namespace" : namespace,
        "replicas"  : replicas,
        "status"    : "success",
        "message"   : f"Deployment {deployment} scaled to {replicas} replicas",
    })


@tool
def kubectl_patch_resource_limits(namespace: str, deployment: str,
                                   memory_limit: str, cpu_limit: str) -> str:
    """Patch memory and CPU limits on a deployment."""
    return json.dumps({
        "action"      : "patch_limits",
        "deployment"  : deployment,
        "new_limits"  : {"memory": memory_limit, "cpu": cpu_limit},
        "status"      : "success",
        "message"     : f"Resource limits updated: memory={memory_limit}, cpu={cpu_limit}",
    })


@tool
def kubectl_rollout_restart(namespace: str, deployment: str) -> str:
    """Perform a rolling restart of a deployment."""
    return json.dumps({
        "action"    : "rollout_restart",
        "deployment": deployment,
        "namespace" : namespace,
        "status"    : "success",
        "message"   : "Rolling restart initiated, pods cycling...",
    })


@tool
def kubectl_rollback_deployment(namespace: str, deployment: str, revision: int = 0) -> str:
    """Rollback a deployment to previous revision."""
    return json.dumps({
        "action"    : "rollback",
        "deployment": deployment,
        "revision"  : revision if revision else "previous",
        "status"    : "success",
        "message"   : f"Deployment rolled back to revision {revision or 'previous'}",
    })


# ── Config / Application tools ────────────────────────────────────────────────

@tool
def update_config_map(namespace: str, configmap: str, key: str, value: str) -> str:
    """Update a Kubernetes ConfigMap key."""
    return json.dumps({
        "action"   : "update_configmap",
        "configmap": configmap,
        "key"      : key,
        "new_value": value,
        "status"   : "success",
    })


@tool
def run_health_check(namespace: str, service: str) -> str:
    """Run synthetic health check against a service endpoint."""
    # Simulate partial recovery after remediation
    recovered = random.random() > 0.3   # 70% chance of recovery in simulation
    return json.dumps({
        "service"        : service,
        "namespace"      : namespace,
        "http_status"    : 200 if recovered else 503,
        "response_time_ms": 145 if recovered else 9999,
        "pod_ready_count": 3 if recovered else 0,
        "error_rate_pct" : 0.1 if recovered else 47.3,
        "cpu_usage_pct"  : 42.0 if recovered else 94.7,
        "memory_usage_pct": 68.0 if recovered else 99.6,
        "recovered"      : recovered,
    })


# ── Notification tools ────────────────────────────────────────────────────────

@tool
def send_slack_notification(channel: str, message: str) -> str:
    """Send a Slack notification to a channel."""
    # In prod: requests.post(SLACK_WEBHOOK_URL, json={"text": message})
    print(f"\n  📣 [SLACK → #{channel}]\n  {message[:200]}\n")
    return json.dumps({"status": "sent", "channel": channel})


@tool
def create_jira_ticket(summary: str, description: str, issue_type: str = "Post-Mortem") -> str:
    """Create a JIRA ticket for post-mortem or follow-up."""
    ticket_id = f"OPS-{random.randint(1000,9999)}"
    print(f"\n  🎫 [JIRA] Created {ticket_id}: {summary}\n")
    return json.dumps({"ticket_id": ticket_id, "status": "created", "summary": summary})


@tool
def resolve_pagerduty_incident(incident_id: str, resolution_note: str) -> str:
    """Mark a PagerDuty incident as resolved."""
    return json.dumps({
        "incident_id"     : incident_id,
        "status"          : "resolved",
        "resolution_note" : resolution_note,
    })


# ── Vector DB / Memory tools ──────────────────────────────────────────────────

@tool
def search_similar_incidents(query: str, top_k: int = 3) -> str:
    """Search vector DB for similar past incidents and their resolutions."""
    # Simulate Chroma / FAISS retrieval
    incidents = [
        {
            "id"        : "INC-20240201-044",
            "title"     : "payments-service OOMKilled after batch size increase",
            "root_cause": "JVM heap exhausted due to large batch processing",
            "resolution": "Increased memory limit to 1Gi, reduced batch size to 1000",
            "similarity": 0.94,
        },
        {
            "id"        : "INC-20231115-089",
            "title"     : "checkout-service crash loop after config change",
            "root_cause": "Connection pool exhausted under high concurrency",
            "resolution": "Rolled back config, increased connection pool size",
            "similarity": 0.81,
        },
    ]
    return json.dumps(incidents, indent=2)


@tool
def store_incident_lesson(incident_id: str, lesson: dict) -> str:
    """Store an incident lesson in the vector DB for future retrieval."""
    # In prod: chroma_client.add_documents(...)
    return json.dumps({
        "status"     : "stored",
        "incident_id": incident_id,
        "vector_id"  : f"vec_{incident_id}",
    })


@tool
def fetch_runbook(service: str, symptom: str) -> str:
    """Fetch the most relevant runbook for a service and symptom."""
    runbook = {
        "runbook_id" : "RB-PAYMENTS-OOM-001",
        "title"      : "payments-service OOMKilled Remediation",
        "steps"      : [
            "1. Check current memory limits: kubectl describe pod",
            "2. Increase memory limit to 2x current: kubectl patch",
            "3. Reduce payment.batch.size to 1000 in ConfigMap",
            "4. Rolling restart to apply changes",
            "5. Monitor for 5 min — verify pod restarts stop",
        ],
        "owner"     : "payments-team",
        "last_updated": "2024-02-01",
    }
    return json.dumps(runbook, indent=2)


# ── All tools grouped by agent ────────────────────────────────────────────────

TRIGGER_TOOLS      = []   # trigger agent uses no tools (receives event)

DIAGNOSIS_TOOLS    = [
    fetch_pod_metrics,
    fetch_application_logs,
    fetch_recent_deployments,
    fetch_service_dependencies,
    kubectl_get_pods,
    kubectl_describe_pod,
]

RCA_TOOLS          = [
    search_similar_incidents,
    fetch_runbook,
    fetch_service_dependencies,
]

PLANNING_TOOLS     = [
    fetch_runbook,
    search_similar_incidents,
]

PRE_VALIDATE_TOOLS = [
    fetch_service_dependencies,
    kubectl_get_pods,
]

EXECUTION_TOOLS    = [
    kubectl_scale_deployment,
    kubectl_patch_resource_limits,
    kubectl_rollout_restart,
    kubectl_rollback_deployment,
    update_config_map,
    run_health_check,
]

POST_VALIDATE_TOOLS = [
    run_health_check,
    fetch_pod_metrics,
    fetch_application_logs,
]

LEARNING_TOOLS     = [
    store_incident_lesson,
    fetch_runbook,
]

FEEDBACK_TOOLS     = [
    send_slack_notification,
    create_jira_ticket,
    resolve_pagerduty_incident,
]
