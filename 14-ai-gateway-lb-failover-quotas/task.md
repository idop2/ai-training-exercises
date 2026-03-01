# The Gatekeeper: Building an AI Gateway

## 🧠 Theory: Production-Grade Reliability
In production, you can't just call the OpenAI API directly. You need reliability. An **AI Gateway** acts as a proxy, handling **Load Balancing** (distributing traffic across multiple keys/models), **Failover** (switching to a backup if the primary fails), and **Quotas** (rate limiting users). This ensures your app stays up even when one provider goes down or a user spams your endpoint.

## 🚀 The Assignment
You will build a simple **AI Gateway** server (using FastAPI or Flask) that acts as a middleware for LLM requests.

### Steps
1.  **The Proxy**: Create a `/v1/chat/completions` endpoint that accepts a standard OpenAI-compatible JSON payload.
2.  **Load Balancer**: Maintain a list of "providers" (mock endpoints or real keys). Implement a Round-Robin strategy to distribute requests evenly.
3.  **Failover Logic**: If a provider returns a 500 error or times out, catch the exception and automatically retry with the next available provider. Log the failure.
4.  **Rate Limiter**: Implement a token bucket algorithm to limit each user (identified by an API key header) to 10 requests per minute. Return a `429 Too Many Requests` if they exceed it.

## 🛠️ Tech Stack
- Python 3.10+
- `fastapi` or `flask` (for building the API)
- `httpx` or `requests` (for making upstream calls)
- `redis` (optional, for shared state/rate limiting)

## 📦 Deliverables
1.  `gateway.py`: Your FastAPI/Flask application.
2.  `test_gateway.py`: A script that fires 20 rapid requests to test the rate limiter and simulates a provider failure to test failover.
3.  `config.yaml`: A configuration file defining your providers and limits.

## 🌟 Bonus Challenges (Optional)
- **Cost Tracking**: Log the token usage and estimated cost for each request to a database.
- **Caching**: Implement a simple cache (using Redis) for identical requests to save money.
