from sqlalchemy.orm import Session
from app.models.api_log import APILog

def calculate_health(api_id: int, db: Session):
    logs = (
        db.query(APILog)
        .filter(APILog.api_id == api_id)
        .order_by(APILog.checked_at.desc())
        .limit(50)
        .all()
    )

    if not logs:
        return {"health_score": 0, "status": "NO_DATA"}

    total = len(logs)
    success_count = sum(1 for log in logs if log.is_success)
    success_rate = (success_count / total) * 100

    avg_response_time = sum(log.response_time for log in logs) / total

    latency_score = max(0, 100 - (avg_response_time * 50))
    health_score = (0.7 * success_rate) + (0.3 * latency_score)

    last_10 = logs[:10]
    last_20 = logs[:20]

    recent_failures = sum(1 for log in last_10 if not log.is_success)
    intermittent_failures = sum(1 for log in last_20 if not log.is_success)

    first_half = logs[25:]
    second_half = logs[:25]

    avg_old_latency = (
        sum(log.response_time for log in first_half) / len(first_half)
        if first_half else avg_response_time
    )

    avg_new_latency = (
        sum(log.response_time for log in second_half) / len(second_half)
        if second_half else avg_response_time
    )

    status = "HEALTHY"
    issue = None

    if recent_failures >= 8:
        status = "DOWN"
        issue = "Most recent requests are failing"

    elif intermittent_failures >= 5:
        status = "FLAKY"
        issue = "Intermittent failures detected"

    elif avg_new_latency > avg_old_latency * 1.5:
        status = "DEGRADED"
        issue = "Response time increasing over time"

    elif health_score < 60:
        status = "UNSTABLE"
        issue = "Low overall health score"

    return {
        "health_score": round(health_score, 2),
        "status": status,
        "issue": issue,
        "success_rate": round(success_rate, 2),
        "avg_response_time": round(avg_response_time, 3)
    }