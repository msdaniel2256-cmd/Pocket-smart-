# Test Cases Specification

| Test ID | Module | Test Scenario | Input Data | Expected Result | Priority |
|---|---|---|---|---|---|
| **TC-01** | Web UI | Landing page accessibility | `GET /` | Status 200; HTML contains branding and planner links | High |
| **TC-02** | Web UI | Login page rendering | `GET /login` | Status 200; Login form rendered with username & password fields | High |
| **TC-03** | Security | OAuth2 token authentication (Positive) | `POST /token` with `sai` / `password123` | Status 200; JSON response contains `access_token` and `token_type: bearer` | Critical |
| **TC-04** | Security | Invalid credential barrier (Negative) | `POST /token` with `sai` / `wrongpwd` | Status 401 Unauthorized; Error detail returned | Critical |
| **TC-05** | Security | Protected route security barrier | `GET /dashboard` without cookie/header | Status 401 or redirect to `/login` | Critical |
| **TC-06** | Dashboard | Authenticated dashboard access | `GET /dashboard` with Bearer token | Status 200; Rendered dashboard with user greeting | High |
| **TC-07** | Session | Active session metadata | `GET /session-info` with Bearer token | Status 200; JSON with username `sai`, login timestamp, duration | Medium |
| **TC-08** | Home Planner | Home interior budget allocation | `POST /home-budget` (Budget: 20000, 4 lights, 2 fans, 1 furniture) | Status 200; Breakdown categories sum <= 20000; Indian shopping links attached | Critical |
| **TC-09** | Party Planner | Party budget & venue suggestions | `POST /party-budget` (Budget: 35000, 25 guests, Birthday) | Status 200; 4+ categories; venue suggestions present; safety buffer calculated | Critical |
| **TC-10** | Jewelry Planner | Occasion jewelry recommendation | `POST /jewelry-budget` (Budget: 15000, Festive Diwali) | Status 200; >= 3 jewelry items; styling tips; Tanishq/CaratLane links | Critical |
| **TC-11** | History | Recommendation history listing | `GET /recommendation-history` | Status 200; JSON array containing user's saved recommendations | High |
| **TC-12** | History | Recommendation details by ID | `GET /recommendation-details/{id}` | Status 200; Full nested breakdown JSON matching ID | High |
| **TC-13** | Security | User logout and token revocation | `GET /logout` | Status 302 to `/login`; access token cookie cleared and blacklisted | High |
| **TC-14** | Registration | New user registration flow | `POST /register` with new unique user | Status 302 to `/dashboard`; session cookie set; user written to DB | High |
| **TC-15** | Background | Session garbage collection | Automated background worker | Inactive sessions > 30 minutes purged from memory | Medium |
