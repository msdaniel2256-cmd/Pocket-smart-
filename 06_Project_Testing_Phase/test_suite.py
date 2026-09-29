"""Automated Integration & Regression Test Suite for PocketSmart AI."""

import sys
import json
import time
from pathlib import Path
import requests

BASE_URL = "http://127.0.0.1:8000"

def run_test_suite():
    print("=" * 70)
    print("PocketSmart AI: Comprehensive Automated Test Suite")
    print(f"Target Server: {BASE_URL}")
    print("=" * 70)
    
    session = requests.Session()
    results = []

    def log_result(tc_id, description, passed, details=""):
        status_str = "PASS" if passed else "FAIL"
        print(f"[{status_str}] {tc_id}: {description} | {details}")
        results.append({
            "test_id": tc_id,
            "description": description,
            "status": status_str,
            "details": details
        })

    # Test 1: Landing Page
    try:
        r = session.get(f"{BASE_URL}/")
        passed = (r.status_code == 200 and "PocketSmart" in r.text)
        log_result("TC-01", "GET Landing Page", passed, f"Status: {r.status_code}")
    except Exception as e:
        log_result("TC-01", "GET Landing Page", False, str(e))

    # Test 2: Login Page
    try:
        r = session.get(f"{BASE_URL}/login")
        passed = (r.status_code == 200 and "login" in r.text.lower())
        log_result("TC-02", "GET Login Page", passed, f"Status: {r.status_code}")
    except Exception as e:
        log_result("TC-02", "GET Login Page", False, str(e))

    # Test 3: OAuth2 Authentication (Positive)
    token = None
    try:
        r = session.post(f"{BASE_URL}/token", data={"username": "sai", "password": "password123"})
        passed = (r.status_code == 200 and "access_token" in r.json())
        if passed:
            token = r.json()["access_token"]
        log_result("TC-03", "POST /token Valid Credentials", passed, f"Status: {r.status_code}")
    except Exception as e:
        log_result("TC-03", "POST /token Valid Credentials", False, str(e))

    # Test 4: OAuth2 Authentication (Negative / Invalid Password)
    try:
        r = session.post(f"{BASE_URL}/token", data={"username": "sai", "password": "wrongpassword!"})
        passed = (r.status_code == 401)
        log_result("TC-04", "POST /token Invalid Password Barrier", passed, f"Status: {r.status_code} (Expected 401)")
    except Exception as e:
        log_result("TC-04", "POST /token Invalid Password Barrier", False, str(e))

    headers = {"Authorization": f"Bearer {token}"} if token else {}

    # Test 5: Unauthenticated Access Barrier
    try:
        unauth_session = requests.Session()
        r = unauth_session.get(f"{BASE_URL}/dashboard", allow_redirects=False)
        passed = (r.status_code in [302, 307] or r.status_code == 401)
        log_result("TC-05", "GET /dashboard Unauthorized Redirect Barrier", passed, f"Status: {r.status_code}")
    except Exception as e:
        log_result("TC-05", "GET /dashboard Unauthorized Redirect Barrier", False, str(e))

    # Test 6: Authenticated Dashboard Access
    try:
        r = session.get(f"{BASE_URL}/dashboard", headers=headers)
        passed = (r.status_code == 200 and "Dashboard" in r.text)
        log_result("TC-06", "GET /dashboard Authenticated User", passed, f"Status: {r.status_code}")
    except Exception as e:
        log_result("TC-06", "GET /dashboard Authenticated User", False, str(e))

    # Test 7: Session Info API
    try:
        r = session.get(f"{BASE_URL}/session-info", headers=headers)
        passed = (r.status_code == 200 and r.json().get("username") == "sai")
        log_result("TC-07", "GET /session-info Active Session Metadata", passed, f"User: {r.json().get('username')}")
    except Exception as e:
        log_result("TC-07", "GET /session-info Active Session Metadata", False, str(e))

    # Test 8: Home Budget Calculation
    try:
        payload = {
            "total_budget": 20000.0,
            "num_lights": 4,
            "num_fans": 2,
            "num_furniture": 1,
            "num_dining_tables": 0,
            "has_living_room": True,
            "has_kitchen": True,
            "has_bedroom": False
        }
        r = session.post(f"{BASE_URL}/home-budget", json=payload, headers=headers)
        data = r.json()
        categories = data.get("budget_breakdown", [])
        passed = (r.status_code == 200 and len(categories) > 0 and data.get("total_budget") == 20000.0)
        log_result("TC-08", "POST /home-budget Allocation & Sourcing Links", passed, f"Categories: {len(categories)}")
    except Exception as e:
        log_result("TC-08", "POST /home-budget Allocation & Sourcing Links", False, str(e))

    # Test 9: Party Budget Calculation
    try:
        payload = {
            "total_budget": 35000.0,
            "num_guests": 25,
            "party_type": "Birthday Celebration",
            "venue_type": "Cafe / Lounge",
            "needs_catering": True,
            "needs_decoration": True,
            "needs_entertainment": True
        }
        r = session.post(f"{BASE_URL}/party-budget", json=payload, headers=headers)
        data = r.json()
        passed = (r.status_code == 200 and "budget_breakdown" in data and len(data.get("venue_suggestions", [])) > 0)
        log_result("TC-09", "POST /party-budget Venue & Buffer Allocation", passed, f"Status: {r.status_code}")
    except Exception as e:
        log_result("TC-09", "POST /party-budget Venue & Buffer Allocation", False, str(e))

    # Test 10: Jewelry Recommendation
    try:
        data_form = {
            "total_budget": 15000.0,
            "occasion": "Festive Diwali Celebration",
            "preferences": "Traditional gold and pearl"
        }
        r = session.post(f"{BASE_URL}/jewelry-budget", data=data_form, headers=headers)
        data = r.json()
        items = data.get("jewelry_recommendations", [])
        passed = (r.status_code == 200 and len(items) > 0)
        log_result("TC-10", "POST /jewelry-budget Occasion Jewelry Matching", passed, f"Items Recommended: {len(items)}")
    except Exception as e:
        log_result("TC-10", "POST /jewelry-budget Occasion Jewelry Matching", False, str(e))

    # Test 11: Recommendation History Listing
    sample_id = None
    try:
        r = session.get(f"{BASE_URL}/recommendation-history", headers=headers)
        history = r.json().get("history", [])
        passed = (r.status_code == 200 and len(history) > 0)
        if len(history) > 0:
            sample_id = history[0]["id"]
        log_result("TC-11", "GET /recommendation-history Audit Trail", passed, f"History Items: {len(history)}")
    except Exception as e:
        log_result("TC-11", "GET /recommendation-history Audit Trail", False, str(e))

    # Test 12: Recommendation Details by ID
    try:
        if sample_id:
            r = session.get(f"{BASE_URL}/recommendation-details/{sample_id}", headers=headers)
            passed = (r.status_code == 200 and r.json().get("id") == sample_id)
            log_result("TC-12", f"GET /recommendation-details/{sample_id}", passed, "Details retrieved successfully")
        else:
            log_result("TC-12", "GET /recommendation-details", False, "No history ID available")
    except Exception as e:
        log_result("TC-12", "GET /recommendation-details", False, str(e))

    print("=" * 70)
    passed_count = sum(1 for r in results if r["status"] == "PASS")
    total_count = len(results)
    pass_pct = (passed_count / total_count) * 100
    print(f"SUMMARY: {passed_count}/{total_count} Tests Passed ({pass_pct:.1f}%)")
    print("=" * 70)

    return results

if __name__ == "__main__":
    run_test_suite()
